A=figure;
A.Position(3:4)=[2000,3000];
plot(t,zad);
title('Входной сигнал');
grid; 
xlabel('t, c');
ylabel('V_{y_{Зад}}, м/с');
saveas(A,'NotLin/Линейный ВС.jpg');

B=figure;
B.Position(3:4)=[2000,3000];
subplot(1,2,1);plot(t,deltaNotLin*57.3);
title('Нелинейное отклонение элевонов');
grid; 
xlabel('t, c');
ylabel('\Delta\delta_{э}, град');
subplot(1,2,2);plot(t,deltaLin*57.3);
title('Линейное отклонение элевонов')
grid;
xlabel('t, c');
ylabel('\Delta\delta_{э}, град');
saveas(B,'NotLin/Руль.jpg');

C=figure;
C.Position(3:4)=[2000,3000];
subplot(1,2,1);plot(t,wzNotLin*57.3);
title('Нелинейное изменение угловой скорости тангажа');
grid; 
xlabel('t, c');
ylabel('\Delta\omega_{z}, град/с');
subplot(1,2,2);plot(t,wzLin*57.3);
title('Линейное изменение угловой скорости тангажа')
grid;
xlabel('t, c');
ylabel('\Delta\omega_{z}, град/c');
saveas(C,'NotLin/wz.jpg');

D=figure;
D.Position(3:4)=[2000,3000];
subplot(1,2,1);plot(t,varthetaNotLin*57.3);
title('Нелинейное изменение тангажа');
grid; 
xlabel('t, c');
ylabel('\Delta\vartheta, град');
subplot(1,2,2);plot(t,varthetaLin*57.3);
title('Линейное изменение тангажа')
grid;
xlabel('t, c');
ylabel('\Delta\vartheta, град');
saveas(D,'NotLin/vartheta.jpg');

E=figure;
E.Position(3:4)=[2000,3000];
subplot(1,2,1);plot(t,VyNotLin);
title('Нелинейное изменение вертикальной скорости');
grid; 
xlabel('t, c');
ylabel('\Delta V_y, м/с');
subplot(1,2,2);plot(t,VyLin);
title('Линейное изменение вертикальной скорости')
grid;
xlabel('t, c');
ylabel('\Delta V_y, м/с');
saveas(E,'NotLin/Vy.jpg');

