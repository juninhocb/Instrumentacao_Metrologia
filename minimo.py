# minima
R1 =100;
R2 =100;
RtMin = 100;
RtMax = 138.51;
R3 = (RtMin+RtMax)/2;
RT = 100;
Rf = 24;
VI= 0.5;

V0ponte = VI*((R2/(R1+R2) - ((RT + Rf)/(R3+RT+2*Rf))));
Va = 0.25;
Vb = Va + V0ponte;
V0 = 200*(Va-Vb)

print(V0)