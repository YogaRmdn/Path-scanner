import requests
import socket
import time
import random
from options.header import *
from options.color import *


# 🔹 List User-Agent biar lebih aman
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.1",
]


def get_headers():
    """Ambil User-Agent random dari list"""
    return {"User-Agent": random.choice(USER_AGENTS)}


def cek_domain(domain):
    """Cek apakah domain valid & bisa diakses"""
    try:
        socket.gethostbyname(domain)
        url = f"https://{domain}"
        r = requests.get(url, headers=get_headers(), timeout=5)
        return r.status_code < 500
    except (socket.gaierror, requests.RequestException):
        return False


def path_scanner(target, wordlist):
    print(f"\n{BOLD_CYAN}[*] Memulai scanning pada {BOLD_RED}{target}{RESET}{BOLD_CYAN}...{RESET}")
    print(f"-"*40)

    try:
        with open(wordlist, 'r') as file:
            datas = file.read().splitlines()
    except FileNotFoundError:
        print(f"\n{BOLD_RED}[!] File wordlist tidak ditemukan{RESET}")
        time.sleep(0.5)
        return

    for data in datas:
        try:
            url = f"https://{target}/{data}"
            respon = requests.get(url, headers=get_headers(), timeout=3)
            hasil = respon.status_code

            if hasil < 400:
                print(f"{BOLD_CYAN}[*]{RESET} {url:<40}: {BOLD_GREEN}{hasil}{RESET}")
                time.sleep(0.5)
        except requests.RequestException:
            time.sleep(0.5)
            pass


if __name__ == "__main__":
    while True:
        try:
            clean()
            header()
            target = input(f"{BOLD_CYAN}[?]{RESET} Domain target\t: ")
            word = input(f"{BOLD_CYAN}[?]{RESET} Wordlist\t\t: ")
            print("-"*40)

            if not cek_domain(target):
                time.sleep(0.5)
                print(f"\n{BOLD_RED}[!] Domain tidak valid / tidak bisa diakses{RESET}")
                time.sleep(1)
                input(f"{BOLD_RED}[!] Klik enter untuk melanjutkan...{RESET}")
                time.sleep(1)
                continue

            path_scanner(target, word)

            print(f"\n{BOLD_CYAN}[?] Scanning selesai...{RESET}")
            time.sleep(0.5)
            t = input(f"{BOLD_CYAN}[?]{RESET} Lagi? (y/n) : ")
            if t.lower() == "y":
                time.sleep(0.5)
                continue
            elif t.lower() == "n":
                time.sleep(0.5)
                break
        except KeyboardInterrupt:
            print(f"\n{BOLD_RED}[!] Tools dihentikan...{RESET}")
            time.sleep(0.5)
            break
