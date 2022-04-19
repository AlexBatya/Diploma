clear
global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
% load('Area_of_possible_flights.mat');
load('Area_of_possible_flights2.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
mass=180000;
Jz=7.7*10^6;
X_Tzv=0.25;

mah=0.8;
height=11000;
number=10;
h_h=2000;


[A,B,C,D]=StateSpace(mah,height);
diffura=ss(A,B,C,D);
diffura.StateName = {'Alpha', 'wz', 'Vy'};
diffura.OutputName = {'Alpha', 'wz', 'Vy'};
diffura.inputname = {'deltaB'}; 

H=Hob(1):h_h:Hob(end);

M_min=interp1(Hob,M_min',H)';
M_max=interp1(Hob,M_max,H)';
M1=[M_min M_max];
[n,m]=size(M1);


for i=1:n 
    M6 = linspace(M1(i,1),M1(i,end),number);
    M5(i,:)=M6;
end
% writematrix(M5,'M.xls')

[Drive,w]=DriveParameters(M5,H);
[Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(M5,H);  
% writematrix(Mz_Alpha,'Mz_Alpha.xls')
% [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w)
% K_v
% K_wz

[n,m]=size(M5);
for i=1:n
    for j=1:m
    [W_raz,K_v(i,j),K_wz(i,j),K_H,i_p(i,j),i_H(i,j)]=Synthesis_of_ACS(M5(i,j),H(i),w);
    end
end
% writematrix(K_wz,'Kwz.xls')
% writematrix(K_v,'Kv.xls')
% K_v
% K_wz
% W=feedback(W_raz,1);


