#!/bin/bash


for db in 'database:db1' 'database2:db2' 'val:val'
do
    db=(${db/:/ })
    src=${db[0]}
    dst=${db[1]}
    echo $src '->' $dst
    cp -v "../../sources/thesis2/results/performance/$src/min/3/ALL/512/window_comparison-ALL.png" "${dst}_window_comparison-ALL.png"
    cp -v "../../sources/thesis2/results/timing_vs_performance/$src/ALL.png" "${dst}_t_vs_p-ALL.png"
done
