import requests, signal
from bs4 import BeautifulSoup
import random, os
from colorama import Fore,init
init()

red = Fore.RED
lw = Fore.LIGHTWHITE_EX
verde = Fore.GREEN
lvrd = Fore.LIGHTGREEN_EX
lmg = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyll = Fore.LIGHTYELLOW_EX
lcyan = Fore.LIGHTCYAN_EX
lb = Fore.LIGHTBLUE_EX

def trap_c(sig, frame):
    print(red+"\nSALIENDO....")
    os.system('clear|| cls')

    exit()  
signal.signal(signal.SIGINT, trap_c)

class MethodMain():

    def __init__(self):
        self.DATA = "fecha_r=21/12/2022_08:52:21%20p.m"
        self.URL = "https://procesos.ramajudicial.gov.co/jepms/armeniajepms/lista.asp"
        self.RequestSend = requests.session()
        self.CEDULA = None
        self.RANDOM_AGENT = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                            'Mozilla/5.0 (X11; Linux i686; rv:107.0) Gecko/20100101 Firefox/107.0',
                            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
                            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1',
                            'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
                            'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
                            'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF',
                            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko',
                            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36']
   
    def grabify_b(self):
        banner_b = f"""
{lw}  ______    ______            ______   ________   ______   _______    ______   __    __ 
 /      \  /      \          /      \ /        | /      \ /       \  /      \ /  |  /  |
/$$$$$$  |/$$$$$$  |        /$$$$$$  |$$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |
$$ |  $$/ $$ |  $$ | ______ $$ \__$$/ $$ |__    $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |__$$ |
$$ |      $$ |  $$ |/      |$$      \ $$    |   $$    $$ |$$    $$< $$ |      $$    $$ |{lw}
$$ |   __ $$ |  $$ |$$$$$$/  $$$$$$  |$$$$$/    $$$$$$$$ |$$$$$$$  |$$ |   __ $$$$$$$$ |{lw}
$$ \__/  |$$ \__$$ |        /  \__$$ |$$ |_____ $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |  $$ |{lw}
$$    $$/ $$    $$/         $$    $$/ $$       |$$ |  $$ |$$ |  $$ |$$    $$/ $$ |  $$ |{lw}
 $$$$$$/   $$$$$$/           $$$$$$/  $$$$$$$$/ $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ {lw}
                                            {lw}"""
        print(banner_b)
        print(f"{lcyan}1 - {lyll}BUSQUEDA CEDULA\n{lcyan}2 - {lyll}BUSQUEDA POR NOMBRE")


    def sendRequest(self):
        cedulaSend = list()
        try:
           cedulaID = int(input(f"{lvrd}[{lb}IDENTIFICACIÓN{lvrd}] {lmg}-> {lw}"))
        except:
            print(red+"USTED DEJO EL CAMPO VACIO")
            return inicie.sendRequest()    
        headers = {"Content-Type": 'application/x-www-form-urlencoded', "User-Agent": random.choice(self.RANDOM_AGENT)} 
        dataEncode = "cbadju=3&norad=%s&Buscar=Buscar" % str((cedulaID))

        response = self.RequestSend.post(self.URL, headers=headers, data=dataEncode)
        s_htmlParsing = BeautifulSoup(response.content, "html.parser")

        if response.status_code == 200:
            try:
                print(f"\n{yellow}SEARCH {lb}[{cedulaID}] {yellow}-> {lmg}✓")
                caseList = s_htmlParsing.find_all('td')[3].text
                cedula = s_htmlParsing.find_all('td')[4].text
                nameAcusado = s_htmlParsing.find_all('td')[5].text
                name_r = s_htmlParsing.find_all('td')[6].text

                print(f"\n{verde}RADICACION: {lw}{caseList}\n{verde}CEDULA: {lw}{cedula}\n{verde}NOMBRE: {lw}{nameAcusado}\n{verde}REPRESENTANTE: {lw}{name_r}")

                cedulaSend.append(caseList)

            except IndexError:
                print(red+"NO SE ENCONTRARON DATOS") 
                exit()
            try:
               infoInput = str(input(f"{lvrd}[SEARCH INFO] {lmg}-> {lw}"))
            except:
                print(red+"NO PUEDE INGRESAR NÚMEROS")
                exit()
            if infoInput == "y":
               self.CEDULA = cedulaSend[0]

            elif infoInput == "n":
                 exit()

            else: 
               print(red+"OPCIÓN INVALIDA")     
        else:
            print(red+"OCURRIO UN ERROR CON EL SERVIDOR")    


    def infoName(self):
        caseSend = list()
        nameInput = input(f"{lvrd}[NAME] {lmg}-> {lw}").split()
        headers_name = {"Content-Type": "application/x-www-form-urlencoded", "User-agent": random.choice(self.RANDOM_AGENT)}
        dataUrl = f"cbadju=2&norad={nameInput[0]}+{nameInput[1]}&Buscar=Buscar"
        responseName = requests.post(self.URL, headers=headers_name, data=dataUrl)
        session_p = BeautifulSoup(responseName.content, "html.parser")
        if responseName.status_code == 200:
           try:
              print(f"{yellow}SEARCH [{lmg}{' '.join(nameInput)}] {yellow}-> {lmg}✓\n")
              caseList = session_p.find_all('td')[3].text
              cedula = session_p.find_all('td')[4].text
              nameAcusado = session_p.find_all('td')[5].text
              name_r = session_p.find_all('td')[6].text
              print(f"{verde}RADICACION: {lw}{caseList}\n{verde}CEDULA: {lw}{cedula}\n{verde}NOMBRE: {lw}{nameAcusado}\n{verde}REPRESENTANTE: {lw}{name_r}\n")
              caseSend.append(caseList)
           except IndexError:
              print(f"{yellow}RESULT [{red}{' '.join(nameInput)}] {yellow}-> {lmg}X")
              exit()
           try:
              optionsSend = str(input(f"{lvrd}[SEARCH INFO] {lmg}-> {lw}"))
           except:
              print(red+"NO INGRESE NUMEROS")
              exit()

           if optionsSend == "y":
              self.CEDULA = caseSend[0]
           elif optionsSend == "n":
                exit()
           else:
              print(red+"OPCIÓN INVALIDA")

        else:
           print("OCURRIO UN ERROR => [%s]" % (responseName.status_code))

    def sendInfo(self):   
        try:
            url = "https://procesos.ramajudicial.gov.co/jepms/armeniajepms/adju.asp?cp4=%s&%s" % (self.CEDULA, self.DATA)
            headers_main = {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": random.choice(self.RANDOM_AGENT)}

            s_request = requests.post(url, headers=headers_main)
            s_parsingMhtml = BeautifulSoup(s_request.content, "html.parser")
            if s_request.status_code == 200:
                print(f"\n{yellow}CASE {lmg}=> {red}[{self.CEDULA}]")
                ciudad = s_parsingMhtml.find_all('div', {'align': 'center'})[4]
                año = s_parsingMhtml.find_all('td', {'class': 'tpar'})[4]
                municipio = s_parsingMhtml.find_all('td', {'class': 'tpar'})[0]
                nomR = s_parsingMhtml.find_all('td', {'class': 'tpar'})[5]
                print(f"\n{verde}CIUDAD {lmg}=> {lw}{ciudad.text}\n{verde}AÑO {lmg}=> {lw}{año.text}\n{verde}MUNCIPIO {lmg}=> {lw}{municipio.text}\n{verde}RADICACIÓN {lmg}=> {lw}{nomR.text}")
            else:
               print("SERVER ERROR => [%s]" % (s_request.status_code))
        except Exception as e:
            print(e)    
           


inicie = MethodMain()
inicie.grabify_b()

try:
    opcionesM = int(input(f"{lvrd}[OPCIÓN] {lmg}-> {lw}"))
except nameError:
    print(red+"INGRESE UNA OPCIÓN VALIDA")

if opcionesM == 1:
   inicie.sendRequest() 
   inicie.sendInfo()

elif opcionesM == 2:
   inicie.infoName()
   inicie.sendInfo()

else:
   print(red+"OPCIÓN INVALIDA")    
