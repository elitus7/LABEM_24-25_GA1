set terminal pngcairo size 1600,1000 enhanced font 'Cambria,22'
set output 'vc_vs_t.png'

set xlabel "Temps (s)"
set ylabel "V_C (V)"
set grid
set decimalsign ','
set yrange [-1:6]
set xrange [0:0.00012]
set format x "%.5f"
set key right top
set key box lw 1

plot 'vc_vs_t.dat' using 3:1 with points pt 7 ps 1.5 lc rgb "black" notitle, \
    2.1 with lines lc rgb "red" dt 2 title "V_C = 2,1 V"

