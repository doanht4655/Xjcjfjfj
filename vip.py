import os
import sys
import time
import json
import requests
import random
from typing import Dict, List, Optional, Union, Any, Tuple

# Thiết lập timezone Việt Nam
import pytz
from datetime import datetime
tz = pytz.timezone("Asia/Ho_Chi_Minh")

# Thêm thư viện để tăng tính thẩm mỹ
import threading
from itertools import cycle

# Constants
AUTH_FILE = "Authorization.txt"
VERSION = "2.0"
AUTHOR = "👑 BÓNG X 👑"

# ANSI Color codes
class Colors:
    YELLOW = "\033[1;33m"
    PINK = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;97m"
    GREEN = "\033[1;32m"
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    PURPLE = "\033[1;95m"
    ORANGE = "\033[38;5;208m"
    MAGENTA = "\033[38;5;201m"
    GOLD = "\033[38;5;220m"
    LIME = "\033[38;5;118m"
    TEAL = "\033[38;5;51m"
    LAVENDER = "\033[38;5;183m"
    RESET = "\033[0m"

# ANSI Style codes
class Styles:
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    ITALIC = "\033[3m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"
    RESET = "\033[0m"

def colored(text: str, color: str, style: str = "") -> str:
    """Hiển thị văn bản có màu và kiểu dáng."""
    colors = {
        "yellow": Colors.YELLOW,
        "pink": Colors.PINK,
        "cyan": Colors.CYAN,
        "white": Colors.WHITE,
        "green": Colors.GREEN,
        "red": Colors.RED,
        "blue": Colors.BLUE,
        "purple": Colors.PURPLE,
        "orange": Colors.ORANGE,
        "magenta": Colors.MAGENTA,
        "gold": Colors.GOLD,
        "lime": Colors.LIME,
        "teal": Colors.TEAL,
        "lavender": Colors.LAVENDER,
        "reset": Colors.RESET
    }
    
    styles = {
        "bold": Styles.BOLD,
        "underline": Styles.UNDERLINE,
        "blink": Styles.BLINK,
        "italic": Styles.ITALIC,
        "reverse": Styles.REVERSE,
        "strikethrough": Styles.STRIKETHROUGH
    }
    
    style_code = styles.get(style, "")
    return style_code + colors.get(color, "") + text + Colors.RESET

# Các hiệu ứng trực quan nâng cao
class AnimationEffect:
    @staticmethod
    def spinner(stop_event: threading.Event, text: str, color: str = "cyan"):
        """Hiệu ứng quay vòng tròn tinh tế."""
        spinners = "⣾⣽⣻⢿⡿⣟⣯⣷"
        for char in cycle(spinners):
            if stop_event.is_set():
                break
            print(colored(f"\r{char} {text}", color), end="", flush=True)
            time.sleep(0.1)
        print("\r" + " " * (len(text) + 2), end="\r", flush=True)
    
    @staticmethod
    def progress_bar(progress: float, total: float, prefix: str = "", suffix: str = "", length: int = 30, 
                    fill: str = "█", empty: str = "░", color: str = "cyan"):
        """Tạo thanh tiến trình đẹp mắt với màu sắc."""
        percent = min(1.0, progress / total) if total else 0
        filled_length = int(length * percent)
        bar = fill * filled_length + empty * (length - filled_length)
        text = f"\r{prefix} [{bar}] {int(percent * 100)}% {suffix}"
        print(colored(text, color), end="", flush=True)
    
    @staticmethod
    def rainbow_text(text: str) -> str:
        """Tạo văn bản với hiệu ứng cầu vồng."""
        colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
        rainbow = ""
        for i, char in enumerate(text):
            if char.strip():
                color = colors[i % len(colors)]
                rainbow += colored(char, color)
            else:
                rainbow += char
        return rainbow
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.03, color: str = "cyan"):
        """Hiệu ứng đánh máy chữ."""
        for char in text:
            print(colored(char, color), end="", flush=True)
            time.sleep(delay)
        print()

def loading_animation(text: str, duration: float = 1, color: str = "cyan") -> None:
    """Hiệu ứng đang tải với nhiều hiệu ứng."""
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=AnimationEffect.spinner, args=(stop_event, text, color))
    spinner_thread.daemon = True
    spinner_thread.start()
    
    time.sleep(duration)
    stop_event.set()
    spinner_thread.join(timeout=0.5)
    print(" " * 70, end="\r")  # Clear the line

def draw_box(text: str, color: str = "white", padding: int = 1, width: Optional[int] = None, 
             title: str = "", style: str = "", shadow: bool = True) -> str:
    """Vẽ hộp tùy chỉnh với nhiều tùy chọn."""
    lines = text.strip().split("\n")
    if width is None:
        width = max(len(line) for line in lines) + padding * 2
    
    # Shadow effect
    shadow_char = "░" if shadow else " "
    
    # Top border with title
    if title:
        title_start = (width - len(title) - 2) // 2
        title_line = "═" * title_start + f"╣ {title} ╠" + "═" * (width - title_start - len(title) - 4)
        box = colored("╔" + title_line + "╗" + (shadow_char if shadow else ""), color, style) + "\n"
    else:
        box = colored("╔" + "═" * width + "╗" + (shadow_char if shadow else ""), color, style) + "\n"
    
    # Content
    for line in lines:
        padding_right = width - len(line) - padding
        box += colored("║" + " " * padding + line + " " * padding_right + "║" + (shadow_char if shadow else ""), color, style) + "\n"
    
    # Bottom border
    box += colored("╚" + "═" * width + "╝" + (shadow_char if shadow else ""), color, style)
    return box

def fancy_banner() -> None:
    """Hiển thị banner ứng dụng với hiệu ứng đẹp mắt."""
    os.system("clear" if os.name == "posix" else "cls")
    
    # Thêm hiệu ứng cho banner
    banner_art = """
 ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗    ██╗   ██╗██╗██████╗ 
██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝    ██║   ██║██║██╔══██╗
██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗      ██║   ██║██║██████╔╝
██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝      ╚██╗ ██╔╝██║██╔═══╝ 
╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗     ╚████╔╝ ██║██║     
 ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚═╝╚═╝     
"""
    
    # Hiển thị banner với hiệu ứng gradient
    gradient_colors = ["magenta", "purple", "blue", "cyan", "teal", "green", "lime"]
    lines = banner_art.split('\n')
    for i, line in enumerate(lines):
        color = gradient_colors[min(i, len(gradient_colors)-1)]
        print(colored(line, color, "bold"))
    
    # Thông tin phụ với hiệu ứng viền đẹp mắt
    current_time = datetime.now(tz).strftime("%H:%M:%S %d/%m/%Y")
    info = f"""
╔══════════════════════════════════════════════════════════════╗
║ {colored('🌟 SUPER VIP TOOL GOLIKE 🌟', 'gold', 'bold')}                                ║
╠══════════════════════════════════════════════════════════════╣
║ {colored('👑 Tool By: Bóng X', 'white')}             {colored(f'Phiên Bản: {VERSION} 🚀', 'lime')}           ║
╠══════════════════════════════════════════════════════════════╣
║ {colored('🆔 Tên   : 👑 BÓNG X 👑', 'cyan')}                                      ║
║ {colored('📱 Tik Tok : https://www.tiktok.com/@doanh21105', 'pink')}              ║
║ {colored('🌅 Zalo     : 🧠0865526740🧠', 'blue')}                                 ║
║ {colored('❤️‍🔥 Telegram : ⚡https://t.me/doanhvip1⚡', 'purple')}                    ║
╠══════════════════════════════════════════════════════════════╣
║ {colored('⏰ Thời gian: ' + current_time, 'teal')}                             ║
╠══════════════════════════════════════════════════════════════╣
║ {colored('⚠️ Lưu ý    : 🌟Tool Sử Dụng Cho Android🌟', 'orange')}                   ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(info)

def read_auth() -> str:
    """Đọc thông tin xác thực từ file."""
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "r", encoding="utf8") as f:
            return f.read().strip()
    return ""

def write_auth(auth: str) -> None:
    """Ghi thông tin xác thực vào file."""
    with open(AUTH_FILE, "w", encoding="utf8") as f:
        f.write(auth.strip())

def clear_auth() -> None:
    """Xóa file xác thực."""
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)
        print_success(f"Đã xóa {AUTH_FILE}!")
    else:
        print_warning(f"File {AUTH_FILE} không tồn tại!")

def print_success(message: str) -> None:
    """Hiển thị thông báo thành công."""
    print(draw_box(f"✅ {message}", "green", title="THÀNH CÔNG", style="bold", shadow=True))

def print_warning(message: str) -> None:
    """Hiển thị cảnh báo."""
    print(draw_box(f"⚠️ {message}", "yellow", title="CẢNH BÁO", style="bold", shadow=True))

def print_error(message: str) -> None:
    """Hiển thị lỗi."""
    print(draw_box(f"❌ {message}", "red", title="LỖI", style="bold", shadow=True))

def print_info(message: str) -> None:
    """Hiển thị thông tin."""
    print(draw_box(f"ℹ️ {message}", "cyan", title="THÔNG TIN", style="bold", shadow=True))

def fancy_menu() -> None:
    """Hiển thị menu với hiệu ứng đẹp mắt."""
    fancy_banner()
    
    # Thử lấy địa chỉ IP để hiển thị
    try:
        ip_response = requests.get("https://api.ipify.org", timeout=3)
        ip_address = ip_response.text if ip_response.status_code == 200 else "192.168.1.1"
    except:
        ip_address = "192.168.1.1"
    
    menu_text = f"""
{colored('🆔 Địa chỉ Ip  : 🚨' + ip_address + '🚨', 'white')}

{colored('🥇 Nhập 1', 'green')} để vào Tool Tiktok {colored('🔥', 'red')}
{colored('🥈 Nhập 2', 'red')} Để Xóa Authorization Hiện Tại {colored('⚠️', 'yellow')}
{colored('🥉 Nhập 3', 'blue')} Để Xem Thông Tin Tool {colored('ℹ️', 'cyan')}

{colored('✨ Hãy lựa chọn chức năng ✨', 'cyan', 'bold')}
"""
    
    print(draw_box(menu_text, "blue", title="MENU CHÍNH", style="bold", shadow=True))

def build_headers(auth: str) -> Dict[str, str]:
    """Tạo headers cho API requests."""
    return {
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Referer': 'https://app.golike.net/',
        'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'T': 'VFZSak1FMTZZM3BOZWtFd1RtYzlQUT09',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        "Authorization": auth,
        'Content-Type': 'application/json;charset=utf-8'
    }

def get_tiktok_accounts(headers: Dict[str, str]) -> Dict[str, Any]:
    """Lấy danh sách tài khoản TikTok."""
    try:
        stop_event = threading.Event()
        spinner_thread = threading.Thread(target=AnimationEffect.spinner, 
                                        args=(stop_event, "Đang lấy danh sách tài khoản TikTok", "magenta"))
        spinner_thread.daemon = True
        spinner_thread.start()
        
        res = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, timeout=10)
        
        stop_event.set()
        spinner_thread.join(timeout=0.5)
        print(" " * 70, end="\r")  # Clear the line
        
        return res.json()
    except Exception as e:
        print_error(f"Lỗi kết nối API: {e}")
        return {}

def get_jobs(account_id: str, headers: Dict[str, str]) -> Dict[str, Any]:
    """Lấy các công việc từ GoLike."""
    try:
        url = f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={account_id}&data=null'
        res = requests.get(url, headers=headers, timeout=10)
        return res.json()
    except Exception as e:
        print_error(f"Lỗi lấy job: {e}")
        return {}

def complete_job(ads_id: str, account_id: str, headers: Dict[str, str]) -> Dict[str, Any]:
    """Hoàn thành công việc."""
    try:
        url = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
        data = {
            "ads_id": ads_id,
            "account_id": account_id,
            "async": True,
            "data": None
        }
        
        # Hiệu ứng hoàn thành nhiệm vụ đẹp mắt
        stop_event = threading.Event()
        spinner_thread = threading.Thread(target=AnimationEffect.spinner, 
                                        args=(stop_event, "Đang hoàn thành nhiệm vụ", "green"))
        spinner_thread.daemon = True
        spinner_thread.start()
        
        res = requests.post(url, data=json.dumps(data), headers=headers, timeout=15)
        
        stop_event.set()
        spinner_thread.join(timeout=0.5)
        print(" " * 70, end="\r")  # Clear the line
        
        return res.json()
    except Exception as e:
        print_error(f"Lỗi hoàn thành job: {e}")
        return {}

def report_job(ads_id: str, object_id: str, account_id: str, job_type: str, headers: Dict[str, str]) -> None:
    """Báo cáo công việc gặp vấn đề."""
    data1 = {
        "description": "Báo cáo hoàn thành thất bại",
        "users_advertising_id": ads_id,
        "type": "ads",
        "provider": "tiktok",
        "fb_id": account_id,
        "error_type": 6
    }
    try:
        requests.post('https://gateway.golike.net/api/report/send', data=json.dumps(data1), headers=headers, timeout=8)
    except: 
        pass

    data2 = {
        "ads_id": ads_id,
        "object_id": object_id,
        "account_id": account_id,
        "type": job_type
    }
    try:
        requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', data=json.dumps(data2), headers=headers, timeout=8)
    except: 
        pass

def show_accounts(accounts: Dict[str, Any]) -> None:
    """Hiển thị danh sách tài khoản với giao diện đẹp."""
    data = accounts.get("data", [])
    if not isinstance(data, list) or not data:
        print_warning("Không có tài khoản TikTok nào!")
        return
    
    account_info = f"🆔 Danh sách {len(data)} tài khoản Tik Tok:\n\n"
    
    for idx, acc in enumerate(data, 1):
        username = acc.get('unique_username', 'N/A')
        status = "✅ Hoạt động" if acc.get('status') != 'suspended' else "❌ Bị khóa"
        account_info += f"[{idx}] 🆔 : {colored(username, 'cyan')} ♦️ : {colored(status, 'green' if '✅' in status else 'red')}\n"
    
    print(draw_box(account_info, "cyan", title="TÀI KHOẢN TIKTOK", style="bold", shadow=True))

def input_int(prompt: str, color: str = "green", minval: int = 1) -> int:
    """Nhập số nguyên với kiểm tra giá trị."""
    while True:
        value = input(colored(f"💬 {prompt}: ", color, "bold")).strip()
        if value.isdigit() and int(value) >= minval:
            return int(value)
        print_warning(f"Vui lòng nhập số nguyên >= {minval}!")

def fancy_input(prompt: str, color: str = "green") -> str:
    """Nhập dữ liệu với giao diện đẹp."""
    return input(colored(f"💬 {prompt}: ", color, "bold")).strip()

def display_stats(dem: int, now: str, status: str, job_type: str, tien: int, tong: int) -> None:
    """Hiển thị thống kê với giao diện đẹp mắt."""
    status_color = "green" if status == "success" else "red"
    
    stats = f"""
┌─────────────────────┬─────────────────────┐
│  {colored('📊 THỐNG KÊ JOB', 'gold', 'bold')}    │  {colored('💰 THỐNG KÊ XU', 'lime', 'bold')}     │
├─────────────────────┼─────────────────────┤
│  Nhiệm vụ: {colored(str(dem).ljust(7), 'cyan')} │  Xu nhận: {colored('+' + str(tien).ljust(7), 'green')} │
│  Thời gian: {colored(now.ljust(7), 'blue')} │  Tổng xu: {colored(str(tong).ljust(8), 'magenta')} │
│  Trạng thái: {colored(status.ljust(5), status_color)} │                     │
│  Loại job: {colored(job_type.ljust(7), 'yellow')} │                     │
└─────────────────────┴─────────────────────┘
"""
    print(stats)

def display_countdown(seconds: int, message: str = "Đang đợi") -> None:
    """Hiển thị đếm ngược với thanh tiến trình đẹp mắt."""
    for t in range(seconds, -1, -1):
        percent = int((seconds - t) / seconds * 100) if seconds > 0 else 100
        bar_length = 20
        filled_length = int(bar_length * (seconds - t) / seconds) if seconds > 0 else bar_length
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        
        # Màu sắc thay đổi theo thời gian
        colors = ["cyan", "blue", "purple", "magenta", "red"]
        color_idx = int(t / seconds * (len(colors)-1)) if seconds > 0 else 0
        color = colors[color_idx]
        
        # Emoji thay đổi theo thời gian
        emojis = ["⏳", "⌛", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
        emoji = emojis[t % len(emojis)]
        
        print(colored(f"\r{emoji} {message}: [{bar}] {percent}% ({t}s)  ", color), end="", flush=True)
        time.sleep(1)
    print(" " * 100, end="\r", flush=True)  # Clear the line

def show_working_menu(job_type: str, account_name: str) -> None:
    """Hiển thị menu khi đang làm việc."""
    current_time = datetime.now(tz).strftime('%H:%M:%S %d/%m/%Y')
    work_info = f"""
🔄 Đang chạy tool cho tài khoản: {colored(account_name, 'green', 'bold')}
🎯 Loại nhiệm vụ: {colored(job_type, 'yellow', 'bold')}
⏰ Thời gian bắt đầu: {colored(current_time, 'blue')}

{colored('Hệ thống đang hoạt động...', 'teal')}
{colored('Nhấn Ctrl+C để dừng tool', 'red', 'bold')}
"""
    print(draw_box(work_info, "white", title="THÔNG TIN CÔNG VIỆC", style="bold", shadow=True))

def show_about() -> None:
    """Hiển thị thông tin về tool."""
    about_text = f"""
{colored('🌟 SUPER VIP TOOL GOLIKE 🌟', 'gold', 'bold')}

{colored('Phiên bản:', 'white')} {colored(VERSION, 'green')}
{colored('Tác giả:', 'white')} {colored(AUTHOR, 'cyan')}

{colored('🔰 Tính năng:', 'yellow')}
• Tự động nhận và hoàn thành nhiệm vụ TikTok trên GoLike
• Hỗ trợ nhiều loại nhiệm vụ: Follow, Like
• Giao diện thân thiện, trực quan
• Tự động báo cáo các job lỗi
• Thống kê chi tiết về số xu kiếm được

{colored('📱 Liên hệ:', 'pink')}
• TikTok: https://www.tiktok.com/@doanh21105
• Zalo: 0865526740
• Telegram: https://t.me/doanhvip1

{colored('⚠️ Lưu ý:', 'red')}
• Tool này được thiết kế để sử dụng trên Android
• Sử dụng có trách nhiệm và tuân thủ điều khoản của GoLike
• Nhập đúng thông tin Authorization để tool hoạt động tốt
"""
    print(draw_box(about_text, "blue", title="THÔNG TIN TOOL", style="bold", shadow=True))

def show_success_animation() -> None:
    """Hiển thị hiệu ứng hoàn thành nhiệm vụ."""
    success_frames = [
        "  ✨  ",
        " ✨✨ ",
        "✨✨✨",
        "✨✨✨",
        " ✨✨ ",
        "  ✨  "
    ]
    
    for frame in success_frames:
        print(colored(f"\r{frame} JOB HOÀN THÀNH THÀNH CÔNG! {frame}", "green", "bold"), end="", flush=True)
        time.sleep(0.1)
    print()

def main() -> None:
    """Hàm chính của chương trình."""
    try:
        while True:
            fancy_menu()
            choose = fancy_input("🥇 Nhập Lựa Chọn (1, 2 hoặc 3)", "white")
            
            if choose == "2":
                clear_auth()
                continue
            elif choose == "3":
                show_about()
                input(colored("\n💬 Nhấn Enter để quay lại menu chính...", "cyan"))
                continue
            elif choose == "1":
                break
            else:
                print_warning("Lựa chọn không hợp lệ!")

        auth = read_auth()
        while not auth:
            auth = fancy_input("📢 Nhập Authorization", "green")
            if auth:
                write_auth(auth)
                loading_animation("Đang lưu Authorization", 1)
                print_success("Đã lưu Authorization thành công!")

        headers = build_headers(auth)
        loading_animation("Đang đăng nhập vào hệ thống", 2)
        print_success("Đăng nhập thành công! Đang vào Tool Tiktok...")
        time.sleep(1)
        
        # Lấy danh sách acc
        accounts = get_tiktok_accounts(headers)
        if not accounts or accounts.get("status") != 200 or not accounts.get("data"):
            print_error("Authorization hoặc T sai hoặc không có tài khoản. Hãy nhập lại!")
            clear_auth()
            input(colored("\n💬 Nhấn Enter để quay lại menu chính...", "cyan"))
            return
            
        show_accounts(accounts)
        
        # Chọn acc
        while True:
            idacc = fancy_input("☀️ Nhập ID Acc Tiktok Vào", "green")
            acc_obj = next((a for a in accounts.get("data", []) if a.get("unique_username") == idacc), None)
            if acc_obj:
                account_id = acc_obj.get("id")
                account_name = acc_obj.get("unique_username")
                break
            print_error("Acc này chưa được thêm vào golike hoặc ID sai!")
            
        # Nhập thông số job
        delay = input_int("👀 Nhập thời gian làm job (giây)")
        
        while True:
            lannhan = fancy_input("🛑 Nhận tiền lần 2 nếu lần 1 fail? (y/n)", "green").lower()
            if lannhan in {"y", "n"}:
                break
            print_warning("Nhập sai! Hãy nhập 'y' hoặc 'n'")
            
        doiacc = input_int("📆 Số job fail để đổi acc TikTok (nhập 1 nếu không muốn dừng)")
        
        job_types_menu = """
♦️ ✈ Nhập 1 : Chỉ nhận nhiệm vụ Follow
🔥 ✈ Nhập 2 : Chỉ nhận nhiệm vụ like
💥 Nhập 12 : Kết hợp cả Like và Follow
"""
        print(draw_box(job_types_menu, "yellow", title="LOẠI NHIỆM VỤ", style="bold", shadow=True))
        
        while True:
            chedo = fancy_input("✅ Chọn lựa chọn", "cyan")
            if chedo in {"1", "2", "12"}:
                break
            print_warning("Nhập sai! Hãy nhập '1', '2' hoặc '12'")
            
        lam = ["follow"] if chedo == "1" else ["like"] if chedo == "2" else ["follow", "like"]
        job_type_text = "Follow" if chedo == "1" else "Like" if chedo == "2" else "Follow & Like"

        # Bắt đầu vòng lặp làm job
        dem = tong = checkdoiacc = 0
        
        show_working_menu(job_type_text, account_name)
        
        print(draw_box("⚡ Bắt đầu chạy tool ⚡", "green", title="BẮT ĐẦU", style="bold", shadow=True))
        
        prev_job = None
        try:
            while True:
                if checkdoiacc >= doiacc:
                    show_accounts(accounts)
                    print_warning(f"Đã đạt giới hạn {doiacc} job fail liên tiếp!")
                    idacc = fancy_input("⚡ Job fail đạt giới hạn, nhập acc mới", "red")
                    acc_obj = next((a for a in accounts.get("data", []) if a.get("unique_username") == idacc), None)
                    if acc_obj:
                        account_id = acc_obj.get("id")
                        account_name = acc_obj.get("unique_username")
                        checkdoiacc = 0
                        show_working_menu(job_type_text, account_name)
                    else:
                        print_error("Acc này chưa được thêm vào golike hoặc ID sai")
                        continue
                        
                # Nhận job
                loading_animation("Đang tìm nhiệm vụ mới", 1, "pink")
                nhanjob = get_jobs(account_id, headers)
                
                if not nhanjob or not nhanjob.get("data"):
                    print_warning("Không tìm thấy nhiệm vụ, đang thử lại sau 10 giây...")
                    display_countdown(10, "Đợi tìm nhiệm vụ mới")
                    continue
                    
                # Check job trùng
                if prev_job and prev_job.get("data", {}).get("link") == nhanjob.get("data", {}).get("link") and prev_job.get("data", {}).get("type") == nhanjob.get("data", {}).get("type"):
                    print_warning("Job trùng với job trước đó - Bỏ qua!")
                    time.sleep(2)
                    if nhanjob.get("data"):
                        report_job(nhanjob["data"].get("id"), nhanjob["data"].get("object_id"), account_id, nhanjob["data"].get("type"), headers)
                    continue
                    
                prev_job = nhanjob
                
                if nhanjob.get("status") == 200:
                    data = nhanjob["data"]
                    ads_id = data.get("id")
                    link = data.get("link")
                    object_id = data.get("object_id")
                    job_type = data.get("type")
                    
                    if not link:
                        print_warning("Job die - Không có link!")
                        time.sleep(2)
                        report_job(ads_id, object_id, account_id, job_type, headers)
                        continue
                        
                    if job_type not in lam:
                        report_job(ads_id, object_id, account_id, job_type, headers)
                        print_warning(f"Đã bỏ qua job {job_type}!")
                        time.sleep(1)
                        continue
                        
                    # Mở link (nếu chạy trên Termux Android, nếu không hãy mở tay)
                    opened = False
                    try:
                        code = os.system(f"termux-open-url {link}")
                        if code == 0:
                            opened = True
                    except:
                        pass
                        
                    if not opened:
                        link_info = f"📱 Vui lòng mở link thủ công:\n\n{colored(link, 'blue', 'underline')}"
                        print(draw_box(link_info, "yellow", title="MỞ LINK", style="bold", shadow=True))
                    else:
                        print_success(f"Đã mở link: {link[:50]}...")
                    
                    # Đếm ngược thời gian
                    display_countdown(delay, "Đang thực hiện nhiệm vụ")
                    
                    # Nhận tiền
                    ok = False
                    for lan in range(1, 3 if lannhan == "y" else 2):
                        if lan > 1:
                            loading_animation("Đang nhận tiền lần 2", 1, "pink")
                            
                        nhantien = complete_job(ads_id, account_id, headers)
                        
                        if nhantien.get("status") == 200:
                            ok = True
                            dem += 1
                            tien = nhantien["data"].get("prices", 0)
                            tong += tien
                            now = datetime.now(tz).strftime("%H:%M:%S")
                            
                            display_stats(dem, now, "success", nhantien['data'].get('type', ''), tien, tong)
                            
                            # Hiệu ứng ngẫu nhiên khi hoàn thành job thành công
                            show_success_animation()
                            success_messages = [
                                "🎉 Hoàn thành nhiệm vụ thành công! 🎉",
                                "💰 Đã nhận xu thành công! 💰",
                                "✅ Nhiệm vụ hoàn tất, xu đã về ví! ✅",
                                "🚀 Thêm một nhiệm vụ thành công! 🚀",
                                "💎 Xu đã được cộng vào tài khoản! 💎"
                            ]
                            print_success(random.choice(success_messages))
                            
                            checkdoiacc = 0
                            break
                        elif lan == 2:
                            break
                            
                    if not ok:
                        report_job(ads_id, object_id, account_id, job_type, headers)
                        print_error(f"Nhiệm vụ thất bại - Đã bỏ qua!")
                        time.sleep(1)
                        checkdoiacc += 1
                else:
                    print_warning("Không tìm thấy nhiệm vụ phù hợp, đợi 10 giây...")
                    display_countdown(10, "Đợi tìm nhiệm vụ mới")
        except KeyboardInterrupt:
            print("\n")
            print_info(f"Đã dừng tool! Tổng cộng: {dem} nhiệm vụ, {tong} xu")
            time.sleep(1)
            input(colored("\n💬 Nhấn Enter để quay lại menu chính...", "cyan"))
            main()  # Quay lại menu chính
    except Exception as e:
        print_error(f"Đã xảy ra lỗi không mong muốn: {e}")
        time.sleep(2)
        main()  # Quay lại menu chính khi có lỗi
        
if __name__ == "__main__":
    main()