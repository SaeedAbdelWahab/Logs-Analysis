#!/usr/bin/python

import datetime
import psycopg2

DBNAME = 'news'


def get_popular_articles():
    """Returns which three articles have been accessed the most
    with their view counts"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = """
    select A.title, count (*) as num
    from articles A, log L
    where L.path like concat('/article/%', A.slug)
    group by A.title
    order by num desc
    limit 3;
    """
    c.execute(q)
    articles = c.fetchall()
    db.close()
    return articles


def get_popular_authors():
    """Returns the authors and their page views in descending order
     according to the page views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = """
    select A.name, sum(views.num) as total_views
    from authors A, articles Ar,
    (
      select A.title, count (*) as num
      from articles A, log L
      where L.path like concat('/article/%', A.slug)
      group by A.title
    ) as views
    where Ar.author = A.id
    and Ar.title = views.title
    group by A.name
    order by total_views desc;
    """
    c.execute(q)
    authors = c.fetchall()
    db.close()
    return authors


def get_errors_days():
    """Returns the days that got an errors with percentage higher
    than 1% when accessed by users and that percentage"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q = """
    select day, percentage
    from (
      select Total.day, ((Fail.req*1.0)/Total.req) as percentage
      from (
        select date_trunc('day', time) as day, count(*) as req
        from log
        where status like '%200%'
        group by day
        order by day
        ) as Total,
        (
        select date_trunc('day', time) as day, count(*) as req
        from log where status like '%404%'
        group by day
        order by day) as Fail
      where Total.day = Fail.day
      ) as result
    where percentage > 0.01;
    """
    c.execute(q)
    days = c.fetchall()
    db.close()
    return days


def print_results(articles, authors, days):
    print ("Top three articles and their views :")
    for i, result in enumerate(articles):
        print ("  "+str(i+1)+")"+" "+"\""+result[0]+"\""+" -- " +
               str(result[1])+" views")
    print ("\nAuthors and their views in descending order:")
    for i, result in enumerate(authors):
        print ("  "+str(i+1)+")"+" "+"\""+result[0]+"\""+" -- " +
               str(result[1])+" views")
    print ("\nDates with error percentages greater than 1%:")
    for i, result in enumerate(days):
        day = result[0].strftime('%B %d, %Y')
        percentage = str(round(result[1]*100, 1))
        print ("  "+str(i+1)+")"+" "+day+" -- "+percentage+"% errors")


articles = get_popular_articles()
authors = get_popular_authors()
days = get_errors_days()
print_results(articles, authors, days)
