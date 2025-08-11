try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")

def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mB\033[1;36mÓ\033[1;35mN\033[1;32mG \033[1;31mX\033[1;34m👑 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;34mB\033[1;31mÓ\033[1;37mN\033[1;36mG \033[1;32mX\033[1;35m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
            "\033[1;31mB\033[1;37mÓ\033[1;36mN\033[1;33mG \033[1;35mX\033[1;37m👑 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            "\033[1;32mB\033[1;33mÓ\033[1;34mN\033[1;35mG \033[1;36mX\033[1;34m🍉 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
            "\033[1;37mB\033[1;34mÓ\033[1;35mN\033[1;36mG \033[1;32mX\033[1;34m👑 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
            "\033[1;34mB\033[1;33mÓ\033[1;37mN\033[1;35mG \033[1;31mX\033[1;37m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;36mB\033[1;35mÓ\033[1;31mN\033[1;34mG \033[1;37mX\033[1;33m👑 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")

def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_INS = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i = 1
    for data in checkurl1_2['data'] :
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"Hoạt Động"+Fore.RED)
        account.append(usernametk)
        print(f'\033[1;36m[{i}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {usernametk} \033[1;97m|\033[1;32m㊪ :\033[1;93m {STATUS[-1]}')
       
        i += 1
    print('\033[97m════════════════════════════════════════════════')
    choose = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_INS) :
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_INS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            cookieX = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Cookie Instagram: ')
            createfile = open('COOKIEINS'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        choose = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Số Lượng Job : '))
        headerINS = {
                'accept': '*/*',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                # 'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookieINS,
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/p/C9RAZEJNjPC/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                'x-asbd-id': '129477',
                'x-csrftoken': cookieINS.split('csrftoken=')[1].split(';')[0],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1Jw2LrciyrzAQskwSVGREElPZZJZjW74y38oTjDnNHOu9e',
                'x-instagram-ajax': '1014868636',
                'x-requested-with': 'XMLHttpRequest',
            }
        param = {
            'instagram_account_id': account_id,
            'data': 'null',
        }
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Delay : '))
        print("\033[97m════════════════════════════════════════════════")
        print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')
        for i in range(choose):
            try:
                job = f'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id={account_id}&data=null'
                nos = ses.get(job, headers=headers, params=param).json()
                if isinstance(nos.get('data'), dict):
                    print(f"[DEBUG] Job: ID={nos['data'].get('id')}, Type={nos['data'].get('type')}, Link={nos['data'].get('link')}")
                else:
                    print(f"⚠️ [DEBUG] Job: {nos.get('message', 'Không rõ')} (Nghỉ vài phút đi ba😴)")

                if nos['status'] != 200:
                    print("[!] Không có job, chờ 5 giây thử lại...\n")
                    time.sleep(5)
                    continue

                ads_id = nos['data']['id']
                object_id = nos['data']['object_id']
                job_type = nos['data']['type']

                if job_type == 'follow':
                    url = f'https://www.instagram.com/api/v1/friendships/create/{object_id}/'
                    data = {
                        'container_module': 'profile',
                        'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                        'user_id': object_id,
                    }
                    response = requests.post(url, headers=headerINS, data=data).text
                    countdown(DELAY)

                    if '"status":"ok"' in response:
                        url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                        json_data = {
                            'instagram_account_id': account_id,
                            'instagram_users_advertising_id': ads_id,
                            'async': True,
                            'data': 'null',
                        }
                        time.sleep(3)
                        response = requests.post(url, headers=headers, json=json_data).json()

                        if response.get('success') == True:
                            dem += 1
                            local_time = time.localtime()
                            h, m, s = [f"{t:02d}" for t in (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)]
                            prices = response['data']['prices']
                            tong += prices
                            print(
                                f"\033[1;31m| \033[1;36m{dem}\033[1;97m | "
                                f"\033[1;33m{h}:{m}:{s}\033[1;97m | "
                                f"\033[1;32msuccess\033[1;97m | "
                                f"\033[1;31mfollow\033[1;97m | "
                                f"\033[1;32mẨn ID\033[1;97m | "
                                f"\033[1;32m+{prices} \033[1;97m| "
                                f"\033[1;33m{tong} vnđ"
                            )
                        else:
                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                            params = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'object_id': object_id,
                                'async': 'true',
                                'data': 'null',
                                'type': job_type,
                            }
                            checkskipjob = ses.post(skipjob, params=params).json()
                            if checkskipjob['status'] == 200:
                                print(Fore.RED + str(checkskipjob['message']))

                    elif '"status":"fail"' in response and '"spam":true' in response:
                        print(Fore.RED + "Tài khoản này bị nhã Follow")
                    elif '"status":"fail"' in response and '"require_login":true' in response:
                        print('Cookie die rồi! Tôi rất tiếc')
                        os.remove(f'COOKIEINS{account_id}.txt')
                        return 0

                elif job_type == 'like':
                    like_id = nos['data']['description']
                    url = f'https://www.instagram.com/api/v1/web/likes/{like_id}/like/'
                    response = requests.post(url, headers=headerINS).text
                    countdown(DELAY)

                    if '"status":"ok"' in response:
                        json_data = {
                            'instagram_account_id': account_id,
                            'instagram_users_advertising_id': ads_id,
                            'async': True,
                            'data': 'null',
                        }
                        time.sleep(3)
                        response = requests.post(
                            'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                            headers=headers,
                            json=json_data,
                        ).json()

                        if response['success'] == True:
                            dem += 1
                            local_time = time.localtime()
                            h = f"{local_time.tm_hour:02d}"
                            m = f"{local_time.tm_min:02d}"
                            s = f"{local_time.tm_sec:02d}"
                            prices = response['data']['prices']
                            tong += prices

                            print(
                                f"\033[1;31m| \033[1;36m{dem}\033[1;97m | "
                                f"\033[1;33m{h}:{m}:{s}\033[1;97m | "
                                f"\033[1;32msuccess\033[1;97m | "
                                f"\033[1;31mlike \033[1;97m | "
                                f"\033[1;32mẨn ID\033[1;97m | "
                                f"\033[1;32m+{prices} \033[1;97m | "
                                f"\033[1;33m{tong} vnđ"
                            )
                        else:
                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                            params = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'object_id': object_id,
                                'async': 'true',
                                'data': 'null',
                                'type': job_type,
                            }
                            checkskipjob = ses.post(skipjob, params=params).json()
                            if checkskipjob['status'] == 200:
                                print(Fore.RED + str(checkskipjob['message']))

                    elif '"status":"fail"' in response and '"spam":true' in response:
                        print(Fore.RED + "Tài khoản này bị chặn like")
                    elif '"status":"fail"' in response and '"require_login":true' in response:
                        print('Cookie die rồi! Tôi rất tiếc')
                        os.remove(f'COOKIEINS{account_id}.txt')
                        return 0

            except Exception as e:
                print(f"[LỖI] {str(e)}")
                time.sleep(3)
                continue

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""  
[1;31m██████╗░░█████╗░███╗░░██╗░██████╗░  ██╗░░██╗
[1;34m██╔══██╗██╔══██╗████╗░██║██╔════╝░  ╚██╗██╔╝
[1;33m██████╦╝██║░░██║██╔██╗██║██║░░██╗░  ░╚███╔╝░
[1;32m██╔══██╗██║░░██║██║╚████║██║░░╚██╗  ░██╔██╗░
[1;35m██████╦╝╚█████╔╝██║░╚███║╚██████╔╝  ██╔╝╚██╗
[1;36m╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝

[1;97mTool By: [1;32mBóng X | Trần Đức Doanh💎        [1;97mPhiên Bản: [1;32mVIP👑     
[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;32m[•] TOOL GOLIKE INSTAGRAM AUTO 100% VIP 👑
[1;36m[•] Telegram: https://t.me/doanhvip1 👀
[1;33m[•] ADMIN: Trần Đức Doanh 💤
[1;31m[•] TIKTOK: 👉 @doanh21105 👈
[1;34m[•] FACEBOOK: https://www.facebook.com/đéo lộ
[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush() 
        sleep(0.00125)

def LIST():
    banner()

os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()

ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9"
])

headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers).json()

if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        LIST()
        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        user_id = checkurl1['data']['id']
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
        print(Fore.RED+'\033[97m════════════════════════════════════════════════')
        print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Instagram\033[1;33m")
        print(Fore.RED+'Nhập 2 Để Xóa Authorization Hiện Tại')
        choose = int(input(Fore.WHITE+'Nhập Lựa Chọn : '))
        if choose == 1:
            os.system('cls' if os.name== 'nt' else 'clear')
            LIST()
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'\033[97m════════════════════════════════════════════════')
            INSTAGRAM()
        elif choose == 2:
                os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')
