global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
load('Area_of_possible_flights.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
m=180000;
Jz=7.7*10^6;
X_Tzv=0.25;

% [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB] = AllCalculations(2.4,11000);
[A,B,C,D]=StateSpace(2,18000);
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

K_wz=-2;
K_v=2;

for i=1:n 
    M6 = linspace(M1(i,1),M1(i,end),1000);
    M5(i,:)=M6;
end

[Drive,w]=DriveParameters(M5,H);
[W_raz,K_v,K_wz]=Synthesis_of_ACS(2.4,18000,w)


