from flask import Flask, render_template, request, Response
import pandas as pd
from calc_densidade import*
from fechamento import*

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html",value=["",""])


@app.route("/calculo_densidade",methods=["POST",])
def calculo_densidade():
    rho = request.form['rho']
    temp = request.form['temp']
    if temp == "":
        temp = 20
    densidade = Densidade(float(rho),float(temp)).d_calc()
    return render_template("index.html",value=[round(densidade[0],4),round(densidade[1],1)])



@app.route("/balcomp")
def balcomp():
    return render_template("balcomp.html")


@app.route("/calculo_balcomp",methods=["POST",])
def calculo_balcomp():
    rho_oleo = request.form['rho_oleo']
    temp_oleo = request.form['temp_oleo']
    rho_res = request.form['rho_res']
    temp_res = request.form['temp_res']
    m_oleo = request.form['m_oleo']
    mas_res = request.form['mas_res']

    perc_mas = request.form['perc_mas']
    perc_vol = request.form['perc_vol']
    
    
    frac_pot = request.form['frac_pot']
    
    aet = [i for i in request.form.getlist('temp')]
    massa = [float(i) for i in request.form.getlist('massa')]
    rho = [i for i in request.form.getlist('rho')]
    rho_temp = [i for i in request.form.getlist('rho_temp')]

    rho_conv = []
    api_conv = []
    vol_dest = []
    for i in range(len(aet)):
        rho_conv.append(Densidade(float(rho[i]),float(rho_temp[i])).d_calc()[0])
        api_conv.append(Densidade(float(rho[i]),float(rho_temp[i])).d_calc()[1])
        vol_dest.append(float(massa[i])/Densidade(float(rho[i]),float(rho_temp[i])).d_calc()[0])
        
    
    if frac_pot:
        
        rho_conv_mvd = [rho_conv[i] for i in range(int(frac_pot))]
        rho_conv_pot = [rho_conv[i] for i in range(int(frac_pot),len(aet),1)]
        api_conv_mvd = [api_conv[i] for i in range(int(frac_pot))]
        api_conv_pot = [api_conv[i] for i in range(int(frac_pot),len(aet),1)]
        vol_dest_mvd = [float(massa[i])/rho_conv[i] for i in range(int(frac_pot))]
        vol_dest_pot = [float(massa[i])/rho_conv[i] for i in range(int(frac_pot),len(aet),1)]
        mas_dest_mvd = [float(massa[i]) for i in range(int(frac_pot))]
        mas_dest_pot = [float(massa[i]) for i in range(int(frac_pot),len(aet),1)]

        m_oleo_p = request.form['m_oleo_p']
        mas_res_p = request.form['mas_res_p']
        rho_res_p = request.form['rho_res_p']
        temp_res_p = request.form['temp_res_p']

        volume_destilado_pot = sum(vol_dest_pot)
        massa_destilado_pot = sum(mas_dest_pot)

        volume_destilado_mvd = sum(vol_dest_mvd)
        massa_destilado_mvd = sum(mas_dest_mvd)

        #destilado da pot
        rho_dest_pot = Densidade(massa_destilado_pot/volume_destilado_pot,20).d_calc()
        dens_dest_pot = rho_dest_pot[0]
        api_dest_pot = rho_dest_pot[1]

        #destilado da mvd
        rho_dest_mvd = Densidade(massa_destilado_mvd/volume_destilado_mvd,20).d_calc()
        dens_dest_mvd = rho_dest_mvd[0]
        api_dest_mvd = rho_dest_mvd[1]

        #carga da mvd
        rho_oleo_mvd = Densidade(float(rho_oleo),float(temp_oleo)).d_calc()
        rho_oleo_conv = rho_oleo_mvd[0]
        api_oleo_conv = rho_oleo_mvd[1]

        #resíduo da mvd
        rho_res_mvd = Densidade(float(rho_res),float(temp_res)).d_calc()
        rho_res_conv = rho_res_mvd[0]
        api_res_conv = rho_res_mvd[1]

        #carga da potstill
        rho_carga_pot = rho_res_conv
        api_carga_pot = api_res_conv

        #resíduo da potstill
        rho_res_pot = Densidade(float(rho_res_p),float(temp_res_p)).d_calc()
        rho_res_conv_pot = rho_res_pot[0]
        api_res_conv_pot = rho_res_pot[1]

        #resultado mvd
        resultado_mvd = Fechamento(float(m_oleo),float(mas_res),float(rho_oleo_conv),float(rho_res_conv),
                               float(massa_destilado_mvd),float(volume_destilado_mvd),
                               float(api_oleo_conv),float(api_dest_mvd),float(api_res_conv)).MVD(float(perc_mas),float(perc_vol))

        resultado_pot = Fechamento(float(m_oleo_p),float(mas_res_p),float(rho_res_conv),float(rho_res_conv_pot),
                               float(massa_destilado_pot),float(volume_destilado_pot),
                               float(api_res_conv),float(api_dest_pot),float(api_res_conv_pot)).potstill()
         #criação da pev
        fracao_massica = []
        soma_mvd = 0
        soma = 0
        for i in range(len(massa)):
            if i<int(frac_pot):
                soma += massa[i]/float(m_oleo)
                fracao_massica.append(round(soma,2))
            else:
                soma += (massa[i]/float(m_oleo))*float(mas_res)/float(m_oleo_p)
                fracao_massica.append(round(soma,2))

        api_conv2 = []
        for i in range(len(aet)):
            api_conv2.append(round(Densidade(float(rho[i]),float(rho_temp[i])).d_calc()[1],1))
        
        return render_template("resultado_baldest_pot.html",resultado=resultado_mvd,resultado_pot=resultado_pot,frac=fracao_massica,api=api_conv2,aet=aet)
    
    else:
        volume_destilado = sum(vol_dest)
        massa_destilado = sum(massa)
        
        rho_dest = Densidade(massa_destilado/volume_destilado,20).d_calc()
        dens_dest = rho_dest[0]
        api_dest = rho_dest[1]

        rho_oleo_2 = Densidade(float(rho_oleo),float(temp_oleo)).d_calc()
        rho_oleo_conv = rho_oleo_2[0]
        api_oleo_conv = rho_oleo_2[1]

        rho_res_2 = Densidade(float(rho_res),float(temp_res)).d_calc()
        rho_res_conv = rho_res_2[0]
        api_res_conv = rho_res_2[1]
        
        resultado = Fechamento(float(m_oleo),float(mas_res),float(rho_oleo_conv),float(rho_res_conv),
                               float(massa_destilado),float(volume_destilado),
                               float(api_oleo_conv),float(api_dest),float(api_res_conv)).MVD(float(perc_mas),float(perc_vol))
        #criação da pev
        fracao_massica = []
        soma = 0
        for i in range(len(massa)):
            soma += massa[i]/float(m_oleo)
            fracao_massica.append(round(soma,2))

        api_conv2 = []
        for i in range(len(aet)):
            api_conv2.append(round(Densidade(float(rho[i]),float(rho_temp[i])).d_calc()[1],1))
        return render_template("resultado_baldest.html",resultado=resultado,frac=fracao_massica,api=api_conv2,aet=aet)
    



if __name__=="__main__":
    app.run(debug=True)

