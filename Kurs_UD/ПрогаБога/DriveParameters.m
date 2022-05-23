function [W_drive,w,w0] = DriveParameters(mah,height)
    [Mz_wz, Mz_Alpha Ya_Alpha Mz_deltaB V q sigma_n]=AllCalculations(mah,height);

    ksi=0.5;
    w0=sqrt(-Mz_wz.*Ya_Alpha-Mz_Alpha);
    
    w1=max(w0);
    w=max(w1);
    
    % T=1/w;
    T=0.02;

    p=tf('s');
    W_drive=1/(T^2*p^2+2*ksi*T*p+1);

end