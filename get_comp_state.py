# CPU使用率
# MEM使用率
# ネットワーク通信量
# の取得
# 0.2秒ごとのため，bpsに変換するには*5する必要がある

# 参考ページ
# https://psutil.readthedocs.io/en/latest/
# https://chantastu.hatenablog.com/entry/2023/07/15/114657#61-%E3%83%8F%E3%83%BC%E3%83%89%E3%82%A6%E3%82%A7%E3%82%A2%E6%B8%A9%E5%BA%A6


import psutil
import time

bytes_sent_buf = psutil.net_io_counters().bytes_sent
bytes_recv_buf = psutil.net_io_counters().bytes_recv

while True:
    # CPU使用率(intervalはCPU時間)
    cpu_per = psutil.cpu_percent(interval=None)
    mem_per = psutil.virtual_memory().percent
    net_info = psutil.net_io_counters()
    bytes_sent = net_info.bytes_sent
    bytes_recv = net_info.bytes_recv
    print("cpu_per：",end="")
    print(cpu_per, end=", ")
    print("mem_per：",end="")
    print(mem_per, end=", ")
    print("net_paket：",end="")
    print((bytes_sent - bytes_sent_buf) + (bytes_recv - bytes_recv_buf))
    bytes_sent_buf = bytes_sent
    bytes_recv_buf = bytes_recv
    time.sleep(0.2)