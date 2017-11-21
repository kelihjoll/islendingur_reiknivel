# -*- coding: utf-8 -*-

def islendingur():
    bakgrunnsuppl = input_bakgrunnsuppl()
    tekjur_e_skatt, stadgreidsla, lifeyrisgreidsla, sereignarlifeyrisgr = stadgreidsla_func(bakgrunnsuppl)
    
    if bakgrunnsuppl['tekjur'][0] >= 1678001/12:
        utvarpsgjald = 16800/12
    else: utvarpsgjald = 0
    
    if bakgrunnsuppl['ororkuhlutfall'] > 0:
        samtals_ororka, ororka_e_skatt, ororka_stadgreidsla, ororka_skattgrunnur,\
        ororkulifeyrir, aldurstengd_uppbot, tekjutrygging,\
        heimilisuppbot, bensinsstyrkur, barnalifeyrir, medlag,\
        foreldralaun, framfaersluppbot = ororka_func(bakgrunnsuppl)
    else: 
        samtals_ororka = ororka_e_skatt = ororka_stadgreidsla = ororka_skattgrunnur =\
        ororkulifeyrir = aldurstengd_uppbot = tekjutrygging =\
        heimilisuppbot = bensinsstyrkur = barnalifeyrir =\
        medlag = foreldralaun = framfaersluppbot = 0
        
    if bakgrunnsuppl['aldur'] > 67:
        samtals_elli, ellilifeyrir_e_skatt, ellilif_stadgreidsla, elli_skattgrunnur,\
        ellilifeyrir, heimilisuppbot_elli, bensinsstyrkur_elli,\
        barnalifeyrir_elli, medlag_elli, foreldralaun_elli = ellilifeyrir_func(bakgrunnsuppl)
    else:
        samtals_elli = ellilifeyrir_e_skatt = ellilif_stadgreidsla = elli_skattgrunnur =\
        ellilifeyrir = heimilisuppbot_elli = bensinsstyrkur_elli =\
        barnalifeyrir_elli = medlag_elli = foreldralaun_elli = 0
    
    husnaedisstudningur, husn_tekjuskerding, husn_eignaskerding =\
        husnaedisstudningur_func(bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
    if bakgrunnsuppl['hjuskaparstada'] != 1:
        barnabaetur = barnabaetur_func(bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
    else: barnabaetur = 0
    
    fjarmagnstekjur_e_skatt = bakgrunnsuppl['tekjur'][1] - (bakgrunnsuppl['tekjur'][1] * 0.2)
    
    netto = tekjur_e_skatt + fjarmagnstekjur_e_skatt + husnaedisstudningur +\
    barnabaetur + ororka_e_skatt + ellilifeyrir_e_skatt - utvarpsgjald
    
    nidurstodur = {'tekjur': bakgrunnsuppl['tekjur'],
                   'tekjur_e_skatt': tekjur_e_skatt,
                   'fjarmagnstekjur_e_skatt': fjarmagnstekjur_e_skatt,
                   'stadgreidsla': stadgreidsla,
                   'lifeyrisgreidsla': (lifeyrisgreidsla+sereignarlifeyrisgr),
                   'husnaedisstudningur': husnaedisstudningur,
                   'husnaedisstudningur_eignaskerd': husn_eignaskerding,
                   'husnaedisstudningur_tekjuskerd': husn_tekjuskerding,
                   'barnabaetur': barnabaetur,
                   'utvarpsgjald': utvarpsgjald,
                   'pjeng_i_vasa': netto,
                   'ororka_alls': samtals_ororka,
                   'ororka_e_skatt': ororka_e_skatt,
                   'ororka_stadgreidsla': ororka_stadgreidsla,
                   'ororkulifeyrir': ororkulifeyrir,
                   'aldurstengd_ororkuuppbot': aldurstengd_uppbot,
                   'tekjutrygging_ororka': tekjutrygging,
                   'heimilisuppbot_ororka': heimilisuppbot,
                   'bensinsstyrkur_ororka': bensinsstyrkur,
                   'barnalifeyrir_ororka': barnalifeyrir,
                   'medlag_ororka': medlag,
                   'foreldralaun_ororka': foreldralaun,
                   'framfaersluppbot_ororka': framfaersluppbot,
                   'ellilifeyrir': ellilifeyrir,
                   'ellilifeyrir_e_skatt': ellilifeyrir_e_skatt,
                   'ellilif_stadgreidsla': ellilif_stadgreidsla,
                   'heimilisuppbot_ellifeyrir': heimilisuppbot_elli,
                   'bensinstyrkur_elli': bensinsstyrkur_elli,
                   'barnalifeyrir_elli': barnalifeyrir_elli,
                   'medlag_elli': medlag_elli,
                   'foreldralaun_elli': foreldralaun_elli,
                   'samtals_elli': samtals_elli}
    
    return nidurstodur, bakgrunnsuppl

def input_bakgrunnsuppl():
    # HJÚSKAPARSTAÐA
    # =======================================================
    hjuskaparstada = 4
    while hjuskaparstada >3 or hjuskaparstada <1:
        hjuskaparstada = int(raw_input('1: einhleypur, 2: einst. foreldri, 3: giftur/sambud '))
    
    # BÚSETUFORM
    # =======================================================
    print "Hver er husnæðisstaða þín? Býrðu í eigin húsnæði, leiguhúsnæði/búsetu eða hvorugt?"
    husn = 4
    while husn >3 or husn <1:
        husn = int(raw_input('1: eigin, 2: leigu, 3: hvorugt '))
    
    # TEKJUR OG IÐGJALD
    # =======================================================
    laun_a_manudi = int(raw_input("Laun fyrir skatt: "))
    fjarmagnstekjur = int(raw_input("Fjarmagnstekjur: "))
    
    print "	Iðgjald í lífeyrissjóð?"
    idgjald = 3
    while idgjald >2 or idgjald <1:
        idgjald = int(raw_input('1: 0%, 2: 4% '))
    if idgjald == 1:
        idgjald = 0.0
    elif idgjald == 2:
        idgjald = 0.04
            
    print "	Iðgjald í séreign?"
    sereignaridgjald = 5
    while sereignaridgjald >4 or sereignaridgjald <0:
        sereignaridgjald = int(raw_input('0: 0%, 1: 1%, 2: 2%, 3: 3%, 4: 4% '))
    sereignaridgjald = sereignaridgjald / 100.0
    
    if hjuskaparstada == 3:
        laun_maka = int(raw_input("Laun maka fyrir skatt: "))
        fjarmagnstekjur_maka = int(raw_input("Fjarmagnstekjur maka: "))
    else:
        laun_maka = 0
        fjarmagnstekjur_maka = 0
    tekju_uppl = [laun_a_manudi, fjarmagnstekjur, laun_maka, fjarmagnstekjur_maka]
    
    # EIGNIR
    # =======================================================
    if hjuskaparstada == 3:
        print "Allar eignir (samanlagðar eignir hjóna) að frádregnum öllum skuldum."
        print "Með eignum skal telja hlutabréf, innstæður og verðbréf: "
    else:
        print "Allar eignir að frádregnum öllum skuldum. Með eignum skal telja hlutabréf, innstæður og verðbréf: "
    eignir = int(raw_input())
    
    # HÚSNÆÐISBREYTUR
    # =======================================================
    if husn == 1:   
        print 'Eftirstöðvar í árslok af lánum sem tekin hafa verið til öflunar íbúðarhúsnæðis til eigin nota: '
        eftirstodvar = int(raw_input())
        print "Vextir og verðbætur af íbúðarlánum á ársgrundvelli, þ.m.t. dráttarvextir og lántökukostnaður: "
        vaxtagjold = int(raw_input())
    else:
        eftirstodvar = 0
        vaxtagjold = 0
    if husn == 2:
        fjoldi_heimilismanna = int(raw_input("fjoldi heimilismanna ad ther medtoldum: "))
        if fjoldi_heimilismanna > 4:
            fjoldi_heimilismanna = 4
        if fjoldi_heimilismanna == 1:
            heimilistekjur = (tekju_uppl[0] + tekju_uppl[1])
            heimiliseignir = eignir
        elif fjoldi_heimilismanna == 2 and hjuskaparstada == 3:
            heimilistekjur = sum(tekju_uppl)
            heimiliseignir = eignir
        else:
            heimilistekjur = int(raw_input('samanlagdar skattskyldar tekjur fyrir skatt allra heimilismanna: '))
            heimiliseignir = int(raw_input('samanlagdar eignir allra heimilismanna: '))
        husnaediskostnadur = int(raw_input('manadarlegur husnaediskostnadur: '))
    else: 
        fjoldi_heimilismanna = 0
        heimilistekjur = 0
        heimiliseignir = 0
        husnaediskostnadur = 0
        
    # BÖRN
    # =======================================================
    if hjuskaparstada != 1:    
        print "Fjöldi barna á heimli: "
        fj_barna = int(raw_input())
        if fj_barna != 0:
            print " - þar af yngri en 7 ára: "
            fj_barna_undir_7 = fj_barna + 1
            while fj_barna_undir_7 > fj_barna:
                fj_barna_undir_7 = int(raw_input())
        elif fj_barna == 0:
            fj_barna_undir_7 = 0
        if fj_barna > 3:
            fj_barna = 3
    else:
        fj_barna = fj_barna_undir_7 = 0
        
    # ÖRORKA
    # =======================================================
    aldur = -1
    while aldur <= 0:
        aldur = int(raw_input("Aldur?"))
    
    if aldur < 67:
        print "Hlutfall örorku?"
        ororkuhlutfall = int(raw_input("Hlutfall i prosentum: "))
        if ororkuhlutfall > 0:
            if ororkuhlutfall >= 75:
                print "Fyrsta 75% örorkumat?"
                fyrsta_75_mat = int(raw_input("Aldur vid fyrsta mat: "))
            else:
                fyrsta_75_mat = 0
            print "Býrðu einn?"
            byr_einn = 2
            while byr_einn <0 or byr_einn >1:
                byr_einn = int(raw_input("0: by ein/n, 1: by ekki ein/n: "))
            print "Hreyfihömlunarmat?"
            hreyfihomlun = 3
            while hreyfihomlun <0 or hreyfihomlun >2:
                hreyfihomlun = int(raw_input("0: Nei, 1: Ja, bensinstyrkur fra TR, 2: Ja, uppbot v/reksturs bifreidar fra TR"))
            if fj_barna >0:
                medlag_fj = 100
                while medlag_fj > fj_barna:
                    medlag_fj = int(raw_input("Fjoldi barna sem medlag faest greitt med fra TR: "))
            else:
                medlag_fj = 0
        else:
            ororkuhlutfall = fyrsta_75_mat = byr_einn = hreyfihomlun = medlag_fj = 0

    else:
        ororkuhlutfall = fyrsta_75_mat = byr_einn = hreyfihomlun = medlag_fj = 0
    
    # ELLILÍFEYRIR
    # =======================================================
    if aldur >= 67:
        print "Býrðu einn?"
        byr_einn = 2
        while byr_einn <0 or byr_einn >1:
            byr_einn = int(raw_input("0: by ein/n, 1: by ekki ein/n: "))
        print "Hreyfihömlunarmat?"
        hreyfihomlun = 3
        while hreyfihomlun <0 or hreyfihomlun >2:
            hreyfihomlun = int(raw_input("0: Nei, 1: Ja, bensinstyrkur fra TR, 2: Ja, uppbot v/reksturs bifreidar fra TR"))
        frestun_ellilif = 61
        while frestun_ellilif > 60 or frestun_ellilif < 0:
            frestun_ellilif = int(raw_input('Fresun ellilifeyris, 0-60 manudir: '))
    else:
        frestun_ellilif = byr_einn = 0
    
    
    # =======================================================
    
    bakgrunnsuppl = {'hjuskaparstada': hjuskaparstada,
                    'busetuform': husn,
                    'tekjur': tekju_uppl,
                    'eignir': eignir,
                    'husnaedislan': eftirstodvar,
                    'vaxtagjold': vaxtagjold,
                    'husnaediskostnadur': husnaediskostnadur,
                    'fjoldi_heimilismanna': fjoldi_heimilismanna,
                    'heimilistekjur': heimilistekjur,
                    'heimiliseignir': heimiliseignir,
                    'fjoldi_barna': fj_barna,
                    'fjoldi_barna_undir_7': fj_barna_undir_7,
                    'idgjald': idgjald,
                    'sereignaridgjald': sereignaridgjald,
                    'ororkuhlutfall': ororkuhlutfall,
                    'fyrsta_75_mat': fyrsta_75_mat,
                    'byr_einn': byr_einn,
                    'hreyfihomlun': hreyfihomlun,
                    'medlag_fj': medlag_fj,
                    'aldur': aldur,
                    'frestun_ellilifeyris': frestun_ellilif
                    }
    
    return bakgrunnsuppl

def stadgreidsla_func(info):
    
    skattthrep = 834707
    skatthlutfall_nedra = 0.3694
    skatthlutfall_efra = 0.4624
    personuafsl = 52907
    
    lifeyrir = (info['tekjur'][0] * info['idgjald'])
    serlifeyrir = (info['tekjur'][0] * info['sereignaridgjald'])
    
    stofn = info['tekjur'][0] - lifeyrir - serlifeyrir
    
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
    if stadgreidsla_alls < 0:
        stadgreidsla_alls = 0
    
    laun_e_skatt = stofn - stadgreidsla_alls
    
    return laun_e_skatt, stadgreidsla_alls, lifeyrir, serlifeyrir

def stadgreidsla_small_func(stofn):
    
    skattthrep = 834707
    skatthlutfall_nedra = 0.3694
    skatthlutfall_efra = 0.4624
    personuafsl = 52907
    
    if stofn <= skattthrep:
        skattstofn_1 = stofn
        skattstofn_2 = 0
    else:
        skattstofn_1 = skattthrep
        skattstofn_2 = stofn - skattthrep
        
    skattur_nedra_threp = (skattstofn_1*skatthlutfall_nedra)
    skattur_efra_threp = (skattstofn_2*skatthlutfall_efra)
    
    reiknud_stadgreidsla = skattur_nedra_threp + skattur_efra_threp
    stadgreidsla_alls = reiknud_stadgreidsla #- personuafsl
    
    laun_e_skatt = stofn - stadgreidsla_alls
    
    return laun_e_skatt, stadgreidsla_alls

def husnaedisstudningur_func(info, ororka, ellilif):

    if info['busetuform'] == 1:      
        studningur = vaxtabaetur_func(info, ororka, ellilif)
        
    elif info['busetuform'] == 2:
        studningur = husnaedisbaetur_func(info, ororka, ellilif)
        
    else:
        studningur = 0
    
    return studningur

def vaxtabaetur_func(info, ororka, ellilif):
    
    hamark_vaxtagjalda = [800000, 1000000, 1200000] #fyrir: [einstakling, einstætt foreldri, hjón]
    hamark_bota = [400000, 500000, 600000] #fyrir: [einstakling, einstætt foreldri, hjón]
    tekjur_yearly = [info['tekjur'][0]*12,\
                     info['tekjur'][1]*12,\
                     info['tekjur'][2]*12,\
                     info['tekjur'][3]*12]
    ororka_yearly = 12*ororka
    ellilif_yearly = 12*ellilif
    
    eignaskerdingarmork_nedri = [4500000.0, 4500000.0, 7300000.0] #fyrir: [einstakling, einstætt foreldri, hjón]
    eignaskerdingarmork_efri = [7200000.0, 7200000.0, 11680000.0] #fyrir: [einstakling, einstætt foreldri, hjón]

    stofn_list = [hamark_vaxtagjalda[info['hjuskaparstada']-1], 
                  0.07*info['husnaedislan'], 
                  info['vaxtagjold']]
    stofn =  min(float(s) for s in stofn_list)
    
    tekjuskerding = (0.085 * (sum(tekjur_yearly) + ororka_yearly + ellilif_yearly))
    baetur = stofn - tekjuskerding
    if baetur < 0:
        baetur = 0
    
    if info['eignir'] >= eignaskerdingarmork_efri[info['hjuskaparstada']-1]:
        eignaskerding = baetur
        baetur = 0
        
    elif info['eignir'] >= eignaskerdingarmork_nedri[info['hjuskaparstada']-1]:
        eignaskerding =\
            baetur *\
            ((info['eignir'] - eignaskerdingarmork_nedri[info['hjuskaparstada']-1]) /
            (eignaskerdingarmork_efri[info['hjuskaparstada']-1] - 
             eignaskerdingarmork_nedri[info['hjuskaparstada']-1]))
        baetur -= eignaskerding
    
    else:
        eignaskerding = 0
            
    if baetur > hamark_bota[info['hjuskaparstada']-1]:
        baetur = hamark_bota[info['hjuskaparstada']-1]

    if info['hjuskaparstada'] == 3:
        baetur = baetur/24 #bætur deilast jafnt milli hjóna
    else:
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

def husnaedisbaetur_func(info, ororka, ellilif):

    grunnfjarhaedir = [372000/12, 492000/12, 576000/12, 624000/12]
    fritekjumark = [3373000/12, 4461064/12, 5222710/12, 5657936/12]
    eignaskerdingarmork_nedri = 6500000.0
    eignaskerdingarmork_efri = 10400000.0
    
    stofn = grunnfjarhaedir[(info['fjoldi_heimilismanna']-1)]
    heimilistekjur = info['heimilistekjur']
    
    if info['fjoldi_heimilismanna'] == 1:
        heimilistekjur += (ororka + ellilif)
    elif info['fjoldi_heimilismanna'] == 2 and info['hjuskaparstada'] == 3:
        heimilistekjur += (ororka + ellilif)
    
    if heimilistekjur <= fritekjumark[info['fjoldi_heimilismanna']-1]:
        baetur = stofn
        tekjuskerding = 0
    else:
        tekjuskerding = 0.09 *\
        (heimilistekjur - fritekjumark[info['fjoldi_heimilismanna']-1])
        baetur = stofn - tekjuskerding
    
    if info['heimiliseignir'] >= eignaskerdingarmork_efri:
        eignaskerding = baetur
        baetur = 0
    elif info['heimiliseignir'] >= eignaskerdingarmork_nedri:
        eignaskerding = baetur *\
            ((info['heimiliseignir'] - eignaskerdingarmork_nedri) /
             (eignaskerdingarmork_efri - eignaskerdingarmork_nedri))
        baetur -= eignaskerding
    else:
        eignaskerding = 0
    
    if baetur > 0.75*info['husnaediskostnadur']:
        baetur = 0.75*info['husnaediskostnadur']
    if baetur < 0:
        baetur = 0
    if tekjuskerding < 0:
        tekjuskerding = 0
    if eignaskerding < 0:
        eignaskerding = 0
            
    return baetur, tekjuskerding, eignaskerding

def barnabaetur_func(info, ororka, ellilif):
    tekjur_yearly = [info['tekjur'][0]*12, 
                     info['tekjur'][1]*12, 
                     info['tekjur'][2]*12, 
                     info['tekjur'][3]*12]
    ororka_yearly = 12*ororka
    ellilif_yearly = 12*ellilif
    
    fj_barna = info['fjoldi_barna']
    fj_barna_undir_7 = info['fjoldi_barna_undir_7']
    
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
    stofn_til_skerdingar = (sum(tekjur_yearly) + ororka_yearly + ellilif_yearly)\
    - skerdingarmork[info['hjuskaparstada']-2]
    if stofn_til_skerdingar < 0:
        stofn_til_skerdingar = 0
        
    almennar_barnabaetur =\
        fjarhaedir_fyrsta_barn[info['hjuskaparstada']-2] +\
        ((fj_barna-1) * fjarhaedir_umfram_born[info['hjuskaparstada']-2]) 
        
    vidbotarbaetur = (fj_barna_undir_7 * vidbotarfjarhaed_hvert_barn_undir_7)
        
    skerding = (skerdingarhlutfoll[fj_barna-1] * stofn_til_skerdingar)
    if skerding > almennar_barnabaetur:
        skerding = almennar_barnabaetur
    skerding_vidbotar = ((fj_barna_undir_7*skerdingarhlutf_vidbot) * stofn_til_skerdingar)
    if skerding_vidbotar > vidbotarbaetur:
        skerding_vidbotar = vidbotarbaetur
    
    baetur = almennar_barnabaetur + vidbotarbaetur - (skerding + skerding_vidbotar)
    if baetur < 0:
        baetur = 0
    
    if info['hjuskaparstada'] == 2:
        return baetur/12
    else:
        return baetur/24 #bætur deilast jafnt milli hjóna

def ororka_func(info):
    """
    Til einfoldunar er gert rad fyrir ad:
        busetuhlutfall = 100%
        hlutfall skattkorts hjá TR = 0%
        greiðslur frá lífeyrissjóðum = 0
        greiðslur úr séreignarsjóðum = 0
        aðrar tekjur = 0 (aðrar tekjur eiga að bætast við launatekjur í útreikningum)
        skattskyldar bætur sveitarfélaga = 0
        afborganir krafna hjá TR = 0
        erlendur grunnlifeyrir = 0
        n.b. aðrar tekjur innihalda ekki fjármagnstekjur
    """
    grunnlifeyrir = 42852.0
    nedri_skerdingarmork_lifeyris = 214602.0
    efri_skerdingarmork_lifeyris = 386010.0
    fritekjumark_fjarmagstekna = 98640.0/12
    fritekjumark_launa = 1315200/12
    fritekjumark_lifeyris = 328800/12
    tekjutrygging = 137226
    tekjutrygging_hamark_tekna = 386010
    heimilisuppbot = 39851
    laun = info['tekjur'][0]
    if info['hjuskaparstada'] == 3:
        fjt =(info['tekjur'][1] + info['tekjur'][3])/2
    else:
        fjt = info['tekjur'][1]
    liftek = info['tekjur'][2] #ATHUGA BREYTA
    barnalifeyrir_per_barn = 31679
    medlag_per_barn = 31679
    framfaersluvidmid_ekki_einn = 227883
    framfaersluvidmid_einn = 280000
    
    ##### TEKJUSKERDINGAR ######
    launatekjur_til_skerdingar =\
        (laun-(laun*(info['idgjald']+info['sereignaridgjald'])))
        # idgjald i lifeyrissjod kemur til fradrattar tekna vid utreikning lifeyris
    fjarmagnstekjur_til_skerdingar = fjt - fritekjumark_fjarmagstekna
    if fjarmagnstekjur_til_skerdingar < 0:
        fjarmagnstekjur_til_skerdingar = 0
    grunnur = launatekjur_til_skerdingar + fjarmagnstekjur_til_skerdingar
        
    tekjuskerding = grunnlifeyrir *\
        ((grunnur - nedri_skerdingarmork_lifeyris) /\
         (efri_skerdingarmork_lifeyris - nedri_skerdingarmork_lifeyris))
    
    if tekjuskerding <0:
        tekjuskerding = 0
        
    ororkulifeyrir = grunnlifeyrir - tekjuskerding
    
    if ororkulifeyrir <0:
        ororkulifeyrir = 0
    
    ##### ALDURSTENGD UPPBÓT ##### 
    if info['fyrsta_75_mat'] <= 24:
        studull = 1
    elif info['fyrsta_75_mat'] <= 27:
        studull = 1 - (0.05 * (info['fyrsta_75_mat'] - 24)) #=> 25=95%, 26=90%, 27=85%
    elif info['fyrsta_75_mat'] <= 39:
        studull = round(0.85 - (0.05 * (info['fyrsta_75_mat'] - 27)),2)
        if (studull*10) % 1 == 0:
            studull -= 0.05
    elif info['fyrsta_75_mat'] <= 45:
        studull = 0.15
    elif info['fyrsta_75_mat'] <= 50:
        studull = 0.10
    elif info['fyrsta_75_mat'] <= 55:
        studull = 0.075
    elif info['fyrsta_75_mat'] <= 60:
        studull = 0.05
    elif info['fyrsta_75_mat'] <= 66:
        studull = 0.025
    else:
        studull = 0
    
    aldurstengd_uppbot = studull * ororkulifeyrir

    ##### TEKJUTRYGGING #####       
    ##
    # tekjurtrygging er rétt hafi viðkomandi engar greiðslur frá lífeyrissjóðum
    # reiknivél TR gerir ekki ráð fyrir tveggja þrepa skerðingu á þeim tekjum
    # hef sent fyrirspurn
    # þegar þetta liggur fyrir þarf að bæta inn þessum faktor og hann telur fyrst í röðinni
    # gr. úr lífeyrissjóð > launatekjur > fjármagnstekjur
    #
    
    if launatekjur_til_skerdingar < nedri_skerdingarmork_lifeyris:
        skerding_laun = 0.3835*(launatekjur_til_skerdingar - fritekjumark_launa)
    else:
        nedri = 0.3835*(nedri_skerdingarmork_lifeyris - fritekjumark_launa)
        efri = 0.1335*(launatekjur_til_skerdingar - nedri_skerdingarmork_lifeyris)
        skerding_laun = efri + nedri
    
    if skerding_laun < 0:
        skerding_laun = 0
    
    if laun == 0:
        if fjt < (nedri_skerdingarmork_lifeyris + fritekjumark_fjarmagstekna):
            skerding_fjt = 0.3835 * (fjt - fritekjumark_fjarmagstekna)
        else:
            nedri = 0.3835 * (nedri_skerdingarmork_lifeyris)
            efri = 0.1335*(fjt - (nedri_skerdingarmork_lifeyris+fritekjumark_fjarmagstekna))
            skerding_fjt = efri + nedri
    elif laun < nedri_skerdingarmork_lifeyris:    
        if fjt < (nedri_skerdingarmork_lifeyris - laun):
            skerding_fjt = 0.3835*(fjt - fritekjumark_fjarmagstekna)
        else:
            nedri = 0.3835 * (nedri_skerdingarmork_lifeyris - laun)
            efri = 0.1335 * (fjt - (nedri_skerdingarmork_lifeyris - laun + fritekjumark_fjarmagstekna))
            skerding_fjt = nedri + efri
    else:
        skerding_fjt = 0.1335 * (fjt - fritekjumark_fjarmagstekna)
        
    if skerding_fjt < 0:
        skerding_fjt = 0
    
    tekjutrygging = tekjutrygging - skerding_laun - skerding_fjt
    if info['tekjur'][0] > tekjutrygging_hamark_tekna:
        tekjutrygging = 0
        
    ##### HEIMILISUPPBÓT #####
    if info['byr_einn'] == 0:
        grunnur_laun = launatekjur_til_skerdingar - fritekjumark_launa
        if grunnur_laun < 0:
            grunnur_laun = 0
        grunnur_liftek = liftek - fritekjumark_lifeyris
        if grunnur_liftek < 0:
            grunnur_liftek = 0
        grunnur_fjt = fjt - fritekjumark_fjarmagstekna
        if grunnur_fjt < 0:
            grunnur_fjt = 0
        grunnur = grunnur_laun + grunnur_liftek + grunnur_fjt

        heimilisuppbot = heimilisuppbot - (0.1114 * grunnur)
    else:
        heimilisuppbot = 0
        
    ##### HREYFIHÖMLUNARMAT #####
    if info['hreyfihomlun'] == 1 or info['hreyfihomlun'] == 2:
        bensinsstyrkur = 15839
    else:
        bensinsstyrkur = 0
        
    ##### BARNALÍFEYRIR #####
    barnalifeyrir = barnalifeyrir_per_barn * info['fjoldi_barna']
    if info['medlag_fj'] > 0:
        medlag = medlag_per_barn * info['medlag_fj']
    else:
        medlag = 0
    
    if info['hjuskaparstada'] == 2:
        if info['fjoldi_barna'] < 2:
            foreldralaun = 0
        if info['fjoldi_barna'] == 2:
            foreldralaun = 9171
        elif info['fjoldi_barna'] > 2:
            foreldralaun = 23844
    else:
        foreldralaun = 0
    
    
    samtals =\
        ororkulifeyrir + aldurstengd_uppbot + tekjutrygging +\
        heimilisuppbot + bensinsstyrkur +\
        barnalifeyrir + medlag + foreldralaun
    
    ##### FRAMFÆRSLUUPPBÓT #####
    grunnur_uppbot = samtals - barnalifeyrir - medlag - bensinsstyrkur +\
        laun + fjt + liftek
    if (grunnur_uppbot < framfaersluvidmid_einn and\
    info['byr_einn'] == 0):
        framfaersluppbot = framfaersluvidmid_einn - (grunnur_uppbot)
    elif (grunnur_uppbot < framfaersluvidmid_ekki_einn and\
    info['byr_einn'] == 1):
        framfaersluppbot = framfaersluvidmid_ekki_einn - (grunnur_uppbot)
    else:
        framfaersluppbot = 0
    
    samtals += framfaersluppbot
    
    skattgrunnur = samtals - barnalifeyrir - medlag
    
    samtals_e_skatt, stadgreidsla = stadgreidsla_small_func(skattgrunnur)
    
    
    """print "ororkulifeyrir: %d" %ororkulifeyrir
    print "aldurstengd uppbot: %d" %aldurstengd_uppbot
    print "tekjutrygging: %d" %tekjutrygging
    print "heimilisuppbot: %d" %heimilisuppbot
    print "framfaersluuppbot: %d" %framfaersluppbot
    print "bensinsstyrkur: %d" %bensinsstyrkur
    print "barnalifeyrir: %d" %barnalifeyrir
    print "maedra-/fedralaun: %d" %foreldralaun
    print "medlag: %d" %medlag
    print ""
    print "Samtals: %d" %samtals
    
    print "skerding launa: %d" %skerding_laun
    print "skerding fjt: %d" %skerding_fjt"""
    
    return samtals, samtals_e_skatt, stadgreidsla, skattgrunnur, ororkulifeyrir,\
            aldurstengd_uppbot, tekjutrygging, heimilisuppbot,\
            bensinsstyrkur, barnalifeyrir, medlag, foreldralaun, framfaersluppbot
        
def ellilifeyrir_func(info):
    '''
    midast vid full rettindi til ellilifeyris (40 ara buseta frá 16-67 ára aldri)
    '''
    
    ellilifeyrir = 228734
    heimilisuppbot = 52316
    uppbot_v_bils = 15839
    radstofunarfe = 68662
    fritekjumork = 25000
    efri_mork_lifeyrir = 533298
    efri_mork_huppbot = 464597
    laun = info['tekjur'][0]
    barnalifeyrir_per_barn = 31679
    medlag_per_barn = 31679
    
    ##### ELLILÍFEYRIR #####
    launatekjur_til_skerdingar =\
        (laun-(laun*(info['idgjald']+info['sereignaridgjald'])))
    tekjur_til_skerdingar =\
        launatekjur_til_skerdingar + info['tekjur'][1]#+lifeyrisgreidslur
        
    if tekjur_til_skerdingar > fritekjumork:
        skerding = 0.45*(tekjur_til_skerdingar - fritekjumork)
        ellilifeyrir -= skerding
        if ellilifeyrir < 0:
            ellilifeyrir = 0
            
    ##### HEIMILISUPPBÓT #####
    if info['byr_einn'] == 0:
        if tekjur_til_skerdingar > fritekjumork:
            skerding = 0.119*(tekjur_til_skerdingar - fritekjumork)
            heimilisuppbot -= skerding
            if heimilisuppbot < 0:
                heimilisuppbot = 0
    else:
        heimilisuppbot = 0
    
    ##### HREYFIHÖMLUNARMAT #####
    if info['hreyfihomlun'] == 1 or info['hreyfihomlun'] == 2:
        bensinsstyrkur = 15839
    else:
        bensinsstyrkur = 0
        
    ##### BARNALÍFEYRIR #####
    barnalifeyrir = barnalifeyrir_per_barn * info['fjoldi_barna']
    if info['medlag_fj'] > 0:
        medlag = medlag_per_barn * info['medlag_fj']
    else:
        medlag = 0
    
    if info['hjuskaparstada'] == 2:
        if info['fjoldi_barna'] < 2:
            foreldralaun = 0
        if info['fjoldi_barna'] == 2:
            foreldralaun = 9171
        elif info['fjoldi_barna'] > 2:
            foreldralaun = 23844
    else:
        foreldralaun = 0
        
    ##### FRESTUN/FLÝTING ELLILIFEYRIS #####
    if info['frestun_ellilifeyris'] > 0:
        ellilifeyrir += ellilifeyrir * (info['frestun_ellilifeyris'] * 0.005)
        heimilisuppbot += heimilisuppbot * (info['frestun_ellilifeyris'] * 0.005)
        
        # bæta inn flýtingu? þá þarf að opna möguleikann á ellilífeyri 2 árum fyrr
    samtals = ellilifeyrir + heimilisuppbot + bensinsstyrkur + barnalifeyrir + medlag + foreldralaun
    
    skattgrunnur = samtals - barnalifeyrir - medlag
    
    samtals_e_skatt, stadgreidsla = stadgreidsla_small_func(skattgrunnur)
    
    return samtals, samtals_e_skatt, stadgreidsla, skattgrunnur,\
        ellilifeyrir, heimilisuppbot, bensinsstyrkur,\
        barnalifeyrir, medlag, foreldralaun
        
def print_dict(person_dict):
    print ""
    print ""
    print "==========LAUN============"
    print "Laun fyrir skatt: {:,}".format(person_dict['tekjur'][0])
    print " - staðgreiðsla: {:,}".format(person_dict['stadgreidsla'])
    print " - greitt i lifeyrissparnad: {:,}".format(person_dict['lifeyrisgreidsla'])
    print "Útborguð laun: {:,}".format(person_dict['tekjur_e_skatt'])
    print ""
    if person_dict['tekjur'][1] > 0:
        print "========FJÁRMAGNSTEKJUR=========="
        print "Fjármagnstekjur fyrir skatt: {:,}".format(person_dict['tekjur'][1])
        print " - fjármagnstekjuskattur: {:,}".format(0.2* person_dict['tekjur'][1])
        print ""
    print "====HÚSNÆÐISSTUÐNINGUR============"
    print "Húsnæðisstuðningur á mánuði: {:,}".format(person_dict['husnaedisstudningur'])
    print ""
    print "====BARNABÆTUR========="
    print "Barnabætur á mánuði: {:,}".format(person_dict['barnabaetur'])
    print ""
    
    if person_dict['ororka_alls'] > 0:
        print "=====ÖRORKUBÆTUR======"
        print "Samtals örorkubætur á mánuði: {:,}".format(person_dict['ororka_alls'])
        if person_dict['ororka_stadgreidsla'] > 0:
            print " - Frádreginn skattur: {:,}".format(person_dict['ororka_stadgreidsla'])
            print "Samtals örorkubætur eftir skatt: {:,}".format(person_dict['ororka_e_skatt'])
        print "== Sundurliðaðar örorkubætur =="
        print " örorkulífeyrir: {:,}".format(person_dict['ororkulifeyrir'])
        print " aldurstengd örorkuuppbót: {:,}".format(person_dict['aldurstengd_ororkuuppbot'])
        if person_dict['tekjutrygging_ororka'] > 0:
            print " tekjutrygging: {:,}".format(person_dict['tekjutrygging_ororka'])
        if person_dict['heimilisuppbot_ororka'] > 0:
            print " heimilisuppbót: {:,}".format(person_dict['heimilisuppbot_ororka'])
        if person_dict['bensinsstyrkur_ororka'] > 0:
            print " bensínstyrkur: {:,}".format(person_dict['bensinsstyrkur_ororka'])
        if person_dict['barnalifeyrir_ororka'] > 0:
            print " barnalífeyrir: {:,}".format(person_dict['barnalifeyrir_ororka'])
        if person_dict['medlag_ororka'] > 0:
            print " meðlag: {:,}".format(person_dict['medlag_ororka'])
        if person_dict['foreldralaun_ororka'] > 0:
            print " foreldralaun: {:,}".format(person_dict['foreldralaun_ororka'])
        if person_dict['framfaersluppbot_ororka'] > 0:
            print " framfærsluuppbót: {:,}".format(person_dict['framfaersluppbot_ororka'])
        print ""
    
    if person_dict['samtals_elli'] > 0:
        print "=====ELLILÍFEYRIR====="
        print "Samtals ellilífeyrir á mánuði: {:,}".format(person_dict['samtals_elli'])
        if person_dict['ellilif_stadgreidsla'] > 0:
            print " - Frádreginn skattur: {:,}".format(person_dict['ellilif_stadgreidsla'])
            print "Samtals ellilífeyrir eftir skatt: {:,}".format(person_dict['ellilifeyrir_e_skatt'])
        print "== Sundurliðaður ellilífeyrir =="
        print " ellilífeyrir: {:,}".format(person_dict['ellilifeyrir'])
        if person_dict['heimilisuppbot_ellifeyrir'] > 0:
            print " heimilisuppbót: {:,}".format(person_dict['heimilisuppbot_ellifeyrir'])
        if person_dict['bensinstyrkur_elli'] > 0:
            print " bensínstyrkur: {:,}".format(person_dict['bensinstyrkur_elli'])
        if person_dict['barnalifeyrir_elli'] > 0:
            print " barnalífeyrir: {:,}".format(person_dict['barnalifeyrir_elli'])
        if person_dict['medlag_elli'] > 0:
            print " meðlag: {:,}".format(person_dict['medlag_elli'])
        if person_dict['foreldralaun_elli'] > 0:
            print " foreldralaun: {:,}".format(person_dict['foreldralaun_elli'])
        print ""
        
    print "=====FRÁDRÁTTUR========"
    print "Útvarpsgjald: {:,}".format(person_dict['utvarpsgjald'])
    print ""
    print ""
    print "====NIÐURSTAÐA========"
    print "Nettó tekjur í hverjum mánuði: {:,}".format(person_dict['pjeng_i_vasa'])
    print "======================"
    
def vasapeningur(bakgrunnsuppl):
    tekjur_e_skatt, stadgreidsla, lifeyrisgreidsla, sereignarlifeyrisgr = stadgreidsla_func(bakgrunnsuppl)
    
    if bakgrunnsuppl['tekjur'][0] >= 1678001/12:
        utvarpsgjald = 16800/12
    else: utvarpsgjald = 0
    
    if bakgrunnsuppl['ororkuhlutfall'] > 0:
        samtals_ororka, ororka_e_skatt, ororka_stadgreidsla, ororka_skattgrunnur,\
        ororkulifeyrir, aldurstengd_uppbot, tekjutrygging,\
        heimilisuppbot, bensinsstyrkur, barnalifeyrir, medlag,\
        foreldralaun, framfaersluppbot = ororka_func(bakgrunnsuppl)
    else: 
        samtals_ororka = ororka_e_skatt = ororka_stadgreidsla = ororka_skattgrunnur =\
        ororkulifeyrir = aldurstengd_uppbot = tekjutrygging =\
        heimilisuppbot = bensinsstyrkur = barnalifeyrir =\
        medlag = foreldralaun = framfaersluppbot = 0
        
    if bakgrunnsuppl['aldur'] > 67:
        samtals_elli, ellilifeyrir_e_skatt, ellilif_stadgreidsla, elli_skattgrunnur,\
        ellilifeyrir, heimilisuppbot_elli, bensinsstyrkur_elli,\
        barnalifeyrir_elli, medlag_elli, foreldralaun_elli = ellilifeyrir_func(bakgrunnsuppl)
    else:
        samtals_elli = ellilifeyrir_e_skatt = ellilif_stadgreidsla = elli_skattgrunnur =\
        ellilifeyrir = heimilisuppbot_elli = bensinsstyrkur_elli =\
        barnalifeyrir_elli = medlag_elli = foreldralaun_elli = 0
    
    husnaedisstudningur, husn_tekjuskerding, husn_eignaskerding =\
        husnaedisstudningur_func(bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
    if bakgrunnsuppl['hjuskaparstada'] != 1:
        barnabaetur = barnabaetur_func(bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
    else: barnabaetur = 0
    
    fjarmagnstekjur_e_skatt = bakgrunnsuppl['tekjur'][1] - (bakgrunnsuppl['tekjur'][1] * 0.2)
    
    netto = tekjur_e_skatt + fjarmagnstekjur_e_skatt + husnaedisstudningur +\
    barnabaetur + ororka_e_skatt + ellilifeyrir_e_skatt - utvarpsgjald
    
    nidurstodur = {'tekjur': bakgrunnsuppl['tekjur'],
                   'tekjur_e_skatt': tekjur_e_skatt,
                   'fjarmagnstekjur_e_skatt': fjarmagnstekjur_e_skatt,
                   'stadgreidsla': stadgreidsla,
                   'lifeyrisgreidsla': (lifeyrisgreidsla+sereignarlifeyrisgr),
                   'husnaedisstudningur': husnaedisstudningur,
                   'husnaedisstudningur_eignaskerd': husn_eignaskerding,
                   'husnaedisstudningur_tekjuskerd': husn_tekjuskerding,
                   'barnabaetur': barnabaetur,
                   'utvarpsgjald': utvarpsgjald,
                   'pjeng_i_vasa': netto,
                   'ororka_alls': samtals_ororka,
                   'ororka_e_skatt': ororka_e_skatt,
                   'ororka_stadgreidsla': ororka_stadgreidsla,
                   'ororkulifeyrir': ororkulifeyrir,
                   'aldurstengd_ororkuuppbot': aldurstengd_uppbot,
                   'tekjutrygging_ororka': tekjutrygging,
                   'heimilisuppbot_ororka': heimilisuppbot,
                   'bensinsstyrkur_ororka': bensinsstyrkur,
                   'barnalifeyrir_ororka': barnalifeyrir,
                   'medlag_ororka': medlag,
                   'foreldralaun_ororka': foreldralaun,
                   'framfaersluppbot_ororka': framfaersluppbot,
                   'ellilifeyrir': ellilifeyrir,
                   'ellilifeyrir_e_skatt': ellilifeyrir_e_skatt,
                   'ellilif_stadgreidsla': ellilif_stadgreidsla,
                   'heimilisuppbot_ellifeyrir': heimilisuppbot_elli,
                   'bensinstyrkur_elli': bensinsstyrkur_elli,
                   'barnalifeyrir_elli': barnalifeyrir_elli,
                   'medlag_elli': medlag_elli,
                   'foreldralaun_elli': foreldralaun_elli,
                   'samtals_elli': samtals_elli}
    
    return nidurstodur