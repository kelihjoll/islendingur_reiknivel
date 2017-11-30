# -*- coding: utf-8 -*-

forsendur_dict = {'utvarpsgjald_threshold_m': 1678001/12,
                 'utvarpsgjald_m': 16800/12,
                 'eftirlaunaaldur': 67,
                 'serstakar_tekjusk_nedri_m': [281083.0, 371755.0, 435226.0, 471495.0],
                 'serstakar_tekjusk_efri_m': [351354, 464694, 544032, 589368],
                 'serstakar_threshold_eign': 5126000,
                 'serstakar_lagmarks_leiga': 40000,
                 'serstakar_plus_venjulegar_hamark': 90000,
                 'stadgr_threp_m': 834707,
                 'stadgr_hlutfall_nedra': 0.3694,
                 'stadgr_hlutfall_efra': 0.4624,
                 'personuafslattur_m': 52907,
                 'hamark_vaxtagjalda_y': [800000, 1000000, 1200000],
                 'hamark_vaxtabota_y': [400000, 500000, 600000],
                 'vaxtab_eignask_nedri': [4500000.0, 4500000.0, 7300000.0],
                 'vaxtab_eignask_efri': [7200000.0, 7200000.0, 11680000.0],
                 'vaxtab_tekjusk_hlutfall': 0.085,
                 'vaxtab_hamarkshl_huslans': 0.07,
                 'husnb_grunnur_m': [372000/12, 492000/12, 576000/12, 624000/12],
                 'husnb_fritekjumark_m': [3373000/12, 4461064/12, 5222710/12, 5657936/12],
                 'husnb_eignask_nedri': 6500000.0,
                 'husnb_eignask_efri': 10400000.0,
                 'husnb_tekjusk_hlutfall': 0.09,
                 'husnb_hamarkshluti_husnkostn': 0.75,
                 'barnab_skerdingarhlutfoll': [0.04, 0.06, 0.08],
                 'barnab_skerdingarhl_vidbot': 0.04,
                 'barnab_fjarh_fyrsta_barn_y': [342939, 205834],
                 'barnab_fjarh_umfram_born_y': [351787, 245087],
                 'barnab_fjarh_barn_undir_7_y': 122879,
                 'barnab_tekjuskmork': [2700000, 5400000],
                 'ororka_grunnur': 42852.0,
                 'ororka_tekjusk_nedri': 214602.0,
                 'ororka_tekjusk_efri': 386010.0,
                 'ororka_fritekjumark_fjtekna_m': 98640.0/12,
                 'ororka_fritekjumark_launa_m': 1315200/12,
                 'ororka_fritekjumark_lifeyris_m': 328800/12,
                 'ororka_tekjutr_m': 137226,
                 'ororka_tekjutr_hamark_tekna_m': 386010,
                 'ororka_heimilisuppbot_m': 39851,
                 'barnalifeyrir/barn': 31679,
                 'medlag/barn': 31679,
                 'ororka_framfvidmid_ekkieinn': 227883,
                 'ororka_framfvidmid_einn': 280000,
                 'ororka_tekjutr_skerdingarhlutf_nedri': 0.3835,
                 'ororka_tekjutr_skerdingarhlutf_efri': 0.1335,
                 'ororka_heimilisuppbot_skerdingarhlutf': 0.114,
                 'ororka_bensinstyrkur_m': 15839,
                 'foreldralaun_2born_m': 9171,
                 'foreldralaun_fleiri_born_m': 23844,
                 'ellilif_lifeyrir_m': 228734,
                 'ellilif_heimilisuppbot_m': 52316,
                 'ellilif_bensinstyrkur_m': 15839,
                 'ellilif_radstofunarfe_m': 68662,
                 'ellilif_fritekjumork': 25000,
                 'ellilif_lifeyrir_efri_mork_m': 533298,
                 'ellilif_heimilisuppbot_efri_mork_m': 464597,
                 'ellilif_lifeyrir_tekjusk_hlutf': 0.45,
                 'ellilif_huppbot_tekjusk_hlutf': 0.119,
                 'ellilif_haekkun_v_frestunar': 0.05
                }

def islendingur(forsendur = forsendur_dict, bakgrunnsuppl = 0):
    if bakgrunnsuppl == 0:
        bakgrunnsuppl = input_bakgrunnsuppl(forsendur)
        
    tekjur_e_skatt, stadgreidsla, lifeyrisgreidsla, sereignarlifeyrisgr = stadgreidsla_func(forsendur, bakgrunnsuppl)
    
    if bakgrunnsuppl['tekjur'][0] >= forsendur['utvarpsgjald_threshold_m']:
        utvarpsgjald = forsendur['utvarpsgjald_m']
    else: utvarpsgjald = 0
    
    if bakgrunnsuppl['ororkuhlutfall'] > 0:
        samtals_ororka, ororka_e_skatt, ororka_stadgreidsla, ororka_skattgrunnur,\
        ororkulifeyrir, aldurstengd_uppbot, tekjutrygging,\
        heimilisuppbot, bensinsstyrkur, barnalifeyrir, medlag,\
        foreldralaun, framfaersluppbot = ororka_func(forsendur, bakgrunnsuppl)
    else: 
        samtals_ororka = ororka_e_skatt = ororka_stadgreidsla = ororka_skattgrunnur =\
        ororkulifeyrir = aldurstengd_uppbot = tekjutrygging =\
        heimilisuppbot = bensinsstyrkur = barnalifeyrir =\
        medlag = foreldralaun = framfaersluppbot = 0
        
    if bakgrunnsuppl['aldur'] > forsendur['eftirlaunaaldur']:
        samtals_elli, ellilifeyrir_e_skatt, ellilif_stadgreidsla, elli_skattgrunnur,\
        ellilifeyrir, heimilisuppbot_elli, bensinsstyrkur_elli,\
        barnalifeyrir_elli, medlag_elli, foreldralaun_elli = ellilifeyrir_func(forsendur, bakgrunnsuppl)
    else:
        samtals_elli = ellilifeyrir_e_skatt = ellilif_stadgreidsla = elli_skattgrunnur =\
        ellilifeyrir = heimilisuppbot_elli = bensinsstyrkur_elli =\
        barnalifeyrir_elli = medlag_elli = foreldralaun_elli = 0
    
    husnaedisstudningur, husn_tekjuskerding, husn_eignaskerding =\
        husnaedisstudningur_func(forsendur, bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
    if bakgrunnsuppl['hjuskaparstada'] != 1:
        barnabaetur = barnabaetur_func(forsendur, bakgrunnsuppl, ororka_skattgrunnur, elli_skattgrunnur)
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

def input_bakgrunnsuppl(forsendur):
    aldur = -1
    while aldur <= 0:
        aldur = int(raw_input("Aldur?"))
        
    # HJÚSKAPARSTAÐA
    # =======================================================
    hjuskaparstada = 4
    while hjuskaparstada >3 or hjuskaparstada <1:
        hjuskaparstada = int(raw_input('1: einhleypur, 2: einst. foreldri, 3: giftur/sambud '))
    
    # TEKJUR OG IÐGJALD
    # =======================================================
    laun_a_manudi = int(raw_input("Laun fyrir skatt: "))
    fjarmagnstekjur = int(raw_input("Fjarmagnstekjur: "))
    
    if laun_a_manudi != 0:
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
       
    else:
        idgjald = sereignaridgjald = 0

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
    
    # BÚSETUFORM
    # =======================================================
    print "Hver er husnæðisstaða þín? Býrðu í eigin húsnæði, leiguhúsnæði/búsetu eða hvorugt?"
    husn = 4
    while husn >3 or husn <1:
        husn = int(raw_input('1: eigin, 2: leigu/busetu, 3: hvorugt '))
    
    # HÚSNÆÐISBREYTUR
    # =======================================================
    serstakar_tekjumork = forsendur['serstakar_tekjusk_efri_m']
    serstakar_eignamork = forsendur['serstakar_threshold_eign']
    
    if husn == 1:   
        print 'Eftirstöðvar í árslok af lánum sem tekin hafa verið til öflunar íbúðarhúsnæðis til eigin nota: '
        eftirstodvar = int(raw_input())
        print "Vextir og verðbætur af íbúðarlánum á ársgrundvelli, þ.m.t. dráttarvextir og lántökukostnaður: "
        vaxtagjold = int(raw_input())
    else:
        eftirstodvar = 0
        vaxtagjold = 0
    if husn == 2:
        husnaediskostnadur = int(raw_input('manadarlegur husnaediskostnadur: '))
        fjoldi_heimilismanna = int(raw_input("fjoldi heimilismanna ad ther medtoldum: "))
        if fjoldi_heimilismanna > 4:
            fjoldi_heimilismanna = 4
            
        if fjoldi_heimilismanna == 1:
            heimilistekjur = 0
            heimiliseignir = eignir
        elif fjoldi_heimilismanna == 2 and hjuskaparstada == 3:
            heimilistekjur = 0
            heimiliseignir = eignir
        else:
            heimilistekjur = int(raw_input('samanlagdar skattskyldar tekjur annarra heimilismanna en þín: '))
            heimiliseignir = int(raw_input('samanlagdar eignir allra heimilismanna: '))
            
        if (heimilistekjur + sum(tekju_uppl)) < (serstakar_tekjumork[fjoldi_heimilismanna-1]) and\
            heimiliseignir < serstakar_eignamork and\
            husnaediskostnadur > forsendur['serstakar_lagmarks_leiga']:
                serstakar = 3
                while serstakar > 2 or serstakar < 1:
                    serstakar = int(raw_input("Attu rett a serstokum husaleigubotum? 1: Ja. 2: Nei. "))
        else:
            serstakar = 0
        
    else: 
        fjoldi_heimilismanna = 0
        heimilistekjur = 0
        heimiliseignir = 0
        husnaediskostnadur = 0
        serstakar = 0
        
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
    if aldur < forsendur['eftirlaunaaldur']:
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
    if aldur >= forsendur['eftirlaunaaldur']:
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
                    'frestun_ellilifeyris': frestun_ellilif,
                    'serstakar': serstakar
                    }
    
    return bakgrunnsuppl

def stadgreidsla_func(forsendur, info):
    
    skattthrep = forsendur['stadgr_threp_m']
    skatthlutfall_nedra = forsendur['stadgr_hlutfall_nedra']
    skatthlutfall_efra = forsendur['stadgr_hlutfall_efra']
    personuafsl = forsendur['personuafslattur_m']
    
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

def stadgreidsla_small_func(forsendur, stofn):
    
    skattthrep = forsendur['stadgr_threp_m']
    skatthlutfall_nedra = forsendur['stadgr_hlutfall_nedra']
    skatthlutfall_efra = forsendur['stadgr_hlutfall_efra']
    personuafsl = forsendur['personuafslattur_m']
    
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

def husnaedisstudningur_func(forsendur, info, ororka, ellilif):

    if info['busetuform'] == 1:      
        studningur, tekjuskerding, eignaskerding = vaxtabaetur_func(forsendur, info, ororka, ellilif)
        
    elif info['busetuform'] == 2:
        studningur, tekjuskerding, eignaskerding, heimilistekjur = husnaedisbaetur_func(forsendur, info, ororka, ellilif)
        if info['serstakar'] == 1:
            serstakar = serstakar_func(forsendur, info, ororka, ellilif, studningur)
            studningur += serstakar
        
    else:
        studningur = 0
    
    return studningur, tekjuskerding, eignaskerding

def vaxtabaetur_func(forsendur, info, ororka, ellilif):
    
    hamark_vaxtagjalda = forsendur['hamark_vaxtagjalda_y'] #fyrir: [einstakling, einstætt foreldri, hjón]
    hamark_bota = forsendur['hamark_vaxtabota_y'] #fyrir: [einstakling, einstætt foreldri, hjón]
    tekjur_yearly = [info['tekjur'][0]*12,\
                     info['tekjur'][1]*12,\
                     info['tekjur'][2]*12,\
                     info['tekjur'][3]*12]
    ororka_yearly = 12*ororka
    ellilif_yearly = 12*ellilif
    tekjur = sum(tekjur_yearly) + ororka_yearly + ellilif_yearly
    
    eignaskerdingarmork_nedri = forsendur['vaxtab_eignask_nedri'] #fyrir: [einstakling, einstætt foreldri, hjón]
    eignaskerdingarmork_efri = forsendur['vaxtab_eignask_efri'] #fyrir: [einstakling, einstætt foreldri, hjón]

    stofn_list = [hamark_vaxtagjalda[info['hjuskaparstada']-1], 
                  forsendur['vaxtab_hamarkshl_huslans']*info['husnaedislan'], 
                  info['vaxtagjold']]
    stofn =  min(float(s) for s in stofn_list)
    
    tekjuskerding = forsendur['vaxtab_tekjusk_hlutfall'] * tekjur
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

def husnaedisbaetur_func(forsendur, info, ororka, ellilif):

    tekjur = info['heimilistekjur'] + sum(info['tekjur']) + ororka + ellilif
    
    grunnfjarhaedir = forsendur['husnb_grunnur_m']
    fritekjumark = forsendur['husnb_fritekjumark_m']
    eignaskerdingarmork_nedri = forsendur['husnb_eignask_nedri']
    eignaskerdingarmork_efri = forsendur['husnb_eignask_efri']
    
    stofn = grunnfjarhaedir[(info['fjoldi_heimilismanna']-1)]
    heimilistekjur = info['heimilistekjur']

    if heimilistekjur <= fritekjumark[info['fjoldi_heimilismanna']-1]:
        baetur = stofn
        tekjuskerding = 0
    else:
        tekjuskerding = forsendur['husnb_tekjusk_hlutfall'] *\
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
    
    if baetur > forsendur['husnb_hamarkshluti_husnkostn']*\
    info['husnaediskostnadur']:
        baetur = forsendur['husnb_hamarkshluti_husnkostn']*\
        info['husnaediskostnadur']
    if baetur < 0:
        baetur = 0
    if tekjuskerding < 0:
        tekjuskerding = 0
    if eignaskerding < 0:
        eignaskerding = 0
            
    return baetur, tekjuskerding, eignaskerding, heimilistekjur

def serstakar_func(forsendur, info, ororka, ellilif, studningur):
    upphaf_skerdingar = forsendur['serstakar_tekjusk_nedri_m']
    lok_skerdingar = forsendur['serstakar_tekjusk_efri_m']
    serstakar_eignamork = forsendur['serstakar_threshold_eign']
    
    serstakar = studningur
    if info['heimiliseignir'] > serstakar_eignamork:
        serstakar = 0
    
    tekjur = info['heimilistekjur'] + sum(info['tekjur']) + ororka + ellilif
    
    tekjuskerding =\
        serstakar * ((tekjur - upphaf_skerdingar[info['fjoldi_heimilismanna']-1]) /
         (lok_skerdingar[info['fjoldi_heimilismanna']-1] - upphaf_skerdingar[info['fjoldi_heimilismanna']-1]))
    print tekjuskerding
    serstakar -= tekjuskerding
    
    if serstakar < 0:
        serstakar = 0
    
    if studningur + serstakar > forsendur['serstakar_plus_venjulegar_hamark']:
        serstakar = forsendur['serstakar_plus_venjulegar_hamark'] - studningur
        
    return serstakar, tekjuskerding

def barnabaetur_func(forsendur, info, ororka, ellilif):
    tekjur_yearly = [info['tekjur'][0]*12, 
                     info['tekjur'][1]*12, 
                     info['tekjur'][2]*12, 
                     info['tekjur'][3]*12]
    ororka_yearly = 12*ororka
    ellilif_yearly = 12*ellilif
    
    fj_barna = info['fjoldi_barna']
    fj_barna_undir_7 = info['fjoldi_barna_undir_7']
    
    # SKERÐINGARHLUFÖLL
    skerdingarhlutfoll = forsendur['barnab_skerdingarhlutfoll'] # [1 barn, 2 börn, 3 börn eða fleiri]
    skerdingarhlutf_vidbot = forsendur['barnab_skerdingarhl_vidbot']
    
    # FJÁRHÆÐIR 2017
    fjarhaedir_fyrsta_barn = forsendur['barnab_fjarh_fyrsta_barn_y'] # [einstætt foreldri, hjón/sambúðarfólk]
    fjarhaedir_umfram_born = forsendur['barnab_fjarh_umfram_born_y'] # [einstætt foreldri, hjón/sambúðarfólk]
    vidbotarfjarhaed_hvert_barn_undir_7 = forsendur['barnab_fjarh_barn_undir_7_y']
    
    # SKERÐINGARMÖRK
    skerdingarmork = forsendur['barnab_tekjuskmork'] # [einstætt foreldri, hjón/sambúðarfólk]
    
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

def ororka_func(forsendur, info):
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
    grunnlifeyrir = forsendur['ororka_grunnur']
    nedri_skerdingarmork_lifeyris = forsendur['ororka_tekjusk_nedri']
    efri_skerdingarmork_lifeyris = forsendur['ororka_tekjusk_efri']
    fritekjumark_fjarmagstekna = forsendur['ororka_fritekjumark_fjtekna_m']
    fritekjumark_launa = forsendur['ororka_fritekjumark_launa_m']
    fritekjumark_lifeyris = forsendur['ororka_fritekjumark_lifeyris_m']
    tekjutrygging = forsendur['ororka_tekjutr_m']
    tekjutrygging_hamark_tekna = forsendur['ororka_tekjutr_hamark_tekna_m']
    heimilisuppbot = forsendur['ororka_heimilisuppbot_m']
    laun = info['tekjur'][0]
    if info['hjuskaparstada'] == 3:
        fjt =(info['tekjur'][1] + info['tekjur'][3])/2
    else:
        fjt = info['tekjur'][1]
    liftek = 0 #ATHUGA BREYTA
    barnalifeyrir_per_barn = forsendur['barnalifeyrir/barn']
    medlag_per_barn = forsendur['medlag/barn']
    framfaersluvidmid_ekki_einn = forsendur['ororka_framfvidmid_ekkieinn']
    framfaersluvidmid_einn = forsendur['ororka_framfvidmid_einn']
    
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
        nedri = forsendur['ororka_tekjutr_skerdingarhlutf_nedri'] *\
        (nedri_skerdingarmork_lifeyris - fritekjumark_launa)
        efri = forsendur['ororka_tekjutr_skerdingarhlutf_efri'] *\
        (launatekjur_til_skerdingar - nedri_skerdingarmork_lifeyris)
        skerding_laun = efri + nedri
    
    if skerding_laun < 0:
        skerding_laun = 0
    
    if laun == 0:
        if fjt < (nedri_skerdingarmork_lifeyris + fritekjumark_fjarmagstekna):
            skerding_fjt = forsendur['ororka_tekjutr_skerdingarhlutf_nedri'] *\
            (fjt - fritekjumark_fjarmagstekna)
        else:
            nedri = forsendur['ororka_tekjutr_skerdingarhlutf_nedri'] *\
            (nedri_skerdingarmork_lifeyris)
            efri = forsendur['ororka_tekjutr_skerdingarhlutf_efri'] *\
            (fjt - (nedri_skerdingarmork_lifeyris+fritekjumark_fjarmagstekna))
            skerding_fjt = efri + nedri
    elif laun < nedri_skerdingarmork_lifeyris:    
        if fjt < (nedri_skerdingarmork_lifeyris - laun):
            skerding_fjt = forsendur['ororka_tekjutr_skerdingarhlutf_nedri'] *\
            (fjt - fritekjumark_fjarmagstekna)
        else:
            nedri = forsendur['ororka_tekjutr_skerdingarhlutf_nedri'] *\
            (nedri_skerdingarmork_lifeyris - laun)
            efri = forsendur['ororka_tekjutr_skerdingarhlutf_efri'] *\
            (fjt - (nedri_skerdingarmork_lifeyris - laun + fritekjumark_fjarmagstekna))
            skerding_fjt = nedri + efri
    else:
        skerding_fjt = forsendur['ororka_tekjutr_skerdingarhlutf_efri'] *\
        (fjt - fritekjumark_fjarmagstekna)
        
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
        bensinsstyrkur = forsendur['ororka_tekjutr_skerdingarhlutf_efri']
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
            foreldralaun = forsendur['foreldralaun_2born_m']
        elif info['fjoldi_barna'] > 2:
            foreldralaun = forsendur['foreldralaun_fleiri_born_m']
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
    
    samtals_e_skatt, stadgreidsla = stadgreidsla_small_func(forsendur, skattgrunnur)
    
    
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
        
def ellilifeyrir_func(forsendur, info):
    '''
    midast vid full rettindi til ellilifeyris (40 ara buseta frá 16-67 ára aldri)
    '''
    
    ellilifeyrir = forsendur['ellilif_lifeyrir_m']
    heimilisuppbot = forsendur['ellilif_heimilisuppbot_m']
    uppbot_v_bils = forsendur['ellilif_bensinstyrkur_m']
    radstofunarfe = forsendur['ellilif_radstofunarfe_m']
    fritekjumork = forsendur['ellilif_fritekjumork']
    efri_mork_lifeyrir = forsendur['ellilif_lifeyrir_efri_mork_m']
    efri_mork_huppbot = forsendur['ellilif_heimilisuppbot_efri_mork_m']
    laun = info['tekjur'][0]
    barnalifeyrir_per_barn = forsendur['barnalifeyrir/barn']
    medlag_per_barn = forsendur['medlag/barn']
    
    ##### ELLILÍFEYRIR #####
    launatekjur_til_skerdingar =\
        (laun-(laun*(info['idgjald']+info['sereignaridgjald'])))
    tekjur_til_skerdingar =\
        launatekjur_til_skerdingar + info['tekjur'][1]#+lifeyrisgreidslur
        
    if tekjur_til_skerdingar > fritekjumork:
        skerding = forsendur['ellilif_lifeyrir_tekjusk_hlutf'] *\
        (tekjur_til_skerdingar - fritekjumork)
        ellilifeyrir -= skerding
        if ellilifeyrir < 0:
            ellilifeyrir = 0
            
    ##### HEIMILISUPPBÓT #####
    if info['byr_einn'] == 0:
        if tekjur_til_skerdingar > fritekjumork:
            skerding = forsendur['ellilif_huppbot_tekjusk_hlutf'] *\
            (tekjur_til_skerdingar - fritekjumork)
            heimilisuppbot -= skerding
            if heimilisuppbot < 0:
                heimilisuppbot = 0
    else:
        heimilisuppbot = 0
    
    ##### HREYFIHÖMLUNARMAT #####
    if info['hreyfihomlun'] == 1 or info['hreyfihomlun'] == 2:
        bensinsstyrkur = uppbot_v_bils
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
            foreldralaun = forsendur['foreldralaun_2born_m']
        elif info['fjoldi_barna'] > 2:
            foreldralaun = forsendur['foreldralaun_fleiri_born_m']
    else:
        foreldralaun = 0
        
    ##### FRESTUN/FLÝTING ELLILIFEYRIS #####
    if info['frestun_ellilifeyris'] > 0:
        ellilifeyrir += ellilifeyrir * (info['frestun_ellilifeyris'] * \
                                       forsendur['ellilif_haekkun_v_frestunar'])
        heimilisuppbot += heimilisuppbot * (info['frestun_ellilifeyris'] * \
                                           forsendur['ellilif_haekkun_v_frestunar'])
        
        # bæta inn flýtingu? þá þarf að opna möguleikann á ellilífeyri 2 árum fyrr
    samtals = ellilifeyrir + heimilisuppbot + bensinsstyrkur + barnalifeyrir + medlag + foreldralaun
    
    skattgrunnur = samtals - barnalifeyrir - medlag
    
    samtals_e_skatt, stadgreidsla = stadgreidsla_small_func(forsendur, skattgrunnur)
    
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