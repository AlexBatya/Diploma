fileName = 'doubleAll.xlsx';

writematrix(K_H,fileName,'Sheet','K_H');
writematrix(i_H,fileName,'Sheet','i_H');
writematrix(i_p,fileName,'Sheet','i_p');
writematrix(K_v,fileName,'Sheet','K_v');
writematrix(K_wz,fileName,'Sheet','K_wz');
markers = ['o','v','^','<','>','.','*','+','x','p','P','X','O','V','|','h','H','_',"pentagram",'hexagram','square'];
A = figure;
for i = 1:length(H)
    plot(q(i,:),K_wz(i,:),marker=markers(i))
    hold on 
end
grid
legend('H = '+string(H)+' км')
ylabel('K_\omega_z, c')
xlabel('q, Н/м$^2')
saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/figures/K_wz.jpg')


A = figure;
for i = 1:length(H)
    plot(q(i,:),K_v(i,:),marker=markers(i))
    hold on 
end
grid
legend('H = '+string(H)+' км')
ylabel('K_\vartheta')
xlabel('q, Н/м^2')

saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/figures/K_v.jpg')
A = figure;
for i = 1:length(H)
    plot(q(i,:),K_H(i,:),marker=markers(i))
    hold on 
end
grid
legend('H = '+string(H)+' км')
ylabel('K_H, м/с')
xlabel('q, Н/м^2')

saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/figures/K_H.jpg')
A = figure;
for i = 1:length(H)
    plot(q(i,:),i_H(i,:),marker=markers(i))
    hold on 
end
grid
legend('H = '+string(H)+' км')
ylabel('i_H, 1/c')
xlabel('q, Н/м^2')

saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/figures/i_H.jpg')
A = figure;
for i = 1:length(H)
    plot(q(i,:),i_p(i,:),marker=markers(i))
    hold on 
end
grid
legend('H = '+string(H)+' км')
ylabel('i_p, 1/c')
xlabel('q, Н/м^2')

saveas(A,'ОтчётLatex/Оглавление/Part2/Sactions/Content/figures/i_p.jpg')


