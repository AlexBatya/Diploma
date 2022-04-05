function [W_raz,K_v,K_wz]=Synthesis_of_ACS(mah,height,w0_max)
    [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB] = AllCalculations(mah,height);
    [Drive]= DriveParameters(mah,height);
    [A,B,C,D] = StateSpace(mah,height);
    diffura=ss(A,B,C,D);
    p=tf('s');

    

    e=0.25;
    K_wzGr=1/(0.01*Mz_deltaB);
    nu=w0_max;
    K_wz=e*K_wzGr;
    K_v=nu*K_wz;
    
    answer=false;
    while(~answer)
        W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz);
        W_raz = 1/p*W_wzZAM*K_v;
        % W_vZAM = feedback(1/p*W_wzZAM*-K_v,1)
        [a,ksi,T] = damp(W_raz);
        ksi=ksi(2);
        if(ksi<=0.6)
            nu=nu-0.025;
            K_v=nu*K_wz;
        end
        if(ksi>=1) 
            e=e-0.025;
            K_wz=e*K_wzGr;
        end
        if and(ksi<1,ksi>0.6) | ksi<0.6
            ksi
            K_wz=e*K_wzGr;
            K_v=nu*K_wz;
            answer=true;
        end
        
        
    end

end