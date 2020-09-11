# Swira-Design-Backend
Hello,
I made a REST microservice that gets the list of languages used by the most trending git repositories in the last 30 days from current day.

To do that, you'll need to call the following endpoint:

https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc

This api returns the 30 most trending repositories in the last 30 days.
Where changing the date with today's date.

Used Python technology.
