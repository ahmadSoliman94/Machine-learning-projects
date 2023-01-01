import pandas as pd
import os


# to remove duplicated header in csv file
def remove_repeating_header(filename, output):

    # Open the CSV file for writing
    in_file = open(filename, 'r')
    out_file = open(output, 'w')

    # create new list to store the rows 
    rows = []

    # Iterate through the values in the row
    for row in in_file:

        ''' to see if the row is ready in row list. 
        Is not add it to the list (rows) '''
        if row in rows:
            continue
        else:
            rows.append(row)
            out_file.write(row)
    out_file.close()
    in_file.close()
    return output


# to fill the values after remove duplicated header
def fill_missing_values(data_frame, out_put):

    # open the new csv_file that was created and store it into a variable
    df = pd.read_csv(data_frame)

    # to remove the new csv_file
    os.remove(data_frame)

    # Iterate through the columns 
    for col in df:
        # select only integer or float dtypes
        if df[col].dtype in ("int", "float"):

            # filling the missing values using median
            df[col] = df[col].fillna(df[col].median())

    # to save the cleaned data
    df.to_csv(out_put, index=False)

 
def main():
    df = remove_repeating_header("./data.csv", "./new_data.csv")
    fill_missing_values(df, './cleaned_data.csv')


if __name__ == '__main__':
    main()
    
