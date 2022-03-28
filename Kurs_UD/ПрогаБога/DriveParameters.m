function z = DriveParameters(mah,height)
    [Mz_wz, Mz_Alpha Ya_Alpha Mz_deltaB]=AllCalculations(mah,height);

    ksi=0.5;
    w=sqrt(-Mz_wz*Ya_Alpha-Mz_Alpha);
    p=tf('s');
    z=1/(p^2+2*ksi*w*p+w^2);

end