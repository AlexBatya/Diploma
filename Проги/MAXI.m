function y=MAXI(Vy,Vy_max,M)
global H 
for j=1:length(H)
    for i=1:length(M)
        if Vy(i,j)==Vy_max(j)
           M_max(j)=M(i);
        end
            
    end
end
y=M_max;
end