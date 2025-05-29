set terminal pngcairo size 1600,1000 enhanced font 'Cambria,22'
set output 'lambda.png'

set ylabel "ln|V_C(t_{n}) - E|"
set xlabel "Temps (s)"
set grid
set decimalsign ','
set key right top
set key box lw 1
set format x "%.5f"
set format y "%.1f"
set xrange [0:0.00011]
f(x) = m*x + b
m = 0
b = 0

fit f(x) 'lambda.dat' using 3:1 via m,b

plot 'lambda.dat' using 3:1:2 with yerrorbars lc rgb "black" notitle, \
     'lambda.dat' using 3:1 with points pt 5 ps 1.5 lc rgb "black" title "Punts experimentals", \
     f(x) with lines lc rgb "red" lw 2 title "Ajust lineal"


set output

