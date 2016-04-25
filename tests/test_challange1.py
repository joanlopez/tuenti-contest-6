from unittest import TestCase
from src.challange1.main import *


class TestChallange1(TestCase):
    def test_that_table_row_has_zero_tables_by_default(self):
        table_row = TableRow()
        self.assertEquals(0, table_row.num_tables)

    def test_that_when_add_table_row_has_one_more_table(self):
        table_row = TableRow()
        pre_num_tables = table_row.num_tables
        table_row.add_table()
        pos_num_tables = table_row.num_tables
        self.assertEquals(pre_num_tables+1, pos_num_tables)

    def test_that_first_table_added_is_an_isolated_table(self):
        table_row = TableRow()
        table_row.add_table()
        self.assertEquals(1, table_row.isolated_tables)

    def test_that_two_tables_are_always_one_sided(self):
        table_row = TableRow()
        table_row.add_table()
        table_row.add_table()
        self.assertEquals(2, table_row.one_sided_tables)

    def test_that_when_two_tables_then_the_next_ones_are_two_sided(self):
        table_row = TableRow()
        table_row.add_table()
        table_row.add_table()
        self.assertEquals(0, table_row.two_sided_tables)
        self.assertEquals(2, table_row.num_tables)
        table_row.add_table()
        self.assertEquals(1, table_row.two_sided_tables)
        table_row.add_table()
        self.assertEquals(2, table_row.two_sided_tables)

    def test_that_with_0_diners_then_the_needed_num_of_tables_is_0(self):
        self.assertEquals(0, count_needed_tables(0))

    def test_that_with_1_diner_then_the_needed_num_of_tables_is_1(self):
        self.assertEquals(1, count_needed_tables(1))

    def test_that_with_4_diners_then_the_needed_num_of_tables_is_1(self):
        self.assertEquals(1, count_needed_tables(4))

    def test_that_with_5_diners_then_the_needed_num_of_tables_is_2(self):
        self.assertEquals(2, count_needed_tables(5))

    def test_that_with_8_diners_then_the_needed_num_of_tables_is_3(self):
        self.assertEquals(3, count_needed_tables(8))

    def test_that_with_9_diners_then_the_needed_num_of_tables_is_4(self):
        self.assertEquals(4, count_needed_tables(9))