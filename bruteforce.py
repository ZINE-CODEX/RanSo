from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def main():
    zipfile_name = input("Enter the name of the zip file: ")
    txtfile_name = input("Enter the name of the text file containing passwords: ")

    print("\n===============================")
    print("|                             |")
    print("|          Lorenzo            |")
    print("|                             |")
    print("===============================\n")

    print("[+] Beginning brute force ")
    found = False
    with ZipFile(zipfile_name, 'r') as zf:
        with open(txtfile_name, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    found = True
                    break
                else:
                    print(f"[-] Incorrect password: {password}")
    
    if not found:
        print("[+] Password not found in list")

if __name__ == "__main__":
    main()
