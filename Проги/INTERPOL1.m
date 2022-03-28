function y=INTERPOL1(M1, Cydop1,M)
for i=1:length(M)
    Cydop(i)=interp1(M1, Cydop1, M(i), 'linear', 'extrap');
end
y=Cydop;
end

