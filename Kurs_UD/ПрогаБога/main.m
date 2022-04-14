clear
global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
load('Area_of_possible_flights.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
mass=180000;
Jz=7.7*10^6;
X_Tzv=0.46;

[A,B,C,D]=StateSpace(2,11000);
diffura=ss(A,B,C,D);
diffura.StateName = {'Alpha', 'wz', 'Vy'};
diffura.OutputName = {'Alpha', 'wz', 'Vy'};
diffura.inputname = {'deltaB'}; 

h_h=50;
H=Hob(1):h_h:Hob(end);

M_min=interp1(Hob,M_min',H)';
M_max=interp1(Hob,M_max,H)';
M1=[M_min M_max];
[n,m]=size(M1);


for i=1:n 
    M6 = linspace(M1(i,1),M1(i,end),1000);
    M5(i,:)=M6;
end
% [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V] = AllCalculations(M5,H);
% Mz_wz=max(Mz_wz);
% Mz_wz=max(Mz_wz);
% Mz_Alpha=max(Mz_Alpha);
% Mz_Alpha=max(Mz_Alpha);
% Ya_Alpha=max(Ya_Alpha);
% Ya_Alpha=max(Ya_Alpha);

[Drive,w]=DriveParameters(M5,H);

[W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(2,11000,w)
% W_zam=feedback(W_raz,1);


