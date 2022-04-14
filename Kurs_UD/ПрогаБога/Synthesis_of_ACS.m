function [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w0_max)
    [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V] = AllCalculations(mah,height);
    [Drive]= DriveParameters(mah,height);
    [A,B,C,D] = StateSpace(mah,height);
    diffura=ss(A,B,C,D);
    p=tf('s');

    
    e=0.25;
    K_wzGr=1/(0.01*Mz_deltaB);
    nu=w0_max;
    h=0.25;
    K_wz=e*K_wzGr;
    K_v=nu*K_wz;
    K_H=V;
    i_p=0.003;
    W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz);
    W_raz = 1/p*W_wzZAM*K_v;

    answer=false;
    while(~answer)
        W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz,-1);
        W_raz = 1/p*W_wzZAM*K_v;
    
        [w,ksi,a] = damp(W_raz);
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
            K_wz=e*K_wzGr;
            K_v=nu*K_wz;
            answer=true;
        end
    end
    i_H=0.8/(1/Ya_Alpha*V);

    Wwz_raz = 1/p*W_wzZAM*K_v;
    W_v=feedback(W_raz,1);
    W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz,-1);
    W_raz=W_v*K_H*(1/(1/Ya_Alpha*p+1))*(i_H+1/p*i_p);
    i_p=0.2*i_H^2*V;
end 