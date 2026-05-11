broot@9080d165f61778:/app# speedtest-cli
Retrieving speedtest.net configuration...
Testing from Vtal (152.236.20.6)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by SpaceCore.pro | Premium VPS Hosting (Singapore) [15725.19 km]: 3.301 ms
Testing download speed................................................................................
Download: 194.70 Mbit/s
Testing upload speed......................................................................................................
Upload: 198.24 Mbit/s
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
}root@9080d165f61778:/app# traceroute google.com
traceroute to google.com (142.251.12.139), 30 hops max, 60 byte packets
 1  172.19.4.217 (172.19.4.217)  0.610 ms  0.552 ms  0.520 ms
 2  206.223.224.235 (206.223.224.235)  0.861 ms 206.223.224.234 (206.223.224.234)  0.830 ms 10.10.218.6 (10.10.218.6)  0.973 ms
 3  10.10.218.4 (10.10.218.4)  0.941 ms 10.10.218.2 (10.10.218.2)  0.911 ms  1.256 ms
 4  pw-ether20.2-lo0-sr1.sin.router.colt.net (193.82.33.69)  1.987 ms 10.10.218.2 (10.10.218.2)  1.171 ms pw-ether20.2-lo0-sr1.sin.router.colt.net (193.82.33.69)  2.091 ms
 5  212.74.84.69 (212.74.84.69)  1.430 ms * *
 6  if-bundle-2-2.qcore2.svw-singapore.as6453.net (209.58.82.129)  1.248 ms * 15169.sgw.equinix.com (27.111.228.30)  1.237 ms
 7  72.14.212.74 (72.14.212.74)  1.197 ms 192.178.109.121 (192.178.109.121)  1.164 ms *
 8  72.14.212.74 (72.14.212.74)  1.005 ms  0.957 ms 192.178.109.193 (192.178.109.193)  2.393 ms
 9  172.253.66.204 (172.253.66.204)  1.378 ms 192.178.109.117 (192.178.109.117)  1.020 ms 192.178.109.193 (192.178.109.193)  1.854 ms
10  142.251.231.253 (142.251.231.253)  1.638 ms 142.251.198.173 (142.251.198.173)  3.371 ms 142.251.192.8 (142.251.192.8)  1.315 ms
11  142.251.231.206 (142.251.231.206)  3.578 ms 108.170.233.227 (108.170.233.227)  1.698 ms 142.251.52.191 (142.251.52.191)  1.905 ms
12  142.251.51.213 (142.251.51.213)  1.608 ms 142.251.51.211 (142.251.51.211)  1.941 ms 209.85.250.141 (209.85.250.141)  1.734 ms
13  142.251.52.193 (142.251.52.193)  1.706 ms 142.251.51.211 (142.251.51.211)  2.054 ms *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * se-in-f139.1e100.net (142.251.12.139)  1.777 ms
root@9080d165f61778:/app# nmap -A -T4 172.19.4.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-05-11 22:28 UTC
Nmap scan report for 172.19.4.217
Host is up (0.00021s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT     STATE  SERVICE    VERSION
5432/tcp closed postgresql
MAC Address: 62:B4:91:A9:25:3B (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.18
OS details: Linux 2.6.18
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.21 ms 172.19.4.217

Nmap scan report for 9080d165f61778 (172.19.4.218)
Host is up (0.000036s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
5901/tcp open  vnc        VNC (protocol 3.8)
8080/tcp open  http-proxy WebSockify Python/3.12.3
|_http-title: Directory listing for /
| http-git: 
|   172.19.4.218:8080/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|       https://github.com/novnc/noVNC.git
|_    Project type: Python application (guessed from .gitignore)
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: WebSockify Python/3.12.3
|     Date: Mon, 11 May 2026 22:30:58 GMT
|     Content-type: text/html; charset=utf-8
|     Content-Length: 1123
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Directory listing for /</title>
|     </head>
|     <body>
|     <h1>Directory listing for /</h1>
|     <hr>
|     <ul>
|     <li><a href=".git/">.git/</a></li>
|     <li><a href=".github/">.github/</a></li>
|     <li><a href=".gitignore">.gitignore</a></li>
|     <li><a href=".gitmodules">.gitmodules</a></li>
|     <li><a href="app/">app/</a></li>
|     <li><a href="AUTHORS">AUTHORS</a></li>
|     <li><a href="core/">core/</a></li>
|     <li><a href="defaults.json">defaults.json</a></li>
|     <li><a href="docs/">docs/</a></li>
|     <li><a href="eslint.config.mjs">eslint.config.mjs</a></li>
|     <li><a href="karma.conf.cjs">karma.conf.cjs</a></li>
|     <li><a href="LICENSE.txt">LICENSE.txt</a></li>
|     <li><a href="mandatory.json">mandatory.json</a></li>
|     <li><a href="pa
|   HTTPOptions: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.12.3
|     Date: Mon, 11 May 2026 22:30:58 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 355
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|_    </html>
|_http-server-header: WebSockify Python/3.12.3
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94SVN%I=7%D=5/11%Time=6A0258A2%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,4FB,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20WebSockify\x20Pyt
SF:hon/3\.12\.3\r\nDate:\x20Mon,\x2011\x20May\x202026\x2022:30:58\x20GMT\r
SF:\nContent-type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x2011
SF:23\r\n\r\n<!DOCTYPE\x20HTML>\n<html\x20lang=\"en\">\n<head>\n<meta\x20c
SF:harset=\"utf-8\">\n<title>Directory\x20listing\x20for\x20/</title>\n</h
SF:ead>\n<body>\n<h1>Directory\x20listing\x20for\x20/</h1>\n<hr>\n<ul>\n<l
SF:i><a\x20href=\"\.git/\">\.git/</a></li>\n<li><a\x20href=\"\.github/\">\
SF:.github/</a></li>\n<li><a\x20href=\"\.gitignore\">\.gitignore</a></li>\
SF:n<li><a\x20href=\"\.gitmodules\">\.gitmodules</a></li>\n<li><a\x20href=
SF:\"app/\">app/</a></li>\n<li><a\x20href=\"AUTHORS\">AUTHORS</a></li>\n<l
SF:i><a\x20href=\"core/\">core/</a></li>\n<li><a\x20href=\"defaults\.json\
SF:">defaults\.json</a></li>\n<li><a\x20href=\"docs/\">docs/</a></li>\n<li
SF:><a\x20href=\"eslint\.config\.mjs\">eslint\.config\.mjs</a></li>\n<li><
SF:a\x20href=\"karma\.conf\.cjs\">karma\.conf\.cjs</a></li>\n<li><a\x20hre
SF:f=\"LICENSE\.txt\">LICENSE\.txt</a></li>\n<li><a\x20href=\"mandatory\.j
SF:son\">mandatory\.json</a></li>\n<li><a\x20href=\"pa")%r(HTTPOptions,21C
SF:,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20WebSockify
SF:\x20Python/3\.12\.3\r\nDate:\x20Mon,\x2011\x20May\x202026\x2022:30:58\x
SF:20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/html;charset=utf
SF:-8\r\nContent-Length:\x20355\r\n\r\n<!DOCTYPE\x20HTML>\n<html\x20lang=\
SF:"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x
SF:20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<title>Error\x20r
SF:esponse</title>\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\x20\
SF:x20\x20\x20\x20\x20\x20\x20<h1>Error\x20response</h1>\n\x20\x20\x20\x20
SF:\x20\x20\x20\x20<p>Error\x20code:\x20405</p>\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20<p>Message:\x20Method\x20Not\x20Allowed\.</p>\n\x20\x20\x20\x20\
SF:x20\x20\x20\x20<p>Error\x20code\x20explanation:\x20405\x20-\x20Specifie
SF:d\x20method\x20is\x20invalid\x20for\x20this\x20resource\.</p>\n\x20\x20
SF:\x20\x20</body>\n</html>\n");
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

Nmap scan report for fly-global-services (172.19.4.219)
Host is up (0.0000070s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
5901/tcp open  vnc        VNC (protocol 3.3; Locked out)
8080/tcp open  http-proxy WebSockify Python/3.12.3
|_http-server-header: WebSockify Python/3.12.3
| http-git: 
|   172.19.4.219:8080/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|       https://github.com/novnc/noVNC.git
|_    Project type: Python application (guessed from .gitignore)
|_http-title: Directory listing for /
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: WebSockify Python/3.12.3
|     Date: Mon, 11 May 2026 22:30:58 GMT
|     Content-type: text/html; charset=utf-8
|     Content-Length: 1123
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Directory listing for /</title>
|     </head>
|     <body>
|     <h1>Directory listing for /</h1>
|     <hr>
|     <ul>
|     <li><a href=".git/">.git/</a></li>
|     <li><a href=".github/">.github/</a></li>
|     <li><a href=".gitignore">.gitignore</a></li>
|     <li><a href=".gitmodules">.gitmodules</a></li>
|     <li><a href="app/">app/</a></li>
|     <li><a href="AUTHORS">AUTHORS</a></li>
|     <li><a href="core/">core/</a></li>
|     <li><a href="defaults.json">defaults.json</a></li>
|     <li><a href="docs/">docs/</a></li>
|     <li><a href="eslint.config.mjs">eslint.config.mjs</a></li>
|     <li><a href="karma.conf.cjs">karma.conf.cjs</a></li>
|     <li><a href="LICENSE.txt">LICENSE.txt</a></li>
|     <li><a href="mandatory.json">mandatory.json</a></li>
|     <li><a href="pa
|   HTTPOptions: 
|     HTTP/1.1 405 Method Not Allowed
|     Server: WebSockify Python/3.12.3
|     Date: Mon, 11 May 2026 22:30:58 GMT
|     Connection: close
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 355
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 405</p>
|     <p>Message: Method Not Allowed.</p>
|     <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.94SVN%I=7%D=5/11%Time=6A0258A2%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,4FB,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20WebSockify\x20Pyt
SF:hon/3\.12\.3\r\nDate:\x20Mon,\x2011\x20May\x202026\x2022:30:58\x20GMT\r
SF:\nContent-type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x2011
SF:23\r\n\r\n<!DOCTYPE\x20HTML>\n<html\x20lang=\"en\">\n<head>\n<meta\x20c
SF:harset=\"utf-8\">\n<title>Directory\x20listing\x20for\x20/</title>\n</h
SF:ead>\n<body>\n<h1>Directory\x20listing\x20for\x20/</h1>\n<hr>\n<ul>\n<l
SF:i><a\x20href=\"\.git/\">\.git/</a></li>\n<li><a\x20href=\"\.github/\">\
SF:.github/</a></li>\n<li><a\x20href=\"\.gitignore\">\.gitignore</a></li>\
SF:n<li><a\x20href=\"\.gitmodules\">\.gitmodules</a></li>\n<li><a\x20href=
SF:\"app/\">app/</a></li>\n<li><a\x20href=\"AUTHORS\">AUTHORS</a></li>\n<l
SF:i><a\x20href=\"core/\">core/</a></li>\n<li><a\x20href=\"defaults\.json\
SF:">defaults\.json</a></li>\n<li><a\x20href=\"docs/\">docs/</a></li>\n<li
SF:><a\x20href=\"eslint\.config\.mjs\">eslint\.config\.mjs</a></li>\n<li><
SF:a\x20href=\"karma\.conf\.cjs\">karma\.conf\.cjs</a></li>\n<li><a\x20hre
SF:f=\"LICENSE\.txt\">LICENSE\.txt</a></li>\n<li><a\x20href=\"mandatory\.j
SF:son\">mandatory\.json</a></li>\n<li><a\x20href=\"pa")%r(HTTPOptions,21C
SF:,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nServer:\x20WebSockify
SF:\x20Python/3\.12\.3\r\nDate:\x20Mon,\x2011\x20May\x202026\x2022:30:58\x
SF:20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/html;charset=utf
SF:-8\r\nContent-Length:\x20355\r\n\r\n<!DOCTYPE\x20HTML>\n<html\x20lang=\
SF:"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x
SF:20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<title>Error\x20r
SF:esponse</title>\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\x20\
SF:x20\x20\x20\x20\x20\x20\x20<h1>Error\x20response</h1>\n\x20\x20\x20\x20
SF:\x20\x20\x20\x20<p>Error\x20code:\x20405</p>\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20<p>Message:\x20Method\x20Not\x20Allowed\.</p>\n\x20\x20\x20\x20\
SF:x20\x20\x20\x20<p>Error\x20code\x20explanation:\x20405\x20-\x20Specifie
SF:d\x20method\x20is\x20invalid\x20for\x20this\x20resource\.</p>\n\x20\x20
SF:\x20\x20</body>\n</html>\n");
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (3 hosts up) scanned in 206.28 seconds
root@9080d165f61778:/app# 
