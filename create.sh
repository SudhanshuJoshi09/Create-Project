#!/usr/bin/env bash


function create_project() {
    cd 
    cd ./Documents/Development/
    dir=$1
    if [[ -d "$dir" ]]
    then
        echo "directory already exists!";
    else
        git init
        python3 create.py $dir
        git remote add origin git@github.com:SudhanshuJoshi09/$dir.git
    fi
}