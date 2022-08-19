# Example

This is a flask api that has just 2 route, [users]("/api/users") and [users/{id}]("/api/users/{id}").
To run this application locally, clone the repository to your local machine, you can do the following commands to set up the virtual environment and have the api running. At the directory do the following: (P.S, you have to have python installed on your local machine already, if you do not, you can go to [python](https://python.org/downloads) on how to do that)

```terminal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Then finally to run the api
python app.py
```

You will be able to view the app on [localhost]("http://localhost/v1")

To load the [data](./data.csv), just go to [localhost/load]("http://localhost/v1/load") and the user data automatically get added to the database, note: this is only possible when the database is empty, if you have already added users to the database, this will not work.

That should get the api up and running. The api uses a mysql database system for data storage (so do not be scared when a sites.db file show up on your system, it is not a bug).
