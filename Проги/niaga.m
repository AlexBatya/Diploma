clc;
clear;
global m S g P_0 H p1 a1 k M A C_xm H1 M1 p1 p11 P1
q_ind=5*10^5;
V_ind=sqrt(2*q_ind/1.225)
m=180000;
Ps=4905;
g=9.81;
S=m*g/Ps;
P_0=0.4;
k=0.95;
CeOH=0.042;
method='linear';

H1=[0 3000 6000 9000 11000];
% load('DataAfterburnerTRDF.mat');
load('AtmosphereStandard.mat');
load('Aerodynamics.mat');
load('Data_Without_AfterburnerTRDF.mat');

M_H=0.03;
M_K=3;
h_m=0.001;
n_m=abs(M_H-M_K)/h_m+1;
for i=1:n_m
  M(i)=M_H; 
  M_H=M_H+h_m;  
end

H_H=0;
H_K=28000;
h_h=1000;
n_h=abs(H_H-H_K)/h_h+1;
for i=1:n_h
    H(i)=H_H;
    H_H=H_H+h_h;    
end

Cydop=INTERPOL1(M2, Cydop1,M);
% C_ym=INTERPOL1(M2,C_ym1,M);
C_xm=INTERPOL1(M2,C_xm1,M);
A=INTERPOL1(M2,A1,M);
p1=INTERPOL1(Ha, pa,H);
ro1=INTERPOL1(Ha, roa,H);
a1=INTERPOL1(Ha, aa,H);


[T11,a11,p11,ro11]=atmosisa(11000);


for j=1:length(H)
    a=a1(j);
    p=p1(j);
    ro=ro1(j); 
    % [T,a,p,ro]=atmosisa(H(j));
    M_maxq(j)=V_ind/(sqrt(ro/1.225)*a);
    for i=1:length(M)
        V(i,j)=M(i)*a;
        Vkm(i,j)=V(i,j)*3.6;
        q(i,j)=0.7*p*M(i)^2;
        Cy(i,j)=(k*m*g)/(q(i,j)*S);
        Cx(i,j)=C_xm(i)+A(i)*(Cy(i,j))^2;
        K(i,j)=Cy(i,j)/Cx(i,j);
        P_pot(i,j)=(k*m*g)/K(i,j);
        if H(j)>=11000
            P_tilda(i,j)=interp2(H1,M1,P1',11000,M(i),method);
            P_rasp(i,j)=P_tilda(i,j)*m*g*P_0*(p/p11);

        else
            P_tilda(i,j)=interp2(H1,M1,P1',H(j),M(i),method);
            P_rasp(i,j)=P_tilda(i,j)*m*g*P_0;
        end
        R(i,j)=P_pot(i,j)/P_rasp(i,j);
        if H(j)==11000
            Ce_isk(i,j)=interp2(H1,M1,Ce1',11000,M(i),method);
            Cedros(i,j)=interp1(R1, Cedros1, R(i,j), method, 'extrap');
            CE(i,j)=0.1*Ce_isk(i,j)*Cedros(i,j);
            CE11(i)=CE(i,j);
        end
        
        if H(j)>=11000
            CE(i,j)=CE11(i);

        else
            Ce_isk(i,j)=interp2(H1,M1,Ce1',H(j),M(i),method);
            Cedros(i,j)=interp1(R1, Cedros1, R(i,j), method, 'extrap');
            CE(i,j)=0.1*Ce_isk(i,j)*Cedros(i,j);
        end   
        nx(i,j)=(P_rasp(i,j)-P_pot(i,j))/(k*m*g);
        Vy(i,j)=nx(i,j)*V(i,j);
% %         if Vy(i,j)<0
% %             Vy(i,j)=0;
% %         end
        q_chas(i,j)=CE(i,j)*P_pot(i,j);
        q_km(i,j)=q_chas(i,j)/(3.6*V(i,j));
    end
end



Vy_max=max(Vy',[],2);
M_maxq;

QKM_min=min(q_km',[],2)
QCHAS_min=min(q_chas',[],2)
% P_potmin=min(P_pot',[],2);


% M_Vy=MAXI(Vy,Vy_max,M);
% M_QKM=MAXI(q_km,QKM_min,M);
% M_QCHAS=MAXI(q_chas,QCHAS_min,M);
% M_P_pot=MAXI(P_pot,P_potmin,M);


% 
% 
% figure
% plot(Vy_max,H)
% grid minor
% figure
% plot(QKM_min,H)
% grid minor
% figure
% plot(QCHAS_min,H)
% grid minor
% 
% 
% for i=1:length(H)
%     H=[0 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 11000];
%     H=H(i);
%     if H == 911
%     break
%     end
%     M_minP(i)=fzero(@fn,0.4);
%     MmaxP(i)=fzero(@fn,0.8);
%     Cy_min(i)=fzero(@fun,0.4);
% end
% % H=[0 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 11000];
% % M_DOP=[0.85 0.85 0.85 0.85 0.85 0.85 0.85 0.85 0.85 0.85 0.85 0.85];
% % plot(M_minP,H,MmaxP,H,Cy_min,H,M_DOP,H,M_maxq,H)
% % grid minor
%      

% l=1;
% H_string=string(H);
% for i=1:length(H)
%     figure
%     % legend(H_string)
%     plot(M,Cy(:,i),M,Cydop)
%     grid minor
% end
% figure
% plot(M,Cydop,M,Cy(:,l))
% grid minor
% figure
% plot(M,Vy(:,l))
% grid minor
% figure
% plot(M,q_chas(:,l))
% grid minor
% figure
% plot(M,q_km(:,l))
% grid minor


% for i=1:length(H)
%     xlswrite('1.xlsx',[M',V(:,i),Vkm(:,i),q(:,i),Cydop',Cy(:,i),K(:,i),P_pot(:,i),P_rasp(:,i),nx(:,i),Vy(:,i),R(:,i),q_chas(:,i),q_km(:,i)],i);  
% end

% xlswrite('2.xlsx',[H',M_minP',MmaxP',Cy_min',M_DOP',M_maxq']);

% xlswrite('3.xlsx',[H',Vy_max,QKM_min,QCHAS_min,P_potmin]);

% xlswrite('4.xlsx',[H',M_Vy',M_QKM',M_QCHAS',M_P_pot'])













