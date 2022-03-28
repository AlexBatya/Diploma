function Print(x,y,x1,y1,King_title,x_label,y_label)
    plot(x,y,x1,y1);  % функция Cx
    title(King_title)
    xlabel(x_label)
    ylabel(y_label)
    grid minor
end