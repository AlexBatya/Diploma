load('polyara.mat')
CyAll = [Cy_alpha07;Cy_alpha22;Cy_alpha15];
CyAlpha = [alpha07;alpha22;alpha15];
CyCx = [Cy07;Cy22;Cy15];
CxAll = [Cx07;Cx22;Cx15];
markers = ['o','^','x'];
subplot(1,2,1)
for i = 1:3 %Cy(alpha)
    plot(CyAlpha(i,:),CyAll(i,:),marker = markers(i))
    hold on 
end
legend('1','2','3')
xlabel('\alpha ,рад');
ylabel('C_y(\alpha)');
grid
subplot(1,2,2)
for i = 1:3 %Поляры
    plot(CxAll(i,:),CyCx(i,:),marker = markers(i))
    hold on 
end
legend('1','2','3')
grid
xlabel( 'C_y');
ylabel('C_x')