set terminal pngcairo size 1600,1000 enhanced font 'Cambria,22'
set output 'f_vs_sep.png'
set xlabel "1/r (m^{-1})"
set ylabel "F (N)"
set grid
set decimalsign ','

set format y "%.5f"
set key outside right top
set key box lw 1

f(x) = m*x + b
m = 1.0
b = 1.0


fit f(x) 'f_vs_sep.dat' using 1:3 via m,b



plot 'f_vs_sep.dat' using 1:3:2:4 with xyerrorbars lc rgb "black" notitle, \
     'f_vs_sep.dat' using 1:3 with points pt 5 ps 1.5 lc rgb "black" title "Punts experimentals", \
     f(x) with lines lc rgb "red" lw 2 title "Ajust lineal"


set output