#!/bin/bash
echo -e "\033[44m --------------------------------------------------------------------------\e[0m"
echo -e "\033[44m make c++ snippets                                                         \e[0m"
echo -e "\033[44m --------------------------------------------------------------------------\e[0m"

rm -rf builds
mkdir builds

g++ template-eg1.cpp -std=c++11 -o builds/template-eg1
g++ template-eg2.cpp -std=c++14 -o builds/template-eg2
g++ template-eg3.cpp -std=c++14 -o builds/template-eg3

