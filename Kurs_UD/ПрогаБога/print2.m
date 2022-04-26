function print2(PicthureName,W_withCAU,W_withoutCAU,leggend_withCAU,leggend_withoutCAU)
    A=figure;
    A.Position(3:4)=[3000,5000];
    subplot(1,2,1);
    margin(W_withCAU);
    legend(leggend_withCAU);
    grid;

    subplot(1,2,2);
    margin(W_withoutCAU);
    legend(leggend_withoutCAU);
    grid;

    saveas(A,PicthureName);
end