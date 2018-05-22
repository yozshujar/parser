#!/usr/bin/env python
# coding: utf8


log = {}
report1 = []
report = {}


def keyfunction(k):
    return report[k]


for string in open('access.log', 'r'):
    split_line = string.split()
    log = {
        split_line[0]: int(split_line[9])
    }
    report1.append(log)


for x in report1:
    for key, val in x.items():
        if key in report:
            report[key] += int(val)
        else:
            report[key] = int(val)


for key in sorted(report, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, report[key]))
