function y=Pr(mah,height)
    global M H p P0 m method Pn p1
    [nh,mh]=size(H);
    [nm,mm]=size(M);
    Pnn=Pn;
    for i=1:mh
        if(H(i)>11000)
            Pnn=[Pnn; Pnn(end,:)];
        end
    end
    for i=1:mh
        for j=1:mm
            if(H(i)>11000)
                Pnn(i,j)=Pnn(i,j).*p1(i)./p(7);
            else
                Pnn(i,j)=Pnn(i,j);
            end
        end
    end
    Pn1=interpol2(M,H,Pnn,mah,height,method);
    y=P0*m*9.81*Pn1;
end