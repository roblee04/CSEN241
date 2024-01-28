# run sysbench 5 times

MEM=2G
FILENAME=mem_tests.txt
CSV=sysbench_mem.csv
sysbench memory --memory-block-size=$MEM run > $FILENAME
sysbench memory --memory-block-size=$MEM run >> $FILENAME
sysbench memory --memory-block-size=$MEM run >> $FILENAME
sysbench memory --memory-block-size=$MEM run >> $FILENAME
sysbench memory --memory-block-size=$MEM run >> $FILENAME

# looking for avg
cat $FILENAME | egrep " cat|threads:|transactions|deadlocks|read/write|min:|avg:|max:|percentile:" | tr -d "\n" | sed 's/Number of threads: /\n/g' | sed 's/\[/\n/g' | sed 's/[A-Za-z\/]\{1,\}://g'| sed 's/ \.//g' | sed -e 's/read\/write//g' -e 's/approx\.  95//g' -e 's/per sec.)//g' -e 's/ms//g' -e 's/(//g' -e 's/^.*cat //g' | sed 's/ \{1,\}/\t/g' > $CSV

# calculate averages of averages
awk -F'\t' 'NR > 1{
    sum2 += $2
    sum3 += $3
    sum4 += $4
    count++
} END {
    if (count > 0) {
        avg2 = sum2 / count
        avg3 = sum3 / count
        avg4 = sum4 / count
        printf "Average of Min: %.2f\n", avg2
        printf "Average of Avg: %.2f\n", avg3
        printf "Average of Max: %.2f\n", avg4
    }
    else {
        print "No data in the file."
    }
}' "$CSV"