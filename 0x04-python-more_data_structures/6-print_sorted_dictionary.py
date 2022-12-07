#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print a dictionary by ordered keys
#
# (C) 2022 Hassan Mohamed, Nairobi, Kenya
# email haska0491434@gmail.com
# -----------------------------------------------------------


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:s}: {}".format(key, a_dictionary[key]))
