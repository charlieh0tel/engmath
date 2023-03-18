#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABCY E-11 Tables."""

import io
import re

import pandas as pd


# Reference: ABYC E-11 2008


def _ColumnSortedValues(frame, column_regex=r"\D*(\d+)\D*"):
    values = set()
    for column in frame.columns:
        match = re.match(column_regex, column)
        values.add(int(match.group(1)))
    return sorted(values)


#
# TABLE VI – B - AC & DC CIRCUITS – ALLOWABLE AMPERAGE OF CONDUCTORS WHEN UP TO
# THREE CURRENT CARRYING CONDUCTORS ARE BUNDLED, SHEATHED OR IN CONDUIT
_TABLE_VI_B_CSV = """
awg,current_60C,current_60C_engroom,current_75C,current_75C_engroom,current_80C,current_80C_engroom,current_90C,current_90C_engroom,current_105C,current_105C_engroom,current_125C,current_125C_engroom,current_200C,current_200C_engroom
18,7.0,0,7.0,5.3,10.5,8.2,14.0,11.5,14.0,11.9,17.5,15.6,17.5
16,10.5,0,10.5,7.9,14.0,10.9,17.5,14.4,17.5,14.9,21.0,18.7,24.5
14,14.0,0,14.0,10.5,17.5,13.7,21.0,17.2,24.5,20.8,28.0,24.9,31.5
12,17.5,0,17.5,13.1,24.5,19.1,28.0,23.0,31.5,26.8,35.0,31.2,38.5
10,28.0,0,28.0,21.0,35.0,27.3,38.5,31.6,42.0,35.7,49.0,43.6,49.0
8,38.5,0,45.5,34.1,49.0,38.2,49.0,40.2,56.0,47.6,63.0,56.1,70.0
6,56.0,0,66.5,49.9,70.0,54.6,70.0,57.4,84.0,71.4,87.5,77.9,94.5
4,73.5,0,87.5,65.6,91.0,71.0,94.5,77.5,112.0,95.2,119.0,105.9,126.0
3,84.0,0,101.5,76.1,105.0,81.9,108.5,89.0,126.0,107.1,136.5,121.5,147.0
2,98.0,0,119.0,89.3,122.5,95.6,126.0,103.3,147.0,125.0,157.5,140.2,168.0
1,115.5,0,136.5,102.4,147.0,114.7,147.0,120.5,171.5,145.8,185.5,165.1,196.0
0,136.5,0,161.0,120.8,171.5,133.8,171.5,140.6,199.5,169.6,213.5,190.0,227.5
2/0,157.5,0,185.5,139.1,199.5,155.6,199.5,163.6,231.0,196.4,248.5,221.2,259.0
3/0,182.0,0,217.0,162.8,231.0,180.2,231.0,189.4,269.5,229.1,287.0,255.4,301.0
4/0,210.0,0,252.0,189.0,269.5,210.2,269.5,221.0,311.5,264.8,332.5,295.9,357.0
"""

TABLE_VI_B = pd.read_csv(io.StringIO(_TABLE_VI_B_CSV)).set_index("awg")
TABLE_VI_B_KNOWN_TEMPS_C = _ColumnSortedValues(TABLE_VI_B)


#
# TABLE IX – CONDUCTORS SIZED FOR 3 PERCENT DROP IN VOLTAGE
# Length of Conductor from Source of Current to Device and Back to Source

#
# 12 Volts - 3% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_12V_3PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,16,14,12,12,10,10,10,8,8,8,6,6,6,6,6,6,6,6
10,14,12,10,10,10,8,6,6,6,6,4,4,4,4,2,2,2,2,2
15,12,10,10,8,8,6,6,6,4,4,2,2,2,2,2,1,1,1,1
20,10,10,8,6,6,6,4,4,2,2,2,2,1,1,1,0,0,0,2/0
25,10,8,6,6,6,4,4,2,2,2,1,1,0,0,0,2/0,2/0,2/0,3/0
30,10,8,6,6,4,4,2,2,1,1,0,0,0,2/0,2/0,3/0,3/0,3/0,3/0
40,8,6,6,4,4,2,2,1,0,0,2/0,2/0,3/0,3/0,3/0,4/0,4/0,4/0,4/0
50,6,6,4,4,2,2,1,0,2/0,2/0,3/0,3/0,4/0,4/0,4/0
60,6,4,4,2,2,1,0,2/0,3/0,3/0,4/0,4/0,4/0
70,6,4,2,2,1,0,2/0,3/0,3/0,4/0,4/0
80,6,4,2,2,1,0,3/0,3/0,4/0,4/0
90,4,2,2,1,0,2/0,3/0,4/0,4/0
100,4,2,2,1,0,2/0,3/0,4/0
"""

TABLE_IX_12V_3PC = pd.read_csv(io.StringIO(_TABLE_IX_12V_3PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_12V_3PC)

#
# 24 Volts - 3% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_24V_3PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,18,18,16,16,14,12,12,12,10,10,10,10,10,8,8,8,8,8
10,18,16,14,12,12,10,10,10,8,8,8,6,6,6,6,6,6,6,6
15,16,14,12,12,10,10,8,8,6,6,6,6,6,4,4,4,4,4,2
20,14,12,10,10,10,8,6,6,6,6,4,4,4,4,2,2,2,2,2
25,12,12,10,10,8,6,6,6,4,4,4,4,2,2,2,2,2,2,1
30,12,10,10,8,8,6,6,4,4,4,2,2,2,2,2,1,1,1,1
40,10,10,8,6,6,6,4,4,2,2,2,2,1,1,1,0,0,0,2/0
50,10,8,6,6,6,4,4,2,2,2,1,1,0,0,0,2/0,2/0,2/0,3/0
60,10,8,6,6,4,4,2,2,1,1,0,0,0,2/0,2/0,3/0,3/0,3/0,3/0
70,8,6,6,4,4,2,2,1,1,0,0,2/0,2/0,3/0,3/0,3/0,3/0,4/0,4/0
80,8,6,6,4,4,2,2,1,0,0,2/0,2/0,3/0,3/0,3/0,4/0,4/0,4/0,4/0
90,8,6,4,4,2,2,1,0,0,2/0,2/0,3/0,3/0,4/0,4/0,4/0,4/0,4/0
100,6,6,4,4,2,2,1,0,2/0,2/0,3/0,3/0,4/0,4/0,4/0
"""

TABLE_IX_24V_3PC = pd.read_csv(io.StringIO(_TABLE_IX_24V_3PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_24V_3PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_24V_3PC)


#
# 32 Volts - 3% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_32V_3PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,18,18,18,16,16,14,14,12,12,12,12,10,10,10,10,10,10,8
10,18,16,16,14,14,12,12,10,10,10,8,8,8,8,8,6,6,6,6
15,16,14,14,12,12,10,10,8,8,8,6,6,6,6,6,6,6,4,4
20,16,14,12,12,10,10,8,8,6,6,6,6,6,4,4,4,4,4,2
25,14,12,12,10,10,8,8,6,6,6,6,4,4,4,4,2,2,2,2
30,14,12,10,10,8,8,6,6,6,4,4,4,4,2,2,2,1,1,1
40,12,10,10,8,8,6,6,4,4,4,2,2,2,2,2,1,1,1,1
50,12,10,8,8,6,6,4,4,2,2,2,2,2,1,1,0,0,0,0
60,10,8,8,6,6,4,4,2,2,2,2,1,1,0,0,0,2/0,2/0,2/0
70,10,8,6,6,6,4,2,2,2,1,1,0,0,0,2/0,2/0,2/0,3/0,3/0
80,10,8,6,6,4,4,2,2,1,1,0,0,0,2/0,2/0,3/0,3/0,3/0,3/0
90,8,6,6,6,4,2,2,2,1,0,0,2/0,2/0,2/0,3/0,3/0,3/0,4/0,4/0
100,8,6,6,4,4,2,2,1,0,0,2/0,2/0,2/0,3/0,3/0,3/0,4/0,4/0,4/0
"""

TABLE_IX_32V_3PC = pd.read_csv(io.StringIO(_TABLE_IX_32V_3PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_32V_3PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_32V_3PC)


#
# 12 Volts - 10% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_12V_10PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,18,18,18,18,16,16,14,14,14,12,12,12,12,12,10,10,10,10
10,18,18,16,16,14,14,12,12,10,10,10,10,8,8,8,8,8,8,6
15,18,16,14,14,12,12,10,10,8,8,8,8,8,6,6,6,6,6,6
20,16,14,14,12,12,10,10,8,8,8,6,6,6,6,6,6,4,4,4
25,16,14,12,12,10,10,8,8,6,6,6,6,6,4,4,4,4,4,2
30,14,12,12,10,10,8,8,6,6,6,6,4,4,4,4,2,2,2,2
40,14,12,10,10,8,8,6,6,6,4,4,4,2,2,2,2,2,2,2
50,12,10,10,8,8,6,6,4,4,4,2,2,2,2,2,1,1,1,1
60,12,10,8,8,6,6,4,4,2,2,2,2,2,1,1,1,0,0,0
70,10,8,8,6,6,6,4,2,2,2,2,1,1,1,0,0,0,2/0,2/0
80,10,8,8,6,6,4,4,2,2,2,1,1,0,0,0,2/0,2/0,2/0,2/0
90,10,8,6,6,6,4,2,2,2,1,1,0,0,0,2/0,2/0,2/0,3/0,3/0
100,10,8,6,6,4,4,2,2,1,1,0,0,0,2/0,2/0,2/0,3/0,3/0,3/0
"""

TABLE_IX_12V_10PC = pd.read_csv(io.StringIO(_TABLE_IX_12V_10PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_12V_10PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_12V_10PC)


#
# 24 Volts - 10% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_24V_10PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,18,18,18,18,18,18,18,16,16,16,16,14,14,14,14,14,14,12
0,18,18,18,18,18,16,16,14,14,14,12,12,12,12,12,10,10,10,10
15,18,18,18,16,16,14,14,12,12,12,10,10,10,10,10,8,8,8,8
20,18,18,16,16,14,14,12,12,10,10,10,10,8,8,8,8,8,8,6
25,18,16,16,14,14,12,12,10,10,10,8,8,8,8,8,6,6,6,6
30,18,16,14,14,12,12,10,10,8,8,8,8,8,6,6,6,6,6,6
40,16,14,14,12,12,10,10,8,8,8,6,6,6,6,6,6,4,4,4
50,16,14,12,12,10,10,8,8,6,6,6,6,6,4,4,4,4,4,2
60,14,12,12,10,10,8,8,6,6,6,6,4,4,4,4,2,2,2,2
70,14,12,10,10,8,8,6,6,6,6,4,4,4,2,2,2,2,2,2
80,14,12,10,10,8,8,6,6,6,4,4,4,2,2,2,2,2,2,2
90,12,10,10,8,8,6,6,6,4,4,4,2,2,2,2,2,2,1,1
100,12,10,10,8,8,6,6,4,4,4,2,2,2,2,2,1,1,1,1
"""

TABLE_IX_24V_10PC = pd.read_csv(io.StringIO(_TABLE_IX_24V_10PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_24V_10PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_24V_10PC)


#
# 32 Volts - 10% Drop Wire Sizes (gauge) - Based on Minimum CM Area
_TABLE_IX_32V_10PC_CSV = """
current_A,awg_10ft,awg_15ft,awg_20ft,awg_25ft,awg_30ft,awg_40ft,awg_50ft,awg_60ft,awg_70ft,awg_80ft,awg_90ft,awg_100ft,awg_110ft,awg_120ft,awg_130ft,awg_140ft,awg_150ft,awg_160ft,awg_170
5,18,18,18,18,18,18,18,18,18,18,18,16,16,16,16,14,14,14,14
10,18,18,18,18,18,18,16,16,14,14,14,14,14,12,12,12,12,12,12
15,18,18,18,18,18,16,14,14,14,12,12,12,12,10,10,10,10,10,10
20,18,18,18,16,16,14,14,12,12,12,10,10,10,10,10,8,8,8,8
25,18,18,16,16,14,14,12,12,10,10,10,10,10,8,8,8,8,8,8
30,18,18,16,14,14,12,12,10,10,10,10,8,8,8,8,8,6,6,6
40,18,16,14,14,12,12,10,10,8,8,8,8,8,6,6,6,6,6,6
50,16,14,14,12,12,10,10,8,8,8,6,6,6,6,6,6,6,4,4
60,16,14,12,12,10,10,8,8,8,6,6,6,6,6,6,4,4,4,4
70,14,14,12,10,10,8,8,8,6,6,6,6,6,4,4,4,4,2,2
80,14,12,12,10,10,8,8,6,6,6,6,4,4,4,4,2,2,2,2
90,14,12,10,10,10,8,6,6,6,6,4,4,4,4,2,2,2,2,2
100,14,12,10,10,8,8,6,6,6,4,4,4,4,2,2,2,2,2,2
"""

TABLE_IX_32V_10PC = pd.read_csv(io.StringIO(_TABLE_IX_32V_10PC_CSV)).set_index(
    "current_A"
)
TABLE_IX_32V_10PC_KNOWN_LENGTHS_FT = _ColumnSortedValues(TABLE_IX_32V_10PC)
