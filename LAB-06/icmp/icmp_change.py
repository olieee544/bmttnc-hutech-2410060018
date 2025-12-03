from scapy.all import *
from scapy.layers.inet import ICMP, IP


def modify_icmp_packet(packet):
    if packet.haslayer(ICMP) and packet.haslayer(IP):
        icmp_packet = packet[ICMP]
        print("Original ICMP Packet:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {icmp_packet.type}")
        print(f"Code: {icmp_packet.code}")
        print(f"ID: {getattr(icmp_packet, 'id', 'N/A')}")
        print(f"Sequence: {getattr(icmp_packet, 'seq', 'N/A')}")
        print("=" * 30)

        # Tạo payload mới
        new_load = b"This is a modified ICMP packet."
        # Tạo packet mới đảo ngược src/dst và giữ nguyên thông số ICMP
        new_packet = IP(src=packet[IP].dst, dst=packet[IP].src) / \
            ICMP(type=icmp_packet.type, code=icmp_packet.code, id=getattr(icmp_packet, 'id', 0), seq=getattr(icmp_packet, 'seq', 0)) / \
            Raw(load=new_load)

        print("Modified ICMP Packet:")
        print(f"Source IP: {new_packet[IP].src}")
        print(f"Destination IP: {new_packet[IP].dst}")
        print(f"Type: {new_packet[ICMP].type}")
        print(f"Code: {new_packet[ICMP].code}")
        print(f"ID: {getattr(new_packet[ICMP], 'id', 'N/A')}")
        print(f"Sequence: {getattr(new_packet[ICMP], 'seq', 'N/A')}")
        print(f"Load: {new_load}")
        print("=" * 30)

        # Gửi packet mới ra mạng
        send(new_packet)

def main():
    print("Đang bắt và sửa các gói ICMP (ping)... Nhấn Ctrl+C để dừng.")
    sniff(prn=modify_icmp_packet, filter="icmp", store=0, iface="Wi-Fi")

if __name__ == '__main__':
    main()