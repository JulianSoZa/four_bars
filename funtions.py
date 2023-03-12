import numpy as np
from math import radians, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

def case(l1, l2, l3, l4, s, l, s_l, p_q):
    if (s_l==p_q):
        if(((l1==l2)&(l3==l4)&(l1!=l3)&(l1+l2<l3+l4))):
            caso = "Delta #1"
            cod = "S2X"
        elif(((l1==l2)&(l3==l4))&(l1!=l3)&(l1+l2>l3+l4)):
            caso = "Delta #2"
            cod = "S2XI"
        elif ((((l2+l4)==(l1+l3))&(l2==s)&(l2!=l3)&(l3!=l4))):
            caso = "Delta #3"
            cod = "S2X"
        elif (l1==l2==l3==l4):
            caso = "Paralelo y antiparalelo"
            cod = "S3X"
        elif ((l1==l4)&(l3==l2)&(l1>l2)):
            caso = "Delta #4"
            cod = "S2X"
        elif ((l1==l4)&(l3==l2)&(l2>l1)):
            caso = "Delta #5"
            cod = "S2X"
        elif ((l2==s)):
            caso = "Especial: manivela - balancin"
            cod = "SCRR"
        elif ((l4==s)):
            caso = "Especial: balancin - manivela"
            cod = "SRRC"
        elif (l1==s):
            caso = "Especial: doble manivela"
            cod = "SCCC"
        elif (l3==s):
            caso = "Especial: doble balancin"
            cod = "SRCR"
        else:
            caso = "¿Falta un caso especial?"
            cod = "0"
    elif (s_l<p_q):
        if ((l3==s)): 
            caso = "Doble balancin"
            cod = "GRCR"
        elif ((l2==s)): 
            caso = "Manivela - balancin"
            cod = "GCRR"
        elif (l4==s):
            caso = "balancin - manivela"
            cod = "GRRC"
        elif (l1==s):
            caso = "Doble manivela"
            cod = "GCCC"
        else:
            caso = "¿Falta un caso grashof?"
            cod = "0"

    elif (s_l>p_q):
        if ((l3==l)):
            caso = "Outward Rockers"
            cod = "RRR3"
        elif ((l1==l)): #caso 5
            caso = "Inward Rockers"
            cod = "RRR1"
        elif ((l2==l)): #caso 6
            caso = "Rockers inwards and outwards" 
            cod = "RRR2"
        elif ((l4 == l)):
            caso = "Inward Rockers"
            cod = "RRR4"
        else:
            caso = "¿Falta un caso no-grashof?"
            cod = "0"

    return caso, cod

def th2(l1, l2, l3, l4, s, l, s_l, p_q, discr, cod):
    if(cod == "GRCR"):
        discr = 500
        th_2_max = np.arccos((-((l3+l4)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_min = np.arccos((-((l4-l3)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_d = np.linspace(th_2_min+0.00001,th_2_max-0.00001,discr)
        th_2_i = np.linspace(th_2_max-0.00001,th_2_min+0.00001,discr)
        th_2 = np.concatenate((th_2_d, th_2_i), axis=None)

    elif ((cod == "RRR3")|(cod == "RRR4")):
        discr = 500
        th_2_max = -np.arccos((-((l3-l4)**2)+(l2**2)+(l1**2))/(2*l2*l1)) + 2*pi
        th_2_min = np.arccos((-((l3-l4)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_d = np.linspace(th_2_min+0.0000001,th_2_max-0.0000001,discr)
        th_2_i = np.linspace(th_2_max-0.0000001,th_2_min+0.0000001,discr)
        th_2 = np.concatenate((th_2_d, th_2_i), axis=None)

    elif (cod == "RRR1"):
        discr = 500
        th_2_max = np.arccos((-((l4+l3)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_min = -np.arccos((-((l4+l3)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_d = np.linspace(th_2_min+0.00001,th_2_max-0.00001,discr)
        th_2_i = np.linspace(th_2_max-0.00001,th_2_min+0.00001,discr)
        th_2 = np.concatenate((th_2_d, th_2_i), axis=None)

    elif (cod == "RRR2"):
        discr = 500 
        th_2_max = np.arccos((-((l3+l4)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_min = -np.arccos((-((l3+l4)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_d = np.linspace(th_2_min+0.00001,th_2_max-0.00001,discr)
        th_2_i = np.linspace(th_2_max-0.00001,th_2_min+0.00001,discr)
        th_2 = np.concatenate((th_2_d, th_2_i), axis=None)

    elif (cod == "SRCR"): 
        discr = 500
        th_2_max = np.arccos((-((l3+l4)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_min = np.arccos((-((l4-l3)**2)+(l2**2)+(l1**2))/(2*l2*l1))
        th_2_d = np.linspace(th_2_min+0.00001,th_2_max-0.00001,discr)
        th_2_i = np.linspace(th_2_max-0.00001,th_2_min+0.00001,discr)
        th_2 = np.concatenate((th_2_d, th_2_i), axis=None)

    else:
        th_2 = np.linspace(0,2*pi,discr)
    
    return th_2

def inv_bars(l1, l2, l3, l4, s_l, p_q, s, l, cod):
    if(cod == "GRRC"):
        l4=l2
        l2=s

    elif (cod == "S2XI"): #especiales
        l1=l4
        l3=l2
        l2=l1
        l4=l3

    elif(cod == "SRRC"):
        l4=l2
        l2=s

    return l1, l2, l3, l4

def conf_abierta(l1, l2, l3, l4, th_2, s_l, p_q, s, l):
    k1=l1/l2
    k2=l1/l4
    k3=((l2**2)-(l3**2)+(l4**2)+(l1**2))/(2*l2*l4)

    A=np.cos(th_2)-k1-k2*np.cos(th_2)+k3
    B=-2*np.sin(th_2)
    C=k1-(k2+1)*np.cos(th_2)+k3

    th_4=2*np.arctan((-B-np.sqrt((B**2)-4*A*C))/(2*A))

    k4=l1/l3
    k5=((l4**2)-(l1**2)-(l2**2)-(l3**2))/(2*l2*l3)

    D=np.cos(th_2)-k1+k4*np.cos(th_2)+k5
    E=-2*np.sin(th_2)
    F=k1+(k4-1)*np.cos(th_2)+k5

    th_3=2*np.arctan((-E-np.sqrt((E**2)-4*D*F))/(2*D))
    return th_3, th_4

def conf_cruzada(l1, l2, l3, l4, th_2, s_l, p_q, s, l):
    k1=l1/l2
    k2=l1/l4
    k3=((l2**2)-(l3**2)+(l4**2)+(l1**2))/(2*l2*l4)

    A=np.cos(th_2)-k1-k2*np.cos(th_2)+k3
    B=-2*np.sin(th_2)
    C=k1-(k2+1)*np.cos(th_2)+k3

    th_4=2*np.arctan((-B+np.sqrt((B**2)-4*A*C))/(2*A))

    k4=l1/l3
    k5=((l4**2)-(l1**2)-(l2**2)-(l3**2))/(2*l2*l3)

    D=np.cos(th_2)-k1+k4*np.cos(th_2)+k5
    E=-2*np.sin(th_2)
    F=k1+(k4-1)*np.cos(th_2)+k5

    th_3=2*np.arctan((-E+np.sqrt((E**2)-4*D*F))/(2*D))
    return th_3, th_4

def inv_graficas(ax, ax2, ax3, ax4, ax5, ax6, ax7, cod):
    if ((cod == "SRRC")|(cod == "GRRC")|(cod == "S2XI")):
        ax.invert_xaxis()
        ax2.invert_xaxis()
        ax3.invert_xaxis()
        ax4.invert_xaxis()
        ax5.invert_xaxis()
        ax6.invert_xaxis()
        ax7.invert_xaxis()

def vel(l1, l2, l3, l4, l5, th_2, th_3, th_4, th_5, w2):

    mat_A = []
    inv_A = []
    mat_B = []
    w4_w3 = []
    v_px = []
    v_py = []
    w3 = []
    w4 = []

    for j in range(len(th_4)):
        mat_A.append(np.array([[(l4*np.sin(th_4[j])),-(l3*np.sin(th_3[j]))], [(l4*np.cos(th_4[j])),-(l3*np.cos(th_3[j]))]]))
        try:
            inv_A.append(np.linalg.inv(mat_A[j]))
        except:
            inv_A.append(np.linalg.pinv(mat_A[j]))

        mat_B.append(np.array([[w2*l2*np.sin(th_2[j])],[w2*l2*np.cos(th_2[j])]]))
        w4_w3.append(inv_A[j] @ mat_B[j])
        w3.append(w4_w3[j][1][0])
        w4.append(w4_w3[j][0][0])
        v_px.append((w2*l2*np.sin(th_2[j]))+(w3[j]*l5*np.sin(th_3[j]+th_5))) 
        v_py.append((w2*l2*np.cos(th_2[j]))+(w3[j]*l5*np.cos(th_3[j]+th_5)))
    
    return w3, w4, v_px, v_py

def componentes(l1, l2, l3 ,l4, l5, th_2, th_3, th_5,s, l, s_l, p_q, discr, cod):
    l2_x= l2*np.cos(th_2)
    l2_y= l2*np.sin(th_2)


    l3_x=l2_x+l3*np.cos(th_3)
    l3_y=l2_y+l3*np.sin(th_3)

    l4_x = np.tile(l1, len(th_2))
    l4_y = np.tile(0, len(th_2))

    px = l2_x+l5*np.cos(th_3+th_5)
    py = l2_y+l5*np.sin(th_3+th_5)

    return l2_x, l2_y, l3_x, l3_y, l4_x, l4_y, px, py

def limits_graf(l2_x, l2_y, l3_x, l3_y, l4_x, l4_y, px, py):

    all_components_x = np.concatenate((px,l2_x,l3_x,l4_x, 0), axis=None)
    all_components_y = np.concatenate((py,l2_y,l3_y,l4_y, 0), axis=None)

    all_components_x = all_components_x[np.isfinite(all_components_x)]
    all_components_y = all_components_y[np.isfinite(all_components_y)]

    lim_max_x = max(all_components_x)
    lim_min_x = min(all_components_x)
    lim_max_y = max(all_components_y)
    lim_min_y = min(all_components_y)

    return lim_max_x, lim_min_x, lim_max_y, lim_min_y

def exchange_angles(th_2, th_4, cod):
    if ((cod == "SRRC")|(cod == "GRRC")):
        (th_2, th_4) = th_4, th_2
    return th_2, th_4