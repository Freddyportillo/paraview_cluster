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

    fn = np.loadtxt(fname=output_path+'/probe_points/'+probe['file'], skiprows=2)
    # vj = 6
    # wj = 12  
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
    min = 10000
    max = 70000
    mod = 1
    uf = []
    vf = []
    wf = []
    tf = []
    ctf = []
    pf = []

    u.append(fn[min:max,uj])
    v.append(fn[min:max,vj])
    w.append(fn[min:max,wj])
    t.append(fn[min:max,tj])
    ct.append(fn[min:max,ctj])
    p.append(fn[min:max,pj])

    u = np.array(u)
    v = np.array(v)
    w = np.array(w)
    t = np.array(t)
    ct = np.array(ct)
    p = np.array(p)

    for i in range(len(u[0])):
        if i%mod==0:
            uf.append(u[0,i])
            vf.append(v[0,i])
            wf.append(w[0,i])
            tf.append(t[0,i])
            ctf.append(ct[0,i])
            pf.append(p[0,i])

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
    plt.axhline(y=np.mean(uf), color='r', linestyle='--')
    plt.legend(['mean'])
    plt.plot(tf, uf, '-',linewidth=0.8,color='black', label="u velocity (m/s)")
    # plt.legend(loc='best')
    # plt.xlim([0.2,0.8])
    plt.grid()
    fig.tight_layout()
    # plt.show()
    plt.savefig(path+'/u_vel_'+probe_id+'.png')


    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('v(t) (m/s)')
    axes1.set_xlabel('t (s)')
    plt.axhline(y=np.mean(vf), color='r', linestyle='--')
    plt.legend(['mean'])
    plt.plot(tf, vf, '-',linewidth=0.8,color='black', label="v velocity (m/s)")
    plt.xlim([0.2,0.8])
    plt.grid()
    fig.tight_layout()
    # plt.show()
    plt.savefig(path+'/v_vel_'+probe_id+'.png')


    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('w(t) (m/s)')
    axes1.set_xlabel('t (s)')
    plt.axhline(y=np.mean(wf), color='r', linestyle='--')
    plt.legend(['mean'])
    plt.plot(tf, wf, '-',linewidth=0.8,color='black', label="w velocity (m/s)")
    plt.xlim([0.2,0.8])
    plt.grid()
    fig.tight_layout()
    # plt.show()
    plt.savefig(path+'/w_vel_'+probe_id+'.png')

    fig = plt.figure(dpi=150)                       # resolução da imagem por ponto
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.set_ylabel('Pressure (Pa)')
    axes1.set_xlabel('t (s)')
    plt.axhline(y=np.mean(pf), color='r', linestyle='--')
    plt.legend(['mean'])
    plt.plot(tf, pf, '-',linewidth=0.8,color='black', label="Pressure (Pa)")
    plt.xlim([0.2,0.8])
    plt.grid()
    fig.tight_layout()
    # plt.show()
    plt.savefig(path+'/pressure_'+probe_id+'.png')


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
        yR = np.exp((-5.0/3.0)*np.log(xR))*1000000000

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

        print("Energia cinética = \n", kinetic_energy)
        print("Frequência = \n", frequency)

        for i in range(len(ept_kinetic)):

            plt.xlabel('$\log{f}$ [Hz]', fontsize=19, fontproperties=font)
            plt.ylabel('$\log{E(f)}$', fontsize=19, fontproperties=font)
            plt.loglog(frequency[i],kinetic_energy[i],color='red',linewidth=0.8)
            p_ret  = plt.loglog(xR,yR,'--',color='black',linewidth=1.5, label='$m = -5/3$')

        ax= plt.gca()	
        ax.set_xlim([1,10000])
        ax.set_ylim([0.00001,10000000])	
        ax.legend(title='Coeficiente Angular')
        plt.title('Densidade Espectral de Energia Cinética Turbulenta')	
        plt.grid()
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
