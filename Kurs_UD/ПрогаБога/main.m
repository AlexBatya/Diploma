clear
global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
load('Area_of_possible_flights.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
mass=180000;
Jz=7.7*10^6;
X_Tzv=0.45;

mah=1;
height=11000;

[A,B,C,D]=StateSpace(mah,height);
diffura=ss(A,B,C,D);
diffura.StateName = {'Alpha', 'wz', 'Vy'};
diffura.OutputName = {'Alpha', 'wz', 'Vy'};
diffura.inputname = {'deltaB'}; 

h_h=2000;
H=Hob(1):h_h:Hob(end);

M_min=interp1(Hob,M_min',H)';
M_max=interp1(Hob,M_max,H)';
M1=[M_min M_max];
[n,m]=size(M1);


for i=1:n 
    M6 = linspace(M1(i,1),M1(i,end),10);
    M5(i,:)=M6;
end

[Drive,w]=DriveParameters(M5,H);
% [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V] = AllCalculations(mah,height);
% [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w);
% K_v
% K_wz
% Ya_Alpha

[n,m]=size(M5);
for i=1:n
    for j=1:m
    [W_raz,K_v(i,j),K_wz(i,j),K_H,i_p,i_H]=Synthesis_of_ACS(M5(i,j),H(i),w);
    end
end
% K_v
% K_wz
% W=feedback(W_raz,1);


