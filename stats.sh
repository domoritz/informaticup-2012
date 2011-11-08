git log --shortstat --author "Dominik Moritz" --since "100 weeks ago" --until "0 week ago" | grep "files changed" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print "files changed", files, "lines inserted:", inserted, "lines deleted:", deleted}'