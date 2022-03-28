function y=interpol(M,C,m,method)
    y=interp1(M,C,m,method,'extrap');
end
