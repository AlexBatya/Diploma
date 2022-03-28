clear
%Исходные данные 
global M H Ps m Cxm Cym A Pn p P0 method Ha p1
H=0:2000:30000;

load('Data_Without_AfterburnerTRDF.mat');
% load('DataAfterburnerTRDF.mat');
load('Aerodynamics.mat');
load('AtmosphereStandard.mat');

m=180000;
Ps=4905;
P0=0.4;

%Новые данные
hm=0.001;
hh=1000;
M1=M(1):hm:M(end);
H1=H(1):hh:H(end);
H2=string(H1);
method='spline';
[hn,hm]=size(H1);
[mn,mm]=size(M1);
p1=interpol(Ha,p,H1,method);

for i=1:hm
    F=@(M1) dP(M1,H1(i));
    df1=fzero(F,0.1);
    df2=fzero(F,0.9);
    Mmin(i)=df1;
    Mmax(i)=df2;
end

Mmin
Mmax

Pp1=Pp(M1,H1);
Pr1=Pr(M1,H1);

Print(M1,Pp1(6,:),M1,Pr1(6,:),'График потребных и располагаемых тяг H=5км',...
    'M','P')
hold on
plot(Mmin(6),Pp(Mmin(6),5000),'mo')
text(Mmin(6),0,'M_{min}')
hold on
plot(Mmax(6),Pp(Mmax(6),5000),'mo')
text(Mmax(6),0,'M_{max}')






