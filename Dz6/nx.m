function z=nx(x,y)
    global m
    [hn,hm]=size(y);
    [mn,mm]=size(x);
    n=dP(x,y)/(m*9.81);
    for i=1:hm
        for j=1:mm
            if(n(i,j)>0)
               n(i,j)=n(i,j);
            else
                n(i,j)=0;
            end
        end
    end
    z=n;
end