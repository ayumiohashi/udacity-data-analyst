import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Valid inputs
    valid_cities = {
        'chicago' : 1,
        'new york' : 1,
        'washington' : 1
    }
    valid_months = {
        'all' : 1,
        'january' : 1,
        'february' : 1,
        'march' : 1,
        'april' : 1,
        'may' : 1,
        'june' : 1
    }
    valid_days = {
        'all' : 1,
        'monday' : 1,
        'tuesday' : 1,
        'wednesday' : 1,
        'thursday' : 1,
        'friday' : 1,
        'saturday' : 1,
        'sunday' : 1,
    }

    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york, washington).
    input_str = 'Would you like to see data for Chicago, New York, or Washington?'
    city = validate_input(input_str, valid_cities)

    # get user input for month (all, january, february, ... , june)
    input_str = 'Which month? All, January, February, March, April, May, or June?'
    month = validate_input(input_str, valid_months)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    input_str = 'Which day? All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +\
                'Saturday, or Sunday?'
    day = validate_input(input_str, valid_days)

    print('-'*40)
    return city, month, day

def validate_input(input_str, valid_input_dict):
    """
    Validates user input and make sure it is valid input.

    Args:
        (str) input_str - Message displayed to ask for user input
        (dict) valid_input_dict - Dictionary of valid choices to validate
                                  against user input
    Returns:
        (str) user_input - user input
    """

    while True:
        user_input = input('\n'+ input_str +'\n')
        user_input = user_input.lower()
        # Check if the user input is a valid choice
        if (valid_input_dict.get(user_input)):
            break

        print('Please re-enter your choice.')

    return user_input

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        int_month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[(df['month'] == int_month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def get_most_common_idx_and_val(col):
    """
    Get the most common occurance of index an value

    Args:
        col - pandas DataFrame column
    Returns:
        (list) - list of index and value of the most occurance in the passed column
    """
    return [ col.value_counts().idxmax(), col.value_counts().max()]

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    num_to_month = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June'
    }

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = get_most_common_idx_and_val(df['month'])
    month[0] = num_to_month[month[0]] # index of month to corresponding string month

    # display the most common day of week
    dow = get_most_common_idx_and_val(df['day_of_week'])

    # find the most popular hour
    hour = get_most_common_idx_and_val(df['hour'])

    print(
        "The Most Common Frequent Times of Travel -\n"
        "    Month       : {0[0]}, count {0[1]}\n"
        "    Day of week : {1[0]}, count {1[1]}\n"
        "    Hour        : {2[0]}, count {2[1]}"
        .format(
            month, dow, hour
        )
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = get_most_common_idx_and_val(df['Start Station'])

    # display most commonly used end station
    end_station = get_most_common_idx_and_val(df['End Station'])

    # display most frequent combination of start station and end station trip
    combination = [
        df.groupby(['Start Station', 'End Station']).size().idxmax(),
        df.groupby(['Start Station', 'End Station']).size().max()
    ]

    print(
        "The Most Commonly Used Stations -\n"
        "    Start Station           : {0[0]}, count {0[1]}\n"
        "    End Station             : {1[0]}, count {1[1]}\n"
        "    Start/End Station Combo : {2[0][0]}/{2[0][1]}, count {2[1]}"
        .format(
            start_station, end_station, combination
        )
    )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = [df['Trip Duration'].sum(), df['Trip Duration'].count()]

    # display mean travel time
    average = df['Trip Duration'].mean()

    print(
        "Total Travel Time   : {0[0]}, count {0[1]}\n"
        "Average Travel Time : {1}"
        .format(
            total, average
        )
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User Type -")
    for type, count in user_type.iteritems():
        print("    {}, count {}".format(type, count))

    # Display counts of gender
    if 'Gender' in df.columns: # Doesn't exist in Washington file
        gender = df['Gender'].value_counts()
        print("\nGender -")
        for type, count in gender.iteritems():
            print("    {}, count {}".format(type, count))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: # Doesn't exist in Washington file
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = get_most_common_idx_and_val(df['Birth Year'])
        most_common[0] = int(most_common[0]) # casting to int to get rid of decimal point

        print(
            "\nYear of Birth -\n"
            "    Earliest    : {0}\n"
            "    Most Recent : {1}\n"
            "    Most Common : {2[0]}, count {2[1]}"
            .format(
                earliest, most_recent, most_common
            )
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays row trip data 5 at a time if requested by user."""

    count = 0
    while True:
        user_input = input('\nWould you like to see{}raw trip data? Enter yes or no.\n'.
            format(' more ' if count > 0 else ' ')
        )
        if user_input.lower() != 'yes':
            break

        # Display 5 rows at a time ([0:5], [5:10], [10:15]...)
        print(df[(count*5):(count+1)*5])
        count += 1

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
