# Open help for the calendar module.
import calendar
help(calendar)
# a. Try the following:

import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)                   # What happens here? Calling the needed year

# b. Observe that the week starts on Monday. An adventurous CompSci student believes that it is better mental
# chunking to have his week start on Thursday, because then there are only two working days to the weekend,
# and every week has a break in the middle. Read the documentation for TextCalendar, and see how you can
# help him print a calendar that suits his needs.

import calendar
cal = calendar.TextCalendar(3)      # Week starting state is 3 - Thursday
cal.pryear(2012)


# c. Find a function to print just the month in which your birthday occurs this year.
print(calendar.month(2019, 2))

# d. Try this:
d = calendar.LocaleTextCalendar(6, "Spanish")
d.pryear(2012)
# Try a few other languages, including one that doesn’t work, and see what happens. It creates an error

# e. Experiment with calendar.isleap.
# What kind of a function is this? Ats.: Its a built in function.
# What does it expect as an argument? Ats.: years
# What does it return as a result? Ats.: Boolean value True or False
print(calendar.isleap(2020))
# Returns True if year is a leap year, otherwise False.

# Make detailed notes about what you learned from these exercises.

print(calendar.TextCalendar(2))
# You can find help documentation throo kite