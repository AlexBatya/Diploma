function z= P_POT(mm,h)
    global a1 p1 H m k g S C_xm A M
    ll=find(H==h);
    lm=find(abs(M-mm)<0.0001);
    V=mm*a1(ll);
    Vkm=V*3.6;
    q=0.7.*p1(ll).*mm.^2;
    Cy=(k*m*g)./(q.*S);
    Cx=C_xm(lm)+A(lm).*(Cy).^2;
    K=Cy./Cx;
    z=(k*m*g)./K;
end