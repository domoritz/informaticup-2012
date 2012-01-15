k='12'
prefix='timesPerN.k'.k
set grid

set title "Times (k=".k.")"
set ylabel "t [s]" 
set xlabel "n" 
plot \
        prefix.".firstSolution.clingo.dat" using 1:2 title 'first solution (clingo)' with linespoints,\
        prefix.".firstSolution.genetic.dat" using 1:2 title 'first solution (genetic)' with linespoints,\
        prefix.".lastSolution.clingo.dat" using 1:2 title 'last (new) solution (clingo)' with linespoints,\
        prefix.".lastSolution.genetic.dat" using 1:2 title 'last (new) solution (genetic)' with linespoints
set terminal pdfcairo
set output prefix.'.pdf'
replot

