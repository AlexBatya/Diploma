function z = P_RASP(mm,h)
    global m g P_0 p11 P1 H1 M1 p1 H
    lk=find(H==h)
    if h>=11000
        P_tilda=interp2(H1,M1,P1',11000,mm,'linear');
        z=P_tilda*m*g*P_0.*(p1(lk)/p11);
    else
        P_tilda=interp2(H1,M1,P1',h,mm,'linear');
        z=P_tilda*m*g*P_0;
    end
end