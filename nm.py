root@9080d165f61778:/app# lshw -short
H/W path  Device    Class      Description
==========================================
                    system     Computer
/0                  bus        Motherboard
/0/0                memory     16GiB System memory
/0/1                processor  AMD EPYC
/0/2                generic    Virtual I/O device
/0/3      /dev/vda  volume     8GiB EXT4 volume
/0/4      /dev/vdb  volume     8GiB EXT4 volume
/0/5      /dev/vdc  disk       274KB Virtual I/O device
/0/6      eth0      network    Ethernet interface
/0/7                generic    Virtual I/O device
/1        input0    input      AT Raw Set 2 keyboard
root@9080d165f61778:/app# hwinfo --short
cpu:                                                            
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
                       AMD EPYC, 2900 MHz
keyboard:
                       AT Raw Set 2 keyboard
  /dev/ttyS0           serial console
storage:
                       Virtio Storage 0
                       Virtio Storage 1
                       Virtio Storage 2
network:
  eth0                 ARM Ethernet controller
                       Virtio Ethernet Card 0
network interface:
  dummy0               Ethernet network interface
  lo                   Loopback network interface
  eth0                 Ethernet network interface
  teql0                Network Interface
disk:
  /dev/vdb             Disk
  /dev/vdc             Disk
  /dev/vda             Disk
bios:
                       BIOS
memory:
                       Main Memory
unknown:
                       FPU
                       DMA controller
                       PIC
                       Keyboard controller
                       Virtio Unclassified device
                       Virtio Unclassified device
  /dev/ttyS0           16550A
root@9080d165f61778:/app# ethtool eth0
Settings for eth0:
	Supported ports: [  ]
	Supported link modes:   Not reported
	Supported pause frame use: No
	Supports auto-negotiation: No
	Supported FEC modes: Not reported
	Advertised link modes:  Not reported
	Advertised pause frame use: No
	Advertised auto-negotiation: No
	Advertised FEC modes: Not reported
	Speed: Unknown!
	Duplex: Unknown! (255)
	Auto-negotiation: off
	Port: Other
	PHYAD: 0
	Transceiver: internal
	Link detected: yes
root@9080d165f61778:/app# nmap -sn 172.19.4.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-11 02:01 UTC
Nmap scan report for 172.19.4.217
Host is up (0.00036s latency).
MAC Address: 62:B4:91:A9:25:3B (Unknown)
Nmap scan report for 9080d165f61778 (172.19.4.218)
Host is up.
Nmap scan report for fly-global-services (172.19.4.219)
Host is up.
Nmap done: 256 IP addresses (3 hosts up) scanned in 200.60 seconds
root@9080d165f61778:/app# nmap -sn -T4 --max-retries 1 172.19.4.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-11 02:05 UTC
Nmap scan report for 172.19.4.217
Host is up (0.00018s latency).
MAC Address: 62:B4:91:A9:25:3B (Unknown)
Nmap scan report for 9080d165f61778 (172.19.4.218)
Host is up.
Nmap scan report for fly-global-services (172.19.4.219)
Host is up.
Nmap done: 256 IP addresses (3 hosts up) scanned in 101.04 seconds
root@9080d165f61778:/app# 
