function [A,B,C,D] = StateSpace(mah,height)
   global aa Ha
   [Mz_wz Mz_Alpha Ya_Alpha Mz_deltaB]=AllCalculations(mah,height);
   a=interp1(Ha,aa,height,'spline');
    
   A=[-Ya_Alpha 1 0;
      Mz_Alpha Mz_wz 0;
      mah*a*Ya_Alpha 0 0];
   B=[0;Mz_deltaB;0];
   C=[1 0 0; 0 1 0; 0 0 1];
   D=[0;0;0];


end