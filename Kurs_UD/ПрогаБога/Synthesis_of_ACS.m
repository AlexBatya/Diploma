function z=Synthesis_of_ACS(mah,height)
    [Mz_wz Mz_Alpha Ya_Alpha Mz_deltaB]=AllCalculations(mah,height);
    w=sqrt(-Mz_wz*Ya_Alpha-Mz_Alpha);
    Tn=0.05;
    nu=w;
    e=0.25;
    Kwz_gr=1/(Tn*Mz_wz)
end