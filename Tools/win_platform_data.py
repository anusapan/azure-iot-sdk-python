import wmi
import ifaddr
import cpuinfo
import platform
from getmac import get_mac_address

print(get_mac_address())

print(platform.processor())
print("--------------------------------------------------")

# print(cpuinfo.get_cpu_info())
# print("--------------------------------------------------")

# adapters = ifaddr.get_adapters()
# for adapter in adapters:
#     print("--------------------------------------------------")
#     print(adapter)
#     print("IPs of network adapter " + adapter.nice_name)
#     for ip in adapter.ips:
#         print(ip.ip, ip.network_prefix)
# print("--------------------------------------------------")

# c = wmi.WMI()
# for os in c.Win32_OperatingSystem():
#   print(os)
