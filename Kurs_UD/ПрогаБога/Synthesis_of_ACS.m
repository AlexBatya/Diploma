function [W_raz,K_v,K_wz,K_H,i_p,i_H]=Synthesis_of_ACS(mah,height,w0_max)
    [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(mah,height);
    [Drive]= DriveParameters(mah,height);
    [A,B,C,D] = StateSpace(mah,height);
    diffura=ss(A,B,C,D);
    p=tf('s');

    
    e=0.25;
    K_wzGr=1/abs(0.02*Mz_deltaB);
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

    % while(~answer)
    %     W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz,-1);
    %     W_raz = 1/p*W_wzZAM*K_v;
    
    %     [w,ksi,a] = damp(W_raz);
    %     ksi=ksi(2);
    %     if(ksi<=0.6)
    %         nu=nu-0.025;
    %         K_v=nu*K_wz;
    %     end
    %     if(ksi>=1) 
    %         e=e-0.025;
    %         K_wz=e*K_wzGr;
    %     end
    %     if and(ksi<1,ksi>0.6) | ksi<0.6
    %         K_wz=e*K_wzGr;
    %         K_v=nu*K_wz;
    %         ksi
    %         answer=true;
    %     end
    % end

    i_H=0.8/(1/Ya_Alpha*V);
    W_wzZAM = feedback(tf(diffura(2))*Drive,K_wz,-1);
    W_v=feedback(W_wzZAM,1,-1);
    i_p=i_H^2*V;
    W_raz=W_v*K_H*(1/(1/Ya_Alpha*p+1))*(i_H+i_p*1/p);
end 