from calc_densidade import*

class Fechamento:
    def __init__(self,m_inicial,m_final,d_inicial,d_final,m_dest,v_dest,api_oleo,api_dest,api_res):
        self.m_inicial = m_inicial
        self.m_final = m_final
        self.d_inicial = d_inicial
        self.d_final = d_final
        self.m_dest = m_dest
        self.v_dest = v_dest
        self.api_oleo = api_oleo
        self.api_dest = api_dest
        self.api_res = api_res


    def MVD(self,perc_mas,perc_vol):
       
        
        self.m_perdas = self.m_inicial - (self.m_final + self.m_dest + perc_mas*self.m_inicial/100)
        self.v_inicial = self.m_inicial/self.d_inicial
        self.v_final = self.m_final/self.d_final
        self.v_perdas = self.v_inicial - (self.v_final + self.v_dest + perc_vol*self.v_inicial/100)
        
        self.mas_dest_perc = 100*self.m_dest/self.m_inicial
        self.vol_dest_perc = 100*self.v_dest/self.v_inicial
        self.mas_res_perc= 100*self.m_final/self.m_inicial
        self.vol_res_perc= 100*self.v_final/self.v_inicial

        self.perda_perc_v = 100*self.v_perdas/self.v_inicial
        self.perda_perc_m = 100*self.m_perdas/self.m_inicial

        self.m_leves = perc_mas*self.m_inicial/100
        self.v_leves = perc_vol*self.v_inicial/100

        #perdas em api
        delta_res = self.api_res*(self.perda_perc_m/100 + self.mas_res_perc/100) + self.api_dest*(self.mas_dest_perc/100) + (perc_mas)

        delta_dest = self.api_res*(self.mas_res_perc/100) + self.api_dest*(self.perda_perc_m/100+self.mas_dest_perc/100) + (perc_mas)
        
        delta_leves = self.api_res*(self.mas_res_perc/100) + self.api_dest*(self.mas_dest_perc/100) + (self.perda_perc_m + perc_mas)

        d = {"Resíduo":abs(delta_res - self.api_oleo),"Destilado":abs(delta_dest - self.api_oleo),"Leves":abs(delta_leves - self.api_oleo)}
        delta = min(d, key=d.get)
        menor = min(d.values())
        
        
        resultado = [self.m_inicial,round(self.v_inicial,1),round(self.m_dest,1),round(self.v_dest,1),self.m_final,round(self.v_final,1),
                     round(self.m_perdas,1),round(self.v_perdas,1),
                     round(self.mas_dest_perc,1),round(self.vol_dest_perc,1),round(self.mas_res_perc,1),round(self.vol_res_perc,1),
                     round(self.perda_perc_m,1),round(self.perda_perc_v,1),round(self.m_leves,1),round(self.v_leves,1),
                     round(self.api_oleo,1),round(self.api_dest,1),round(self.api_res,1),round(perc_mas,1),round(perc_vol,1),
                     delta,round(menor,2)]
        return resultado

    def potstill(self):
        self.m_perdas_p = self.m_inicial - (self.m_final + self.m_dest)
        self.v_inicial_p = self.m_inicial/self.d_inicial
        self.v_final_p = self.m_final/self.d_final
        self.v_perdas_p = self.v_inicial_p - (self.v_final_p + self.v_dest)

        self.mas_dest_perc = 100*self.m_dest/self.m_inicial
        self.vol_dest_perc = 100*self.v_dest/self.v_inicial_p
        self.mas_res_perc= 100*self.m_final/self.m_inicial
        self.vol_res_perc= 100*self.v_final_p/self.v_inicial_p

        self.perda_perc_v_p = 100*self.v_perdas_p/self.v_inicial_p
        self.perda_perc_m_p = 100*self.m_perdas_p/self.m_inicial

        #perdas em api
        delta_res = self.api_res*(self.perda_perc_m_p/100 + self.mas_res_perc/100) + self.api_dest*(self.mas_dest_perc/100) 

        delta_dest = self.api_res*(self.mas_res_perc/100) + self.api_dest*(self.perda_perc_m_p/100+self.mas_dest_perc/100)
        

        d = {"Resíduo":abs(delta_res - self.api_oleo),"Destilado":abs(delta_dest - self.api_oleo)}
        delta = min(d, key=d.get)
        menor = min(d.values())
        
        
        resultado = [self.m_inicial,round(self.v_inicial_p,1),round(self.m_dest,1),round(self.v_dest,1),self.m_final,round(self.v_final_p,1),
                     round(self.m_perdas_p,1),round(self.v_perdas_p,1),
                     round(self.mas_dest_perc,1),round(self.vol_dest_perc,1),round(self.mas_res_perc,1),round(self.vol_res_perc,1),
                     round(self.perda_perc_m_p,1),round(self.perda_perc_v_p,1),
                     round(self.api_oleo,1),round(self.api_dest,1),round(self.api_res,1),
                     delta,round(menor,2)]
        return resultado
