function y=interpol2(x,y,matrix,x1,y1,method)
    [X,Y]=meshgrid(x,y);
    [X1,Y1]=meshgrid(x1,y1);
    y=interp2(X,Y,matrix,X1,Y1,method);
end

