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
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, IntPrompt
    from rich.text import Text
    from rich.layout import Layout
    from rich.align import Align
    from rich import box
    from rich.live import Live
    from datetime import datetime
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install rich")
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, IntPrompt
    from rich.text import Text
    from rich.layout import Layout
    from rich.align import Align
    from rich import box
    from rich.live import Live
    from datetime import datetime

console = Console()

def countdown(time_sec):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Đang chờ...", total=time_sec)
        
        for remaining_time in range(time_sec, -1, -1):
            progress.update(task, description=f"[yellow]⏱️  Còn lại {remaining_time} giây - [green]Đang nhận tiền...", completed=time_sec-remaining_time)
            time.sleep(1)
        
        progress.update(task, description="[green]✅ Hoàn thành!", completed=time_sec)

def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    
    # Tạo bảng hiển thị tài khoản Instagram
    table = Table(title="[bold cyan]📱 DANH SÁCH TÀI KHOẢN INSTAGRAM", box=box.ROUNDED)
    table.add_column("[bold blue]STT", style="cyan", no_wrap=True)
    table.add_column("[bold green]👤 Tên tài khoản", style="green")
    table.add_column("[bold yellow]📊 Trạng thái", style="yellow")
    
    user_INS = []
    account_id1 = []
    i = 1
    for data in checkurl1_2['data']:
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        
        table.add_row(
            str(i),
            f"[bold cyan]@{usernametk}",
            "[green]✅ Hoạt động"
        )
        i += 1
    
    console.print(table)
    console.print()
    
    # Nhập lựa chọn tài khoản
    choose = IntPrompt.ask("[bold yellow]🎯 Chọn tài khoản Instagram", default=1)
    
    console.clear()
    
    if choose >=1 or choose <= len(user_INS):
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_INS[0] 
        account_id = account_id1[0]
        
        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            console.print(Panel.fit(
                "[bold yellow]🍪 NHẬP COOKIE INSTAGRAM",
                border_style="yellow"
            ))
            cookieX = Prompt.ask("[bold green]Cookie Instagram")
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
            
        console.clear()
        banner()
        
        # Panel cấu hình
        config_panel = Panel(
            "[bold cyan]⚙️  CẤU HÌNH TOOL\n\n"
            "[yellow]• Số lượng job: Số nhiệm vụ muốn làm\n"
            "[yellow]• Delay: Thời gian chờ giữa các job (giây)",
            title="[bold green]📋 Hướng dẫn",
            border_style="green"
        )
        console.print(config_panel)
        
        choose = IntPrompt.ask("[bold cyan]🎯 Nhập số lượng Job", default=50)
        DELAY = IntPrompt.ask("[bold yellow]⏱️  Nhập Delay (giây)", default=10)
        
        console.clear()
        
        # Header cookies Instagram
        headerINS = {
                'accept': '*/*',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
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
        
        # Tạo bảng kết quả
        result_table = Table(title="[bold green]📊 KẾT QUẢ THỰC HIỆN", box=box.DOUBLE)
        result_table.add_column("[bold blue]STT", style="cyan", no_wrap=True)
        result_table.add_column("[bold yellow]⏰ Thời gian", style="yellow")
        result_table.add_column("[bold green]📋 Trạng thái", style="green")
        result_table.add_column("[bold red]🎯 Loại Job", style="red")
        result_table.add_column("[bold cyan]💰 Xu nhận", style="cyan")
        result_table.add_column("[bold magenta]💎 Tổng xu", style="magenta")
        
        tong = 0
        dem = 0
        
        # Panel thông tin bắt đầu
        start_panel = Panel(
            f"[bold green]🚀 BẮT ĐẦU THỰC HIỆN\n\n"
            f"[yellow]📊 Số job cần làm: [bold cyan]{choose}\n"
            f"[yellow]⏱️  Delay giữa các job: [bold cyan]{DELAY} giây\n"
            f"[yellow]👤 Tài khoản: [bold cyan]@{user_tiktok}",
            title="[bold blue]🎮 TOOL INSTAGRAM",
            border_style="blue"
        )
        console.print(start_panel)
        console.print()
        
        with Live(result_table, refresh_per_second=1, console=console) as live:
            for i in range(choose):
                try:
                    job = f'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id={account_id}&data=null'
                    nos = ses.get(job, headers=headers, params=param).json()
                    
                    if isinstance(nos.get('data'), dict):
                        console.print(f"[bold blue]🔍 [DEBUG] Job: ID={nos['data'].get('id')}, Type={nos['data'].get('type')}, Link={nos['data'].get('link')}")
                    else:
                        console.print(f"[bold yellow]⚠️  [DEBUG] Job: {nos.get('message', 'Không rõ')} (Nghỉ vài phút đi ba😴)")

                    if nos['status'] != 200:
                        console.print("[bold red]❌ Không có job, chờ 5 giây thử lại...\n")
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
                                current_time = datetime.now().strftime("%H:%M:%S")
                                prices = response['data']['prices']
                                tong += prices
                                
                                result_table.add_row(
                                    str(dem),
                                    current_time,
                                    "[green]✅ Thành công",
                                    "[red]👥 Follow",
                                    f"[cyan]+{prices}",
                                    f"[magenta]{tong} vnđ"
                                )
                                live.update(result_table)
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
                                    console.print(f"[bold red]⚠️  {checkskipjob['message']}")

                        elif '"status":"fail"' in response and '"spam":true' in response:
                            console.print("[bold red]🚫 Tài khoản này bị chặn Follow")
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            console.print('[bold red]💀 Cookie đã hết hạn! Đang xóa file cookie...')
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
                                current_time = datetime.now().strftime("%H:%M:%S")
                                prices = response['data']['prices']
                                tong += prices

                                result_table.add_row(
                                    str(dem),
                                    current_time,
                                    "[green]✅ Thành công",
                                    "[red]❤️  Like",
                                    f"[cyan]+{prices}",
                                    f"[magenta]{tong} vnđ"
                                )
                                live.update(result_table)
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
                                    console.print(f"[bold red]⚠️  {checkskipjob['message']}")

                        elif '"status":"fail"' in response and '"spam":true' in response:
                            console.print("[bold red]🚫 Tài khoản này bị chặn like")
                        elif '"status":"fail"' in response and '"require_login":true' in response:
                            console.print('[bold red]💀 Cookie đã hết hạn! Đang xóa file cookie...')
                            os.remove(f'COOKIEINS{account_id}.txt')
                            return 0

                except Exception as e:
                    console.print(f"[bold red]❌ [LỖI] {str(e)}")
                    time.sleep(3)
                    continue
        
        # Thông báo hoàn thành
        finish_panel = Panel(
            f"[bold green]🎉 HOÀN THÀNH!\n\n"
            f"[yellow]📊 Tổng job đã làm: [bold cyan]{dem}\n"
            f"[yellow]💰 Tổng xu kiếm được: [bold green]{tong} vnđ\n"
            f"[yellow]⏱️  Thời gian kết thúc: [bold cyan]{datetime.now().strftime('%H:%M:%S')}",
            title="[bold blue]📋 BÁO CÁO KẾT QUẢ",
            border_style="green"
        )
        console.print(finish_panel)

def banner():
    console.clear()
    
    # Tạo banner với Rich
    banner_text = Text()
    banner_text.append("██████╗░░█████╗░███╗░░██╗░██████╗░  ██╗░░██╗\n", style="bold red")
    banner_text.append("██╔══██╗██╔══██╗████╗░██║██╔════╝░  ╚██╗██╔╝\n", style="bold blue")
    banner_text.append("██████╦╝██║░░██║██╔██╗██║██║░░██╗░  ░╚███╔╝░\n", style="bold yellow")
    banner_text.append("██╔══██╗██║░░██║██║╚████║██║░░╚██╗  ░██╔██╗░\n", style="bold green")
    banner_text.append("██████╦╝╚█████╔╝██║░╚███║╚██████╔╝  ██╔╝╚██╗\n", style="bold magenta")
    banner_text.append("╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝", style="bold cyan")
    
    banner_panel = Panel(
        Align.center(banner_text),
        title="[bold blue]🎮 TOOL GOLIKE INSTAGRAM VIP",
        subtitle="[bold green]by Bóng X | Trần Đức Doanh 💎",
        border_style="blue",
        box=box.DOUBLE
    )
    
    info_text = Text()
    info_text.append("🔥 TOOL GOLIKE INSTAGRAM AUTO 100% VIP 👑\n", style="bold green")
    info_text.append("📱 Telegram: https://t.me/doanhvip1 👀\n", style="bold cyan")
    info_text.append("👑 ADMIN: Trần Đức Doanh 💤\n", style="bold yellow")
    info_text.append("🎵 TIKTOK: @doanh21105 👈\n", style="bold red")
    info_text.append("📘 FACEBOOK: Liên hệ qua Telegram", style="bold blue")
    
    info_panel = Panel(
        info_text,
        title="[bold yellow]ℹ️  THÔNG TIN TOOL",
        border_style="yellow"
    )
    
    console.print(banner_panel)
    console.print()
    console.print(info_panel)
    console.print()

def LIST():
    banner()

console.clear()
banner()

checkfile = os.path.isfile('user.txt')
if checkfile == False:
    auth_panel = Panel(
        "[bold yellow]🔑 ĐĂNG NHẬP GOLIKE\n\n"
        "[white]Nhập Authorization token từ Golike để tiếp tục:",
        title="[bold green]🚪 XÁC THỰC",
        border_style="green"
    )
    console.print(auth_panel)
    
    AUTHUR = Prompt.ask("[bold green]Authorization Golike")
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

if checkurl1['status']== 200:
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[green]Đang đăng nhập...", total=100)
        for i in range(100):
            time.sleep(0.03)
            progress.update(task, advance=1)
        
    console.print("[bold green]✅ ĐĂNG NHẬP THÀNH CÔNG!")
    time.sleep(2)
    console.clear()
    LIST()
    
    username = checkurl1['data']['username']
    coin = checkurl1['data']['coin']
    user_id = checkurl1['data']['id']
    
    # Hiển thị thông tin tài khoản
    account_info = Table(title="[bold cyan]👤 THÔNG TIN TÀI KHOẢN", box=box.ROUNDED)
    account_info.add_column("[bold yellow]Thông tin", style="yellow")
    account_info.add_column("[bold green]Chi tiết", style="green")
    
    account_info.add_row("👤 Tài khoản", f"[bold cyan]{username}")
    account_info.add_row("💰 Tổng tiền", f"[bold yellow]{coin} vnđ")
    account_info.add_row("🆔 User ID", f"[bold magenta]{user_id}")
    
    console.print(account_info)
    console.print()
    
    # Menu lựa chọn
    menu_panel = Panel(
        "[bold cyan]🎮 MENU CHÍNH\n\n"
        "[green]1. [bold white]🎯 Vào Tool Instagram\n"
        "[red]2. [bold white]🗑️  Xóa Authorization hiện tại",
        title="[bold blue]📋 LỰA CHỌN",
        border_style="blue"
    )
    console.print(menu_panel)
    
    choose = IntPrompt.ask("[bold white]Nhập lựa chọn", choices=["1", "2"], default="1")
    
    if choose == 1:
        console.clear()
        LIST()
        
        # Hiển thị lại thông tin tài khoản
        account_info = Table(title="[bold cyan]👤 THÔNG TIN TÀI KHOẢN", box=box.ROUNDED)
        account_info.add_column("[bold yellow]Thông tin", style="yellow")
        account_info.add_column("[bold green]Chi tiết", style="green")
        
        account_info.add_row("👤 Tài khoản", f"[bold cyan]{username}")
        account_info.add_row("💰 Tổng tiền", f"[bold yellow]{coin} vnđ")
        
        console.print(account_info)
        console.print()
        
        INSTAGRAM()
    elif choose == 2:
        console.print("[bold yellow]🗑️  Đang xóa Authorization...")
        os.remove('user.txt')
        console.print("[bold green]✅ Đã xóa thành công! Khởi động lại tool để đăng nhập mới.")
else:
    console.print(Panel(
        "[bold red]❌ ĐĂNG NHẬP THẤT BẠI!\n\n"
        "[yellow]Vui lòng kiểm tra lại Authorization token.",
        title="[bold red]🚫 LỖI XÁC THỰC",
        border_style="red"
    ))
    if os.path.exists('user.txt'):
        os.remove('user.txt')