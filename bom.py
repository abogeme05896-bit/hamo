root@9080d165f61778:/app# curl ipinfo.io
{
  "ip": "152.236.20.6",
  "city": "Singapore",
  "region": "Singapore",
  "country": "SG",
  "loc": "1.3557,103.8237",
  "org": "AS396356 Latitude.sh",
  "postal": "574180",
  "timezone": "Asia/Singapore",
  "readme": "https://ipinfo.io/missingauth"
}root@9080d165f61778:/app# lscpu
Architecture:                x86_64
  CPU op-mode(s):            32-bit, 64-bit
  Address sizes:             52 bits physical, 57 bits virtual
  Byte Order:                Little Endian
CPU(s):                      8
  On-line CPU(s) list:       0-7
Vendor ID:                   AuthenticAMD
  Model name:                AMD EPYC
    CPU family:              25
    Model:                   17
    Thread(s) per core:      1
    Core(s) per socket:      8
    Socket(s):               1
    Stepping:                1
    BogoMIPS:                5800.00
    Flags:                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pg
                             e mca cmov pat pse36 clflush mmx fxsr sse sse2 ht s
                             yscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constan
                             t_tsc rep_good nopl xtopology nonstop_tsc cpuid ext
                             d_apicid tsc_known_freq pni pclmulqdq ssse3 fma cx1
                             6 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave 
                             avx f16c rdrand hypervisor lahf_lm cmp_legacy cr8_l
                             egacy abm sse4a misalignsse 3dnowprefetch osvw topo
                             ext perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsb
                             ase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx
                             512f avx512dq rdseed adx smap avx512ifma clflushopt
                              clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xs
                             avec xgetbv1 xsaves avx512_bf16 clzero xsaveerptr w
                             bnoinvd arat avx512vbmi umip pku ospke avx512_vbmi2
                              gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx
                             512_vpopcntdq rdpid fsrm
Virtualization features:     
  Hypervisor vendor:         KVM
  Virtualization type:       full
Caches (sum of all):         
  L1d:                       256 KiB (8 instances)
  L1i:                       256 KiB (8 instances)
  L2:                        8 MiB (8 instances)
  L3:                        32 MiB (1 instance)
NUMA:                        
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-7
Vulnerabilities:             
  Gather data sampling:      Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Vulnerable: Safe RET, no microcode
  Spec store bypass:         Mitigation; Speculative Store Bypass disabled via p
                             rctl
  Spectre v1:                Mitigation; usercopy/swapgs barriers and __user poi
                             nter sanitization
  Spectre v2:                Mitigation; Retpolines; IBPB conditional; IBRS_FW; 
                             STIBP disabled; RSB filling; PBRSB-eIBRS Not affect
                             ed; BHI Not affected
  Srbds:                     Not affected
  Tsa:                       Mitigation; Clear CPU buffers
  Tsx async abort:           Not affected
  Vmscape:                   Not affected
root@9080d165f61778:/app# free -h
               total        used        free      shared  buff/cache   available
Mem:            15Gi       762Mi        13Gi        19Mi       1.8Gi        14Gi
Swap:             0B          0B          0B
root@9080d165f61778:/app# df -h
Filesystem      Size  Used Avail Use% Mounted on
none            7.8G  1.3G  6.2G  18% /
/dev/vdb        7.8G  1.3G  6.2G  18% /.fly-upper-layer
shm             7.9G     0  7.9G   0% /dev/shm
tmpfs           7.9G     0  7.9G   0% /sys/fs/cgroup
root@9080d165f61778:/app# df -h
Filesystem      Size  Used Avail Use% Mounted on
none            7.8G  1.3G  6.2G  18% /
/dev/vdb        7.8G  1.3G  6.2G  18% /.fly-upper-layer
shm             7.9G     0  7.9G   0% /dev/shm
tmpfs           7.9G     0  7.9G   0% /sys/fs/cgroup
root@9080d165f61778:/app# uname -a
Linux 9080d165f61778 6.12.84-fly #1 SMP PREEMPT_DYNAMIC Tue May  5 19:01:46 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
root@9080d165f61778:/app# ss -tun
Netid  State  Recv-Q  Send-Q   Local Address:Port    Peer Address:Port  Process 
tcp    ESTAB  0       0            127.0.0.1:5901       127.0.0.1:58196         
tcp    ESTAB  0       0            127.0.0.1:58196      127.0.0.1:5901          
tcp    ESTAB  0       0         172.19.4.218:8080    172.16.4.218:64778         
root@9080d165f61778:/app# who
root@9080d165f61778:/app# aplay -l
bash: aplay: command not found
root@9080d165f61778:/app# lsusb
bash: lsusb: command not found
root@9080d165f61778:/app# lspci
bash: lspci: command not found
root@9080d165f61778:/app# 
