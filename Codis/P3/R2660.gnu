set terminal pngcairo size 1600,1000 enhanced font 'Cambria,22'
set output 'R2660.png'

set xlabel "Freqüència (Hz)"
set ylabel "Guany"
set grid
set samples 1000
set format y "%.1f"
set decimalsign ','

R = 2660
A = 2.2e-2
B = 1.5e-8
pi = 3.141592653589793
Y = (1 / (2 * pi)) * sqrt(1 / (A * B))
Z1 = 2860 
Z2 = 3391

g(x) = sqrt( R**2 / (R**2 + (A * x * 2 * pi - 1 / (B * x * 2 * pi))**2) )
set arrow from Y, graph 0 to Y, graph 1 nohead lc rgb "black" lw 2
set arrow from Z1, graph 0 to Z1, graph 1 nohead lc rgb "red" lw 2
set arrow from Z2, graph 0 to Z2, graph 1 nohead lc rgb "purple" lw 2

set xrange [0:25000]
set yrange [-0.1:1.1]
plot g(x) notitle lw 2 lc rgb "blue"