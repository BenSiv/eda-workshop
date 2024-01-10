"""
generates synthetic data for exploration
"""

import os
import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Person:
    def __init__(self, salary_mean, salary_std, expenses_range, expense_probability, salary_date, major_expenses):
        self.salary_mean = salary_mean
        self.salary_std = salary_std
        self.expenses_range = expenses_range
        self.expense_probability = expense_probability
        self.salary_date = salary_date
        self.major_expenses = major_expenses

    def get_person(self):
        # Randomize values for a person
        salary = max(round(np.random.normal(self.salary_mean, self.salary_std), 2), 0)
        expenses = round(random.uniform(*self.expenses_range), 2)
        return salary, expenses


def generate_month(person, initial_balance, month_start):
    data = []
    current_date = month_start
    current_balance = initial_balance

    while current_date.month == month_start.month:
        salary, expenses = person.get_person()

        # Major expenses on specified dates
        if current_date.day in person.major_expenses:
            expenses += person.major_expenses[current_date.day]

        transaction_in = salary
        transaction_out = expenses

        current_balance = round(current_balance + transaction_in - transaction_out, 2)

        data.append([current_date.strftime("%Y-%m-%d"), transaction_in, transaction_out, current_balance])

        current_date += timedelta(days=1)

    columns = ["Date", "In", "Out", "Balance"]
    df = pd.DataFrame(data, columns=columns)

    return df

def generate_dataset(num_people, num_months, start_date):
    # Generate data for multiple people over several months
    combined_data = []

    for _ in range(num_people):
        person = Person(salary_mean=16000, salary_std=4000, expenses_range=(500, 3000),
                        expense_probability=0.4, salary_date=15, major_expenses={5: 2000, 20: 1500})

        initial_balance = 1000  # You can set the initial balance as needed

        for month in range(num_months):
            month_start = start_date + relativedelta(months=month)
            month_data = generate_month(person, initial_balance, month_start)
            combined_data.append(month_data)

    # Concatenate the individual month datasets
    df_combined = pd.concat(combined_data, ignore_index=True)

    return df_combined

start_date = datetime(2022, 1, 1)
synthetic_data_combined = generate_dataset(num_people=2, num_months=3, start_date=start_date)










def generate_single_sample(sample_id, sample_duration, start_date, initial_balance,
                            in_probability=0.03, out_probability=0.4):
    # Convert start_date to a datetime object
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Generate random data for a single sample
    data = []
    end_date = start_date + timedelta(days=sample_duration - 1)

    current_date = start_date
    current_balance = initial_balance

    while current_date <= end_date:
        if random.uniform(0, 1) < in_probability:
            transaction_in = max(round(np.random.normal(16000, 4000), 2), 0)
            transaction_out = 0
        elif random.uniform(0, 1) < out_probability:
            transaction_out = max(round(np.random.normal(300, 50), 2), 0)
            transaction_in = 0
        else:
            transaction_in = 0
            transaction_out = 0

        current_balance = round(current_balance + transaction_in - transaction_out, 2)
        data.append([sample_id, current_date.strftime("%Y-%m-%d"), transaction_in, transaction_out, current_balance])

        current_date += timedelta(days=1)

    columns = ["ID", "Date", "In", "Out", "Balance"]
    df = pd.DataFrame(data, columns=columns)

    return df

def generate_combined_dataset(num_samples, sample_duration, start_date, initial_balance,
                              in_probability=0.03, out_probability=0.4):
    # Generate individual sample datasets and combine them into one DataFrame
    combined_data = []
    for sample_id in range(1, num_samples + 1):
        single_sample = generate_single_sample(sample_id, sample_duration, start_date, initial_balance,
                                               in_probability, out_probability)
        combined_data.append(single_sample)

    # Concatenate the individual sample datasets
    df_combined = pd.concat(combined_data, ignore_index=True)

    return df_combined


def main():
    script_path = os.path.realpath(__file__)
    project_path = os.path.dirname(os.path.dirname(script_path))
    output_file = os.path.join(project_path, "data", "transactions.csv")
    # Example usage:
    synthetic_data_combined = generate_combined_dataset(num_samples=3, sample_duration=20, start_date="2022-01-01", initial_balance=1000)
    print(synthetic_data_combined)
    synthetic_data_combined.to_csv(output_file)

if __name__ == "__main__":
    main()