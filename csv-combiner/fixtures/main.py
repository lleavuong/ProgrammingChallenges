import csv
import sys
import os

def merge_csv(files):
    title = []                              # array contains the titles - email_hash,category
    rows = []                               # array contains the rows
    for filename in files:
        # open and read file
        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)
            for row in csv_reader:
                rows.append(row + [os.path.basename(filename)])     # add file name to the array
    title =title + ["filename"]             # add filename title
    return title, rows

#if __name__ == "__main__":
title , rows = merge_csv(["accessories.csv","household_cleaners.csv"])  # test if can read file
filename = "merge.cvs"
#title, rows = merge_csv(sys.argv[1:])     # pass arguments
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    writer = csv.writer(csvfile)
    writer.writerow(title)
    writer.writerows(rows)