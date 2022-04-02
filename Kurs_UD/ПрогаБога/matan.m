clear
syms p Mz_deltaB h w0 Ya_Alpha K_v K_wz Vzad Wpriv W ksi tau
W=Mz_deltaB*(p+Ya_Alpha)/(p^2+2*h*p+w0^2);
% Wpriv=1/(tau^2*p^2+2*tau*ksi*p+1);
A=[1 -1/p;
   -K_v/(1/(W*Wpriv)+K_wz) 1];
B=[0; -K_v*Vzad/(1/(W*Wpriv)+K_wz)];
