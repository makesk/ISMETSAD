from durable.lang import *

with ruleset('test'):
    @when_any(m.Arenguklass == 'Noorendik')
    def ei_raie_noorendik(c):
        print('Ei raiu, sest arengusklass on {0}'.format(c.m.Arenguklass))
        
    @when_any ((m.Arenguklass == 'latimets') & (m.Puudearv < 30000), (m.Arenguklass == 'noorendik'), (m.Looduskaitsealune == 'jah'))
    def ei_raie(c):
        print ('Ei raiu, lõpeta kogu töö. Raiumisotsus: ei')
    @when_all ((m.Arenguklass == 'latimets') & (m.Puudearv > 30000))
    def jah_raie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Valgustusraie')
        
    @when_all ((m.Arenguklass == 'latimets') & (m.Diameeter > 6))
    def harvendusraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie. Puu diameeter:{0}'.format(c.m.Diameeter))
        Vanus = c.m.Vanus;
        peapuuliik = c.m.Peapuuliik;
        if((30<Vanus<40) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus 30- 40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus>40) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus >40 SIIS raiemaht on 1/4 tagavara')
        if((Vanus<30) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus <30 SIIS raiemaht on 1/2 tagavara')
        if((Vanus<40) and peapuuliik=='Kuusk'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kuusk JA vanus <40 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>40) and peapuuliik=='Kuusk'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kuusk JA vanus >40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus<30) and peapuuliik=='Kask'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kask JA vanus <30 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>30) and peapuuliik=='Kask'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kask JA vanus >30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus<30) and peapuuliik=='Haab'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on haab JA vanus <30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus>30) and peapuuliik=='Haab'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on haab JA vanus >30 aastat SIIS raiemaht on 1/3 tagavara')
            
    @when_all ((m.Arenguklass == 'Keskealine') | (m.Arenguklass=='Valmiv mets')|(m.Arenguklass=='Küpsmets'))
    def harvendusraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Harvendusraie.')
        Vanus = c.m.Vanus;
        peapuuliik = c.m.Peapuuliik;
        if((30<Vanus<40) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus 30- 40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus>40) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus >40 SIIS raiemaht on 1/4 tagavara')
        if((Vanus<30) and peapuuliik=='Mänd'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on mänd JA vanus <30 SIIS raiemaht on 1/2 tagavara')
        if((Vanus<40) and peapuuliik=='Kuusk'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kuusk JA vanus <40 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>40) and peapuuliik=='Kuusk'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kuusk JA vanus >40 aastat SIIS raiemaht on 1/3 tagavara')
        if((Vanus<30) and peapuuliik=='Kask'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kask JA vanus <30 aastat SIIS raiemaht on 2/3 tagavara')
        if((Vanus>30) and peapuuliik=='Kask'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on kask JA vanus >30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus<30) and peapuuliik=='Haab'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on haab JA vanus <30 aastat SIIS raiemaht on 1/2 tagavara')
        if((Vanus>30) and peapuuliik=='Haab'):
            print('Kuna raietüüp on harvendusraie JA peapuuliik on haab JA vanus >30 aastat SIIS raiemaht on 1/3 tagavara')
            
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 90)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 100)&(m.Boniteediklass =='3'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 110)&(m.Boniteediklass =='4'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Mänd')| (m.Peapuuliik == 'Lehis')| (m.Peapuuliik == 'Seedermänd')&(m.Vanus >= 120)&(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 80)&(m.Boniteediklass =='1')|(m.Boniteediklass =='1A')|(m.Boniteediklass =='2'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Kuusk')| (m.Peapuuliik=='Nulg') | (m.Peapuuliik=='Ebatsuuga'))&(m.Vanus >= 90)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
    
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 60)&((m.Boniteediklass =='1A')|(m.Boniteediklass =='1')))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Kask')&(m.Vanus >= 70)&((m.Boniteediklass =='2')|(m.Boniteediklass =='3')|(m.Boniteediklass =='5A')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        str = str(m.Raiekpv)
        print(str)
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 30)&(m.Boniteediklass =='1A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 40)&(m.Boniteediklass =='1')|(m.Boniteediklass =='2'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all (((m.Peapuuliik == 'Haab')| (m.Peapuuliik=='Pappel') | (m.Peapuuliik=='Pihlakas'))&(m.Vanus >= 50)&(m.Boniteediklass =='3')|(m.Boniteediklass =='4')|(m.Boniteediklass =='5')|(m.Boniteediklass =='5A'))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all(m.Kahjustus == 'Nõrk')
    def ei_raie_kahjustatus(c):
        print('Ei raiu, sest kahjustatus on {0}'.format(c.m.Kahjustus))
        
    @when_any((m.Kahjustus == 'Keskmine') | (m.Kahjustus == 'Tugev') | (m.Kahjustus == 'Väga tugev'))
    def ei_rai_kahjustatus(c):
        print ('Raiumisotsus:Jah. Raietüüp: Sanitaarraie. Kahjustatus on {0}'.format(c.m.Kahjustus))
        
    @when_all ((m.Peapuuliik == 'Sanglepp')&(m.Vanus >= 60))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))
        
    @when_all ((m.Peapuuliik == 'Hall-lepp')&(m.Vanus >= 30))
    def lageraie(c):
        print ('Raiumisotsus:Jah. Raietüüp: Lageraie. Peapuuliik: {0}'.format(c.m.Peapuuliik))

#
#post('test', {'Arenguklass':'suva',
#              'Peapuuliik' : 'Kask',
#              'Puudearv':31000,
#              'Raiekpv':'15-05-2020',
#              'Vanus':71, 
#              'Diameeter':8, 
#              'Boniteediklass':'3'
#              'Kahjustus':'Nõrk'
#              }) 

post('test', {'Arenguklass':'latimets', 

              'Peapuuliik' : 'Kask', 

              'Puudearv':1500, 

              'Vanus':71,  

              'Diameeter':8,  

              'Boniteediklass':'3' }) 
    

