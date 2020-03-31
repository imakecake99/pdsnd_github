import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("\nChoose your city by typing one of the following - chicago, new york city, washington: ")
        if city in ('chicago', 'new york city', 'washington'):
                break
        elif city not in ('chicago', 'new york city', 'washington'):
            print("\nOops! Please try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month  = input("\nChoose a month by typing one of the following - january, february, march, april, may, june, or type \'all\' to see unfiltered data: ")
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        elif month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("\nOops! Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nChoose a day of the week by typing the name in full, or type \'all\' to see unfiltered data: ")
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        elif day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("\nOops! Please try again.")

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display most common month
    popular_month = df['month'].mode()[0]
    # display most common day of week
    popular_day = df['day_of_week'].mode()[0]
    # display most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Popular Month:', popular_month)
    print('Most Popular Day:', popular_day)
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_station_start = df['Start Station'].mode()[0]
    # display most commonly used end station
    popular_station_end = df['End Station'].mode()[0]
    # display most frequent combination of start station and end station trip
    popular_station_combo = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Popular Start Station:', popular_station_start)
    print('Most Popular End Station:', popular_station_end)
    print('Most Popular Combo of Start & End Stations:', popular_station_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    # display mean travel time
    average_travel_time = sum(df['Trip Duration'])/df['Trip Duration'].count()
    print('Total Travel Time:', total_travel_time)
    print('Average Travel Time:', average_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # Display counts of gender
    while True:
        try:
            gender_types = df['Gender'].value_counts()
            break
        except KeyError:
            gender_types = 'data not available'
            break
    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest_birth_year = int(df['Birth Year'].min())
            most_recent_birth_year = int(df['Birth Year'].max())
            popular_birth_year = int(df['Birth Year'].mode()[0])
            break
        except KeyError:
            earliest_birth_year = 'data not available'
            most_recent_birth_year = 'data not available'
            popular_birth_year = 'data not available'
            break
    print('User Types:\n', user_types)
    print('\nGender Types:\n', gender_types)
    print('\nEarliest Year of Birth:', earliest_birth_year)
    print('Most Recent Year of Birth:', most_recent_birth_year)
    print('Most Popular Year of Birth:', popular_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
