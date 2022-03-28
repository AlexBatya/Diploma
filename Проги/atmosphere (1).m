function [P_dav,a]=atmosphere(H)
    global Ha pa aa
    P_dav=interp1(Ha,pa,H,'linear','extrap');
    a=interp1(Ha,aa,H,'linear','extrap');
end