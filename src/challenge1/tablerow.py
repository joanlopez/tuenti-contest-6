#!/usr/bin/env python


class TableRow(object):
    def __init__(self):
        self.isolated_tables = 0
        self.one_sided_tables = 0
        self.two_sided_tables = 0

    def add_table(self):
        if self.one_sided_tables == 0:
            if self.isolated_tables == 0:
                self.isolated_tables += 1
            else:
                self.isolated_tables = 0
                self.one_sided_tables = 2
        elif self.one_sided_tables == 2:
            self.two_sided_tables += 1

    @property
    def max_diners(self):
        return (self.isolated_tables * 4) \
               + (self.one_sided_tables * 3) \
               + (self.two_sided_tables * 2)

    @property
    def num_tables(self):
        return self.isolated_tables \
               + self.one_sided_tables \
               + self.two_sided_tables
