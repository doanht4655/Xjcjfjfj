import requests
import random
import string
import hashlib, os

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"
# Thêm màu mới
cam = "\033[1;38;5;208m\033[1m"
hong = "\033[1;38;5;205m\033[1m"
xanh_bien = "\033[1;38;5;39m\033[1m"

import os

try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

# Giao diện mới với chủ đề "Bóng x"
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{xanh_bien}╔═══════════════════════════════════════════════════════════════╗
{xanh_bien}║ {tim}██████╗  ██████╗ ███╗   ██╗ ██████╗     {hong}██╗  ██╗{xanh_bien}       ║
{xanh_bien}║ {tim}██╔══██╗██╔═══██╗████╗  ██║██╔════╝     {hong}╚██╗██╔╝{xanh_bien}       ║
{xanh_bien}║ {tim}██████╔╝██║   ██║██╔██╗ ██║██║  ███╗     {hong}╚███╔╝ {xanh_bien}       ║
{xanh_bien}║ {tim}██╔══██╗██║   ██║██║╚██╗██║██║   ██║     {hong}██╔██╗ {xanh_bien}       ║
{xanh_bien}║ {tim}██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝    {hong}██╔╝ ██╗{xanh_bien}       ║
{xanh_bien}║ {tim}╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     {hong}╚═╝  ╚═╝{xanh_bien}       ║
{xanh_bien}╠═══════════════════════════════════════════════════════════════╣
{xanh_bien}║ {vang}[+] Công Cụ Tự Động Tạo Tài Khoản Facebook               {xanh_bien}║
{xanh_bien}║ {vang}[+] Version: 2.0                                         {xanh_bien}║
{xanh_bien}║ {vang}[+] Tạo bởi: Bóng x                                      {xanh_bien}║
{xanh_bien}╚═══════════════════════════════════════════════════════════════╝
""")

print_banner()

def reverse_string(s):
    return s[::-1]

def xePwjMDG(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def tLx6cpsx():
    url = 'https://api.mail.tm/domains'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            pass
            return None
    except Exception as e:
        print(f'{vua}{do}[×] Lỗi: {e}')
        return None

def f9kSLNSXl():
    fake = Faker()
    mail_domains = tLx6cpsx()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = xePwjMDG(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = 'https://api.mail.tm/accounts'
        headers = {'Content-Type': 'application/json'}
        data = {'address': f'{username}@{domain}', 'password': password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'{vua}{xanh_la}[√] Email đã tạo: {username}@{domain}')
                return (f'{username}@{domain}', password, first_name, last_name, birthday)
            else:
                pass
                return None, None, None, None, None
        except Exception as e:
            print(f'{vua}{do}[×] Lỗi: {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def QuanHau(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': xePwjMDG(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    response = requests.post(api_url, data=req)

    if response.status_code == 200:
        reg = response.json()
        id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')
        print(f"""
{xanh_bien}╔════════════════════════════════════════════╗
{xanh_bien}║ {vang}[+] Thông Tin Tài Khoản Facebook Mới      {xanh_bien}║
{xanh_bien}╠════════════════════════════════════════════╣
{xanh_bien}║ {xanh_la}[+] Email: {trang}{email}{xanh_bien}
{xanh_bien}║ {xanh_la}[+] Mật khẩu: {trang}{password}{xanh_bien}
{xanh_bien}║ {xanh_la}[+] Tên: {trang}{first_name} {last_name}{xanh_bien}
{xanh_bien}║ {xanh_la}[+] Ngày sinh: {trang}{birthday}{xanh_bien}
{xanh_bien}║ {xanh_la}[+] Giới tính: {trang}{gender}{xanh_bien}
{xanh_bien}╚════════════════════════════════════════════╝
""")
    else:
        print(f'{vua}{do}[×] Lỗi đăng ký: {response.text}')

def WcfriFTc(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def create_accounts(num_accounts):
    print(f"{xanh_bien}╔════════════════════════════════════════════╗")
    print(f"{xanh_bien}║ {vang}[+] Bắt đầu quá trình tạo tài khoản...     {xanh_bien}║")
    print(f"{xanh_bien}╚════════════════════════════════════════════╝")
    
    success = 0
    for i in range(num_accounts):
        print(f"{vang}[*] Đang tạo tài khoản {i+1}/{num_accounts}...")
        email, password, first_name, last_name, birthday = f9kSLNSXl()
        if email and password and first_name and last_name and birthday:
            QuanHau(email, password, first_name, last_name, birthday)
            success += 1
    
    print(f"{xanh_bien}╔════════════════════════════════════════════╗")
    print(f"{xanh_bien}║ {vang}[+] Hoàn thành tạo tài khoản               {xanh_bien}║")
    print(f"{xanh_bien}║ {vang}[+] Tổng số: {xanh_la}{num_accounts} {vang}| Thành công: {xanh_la}{success} {vang}| Thất bại: {do}{num_accounts-success}{xanh_bien} ║")
    print(f"{xanh_bien}╚════════════════════════════════════════════╝")

# Sử dụng: gọi hàm create_accounts với số lượng tài khoản cần tạo
print(f"{xanh_bien}╔════════════════════════════════════════════╗")
num_accounts = int(input(f"{xanh_bien}║ {vang}[+] Số tài khoản cần tạo: {xanh_la}"))
print(f"{xanh_bien}╚════════════════════════════════════════════╝")
create_accounts(num_accounts)
