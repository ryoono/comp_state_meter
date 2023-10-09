# CPU使用率
# MEM使用率
# ネットワーク通信量
# の取得
# 0.2秒ごとのため，bpsに変換するには*5する必要がある

# 参考ページ
# PC状態取得
# https://psutil.readthedocs.io/en/latest/
# https://chantastu.hatenablog.com/entry/2023/07/15/114657#61-%E3%83%8F%E3%83%BC%E3%83%89%E3%82%A6%E3%82%A7%E3%82%A2%E6%B8%A9%E5%BA%A6

# Arduinoへの送信
# https://qiita.com/keitasumiya/items/25a707c37a73bfd95bac

import psutil
import serial

val_size = 3
values = [ 0, 0, 0]

bytes_sent_buf = psutil.net_io_counters().bytes_sent
bytes_recv_buf = psutil.net_io_counters().bytes_recv

dev_name = "/dev/cu.usbmodem1421"
ser = serial.Serial( dev_name, 9600, timeout=0.1)

def main():
    while True:
        # PC情報の収集
        getCompState()
        sendArduino()

        print(values)
        # time.sleep(0.2)   # cpu使用率取得のインターバルで0.2秒止めているのでコメントアウト


# Arduinoへ変数valuesをシリアル通信で送信する
def sendArduino():

    for i in range(val_size):
        head = 128+i
        high = (values[i] >> 7) & 127
        low  = values[i] & 127
        headByte = head.to_bytes(1, 'big')
        highByte = high.to_bytes(1, 'big')
        lowByte = low.to_bytes(1, 'big')
        ser.write(headByte)
        ser.write(highByte)
        ser.write(lowByte)


# PCの状態を取得する
def getCompState():

    global values, bytes_sent_buf, bytes_recv_buf

    cpu_per = int(psutil.cpu_percent(interval=0.2))
    mem_per = int(psutil.virtual_memory().percent)
    net_info = psutil.net_io_counters()
    bytes_sent = net_info.bytes_sent
    bytes_recv = net_info.bytes_recv
    bytes_sent_recv_bps = int(8 * ((bytes_sent - bytes_sent_buf) + (bytes_recv - bytes_recv_buf)) * 5)
    values = [ cpu_per, mem_per, bytes_sent_recv_bps]
    bytes_sent_buf = bytes_sent
    bytes_recv_buf = bytes_recv


if __name__ == "__main__":
    main()