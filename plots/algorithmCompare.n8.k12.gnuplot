n=8
k=12
prefix='algorithmCompare.n'.n.'.k'.k
set grid

set title 'Algorithm compare n='.n.', k='.k
set ylabel "Costs [min costs]" 
set yrange [0:2.5]
set xlabel "t [s]" 
plot \
        prefix.".clingo.dat" using 1:2 title 'clingo' with linespoints,\
        prefix.".genetic.dat" using 1:2 title 'genetic' with linespoints
set terminal pdfcairo
set output prefix.'.pdf'
replot

