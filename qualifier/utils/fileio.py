# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(output_path, qualifying_loans):
    # Set the output header
    header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
    # Use the csv library and `csv.writer` to write the header row
    # and each row of `loan.values()` from the `inexpensive_loans` list.
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for loan in qualifying_loans:
            csvwriter.writerow(loan.values())
