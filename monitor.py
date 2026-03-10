import psutil
import time
from rich.console import Console
from rich.table import Table

# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

console = Console()

def get_stats():
    cpu = psutil.cpu_percent(1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())
    uptime = time.time() - psutil.boot_time()

    return cpu, memory, disk, processes, uptime

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) / 60)

    return f"{hours}h {minutes}m"

def display_dashboard():
    cpu, memory, disk, processes, uptime = get_stats()
    table = Table(title="System Monitor")

    table.add_column("System")
    table.add_column("Value")

    table.add_row("Cpu", f"{cpu}%")
    table.add_row("Memory", f"{memory}%")
    table.add_row("disk", f"{disk}%")
    table.add_row("processes", str(processes))
    table.add_row("uptime", format_time(uptime))

    console.clear()
    console.print(table)


if __name__ == "__main__":
    display_dashboard()
