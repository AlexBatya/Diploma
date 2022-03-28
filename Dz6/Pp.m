function y=Pp(mah,height)
    global M H Ps m Cxm Cym A p method Ha
    
    Cxm1=interpol(M,Cxm,mah,method);
    % Cym1=interpol(M,Cym,mah,method);
    A1=interpol(M,A,mah,method);
    p1=interpol(Ha,p,height,method);
    
    q=0.7.*p1'.*mah.^2;
    Cy=0.95*Ps./q;
    Cx=Cxm1+A1.*(Cy).^2;
    K=Cy./Cx;
    y=0.95*m*9.81./K;  
end