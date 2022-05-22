A=figure;
A.Position(3:4)=[1200,3000];
plot(t,zad);
title('Входной сигнал');
grid; 
xlabel('t, c');
ylabel('V_{y_{Зад}}, м/с');
saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/NotLinFig/Линейный ВС.jpg');

B=figure;
B.Position(3:4)=[1200,3000];
subplot(1,2,1);plot(t,delta*57.3);
title('Нелинейное отклонение элевонов');
grid; 
xlabel('t, c');
ylabel('\Delta\delta_{э}, град');
subplot(1,2,2);plot(t,deltaLin*57.3);
title('Линейное отклонение элевонов')
grid;
xlabel('t, c');
ylabel('\Delta\delta_{э}, град');
saveas(B,'ОтчётLatex/Оглавление/Part2/Sactions/Content/NotLinFig/Руль.jpg');

C=figure;
C.Position(3:4)=[1200,3000];
subplot(1,2,1);plot(t,wz*57.3);
title('Нелинейное изменение угловой скорости тангажа');
grid; 
xlabel('t, c');
ylabel('\Delta\omega_{z}, град/с');
subplot(1,2,2);plot(t,wzLin*57.3);
title('Линейное изменение угловой скорости тангажа')
grid;
xlabel('t, c');
ylabel('\Delta\omega_{z}, град/c');
saveas(C,'ОтчётLatex/Оглавление/Part2/Sactions/Content/NotLinFig/wz.jpg');

D=figure;
D.Position(3:4)=[1200,3000];
subplot(1,2,1);plot(t,vartheta*57.3);
title('Нелинейное изменение тангажа');
grid; 
xlabel('t, c');
ylabel('\Delta\vartheta, град');
subplot(1,2,2);plot(t,varthetaLin*57.3);
title('Линейное изменение тангажа')
grid;
xlabel('t, c');
ylabel('\Delta\vartheta, град');
saveas(D,'ОтчётLatex/Оглавление/Part2/Sactions/Content/NotLinFig/vartheta.jpg');

E=figure;
E.Position(3:4)=[1200,3000];
subplot(1,2,1);plot(t,Vy);
title('Нелинейное изменение вертикальной скорости');
grid; 
xlabel('t, c');
ylabel('\Delta V_y, м/с');
subplot(1,2,2);plot(t,VyLin);
title('Линейное изменение вертикальной скорости')
grid;
xlabel('t, c');
ylabel('\Delta V_y, м/с');
saveas(E,'ОтчётLatex/Оглавление/Part2/Sactions/Content/NotLinFig/Vy.jpg');

