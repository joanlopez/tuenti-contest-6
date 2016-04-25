#!/usr/bin/env python

from tablerow import *


def print_output_line(case, result):
    print("Case #" + str(case) + ": " + str(result))


def count_needed_tables(num_of_diners):
    table_row = TableRow()
    while table_row.max_diners < num_of_diners:
        table_row.add_table()
    return table_row.num_tables


def main():
    num_of_cases = int(raw_input())

    for i in range(num_of_cases):
        num_of_diners = int(raw_input())
        needed_tables = count_needed_tables(num_of_diners)
        print_output_line(i+1, needed_tables)

if __name__ == '__main__':
    main()
