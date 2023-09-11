import sys
import ipaddress

def is_valid_ip(ip_str):
    try:
        ipaddress.IPv4Address(ip_str)  # Încearcă să parseze șirul ca o adresă IPv4
        return True
    except ipaddress.AddressValueError:
        try:
            ipaddress.IPv6Address(ip_str)  # Încearcă să parseze șirul ca o adresă IPv6
            return True
        except ipaddress.AddressValueError:
            return False  # Șirul nu este nici IPv4, nici IPv6

def is_valid_subnet_mask(mask_str):
    try:
        ipaddress.IPv4Network(f"192.168.1.0/{mask_str}", strict=False)
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False

def scan_networ(ip_input, subnet_mask_input):
    import ipaddress
    # Citește adresa IP și mășca de subrețea de la utilizator
    if not (is_valid_ip(ip_input)):
        ip_input = input("Ati introdus o adresa gresita->(exemplu: 192.168.1.0): ")
    if not (is_valid_subnet_mask(subnet_mask_input)):
        subnet_mask_input = input("Mășca de subrețea este gresita->(exemplu: 255.255.255.0): ")

    # Parsează adresa IP și mășca de subrețea introduse de utilizator
    try:
        ip_network = ipaddress.IPv4Network(f"{ip_input}/{subnet_mask_input}", strict=False)
    except ValueError as e:
        print(f"Eroare: {e}")
        exit(1)

    # Afișează toate adresele IP din subrețea
    print("Adresele IP din subrețea specificată sunt:")
    for ip in ip_network.hosts():
        print(ip)


if __name__ == "__main__":
    if "-n" in sys.argv:
        scan_networ(sys.argv[sys.argv.index("-n") + 1], sys.argv[sys.argv.index("-n") + 2])
    # print(sys.argv[1])
