import json
import os, time
import cloudscraper
import requests
import socket
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys
import base64
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.rule import Rule
from rich import box
from rich.tree import Tree
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.status import Status
import threading

# Khởi tạo Rich Console
console = Console()

def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        console.print(Panel(
            "[bold red]⚠️ Mạng không ổn định hoặc bị mất kết nối!\n[white]Vui lòng kiểm tra lại kết nối mạng của bạn.",
            title="[bold red]🔴 LỖI MẠNG",
            title_align="center",
            border_style="red",
            padding=(1, 2)
        ))
        return False

def hien_thi_banner():
    """Hiển thị banner với Rich"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII Art với gradient màu
    ascii_art = """
██████╗  ██████╗ ███╗   ██╗ ██████╗     ██╗  ██╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝     ╚██╗██╔╝
██████╔╝██║   ██║██╔██╗ ██║██║  ███╗     ╚███╔╝ 
██╔══██╗██║   ██║██║╚██╗██║██║   ██║     ██╔██╗ 
██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝    ██╔╝ ██╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝
    """
    
    # Tạo panel chính cho banner
    banner_text = Text()
    banner_text.append(ascii_art, style="bold cyan")
    banner_text.append("\n\n")
    banner_text.append("🔥 GOLIKE AUTO TIKTOK - PHIÊN BẢN VIP 🔥", style="bold yellow")
    banner_text.append("\n")
    banner_text.append("👨‍💻 Admin: Trần Đức Doanh", style="bold green")
    banner_text.append(" | ", style="white")
    banner_text.append("📱 Telegram: @doanhvip1", style="bold blue")
    banner_text.append("\n")
    banner_text.append("🌐 Telegram: https://t.me/doanhvip1", style="bold magenta")
    banner_text.append("\n")
    banner_text.append(f"📅 Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", style="bold white")
    
    # Tạo panel với hiệu ứng đẹp
    banner_panel = Panel(
        Align.center(banner_text),
        title="[bold red]🚀 TOOL AUTO GOLIKE PREMIUM 🚀",
        title_align="center",
        border_style="bright_cyan",
        box=box.DOUBLE_EDGE,
        padding=(1, 2)
    )
    
    console.print(banner_panel)
    console.print()

def tao_panel_dang_nhap():
    """Tạo panel đăng nhập đẹp"""
    login_panel = Panel(
        Text("🔐 ĐĂNG NHẬP HỆ THỐNG GOLIKE", justify="center", style="bold yellow"),
        title="[bold green]⚡ AUTHENTICATION ⚡",
        title_align="center",
        border_style="green",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(login_panel)

def doc_file_auth():
    """Đọc file Authorization và Token an toàn"""
    try:
        # Tạo file nếu chưa tồn tại
        if not os.path.exists("Authorization.txt"):
            with open("Authorization.txt", "w", encoding='utf-8') as f:
                f.write("")
        
        if not os.path.exists("token.txt"):
            with open("token.txt", "w", encoding='utf-8') as f:
                f.write("")
        
        # Đọc nội dung file
        with open("Authorization.txt", "r", encoding='utf-8') as f:
            author = f.read().strip()
        
        with open("token.txt", "r", encoding='utf-8') as f:
            token = f.read().strip()
            
        return author, token
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Lỗi đọc file: {str(e)}\n[white]Sẽ tạo file mới...",
            title="[bold red]🚫 LỖI FILE",
            border_style="red"
        ))
        return "", ""

def ghi_file_auth(author, token):
    """Ghi file Authorization và Token an toàn"""
    try:
        with open("Authorization.txt", "w", encoding='utf-8') as f:
            f.write(author.strip())
        
        with open("token.txt", "w", encoding='utf-8') as f:
            f.write(token.strip())
        
        return True
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Lỗi ghi file: {str(e)}",
            title="[bold red]🚫 LỖI GHI FILE",
            border_style="red"
        ))
        return False

def lay_thong_tin_dang_nhap():
    """Lấy thông tin đăng nhập với giao diện đẹp và xử lý lỗi"""
    author, token = doc_file_auth()
    
    if not author or not token:
        with Status("[bold green]Đang chuẩn bị form đăng nhập...", spinner="dots"):
            time.sleep(1)
        
        console.print(Panel(
            "[bold cyan]📝 Vui lòng nhập thông tin đăng nhập của bạn:\n"
            "[bold yellow]💡 Hướng dẫn lấy Authorization và Token:\n"
            "[white]1. Đăng nhập vào app.golike.net\n"
            "[white]2. Mở Developer Tools (F12)\n"
            "[white]3. Vào tab Network > F5 reload trang\n"
            "[white]4. Tìm request có chứa Authorization trong Headers\n"
            "[white]5. Copy giá trị Authorization và t (Token)",
            title="[bold yellow]🔑 THÔNG TIN ĐĂNG NHẬP",
            border_style="yellow",
            padding=(1, 2)
        ))
        
        while True:
            try:
                author = Prompt.ask("[bold green]🔐 Nhập AUTHORIZATION", 
                                  default="",
                                  show_default=False).strip()
                
                if not author:
                    console.print("[bold red]❌ Authorization không được để trống!")
                    continue
                
                if not author.startswith('Bearer '):
                    console.print("[bold yellow]⚠️ Authorization thường bắt đầu bằng 'Bearer '")
                    xac_nhan = Confirm.ask("[bold blue]🤔 Bạn có chắc chắn đây là Authorization đúng?")
                    if not xac_nhan:
                        continue
                
                token = Prompt.ask("[bold green]🎯 Nhập T (Token)", 
                                 default="",
                                 show_default=False).strip()
                
                if not token:
                    console.print("[bold red]❌ Token không được để trống!")
                    continue
                
                break
                
            except KeyboardInterrupt:
                console.print(Panel(
                    "[bold red]👋 Đã hủy đăng nhập!",
                    title="[bold yellow]🛑 DỪNG",
                    border_style="red"
                ))
                sys.exit(0)
            except Exception as e:
                console.print(f"[bold red]❌ Lỗi nhập liệu: {str(e)}")
                continue
        
        # Lưu thông tin đăng nhập
        if ghi_file_auth(author, token):
            console.print(Panel(
                "[bold green]✅ Đã lưu thông tin đăng nhập thành công!",
                title="[bold green]🎉 THÀNH CÔNG",
                border_style="green"
            ))
        else:
            console.print(Panel(
                "[bold red]❌ Không thể lưu thông tin đăng nhập!\n"
                "[white]Tool vẫn sẽ chạy với thông tin vừa nhập.",
                title="[bold yellow]⚠️ CẢNH BÁO",
                border_style="yellow"
            ))
            
    else:
        console.print(Panel(
            f"[bold green]✅ Đã tìm thấy thông tin đăng nhập!\n"
            f"[bold blue]Authorization: [white]{author[:20]}...\n"
            f"[bold blue]Token: [white]{token[:10]}...",
            title="[bold blue]💾 THÔNG TIN CŨ",
            border_style="blue"
        ))
        
        try:
            select = Prompt.ask(
                "[bold green]🔄 Nhấn [Enter] để tiếp tục hoặc nhập '1' để thay đổi tài khoản",
                default="",
                choices=["", "1"],
                show_choices=False
            )
            
            if select == "1":
                console.print(Panel(
                    "[bold cyan]🔄 Thay đổi thông tin đăng nhập:",
                    title="[bold yellow]🔑 ĐĂNG NHẬP MỚI",
                    border_style="yellow"
                ))
                
                while True:
                    try:
                        author = Prompt.ask("[bold green]🔐 Nhập AUTHORIZATION mới", 
                                          default="",
                                          show_default=False).strip()
                        
                        if not author:
                            console.print("[bold red]❌ Authorization không được để trống!")
                            continue
                        
                        token = Prompt.ask("[bold green]🎯 Nhập T (Token) mới", 
                                         default="",
                                         show_default=False).strip()
                        
                        if not token:
                            console.print("[bold red]❌ Token không được để trống!")
                            continue
                        
                        break
                        
                    except KeyboardInterrupt:
                        console.print(Panel(
                            "[bold red]👋 Đã hủy thay đổi!",
                            title="[bold yellow]🛑 DỪNG",
                            border_style="red"
                        ))
                        return author, token  # Trả về thông tin cũ
                
                # Lưu thông tin mới
                if ghi_file_auth(author, token):
                    console.print(Panel(
                        "[bold green]✅ Đã cập nhật thông tin đăng nhập!",
                        title="[bold green]🎉 CẬP NHẬT THÀNH CÔNG",
                        border_style="green"
                    ))
                    
        except KeyboardInterrupt:
            console.print(Panel(
                "[bold red]👋 Đã hủy thao tác!",
                title="[bold yellow]🛑 DỪNG",
                border_style="red"
            ))
            sys.exit(0)
    
    return author, token

def kiem_tra_thong_tin_dang_nhap(headers, scraper):
    """Kiểm tra thông tin đăng nhập có hợp lệ không"""
    try:
        with Status("[bold green]🔍 Đang kiểm tra thông tin đăng nhập...", spinner="dots"):
            response = scraper.get(
                'https://gateway.golike.net/api/tiktok-account',
                headers=headers,
                json={},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == 200:
                    console.print(Panel(
                        "[bold green]✅ Thông tin đăng nhập hợp lệ!",
                        title="[bold green]🎉 XÁC THỰC THÀNH CÔNG",
                        border_style="green"
                    ))
                    return True, data
                else:
                    console.print(Panel(
                        f"[bold red]❌ Lỗi API: {data.get('message', 'Không xác định')}\n"
                        f"[white]Status code: {data.get('status', 'N/A')}",
                        title="[bold red]🚫 LỖI API",
                        border_style="red"
                    ))
                    return False, None
            else:
                console.print(Panel(
                    f"[bold red]❌ Lỗi HTTP: {response.status_code}\n"
                    f"[white]Response: {response.text[:100]}...",
                    title="[bold red]🚫 LỖI HTTP",
                    border_style="red"
                ))
                return False, None
                
    except requests.exceptions.Timeout:
        console.print(Panel(
            "[bold red]❌ Kết nối timeout!\n[white]Vui lòng kiểm tra mạng và thử lại.",
            title="[bold red]⏰ TIMEOUT",
            border_style="red"
        ))
        return False, None
    except requests.exceptions.ConnectionError:
        console.print(Panel(
            "[bold red]❌ Không thể kết nối đến server!\n[white]Vui lòng kiểm tra kết nối mạng.",
            title="[bold red]🌐 LỖI KẾT NỐI",
            border_style="red"
        ))
        return False, None
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Lỗi không xác định: {str(e)}",
            title="[bold red]🚫 LỖI HỆ THỐNG",
            border_style="red"
        ))
        return False, None

def hien_thi_danh_sach_acc(chontktiktok):
    """Hiển thị danh sách tài khoản với Rich Table"""
    if chontktiktok.get("status") != 200:
        console.print(Panel(
            "[bold red]❌ Authorization hoặc Token không hợp lệ!\n"
            "[white]Vui lòng kiểm tra lại thông tin đăng nhập.\n"
            "[yellow]💡 Có thể do:\n"
            "[white]- Authorization/Token đã hết hạn\n"
            "[white]- Sai định dạng Authorization/Token\n"
            "[white]- Tài khoản bị khóa/hạn chế",
            title="[bold red]🚫 LỖI XÁC THỰC",
            border_style="red",
            padding=(1, 2)
        ))
        
        # Hỏi người dùng có muốn nhập lại không
        try:
            nhap_lai = Confirm.ask("[bold blue]🔄 Bạn có muốn nhập lại thông tin đăng nhập?")
            if nhap_lai:
                # Xóa file cũ để nhập lại
                try:
                    if os.path.exists("Authorization.txt"):
                        os.remove("Authorization.txt")
                    if os.path.exists("token.txt"):
                        os.remove("token.txt")
                except:
                    pass
                
                console.print(Panel(
                    "[bold green]🔄 Đã xóa thông tin cũ. Vui lòng khởi động lại tool!",
                    title="[bold green]✅ THÀNH CÔNG",
                    border_style="green"
                ))
        except KeyboardInterrupt:
            pass
            
        sys.exit(1)
    
    # Tạo bảng đẹp cho danh sách tài khoản
    table = Table(
        title="[bold cyan]📱 DANH SÁCH TÀI KHOẢN TIKTOK",
        title_style="bold cyan",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        border_style="bright_blue"
    )
    
    table.add_column("STT", justify="center", style="bold yellow", width=8)
    table.add_column("👤 Nickname", justify="left", style="bold green", width=25)
    table.add_column("📊 Trạng thái", justify="center", style="bold cyan", width=15)
    table.add_column("🎯 ID", justify="center", style="dim white", width=12)
    
    for i in range(len(chontktiktok["data"])):
        table.add_row(
            f"[bold yellow]{i+1}[/bold yellow]",
            f"[bold green]{chontktiktok['data'][i]['nickname']}[/bold green]",
            "[bold green]🟢 Hoạt động[/bold green]",
            f"[dim]{chontktiktok['data'][i]['id']}[/dim]"
        )
    
    console.print(table)
    console.print()

def chon_loai_nhiem_vu():
    """Chọn loại nhiệm vụ với giao diện đẹp"""
    console.print(Panel(
        Text("🎯 CHỌN LOẠI NHIỆM VỤ", justify="center", style="bold yellow"),
        title="[bold green]⚙️ CÀI ĐẶT NHIỆM VỤ ⚙️",
        border_style="green",
        box=box.ROUNDED
    ))
    
    # Tạo menu với Rich
    menu_table = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    menu_table.add_column(style="bold cyan", width=5)
    menu_table.add_column(style="bold green", width=30)
    
    menu_table.add_row("[1]", "👥 Follow")
    menu_table.add_row("[2]", "❤️ Like")
    menu_table.add_row("[3]", "🔥 Cả hai (Follow + Like)")
    
    console.print(menu_table)
    console.print()
    
    while True:
        try:
            loai_nhiem_vu = IntPrompt.ask("[bold green]🎯 Chọn loại nhiệm vụ", choices=["1", "2", "3"])
            return loai_nhiem_vu
        except KeyboardInterrupt:
            console.print(Panel(
                "[bold red]👋 Đã hủy chọn nhiệm vụ!",
                title="[bold yellow]🛑 DỪNG",
                border_style="red"
            ))
            sys.exit(0)
        except:
            console.print("[bold red]❌ Vui lòng chọn số từ 1 đến 3!")

def cau_hinh_adb(loai_nhiem_vu):
    """Cấu hình ADB với giao diện đẹp"""
    console.print(Panel(
        Text("🤖 CẤU HÌNH ADB TỰ ĐỘNG", justify="center", style="bold yellow"),
        title="[bold blue]📱 AUTOMATION SETUP 📱",
        border_style="blue"
    ))
    
    try:
        adb_choice = Prompt.ask(
            "[bold green]🚀 Bạn có muốn sử dụng ADB tự động không?",
            choices=["1", "2"],
            default="2"
        )
        
        if adb_choice == "1":
            return setup_adb_advanced(loai_nhiem_vu)
        else:
            return None, None, None, None, False
            
    except KeyboardInterrupt:
        console.print(Panel(
            "[bold red]👋 Đã hủy cấu hình ADB!",
            title="[bold yellow]🛑 DỪNG",
            border_style="red"
        ))
        return None, None, None, None, False

def setup_adb_advanced(loai_nhiem_vu):
    """Setup ADB với giao diện nâng cao"""
    with Status("[bold green]🔧 Đang chuẩn bị cấu hình ADB...", spinner="dots"):
        time.sleep(1)
    
    config_file = "adb_config.txt"
    like_coords_file = "toa_do_tim.txt"
    follow_coords_file = "toa_do_follow.txt"
    
    try:
        # Panel nhập thông tin ADB
        console.print(Panel(
            "[bold cyan]📱 Nhập thông tin kết nối thiết bị Android",
            title="[bold yellow]🔗 KẾT NỐI THIẾT BỊ",
            border_style="yellow"
        ))
        
        ip = Prompt.ask("[bold green]🌐 IP của thiết bị", default="192.168.1.2")
        adb_port = Prompt.ask("[bold green]🔌 Port ADB", default="39327")
        
        # Kiểm tra tọa độ có sẵn
        x_like, y_like, x_follow, y_follow = None, None, None, None
        
        if os.path.exists(like_coords_file):
            try:
                with open(like_coords_file, "r", encoding='utf-8') as f:
                    coords = f.read().strip().split("|")
                    if len(coords) == 2:
                        x_like, y_like = coords
                        console.print(f"[bold green]✅ Đã tìm thấy tọa độ nút tim: X={x_like}, Y={y_like}")
            except:
                pass
        
        if os.path.exists(follow_coords_file):
            try:
                with open(follow_coords_file, "r", encoding='utf-8') as f:
                    coords = f.read().strip().split("|")
                    if len(coords) == 2:
                        x_follow, y_follow = coords
                        console.print(f"[bold green]✅ Đã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
            except:
                pass
        
        # Cấu hình ghép nối lần đầu
        if not os.path.exists(config_file):
            console.print(Panel(
                "[bold yellow]🔐 Lần đầu chạy, cần nhập thông tin ghép nối",
                title="[bold red]⚠️ THIẾT LẬP ĐẦU TIÊN",
                border_style="red"
            ))
            
            pair_code = Prompt.ask("[bold green]🔑 Mã ghép nối (6 số)", default="322763")
            pair_port = Prompt.ask("[bold green]🔌 Port ghép nối", default="44832")
            
            try:
                with open(config_file, "w", encoding='utf-8') as f:
                    f.write(f"{pair_code}|{pair_port}")
            except:
                console.print("[bold yellow]⚠️ Không thể lưu cấu hình ADB")
        else:
            try:
                with open(config_file, "r", encoding='utf-8') as f:
                    pair_code, pair_port = [s.strip() for s in f.read().split("|")]
            except:
                pair_code = Prompt.ask("[bold green]🔑 Mã ghép nối (6 số)", default="322763")
                pair_port = Prompt.ask("[bold green]🔌 Port ghép nối", default="44832")
        
        # Kết nối ADB với progress bar
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
        ) as progress:
            task1 = progress.add_task("🔗 Đang ghép nối với thiết bị...", total=100)
            os.system(f"adb pair {ip}:{pair_port} {pair_code} > /dev/null 2>&1")
            progress.update(task1, advance=50)
            time.sleep(2)
            
            task2 = progress.add_task("📱 Đang kết nối ADB...", total=100)
            os.system(f"adb connect {ip}:{adb_port} > /dev/null 2>&1")
            progress.update(task2, advance=50)
            time.sleep(2)
            progress.update(task1, completed=100)
            progress.update(task2, completed=100)
        
        # Kiểm tra kết nối
        devices = os.popen("adb devices").read()
        if ip not in devices:
            console.print(Panel(
                "[bold red]❌ Kết nối ADB thất bại!\n[white]Vui lòng kiểm tra lại IP, Port và mã ghép nối.",
                title="[bold red]🚫 LỖI KẾT NỐI",
                border_style="red"
            ))
            return None, None, None, None, False
        else:
            console.print(Panel(
                "[bold green]✅ Kết nối ADB thành công!",
                title="[bold green]🎉 THÀNH CÔNG",
                border_style="green"
            ))
        
        # Nhập tọa độ nếu cần
        if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
            console.print(Panel(
                "[bold cyan]📍 Nhập tọa độ nút Follow",
                title="[bold yellow]🎯 THIẾT LẬP TỌA ĐỘ",
                border_style="yellow"
            ))
            x_follow = Prompt.ask("[bold green]📍 Tọa độ X của nút follow")
            y_follow = Prompt.ask("[bold green]📍 Tọa độ Y của nút follow")
            try:
                with open(follow_coords_file, "w", encoding='utf-8') as f:
                    f.write(f"{x_follow}|{y_follow}")
            except:
                console.print("[bold yellow]⚠️ Không thể lưu tọa độ follow")
        
        if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
            console.print(Panel(
                "[bold cyan]📍 Nhập tọa độ nút Tim",
                title="[bold yellow]❤️ THIẾT LẬP TỌA ĐỘ",
                border_style="yellow"
            ))
            x_like = Prompt.ask("[bold green]📍 Tọa độ X của nút tim")
            y_like = Prompt.ask("[bold green]📍 Tọa độ Y của nút tim")
            try:
                with open(like_coords_file, "w", encoding='utf-8') as f:
                    f.write(f"{x_like}|{y_like}")
            except:
                console.print("[bold yellow]⚠️ Không thể lưu tọa độ like")
        
        return x_like, y_like, x_follow, y_follow, True
        
    except KeyboardInterrupt:
        console.print(Panel(
            "[bold red]👋 Đã hủy cấu hình ADB!",
            title="[bold yellow]🛑 DỪNG",
            border_style="red"
        ))
        return None, None, None, None, False
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Lỗi cấu hình ADB: {str(e)}",
            title="[bold red]🚫 LỖI",
            border_style="red"
        ))
        return None, None, None, None, False

def tao_bang_ket_qua():
    """Tạo bảng hiển thị kết quả với Rich Table"""
    table = Table(
        title="[bold cyan]📊 KẾT QUẢ THỰC HIỆN NHIỆM VỤ",
        title_style="bold cyan",
        box=box.DOUBLE_EDGE,
        show_header=True,
        header_style="bold magenta",
        border_style="bright_green"
    )
    
    table.add_column("STT", justify="center", style="bold yellow", width=6)
    table.add_column("🕐 Thời gian", justify="center", style="bold blue", width=12)
    table.add_column("📊 Trạng thái", justify="center", style="bold green", width=12)
    table.add_column("🎯 Loại job", justify="center", style="bold cyan", width=10)
    table.add_column("👤 ID Acc", justify="center", style="bold white", width=10)
    table.add_column("💰 Xu", justify="center", style="bold yellow", width=8)
    table.add_column("📈 Tổng", justify="center", style="bold magenta", width=10)
    
    return table

def main():
    """Hàm chính với giao diện Rich đẹp"""
    try:
        # Kiểm tra mạng
        if not kiem_tra_mang():
            return
        
        scraper = cloudscraper.create_scraper()
        
        # Hiển thị banner
        hien_thi_banner()
        
        # Đăng nhập với xử lý lỗi tốt hơn
        tao_panel_dang_nhap()
        
        # Lặp lại cho đến khi đăng nhập thành công
        while True:
            author, token = lay_thong_tin_dang_nhap()
            
            # Tạo headers
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json;charset=utf-8',
                'Authorization': author,
                't': token,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'Referer': 'https://app.golike.net/account/manager/tiktok',
            }
            
            # Kiểm tra thông tin đăng nhập
            login_success, chontktiktok = kiem_tra_thong_tin_dang_nhap(headers, scraper)
            
            if login_success:
                break
            else:
                # Xóa thông tin đăng nhập cũ và yêu cầu nhập lại
                try:
                    if os.path.exists("Authorization.txt"):
                        os.remove("Authorization.txt")
                    if os.path.exists("token.txt"):
                        os.remove("token.txt")
                except:
                    pass
                
                console.print(Panel(
                    "[bold yellow]🔄 Vui lòng nhập lại thông tin đăng nhập!",
                    title="[bold red]❌ ĐĂNG NHẬP THẤT BẠI",
                    border_style="red"
                ))
                
                try:
                    tiep_tuc = Confirm.ask("[bold blue]🤔 Bạn có muốn thử lại?")
                    if not tiep_tuc:
                        console.print(Panel(
                            "[bold red]👋 Tạm biệt! Cảm ơn bạn đã sử dụng tool.",
                            title="[bold yellow]🛑 THOÁT",
                            border_style="yellow"
                        ))
                        sys.exit(0)
                except KeyboardInterrupt:
                    sys.exit(0)
        
        # Các hàm xử lý API
        def chonacc():
            json_data = {}
            response = scraper.get(
                'https://gateway.golike.net/api/tiktok-account',
                headers=headers,
                json=json_data
            ).json()
            return response
        
        def nhannv(account_id):
            try:
                params = {
                    'account_id': account_id,
                    'data': 'null',
                }
                response = scraper.get(
                    'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
                    headers=headers,
                    params=params,
                    json={}
                )
                return response.json()
            except Exception as e:
                return {}
        
        def hoanthanh(ads_id, account_id):
            try:
                json_data = {
                    'ads_id': ads_id,
                    'account_id': account_id,
                    'async': True,
                    'data': None,
                }
                response = scraper.post(
                    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                    headers=headers,
                    json=json_data,
                    timeout=6
                )
                return response.json()
            except Exception as e:
                return {}
        
        def baoloi(ads_id, object_id, account_id, loai):
            try:
                json_data1 = {
                    'description': 'Tôi đã làm Job này rồi',
                    'users_advertising_id': ads_id,
                    'type': 'ads',
                    'provider': 'tiktok',
                    'fb_id': account_id,
                    'error_type': 6,
                }
                scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
                json_data2 = {
                    'ads_id': ads_id,
                    'object_id': object_id,
                    'account_id': account_id,
                    'type': loai,
                }
                scraper.post(
                    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                    headers=headers,
                    json=json_data2,
                )
            except Exception as e:
                pass
        
        # Hiển thị danh sách tài khoản
        os.system('cls' if os.name == 'nt' else 'clear')
        hien_thi_banner()
        hien_thi_danh_sach_acc(chontktiktok)
        
        # Chọn tài khoản
        while True:
            try:
                luachon = IntPrompt.ask(
                    "[bold green]🎯 Chọn tài khoản TIKTOK",
                    choices=[str(i+1) for i in range(len(chontktiktok["data"]))]
                )
                account_id = chontktiktok["data"][luachon - 1]["id"]
                break
            except KeyboardInterrupt:
                console.print(Panel(
                    "[bold red]👋 Đã hủy chọn tài khoản!",
                    title="[bold yellow]🛑 DỪNG",
                    border_style="red"
                ))
                sys.exit(0)
            except:
                console.print("[bold red]❌ Lựa chọn không hợp lệ!")
        
        # Cài đặt delay và số lần thất bại
        try:
            delay = IntPrompt.ask("[bold green]⏱️ Delay (giây)", default=10)
            doiacc = IntPrompt.ask("[bold green]🔄 Thất bại bao nhiêu lần thì đổi acc", default=5)
        except KeyboardInterrupt:
            console.print(Panel(
                "[bold red]👋 Đã hủy cài đặt!",
                title="[bold yellow]🛑 DỪNG",
                border_style="red"
            ))
            sys.exit(0)
        
        # Chọn loại nhiệm vụ
        loai_nhiem_vu = chon_loai_nhiem_vu()
        
        # Cấu hình ADB
        x_like, y_like, x_follow, y_follow, adb_enabled = cau_hinh_adb(loai_nhiem_vu)
        
        # Bắt đầu chạy tool
        os.system('cls' if os.name == 'nt' else 'clear')
        hien_thi_banner()
        
        # Hiển thị thông tin cấu hình
        config_info = Table(box=box.ROUNDED, title="[bold cyan]⚙️ THÔNG TIN CẤU HÌNH", title_style="bold cyan")
        config_info.add_column("Tham số", style="bold yellow", width=20)
        config_info.add_column("Giá trị", style="bold green", width=30)
        
        config_info.add_row("👤 Tài khoản", chontktiktok["data"][luachon-1]["nickname"])
        config_info.add_row("⏱️ Delay", f"{delay} giây")
        config_info.add_row("🔄 Đổi acc sau", f"{doiacc} lần lỗi")
        
        if loai_nhiem_vu == 1:
            loai_text = "👥 Follow"
        elif loai_nhiem_vu == 2:
            loai_text = "❤️ Like"
        else:
            loai_text = "🔥 Follow + Like"
        
        config_info.add_row("🎯 Loại nhiệm vụ", loai_text)
        config_info.add_row("🤖 ADB", "✅ Bật" if adb_enabled else "❌ Tắt")
        
        console.print(config_info)
        console.print()
        
        # Tạo bảng kết quả
        result_table = tao_bang_ket_qua()
        console.print(result_table)
        
        # Biến đếm
        dem = 0
        tong = 0
        checkdoiacc = 0
        dsaccloi = []
        
        # Vòng lặp chính
        while True:
            if checkdoiacc == doiacc:
                dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
                
                console.print(Panel(
                    f"[bold red]⚠️ Tài khoản {dsaccloi[-1]} gặp vấn đề!\n[white]Đang chuyển sang tài khoản khác...",
                    title="[bold red]🔄 CHUYỂN TÀI KHOẢN",
                    border_style="red"
                ))
                
                hien_thi_danh_sach_acc(chontktiktok)
                
                while True:
                    try:
                        luachon = IntPrompt.ask(
                            "[bold green]🎯 Chọn tài khoản mới",
                            choices=[str(i+1) for i in range(len(chontktiktok["data"]))]
                        )
                        account_id = chontktiktok["data"][luachon - 1]["id"]
                        checkdoiacc = 0
                        os.system('cls' if os.name == 'nt' else 'clear')
                        hien_thi_banner()
                        break
                    except KeyboardInterrupt:
                        console.print(Panel(
                            "[bold red]👋 Tool đã dừng!",
                            title="[bold yellow]🛑 DỪNG",
                            border_style="red"
                        ))
                        sys.exit(0)
                    except:
                        console.print("[bold red]❌ Lựa chọn không hợp lệ!")
            
            # Tìm nhiệm vụ
            with Status("[bold cyan]🔍 Đang tìm nhiệm vụ...", spinner="dots") as status:
                max_retries = 3
                retry_count = 0
                nhanjob = None
                
                while retry_count < max_retries:
                    try:
                        nhanjob = nhannv(account_id)
                        if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                            break
                        else:
                            retry_count += 1
                            time.sleep(2)
                    except Exception as e:
                        retry_count += 1
                        time.sleep(1)
            
            if not nhanjob or retry_count >= max_retries:
                time.sleep(1)
                continue
            
            ads_id = nhanjob["data"]["id"]
            link = nhanjob["data"]["link"]
            object_id = nhanjob["data"]["object_id"]
            job_type = nhanjob["data"]["type"]
            
            # Kiểm tra loại nhiệm vụ
            if (loai_nhiem_vu == 1 and job_type != "follow") or \
               (loai_nhiem_vu == 2 and job_type != "like") or \
               (job_type not in ["follow", "like"]):
                baoloi(ads_id, object_id, account_id, job_type)
                continue
            
            # Mở link
            try:
                if adb_enabled:
                    os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
                else:
                    subprocess.run(["termux-open-url", link])
                
                with Status("[bold blue]🌐 Đang mở liên kết...", spinner="dots"):
                    time.sleep(3)
                    
            except Exception as e:
                baoloi(ads_id, object_id, account_id, job_type)
                continue
            
            # Thực hiện thao tác ADB
            if adb_enabled:
                if job_type == "like" and x_like and y_like:
                    os.system(f"adb shell input tap {x_like} {y_like}")
                    with Status("[bold red]❤️ Đang thực hiện Like...", spinner="hearts"):
                        time.sleep(1)
                elif job_type == "follow" and x_follow and y_follow:
                    os.system(f"adb shell input tap {x_follow} {y_follow}")
                    with Status("[bold blue]👥 Đang thực hiện Follow...", spinner="dots"):
                        time.sleep(1)
            
            # Đếm ngược delay với progress bar
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]{task.description}"),
                BarColumn(complete_style="green", finished_style="bold green"),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
            ) as progress:
                task = progress.add_task(f"⏳ Đang chờ delay...", total=delay)
                for i in range(delay):
                    progress.update(task, advance=1)
                    time.sleep(1)
            
            # Hoàn thành job
            with Status("[bold green]💰 Đang nhận tiền...", spinner="dots"):
                max_attempts = 2
                attempts = 0
                nhantien = None
                
                while attempts < max_attempts:
                    try:
                        nhantien = hoanthanh(ads_id, account_id)
                        if nhantien and nhantien.get("status") == 200:
                            break
                    except:
                        pass
                    attempts += 1
            
            # Xử lý kết quả
            if nhantien and nhantien.get("status") == 200:
                dem += 1
                tien = nhantien["data"]["prices"]
                tong += tien
                
                local_time = time.localtime()
                time_str = time.strftime("%H:%M:%S", local_time)
                
                # Thêm dòng mới vào bảng
                result_table.add_row(
                    f"[bold yellow]{dem}[/bold yellow]",
                    f"[bold blue]{time_str}[/bold blue]",
                    "[bold green]✅ Success[/bold green]",
                    f"[bold cyan]{job_type}[/bold cyan]",
                    "[bold white]***[/bold white]",
                    f"[bold yellow]+{tien}[/bold yellow]",
                    f"[bold magenta]{tong}[/bold magenta]"
                )
                
                # In lại bảng
                os.system('cls' if os.name == 'nt' else 'clear')
                hien_thi_banner()
                console.print(config_info)
                console.print()
                console.print(result_table)
                
                # Thông báo thành công
                console.print(Panel(
                    f"[bold green]🎉 Hoàn thành nhiệm vụ {job_type} - Nhận được {tien} xu!",
                    title="[bold green]✅ THÀNH CÔNG",
                    border_style="green"
                ))
                
                checkdoiacc = 0
            else:
                try:
                    baoloi(ads_id, object_id, account_id, job_type)
                    console.print(Panel(
                        "[bold yellow]⚠️ Bỏ qua nhiệm vụ do lỗi",
                        title="[bold yellow]🔄 SKIP",
                        border_style="yellow"
                    ))
                    checkdoiacc += 1
                except:
                    pass
                    
    except KeyboardInterrupt:
        console.print(Panel(
            "[bold red]👋 Cảm ơn bạn đã sử dụng tool!\n[white]Tool đã được dừng an toàn.",
            title="[bold yellow]🛑 DỪNG TOOL",
            border_style="red"
        ))
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Đã xảy ra lỗi: {str(e)}\n[white]Vui lòng liên hệ admin để được hỗ trợ.",
            title="[bold red]🚫 LỖI HỆ THỐNG",
            border_style="red"
        ))

if __name__ == "__main__":
    main()
