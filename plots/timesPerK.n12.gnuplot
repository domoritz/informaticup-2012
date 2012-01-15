n='12'
prefix='timesPerK.n'.n
set grid

set title "Times (n=".n.")"
set ylabel "t [s]" 
set xlabel "k" 
plot \
        prefix.".firstSolution.clingo.dat" using 1:2 title 'first solution (clingo)' with linespoints,\
        prefix.".firstSolution.genetic.dat" using 1:2 title 'first solution (genetic)' with linespoints,\
        prefix.".lastSolution.clingo.dat" using 1:2 title 'last (new) solution (clingo)' with linespoints,\
        prefix.".lastSolution.genetic.dat" using 1:2 title 'last (new) solution (genetic)' with linespoints
set terminal pdfcairo
set output prefix.'.pdf'
replot

