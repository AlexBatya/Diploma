clear
global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha 
% load('Area_of_possible_flights.mat');
% load('Area_of_possible_flights2.mat');
load('Area_of_possible_flights3.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');
S=360;
ba=14.5;
mass=180000;
Jz=7.7*10^6;
X_Tzv=0.25;

mah=1.0976;
height=0;
number=10;
h_h=1000;

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



[Drive,w,w0]=DriveParameters(M5,H);
[Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(M5,H);  
% [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(mah,height);  
% [W_raz,K_v,K_wz,K_H,Kp,Ki]=Synthesis_of_ACS(mah,height,w)
% W_zam = feedback(W_raz,1);
 
% Wwz_raz1 = Drive * tf(diffura(2))* -K_wz ;%с САУ
% Wwz_raz2 =- Drive * tf(diffura(2)); %без САУ
% Wwz_zam1 = feedback(Drive* tf(diffura(2)),-K_wz);
% Wwz_zam2 = feedback(Drive* tf(diffura(2)),-1);

% Wv_raz1 = Wwz_zam1* 1/p * -K_v;
% Wv_raz2 = Wwz_zam1 * -1/p;
% Wv_zam1 = feedback(Wv_raz1,1);
% Wv_zam2 = feedback(Wv_raz1,1);

% WVy_raz1 = Wv_zam1 * K_H/(p/Ya_Alpha+1) *(Kp+1/p*Ki);
% WVy_raz2 = Wv_zam2 *  K_H/(p/Ya_Alpha+1);
% WVy_zam1 = feedback(WVy_raz1,1);
% WVy_zam2 = feedback(WVy_raz2,1);
% _____________________________________________________________
% FreqName3qmax = 'ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/ZAM qMAX.jpg';
% FreqName3qmax = 'ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/ZAM qMIN.jpg';
% FreqName3qmax = 'ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/ZAM qKR.jpg';

% FreqName_Wwz_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Угловая скорость тангажа раз qMAX.jpg';
% FreqName_Wv_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/Тангаж раз qMAX.jpg';
% FreqName_WVy_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/Вертикальная скорость раз qMAX.jpg';

% FreqName_Wwz_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Угловая скорость тангажа раз qMIN.jpg';
% FreqName_Wv_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Тангаж раз qMIN.jpg';
% FreqName_WVy_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Вертикальная скорость раз qMIN.jpg';

% FreqName_Wwz_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Угловая скорость тангажа раз qKR.jpg';
% FreqName_Wv_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Тангаж раз qKR.jpg';
% FreqName_WVy_qmax='ОтчётLatex/Оглавление/Part2/Sactions/Content/frequencies/Вертикальная скорость раз qKR.jpg';
% %__________________________________________________________________________________________________________
% A=figure;
% A.Position(3:4)=[3000,5000];
% subplot(1,3,1);
% bode(Wwz_zam1);
% title('Замкнутый контур стабилизации угловой скорости тангажа');
% grid;

% subplot(1,3,2);
% bode(Wv_zam1);
% title('Замкнутый контур стабилизации тангажа')
% grid;

% subplot(1,3,3);
% bode(WVy_zam1);
% title('Замкнутый контур стабилизации вертикальной скорости')
% grid;
% saveas(A,FreqName3qmax);

% print2(FreqName_Wwz_qmax,Wwz_raz1,Wwz_raz2,'Разомкнутый контур стабилизации угловой скорости тангажа',...
% 'Разомкнутый контур стабилизации угловой скорости тангажа без САУ')

% print2(FreqName_Wv_qmax,Wv_raz1,Wv_raz2,'Разомкнутый контур стабилизации тангажа',...
% 'Разомкнутый контур стабилизации тангажа без САУ')

% print2(FreqName_WVy_qmax,WVy_raz1,WVy_raz2,'Разомкнутый контур стабилизации вертикальной скорости',...
% 'Разомкнутый контур стабилизации вертикальной скорости без САУ')



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




