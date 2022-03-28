global aa m pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
load('Area_of_possible_flights.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
m=180000;
Jz=7.7*10^6;
X_Tzv=0.25;

% [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB] = AllCalculations(0.5,5000)
[A,B,C,D]=StateSpace(2,18000);
diffura=ss(A,B,C,D);
diffura.StateName = {'Alpha', 'wz', 'Vy'};
diffura.OutputName = {'Alpha', 'wz', 'Vy'};
diffura.inputname = {'deltaB'}; 

[Mz_wz Mz_Alpha Ya_Alpha Mz_deltaB]=AllCalculations(0.3,1500);
Drive=DriveParameters(0.3,1500);




