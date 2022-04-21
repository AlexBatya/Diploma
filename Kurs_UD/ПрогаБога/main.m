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

mah=0.7521;
height=12000;
number=10;
h_h=2000;


[A,B,C,D]=StateSpace(mah,height);
diffura=ss(A,B,C,D);
diffura.StateName = {'Alpha', 'wz', 'Vy'};
diffura.OutputName = {'Alpha', 'wz', 'Vy'};
diffura.inputname = {'deltaB'}; 

H=Hob(1):h_h:Hob(end);

p=tf('s');
M_min=interp1(Hob,M_min',H)';
M_max=interp1(Hob,M_max,H)';
M1=[M_min M_max];
[n,m]=size(M1);


for i=1:n 
    M6 = linspace(M1(i,1),M1(i,end),number);
    M5(i,:)=M6;
end



[Drive,w]=DriveParameters(M5,H);
[Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(mah,height);  

% [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w)
% Wwz_raz1 = Drive * tf(diffura(2))* -K_wz ;%с САУ
% Wwz_raz2 = Drive * tf(diffura(2)); %без САУ
% Wwz_zam1 = feedback(Drive* tf(diffura(2)),-K_wz);
% Wwz_zam2 = feedback(Drive* tf(diffura(2)),1);

% Wv_raz1 = Wwz_zam1* 1/p * -K_v;
% Wv_raz2 = Wwz_zam2 * 1/p;
% Wv_zam1 = feedback(Wv_raz1,1);
% Wv_zam2 = feedback(Wv_raz2,1);

% WVy_raz1 = Wv_zam1 * K_H/(p/Ya_Alpha+1) *(i_H+i_p/p);
% WVy_raz2 = Wv_zam2 *  K_H/(p/Ya_Alpha+1);
% WVy_zam1 = feedback(WVy_raz1,1);
% WVy_zam2 = feedback(WVy_raz2,1)

% figure
% subplot(1,3,1)
% bode(Wwz_zam1)
% title('Замкнутый контур стабилизации угловой скорости тангажа')
% grid

% subplot(1,3,2)
% bode(Wv_zam1)
% title('Замкнутый контур стабилизации тангажа')
% grid

% subplot(1,3,3)
% bode(WVy_zam1)
% title('Замкнутый контур стабилизации вертикальной скорости')
% grid

% figure
% subplot(1,2,1)
% margin(Wwz_raz1)
% legend('Разомкнутый контур стабилизации угловой скорости тангажа')
% grid

% subplot(1,2,2)
% margin(Wwz_raz2)
% legend('Разомкнутый контур стабилизации угловой скорости тангажа без САУ')
% grid

% figure
% subplot(1,2,1)
% margin(Wv_raz1)
% legend('Разомкнутый контур стабилизации тангажа')
% grid

% subplot(1,2,2)
% margin(Wv_raz2)
% legend('Разомкнутый контур стабилизации тангажа без САУ')
% grid

% figure
% subplot(1,2,1)
% margin(WVy_raz1)
% legend('Разомкнутый контур стабилизации вертикальной скорости')
% grid

% subplot(1,2,2)
% margin(WVy_raz2)
% legend('Разомкнутый контур стабилизации вертикальной скорости без САУ')
% grid


[n,m]=size(M5);
for i=1:n
    for j=1:m
    [W_raz,K_v(i,j),K_wz(i,j),K_H(i,j),i_p(i,j),i_H(i,j)]=Synthesis_of_ACS(M5(i,j),H(i),w);
    end
end

% MAX = table(M5);
% writetable(MAX,'Kurs_UD/ПрогаБога/python/Data/MAX.xlsx');
% Hint = table(H);
% writetable(Hint,'Kurs_UD/ПрогаБога/python/Data/H.xlsx');
% K_WZ = table(K_wz);
% writetable(K_WZ,'Kurs_UD/ПрогаБога/python/Data/K_wz.xlsx');
% K_V = table(K_v);
% writetable(K_V,'Kurs_UD/ПрогаБога/python/Data/K_v.xlsx');
% I_H = table(i_H);
% writetable(I_H,'Kurs_UD/ПрогаБога/python/Data/i_H.xlsx');
% I_P = table(i_p);
% writetable(I_P,'Kurs_UD/ПрогаБога/python/Data/i_p.xlsx');




