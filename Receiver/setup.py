'''
I vari KEYCODE abbinati ad ogni tasto della tastiera:
http://win32com.goermezer.de/content/view/136/284/
oppure direttamente dal sito di microsoft: http://msdn.microsoft.com/en-us/library/8c6yea83
'''
 #prova branca
import serial, sys
import win32com.client  
import win32api
import py2exe
import win32gui
 
 
#LETTURA DEI DATI DA SERIALE:
 
 
SERIALPORT = raw_input("Inserire la porta seriale a cui e' connesso il dispositivo: ")
# Set up serial port
try:
	ser = serial.Serial(SERIALPORT, 9600) #inizializziamo la connessione e settiamo la porta con frequenza a 9600
	shell = win32com.client.Dispatch("WScript.Shell") #istruzione per poter interagire col sistema operativo.

except serial.SerialException:
	print "no device connected - exiting\n"
	sys.exit()
 
#FUNZIONI PER IL CONTROLLO DI VLC:
 
def vol_piu():
    print "Aumento volume...\n"
    win32api.Sleep(100)
    shell.SendKeys("^{UP}")
 
def vol_meno():
    print "Abbasso volume...\n"
    win32api.Sleep(100)
    shell.SendKeys("^{DOWN}")
 
def big_screen():
    print "Schermo intero\n"
    win32api.Sleep(100)
    shell.SendKeys("{F11}")
 
def start_pause():
    print "Riprendi/Pausa\n"
    win32api.Sleep(100)
    shell.SendKeys(" ") #equivale al tasto SPACE
 
def fast():
    print "Piu veloce...\n"
    win32api.Sleep(100)
    shell.SendKeys("{+}")
 
def slow():
    print "Piu lento...\n"
    win32api.Sleep(100)
    shell.SendKeys("{-}")
 
def stop():
    print "Stop!\n"
    win32api.Sleep(100)
    shell.SendKeys("s")
 
def muto():
    print "Muto...\n"
    win32api.Sleep(100)
    shell.SendKeys("m")
 
def select_vlc():
    print "Porto in primo piano finestra VLC\n"
    win32api.Sleep(100)
    shell.AppActivate("- Lettore Multimediale VLC") #permette di portare in primo piano la finestra col nome fra virgolette
 
def title():
    print "Titolo finestra: "
    win32api.Sleep(100)
    title_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print title_window
 
 
signals = {"2011287572\r\n" : vol_piu,
           "2011279380\r\n" : vol_meno,
		   "2011242516\r\n" : start_pause,
		   "2011291668\r\n" : fast,
           "2011238420\r\n" : slow,
           "1FE10EF\r\n" : stop,
           "1FE20DF\r\n" : select_vlc,
           "2011250708\r\n" : big_screen,
           "1FE7887\r\n" : muto,
           "1FE906F\r\n" : title,
           }
#Apple remote signals
 
# LETTURA CICLICA COMANDI DA SERIALE.
 
while (1):
   z = ser.readline()
   print z
 
   if signals.get(z): #Se i segnali ricevuti sono presenti nel dizionario, processa la relativa funzione associata.
     signals[z]()