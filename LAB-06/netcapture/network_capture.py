import subprocess
from scapy.all import sniff, Raw

def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]  # Bỏ 3 dòng tiêu đề đầu
    interfaces = []
    for line in output_lines:
        parts = line.split()
        if len(parts) > 3:
            interfaces.append(parts[3])  # Tên giao diện ở cột thứ 4
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

if __name__ == "__main__":
    interfaces = get_interfaces()
    print("Danh sách các giao diện mạng:")
    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. {iface}")

    choice = int(input("Chọn một giao diện mạng (nhập số): "))
    selected_iface = interfaces[choice - 1]

    print(f"Bắt gói tin trên giao diện {selected_iface}...")
    sniff(iface=selected_iface, prn=packet_handler, filter="tcp")