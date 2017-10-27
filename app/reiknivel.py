#!/usr/bin/python
# -*- coding: utf-8 -*-

def islendingur_input():
    hjuskaparstada = input_hjusskaparst() #gefur hjúskaparstöðu, int á bilinu 1-3
    tekjur = input_tekjur(hjuskaparstada) #gefur tekjulista [tekjur, fjármagnstekjur, tekjur maka, fjármagnstekjur maka]
    tekjur_e_skatt, stadgreidsla, lifeyrisgreidsla, sereignarlifeyrisgr = stadgreidsla_func(tekjur[0])
    husnaedisstudningur, husn_eignaskerding, husn_tekjuskerding =\
        husnaedisstudningur_func(tekjur, hjuskaparstada)
    if hjuskaparstada != 1:
        barnabaetur = barnabaetur_func(hjuskaparstada, tekjur)
    else: barnabaetur = 0
    
    if tekjur[0] >= 1678001/12:
        utvarpsgjald = 16800/12
    else: utvarpsgjald = 0
    
    #print_all(tekjur, tekjur_e_skatt, stadgreidsla, lifeyrisgreidsla,\
    #          sereignarlifeyrisgr, husnaedisstudningur, barnabaetur, utvarpsgjald)
    netto = tekjur_e_skatt + husnaedisstudningur + barnabaetur - utvarpsgjald
    
    nidurstodur = {'allar_tekjur': [tekjur, tekjur_e_skatt],\
                   'allar_baetur': [husnaedisstudningur, barnabaetur],\
                   'fradrattur': [utvarpsgjald, stadgreidsla, lifeyrisgreidsla],\
                   'pjeng_i_vasa': (netto)}
    
    return nidurstodur

def input_hjusskaparst():
    hjuskaparstada = 4
    while hjuskaparstada >3 or hjuskaparstada <1:
        hjuskaparstada = int(raw_input('1: einhleypur, 2: einst. foreldri, 3: giftur/sambud '))
        
    return hjuskaparstada

def input_tegund_husnaedis():
    print "Hver er husnæðisstaða þín? Býrðu í eigin húsnæði, leiguhúsnæði eða hvorugt?"
    
    tegund = 4
    while tegund >3 or tegund <1:
        tegund = int(raw_input('1: eigin, 2: leigu, 3: hvorugt '))
    
    return tegund

def input_tekjur(hjuskaparstada):
    laun_a_manudi = int(raw_input("Laun fyrir skatt: "))
    fjarmagnstekjur = int(raw_input("Fjarmagnstekjur: "))
    if hjuskaparstada == 3:
        laun_maka = int(raw_input("Laun maka fyrir skatt: "))
        fjarmagnstekjur_maka = int(raw_input("Fjarmagnstekjur maka: "))
    else:
        laun_maka = 0
        fjarmagnstekjur_maka = 0
    
    tekju_uppl = [laun_a_manudi, fjarmagnstekjur, laun_maka, fjarmagnstekjur_maka]
    
    return tekju_uppl

def stadgreidsla_func(tekjur):
    
    skattthrep = 834707
    skatthlutfall_nedra = 0.3694
    skatthlutfall_efra = 0.4624
    personuafsl = 52907
    
    print " Iðgjald í lífeyrissjóð?"
    idgjald = 3
    while idgjald >2 or idgjald <1:
        idgjald = int(raw_input('1: 0%, 2: 4% '))
    if idgjald == 1:
        idgjald = 0.0
    elif idgjald == 2:
        idgjald = 0.04
            
    print " Iðgjald í séreign?"
    sereignaridgjald = 5
    while sereignaridgjald >4 or sereignaridgjald <0:
        sereignaridgjald = int(raw_input('0: 0%, 1: 1%, 2: 2%, 3: 3%, 4: 4% '))
    sereignaridgjald = sereignaridgjald / 100.0
    
    lifeyrir = (tekjur * idgjald)
    serlifeyrir = (tekjur * sereignaridgjald)
    
    stofn = tekjur - lifeyrir - serlifeyrir
    
    if stofn <= skattthrep:
        skattstofn_1 = stofn
        skattstofn_2 = 0
    else:
        skattstofn_1 = skattthrep
        skattstofn_2 = stofn - skattthrep
        
    skattur_nedra_threp = (skattstofn_1*skatthlutfall_nedra)
    skattur_efra_threp = (skattstofn_2*skatthlutfall_efra)
    
    reiknud_stadgreidsla = skattur_nedra_threp + skattur_efra_threp
    stadgreidsla_alls = reiknud_stadgreidsla - personuafsl
    
    laun_e_skatt = stofn - stadgreidsla_alls
    
    return laun_e_skatt, stadgreidsla_alls, lifeyrir, serlifeyrir

def husnaedisstudningur_func(tekjur, hjuskaparstada):
    
    tegund_husnaedis = input_tegund_husnaedis()
    
    if tegund_husnaedis == 1:      
        studningur = vaxtabaetur_func(tekjur, hjuskaparstada)
        
    elif tegund_husnaedis == 2:
        studningur = husnaedisbaetur_func(tekjur)
        
    else:
        studningur = 0
    
    return studningur

def vaxtabaetur_func(tekjur, hjuskaparstada):
    
    hamark_vaxtagjalda = [800000, 1000000, 1200000] #fyrir: [einstakling, einstætt foreldri, hjón]
    hamark_bota = [400000, 500000, 600000] #fyrir: [einstakling, einstætt foreldri, hjón]
    tekjur_yearly = [tekjur[0]*12, tekjur[1]*12, tekjur[2]*12, tekjur[3]*12]
    
    eignaskerdingarmork_nedri = [4500000.0, 4500000.0, 7300000.0] #fyrir: [einstakling, einstætt foreldri, hjón]
    eignaskerdingarmork_efri = [7200000.0, 7200000.0, 11680000.0] #fyrir: [einstakling, einstætt foreldri, hjón]

    print "Allar eignir að frádregnum öllum skuldum. Með eignum skal telja hlutabréf, innstæður og verðbréf: "
    eignir = int(raw_input())
    print 'Eftirstöðvar í árslok af lánum sem tekin hafa verið til öflunar íbúðarhúsnæðis til eigin nota: '
    eftirstodvar = int(raw_input())
    print "Vextir og verðbætur af íbúðarlánum á ársgrundvelli, þ.m.t. dráttarvextir og lántökukostnaður: "
    vaxtagjold = int(raw_input())
    
    stofn_list = [hamark_vaxtagjalda[hjuskaparstada-1], 0.07*eftirstodvar, vaxtagjold]
    stofn =  min(float(s) for s in stofn_list)
    
    tekjuskerding = (0.085 * sum(tekjur_yearly))
    baetur = stofn - tekjuskerding
    
    if eignir >= eignaskerdingarmork_efri[hjuskaparstada-1]:
        eignaskerding = baetur
        baetur = 0
        
    elif eignir >= eignaskerdingarmork_nedri[hjuskaparstada-1]:
        eignaskerding =\
            baetur * ((eignir - eignaskerdingarmork_nedri[hjuskaparstada-1]) /
                      (eignaskerdingarmork_efri[hjuskaparstada-1] - eignaskerdingarmork_nedri[hjuskaparstada-1]))
        baetur -= eignaskerding
    
    else:
        eignaskerding = 0
            
    if baetur > hamark_bota[hjuskaparstada-1]:
        baetur = hamark_bota[hjuskaparstada-1]

    baetur = baetur/12
    tekjuskerding = tekjuskerding/12
    eignaskerding = (eignaskerding/12)
    
    if baetur < 0:
        baetur = 0
    if tekjuskerding < 0:
        tekjuskerding = 0
    if eignaskerding < 0:
        eignaskerding = 0
            
    return baetur, tekjuskerding, eignaskerding

def husnaedisbaetur_func(tekjur):
    fjoldi_heimilismanna = int(raw_input("fjoldi heimilismanna ad ther medtoldum: "))
    if fjoldi_heimilismanna > 4:
        fjoldi_heimilismanna = 4
    
    if fjoldi_heimilismanna == 1:
        heimilistekjur = (tekjur[0] + tekjur[1])
    else:
        heimilistekjur = int(raw_input('samanlagdar manadartekjur allra heimilismanna: '))
    heimiliseignir = int(raw_input('samanlagdar eignir allra heimilismanna: '))
    husnaediskostnadur = int(raw_input('manadarlegur husnaediskostnadur: '))
    
    grunnfjarhaedir = [372000/12, 492000/12, 576000/12, 624000/12]
    fritekjumark = [3373000/12, 4461064/12, 5222710/12, 5657936/12]
    eignaskerdingarmork_nedri = 6500000.0
    eignaskerdingarmork_efri = 10400000.0
    
    stofn = grunnfjarhaedir[fjoldi_heimilismanna-1]
    
    if heimilistekjur <= fritekjumark[fjoldi_heimilismanna-1]:
        baetur = stofn
        tekjuskerding = 0
    else:
        tekjuskerding = 0.09 * (heimilistekjur - fritekjumark[fjoldi_heimilismanna-1])
        baetur = stofn - tekjuskerding
    
    if heimiliseignir >= eignaskerdingarmork_efri:
        eignaskerding = baetur
        baetur = 0
    elif heimiliseignir >= eignaskerdingarmork_nedri:
        eignaskerding = baetur *\
            ((heimiliseignir - eignaskerdingarmork_nedri) / (eignaskerdingarmork_efri - eignaskerdingarmork_nedri))
        baetur -= eignaskerding
    else:
        eignaskerding = 0
    
    if baetur > 0.75*husnaediskostnadur:
        baetur = 0.75*husnaediskostnadur
    if baetur < 0:
        baetur = 0
    if tekjuskerding < 0:
        tekjuskerding = 0
    if eignaskerding < 0:
        eignaskerding = 0
            
    return baetur, tekjuskerding, eignaskerding

def barnabaetur_func(hjuskaparstada, tekjur):
    tekjur_yearly = [tekjur[0]*12, tekjur[1]*12, tekjur[2]*12, tekjur[3]*12]
    
    print "Fjöldi barna á heimli: "
    fj_barna = int(raw_input())
    if fj_barna == 0:
        return
    print " - þar af yngri en 7 ára: "
    fj_barna_undir_7 = fj_barna + 1
    while fj_barna_undir_7 > fj_barna:
        fj_barna_undir_7 = int(raw_input())
    if fj_barna > 3:
        fj_barna = 3
    
    # SKERÐINGARHLUFÖLL
    skerdingarhlutfoll = [0.04, 0.06, 0.08] # [1 barn, 2 börn, 3 börn eða fleiri]
    skerdingarhlutf_vidbot = 0.04
    
    # FJÁRHÆÐIR 2017
    fjarhaedir_fyrsta_barn = [342939, 205834] # [einstætt foreldri, hjón/sambúðarfólk]
    fjarhaedir_umfram_born = [351787, 245087] # [einstætt foreldri, hjón/sambúðarfólk]
    vidbotarfjarhaed_hvert_barn_undir_7 = 122879
    
    # SKERÐINGARMÖRK
    skerdingarmork = [2700000, 5400000] # [einstætt foreldri, hjón/sambúðarfólk]
    
    # ÚTREIKNINGUR ÓSKERTRAR BÓTAFJÁRHÆÐAR
    stofn_til_skerdingar = sum(tekjur_yearly) - skerdingarmork[hjuskaparstada-2]
    if stofn_til_skerdingar < 0:
        stofn_til_skerdingar = 0
        
    almennar_barnabaetur =\
        fjarhaedir_fyrsta_barn[hjuskaparstada-2] + ((fj_barna-1) * fjarhaedir_umfram_born[hjuskaparstada-2]) 
        
    vidbotarbaetur = (fj_barna_undir_7 * vidbotarfjarhaed_hvert_barn_undir_7)
        
    skerding = (skerdingarhlutfoll[fj_barna-1] * stofn_til_skerdingar)
    skerding_vidbotar = ((fj_barna_undir_7*skerdingarhlutf_vidbot) * stofn_til_skerdingar)
    
    baetur = almennar_barnabaetur + vidbotarbaetur - (skerding + skerding_vidbotar)
    if baetur < 0:
        baetur = 0
    
    '''print "Tekjustofn: {:,}".format(sum(tekjur_yearly))
    print "Skerdingarmork: {:,}".format(skerdingarmork[hjuskaparstada-2])
    print "Stofn til skerdingar: {:,}".format(stofn_til_skerdingar)
    print
    print "Almennar barnabaetur: {:,}".format(almennar_barnabaetur)
    print "Skerding vegna tekna: {:,}".format(skerding) 
    print
    print "Viðbót vegna barna yngri en 7 ára: {:,}".format(vidbotarbaetur)
    print "Skerðing vegna tekna: {:,}".format(skerding_vidbotar)
    print
    print "Barnabaetur alls: {:,}".format(baetur)
    print "Baetur skiptast jafnt 'a milli hjona: {:,}".format(baetur/2)
    print "Til greiðslu í hverjum ársfjórðungi: {:,}".format(baetur/4)'''
    
    return baetur/12

def print_dict(person_dict):
    print ""
    print ""
    print "==========LAUN============"
    print "Tekjur fyrir skatt: {:,}".format(person_dict['allar_tekjur'][0][0])
    print " - staðgreiðsla: {:,}".format(person_dict['fradrattur'][1])
    print " - greitt i lifeyrissparnad: {:,}".format(person_dict['fradrattur'][2])
    print "Útborguð laun: {:,}".format(person_dict['allar_tekjur'][1])
    print ""
    print "====HÚSNÆÐISSTUÐNINGUR============"
    print "Húsnæðisstuðningur á mánuði: {:,}".format(person_dict['allar_baetur'][0])
    print ""
    print "====Barnabætur========="
    print "Barnabætur á mánuði: {:,}".format(person_dict['allar_baetur'][1])
    print ""
    print "=====FRÁDRÁTTUR========"
    print "Útvarpsgjald: {:,}".format(person_dict['fradrattur'][0])
    print ""
    print ""
    print "====NIÐURSTAÐA========"
    print "Pjénge í vasann í hverjum mánuði: {:,}"\
        .format(person_dict['pjeng_i_vasa'])
    print "======================"


kelson = islendingur_input()
print kelson