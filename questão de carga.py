Pmax = 197; #alterado
Peso = 86; #alterado 
EmaxTra = 0.02; #def max
EmaxCom = -0.01; # def max
R0 = 210; #alterado
G = 2.2; # ok



mtra = EmaxTra / Pmax;
mcom = EmaxCom /Pmax;

Etra = mtra*Peso;
Ecom = mcom*Peso;

RTtra = R0+(G*R0*Etra)
RTcom = R0+(G*R0*Ecom)


i = 15/(RTtra + RTcom);

V0Mais = 15 - i*RTcom;
V0menos = 15 - i*RTtra;

V0 = V0Mais - V0menos

print(V0)