from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
from numpy import fft
import os


################################################################
# Ricardo Tadeu Oliveira Catta Preta
# e-mail: ricardocatta@gmail.com
################################################################
"""
Este código irá carregar o módulo statistica_probes.
As possibilidades de pós processamento aqui desenvolvidas são:
- VELOCIDADE MÉDIA: de algum componente do vetor velocidade;
- DESVIO PADRÃO: de algum componente do vetor velocidade;'
- ENERGIA CINÉTICA TURBULENTA;
- TENSOR DE REYNOLDS SUBMALHA EXATO E ADIMENSIONAL.

Coloquei especificamente para plotar a velocidade média w, a energia cinética
turbulenta e os desvios padrões de u e w.

Para outras componentes, basta alterar de acordo com a necessidade.
"""
# As colunas dos arquivos 'surf00001*' estão salvas na seguinte ordem: 
# names=['ct,t,dt,xc,yc,zc,u,v,w,P,rho,mu,dpm_u,dpm_v,dpm_w,dpm_ufluct,dpm_vfluct,dpm_wfluct'])

# obs: Este código precisa estar dentro da pasta probe_points, que fica dentro do output
#filenames = sorted(glob.glob('datasets/extracts_wu/dataset_*.csv')) # chamando e ordenando os arquivos em ordem crescente
# filenames = sorted(glob.glob('datasets/slide20/00m/20s/surf00001_sonda00058.dat')) # chamando e ordenando os arquivos em ordem crescente
#probes: 719 - 725; 81 - 88; 
def run_fluid_postproc(output_path, result_path, probe):
    probe_id = probe['id']
    path = result_path+'/fluid_results/'+probe_id
    os.makedirs(path,exist_ok = True)

    fn = np.loadtxt(fname=output_path+'/probe_points/'+probe['file'], skiprows=200)
    # vj = 6
    # wj = 12  
    # fn = np.where(fn<1E-12,0,fn)
    ctj = 0
    tj = 1
    i = 3
    j = 4
    k = 5
    uj = 6
    vj = 7
    wj = 8
    pj = 9

    x = []
    y = [] 
    z = []
    u = []                                          # lista para a velocidade u
    v = []                                          # lista para a velocidade v
    w = []    
    ct = []
    t = []                                      # lista para a velocidade w  
    dt = []
    p = []

    xc = [0.173,0.118,0.0899]
    lmin = 10000
    lmax = 70000
    mod = 1
    uf = []
    vf = []
    wf = []
    tf = []
    ctf = []
    pf = []

    u.append(fn[10000:,uj])
    v.append(fn[10000:,vj])
    w.append(fn[10000:,wj])
    t.append(fn[10000:,tj])
    ct.append(fn[10000:,ctj])
    p.append(fn[10000:,pj])

    u = np.array(u)
    v = np.array(v)
    w = np.array(w)
    t = np.array(t)
    ct = np.array(ct)
    p = np.array(p)

    # u = np.where(u<1E-12,0,u)
    # v = np.where(v<1E-12,0,v)
    # w = np.where(w<1E-12,0,w)
    # p = np.where(p<1E-12,0,p)


    for i in range(len(u[0])): #(lmin,lmax): #(len(u[0])):
        if i%mod==0:
            uf.append(u[0,i])
            vf.append(v[0,i])
            wf.append(w[0,i])
            tf.append(t[0,i])
            ctf.append(ct[0,i])
            pf.append(p[0,i])

    uf = np.array(uf)
    vf = np.array(vf)
    wf = np.array(wf)
    tf = np.array(tf)
    ctf = np.array(ctf)
    pf = np.array(pf)
    pf /= 1000
    #sp.plot_espectro(u,v,w,t,xc,ct)
    """
    Irá plotar respectivamente a velocidade média w, desvio padrão de w, 
    desvio padrão de u e energia cinética turbulenta. Os plotes irão comparar
    os resultados simulados com os experimentais.
    """
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('u(t) (m/s)')
    axes1.set_xlabel('t (s)')
    # plt.axhline(y=np.mean(uf), color='r', linestyle='--')
    # plt.legend(['mean'])
    media = np.mean(uf)
    std=np.std(uf)
    axes1.text(tf[len(tf)//2], np.min(uf)-0.05*abs(np.min(uf)), rf'média = ${media:4.2f} \pm {std:4.2f} \, m/s$')
    plt.plot(tf, uf, '-',linewidth=0.8,color='black',alpha=0.6, label="Sonda "+probe_id)
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='purple', label='média')
    plt.ylim([np.min(uf)-0.2*abs(np.min(uf)),1.1*np.max(uf)])
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()
    plt.savefig(path+'/u_vel_'+probe_id+'.png')


    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('v(t) (m/s)')
    axes1.set_xlabel('t (s)')
    media = np.mean(vf)
    std=np.std(vf)
    axes1.text(tf[len(tf)//2], np.min(vf)-0.05*abs(np.min(vf)), rf'média = ${media:4.2f} \pm {std:4.2f} \, m/s$')
    plt.ylim([np.min(vf)-0.2*abs(np.min(vf)),1.1*np.max(vf)])
    plt.plot(tf, vf, '-',linewidth=0.8,color='black',alpha=0.6, label="v velocity (m/s)")
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='purple', label='média')
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()
    plt.savefig(path+'/v_vel_'+probe_id+'.png')


    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('w(t) (m/s)')
    axes1.set_xlabel('t (s)')
    media = np.mean(wf)
    std=np.std(wf)
    axes1.text(tf[len(tf)//2], np.min(wf)-0.05*abs(np.min(wf)), rf'média = ${media:4.2f} \pm {std:4.2f} \, m/s$')
    plt.ylim([np.min(wf)-0.2*abs(np.min(wf)),1.1*np.max(wf)])
    plt.plot(tf, wf, '-',linewidth=0.8,color='black',alpha=0.6, label="w velocity (m/s)")
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='purple', label='média')
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()
    # plt.show()
    plt.savefig(path+'/w_vel_'+probe_id+'.png')

    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Pressure [kPa]')
    axes1.set_xlabel('t [s]')
    media = np.mean(pf)
    std=np.std(pf)
    axes1.text(tf[len(tf)//2], (np.min(pf)-0.005*abs(np.min(pf))), rf'$\mu = {media:4.2f} \pm {std:4.2f} \, kPa$')
    plt.ylim([(np.min(pf)-0.01*abs(np.min(pf))),(1.01*np.max(pf))])
    plt.plot(tf, pf, '-',linewidth=0.8,color='black',alpha=0.6, label="Pressure [kPa]")
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='blue')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='purple', label='mean')
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()
    plt.savefig(path+'/pressure_'+probe_id+'.png')

        # PLOT VELOCITY MAGNITUDE
    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    # axes1.set_ylabel(r'Magnitude da velocidade $[ m/s ]$')
    axes1.set_ylabel(r'Velocity magnitude $[ m/s ]$')
    axes1.set_xlabel('t [s]')
    vel_mag = np.sqrt(uf**2+vf**2+wf**2)
    media = np.mean(vel_mag)
    std=np.std(vel_mag)
    axes1.text(tf[len(tf)//2], np.min(vel_mag)-0.1*abs(np.min(vel_mag)), rf'$\mu = {media:4.2f} \pm {std:4.2f} \, m/s$')
    plt.plot([tf[0],tf[len(tf)-1]],[media-std,media-std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media+std,media+std], '--', linewidth=0.6,color='red')
    plt.plot([tf[0],tf[len(tf)-1]],[media,media], '--', linewidth=0.6,color='brown', label='mean')
    plt.ylim([np.min(vel_mag)-0.5*abs(np.min(vel_mag)),1.1*np.max(vel_mag)])
    plt.plot(tf, vel_mag, '-',linewidth=0.8,color='black',alpha=0.6, label="Probe: "+ probe_id)
    plt.legend(loc='upper left')
    plt.grid(linestyle='--', linewidth=0.3)
    fig.tight_layout()

    plt.savefig(path+'/velmag_mag_'+probe_id+'.png')


    ####################################################################
    # PLOT SPECTRA
    ####################################################################
    def plot_espectro(u,v,w,t,xc):
        """
         Plota a densidade espectral da energia cinética turbulenta.
        """

        font = FontProperties()
        font.set_family('serif')

        x1R = 1
        x2R = 10000
        xR = np.arange(x1R,x2R,10)
        yR = np.exp((-5.0/3.0)*np.log(xR))*10000000000

        dir = [""]

        ept_kinetic = []

        kinetic_energy =[]
        frequency = []

        ept = Fourier_transform_ke(t,xc,u,v,w)
        ept_kinetic.append(ept)

        kinetic_energy1,  frequency1 = Fourier_transform_ke(t,xc,u,v,w)
        kinetic_energy.append(kinetic_energy1)
        frequency.append(frequency1)    


        cor =["darkgray","tab:blue","tab:red","black"]
        plt.figure(dpi=150)

        # print("Energia cinética = \n", kinetic_energy)
        # print("Frequência = \n", frequency)

        for i in range(len(ept_kinetic)):

            plt.xlabel(r'$\log{f}$ [Hz]', fontsize=18, fontproperties=font)
            plt.ylabel(r'$\log{E_{k}}$', fontsize=18, fontproperties=font)
            plt.loglog(frequency[i],kinetic_energy[i],color='red',linewidth=0.8)
            p_ret  = plt.loglog(xR,yR,'--',color='black',alpha=0.6,linewidth=1.5, label=rf'$m = -5/3$')

        ax= plt.gca()	
        ax.set_xlim([1,1000])
        ax.set_ylim([0.00001,100000000])	
        # ax.legend(title='Coeficiente Angular')
        ax.legend(title='Slope')
        # plt.title('Densidade Espectral de Energia Cinética Turbulenta')	
        plt.title('Turbulent Kinetic Energy Spectrum')	
        plt.grid(linestyle='--', linewidth=0.3)

        plt.tight_layout()
        plt.savefig(path+'/ke_'+probe_id+'.png')

        #plt.savefig('Espectro.png', format='png', dpi=350)
        # plt.show()

    ####################################################################
    # FOURIER TRANSFORM
    ####################################################################
    def Fourier_transform_ke(t,xc,u,v,w):
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


    plot_espectro(u[0,:],v[0,:],w[0,:],t[0,:],xc)
