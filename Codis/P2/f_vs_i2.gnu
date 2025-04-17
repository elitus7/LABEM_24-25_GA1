set terminal pngcairo size 1500,1080 enhanced font 'Cambria,20'
set output 'f_vs_i2.png'
set xlabel "I^{2} (A^{2})"
set ylabel "F (N)"
set grid

set format y "%.4f"


f(x) = m*x + b
m = 0
b = 0

# Hacer ajuste (en modo silencioso)
fit f(x) 'f_vs_i2.dat' using 1:3 via m,b



plot 'f_vs_i2.dat' using 1:3:2:4 with xyerrorbars lc rgb "black" notitle, \
     'f_vs_i2.dat' using 1:3 with points pt 5 ps 1.5 lc rgb "black" notitle, \
     f(x) with lines lc rgb "red" lw 2 notitle


set output

