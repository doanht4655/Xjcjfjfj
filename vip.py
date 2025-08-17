trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hong = "\033[1;95m"
cam = "\033[1;91m"

import json
import requests, os, time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    clear()
    print(f"""
\033[1;96m┌─────────────────────────────────────────────────────────────┐
\033[1;96m│  \033[1;93m██████╗  ██████╗ ███╗   ██╗ ██████╗    ██╗  ██╗           \033[1;96m│
\033[1;96m│  \033[1;93m██╔══██╗██╔═══██╗████╗  ██║██╔════╝    ╚██╗██╔╝           \033[1;96m│
\033[1;96m│  \033[1;93m██████╔╝██║   ██║██╔██╗ ██║██║  ███╗    ╚███╔╝            \033[1;96m│
\033[1;96m│  \033[1;93m██╔══██╗██║   ██║██║╚██╗██║██║   ██║    ██╔██╗            \033[1;96m│
\033[1;96m│  \033[1;93m██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝   ██╔╝ ██╗           \033[1;96m│
\033[1;96m│  \033[1;93m╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝    ╚═╝  ╚═╝           \033[1;96m│
\033[1;96m├─────────────────────────────────────────────────────────────┤
\033[1;96m│     \033[1;91m🔥 TIKTOK AUTO TOOL - PREMIUM VERSION 🔥         \033[1;96m│
\033[1;96m├─────────────────────────────────────────────────────────────┤
\033[1;96m│ \033[1;95m👤 Dev: \033[1;93mTrần Đức Doanh \033[1;96m│ \033[1;95m📱 TG: \033[1;94m@doanhvip1     \033[1;96m│
\033[1;96m│ \033[1;95m⚡ Ver: \033[1;92mV3.0 Premium    \033[1;96m│ \033[1;95m🎯 Brand: \033[1;91mBÓNG X   \033[1;96m│
\033[1;96m└─────────────────────────────────────────────────────────────┘\033[0m
    """)

def loading(text, time_sleep=1):
    """Animation loading gọn gàng"""
    for i in "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏":
        print(f"\r\033[1;93m{i} {text}...\033[0m", end="", flush=True)
        time.sleep(0.1)
    time.sleep(time_sleep)
    print("\r" + " " * 50 + "\r", end="")

def log(msg, type="info"):
    """Log gọn gàng với icon"""
    now = datetime.now().strftime('%H:%M:%S')
    if type == "success":
        print(f"\033[1;92m✓\033[0m \033[1;97m{now}\033[0m {msg}")
    elif type == "error":
        print(f"\033[1;91m✗\033[0m \033[1;97m{now}\033[0m {msg}")
    elif type == "warning":
        print(f"\033[1;93m⚠\033[0m \033[1;97m{now}\033[0m {msg}")
    else:
        print(f"\033[1;94mℹ\033[0m \033[1;97m{now}\033[0m {msg}")

def input_styled(prompt, color="\033[1;96m"):
    """Input với style đẹp"""
    return input(f"{color}➤ {prompt}\033[1;97m")

logo()
loading("Khởi động hệ thống")

# Xử lý file config
try:
    Authorization = open('Authorization.txt', 'x')
    t = open('token.txt', 'x')
except:
    pass

Authorization = open('Authorization.txt', 'r')
t = open('token.txt', 'r')
author = Authorization.read()
token = t.read()

if author == '':
    print(f"\n\033[1;96m┌─ CẤU HÌNH TÀI KHOẢN ─┐\033[0m")
    author = input_styled("Nhập Authorization:", "\033[1;93m")
    token = input_styled("Nhập Token:", "\033[1;93m")
    Authorization = open('Authorization.txt', 'w')
    t = open('token.txt', 'w')
    Authorization.write(author)
    t.write(token)
    log("Lưu thông tin thành công!", "success")
else:
    print(f"\n\033[1;96m┌─ TÀI KHOẢN HIỆN TẠI ─┐\033[0m")
    select = input_styled("Enter = Giữ nguyên | Nhập auth mới = Đổi tài khoản:", "\033[1;93m")
    if select != '':
        author = select
        token = input_styled("Nhập Token mới:", "\033[1;93m")
        Authorization = open('Authorization.txt', 'w')
        t = open('token.txt', 'w')
        Authorization.write(author)
        t.write(token)
        log("Cập nhật tài khoản thành công!", "success")

Authorization.close()
t.close()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok'
}

def chonacc():
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
    return response

def nhannv(account_id):
    params = {'account_id': account_id, 'data': 'null'}
    json_data = {}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers, json=json_data).json()
    return response

def hoanthanh(ads_id, account_id):
    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'data': None}
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json=json_data).json()
    return response

def baoloi(ads_id, object_id, account_id, loai):
    json_data1 = {'description': 'Tôi đã làm Job này rồi', 'users_advertising_id': ads_id, 'type': 'ads', 'provider': 'tiktok', 'fb_id': account_id, 'error_type': 6}
    response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()
    json_data = {'ads_id': ads_id, 'object_id': object_id, 'account_id': account_id, 'type': loai}
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data).json()

loading("Đang kết nối server")
chontktiktok = chonacc()

def show_accounts():
    if chontktiktok['status'] != 200:
        log('Lỗi Authorization hoặc Token!', "error")
        quit()
    
    print(f"\n\033[1;96m┌─ DANH SÁCH TÀI KHOẢN ─┐\033[0m")
    for i in range(len(chontktiktok['data'])):
        print(f"\033[1;97m{i + 1}. \033[1;93m{chontktiktok['data'][i]['nickname']}\033[0m")
    print(f"\033[1;96m└─────────────────────────┘\033[0m")

show_accounts()

# Chọn tài khoản
while True:
    try:
        luachon = int(input_styled("Chọn tài khoản:", "\033[1;95m"))
        if luachon > len(chontktiktok['data']) or luachon < 1:
            log("Số thứ tự không hợp lệ!", "error")
            continue
        account_id = chontktiktok['data'][luachon - 1]['id']
        log(f"Đã chọn: {chontktiktok['data'][luachon - 1]['nickname']}", "success")
        break
    except:
        log("Vui lòng nhập số!", "error")

# Cài đặt delay
while True:
    try:
        delay = int(input_styled("Thiết lập delay (giây):", "\033[1;95m"))
        log(f"Delay: {delay}s", "success")
        break
    except:
        log("Vui lòng nhập số!", "error")

# Cài đặt giới hạn lỗi
while True:
    try:
        doiacc = int(input_styled("Số lần thất bại tối đa:", "\033[1;95m"))
        log(f"Giới hạn lỗi: {doiacc} lần", "success")
        break
    except:
        log("Vui lòng nhập số!", "error")

# Bắt đầu chạy
logo()
log("🚀 Bắt đầu chạy tool!", "success")
print()

dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []

while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok['data'][luachon - 1]['nickname'])
        log(f"Tài khoản {dsaccloi} gặp lỗi! Đổi tài khoản.", "warning")
        show_accounts()
        while True:
            try:
                luachon = int(input_styled("Chọn tài khoản mới:", "\033[1;95m"))
                if luachon > len(chontktiktok['data']) or luachon < 1:
                    continue
                account_id = chontktiktok['data'][luachon - 1]['id']
                checkdoiacc = 0
                log(f"Đổi sang: {chontktiktok['data'][luachon - 1]['nickname']}", "success")
                break
            except:
                log("Vui lòng nhập số!", "error")

    print(f"\033[1;94m🔍 Tìm nhiệm vụ...\033[0m", end="\r")
    
    while True:
        try:
            nhanjob = nhannv(account_id)
            break
        except:
            pass

    if nhanjob['status'] == 200:
        ads_id = nhanjob['data']['id']
        link = nhanjob['data']['link']
        object_id = nhanjob['data']['object_id']
        
        if nhanjob['data']['type'] != 'follow':
            baoloi(ads_id, object_id, account_id, nhanjob['data']['type'])
            continue

        print(f"\033[1;92m✓ Tìm thấy job: {link[:50]}...\033[0m")
        os.system(f'termux-open-url {link}')

        # Countdown đẹp và gọn
        for i in range(delay, -1, -1):
            colors = ['\033[1;91m', '\033[1;93m', '\033[1;92m', '\033[1;96m', '\033[1;95m']
            icons = ['🔥', '⚡', '💎', '⭐', '🌟']
            color = colors[i % len(colors)]
            icon = icons[i % len(icons)]
            print(f"\r{color}{icon} BÓNG X {icon} ⏰ {i:02d}s\033[0m", end="", flush=True)
            time.sleep(1)
        
        print("\r" + " " * 30 + "\r", end="")
        print("\033[1;95m💰 Đang nhận tiền...\033[0m", end="\r")
        
        attempts = 0
        max_attempts = 2
        
        while attempts < max_attempts:
            try:
                nhantien = hoanthanh(ads_id, account_id)
                if nhantien['status'] == 200:
                    dem += 1
                    tien = nhantien['data']['prices']
                    tong += tien
                    
                    now = datetime.now().strftime('%H:%M:%S')
                    print(" " * 50, end="\r")
                    print(f"\033[1;92m✓ #{dem} \033[1;97m{now} \033[1;93m+{tien}đ \033[1;95m💰{tong}đ \033[1;94m{nhantien['data']['type']}\033[0m")
                    checkdoiacc = 0
                    break
                    
                elif attempts == 0:
                    for j in range(3, 0, -1):
                        print(f"\r\033[1;93m⏳ Thử lại... {j}s\033[0m", end="", flush=True)
                        time.sleep(1)
                    print("\r" + " " * 20 + "\r", end="")
                attempts += 1
            except Exception as e:
                attempts += 1
                time.sleep(1)

        if attempts == max_attempts and nhantien['status'] != 200:
            log("Bỏ qua nhiệm vụ", "warning")
            try:
                baoloi(ads_id, object_id, account_id, nhanjob['data']['type'])
                checkdoiacc += 1
            except:
                pass
    else:
        log("Không có nhiệm vụ", "warning")
        time.sleep(5)
