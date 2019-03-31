#####################################################################
#
#   Programming for Data Science #3 - March 26th by JF Belisle
#
#####################################################################


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' } # Load city data

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june'] # Create a variable to store months of the year available, including the "all" option

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] # Create a variable to store days of week, including the "all" option


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_temp = ''
    while city_temp.lower() not in CITY_DATA:
        city_temp = str(input('For which city would you like to see data? Chicago, New York, or Washington?\n').lower())      
        if city_temp.lower() in CITY_DATA:
            city = city_temp
            break
        else:
            print('This city is not available.')
            continue
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_temp = ''
    while month_temp.lower() not in MONTH_DATA:
        month_temp = input('For which month would you like to see the data?\nPlease enter any month from January to June or enter all to see data for all the months available\n')
        if month_temp.lower() in MONTH_DATA:
            month = month_temp.lower()
        else:
            print('This month is not available.') # Error message

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_temp = ''
    while day_temp.lower() not in DAY_DATA:
        day_temp = input ('For which day of the week would you like to see the data?\nPlease enter any day from Monday to Sunday or enter all to see data for all the days\n')
        if day_temp.lower() in DAY_DATA:
            day = day_temp.lower()
        else:
            print('This day of the week does not exist.') # Error message
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load datafile into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of the week from Start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    #to filter by month when applicable
    if month != 'all':
        month = MONTH_DATA.index(month)

    #filter by month to create a new DataFrame
        df = df[df['month'] == month]

    #filter by day of the week where applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is', MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is', common_start_hour)

    print("\nRunning this code took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most frequent combination of start and end station trip are', popular_trip)

    print("\nRunning this code took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is', mean_travel_time)

    print("\nRunning this code took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The number of subscribers and customers are:', user_types)
        
    # TO DO: Display counts of gender
    if 'Gender' in df: # perform gender related calculation
        gender = df['Gender'].value_counts()
        print('The number of males and females are:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df: # perform gender related calculation
        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth is', earliest_year)

        recent_year = df['Birth Year'].max()
        print('The most recent year of birth is', recent_year)

        common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is', common_year)

        print("\nRunning this code took %s seconds." % (time.time() - start_time))
        print('-'*40)


def display_data(df):
    while True:
        display = input("Do you want to view the first 5 records of raw data? Enter yes or no : ").lower()
        # display first 5 records
        if display == 'yes':
            current = 0     # current index
            counter = 5     # number of records to display
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df.iloc[current:counter, ])
            current += counter
            while current < df.shape[0]:
                add_records = input("Do you want to view 5 additional records of raw data? Enter yes or no : ").lower()
                if add_records == 'yes':
                    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                        print(df.iloc[current:current+counter, ])
                    current += counter
                elif add_records == 'no': 
                    break
                else: 
                    print('Invalid entry. Please Enter yes or no')
            break
        if display == 'no': 
            break
        print('Invalid entry. Please Enter yes or no.\n')
    
    
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


################################################################
# End of the program
################################################################