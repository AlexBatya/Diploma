function [W_drive,w] = DriveParameters(mah,height)
    [Mz_wz, Mz_Alpha Ya_Alpha Mz_deltaB]=AllCalculations(mah,height);

    ksi=0.5;
    w=sqrt(-Mz_wz.*Ya_Alpha-Mz_Alpha);
    
    w1=max(w);
    w=max(w1);

    w=w;

    p=tf('s');
    W_drive=1/(1/w^2*p^2+2*ksi*1/w*p+1);

end