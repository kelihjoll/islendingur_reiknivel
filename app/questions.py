#!/usr/bin/python
# -*- coding: utf-8 -*-

questions_list = []


q2 = {}
q2["question"] = "Hvað ertu gömul/gamall?"
q2["type"] = "input"
q2["name"] = "age"
q2["placeholder"] = "Aldur í árum"

q3 = {}
q3["question"] = "Hver er hjúskaparstaða þín?"
q3["name"] = "relationship_status"
q3["type"] = "multiple_choice"
q3["choices"] = ["Einhleyp(ur)", "Einstætt foreldri", "Gift(ur)/í sambúð"]

q4 = {}
q4["question"] = "Hverjar eru launatekjur þínar fyrir skatt á mánuði?"
q4["name"] = "monthly_pretax_salary_income"
q4["placeholder"] = "Mánaðarlegar launatekjur þínar fyrir skatt"
q4["type"] = "input-money"

q5 = {}
q5["question"] = "Hverjar, ef einhverjar, eru áætlaðar fjármagnstekjur heimilisins á árinu?"
q5["name"] = "annual_capital_gains_income"
q5["placeholder"] = "Fjármagnstekjur ársins"
q5["type"] = "input-money"

q6 = {}
q6["question"] = "Hversu hátt hlutfall launa greiðiru í lífeyrissjóð?"
q6["name"] = "pension_pay_ratio"
q6["choices"] = ["0%", "4%"]
q6["type"] = "multiple_choice"

q7 = {}
q7["question"] = "Hversu hátt hlutfall launa greiðiru í séreignasjóð?"
q7["name"] = "multiple_choice"
q7["choices"] = ["0%", "1%", "2%", "3%", "4%"]
q7["type"] = "multiple_choice"

q8 = {}
q8["question"] = "Hverjar, ef einhverjar, eru áætlaðar fjármagnstekjur þínar á árinu?"
q8["name"] = "annual_capital_gains_income"
q8["placeholder"] = "Fjármagnstekjur þínar fyrir árið"
q8["type"] = "input-money"

q9 = {}
q9["question"] = "Hverjar eru mánaðarlegar launatekjur maka fyrir skatt?"
q9["name"] = "monthly_pretax_salary_income_mate"
q9["placeholder"] = "Mánaðarlegar launatekjur maka fyrir skatt"
q9["type"] = "input-money"


q10 = {}
q10["question"] = "Hversu miklar eignir á heimilið í heild? Þá meina ég samanlagðar eignir hjóna / sambúðarfólks að frádregnum öllum skuldum? Mundu að telja með hlutabréf, innistæður á reikningum og verðbréf."
q10["name"] = "total_equity_couple"
q10["placeholder"] = "Heildareignir heimilisins að frádregnum skuldum"
q10["type"] = "input-money"

q11 = {}
q11["question"] = "Hverjar eru heildareignir þínar? Þá meina ég samanlagðar eignir þínar að frádregnum öllum skuldum? Mundu að telja með hlutabréf, innistæður á reikningum og verðbréf."
q11["name"] = "total_equity_single"
q11["placeholder"] = "Heildareignir þínar að frádregnum skuldum"
q11["type"] = "input-money"

q12 = {}
q12["question"] = "Hverjar eru húsnæðisaðstæður þínar?"
q12["name"] = "housing"
q12["type"] = "multiple_choice"
q12["choices"] = ["Ég bý í eigin húsnæði", "Ég bý í leiguíbúð eða búseturéttaríbúð", "Hvorugt passar"]

q13 = {}
q13["question"] = "Hverjar eru eftirstöðvar í árslok af lánum sem þú hefur tekið til kaupa á húsnæði til eigin nota?"
q13["name"] = "mortgage_principal"
q13["type"] = "input-money"
q13["placeholder"] = "Eftirstöðvar húsnæðisláns í árslok síðasta árs"

q14 = {}
q14["question"] =  "Hversu mikla vexti af íbúðarlánum greiddiru á síðasta ári? Mundu að telja með dráttarvexti og lántökukostnað ef það á við."
q14["name"] = "mortgage_cost"
q14["type"] = "input-money"
q14["placeholder"] = "Samtals vextir ásamt dráttarvöxtum og lántökukostnaði á síðasta ári"

q15 = {}
q15["question"] =  "Hver er mánaðarleg húsaleiga þín? Hér skaltu bara skrifa það sem stendur á leigusamningnum, óháð því hvað er innifalið (eins og rafmagn og hiti t.d.)"
q15["name"] = "rent_payment"
q15["type"] = "input-money"
q15["placeholder"] = "Mánaðarleg húsaleiga"

q16 = {}
q16["question"] =  "Hversu margir búa á heimilinu að þér meðtöldum/meðtaldri?"
q16["name"] = "no_of_inhabitants_home"
q16["type"] = "multiple_choice"
q16["choices"] = ["1","2","3","4 eða fleiri"]

q17 = {}
q17["question"] =  "Hverjar eru samanlagðar mánaðarlegar skattskyldar tekjur annarra á heimilismanna en þín og maka þíns?"
q17["name"] = "income_other_inhabitants_than_mate"
q17["type"] = "input-money"
q17["placeholder"] = "Skattskyldar mánaðarlegar tekjur annarra á heimilinu en þín og maka þíns"

q18 = {}
q18["question"] =  "Hverjar eru samanlagðar eignir annarra á heimilismanna en þín og maka þíns?"
q18["name"] = "equity_other_inhabitants_than_mate"
q18["type"] = "input-money"
q18["placeholder"] = "Eignir annarra á heimilinu en þín og maka þíns"

q19 = {}
q19["question"] =  "Hverjar eru samanlagðar mánaðarlegar skattskyldar tekjur annarra heimilismanna en þín?"
q19["name"] = "income_other_inhabitants"
q19["type"] = "input-money"
q19["placeholder"] = "Skattskyldar mánaðarlegar tekjur annarra á heimilinu en þín"

q20 = {}
q20["question"] =  "Hverjar eru samanlagðar eignir annarra heimilismanna en þín?"
q20["name"] = "equity_other_inhabitants_than_mate"
q20["type"] = "input-money"
q20["placeholder"] = "Eignir annarra á heimilinu en þín"

q21 = {}
q21["question"] =  "Áttu rétt á sérstökum húsaleigubótum?"
q21["name"] = "special_rental_benefits"
q21["type"] = "multiple_choice"
q21["choices"] = ["Já","Nei"]

q22 = {}
q22["question"] =  "Býrðu ein(n)?"
q22["name"] = "lives_alone"
q22["type"] = "multiple_choice"
q22["choices"] = ["Já","Nei"]

q23 = {}
q23["question"] = "Hver er fjöldi barna á heimilinu?"
q23["name"] = "num_kids"
q23["type"] = "input"
q23["placeholder"] = "Fjöldi barna"

q24 = {}
q24["question"] = "Þar af fjöldi barna yngri en 7 ára?"
q24["name"] = "num_kids_under_seven"
q24["type"] = "input"
q24["placeholder"] = "Fjöldi barna yngri en 7"

q25 = {}
q25["question"] =  "Hefurðu fengið viðurkennt hreyfihömlunarmat?"
q25["name"] = "lives_alone"
q25["type"] = "multiple_choice"
q25["choices"] = ["Nei","Já, ég er með bensínstyrk frá TR", "Já, ég fæ uppbót v. reksturs bifreiðar frá TR"]

q26 = {}
q26["question"] = "Áttu rétt á örorkulífeyri?"
q26["name"] = "disability_rights"
q26["type"] = "multiple_choice"
q26["choices"] = ["Já", "Nei"]

q27 = {}
q27["question"] = "Hvert er hlutfall örorku í prósentum?"
q27["name"] = "disability_perc"
q27["type"] = "input"
q27["placeholder"] = "Hlutfall örorku"

q28 = {}
q28["question"] = "Hvað varstu gamall/gömul við fyrsta 75% örorkumat?"
q28["name"] = "disability_age"
q28["type"] = "input"
q28["placeholder"] = "Fyrsta 75% örorkumat"

q29 = {}
q29["question"] =  "Hversu mörg börn áttu sem meðlag fæst greitt með frá TR?"
q29["name"] = "no_of_children_tr_alimony"
q29["type"] = "input"
q29["placeholder"] = "Fjöldi barna sem fæst með greitt meðlag frá TR"


questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)
questions_list.append(q11)
questions_list.append(q12)
questions_list.append(q13)
questions_list.append(q14)
questions_list.append(q15)
questions_list.append(q16)
questions_list.append(q17)
questions_list.append(q18)
questions_list.append(q19)
questions_list.append(q20)
questions_list.append(q21)
questions_list.append(q22)
questions_list.append(q23)
questions_list.append(q24)
questions_list.append(q25)
questions_list.append(q26)
questions_list.append(q27)
questions_list.append(q28)
questions_list.append(q29)


class Question(object):

    def __init__(self, question=None):

        self.question = question["question"]
        self.type = question["type"]
        self.name = question["name"]
        self.placeholder = question["placeholder"] if hasattr(question, "placeholder") else None
        self.choices = question["choices"] if hasattr(question, "choices") else None

    def print(self):
        return self.name

    def get_name(self):
        return self.name

    def get_question(self):
        return self.question

class Questions(object):

    def __init__(self):
        self.questions = []
        for question in questions_list:
            self.add(Question(question))

    def add(self, question):
        self.questions.append(question)

    def get_question_by_name(self, name):
        for q in self.questions:
            if q.get_name() == name:
                return q

    def print_question_by_name(self, name):
        question = self.get_question_by_name(name)
        return question.get_question()

