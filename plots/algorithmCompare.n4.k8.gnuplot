prefix='algorithmCompare.n4.k8'
set grid

set title "Algorithm compare n=4, k=8"
set ylabel "Costs [min costs]" 
set yrange [0:2]
set xlabel "t [s]" 
plot \
        prefix.".clingo.dat" using 1:2 title 'clingo' with linespoints,\
        prefix.".genetic.dat" using 1:2 title 'genetic' with linespoints
set terminal pdfcairo
set output prefix.'.pdf'
replot

