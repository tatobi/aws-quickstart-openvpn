#!/usr/bin/env python3

import csv
import time
import subprocess

from flask import Flask, render_template, send_file, abort, request, Markup

#CONFIG
AUTH_TOKEN={"key":"Vpnmanagertoken","value":"randomnumber"}
CHECK_HEADER_TOKEN=False
CHECK_HEADER_AUTH=False
APP_ROOT=""
HOST='127.0.0.1'
PORT=5000
TRUSTED_PROXIES = ('127.0.0.1')
TRUSTED_HOSTS = ('127.0.0.1')
KEYGEN_BASE="/etc/openvpn/keygen"
KEYS_BASE="/etc/openvpn/keys"
CA_INDEX_DB=KEYS_BASE+"/index.txt"
SITE="example-com-vpn"
CSS_FILE="bulma.min.css"
CSS_LOGO="openvpn-logo.png"
FAVICON="favicon.ico"
ZIP_ENABLED=False


"""
OpenSSL Index file 
The index file consists of zero or more lines, each containing the following fields separated by tab characters:

#0 1. Certificate status flag (V=valid, R=revoked, E=expired).
#1 2. Certificate expiration date in YYMMDDHHMMSSZ format.
#2 3. Certificate revocation date in YYMMDDHHMMSSZ[,reason] format. Empty if not revoked.
#3 4. Certificate serial number in hex.
#4 5. Certificate filename or literal string ‘unknown’.
#5 6. Certificate distinguished name.
"""

app = Flask(__name__)

# ['V', '340414203029Z', '', '01', 'unknown', '/C=GB/ST=London/L=London/O=Example OU/OU=IT/CN=jira.example.com/emailAddress=it-support@example.com']

#open index file
def read_index():
    CA_DB=[]
    CA_DB_SERIAL_DICT={}
    CA_DB_NAME_DICT={}
    with open(CA_INDEX_DB, "r", newline='') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for num, row in enumerate(reader):
            if num == 0 or "site-2-site" in row:
                #skip server self cert and s2s certs
                continue
            serial=row[3]
            out=[]
            elem=""
            for elnum, elem in enumerate(row):
                if elnum == 1 or elnum == 2:
                    if elem:
                        elem=elem[2:4]+"/"+elem[4:6]+"/20"+elem[:2]+" "+elem[6:8]+":"+elem[8:10]+":"+elem[10:12]
                    else:
                        elem = ""
                if elnum == 5:
                    elem=elem.split("CN=")[1].split("/")[0]
                out.append(elem)
            CA_DB.append(out)
            CA_DB_SERIAL_DICT[serial]=out
            CA_DB_NAME_DICT[elem]=out
            CA_DB=[]
            for k in sorted(CA_DB_NAME_DICT):
                CA_DB.append(CA_DB_NAME_DICT[k])
    return (CA_DB_SERIAL_DICT, CA_DB)

def protect_invalid_chars(txt=""):
    invalid_chars=["<",">",'"',"'","`","(",")","[","]","{","}","&","$","^","~","ˇ","˘",'˝',";",":","/","=","!","%","\\","|","€"," ","*"]
    return "".join([char for char in txt if char not in invalid_chars])

def processExecutor(cmd, args=''):
    try:
        ps= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ps.stdout.read()
        err = ps.stderr.read()
        ps.stdout.close()
        ps.stderr.close()
        ps.wait()
        return str(err.decode("utf-8"))+str(output.decode("utf-8"))
    except Exception as e:
        print(e)
        return None

@app.route(APP_ROOT+"/")
def list():
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    return render_template('template.html', title="List of All OpenVPN certificates", all_tab_active="is-active", site=SITE, my_list=CA_DB, app_route=APP_ROOT)

@app.route(APP_ROOT+"/list-valid")
def list_valid():
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    CA_DB=[j for j in CA_DB if 'V' in j[0]]
    return render_template('template.html', title="List of Valid OpenVPN certificates", valid_tab_active="is-active", site=SITE, my_list=CA_DB, app_route=APP_ROOT)

@app.route(APP_ROOT+"/list-revoke")
def list_revoke():
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    CA_DB=[j for j in CA_DB if 'R' in j[0]]
    return render_template('template.html', title="List of Revoked OpenVPN certificates", revoke_tab_active="is-active", site=SITE, my_list=CA_DB, app_route=APP_ROOT)

@app.route(APP_ROOT+'/download/<serial>', methods=['GET', 'POST'])
def download(serial):
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    serial=protect_invalid_chars(serial)
    if serial in CA_DB_SERIAL_DICT:
        if CA_DB_SERIAL_DICT[serial][0] == 'V':
            cert_name=CA_DB_SERIAL_DICT[serial][5]
            if ZIP_ENABLED:
                file_name=KEYS_BASE+"/"+cert_name+"/"+cert_name+".zip"
            else:
                file_name=KEYS_BASE+"/"+cert_name+"/"+cert_name+".ovpn"
            return send_file(file_name, as_attachment=True)
        else:
            abort(404)  # 404 Not Found
    
@app.route(APP_ROOT+'/revoke/<serial>', methods=['GET'])
def revoke(serial):
    serial=protect_invalid_chars(serial)
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    message="Confirm revoke certificate"
    if serial in CA_DB_SERIAL_DICT:
        if CA_DB_SERIAL_DICT[serial][0] == 'V':
            cert_to_revoke=CA_DB_SERIAL_DICT[serial][5]
        else:
            abort(404)  # 404 Not Found
    return render_template('revoke.html', title=message, serial=serial, cert_name=cert_to_revoke,app_route=APP_ROOT, site=SITE)

@app.route(APP_ROOT+'/revoke_certificate/<serial>', methods=['POST'])
def revoke_certificate(serial):
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    message="Certificate revoked"
    certname=""
    serial=protect_invalid_chars(serial)
    if serial in CA_DB_SERIAL_DICT:
        if CA_DB_SERIAL_DICT[serial][0] == 'V':
            certname=CA_DB_SERIAL_DICT[serial][5]
        else:
            abort(404)  # 404 Not Found
    if certname:
        cmd="cd "+KEYGEN_BASE+" && ./revoke-client "+certname
    
        #execute create command
        out=""
        done=""
        lines = processExecutor(cmd).split("\n")
        print(lines)
        for line in lines:
            out+=str(line)+"<br />"
        #out=out.replace("b'","").replace("'","").replace('"',"")
        if "DONE." in out and "certificate revoked" in out:
            done="done"
        out=Markup(out)
        CA_DB_SERIAL_DICT, CA_DB = read_index()
        return render_template('revoke.html', title=message, serial=serial, cert_name=certname, done=done, out=out, app_route=APP_ROOT)
    else:
        return render_template('revoke.html', title="Certificate revocation error.", serial=serial, cert_name="Missing cert name", app_route=APP_ROOT, site=SITE)
    
@app.route(APP_ROOT+"/create")
def create():
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    return render_template('create.html', title="Create NEW OpenVPN certificate", selected_tcp="selected",app_route=APP_ROOT, site=SITE)

@app.route(APP_ROOT+"/create-form", methods=['POST'])
def create_form():
    CA_DB_SERIAL_DICT, CA_DB = read_index()
    error_msg=""
    selected_internal="selected"
    title="Creating new certificate ..."
    error=""
    done=""
    cmd=""
    certname=""
    download_serial="0"
    new_cert = protect_invalid_chars(request.form["cert_name"])
    cert_type = protect_invalid_chars(request.form["select_gw"])
    if not len(new_cert):
        error_msg="Certificate name cannot be empty!"
        error=" ERROR."
    
    #disable s2s
    if "site-2-site" in new_cert:
        error_msg="Do not generate / manage S2S via WEB interface!"
        title+=" ERROR."
    
    if cert_type == "gw":
        selected_gw="selected"
        selected_tcp=""
        selected_internal=""
        certname=new_cert+"-"+SITE+"-tcp-gw"
        cmd="cd "+KEYGEN_BASE+" && ./build-key-embed-tcp-commongw "+certname
    elif cert_type == "tcp":
        selected_gw=""
        selected_tcp="selected"
        selected_internal=""
        certname=new_cert+"-"+SITE+"-tcp"
        cmd="cd "+KEYGEN_BASE+" && ./build-key-embed-tcp "+certname
    else:
        selected_gw=""
        selected_tcp=""
        selected_internal="selected"
        certname=new_cert+"-"+SITE
        cmd="cd "+KEYGEN_BASE+" && ./build-key-embed "+certname
    
    #check exiting certificate
    if not error_msg:
        for v in CA_DB:
            if new_cert == v[5]:
                error_msg="Already existing certificate name in cert database!"
                error=" ERROR."
                break

    #execute create command
    out=""
    if not error_msg:
        lines = processExecutor(cmd).split("\n")
        print(lines)
        for line in lines:
            out+=str(line)+"<br />"
        #out=out.replace("b'","").replace("'","").replace('"',"")
        if "DONE." in out:
            done="done"
        out=Markup(out)
        CA_DB_SERIAL_DICT, CA_DB = read_index()
        for k,v in CA_DB_SERIAL_DICT.items():
            if v[5] == certname:
                download_serial=k
                break
    return render_template('create.html', title=title, error=error, error_message=error_msg, read_only="readonly", selected_internal=selected_internal, selected_gw=selected_gw, cert_name_val=certname,out=out,done=done,serial=download_serial,selected_tcp=selected_tcp,app_route=APP_ROOT, site=SITE)
    
@app.route(APP_ROOT+"/css")
def css():
    return send_file(CSS_FILE, as_attachment=True)
    
@app.route(APP_ROOT+"/logo")
def logo():
    return send_file(CSS_LOGO, as_attachment=True)

@app.route(APP_ROOT+"/favicon.ico")
def favicon():
    return send_file(FAVICON, as_attachment=True)

@app.before_request
def limit_remote_addr():
    route = request.access_route + [request.remote_addr]
    #print("Route:",route)
    #remote_addr = next((addr for addr in reversed(route) if addr not in TRUSTED_PROXIES), request.remote_addr)
    #print("Remote Addr:",remote_addr)
    print("Remote Addr:",request.remote_addr)
    auth_header=request.headers.get('Authorization')
    token_header=request.headers.get(AUTH_TOKEN["key"])
    if request.remote_addr not in TRUSTED_HOSTS:
        print("Untrused remote address, 403:",request.remote_addr)
        abort(403)  # Forbidden
    if CHECK_HEADER_TOKEN and (not auth_header):
        print("No authorization header, 403:",request.remote_addr)
        abort(403)  # Forbidden
    if CHECK_HEADER_AUTH and (token_header != AUTH_TOKEN["value"]):
        print("Authorization token mismatch, 403:",request.remote_addr)
        abort(403)  # Forbidden

if __name__ == '__main__':
    try:
        app.run(host=HOST, port=PORT, debug=True)
    except OSError:
        print("Process already running. Exit.")
