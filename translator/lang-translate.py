#################### MODULES #################################
import sys
from datetime import datetime
try:
    from googletrans import Translator
##############################################################
    
    pf = pyfiglet.figlet_format("TRANSLATOR")
    print(pf,"\n version 2.0")
    print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
    def translate():
        translator=Translator()
        while True:
            print("------------------------------------------------------- :INSTRUCTIONS: ----------------------------------------------------------------------------------")
            print('''[?]Languages Instructions:
        **********************
        
(01) af: Afrikaans              (24) jw: Javanese            (47) zu: Zulu
(02) sq: Albanian               (25) km: Khmer
(03) ar: Arabic                 (26) ko: Korean
(04) hy: Armenian               (27) la: Latin
(05) bn: Bengali                (28) mr: Marathi
(06) bs: Bosnian                (29) pl: Polish
(07) ca: Catalan                (30) pt: Portuguese
(08) hr: Croatian               (31) ro: Romanian
(09) cs: Czech                  (32) ru: Russian
(10) da: Danish                 (33) sr: Serbian
(11) nl: Dutch                  (34) si: Sinhala
(12) en: English                (35) es: Spanish
(13) eo: Esperanto              (36) su: Sundanese
(14) fi: Finnish                (37) sw: Swahili
(15) fr: French                 (38) ta: Tamil
(16) de: German                 (39) te: Telugu
(17) el: Greek                  (40) th: Thai
(18) gu: Gujarati               (41) tr: Turkish
(19) hi: Hindi                  (42) uk: Ukrainian
(20) hu: Hungarian              (43) vi: Vietnamese
(21) id: Indonesian             (44) cy: Welsh
(22) it: Italian                (45) xh: Xhosa
(23) ja: Japanese               (46) yi: Yiddish
   ''')
            print("------------------------------------------------------- :INPUT DETAILS: ---------------------------------------------------------------------------------")
            print()
            maintext=str(input("Enter the text to translate: "))
            des=input("Enter destination language code(en,ben): ")
            print()
            print("------------------------------------------------------- :PROCESSING: ------------------------------------------------------------------------------------")
            print()
            translated=translator.translate(maintext,dest=des)
            print()
            print("[>>]Generating Answers....")
            time.sleep(3)
            for A in range(3,0,-1):
                print(A,end='\r')
                time.sleep(1)
            print("------------------------------------------------------- :ANSWER: ----------------------------------------------------------------------------------------")
            print()
            print("[*]Your text: ",maintext)
            print()
            print("[>]Your translated text: ",translated.text)
            print()
            print("------------------------------------------------------- :COMPLETE: --------------------------------------------------------------------------------------")
            print()
            inpu=input("[+]Enter <Continue> to Continue or <Exit> to Stop: ")
            print()
            if inpu=="Continue" or inpu=="continue":
                pass
            else:
                print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
                break
    inp=input("[+]Enter <Start> to Start or <Exit> to Stop: ")
    print()
    if inp=="Start" or inp=="start":
        translate()
    else:
        print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
        sys.exit()
except Exception or KeyboardInterrupt:
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("[-]Something Went Wrong!")
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    sys.exit()
