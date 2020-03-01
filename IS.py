from durable.lang import *


import json
import datetime

start =datetime.datetime.strptime("15-04-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("15-06-2020", "%d-%m-%Y")

print(start,end)

#def myconverter(o):
#    if isinstance(o, datetime.datetime):
#        return o.__str__()
#m = '15-05-2020'
#
#dt_obj = datetime.datetime.strptime(m,"%d-%m-%Y")
#print(dt_obj)
#m = m.Raiekpv
#dt = datetime.datetime.strptime(m.Raiekpv,"%d-%m-%Y")
#print(dt)
with ruleset('test'):
    # antecedent
    @when_any ((m.Arenguklass == 'latimets') & (m.Puudearv < 30000), (m.Arenguklass == 'noorendik'), (m.Looduskaitsealune == 'jah'))
    def say_hello(c):
        # consequent
        print ('Ei raiu, lõpeta kogu töö. Raiumisotsus: ei') 
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Puudearv > 30000))
    def say_hello(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Valgustusraie. Raieplaneeritud kuupäev langeb linnurahuajale, soovitame raiet teostada alates 16.06.2020')
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Diameeter > 6))
    def say_hello(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie.')
    @when_all ((m.Arenguklass == 'Keskealine' or'Valmiv mets' or'Küpsmets'))
    def say_hello(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie.')
 




 
post('test', {'Arenguklass':'latimets',
              'Puudearv': 25000,
              'Raiekpv':'15-05-2020'
              }) 

#infoks: @when_any kasutame siis, kui ükskõik milline neist reeglitest kehtib. @when_all - kõik reeglid peavad kehtima.
#Sisendid 
#
#(start <= json.dumps(m.Raiekpv, default = myconverter) <= end)
#,(start <= datetime.datetime.strptime(m.Raiekpv,"%d-%m-%Y") <= end)
#Puuliik 
#
#Vanus 
#
#Diameeter 
#
#Kõrgus  (selle abil saab teada boniteediklassi) 
#
#Puudearv hektari kohta ( selle abil saab planeerida valgustusraiet) 
#
#Tagavara 
#
#Looduskaitsealune (jah /ei) 
#
#Raiekuupäev → linnurahu 15. Aprillist  15. juunini 
#
#Arenguklass 
#
#Kasvukoht 
#
#Väljundid 
#
#Raiumisotsus (jah, ei) 
#
#Raietüüp (lageraie, harvendusraie, valgustusraie, sanitaarraie) 
#
#Mis asemele istutada? 
#
#Raiemaht 