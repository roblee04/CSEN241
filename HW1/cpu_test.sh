# run sysbench 5 times

PRIME=20000
FILENAME=cpu_tests.txt
CSV=sysbench_cpu.csv
sysbench cpu --cpu-max-prime=$PRIME run > $FILENAME
sysbench cpu --cpu-max-prime=$PRIME run >> $FILENAME
sysbench cpu --cpu-max-prime=$PRIME run >> $FILENAME
sysbench cpu --cpu-max-prime=$PRIME run >> $FILENAME
sysbench cpu --cpu-max-prime=$PRIME run >> $FILENAME

# looking for avg
# cat $FILENAME | egrep " cat|total time:|total number of events:|deadlocks|read/write|min:|avg:|max:|percentile:" | tr -d "\n" | sed 's/total time: //g' | sed 's/total number of events: /\n/g' | sed 's/\[/\n/g' | sed 's/[A-Za-z\/]\{1,\}://g'| sed 's/ \.//g' | sed -e 's/read\/write//g' -e 's/approx\.  95/\n/g' -e 's/per sec.)//g' -e 's/ms//g' -e 's/(//g' -e 's/^.*cat //g' | sed 's/ \{1,\}/\t/g' > $CSV
cat $FILENAME | egrep " cat|threads:|total time:|total number of events:|read/write|min:|avg:|max:|percentile:" | tr -d "\n" | sed 's/Number of threads: /\n/g' | sed 's/total time: //g' | sed 's/[A-Za-z\/] //g' | sed 's/\[/\n/g' | sed 's/[A-Za-z\/]\{1,\}://g'| sed 's/ \.//g' | sed -e 's/read\/write//g' -e 's/approx\.  95//g' -e 's/per sec.)//g' -e 's/ms//g' -e 's/(//g' -e 's/^.*cat //g' | sed 's/ \{1,\}/\t/g' > $CSV

# calculate averages of averages
# Calculate the average of the second, third, and fifth columns
average_column_2=$(awk -F '[ \t]+' 'NR > 1 {sum += $2} END {print sum / (NR - 1)}' "$CSV")
average_column_3=$(awk -F '[ \t]+' 'NR > 1 {sum += $3} END {print sum / (NR - 1)}' "$CSV")
average_column_5=$(awk -F '[ \t]+' 'NR > 1 {sum += $5} END {print sum / (NR - 1)}' "$CSV")
std_dev_third_col=$(awk -F '[ \t]+' -v avg="$average_column_5" 'NR > 1 { sum += ($5 - avg)^2 } END { printf "%.2f", sqrt(sum/(NR - 1)) }' "$CSV")
# Find the min of the fourth column
min_column_4=$(awk -F '[ \t]+' 'NR > 1 && (NR == 2 || $4 < min) {min = $4} END {print min}' "$CSV")
# Find the max of the sixth column
max_column_6=$(awk -F '[ \t]+' 'NR > 1 && (NR == 2 || $6 > max) {max = $6} END {print max}' "$CSV")
# Display the results
echo "Average of the total time: $average_column_2"
echo "Average of the events: $average_column_3"
echo "Average of the average: $average_column_5"
echo "Standard deviation of average: $std_dev_third_col"
echo "global Minimum: $min_column_4"
echo "global Maximum: $max_column_6"
