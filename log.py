import logging

logging.basicConfig (
    filename = "system.log",
    level = logging.INFO,
    format = "%(asctime)s - %(message)s"
)

def log_stats(cpu, memory, disk):
    logging.info(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

def log_message(text):
    logging.warning(text)