"""Something with a Jupyter Notebook!"""
__author__ = "730471008"

import csv


def read_cvs_rows(filename: str) -> list[dict[str, str]]:
    """Return list of a two string dict!"""
    x: list[dict[str, str]] = []
    storage = open(filename, "r", encoding="utf8")
    read = csv.DictReader(storage)
    for row in read:
        x.append(row)
    storage.close()
    return x


def column_values(table: list[dict[str, str]], header: str) ->list[str]:
    """Return a table of values!"""
    x: list[str] = []
    for row in table:
        x.append(row[header])
    return x


def columnar(table: list [dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table into a dict of columns!"""
    x: dict[str, list[str]] = {}
    row1: dict[str, str] = table[0]
    for key in row1:
        x[key] = column_values(table, key)
    return x


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Make a new column-based table with only the first N rows!"""
    x: dict[str, list[str]] = {}
    if N >= len(table):
        x = table
        return x
    for key in table:
        empty: list[str] = table[key]
        N_storage: list[str] = []
        idx: int = 0
        while idx < N:
            N_storage.append(empty[idx])
            idx += 1
        x[key] = N_storage
    return x


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce new column-based talbe with subset!"""
    x: dict[str, list[str]] = {}
    for key in table:
        idx: int = 0
        while idx < len(column):
            if column[idx] == key:
                x[key] = table[key]
            idx += 1
    return x


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) ->dict[str, list[str]]:
    """Produce a talbe with combined values!"""
    together: dict[str, list[str]] = {}
    for key in table1:
        together[key] = []
        together[key] += table1[key]
    for key in table2:
        if key not in together:
            together[key] = []
            together[key] += table2[key]
        else:
            together[key] += table2[key]
    return together


def count(freq: list[str]) -> dict[str, int]:
    """Count the frequency of a number!"""
    x: dict[str, int] = {}
    for idx in x:
        if idx not in x:
            x[idx] = 1
        else:
            x[idx] += 1
    return x