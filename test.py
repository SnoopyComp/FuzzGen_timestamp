#!/usr/bin/env python3.11
# lines = ["#include <stream>", "precode 1;", "precode 2;", "int a = targetfunction(","int x1, int x2, int x3,", "double b1, double b2, double b3);", "some code1;", "some code2;"]
lines = ["#include <stream>", "precode 1;", "precode 2;", "int a = targetfunction(double b1, double b2, double b3);", "some code1;", "some code2;","int a = targetfunction(","int x1, int x2, int x3,", "double b1, double b2, double b3);","post code1;","post code 2;", "return 0;"]
lines = ["#include <stream>", "precode 1;", "precode 2;", "int a = targetfunction(double b1, double b2, double b3);","int a = targetfunction(","int x1, int x2, int x3,", "double b1, double b2, double b3);","post code1;","post code 2;", "return 0;"]

fs = "targetfunction"

i=0
while i < len(lines):
    # print(str(i) + "start: "+ lines[i])
    if fs in lines[i]:
        lines.insert(i, "function_start")
        i += 1
        while(1):
            # print(i)
            # print(lines[i])
            if ";" in lines[i].split('//')[0] :
                break
            i += 1

        lines.insert(i+1, "function_end1")
        i += 1
        lines.insert(i+1, "function_end2")
        i += 1
    i+=1
for i in range(len(lines)):
    print(lines[i])