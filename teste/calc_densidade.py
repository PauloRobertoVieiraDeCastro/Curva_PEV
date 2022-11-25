class Densidade:
    def __init__(self,SG_T,T):
        self._SG_T = SG_T
        self._T = T

    def d_calc(self):
        import math
        SG_20 = self._SG_T;
        SG_20_n_menos_1 = 0;
        while True:
            if(SG_20< 0.479):
                a1 = -2462*math.pow(10,-6)
                a2 = 3215*math.pow(10,-6)
                b1 = -10.14*math.pow(10,-6)
                b2 = 17.38*math.pow(10,-6)

            if(SG_20>=0.498 and SG_20< 0.518):
                a1 = -2391*math.pow(10,-6)
                a2 = 3074*math.pow(10,-6)
                b1 = -8.41*math.pow(10,-6)
                b2 = 13.98*math.pow(10,-6)


            if(SG_20>=0.518 and SG_20< 0.539):
                a1 = -2294*math.pow(10,-6)
                a2 = 2887*math.pow(10,-6)
                b1 = -8.39*math.pow(10,-6)
                b2 = 13.87*math.pow(10,-6)

            if(SG_20>=0.539 and SG_20< 0.559):
                a1 = -2164*math.pow(10,-6)
                a2 = 2615*math.pow(10,-6)
                b1 = -5.46*math.pow(10,-6)
                b2 = 8.55*math.pow(10,-6)

            if(SG_20>=0.559 and SG_20< 0.579):
                a1 = -1920*math.pow(10,-6)
                a2 = 2214*math.pow(10,-6)
                b1 = -5.51*math.pow(10,-6)
                b2 = 8.55*math.pow(10,-6)

            if(SG_20>=0.579 and SG_20< 0.6):
                a1 = -2358*math.pow(10,-6)
                a2 = 2962*math.pow(10,-6)
                b1 = -12.25*math.pow(10,-6)
                b2 = 20.15*math.pow(10,-6)

            if(SG_20>=0.6 and SG_20< 0.615):
                a1 = -1361*math.pow(10,-6)
                a2 = 1300*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.615 and SG_20< 0.635):
                a1 = -1237*math.pow(10,-6)
                a2 = 1100*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.635 and SG_20<0.655):
                a1 = -1077*math.pow(10,-6)
                a2 = 850*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.655 and SG_20<0.675):
                a1 = -1011*math.pow(10,-6)
                a2 = 750*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.675 and SG_20<0.695):
                a1 = -977*math.pow(10,-6)
                a2 = 700*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.695 and SG_20<0.746):
                a1 = -1005*math.pow(10,-6)
                a2 = 740*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.746 and SG_20<0.766):
                a1 = -1238*math.pow(10,-6)
                a2 = 1050*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.766 and SG_20<0.786):
                a1 = -1084*math.pow(10,-6)
                a2 = 850*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.786 and SG_20<0.806):
                a1 = -965*math.pow(10,-6)
                a2 = 700*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.806 and SG_20<0.826):
                a1 = -843.5*math.pow(10,-6)
                a2 = 550*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.826 and SG_20<0.846):
                a1 = -719*math.pow(10,-6)
                a2 = 400*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.846 and SG_20<0.871):
                a1 = -617*math.pow(10,-6)
                a2 = 280*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.871 and SG_20<0.896):
                a1 = -512*math.pow(10,-6)
                a2 = 160*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.896 and SG_20<0.996):
                a1 = -394.8*math.pow(10,-6)
                a2 = 30*math.pow(10,-6)
                b1 = -0.49*math.pow(10,-6)
                b2 = 0.6*math.pow(10,-6)

            if(SG_20>=0.996):
                a1 = -542.6*math.pow(10,-6)
                a2 = 177.8*math.pow(10,-6)
                b1 = 2.31*math.pow(10,-6)
                b2 = -2.2*math.pow(10,-6)

            P1a = (9/5)*0.999042*(a1 + 16*b1 - (a2 + 16*b2)*(8*a1 + 64*b1)/(1 + 8*a2 + 64*b2))
            P1 = P1a
            P2a = (9/5)*(a2 + 16*b2)/(1 + 8*a2 + 64*b2)
            P2 = P2a
            P3a = (81/25)*0.999042*(b1 - b2*(8*a1 + 64*b1)/(1 + 8*a2 + 64*b2))
            P3 = P3a
            P4a = (81/25)*b2/(1 + 8*a2 + 64*b2)
            P4 = P4a

            SG_20_n_menos_2 = SG_20_n_menos_1
            SG_20_n_menos_1 = SG_20
            SG_20 = ( self._SG_T - P1*(self._T - 20) - P3*math.pow((self._T - 20),2) )/(1 + P2*(self._T - 20) + P4*math.pow((self._T-20),2))
            #print(SG_20)
            if(abs(SG_20 - SG_20_n_menos_1) > 0.000001):
                if(abs(SG_20 - SG_20_n_menos_2) > 0.000001):
                    keeplooping = 1
                else:
                    SG_20 = (SG_20 + SG_20_n_menos_1)/2.0
                    keeplooping = 0
            else:
                #//SG_20 = (SG_20 + SG_20_n_menos_1)/2.0;
                keeplooping = 0

            if(keeplooping == 1 or self._T == 20):
                SG_15 = ( SG_20 - 0.999042*(8*a1 + 64*b1))/(0.999042*(1 + 8*a2 + 64*b2))
                APIa = (141.5/SG_15) - 131.5

                break
        return [SG_20,APIa]
    
    def __str__(self):
        return "Modelo de cálculo de densidade de óleos em temperaturas diferentes"

#a = Densidade(0.8778,70)
#print(a)
#cimentO1!2013@
