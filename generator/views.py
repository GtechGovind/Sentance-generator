from django.shortcuts import render
import random

# Simple 
from . import simple_s_v_o as simple_fun

def index(request):
    return render(request, 'index.html')

def home(request):
    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Simple

def simple(request):
    return render(request, 'Simple/simple.html')

from . import simple_s_v_o as simple_fun
def s_v_o(request):
    return render(request, 'Simple/s_v_o.html')

# Statement Types for Simple
def s_v_o_ask(request):
    statement = simple_fun.AskSvo()
    selector = 's_v_o_ask'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_o_buy(request):
    statement = simple_fun.BuySvo()
    selector = 's_v_o_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_o_close(request):
    statement = simple_fun.CloseSvo()
    selector = 's_v_o_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_o_drink(request):
    statement = simple_fun.DrinkSvo()
    selector = 's_v_o_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_o_eat(request):
    statement = simple_fun.EatSvo()
    selector = 's_v_o_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})


from . import simple_ms_v_o as ms_v_o_fun
def ms_v_o(request):
    return render(request, 'Simple/ms_v_o.html')

def ms_v_o_ask(request):
    statement = ms_v_o_fun.AskSsvo()
    selector = 'ms_v_o_ask'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def ms_v_o_buy(request):
    statement = ms_v_o_fun.BuySsvo()
    selector = 'ms_v_o_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def ms_v_o_close(request):
    statement = ms_v_o_fun.CloseSsvo()
    selector = 'ms_v_o_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def ms_v_o_drink(request):
    statement = ms_v_o_fun.DrinkSsvo()
    selector = 'ms_v_o_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def ms_v_o_eat(request):
    statement = ms_v_o_fun.EatSsvo()
    selector = 'ms_v_o_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})


from . import simple_s_v_mo
def s_v_mo(request):
    return render(request, 'Simple/s_v_mo.html')

def s_v_mo_ask(request):
    statement = simple_s_v_mo.AskSvoo()
    selector = 's_v_mo_ask'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_mo_buy(request):
    statement = simple_s_v_mo.BuySvoo()
    selector = 's_v_mo_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_mo_close(request):
    statement = simple_s_v_mo.CloseSvoo()
    selector = 's_v_mo_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_mo_drink(request):
    statement = simple_s_v_mo.DrinkSvoo()
    selector = 's_v_mo_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def s_v_mo_eat(request):
    statement = simple_s_v_mo.EatSvoo()
    selector = 's_v_mo_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})




# Interrogative

def interrogative(request):
    return render(request, 'Interrogative/interrogative_type.html')

def sentance_type(request):
    return render(request, 'Interrogative/sentance_type.html')

#-----------------------------------------------NORMAL--------------------------------------------

from . import interrogative_s_v_o
def normal(request):
    return render(request, 'Interrogative/normal.html')

#-----------------------------------------------WHAT--------------------------------------------

def interrogative_n_what(request):
    ele1 = 'DRINK'
    ele2 = 'EAT'
    link1 = 'interrogative_n_what_drink'
    link2 = 'interrogative_n_what_eat'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })

def interrogative_n_what_drink(request):
    statement = interrogative_s_v_o.DrinkSvo()
    selector = 'interrogative_n_what_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_n_what_eat(request):
    statement = interrogative_s_v_o.EatSvo()
    selector = 'interrogative_n_what_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHEN--------------------------------------------

def interrogative_n_when(request):
    ele1 = 'CLOSE'
    ele2 = 'OPEN'
    link1 = 'interrogative_n_when_close'
    link2 = 'interrogative_n_when_open'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })

def interrogative_n_when_close(request):
    statement = interrogative_s_v_o.CloseSvo()
    selector = 'interrogative_n_when_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_n_when_open(request):
    statement = interrogative_s_v_o.OpenSvo()
    selector = 'interrogative_n_when_open'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHERE--------------------------------------------

def interrogative_n_where(request):
    ele1 = 'BUY'
    ele2 = 'GO'
    link1 = 'interrogative_n_where_buy'
    link2 = 'interrogative_n_where_go'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_n_where_buy(request):
    statement = interrogative_s_v_o.BuySvo()
    selector = 'interrogative_n_where_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_n_where_go(request):
    statement = interrogative_s_v_o.GoSvo()
    selector = 'interrogative_n_where_go'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})


#-----------------------------------------------MS_V_O--------------------------------------------

from . import interrogative_ms_v_o
def int_ms_v_o(request):
    return render(request, 'Interrogative/ms_v_o.html')

#-----------------------------------------------WHAT--------------------------------------------

def interrogative_int_ms_v_o_what(request):
    ele1 = 'DRINK'
    ele2 = 'EAT'
    link1 = 'interrogative_int_ms_v_o_what_drink'
    link2 = 'interrogative_int_ms_v_o_what_eat'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_int_ms_v_o_what_drink(request):
    statement = interrogative_ms_v_o.DrinkSsvo()
    selector = 'interrogative_int_ms_v_o_what_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_ms_v_o_what_eat(request):
    statement = interrogative_ms_v_o.EatSsvo()
    selector = 'interrogative_int_ms_v_o_what_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHEN--------------------------------------------

def interrogative_int_ms_v_o_when(request):
    ele1 = 'CLOSE'
    ele2 = 'FLY'
    link1 = 'interrogative_int_ms_v_o_when_close'
    link2 = 'interrogative_int_ms_v_o_when_open'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_int_ms_v_o_when_close(request):
    statement = interrogative_ms_v_o.CloseSsvo()
    selector = 'interrogative_int_ms_v_o_when_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_ms_v_o_when_open(request):
    statement = interrogative_ms_v_o.FlySsvo()
    selector = 'interrogative_int_ms_v_o_when_open'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHERE--------------------------------------------

def interrogative_int_ms_v_o_where(request):
    ele1 = 'BUY'
    ele2 = 'GO'
    link1 = 'interrogative_int_ms_v_o_where_buy'
    link2 = 'interrogative_int_ms_v_o_where_go'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_int_ms_v_o_where_buy(request):
    statement = interrogative_ms_v_o.BuySsvo()
    selector = 'interrogative_int_ms_v_o_where_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_ms_v_o_where_go(request):
    statement = interrogative_ms_v_o.GoSsvo()
    selector = 'interrogative_int_ms_v_o_where_go'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------S_V_MO--------------------------------------------
#-----------------------------------------------S_V_MO--------------------------------------------

from . import interrogative_s_v_mo
def int_s_v_mo(request):
    return render(request, 'Interrogative/s_v_mo.html')

#-----------------------------------------------WHAT--------------------------------------------

def interrogative_int_s_v_mo_what(request):
    ele1 = 'DRINK'
    ele2 = 'EAT'
    link1 = 'interrogative_int_s_v_mo_what_drink'
    link2 = 'interrogative_int_s_v_mo_what_eat'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_int_s_v_mo_what_drink(request):
    statement = interrogative_s_v_mo.DrinkSvoo()
    selector = 'interrogative_int_s_v_mo_what_drink'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_s_v_mo_what_eat(request):
    statement = interrogative_s_v_mo.EatSvoo()
    selector = 'interrogative_int_s_v_mo_what_eat'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHEN--------------------------------------------

def interrogative_int_s_v_mo_when(request):
    ele1 = 'CLOSE'
    ele2 = 'OPEN'
    link1 = 'interrogative_int_s_v_mo_when_close'
    link2 = 'interrogative_int_s_v_mo_when_open'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })


def interrogative_int_s_v_mo_when_close(request):
    statement = interrogative_s_v_mo.CloseSvoo()
    selector = 'interrogative_int_s_v_mo_when_close'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_s_v_mo_when_open(request):
    statement = interrogative_s_v_mo.OpenSvoo()
    selector = 'interrogative_int_s_v_mo_when_open'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

#-----------------------------------------------WHERE--------------------------------------------

def interrogative_int_s_v_mo_where(request):
    ele1 = 'BUY'
    ele2 = 'GO'
    link1 = 'interrogative_int_s_v_mo_where_buy'
    link2 = 'interrogative_int_s_v_mo_where_go'

    return render(request, 'Interrogative/word_type.html', { 
        'ele1': ele1, 'ele2': ele2, 'link1': link1, 'link2': link2
     })

def interrogative_int_s_v_mo_where_buy(request):
    statement = interrogative_s_v_mo.BuySvoo()
    selector = 'interrogative_int_s_v_mo_where_buy'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})

def interrogative_int_s_v_mo_where_go(request):
    statement = interrogative_s_v_mo.GoSvoo()
    selector = 'interrogative_int_s_v_mo_where_go'
    return render(request, 'result.html', {'statement': statement, 'selector': selector})


# Exclamatory

def exclamatory(request):
    return render(request, 'Exclamatory/exclamatory.html')

#-----------------------------------------------HOW--------------------------------------------

def exclamatory_how(request):
    ele1 = 'DRINK'
    ele2 = 'EAT'
    ele3 = 'FLY'
    ele4 = 'LITERARY'
    ele5 = 'MOVEMENT'
    link1 = 'exclamatory_how_drink'
    link2 = 'exclamatory_how_eat'
    link3 = 'exclamatory_how_fly'
    link4 = 'exclamatory_how_literary'
    link5 = 'exclamatory_how_movement'

    return render(request, 'Exclamatory/exclamatory_buttons.html', { 
        'ele1': ele1, 'ele2': ele2,'ele3': ele3, 'ele4': ele4, 'ele5': ele5, 'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5
     })
    
from . import exclamatory_how_fun

def exclamatory_how_drink(request):
    sentance = exclamatory_how_fun.how_drink()
    selector = 'exclamatory_how_drink'
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

def exclamatory_how_eat(request):
    sentance = exclamatory_how_fun.how_eat()
    selector = 'exclamatory_how_eat'
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

def exclamatory_how_fly(request):
    sentance = exclamatory_how_fun.how_fly()
    selector = 'exclamatory_how_fly'
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

def exclamatory_how_literary(request):
    sentance = exclamatory_how_fun.how_literary()
    selector = 'exclamatory_how_literary'
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

def exclamatory_how_movement(request):
    sentance = exclamatory_how_fun.how_movement()
    selector = 'exclamatory_how_movement'
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

#-----------------------------------------------ORDER--------------------------------------------

def exclamatory_order(request):
    ele1 = 'BRING'
    ele2 = 'DRINK'
    ele3 = 'EAT'
    ele4 = 'OPEN'
    ele5 = 'PICK'
    ele6 = 'READ'
    ele7 = 'SHUTUP'
    link1 = 'exclamatory_order_bring'
    link2 = 'exclamatory_order_drink'
    link3 = 'exclamatory_order_eat'
    link4 = 'exclamatory_order_open'
    link5 = 'exclamatory_order_pick'
    link6 = 'exclamatory_order_read'
    link7 = 'exclamatory_order_shutup'

    return render(request, 'Exclamatory/exclamatry_button_order.html', { 
        'ele1': ele1, 'ele2': ele2,'ele3': ele3, 'ele4': ele4, 'ele5': ele5, 'ele6': ele6, 'ele7': ele7, 'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7
     })

from . import exclamatory_order_fun

def exclamatory_order_bring(request):
    sentance = exclamatory_order_fun.order_bring()
    selector = 'exclamatory_order_bring'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_drink(request):
    sentance = exclamatory_order_fun.order_drink()
    selector = 'exclamatory_order_drink'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_eat(request):
    sentance = exclamatory_order_fun.order_eat()
    selector = 'exclamatory_order_eat'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_open(request):
    sentance = exclamatory_order_fun.order_open()
    selector = 'exclamatory_order_open'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_pick(request):
    sentance = exclamatory_order_fun.order_pick()
    selector = 'exclamatory_order_pick'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_read(request):
    sentance = exclamatory_order_fun.order_read()
    selector = 'exclamatory_order_read'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_order_shutup(request):
    sentance = exclamatory_order_fun.order_shutup()
    selector = 'exclamatory_order_shutup'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })


#-----------------------------------------------SUCH--------------------------------------------
from . import exclamatory_such_fun
def exclamatory_such(request):
    sentance = exclamatory_such_fun.such()
    selector = "exclamatory_such"
    return render(request, 'result.html', { 'statement' : sentance, 'selector' : selector })

#-----------------------------------------------WHAT--------------------------------------------

from . import exclamatory_what_fun
def exclamatory_what(request):
    sentance = exclamatory_what_fun.what()
    selector = 'exclamatory_what'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

#-----------------------------------------------WISH--------------------------------------------
from . import exclamatory_wish_fun

def exclamatory_wish(request):
    ele1 = 'SUB - VERB - OBJ'
    ele2 = 'MUL SUB - VERB - OBJ'
    link1 = 'exclamatory_wish_s_v_o'
    link2 = 'exclamatory_wish_ms_v_o'

    return render(request, 'Exclamatory/exclamatoray_button_wish.html', { 
        'ele1': ele1, 'ele2': ele2,'link1': link1, 'link2': link2
     })
    
def exclamatory_wish_s_v_o(request):
    sentance = exclamatory_wish_fun.wish_s_v_o()
    selector = 'exclamatory_wish_s_v_o'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def exclamatory_wish_ms_v_o(request):
    sentance = exclamatory_wish_fun.wish_ms_v_o()
    selector = 'exclamatory_wish_ms_v_o'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })


# Compound
from .compound import *
def Compound(request):
    ele1 = 'Buy'
    ele2 = 'Went'
    ele3 = 'study'
    link1 = 'Compound_buy'
    link2 = 'Compound_went'
    link3 = 'Compound_study'

    return render(request, 'Compound\compound_buttons.html', {
        'ele1': ele1, 'ele2': ele2, 'ele3': ele3, 'link1': link1, 'link2': link2, 'link3': link3
     })

def Compound_buy(request):
    sentence = buy()
    selector = 'Compound_buy'
    return render(request, 'result.html', { 'statement' : sentence , 'selector' : selector })

def Compound_went(request):
    sentance = went()
    selector = 'Compound_went'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

def Compound_study(request):
    sentance = study()
    selector = 'Compound_study'
    return render(request, 'result.html', { 'statement' : sentance , 'selector' : selector })

# Complex
from .Complex import *
def Complex(request):
    ele1 = 'Although'
    ele2 = 'Inspite'
    ele3 = 'Whenever'
    link1 = 'complex_although'
    link2 = 'Complex_inspite'
    link3 = 'complex_whenever'

    return render(request, 'Complex\complex_buttons.html', {
        'ele1': ele1, 'ele2': ele2, 'ele3' : ele3, 'link1': link1, 'link3': link3, 'link2': link2
     })

def complex_although(request):
    sentence = although()
    selector = 'complex_although'
    return render(request, 'result.html', { 'statement' : sentence , 'selector' : selector })

def complex_whenever(request):
    sentence = whenever()
    selector = 'complex_whenever'
    return render(request, 'result.html', { 'statement' : sentence , 'selector' : selector })

def Complex_inspite(request):
    sentence = old()
    selector = 'Complex_inspite'
    return render(request, 'result.html', { 'statement' : sentence , 'selector' : selector })