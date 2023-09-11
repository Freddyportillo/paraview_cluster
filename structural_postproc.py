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
    node_id = node['id']
    path = result_path+'/str_results/'+node_id
    os.makedirs(path,exist_ok = True)

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

    uf = np.array(uf)
    vf = np.array(vf)
    wf = np.array(wf)
    xf = np.array(xf)
    yf = np.array(yf)
    zf = np.array(zf)
    tf = np.array(tf)
    ctf = np.array(ctf)
    
    xf -= x[0,0]
    yf -= y[0,0]
    zf -= z[0,0]

    xf *= 10000.0
    yf *= 10000.0
    zf *= 10000.0

    # PLOT X DISPLACMENT 
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel(r'Deslocamento nodal na direção $x$ [$ \times 10^{-3} $m]')
    axes1.set_xlabel('t (s)')
    media = np.mean(xf)
    std=np.std(xf)
    axes1.text(tf[len(tf)//2], np.min(xf)-0.1*abs(np.min(xf)), rf'$\mu = {media:4.2f} \pm {std:4.2f} \, mm$')
    plt.ylim([np.min(xf)-0.2*abs(np.min(xf)),1.1*np.max(xf)])
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='brown', label='média')
    plt.plot(tf, xf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()
    plt.savefig(path+'/u_disp_'+node_id+'.png')

    # PLOT Y DISPLACEMENT
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel(r'Deslocamento nodal na direção $y$ [$ \times 10^{-3} $m]')
    axes1.set_xlabel('t (s)')
    media = np.mean(yf)
    std=np.std(yf)
    axes1.text(tf[len(tf)//2], np.min(yf)-0.1*abs(np.min(yf)), rf'$\mu = {media:4.2f} \pm {std:4.2f} \,  mm $')
    plt.ylim([np.min(yf)-0.2*abs(np.min(yf)),1.1*np.max(yf)])
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='brown', label='média')
    plt.plot(tf, yf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()

    plt.savefig(path+'/v_disp_'+node_id+'.png')

    # PLOT Z DISPLACEMENT
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel(r'Deslocamento nodal na direção $z$ [$ \times 10^{-3} $m]')
    axes1.set_xlabel('t (s)')
    media = np.mean(zf)
    std=np.std(zf)
    axes1.text(tf[len(tf)//2], np.min(zf)-0.1*abs(np.min(zf)), rf'$\mu = {media:4.2f} \pm {std:4.2f} \, mm$')
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='brown', label='média')
    plt.ylim([np.min(zf)-0.2*abs(np.min(zf)),1.1*np.max(zf)])
    plt.plot(tf, zf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()

    plt.savefig(path+'/w_disp_'+node_id+'.png')

    # PLOT DISPLACEMENT MAGNITUDE
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel(r'Magnitude do deslocamento nodal [$ \times 10^{-3} $m]')
    axes1.set_xlabel('t (s)')
    disp_mag = np.sqrt(xf**2+yf**2+zf**2)
    media = np.mean(disp_mag)
    std=np.std(disp_mag)
    axes1.text(tf[len(tf)//2], np.min(disp_mag)-0.1*abs(np.min(disp_mag)), rf'$\mu = {media:4.2f} \pm {std:4.2f} \, mm$')
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='brown', label='média')
    plt.ylim([np.min(disp_mag)-0.2*abs(np.min(disp_mag)),1.1*np.max(disp_mag)])
    plt.plot(tf, disp_mag, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()

    plt.savefig(path+'/disp_mag_'+node_id+'.png')

    # # PLOT VELOCIY IN X DIRECTION
    # fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    # axes1 = fig.add_subplot(1, 1, 1)
    # axes1.set_ylabel('Velocidade nodal na direção x [m/s]')
    # axes1.set_xlabel('t (s)')
    # plt.plot(tf, uf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    # plt.legend(loc='best')
    # plt.grid(linestyle='--', linewidth=0.3)
    # fig.tight_layout()

    # plt.savefig(path+'/xvel_disp_'+node_id+'.png')

    # # PLOT VELOCIY IN Y DIRECTION
    # fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    # axes1 = fig.add_subplot(1, 1, 1)
    # axes1.set_ylabel('Velocidade nodal na direção y [m/s]')
    # axes1.set_xlabel('t (s)')
    # plt.plot(tf, vf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    # plt.legend(loc='best')
    # plt.grid(linestyle='--', linewidth=0.3)
    # fig.tight_layout()

    # plt.savefig(path+'/yvel_disp_'+node_id+'.png')

    # # PLOT VELOCIY IN Z DIRECTION
    # fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    # axes1 = fig.add_subplot(1, 1, 1)
    # axes1.set_ylabel('Velocidade nodal na direção z [m/s]')
    # axes1.set_xlabel('t (s)')
    # plt.plot(tf, wf, '-',linewidth=0.8,color='black', label="Node: "+ node_id)
    # plt.legend(loc='best')
    # plt.grid(linestyle='--', linewidth=0.3)
    # fig.tight_layout()

    # plt.savefig(path+'/zvel_disp_'+node_id+'.png')

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
        dt = t[N//2+1]-t[N//2]
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

        plt.xlabel('Frequencia [Hz]', fontsize=19, fontproperties=font)
        plt.ylabel(r'Amplitude [$ \times 10^{-3} $m]', fontsize=19, fontproperties=font)
        plt.plot(f_plot,X_mag_plot,color='black',linewidth=0.9, label = 'x')
        plt.plot(f_plot,Y_mag_plot,color='blue',linewidth=0.9, label = 'y')
        plt.plot(f_plot,Z_mag_plot,color='red',linewidth=0.9, label = 'z')
        plt.legend(loc='best')

        maxdeslocs = [np.max(X_mag_plot),np.max(Y_mag_plot),np.max(Z_mag_plot) ]
        ax= plt.gca()	
        # ax.set_yscale('log')
        ax.set_xlim([0,60])
        ax.set_ylim([-0.05,1.2*np.max(maxdeslocs)])	
        plt.title('FFT')	
        plt.grid(linestyle='--', linewidth=0.3)
        plt.tight_layout()
        # plt.show()
        plt.savefig(path+'/FFT_'+node_id+'.png')

###########################################################################
    Fourier_transform(tf,xf,yf,zf)
    
    print('STRUCTURAL_OUTPUT: ',path)
    print('The structural probe was readed and treated succesfully')
    print('END OF POST-PROCESSING ROUTINE')