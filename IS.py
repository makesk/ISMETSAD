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
#boniteediklass = str(m.Kõrgus + m.Vanus) #proovisin inputist kätte saada väärtusi, annab mingi errori

#    @when_any(m.Kahjustus == 'Keskmine' or 'Tugev' or 'Väga tugev')
#    def ei_raie_kahjustatus(c):
#        print('Ei raiu, sest kahjustatus on {0}'.format(c.m.Kahjustus)) #Siin peab määrama veel midagi
with ruleset('test'):
    # antecedent
    @when_any(m.Arenguklass == 'Noorendik')
    def ei_raie_noorendik(c):
        print('Ei raiu, sest arengusklass on {0}'.format(c.m.Arenguklass))
        
    @when_any ((m.Arenguklass == 'latimets') & (m.Puudearv < 30000), (m.Arenguklass == 'noorendik'), (m.Looduskaitsealune == 'jah'))
    def ei_raie(c):
        # consequent
        print ('Ei raiu, lõpeta kogu töö. Raiumisotsus: ei') 
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Diameeter > 6))
    def harvendusraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie. Puu diaameeter:{0}'.format(c.m.Diameeter))
    @when_all ((m.Arenguklass == 'Keskealine' or'Valmiv mets' or'Küpsmets'))
    def harvendusraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie.')
    @when_all ((m.Peapuuliik == 'Mänd' or'Lehis' or'Seedermänd')&(m.Vanus >= 90)&(m.Arenguklass == 'Küpsmets' or'Valmiv mets'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    @when_all ((m.Peapuuliik == 'Kuusk' or'Nulg' or'Ebatsuuga')&(m.Vanus >= 80))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 60))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))

post('test', {'Arenguklass':'Suva',
              'Peapuuliik' : 'Kask',
              'Puudearv':31000,
              'Raiekpv':'15-05-2020',
              'Vanus':91, 
              'Diameeter':8, 
              'Korgus':100
              }) 
post('test', {'Peapuuliik':'Mänd', 'Vanus':65, 'Kahjustus':'Väga tugev'})

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