import os
import hashlib
import json
import time
import argparse
from tqdm import tqdm

# Path to store the hash records
HASH_RECORD_FILE = "hashes.json"
IGNORED_DIRS = {'.git', 'node_modules', '__pycache__', 'venv'}
MAX_FILE_SIZE_MB = 50  # skip files bigger than this (optional)


def compute_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"⚠️ Could not read {file_path}: {e}")
        return None


def scan_directory(directory):
    hash_data = {}
    all_files = []

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            full_path = os.path.abspath(os.path.join(root, file))
            if os.path.getsize(full_path) > MAX_FILE_SIZE_MB * 1024 * 1024:
                continue
            all_files.append(full_path)

    print(f"\n🔎 Scanning {len(all_files)} files...")
    for file_path in tqdm(all_files, desc="🧠 Hashing", unit="file"):
        rel_path = os.path.relpath(file_path, directory)
        file_hash = compute_hash(file_path)
        if file_hash:
            hash_data[rel_path] = file_hash

    return hash_data


def save_hashes(hash_data):
    data_to_save = {
        "timestamp": time.time(),
        "hashes": hash_data
    }
    with open(HASH_RECORD_FILE, "w") as f:
        json.dump(data_to_save, f, indent=4)


def load_hashes():
    if not os.path.exists(HASH_RECORD_FILE):
        return {}
    with open(HASH_RECORD_FILE, "r") as f:
        return json.load(f).get("hashes", {})


def compare_hashes(old_hashes, new_hashes):
    modified = []
    added = []
    deleted = []

    for path in old_hashes:
        if path not in new_hashes:
            deleted.append(path)
        elif old_hashes[path] != new_hashes[path]:
            modified.append(path)

    for path in new_hashes:
        if path not in old_hashes:
            added.append(path)

    return modified, added, deleted


def pretty_print_report(modified, added, deleted):
    print("\n📋 \033[1mReport:\033[0m")
    if modified:
        print("\n🔄 Modified files:")
        for f in modified:
            print(f"  - {f}")
    if added:
        print("\n➕ New files added:")
        for f in added:
            print(f"  - {f}")
    if deleted:
        print("\n❌ Deleted files:")
        for f in deleted:
            print(f"  - {f}")
    if not (modified or added or deleted):
        print("\n✅ No changes detected.")


def main():
    parser = argparse.ArgumentParser(description="🔐 File Integrity Checker")
    parser.add_argument("--path", help="Directory path to monitor", required=True)
    parser.add_argument("--update", action="store_true", help="Update hash record after checking")
    args = parser.parse_args()

    directory = args.path
    print("""
==========================================
📂 FILE INTEGRITY CHECKER v2
==========================================
    """)

    if not os.path.isdir(directory):
        print("❌ Invalid directory.")
        return

    new_hashes = scan_directory(directory)

    if not os.path.exists(HASH_RECORD_FILE):
        print("\n🔐 First-time setup: saving current file hashes...")
        save_hashes(new_hashes)
        print("✅ Hashes saved.")
    else:
        print("\n🔍 Comparing with saved hash record...")
        old_hashes = load_hashes()
        modified, added, deleted = compare_hashes(old_hashes, new_hashes)
        pretty_print_report(modified, added, deleted)

        if args.update:
            save_hashes(new_hashes)
            print("\n✔ Hash record updated.")
        else:
            print("\n📌 Tip: Run with --update to refresh the saved hashes.")


if __name__ == "__main__":
    main()