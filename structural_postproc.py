#!./paraview-5.11.1/bin/pvpython
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import fft
# importing os module
import os
from matplotlib.font_manager import FontProperties


def run_structural_postproc(output_path, node):
    directory = 'str_'+node
    path = os.path.join(output_path,directory)
    os.makedirs(path,exist_ok = True)

    if len(node)==1:
        node_id = '00000'+ node
    elif len(node)==2: 
        node_id = '0000'+ node
    elif len(node)==3: 
        node_id = '000'+ node
    elif len(node)==4: 
        node_id = '00'+ node
    elif len(node)==5: 
        node_id = '0'+ node
    elif len(node)==6: 
        node_id = node

    fn = np.loadtxt(fname=output_path+'/probes_fsi/str_001_node'+node_id+'.dat', skiprows=2)

    ctj = 0; tj = 1; i = 2; j = 3; k = 4; uj = 5; vj = 6; wj = 7 #id's into .dat file

    x = []
    y = [] 
    z = []
    u = []                                          # lista para a velocidade u
    v = []                                          # lista para a velocidade v
    w = []    
    ct = []
    t = []                                      # lista para a velocidade w  
    dt = []

    min = 0 #277
    max = 4720#1685
    mod = 1

    uf = []
    vf = []
    wf = []
    tf = []
    ctf = []
    xf = []
    yf = []
    zf = []

    u.append(fn[:,uj])
    v.append(fn[:,vj])
    w.append(fn[:,wj])
    t.append(fn[:,tj])
    ct.append(fn[:,ctj])
    x.append(fn[:,i])
    y.append(fn[:,j])
    z.append(fn[:,k])

    u = np.array(u)
    v = np.array(v)
    w = np.array(w)
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    t = np.array(t)
    ct = np.array(ct)

    for i in range(len(u[0])):
        if i%mod==0:
            uf.append(u[0,i])
            vf.append(v[0,i])
            wf.append(w[0,i])
            tf.append(t[0,i])
            ctf.append(ct[0,i])
            xf.append(x[0,i])
            yf.append(y[0,i])
            zf.append(z[0,i])

    xf -= x[0,0]
    yf -= y[0,0]
    zf -= z[0,0]


    # PLOT X DISPLACMENT 
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Deslocamento nodal na direção x (m)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, xf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/u_disp_'+node_id+'.png')

    # PLOT Y DISPLACEMENT
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Deslocamento nodal na direção y (m)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, yf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/v_disp_'+node_id+'.png')

    # PLOT Z DISPLACEMENT
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Deslocamento nodal na direção z (m)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, zf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/w_disp_'+node_id+'.png')

    # PLOT VELOCIY IN X DIRECTION
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Velocidade nodal na direção x (m/s)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, uf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/xvel_disp_'+node_id+'.png')

    # PLOT VELOCIY IN Y DIRECTION
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Velocidade nodal na direção y (m/s)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, vf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/yvel_disp_'+node_id+'.png')

    # PLOT VELOCIY IN Z DIRECTION
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Velocidade nodal na direção z (m/s)')
    axes1.set_xlabel('t (s)')
    plt.plot(tf, wf[0:], '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='best')
    plt.grid()
    fig.tight_layout()

    plt.savefig(path+'/zvel_disp_'+node_id+'.png')

    ###########################################################################
    ###########################################################################

    ####################################################################
    # PLOT SPECTRA
    ####################################################################
    def plot_espectro(u,v,w,t):
        """
        Plota a densidade espectral da energia cinética turbulenta.
        """

        font = FontProperties()
        font.set_family('serif')

        x1R = 1
        x2R = 10000
        xR = np.arange(x1R,x2R,10)
        yR = np.exp((-5.0/3.0)*np.log(xR))*1000000000

        dir = [""]

        ept_kinetic = []

        kinetic_energy =[]
        frequency = []

        ept = Fourier_transform_ke(t,u,v,w)
        ept_kinetic.append(ept)

        kinetic_energy1,  frequency1 = Fourier_transform_ke(t,u,v,w)
        kinetic_energy.append(kinetic_energy1)
        frequency.append(frequency1)    


        cor =["darkgray","tab:blue","tab:red","black"]
        plt.figure(dpi=150)

        print("Energia cinética = \n", kinetic_energy)
        print("Frequência = \n", frequency)

        for i in range(len(ept_kinetic)):

            plt.xlabel('Frequency [Hz]', fontsize=19, fontproperties=font)
            plt.ylabel('Amplitude [m]', fontsize=19, fontproperties=font)
            plt.plot(frequency[i],kinetic_energy[i],color='red',linewidth=0.8)
            # p_ret  = plt.loglog(xR,yR,'--',color='black',linewidth=1.5, label='$m = -5/3$')

        ax= plt.gca()	
        ax.set_yscale('linear')
        ax.set_xlim([0,500])
        # ax.set_ylim([0.00001,0.01])	
        # ax.legend(title='Coeficiente Angular')
        plt.title('FFT')	
        plt.grid()
        #plt.savefig('Espectro.png', format='png', dpi=350)
        plt.savefig(path+'/FFT_'+node_id+'.png')

    ####################################################################
    # FOURIER TRANSFORM
    ####################################################################
    def Fourier_transform_ke(t,u,v,w):
        """
        Calcula a transformada de Fourier da energia cinética turbulenta.
        INPUT:
        - ul = componente x da flutuação da velocidade;
        - vl = componente y da flutuação da velocidade;
        - wl = componente z da flutuação da velocidade;
        - xc = componente x do espaço;
        - t = tempo.
        OUTPUT:
        Retorna os valores da energia cinética turbulenta e a frequência.
        """
        # Calculando as flutações das componentes da velocidade
        ul = u - np.mean(u)
        vl = v - np.mean(v)
        wl = w - np.mean(w)

        Enel = (ul * ul + vl * vl + wl * wl)/2

        yl = Enel
        nl = len(yl)
        kl = np.arange(nl)
        frql = kl
        frql = frql[range(nl//2)]
        Yl1 = np.fft.fft(yl)
        Yl = np.sqrt(Yl1.real ** 2 + Yl1.imag ** 2)
        Yl = Yl[range(nl//2)]
        return Yl, frql
    ###########################################################################
    ###########################################################################
    plot_espectro(uf,vf,wf,tf)
    # plot_espectro(vf,vf,vf,tf)
    # plot_espectro(wf,wf,wf,tf)