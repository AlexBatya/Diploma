function y=fun(M)
    global m S g H Cydop1 M1;
    Cydop=interp1(M1, Cydop1, M, 'linear', 'extrap');
    P_H=atmosphere(H);
    q=0.7*P_H*M^2;
    Cy_gp=0.95*m*g/(q*S);
    y=Cy_gp-Cydop;
end

