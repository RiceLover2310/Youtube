from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
log_file = "ip_logs.txt"

target_url = "www.youtube.com"  # Change this to the URL you want to redirect users to

@app.route("/<path:any_path>")
def redirect_and_log(any_path):
    with open(log_file, "a") as f:
        f.write(f"{request.remote_addr} - {any_path}\n")
    return redirect(url_for("target", path=any_path))

@app.route("/target/<path:path>")
def target(path):
    return redirect(target_url + path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)