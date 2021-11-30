# DataBase MongoDB Atlas communication tool for laser market competitors info storaging

This is the second part of **5-stage project**, connected with scoring the companies in laser industry.

Other parts of project:
- https://github.com/jularina/CompetitorsAmpl1
- https://github.com/jularina/CompetitorsAmpl3
- https://github.com/jularina/CompetitorsAmpl4
- https://github.com/jularina/CompetitorsAmpl5

Here the main accent is on storaging the parsed data of laser competitors to DataBase MongoDB Atlas, using MongoEngine.

The database itself consists of two defined collections that store information about competitors:

- Competitors - a collection containing the main characteristics of each competitor.
- CompetitorsCustomers - a collection where each competitor is compared with textual data about his activities from web resources, including social networks. 
This information has been moved to a separate scheme, since the results of the NLP models are added to it and a separate call is made to it using a special script.
It is shown in part 3 (https://github.com/jularina/CompetitorsAmpl3).
