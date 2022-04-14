function [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V] = AllCalculations(mah,height)
    global aa mass pa S ba Jz mz_wz1 Cy_Alpha1 X_Tzv X_Fe1 X_T X_F1 Cy_AlphaE1 M11 Ha
    a=interp1(Ha,aa,height,'spline');
    p=interp1(Ha,pa,height,'spline');
    mz_wz=interp1(M11,mz_wz1,mah,'spline');    
    Cy_Alpha=interp1(M11,Cy_Alpha1,mah,'spline');    
    X_F=interp1(M11,X_F1,mah,'spline');
    X_Fe=interp1(M11,X_Fe1,mah,'spline');
    Cy_AlphaE=interp1(M11,Cy_AlphaE1,mah,'spline'); 


    q=0.7.*mah.^2.*p';
    V=mah.*a';
    mz_Wz=mz_wz.*ba./(mah.*a');
    mz_Alpha=(X_Tzv-X_F).*Cy_Alpha;
    mz_deltaB=(X_T-X_Fe).*Cy_AlphaE;
    Ya_Alpha=Cy_Alpha.*q.*S./(mah.*a'.*mass);
    Mz_wz=mz_Wz.*q.*S.*ba./Jz;
    Mz_Alpha=mz_Alpha.*q.*S.*ba./Jz;
    Mz_deltaB=mz_deltaB.*q.*S.*ba./Jz;
end