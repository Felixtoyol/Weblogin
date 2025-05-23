# WebDAV Uploader v3.0

> **For Authorized Penetration Testing and Educational Use Only**

A sleek and powerful CLI utility designed to assess and exploit WebDAV PUT upload vulnerabilities with intelligent filename bypass techniques.

---

## Features

**Auto-Bypass Payloads:** Generate and attempt multiple filename variants to circumvent server-side filters.
**Single & Batch Modes:** Target individual URLs or process multiple endpoints from a list.
**Verification & Logging:** Automatically verify successful uploads and record accessible URLs in `found_vuln.txt`.
**Extensible & Lightweight:** Minimal dependencies for fast setup.


## Prerequisites

**Python 3.6+**
**pip** (Python package installer)


## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/dxister-webdav-uploader.git
   cd dxister-webdav-uploader
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 📋 Usage

Run the tool with Python:

```bash
python dxister_webdav.py
```

Follow the on-screen menu:

1. **Single Target Upload**

   * Input the target URL (e.g., `http://example.com`).
   * Specify your defacement file (e.g., `deface.html`).
   * Optionally enable auto-bypass for multiple filename variants.

2. **Batch Mode**

   * Provide a `targets.txt` file containing one URL per line.
   * Specify the defacement file to use.

3. **Exit**

Successful uploads are verified


## 📁 Project Structure

```plaintext
.
├── dxister_webdav.py        # Main script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── targets.txt              # Example target list
└── deface.html              # Example defacement file
```

## ⚠️ Legal Disclaimer

This tool is provided **"as is"** for **authorized security assessments** and **educational purposes** only. Unauthorized use against systems without explicit permission is strictly prohibited and may be illegal.


## 📜 License

Distributed under the [MIT License](LICENSE).
