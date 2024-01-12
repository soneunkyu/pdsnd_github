#hi
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#월 주 
def get_filters():
    """
    유다시티 프로젝트
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('도시를 입력하세요 (chicago, new york city, washington): ')
    while city.lower() not in CITY_DATA:
        city = input('도시를 입력하세요 (chicago, new york city, washington): ')
        if city.lower() not in CITY_DATA:
            print('유효하지 않은 도시입니다. 올바른 도시를 입력하세요.')

    month = input('월을 입력하세요 (all, January, February, March, April, May, June): ')
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('월을 입력하세요 (all, January, February, March, April, May, June): ')
        if month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('유효하지 않은 월입니다. 올바른 월을 입력하세요.')

    day = input('요일을 입력하세요 (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ')
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('요일을 입력하세요 (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ')
        if day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('유효하지 않은 요일입니다. 올바른 요일을 입력하세요.')

 
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
    
    # Convert user input city to lowercase
    city = city.lower()

    # Convert user input month to lowercase
    month = month.lower()
    
    # Convert user input day to lowercase
    day = day.lower()
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # TO DO: convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    # TO DO: filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # TO DO: filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

# 역
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month: {common_month}")

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(f"The most common day of week: {common_day_of_week}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#여행시간
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {common_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['Combination'].mode()[0]
    print(f"The most frequent combination of start and end station trip: {common_combination}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#시작시간
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#사용자 통계
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_type_counts)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender data not available in this dataset.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest birth year:", int(earliest_birth_year))
        print("Most recent birth year:", int(most_recent_birth_year))
        print("Most common birth year:", int(common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   #반복 
def display_raw_data(df):
    """Displays raw data to the user in groups of 5 rows at a time."""
    i = 1

    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            print(df[i:i+5])
            i = i+5
        else:
            break
# 메인함수
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes to continue: ')
        if restart.lower() not in ['yes', 'y'] :
            break


if __name__ == "__main__":
	main()
