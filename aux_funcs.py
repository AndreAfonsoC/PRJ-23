import matplotlib.pyplot as plt
import numpy as np

import aux_tools as at
import design_tools_hermes as dt


def print_aircraft_dimensions(aircraft):
    dimensions = aircraft['dimensions']

    # Asa (wing)
    print("Asa (Wing):")
    wing = dimensions['wing']
    for key, value in sorted(wing.items()):
        print(f"\t{key}: {value}")
    print()

    # Empenagem Horizontal (EH)
    print("Empenagem Horizontal (EH):")
    EH = dimensions['EH']
    for key, value in sorted(EH.items()):
        print(f"\t{key}: {value}")
    print()

    # Empenagem Vertical (EV)
    print("Empenagem Vertical (EV):")
    EV = dimensions['EV']
    for key, value in sorted(EV.items()):
        print(f"\t{key}: {value}")
    print()

def plot2d_top_view(aircraft):

    xr_w = aircraft['geo_param']['wing']['xr']
    cr_w = aircraft['dimensions']['wing']['cr']
    xt_w = aircraft['dimensions']['wing']['xt']
    yt_w = aircraft['dimensions']['wing']['yt']
    ct_w = aircraft['dimensions']['wing']['ct']
    xr_h = aircraft['dimensions']['EH']['xr']
    cr_h = aircraft['dimensions']['EH']['cr']
    xt_h = aircraft['dimensions']['EH']['xt']
    yt_h = aircraft['dimensions']['EH']['yt']
    ct_h = aircraft['dimensions']['EH']['ct']
    xr_v = aircraft['dimensions']['EV']['xr']
    cr_v = aircraft['dimensions']['EV']['cr']
    xt_v = aircraft['dimensions']['EV']['xt']
    ct_v = aircraft['dimensions']['EV']['ct']
    L_f = aircraft['dimensions']['fus']['Lf']
    x_n = aircraft['dimensions']['nacelle']['xn']
    y_n = aircraft['dimensions']['nacelle']['yn']
    L_n = aircraft['dimensions']['nacelle']['Ln']
    xcg_0 = aircraft['dimensions']['fus']['xcg']
    xnp = aircraft['dimensions']['fus']['xnp']
           
    ### PLOT

    fig, ax = plt.subplots()

    # Wing
    ax.plot([xr_w, xt_w, xt_w+ct_w, xr_w+cr_w, xt_w+ct_w, xt_w, xr_w],
            [0.0, yt_w, yt_w, 0.0, -yt_w, -yt_w, 0.0], 'b-')

    # Horizontal Stabilizer (EH)
    ax.plot([xr_h, xt_h, xt_h+ct_h, xr_h+cr_h, xt_h+ct_h, xt_h, xr_h],
            [0.0, yt_h, yt_h, 0.0, -yt_h, -yt_h, 0.0], 'orange')

    # Vertical Stabilizer (EV) - Only the top projection, so it appears as a single line along the centerline
    ax.plot([xr_v, xt_v+ct_v], [0.0, 0.0], 'g-')

    # Fuselage
    ax.plot([0.0, L_f], [0.0, 0.0], 'r-')

    # Nacelles
    ax.plot([x_n, x_n+L_n], [y_n, y_n], 'purple')
    ax.plot([x_n, x_n+L_n], [-y_n, -y_n], 'purple')

    # Center of Gravity (CG) and Neutral Point (NP)
    ax.plot([xcg_0], [0.0], 'ko')  # Black dot for CG
    ax.plot([xnp], [0.0], 'ro')  # Red dot for NP

    ax.set_aspect('equal')
    plt.xlabel('x (meters)')
    plt.ylabel('y (meters)')
    plt.grid(True)
    plt.show()

def plot3d_new(aircraft, elevacao = 90, azimute = 0):
    xr_w = aircraft['geo_param']['wing']['xr']
    zr_w = aircraft['geo_param']['wing']['zr']
    cr_w = aircraft['dimensions']['wing']['cr']
    xt_w = aircraft['dimensions']['wing']['xt']
    yt_w = aircraft['dimensions']['wing']['yt']
    zt_w = aircraft['dimensions']['wing']['zt']
    ct_w = aircraft['dimensions']['wing']['ct']
    xr_h = aircraft['dimensions']['EH']['xr']
    zr_h = aircraft['geo_param']['EH']['zr']
    cr_h = aircraft['dimensions']['EH']['cr']
    xt_h = aircraft['dimensions']['EH']['xt']
    yt_h = aircraft['dimensions']['EH']['yt']
    zt_h = aircraft['dimensions']['EH']['zt']
    ct_h = aircraft['dimensions']['EH']['ct']
    xr_v = aircraft['dimensions']['EV']['xr']
    zr_v = aircraft['geo_param']['EV']['zr']
    cr_v = aircraft['dimensions']['EV']['cr']
    xt_v = aircraft['dimensions']['EV']['xt']
    zt_v = aircraft['dimensions']['EV']['zt']
    ct_v = aircraft['dimensions']['EV']['ct']
    L_f = aircraft['dimensions']['fus']['Lf']
    D_f = aircraft['dimensions']['fus']['Df']
    x_n = aircraft['dimensions']['nacelle']['xn']
    y_n = aircraft['dimensions']['nacelle']['yn']
    z_n = aircraft['dimensions']['nacelle']['zn']
    L_n = aircraft['dimensions']['nacelle']['Ln']
    D_n = aircraft['dimensions']['nacelle']['Dn']
    xcg_0 = aircraft['dimensions']['fus']['xcg']
    xnp = aircraft['dimensions']['fus']['xnp']

    
    ### PLOT
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_aspect('equal')
    # Adicionar logo após a criação do objeto 'ax'
    ax.view_init(elev=elevacao, azim=azimute)  # Muda a perspectiva para ver de cima    
    ax.plot([xr_w, xt_w, xt_w+ct_w, xr_w+cr_w, xt_w+ct_w, xt_w, xr_w],
            [0.0, yt_w, yt_w, 0.0, -yt_w, -yt_w, 0.0],
            [zr_w, zt_w, zt_w, zr_w, zt_w, zt_w, zr_w])
    ax.plot([xr_h, xt_h, xt_h+ct_h, xr_h+cr_h, xt_h+ct_h, xt_h, xr_h],
            [0.0, yt_h, yt_h, 0.0, -yt_h, -yt_h, 0.0],
            [zr_h, zt_h, zt_h, zr_h, zt_h, zt_h, zr_h])
    ax.plot([xr_v, xt_v, xt_v+ct_v, xr_v+cr_v, xr_v],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [zr_v, zt_v, zt_v, zr_v, zr_v])

    ax.plot([0.0, L_f],
            [0.0, 0.0],
            [0.0, 0.0])
    ax.plot([x_n, x_n+L_n],
            [y_n, y_n],
            [z_n, z_n])
    ax.plot([x_n, x_n+L_n],
            [-y_n, -y_n],
            [z_n, z_n])

    ax.plot([xcg_0, xcg_0],
            [0.0, 0.0],
            [0.0, 0.0],'o')

    ax.plot([xnp, xnp],
            [0.0, 0.0],
            [0.0, 0.0],'o')

    # Create cubic bounding box to simulate equal aspect ratio
    X = np.array([xr_w, xt_h+ct_h, xt_v+ct_v])
    Y = np.array([-yt_w, yt_w])
    Z = np.array([zt_w, zt_h, zt_v])
    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())

    # Comment or uncomment following both lines to test the fake bounding box:
    for xb, yb, zb in zip(Xb, Yb, Zb):
        ax.plot([xb], [yb], [zb], 'w')

    plt.show()

def section_chord(aircraft, y_percent, kind='wing'):
    '''y_percent é o y da seção pela semienvergadura (b)
    Ou seja, o percentual da semienvergadura em que a seção em questão está
    kind pode ser wing, EH ou EV, mas o padrão é wing'''
    cr = aircraft['dimensions'][kind]['cr']
    ct = aircraft['dimensions'][kind]['ct']
    sec_chord = cr-np.abs(y_percent)*(cr-ct) 
    return sec_chord 

def chord_surface(aircraft, y_percent, surface_chord_percent, kind='wing'):
    '''dá a corda da superfície (flap, slat, ...)
    inputs: y_percent é a porcentagem da semienvergadura em que a seção se enconra
            surface_chord_percent = percentual da corda preenchida pela superfície
            ex: se o flape ocupa 10% da asa, esse valor deve ser 0.1'''
    sec_chord = section_chord(aircraft, y_percent, kind)
    surface_chord = surface_chord_percent * sec_chord
    return surface_chord