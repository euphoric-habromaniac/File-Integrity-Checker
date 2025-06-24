import os
import subprocess
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_dependencies():
    print("\n📦 Installing required libraries...\n")
    requirements = [
        "requests", "beautifulsoup4", "tqdm", "cryptography"
    ]
    for lib in requirements:
        print(f"🔧 Installing {lib}...")
        subprocess.call([sys.executable, "-m", "pip", "install", lib])
    print("\n✅ All libraries installed successfully!\n")
    input("🔁 Press Enter to return to main menu...")

def run_task(task_number):
    paths = {
        '1': os.path.join("First Task", "first_task.py"),
        '2': os.path.join("Second Task", "second_task.py"),
        '3': os.path.join("Third Task", "third_task.py"),
        '4': os.path.join("Fourth Task", "fourth_task.py"),
    }
    script = paths.get(task_number)
    if not script:
        print("❌ Invalid task.")
        return
    print(f"\n🚀 Running Task {task_number}...\n")
    subprocess.call([sys.executable, script])
    input("\n🔁 Press Enter to return to task menu...")

def task_menu():
    while True:
        clear()
        print("="*60)
        print("📂 SELECT A TASK TO RUN")
        print("="*60)
        print("1. 🧮 First Task – File Integrity Checker")
        print("2. 🛡️  Second Task – Web Vulnerability Scanner")
        print("3. 🧰 Third Task – Pentesting Toolkit")
        print("4. 🔐 Fourth Task – AES Encryption Tool")
        print("0. 🔙 Go Back")
        print("="*60)
        choice = input("📥 Enter your choice: ").strip()
        if choice == '0':
            break
        run_task(choice)

def main_menu():
    while True:
        clear()
        print("="*60)
        print("🎯 PYTHON SECURITY TOOLKIT – MAIN MENU")
        print("="*60)
        print("1. ⚙️  Setup Dependencies")
        print("2. 🧪 Run Tasks")
        print("0. ❌ Exit")
        print("="*60)
        choice = input("📥 Enter your choice: ").strip()

        if choice == '1':
            clear()
            install_dependencies()
        elif choice == '2':
            task_menu()
        elif choice == '0':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")
            input("🔁 Press Enter to continue...")

if __name__ == "__main__":
    main_menu()