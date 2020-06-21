from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'abput'),

    # Simple
    path('simple/', views.simple, name = 'simple'),
    path('s_v_o/', views.s_v_o, name = 's_v_o'),
        path('s_v_o_ask/', views.s_v_o_ask, name = 's_v_o_ask'),
        path('s_v_o_buy/', views.s_v_o_buy, name = 's_v_o_buy'),
        path('s_v_o_close/', views.s_v_o_close, name = 's_v_o_close'),
        path('s_v_o_drink/', views.s_v_o_drink, name = 's_v_o_drink'),
        path('s_v_o_eat/', views.s_v_o_eat, name = 's_v_o_eat'),
        
    path('ms_v_o/', views.ms_v_o, name = 'ms_v_o'),
        path('ms_v_o_ask/', views.ms_v_o_ask, name = 'ms_v_o_ask'),
        path('ms_v_o_buy/', views.ms_v_o_buy, name = 'ms_v_o_buy'),
        path('ms_v_o_close/', views.ms_v_o_close, name = 'ms_v_o_close'),
        path('ms_v_o_drink/', views.ms_v_o_drink, name = 'ms_v_o_drink'),
        path('ms_v_o_eat/', views.ms_v_o_eat, name = 'ms_v_o_eat'),

    path('s_v_mo/', views.s_v_mo, name = 's_v_mo'),
        path('s_v_mo_ask/', views.s_v_mo_ask, name = 's_v_mo_ask'),
        path('s_v_mo_buy/', views.s_v_mo_buy, name = 's_v_mo_buy'),
        path('s_v_mo_close/', views.s_v_mo_close, name = 's_v_mo_close'),
        path('s_v_mo_drink/', views.s_v_mo_drink, name = 's_v_mo_drink'),
        path('s_v_mo_eat/', views.s_v_mo_eat, name = 's_v_mo_eat'),

    # Interrogative
    path('interrogative/', views.interrogative, name = 'interrogative'),
    path('sentance_type/', views.sentance_type, name = 'sentance_type'),
    
    path('normal/', views.normal, name = 'normal'),
        path('interrogative_n_what/', views.interrogative_n_what, name = 'interrogative_n_what'),
            path('interrogative_n_what_drink/', views.interrogative_n_what_drink, name = 'interrogative_n_what_drink'),
            path('interrogative_n_what_eat/', views.interrogative_n_what_eat, name = 'interrogative_n_what_eat'),
        
        path('interrogative_n_when/', views.interrogative_n_when, name = 'interrogative_n_when'),
            path('interrogative_n_when_close/', views.interrogative_n_when_close, name = 'interrogative_n_when_close'),
            path('interrogative_n_when_open/', views.interrogative_n_when_open, name = 'interrogative_n_when_open'),
        
        path('interrogative_n_where/', views.interrogative_n_where, name = 'interrogative_n_where'),
            path('interrogative_n_where_buy/', views.interrogative_n_where_buy, name = 'interrogative_n_where_buy'),
            path('norminterrogative_n_where_goal/', views.interrogative_n_where_go, name = 'interrogative_n_where_go'),


    path('int_ms_v_o/', views.int_ms_v_o, name = 'int_ms_v_o'),
        path('interrogative_int_ms_v_o_what/', views.interrogative_int_ms_v_o_what, name = 'interrogative_int_ms_v_o_what'),
            path('interrogative_int_ms_v_o_what_drink/', views.interrogative_int_ms_v_o_what_drink, name = 'interrogative_int_ms_v_o_what_drink'),
            path('interrogative_int_ms_v_o_what_eat/', views.interrogative_int_ms_v_o_what_eat, name = 'interrogative_int_ms_v_o_what_eat'),

        path('interrogative_int_ms_v_o_when/', views.interrogative_int_ms_v_o_when, name = 'interrogative_int_ms_v_o_when'),
            path('interrogative_int_ms_v_o_when_close/', views.interrogative_int_ms_v_o_when_close, name = 'interrogative_int_ms_v_o_when_close'),
            path('interrogative_int_ms_v_o_when_open/', views.interrogative_int_ms_v_o_when_open, name = 'interrogative_int_ms_v_o_when_open'),

        path('interrogative_int_ms_v_o_where/', views.interrogative_int_ms_v_o_where, name = 'interrogative_int_ms_v_o_where'),
            path('interrogative_int_ms_v_o_where_buy/', views.interrogative_int_ms_v_o_where_buy, name = 'interrogative_int_ms_v_o_where_buy'),
            path('interrogative_int_ms_v_o_where_go/', views.interrogative_int_ms_v_o_where_go, name = 'interrogative_int_ms_v_o_where_go'),

    path('int_s_v_mo/', views.int_s_v_mo, name = 'int_s_v_mo'),
        path('interrogative_int_s_v_mo_what/', views.interrogative_int_s_v_mo_what, name = 'interrogative_int_s_v_mo_what'),
            path('interrogative_int_s_v_mo_what_drink/', views.interrogative_int_s_v_mo_what_drink, name = 'interrogative_int_s_v_mo_what_drink'),
            path('interrogative_int_s_v_mo_what_eat/', views.interrogative_int_s_v_mo_what_eat, name = 'interrogative_int_s_v_mo_what_eat'),
            
        path('interrogative_int_s_v_mo_when/', views.interrogative_int_s_v_mo_when, name = 'interrogative_int_s_v_mo_when'),
            path('interrogative_int_s_v_mo_when_close/', views.interrogative_int_s_v_mo_when_close, name = 'interrogative_int_s_v_mo_when_close'),
            path('interrogative_int_s_v_mo_when_open/', views.interrogative_int_s_v_mo_when_open, name = 'interrogative_int_s_v_mo_when_open'),

        path('interrogative_int_s_v_mo_where/', views.interrogative_int_s_v_mo_where, name = 'interrogative_int_s_v_mo_where'),
            path('interrogative_int_s_v_mo_where_buy/', views.interrogative_int_s_v_mo_where_buy, name = 'interrogative_int_s_v_mo_where_buy'),
            path('interrogative_int_s_v_mo_where_go/', views.interrogative_int_s_v_mo_where_go, name = 'interrogative_int_s_v_mo_where_go'),

    # Exclamatory
    path('exclamatory/', views.exclamatory, name = 'exclamatory'),

    path('exclamatory_how/', views.exclamatory_how, name = 'exclamatory_how'),
        path('exclamatory_how_drink/', views.exclamatory_how_drink, name = 'exclamatory_how_drink'),
        path('exclamatory_how_eat/', views.exclamatory_how_eat, name = 'exclamatory_how_eat'),
        path('exclamatory_how_fly/', views.exclamatory_how_fly, name = 'exclamatory_how_fly'),
        path('exclamatory_how_literary/', views.exclamatory_how_literary, name = 'exclamatory_how_literary'),
        path('exclamatory_how_movement/', views.exclamatory_how_movement, name = 'exclamatory_how_movement'),

    path('exclamatory_order/', views.exclamatory_order, name = 'exclamatory_order'),
        path('exclamatory_order_bring/', views.exclamatory_order_bring, name = 'exclamatory_order_bring'),
        path('exclamatory_order_drink/', views.exclamatory_order_drink, name = 'exclamatory_order_drink'),
        path('exclamatory_order_eat/', views.exclamatory_order_eat, name = 'exclamatory_order_eat'),
        path('exclamatory_order_open/', views.exclamatory_order_open, name = 'exclamatory_order_open'),
        path('exclamatory_order_pick/', views.exclamatory_order_pick, name = 'exclamatory_order_pick'),
        path('exclamatory_order_read/', views.exclamatory_order_read, name = 'exclamatory_order_read'),
        path('exclamatory_order_shutup/', views.exclamatory_order_shutup, name = 'exclamatory_order_shutup'),

    path('exclamatory_such/', views.exclamatory_such, name = 'exclamatory_such'),

    path('exclamatory_what/', views.exclamatory_what, name = 'exclamatory_what'),

    path('exclamatory_wish/', views.exclamatory_wish, name = 'exclamatory_wish'),
        path('exclamatory_wish_s_v_o/', views.exclamatory_wish_s_v_o, name = 'exclamatory_wish_s_v_o'),
        path('exclamatory_wish_ms_v_o/', views.exclamatory_wish_ms_v_o, name = 'exclamatory_wish_ms_v_o'),

    # Compound
    path('compound/', views.Compound, name = 'Compound'),
        path('Compound_buy/', views.Compound_buy, name = 'Compound_buy'),
        path('Compound_went/', views.Compound_went, name = 'Compound_went'),
        path('Compound_study/', views.Compound_study, name = 'Compound_study'),

    # Complex
    path('Complex/', views.Complex, name='Complex'),
        path('complex_although/', views.complex_although, name='complex_although'),
        path('complex_whenever/', views.complex_whenever, name='complex_whenever'),
        path('Complex_inspite/', views.Complex_inspite, name='Complex_inspite'),
]
