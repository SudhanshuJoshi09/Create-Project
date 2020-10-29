#!/usr/bin/env bash


function create_project() {
    cd
    cd ./Documents/Development/
    dir=$1
    if [[ -d "$dir" ]]
    then
        echo "directory already exists!";
    else
        mkdir $dir
        cd $dir
        git init
        python3 ~/.bin/Create-Project/create.py "$dir"
        git remote add origin git@github.com:SudhanshuJoshi09/$dir.git
    fi
}