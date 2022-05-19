function [W_raz,K_v,K_wz,K_H,Kp,Ki]=Synthesis_of_ACS(mah,height,w0_max)
    [Mz_wz, Mz_Alpha, Ya_Alpha Mz_deltaB V q sigma_n] = AllCalculations(mah,height);
    [Drive]= DriveParameters(mah,height);
    [A,B,C,D] = StateSpace(mah,height);
    diffura=ss(A,B,C,D);
    p=tf('s');

    
    e=0.25;
    K_wzGr=1/abs(Mz_deltaB)/0.15;
    nu=w0_max;
    K_wz=e*K_wzGr;
    K_v=nu*K_wz;
    K_H=V;
    stocks = 12;
    % answer = false; 
    % while(~answer)
    %     if(nu<=Ya_Alpha)
    %         nu=nu+0.01;
    %     else
    %         nu=nu-0.01;
    %     end
    %     if(abs(nu-Ya_Alpha)<=0.2)
    %         K_v=nu*K_wz;
    %         answer=true;
    %     end
    % end
    answer = false;
    while ~answer 
        Wwz_raz1 = Drive* tf(diffura(2)) * -K_wz;  
        [L,fi,wsr] = margin(Wwz_raz1);
        % abs(20*log10(L))
        if abs(20*log10(L)-stocks)<=0.1
            K_wz=e*K_wzGr;
            answer = true ;
        elseif abs(20*log10(L))> stocks
            e = e + 0.01;
            K_wz=e*K_wzGr;
        elseif abs(20*log10(L))< stocks
            e = e - 0.01;
            K_wz=e*K_wzGr;
        end
    end 
    Wwz_zam1 = feedback(Drive* tf(diffura(2)),-K_wz);
    answer = false;

    while(~answer)
        Wv_raz1 = Wwz_zam1* 1/p * -K_v;
        [L,fi,wsr] = margin(Wv_raz1);
        % abs(20*log10(L))
        if(abs(20*log10(L))-stocks) <=0.1
            K_v=nu*K_wz;
            answer = true ; 
        elseif abs(20*log10(L))> stocks
            e = e + 0.01;
            K_v=e*K_wzGr;
        elseif abs(20*log10(L))< stocks
            e = e - 0.01;
            K_v=e*K_wzGr;
        end
    end 

    Wwz_zam1 = feedback(Drive* tf(diffura(2)),-K_wz);
    Wv_raz1 = Wwz_zam1* 1/p * -K_v;
    Wv_zam1 = feedback(Wv_raz1,1);
    W_raz = Wv_zam1 * K_H/(p/Ya_Alpha+1);

    [w2 a1 a2] = damp(W_raz);
    tau1=1/w2(2);
    tau2 = 1/w2(3);
    Ki = 0.2*1/(K_H*tau2);
    Kp = Ki * tau1;

    W_raz = Wv_zam1 * K_H/(p/Ya_Alpha+1) *(1/p*Ki+Kp);
end 