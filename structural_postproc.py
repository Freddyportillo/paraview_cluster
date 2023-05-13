#!./paraview-5.11.1/bin/pvpython
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import fft
# importing os module
import os
from matplotlib.font_manager import FontProperties


def run_structural_postproc(output_path, result_path, node):
    # directory = 'str_'+node
    # # path = os.path.join(output_path,directory)
    # # os.makedirs(path,exist_ok = True)
    path = result_path
    node_id = node['id']

    fn = np.loadtxt(fname=output_path+'/probes_fsi/'+node['file'], skiprows=2)

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

    # xf -= x[0,0]
    # yf -= y[0,0]
    # zf -= z[0,0]


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
    ###########################################################################

    def Fourier_transform(t,x,y,z):
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

        font = FontProperties()
        font.set_family('serif')

        N = len(t)
        dt = t[101]-t[100]
        freq_sampling = 1/dt
        fstep = freq_sampling/N
        frq = np.linspace(0, (N-1)*fstep, N) 

        X = np.fft.fft(x)
        X_mag = np.abs(X)/N

        Y = np.fft.fft(y)
        Y_mag = np.abs(Y)/N

        Z = np.fft.fft(z)
        Z_mag = np.abs(Z)/N

        f_plot = frq[0:int(N/2+1)]
        X_mag_plot = 2*X_mag[0:int(N/2+1)]
        Y_mag_plot = 2*Y_mag[0:int(N/2+1)]
        Z_mag_plot = 2*Z_mag[0:int(N/2+1)]

        plt.figure(dpi=150)

        plt.xlabel('Frequency [Hz]', fontsize=19, fontproperties=font)
        plt.ylabel('Amplitude [m]', fontsize=19, fontproperties=font)
        plt.plot(f_plot,X_mag_plot,color='black',linewidth=0.8, label = 'u')
        plt.plot(f_plot,Y_mag_plot,color='blue',linewidth=0.8, label = 'v')
        plt.plot(f_plot,Z_mag_plot,color='red',linewidth=0.8, label = 'w')
        plt.legend(loc='best')

        ax= plt.gca()	
        ax.set_yscale('log')
        ax.set_xlim([0,350])
        # ax.set_ylim([-0.0001,0.001])	
        plt.title('FFT')	
        plt.grid()

        plt.savefig(path+'/FFT_'+node_id+'.png')

###########################################################################
    Fourier_transform(tf,xf,yf,zf)
    
    print('STRUCTURAL_OUTPUT: ',path)
    print('The structural probe was readed and treated succesfully')
    print('END OF POST-PROCESSING ROUTINE')