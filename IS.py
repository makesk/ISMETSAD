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

#     #Siin peab määrama veel midagi
with ruleset('test'):
    # antecedent
    @when_any(m.Arenguklass == 'Noorendik')
    def ei_raie_noorendik(c):
        print('Raiumisotsus: Ei. sest arengusklass on {0}'.format(c.m.Arenguklass))
        
    @when_any(m.Looduskaitsealune == 'jah')
    def ei_raie_noorendik(c):
        print('Raiumisotsus: Ei. Looduskaitsealune'.format(c.m.Looduskaitsealune))
    
    @when_any ((m.Arenguklass == 'latimets') & (m.Puudearv < 30000), (m.Arenguklass == 'noorendik'), (m.Looduskaitsealune == 'jah'))
    def ei_raie(c):
        # consequent
        print ('Raiumisotsus: Ei. Lõpeta kogu töö. ')
    @when_all ((m.Arenguklass == 'latimets') & (m.Puudearv > 30000))
    def jah_raie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Valgustusraie')
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Diameeter > 6))
    def harvendusraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie. Puu diameeter:{0}'.format(c.m.Diameeter))
    @when_all ((m.Arenguklass == 'Keskealine') | (m.Arenguklass=='Valmiv mets')|(m.Arenguklass=='Küpsmets'))
    def harvendusraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie.')
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 90)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 100)&(m.Boniteediklass =='3'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 110)&(m.Boniteediklass =='4'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 120)&(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 80)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 90)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 60)&((m.Boniteediklass =='1A')|(m.Boniteediklass =='1')))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 70)&((m.Boniteediklass =='2')|(m.Boniteediklass =='3')|(m.Boniteediklass =='5A')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 30)&(m.Boniteediklass =='1A'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 40)&(m.Boniteediklass =='1')|(m.Boniteediklass =='2'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 50)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all((m.Kahjustus == 'Keskmine') | (m.Kahjustus == 'Tugev') | (m.Kahjustus == 'Väga tugev'))
    def ei_raie_kahjustatus(c):
        print('Ei raiu, sest kahjustatus on {0}'.format(c.m.Kahjustus))
        
    @when_all ((m.Peapuuliik == 'Sanglepp')&(m.Vanus >= 60))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Hall-lepp')&(m.Vanus >= 30))
    def lageraie(c):
        # consequent
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))

post('test', {'Arenguklass':'suva',
              'Peapuuliik' : 'Kask',
              'Puudearv':31000,
              'Raiekpv':'15-05-2020',
              'Vanus':71, 
              'Diameeter':8, 
              'Boniteediklass':'3'
              }) 
post('test', {
              'Kahjustus':'Väga tugev'})

post('test', {'Arenguklass':'Noorendik',
              'Peapuuliik' : 'Mänd',
              'Puudearv':1000,
              'Raiekpv':'15-05-2020',
              'Vanus':52, 
              'Diameeter':4, 
              'Boniteediklass':'1'
              }) 

post('test', {'Arenguklass':'Latimets',
              'Peapuuliik' : 'Hall pähklipuu',
              'Puudearv':1,
              'Vanus':230, 
              'Looduskaitsealune':'jah'
              }) 