# -*- coding: utf-8 -*-

bakgrunnsuppl = {'hjuskaparstada': 2, #'1: einhleypur, 2: einst. foreldri, 3: giftur/sambud '
                    'busetuform': 2, #'1: eigin, 2: leigu/busetu, 3: hvorugt '
                    'tekjur': [470000, 0, 0, 0], #[laun_a_manudi, fjarmagnstekjur, laun_maka, fjarmagnstekjur_maka]
                    'eignir': 5000000.0,
                    'husnaedislan': 35000000,
                    'vaxtagjold': 2000000,
                    'husnaediskostnadur': 250000,
                    'fjoldi_heimilismanna': 3,
                    'heimilistekjur': 200000, #tekjur annarra en viðkomandi/hjóna
                    'heimiliseignir': 5000000, #eignir annarra en viðkomandi/hjóna
                    'fjoldi_barna': 4,
                    'fjoldi_barna_undir_7': 2,
                    'idgjald': 0.04,
                    'sereignaridgjald': 0.02,
                    'serstakar': 0,
                    'ororkuhlutfall': 0,
                    'fyrsta_75_mat': 0,
                    'byr_einn': 0,
                    'hreyfihomlun': 0,
                    'medlag_fj': 0,
                    'aldur': 0,
                    'frestun_ellilifeyris': 0,
                    }

results = {'tekjur_e_skatt': 0,
           'stadgreidsla' : 0,
           'lifeyrisgreidsla' : 0,
           'sereignarlifeyrisgreidsla' : 0,
           'barnabaetur': 0,
           'barnabaetur_skerding': 0,
           'husnaedisstudningur' : 0,
           'husnaedisstudningur_tekjuskerding' : 0,
           'husnaedisstudningur_eignaskerding' : 0,
           'radstofunartekjur': 0
          }

def litill_islendingur(bakgrunnsuppl):
    if bakgrunnsuppl['tekjur'] != 0:
        results['tekjur_e_skatt'], \
        results['stadgreidsla'], \
        results['lifeyrisgreidsla'], \
        results['sereignarlifeyrisgreidsla'] = \
        stadgreidsla_func(bakgrunnsuppl)
        
    if bakgrunnsuppl['fjoldi_barna'] != 0 and bakgrunnsuppl['hjuskaparstada'] != 1:
        results['barnabaetur'], results['barnabaetur_skerding'] = barnabaetur_func(bakgrunnsuppl)
    else:
        results['barnabaetur'] = 0, results['barnabaetur_skerding'] = 0
        
    if bakgrunnsuppl['busetuform'] != 3:
        results['husnaedisstudningur'], \
        results['husnaedisstudningur_tekjuskerding'], \
        results['husnaedisstudningur_eignaskerding'] = husnaedisstudningur_func(bakgrunnsuppl)
    else:
        results['husnaedisstudningur'], \
        results['husnaedisstudningur_tekjuskerding'], \
        results['husnaedisstudningur_eignaskerding'] = 0
    
    results['radstofunartekjur'] = results['tekjur_e_skatt'] + results['barnabaetur'] + results['husnaedisstudningur']
        
    return results
     
def stadgreidsla_func(bakgrunnsuppl):
    
    '''
    Reiknar staðgreiðslu útfrá gefnum forsendum.

    Skilar: launum eftir skatt (int), staðgreiðslu (int),
            skyldulífeyri (int), séreignarlífeyri (int)
    '''
    
    skattthrep = forsendur_dict['stadgr_threp_m']
    skatthlutfall_nedra = forsendur_dict['stadgr_hlutfall_nedra']
    skatthlutfall_efra = forsendur_dict['stadgr_hlutfall_efra']
    personuafsl = forsendur_dict['personuafslattur_m']

    lifeyrir = (bakgrunnsuppl['tekjur'][0] * bakgrunnsuppl['idgjald'])
    serlifeyrir = (bakgrunnsuppl['tekjur'][0] * bakgrunnsuppl['sereignaridgjald'])

    stofn = bakgrunnsuppl['tekjur'][0] - lifeyrir - serlifeyrir

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

def barnabaetur_func(bakgrunnsuppl):#, ororka, ellilif):
    '''
    Reiknar barnabætur út frá gefnum forsendum

    Skilar mánaðarlegum barnabótum (int)'''

    tekjur_yearly = [bakgrunnsuppl['tekjur'][0]*12,
                     bakgrunnsuppl['tekjur'][1]*12,
                     bakgrunnsuppl['tekjur'][2]*12,
                     bakgrunnsuppl['tekjur'][3]*12]
    #ororka_yearly = 12*ororka
    #ellilif_yearly = 12*ellilif

    fj_barna = bakgrunnsuppl['fjoldi_barna']
    fj_barna_undir_7 = bakgrunnsuppl['fjoldi_barna_undir_7']

    # SKERÐINGARHLUFÖLL
    skerdingarhlutfoll = forsendur_dict['barnab_skerdingarhlutfoll']
        # [1 barn, 2 börn, 3 börn eða fleiri]
    skerdingarhlutfoll_umframskerding = forsendur_dict['barnab_umframskerdingarhlutfoll']
    skerdingarhlutf_vidbot = forsendur_dict['barnab_skerdingarhl_vidbot']

    # FJÁRHÆÐIR 2017
    fjarhaedir_fyrsta_barn = forsendur_dict['barnab_fjarh_fyrsta_barn_y'] 
        # [einstætt foreldri, hjón/sambúðarfólk]
    fjarhaedir_umfram_born = forsendur_dict['barnab_fjarh_umfram_born_y'] 
        # [einstætt foreldri, hjón/sambúðarfólk]
    vidbotarfjarhaed_hvert_barn_undir_7 = forsendur_dict['barnab_fjarh_barn_undir_7_y']

    # SKERÐINGARMÖRK
    skerdingarmork = forsendur_dict['barnab_tekjuskmork'] # [einstætt foreldri, hjón/sambúðarfólk]
    skerdingarmork_umfram = forsendur_dict['barnab_tekjuskmork_umframskerding']

    # ÚTREIKNINGUR ÓSKERTRAR BÓTAFJÁRHÆÐAR
    if sum(tekjur_yearly) > skerdingarmork_umfram[bakgrunnsuppl['hjuskaparstada']-2]:
        stofn_til_umframskerdingar = sum(tekjur_yearly) -\
            skerdingarmork_umfram[bakgrunnsuppl['hjuskaparstada']-2]
        stofn_til_skerdingar = skerdingarmork_umfram[bakgrunnsuppl['hjuskaparstada'] - 2] -\
            skerdingarmork[bakgrunnsuppl['hjuskaparstada'] - 2]
    else:
        stofn_til_umframskerdingar = 0
        stofn_til_skerdingar = sum(tekjur_yearly) - skerdingarmork[bakgrunnsuppl['hjuskaparstada']-2] 
        #+ ororka_yearly + ellilif_yearly
    if stofn_til_skerdingar < 0:
        stofn_til_skerdingar = 0

    almennar_barnabaetur =\
        fjarhaedir_fyrsta_barn[bakgrunnsuppl['hjuskaparstada']-2] +\
        ((fj_barna-1) * fjarhaedir_umfram_born[bakgrunnsuppl['hjuskaparstada']-2])

    vidbotarbaetur = (fj_barna_undir_7 * vidbotarfjarhaed_hvert_barn_undir_7)
    
    # listi með skerðingarhlutföllum hefur þrjú stök: 1 barn, 2 börn, 3 eða fleiri börn
    # ef börn eru fleiri en þrjú erum við komin út fyrir listann og því er fj barna settur í 3
    if bakgrunnsuppl['fjoldi_barna'] > 3:
        fj_barna = 3
    
    skerding = (skerdingarhlutfoll[fj_barna-1] * stofn_til_skerdingar)
    umframskerding = (skerdingarhlutfoll_umframskerding[fj_barna-1] * stofn_til_umframskerdingar)
        
    if skerding > almennar_barnabaetur:
        skerding = almennar_barnabaetur
    skerding_vidbotar = ((fj_barna_undir_7*skerdingarhlutf_vidbot) * \
                         (stofn_til_skerdingar + stofn_til_umframskerdingar))
    if skerding_vidbotar > vidbotarbaetur:
        skerding_vidbotar = vidbotarbaetur

    baetur = almennar_barnabaetur + vidbotarbaetur - (skerding + umframskerding + skerding_vidbotar)
    if baetur < 0:
        baetur = 0
       
    skerding += umframskerding + skerding_vidbotar
    
    if bakgrunnsuppl['hjuskaparstada'] == 2:
        return baetur/12, skerding
    else:
        return baetur/24, skerding #bætur deilast jafnt milli hjóna

def husnaedisstudningur_func(bakgrunnsuppl):#, ororka, ellilif):
    ''' Kallar á rétt húsnæðisstuðningsfall eftir búsetuformi í forsendum '''

    if bakgrunnsuppl['busetuform'] == 1:
        studningur, tekjuskerding, eignaskerding = vaxtabaetur_func(bakgrunnsuppl)#, ororka, ellilif)

    elif bakgrunnsuppl['busetuform'] == 2:
        studningur, tekjuskerding, eignaskerding, heimilistekjur = husnaedisbaetur_func(bakgrunnsuppl)#, ororka, ellilif)
        if bakgrunnsuppl['serstakar'] == 1:
            serstakar, tekjuskerding_serstakar = serstakar_func(studningur) #ororka, ellilif, studningur)
            studningur += serstakar
            tekjuskerding += tekjuskerding_serstakar

    else:
        studningur = 0

    return studningur, tekjuskerding, eignaskerding

def vaxtabaetur_func(bakgrunnsuppl):#, ororka, ellilif):
    '''
    Reiknar vaxtabætur út frá gefnum forsendum.

    Skilar: vaxtabótum (int), tekjuskerðingu (int) og eignaskerðingu (int)
    '''

    hamark_vaxtagjalda = forsendur_dict['hamark_vaxtagjalda_y'] #fyrir: [einstakling, einstætt foreldri, hjón]
    hamark_bota = forsendur_dict['hamark_vaxtabota_y'] #fyrir: [einstakling, einstætt foreldri, hjón]
    tekjur_yearly = [bakgrunnsuppl['tekjur'][0]*12,\
                     bakgrunnsuppl['tekjur'][1]*12,\
                     bakgrunnsuppl['tekjur'][2]*12,\
                     bakgrunnsuppl['tekjur'][3]*12]
    #ororka_yearly = 12*ororka
    #ellilif_yearly = 12*ellilif
    tekjur = sum(tekjur_yearly) #+ ororka_yearly + ellilif_yearly

    eignaskerdingarmork_nedri = forsendur_dict['vaxtab_eignask_nedri'] 
        #fyrir: [einstakling, einstætt foreldri, hjón]
    eignaskerdingarmork_efri = forsendur_dict['vaxtab_eignask_efri'] 
        #fyrir: [einstakling, einstætt foreldri, hjón]

    stofn_list = [hamark_vaxtagjalda[bakgrunnsuppl['hjuskaparstada']-1],
                  forsendur_dict['vaxtab_hamarkshl_huslans']*bakgrunnsuppl['husnaedislan'],
                  bakgrunnsuppl['vaxtagjold']]
    stofn =  min(float(s) for s in stofn_list)

    tekjuskerding = forsendur_dict['vaxtab_tekjusk_hlutfall'] * tekjur
    baetur = stofn - tekjuskerding
    if baetur < 0:
        baetur = 0

    if bakgrunnsuppl['eignir'] >= eignaskerdingarmork_efri[bakgrunnsuppl['hjuskaparstada']-1]:
        eignaskerding = baetur
        baetur = 0

    elif bakgrunnsuppl['eignir'] >= eignaskerdingarmork_nedri[bakgrunnsuppl['hjuskaparstada']-1]:
        eignaskerding =\
            baetur *\
            ((bakgrunnsuppl['eignir'] - eignaskerdingarmork_nedri[bakgrunnsuppl['hjuskaparstada']-1]) /
            (eignaskerdingarmork_efri[bakgrunnsuppl['hjuskaparstada']-1] -
             eignaskerdingarmork_nedri[bakgrunnsuppl['hjuskaparstada']-1]))
        baetur -= eignaskerding

    else:
        eignaskerding = 0

    if baetur > hamark_bota[bakgrunnsuppl['hjuskaparstada']-1]:
        baetur = hamark_bota[bakgrunnsuppl['hjuskaparstada']-1]

    if bakgrunnsuppl['hjuskaparstada'] == 3:
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

def husnaedisbaetur_func(bakgrunnsuppl):#ororka, ellilif):
    '''
    Reiknar húsnæðisbætur (húsaleigubætur) út frá gefnum forsendum

    Skilar húsaleigubótum (int), tekjurskerðingu (int),
    eignaskerðingu (int) og heimilistekjum (int)
    '''

    tekjur = bakgrunnsuppl['heimilistekjur'] + sum(bakgrunnsuppl['tekjur']) #+ ororka + ellilif
    eignir = bakgrunnsuppl['heimiliseignir'] + bakgrunnsuppl['eignir']
    
    if bakgrunnsuppl['fjoldi_heimilismanna'] > 4:
        fjoldi_heimilismanna = 4
    else:
        fjoldi_heimilismanna = bakgrunnsuppl['fjoldi_heimilismanna']
        
    grunnfjarhaedir = forsendur_dict['husnb_grunnur_m']
    fritekjumark = forsendur_dict['husnb_fritekjumark_m']
    eignaskerdingarmork_nedri = forsendur_dict['husnb_eignask_nedri']
    eignaskerdingarmork_efri = forsendur_dict['husnb_eignask_efri']

    stofn = grunnfjarhaedir[fjoldi_heimilismanna-1]
    heimilistekjur = bakgrunnsuppl['heimilistekjur']

    if tekjur <= fritekjumark[fjoldi_heimilismanna-1]:
        baetur = stofn
        tekjuskerding = 0
    else:
        tekjuskerding = forsendur_dict['husnb_tekjusk_hlutfall'] *\
        (tekjur - fritekjumark[fjoldi_heimilismanna-1])
        baetur = stofn - tekjuskerding

    if eignir >= eignaskerdingarmork_efri:
        eignaskerding = baetur
        baetur = 0
    elif eignir >= eignaskerdingarmork_nedri:
        eignaskerding = baetur *\
            ((eignir - eignaskerdingarmork_nedri) /
             (eignaskerdingarmork_efri - eignaskerdingarmork_nedri))
        baetur -= eignaskerding
    else:
        eignaskerding = 0

    if baetur > forsendur_dict['husnb_hamarkshluti_husnkostn']*\
    bakgrunnsuppl['husnaediskostnadur']:
        baetur = forsendur_dict['husnb_hamarkshluti_husnkostn']*\
        bakgrunnsuppl['husnaediskostnadur']
    if baetur < 0:
        baetur = 0
    if tekjuskerding < 0:
        tekjuskerding = 0
    if eignaskerding < 0:
        eignaskerding = 0

    return baetur, tekjuskerding, eignaskerding, heimilistekjur

forsendur_dict = {'utvarpsgjald_threshold_m': 1678001/12,
                 'utvarpsgjald_m': 16800/12,
                 'eftirlaunaaldur': 67,
                 'serstakar_tekjusk_nedri_m': [281083.0, 371755.0, 435226.0, 471495.0],
                 'serstakar_tekjusk_efri_m': [351354, 464694, 544032, 589368],
                 'serstakar_threshold_eign': 5126000,
                 'serstakar_lagmarks_leiga': 40000,
                 'serstakar_plus_venjulegar_hamark': 90000,
                 'stadgr_threp_m': 927087,
                 'stadgr_hlutfall_nedra': 0.3694,
                 'stadgr_hlutfall_efra': 0.4624,
                 'fjarmagstekjuskattur_hlutfall': 0.2,
                 'personuafslattur_m': 56447,
                 'hamark_vaxtagjalda_y': [840000, 1050000, 1260000],
                 'hamark_vaxtabota_y': [420000, 525000, 630000],
                 'vaxtab_eignask_nedri': [5000000.0, 5000000.0, 8000000.0],
                 'vaxtab_eignask_efri': [8000000.0, 8000000.0, 12800000.0],
                 'vaxtab_tekjusk_hlutfall': 0.085,
                 'vaxtab_hamarkshl_huslans': 0.07,
                 'husnb_grunnur_m': [389520/12, 515172/12, 603132/12, 653388/12],
                 'husnb_fritekjumark_m': [3885000/12, 5138226/12, 6015484/12, 6516774/12],
                 'husnb_eignask_nedri': 6500000.0,
                 'husnb_eignask_efri': 10400000.0,
                 'husnb_tekjusk_hlutfall': 0.09,
                 'husnb_hamarkshluti_husnkostn': 0.75,
                 'barnab_skerdingarhlutfoll': [0.04, 0.06, 0.08],
                 'barnab_umframskerdingarhlutfoll' : [0.055, 0.075, 0.095],
                 'barnab_skerdingarhl_vidbot': 0.04,
                 'barnab_fjarh_fyrsta_barn_y': [390700, 234500],
                 'barnab_fjarh_umfram_born_y': [400800, 279200],
                 'barnab_fjarh_barn_undir_7_y': 140000,
                 'barnab_tekjuskmork': [3600000, 7200000],
                 'barnab_tekjuskmork_umframskerding' : [5500000, 11000000],
                 'ororka_grunnur': 44866.0,
                 'ororka_tekjusk_nedri': 214602.0,
                 'ororka_tekjusk_efri': 394066.0,
                 'ororka_fritekjumark_fjtekna_m': 98640.0/12,
                 'ororka_fritekjumark_launa_m': 1315200/12,
                 'ororka_fritekjumark_lifeyris_m': 328800/12,
                 'ororka_tekjutr_m': 143676,
                 'ororka_tekjutr_hamark_tekna_m': 376644,
                 'ororka_heimilisuppbot_m': 48564,
                 'barnalifeyrir/barn': 33168,
                 'medlag/barn': 33168,
                 'ororka_framfvidmid_ekkieinn': 238594,
                 'ororka_framfvidmid_einn': 300000,
                 'ororka_tekjutr_skerdingarhlutf_nedri': 0.3835,
                 'ororka_tekjutr_skerdingarhlutf_efri': 0.1335,
                 'ororka_heimilisuppbot_skerdingarhlutf': 0.1296,
                 'ororka_bensinstyrkur_m': 16583,
                 'foreldralaun_2born_m': 9602,
                 'foreldralaun_fleiri_born_m': 24965,
                 'ellilif_lifeyrir_m': 239484,
                 'ellilif_heimilisuppbot_m': 60516,
                 'ellilif_bensinstyrkur_m': 16583,
                 'ellilif_radstofunarfe_m': 71889,
                 'ellilif_fritekjumork': 25000,
                 'ellilif_lifeyrir_efri_mork_m': 557187,
                 'ellilif_heimilisuppbot_efri_mork_m': 533538,
                 'ellilif_lifeyrir_tekjusk_hlutf': 0.45,
                 'ellilif_huppbot_tekjusk_hlutf': 0.119,
                 'ellilif_haekkun_v_frestunar': 0.05
                }