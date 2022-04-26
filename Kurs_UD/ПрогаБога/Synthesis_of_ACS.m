function [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w0_max)
    [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(mah,height);
    [Drive]= DriveParameters(mah,height);
    [A,B,C,D] = StateSpace(mah,height);
    diffura=ss(A,B,C,D);
    p=tf('s');

    
    e=0.25;
    K_wzGr=1/abs(Mz_deltaB)/0.025;
    nu=w0_max;
    K_wz=e*K_wzGr;
    K_v=nu*K_wz;
    K_H=V;

    answer=false;

    while(~answer)
        if(nu<=Ya_Alpha)
            nu=nu+0.01;
        else
            nu=nu-0.01;
        end
        if(abs(nu-Ya_Alpha)<=0.2)
            K_v=nu*K_wz;
            answer=true;
        end
    end

    Wwz_zam1 = feedback(Drive* tf(diffura(2)),-K_wz);
    Wv_raz1 = Wwz_zam1* 1/p * -K_v;
    Wv_zam1 = feedback(Wv_raz1,1);
    W_raz = Wv_zam1 * K_H/(p/Ya_Alpha+1);
    [w2 a1 a2] = damp(W_raz);
    T=1/w2(4);
    % i_H = 0.8/(1/Ya_Alpha*V);
    i_H=0.25/abs(T*V);
    i_p=0.15*i_H^2*V;
    W_raz = Wv_zam1 * K_H/(p/Ya_Alpha+1) *(i_H);
end 