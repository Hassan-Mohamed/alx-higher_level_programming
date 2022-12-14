#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list, in reverse order
#
# (C) 2022 Hassan Mohamed, Nairobi, Kenya
# email haska0491434@gmail.com
# -----------------------------------------------------------


def multiple_returns(sentence):
    """
    Args:
        sentence: a string argument
    Returns:
        a tuple with the length of a string and its first character
    """

    str_len, first_char = len(sentence), sentence[0]
    return (str_len, first_char)
