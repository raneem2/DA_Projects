import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS= ['january', 'february', 'march', 'april', 'may', 'june']
DAYS= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    flag=True
    city= input("Would you like to see data for chicago, new york city, or washington?").lower()
    if city in CITY_DATA:
        flag = False
    while (flag==True):   
        city= input("Error! Would you like to see data for chicago, new York, or washington?").lower()
        if city in CITY_DATA:
            flag = False
                       
    flag=True
    month= input("Which month? all, january, february, ... , june?").lower()
    if month in MONTHS:
        flag = False
    while (flag==True):   
        month= input("Error! Would you like to see data for all, january, february, ... , june?").lower()
        if month in MONTHS:
            flag = False

    flag=True
    day= input("Which day? Please type your prefered day (e.g., all, monday, tuesday, ... sunday)").lower()
    if day in DAYS:
        flag = False
    while (flag==True):   
        day= input("Error! Would you like to see data for all, monday, tuesday, ... sunday ").lower()
        if day in DAYS:
            flag = False

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
    df= pd.read_csv(CITY_DATA[city])
    view_data= input('\n Would you like to view 5 rows of individual trip data? Enter yes or no \n').lower()
    start_loc= 0
    while(view_data == 'yes'):
        print(df.iloc[start_loc: start_loc+5])
        start_loc+=5
        view_data=input('Do you wish to continue?: ').lower()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

  
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

     
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    most_common_month= df['month'].value_counts().idxmax()
    if(most_common_month == 1):
        most_common_month= "january"
    elif(most_common_month == 2):
        most_common_month= "february"
    elif(most_common_month == 3):
        most_common_month= "march"
    elif(most_common_month == 4):
        most_common_month= "april"
    elif(most_common_month == 5):
        most_common_month= "may"
    elif(most_common_month == 6):
        most_common_month= "june"
    print('most common month ', most_common_month)
    
    most_common_weekday= df['day_of_week'].value_counts().idxmax()
    print('most common day of week ', most_common_weekday)
    
    most_common_starthr= df['hour'].value_counts().idxmax()
    print('most common start hour ', most_common_starthr)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    most_common_start_station1= df['Start Station'].value_counts().idxmax()
    most_common_start_station2= df['Start Station'].value_counts().max()
    print('most commonly used start station {}     {}'.format(most_common_start_station1, most_common_start_station2))
    
    most_common_end_station1= df['End Station'].value_counts().idxmax()
    most_common_end_station2= df['End Station'].value_counts().max()
    print('most commonly combination of start station and end station trip {}     {}'.format(most_common_end_station1, most_common_end_station2))
          
    most_freq_combination= df.groupby(['Start Station', 'End Station']).size().idxmax() 
    print('most frequent combination of start station and end station trip {}, {}'.format(most_freq_combination[0], most_freq_combination[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   
    total_travel_time= df['Trip Duration'].sum()
    print('display total travel time ', total_travel_time, 'seconds')
    
    mean_travel_time= df['Trip Duration'].mean()
    print('mean travel time ', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types= df["User Type"].value_counts()
    print('counts of user types', user_types)
    try:
          gender_count= df["Gender"].value_counts()
          print('counts of user types', gender_count)
    except:
          print('Oops! Gender is not available in the Washington dataset')
    
    try:
          earliest_birthyear= df['Birth Year'].min()
          print('earliest year of birth ', earliest_birthyear)
          most_recent_birthyear= df['Birth Year'].max()
          print('most recent year of birth ', most_recent_birthyear)
          most_common_birthyear= df['Birth Year'].value_counts().idxmax()
          print('most common year year of birth ', most_common_birthyear)
    except:
          print('Oops! Birth year is not available in the Washington dataset')
    
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
  
