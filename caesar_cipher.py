import os
from datetime import datetime

LOG_FILE = os.path.join("exports", "activity_log.txt")

COMMON_WORDS = {
    "the", "and", "hello", "security", "network", "attack",
    "password", "cyber", "computer", "system", "user", "admin"
}


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print("Invalid input. Enter a number only.")


def encrypt_text():
    text = input("Enter text to encrypt: ")
    shift = get_shift()

    encrypted = caesar_encrypt(text, shift)

    print("\nEncrypted Text:")
    print(encrypted)

    write_log("ENCRYPT", f"Shift={shift}, Length={len(text)}")


def decrypt_text():
    text = input("Enter text to decrypt: ")
    shift = get_shift()

    decrypted = caesar_decrypt(text, shift)

    print("\nDecrypted Text:")
    print(decrypted)

    write_log("DECRYPT", f"Shift={shift}, Length={len(text)}")


def brute_force_analysis():
    ciphertext = input("Enter encrypted text: ")

    results = []

    print("\nPossible Decryptions:\n")

    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        score = score_plaintext(decrypted)

        results.append((score, shift, decrypted))

        print(f"Shift {shift:2} -> {decrypted}")

    best = max(results)

    print("\nMost Likely Plaintext:")
    print(f"Shift {best[1]}")
    print(best[2])

    write_log(
        "BRUTE_FORCE_ANALYSIS",
        f"Length={len(ciphertext)}, BestShift={best[1]}"
    )


def write_log(action, details):
    ensure_folders()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] {action} | {details}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)


def ensure_folders():
    os.makedirs("encrypted_files", exist_ok=True)
    os.makedirs("decrypted_files", exist_ok=True)
    os.makedirs("exports", exist_ok=True)


def encrypt_file():
    ensure_folders()

    file_path = input("Enter file path to encrypt: ")

    if not os.path.exists(file_path):
        print("File not found.")
        return

    shift = get_shift()

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    encrypted_content = caesar_encrypt(content, shift)

    filename = os.path.basename(file_path)
    output_path = os.path.join("encrypted_files", "encrypted_" + filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(encrypted_content)

    write_log(
        "FILE_ENCRYPT",
        f"File={file_path}, Output={output_path}, Shift={shift}, "
        f"Length={len(content)}, Status=SUCCESS"
    )

    print("\nFile encrypted successfully.")
    print(f"Saved as: {output_path}")


def decrypt_file():
    ensure_folders()

    file_path = input("Enter file path to decrypt: ")

    if not os.path.exists(file_path):
        print("File not found.")
        return

    shift = get_shift()

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    decrypted_content = caesar_decrypt(content, shift)

    filename = os.path.basename(file_path)
    output_path = os.path.join("decrypted_files", "decrypted_" + filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(decrypted_content)

    write_log(
        "FILE_DECRYPT",
        f"File={file_path}, Output={output_path}, Shift={shift}, "
        f"Length={len(content)}, Status=SUCCESS"
    )

    print("\nFile decrypted successfully.")
    print(f"Saved as: {output_path}")


def view_history():
    if not os.path.exists(LOG_FILE):
        print("No activity log found.")
        return

    print("\nActivity log is ready.")
    print(f"Location: {LOG_FILE}")
    print("Open the exports folder to view the activity log.")


def export_report():
    operation_counts = {}

    ensure_folders()

    if not os.path.exists(LOG_FILE):
        print("No history available.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as log_file:
        logs = log_file.readlines()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_path = os.path.join("exports", "security_report.txt")

    for line in logs:
        if "] " in line:
            action_part = line.split("] ")[1]
            action = action_part.split(" | ")[0].strip()
            operation_counts[action] = operation_counts.get(action, 0) + 1

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("CAESAR CIPHER TOOLKIT SECURITY REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Generated On: {timestamp}\n\n")
        report.write(f"Total Operations: {len(logs)}\n\n")

        report.write("Operation Summary:\n")
        report.write("-" * 30 + "\n")

        for action, count in operation_counts.items():
            report.write(f"{action}: {count}\n")

        report.write("\nHistory Entries:\n")
        report.write("-" * 50 + "\n")

        for entry in logs:
            report.write(entry)

    print("\nReport exported successfully.")
    print(f"Location: {report_path}")
    print("Open the exports folder to view the generated report.")


def score_plaintext(text):
    words = text.lower().split()
    score = 0

    for word in words:
        if word in COMMON_WORDS:
            score += 1

    return score


def search_logs():
    if not os.path.exists(LOG_FILE):
        print("No history log found.")
        return

    keyword = input("Enter keyword to search: ").strip()

    found = False

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No matching entries found.")


def rot13(text):
    return caesar_encrypt(text, 13)


def rot13_menu():
    text = input("Enter text: ")

    result = rot13(text)

    print("\nROT13 Result:")
    print(result)

    write_log("ROT13", f"Length={len(text)}")


def main():
    while True:
        print("\n" + "=" * 42)
        print(" CIPHERFORGE - CAESAR CIPHER TOOLKIT")
        print("=" * 42)

        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Brute Force Analysis")
        print("4. Encrypt File")
        print("5. Decrypt File")
        print("6. View History Log")
        print("7. Export Security Report")
        print("8. Search Logs")
        print("9. ROT13 Encoder")
        print("10. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            encrypt_text()
        elif choice == "2":
            decrypt_text()
        elif choice == "3":
            brute_force_analysis()
        elif choice == "4":
            encrypt_file()
        elif choice == "5":
            decrypt_file()
        elif choice == "6":
            view_history()
        elif choice == "7":
            export_report()
        elif choice == "8":
            search_logs()
        elif choice == "9":
            rot13_menu()
        elif choice == "10":
            print("Goodbye!\n")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
