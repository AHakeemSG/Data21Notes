import csv



with open("user_details.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  # will pass the csv file, delimiter will remove comma

    for row in csvreader:  # to print each row because it is in a list of lists
        print(row)
       # print(row[-1])  # to only access the last item of each list

    iterable_csv = iter(csvreader)  # to skip the first line
    next(iterable_csv)
    for row in iterable_csv:  # to print each row because it is in a list of lists
        print(row)


# Performing a simple ETL

# Extraction and Transform in one function

def transform_user_details(csv_name):  # want a transformation that only returns name and email
    with open("user_details.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        iterable_csv = iter(csv_name)
        next(iterable_csv)  # will give us the next row
        for row in iterable_csv:
            print(row[1], row[2], row[-1])  # this will return first name, last name and email



# Another solution

# Extraction
def extract_csv(csv_file: str, delim: str = ',') -> list:
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        csv_list = list(csv_reader)

        return csv_list


# Transformation


def transform_user_details2(csv_list: list) -> list:
    # we want to retrieve the first name, last name and email
    csv_list = list[1:]

    new_list = []
    for item in csv_list:
        new_list.append([item[x] for x in [1, 2, 4]])

    return new_list


csv_reader = extract_csv("user_details.csv")
names_and_email = transform_user_details2(csv_reader)
print(names_and_email)




# Third solution
def transform_user_details3(csv_file_name)
    new_user_data = []

    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data


# Saving the file function
def create_csv_file(old_user_details="user_details.csv", new_file_name="new_details.csv")
    new_user_details = transform_user_details3(old_user_details)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)


create_csv_file()