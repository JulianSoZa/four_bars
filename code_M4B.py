
import numpy as np
from math import radians, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
from funtions import *

##definir barras


l1 = float(input('Ingrese la longitud de la barra de bancada "L1": '))
l2 = float(input('Ingrese la longitud de la barra de entrada "L2": '))
l3 = float(input('Ingrese la longitud de la barra acopladora "L3": '))
l4 = float(input('Ingrese la longitud de la barra de salida "L4": '))

l5 = float(input('Ingrese la longitud de la barra "L5": '))

th_5_usu = float(input('Ingrese el valor del angulo en grados de la barra "L5": '))

w2 = float(input('Ingrese el valor de la velocidad angular en rad/s de la barra de entrada "L2": ')) 

th_1 = 0


th_5 = radians(th_5_usu)

bars = [l1,l2,l3,l4] 

s = min(bars)
l = max(bars)

bars.remove(s)
bars.remove(l)

s_l = s + l
p_q = sum(bars)

discr=1000

(caso , cod) = case(l1, l2, l3, l4, s, l, s_l, p_q)

if ((cod == "SRRC")|(cod == "GRRC")|(cod == "S2XI")):
    (l1,l2,l3,l4) = inv_bars(l1, l2, l3, l4, s_l, p_q, s, l, cod)

## funciones 
if(l==(s+p_q)):
    print( "Esta configuracion corresponda a una estructura :)")
else:
    
    (th_2) = th2(l1, l2, l3, l4, s, l, s_l, p_q, discr, cod)
    
    print( "Seleccione la configuracion del mecanismo: ")
    print( "Ingrese '0' para la configuracion abierta.")
    print( "Ingrese '1' para la configuracion cruzada.")
    conf = int(input())

    if(conf == 0):
        (th_3, th_4) = conf_abierta(l1, l2, l3, l4, th_2, s_l, p_q, s, l)
    elif (conf == 1):
        (th_3, th_4) = conf_cruzada(l1, l2, l3, l4, th_2, s_l, p_q, s, l)
    else:
        (th_3, th_4) = conf_abierta(l1, l2, l3, l4, th_2, s_l, p_q, s, l)

    if((cod == "S2X")|(cod == "S2XI")|(cod == "S3X")|(cod == "SRRC")|(cod == "GRCR")|(cod == "RRR4")|(cod == "SRCR")):
        confA = np.array(conf_abierta(l1, l2, l3, l4, th_2, s_l, p_q, s, l))
        confC = np.array(conf_cruzada(l1, l2, l3, l4, th_2, s_l, p_q, s, l))
        th_3 = np.concatenate((confA[0], confC[0]), axis=None)
        th_4 = np.concatenate((confA[1], confC[1]), axis=None)
        th_2 = np.concatenate((th_2, th_2+2*pi), axis=None)

    print("th_2: ")
    print(th_2)
    print("th_3: ")
    print(th_3)
    print("th_4: ")
    print(th_4)

    (l2_x, l2_y, l3_x, l3_y, l4_x, l4_y, px, py) = componentes(l1, l2, l3 ,l4, l5, th_2, th_3, th_5,s,l,s_l,p_q,discr,cod)

    #Analisis de velocidad
    (w3, w4, v_px, v_py) = vel(l1, l2, l3, l4, l5, th_2, th_3, th_4, th_5, w2)

    print("w3")
    print(w3)

    #Graficar

    (lim_max_x, lim_min_x, lim_max_y, lim_min_y) = limits_graf(l2_x, l2_y, l3_x, l3_y, l4_x, l4_y, px, py)

    (th_2, th_4) = exchange_angles(th_2, th_4, cod)

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(autoscale_on=False, xlim=(lim_min_x-1, lim_max_x+1), ylim=(lim_min_y-1, lim_max_y+1))
    ax.set_aspect('equal')
    ax.grid()
    plt.suptitle(caso)
    
    fig2, ((ax2, ax3), (ax4, ax5), (ax6,ax7)) = plt.subplots(3,2)

    ax2.plot(th_2, w3, color = 'orange')
    ax2.set_xlabel('Theta 2')
    ax2.set_ylabel('W3')
    ax2.grid()

    ax3.plot(px, py, color = 'green')
    ax3.set_xlabel('Px')
    ax3.set_ylabel('Py')
    ax3.set_aspect('equal')
    ax3.grid()

    ax4.plot(th_2, v_px, color = '#FFDC00')
    ax4.set_xlabel('Theta 2')
    ax4.set_ylabel('Vpx')
    ax4.grid()

    ax5.plot(th_2, v_py, color = '#FF0097')
    ax5.set_xlabel('Theta 2')
    ax5.set_ylabel('Vpy')
    ax5.grid()

    ax6.plot(th_2, px , color = '#F11832')
    ax6.set_xlabel('Theta 2')
    ax6.set_ylabel('Px')
    ax6.grid()

    ax7.plot(th_2, py, color = '#181FF1')
    ax7.set_xlabel('Theta 2')
    ax7.set_ylabel('Py')
    ax7.grid()

    inv_graficas(ax, ax2, ax3, ax4, ax5, ax6, ax7, cod)

    ##definicion de la grafica
    history_len = 100000
    #dt = 800/w2
    #dt = 10
    dt = w2/1000

    line, = ax.plot([], [], 'o-', lw=2)
    line2, = ax.plot([], [], 'o-', lw=2)
    trace, = ax.plot([], [], '.-', lw=1, ms=2)
    time_template = 'time = %0.1fs'
    history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)

    def animate(i):
        thisx = [0, l2_x[i], l3_x[i], l4_x[i], 0]
        thisy = [0, l2_y[i], l3_y[i], l4_y[i], 0]
        this2x = [l2_x[i], px[i], l3_x[i]]
        this2y = [l2_y[i], py[i], l3_y[i]]
        
        if i == 0:
            history_x.clear()
            history_y.clear()

        history_x.appendleft(this2x[1])
        history_y.appendleft(this2y[1])

        line.set_data(thisx, thisy)
        line2.set_data(this2x, this2y)
        
        trace.set_data(history_x, history_y)
        return line, line2, trace

    ani = animation.FuncAnimation(
    fig, animate, len(px), interval=dt, blit=True)
    plt.tight_layout()
    plt.show()
