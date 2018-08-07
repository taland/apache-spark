"""
Connect to DB:
```
$ psql -h postgres -U postgres
```

Create new database:
```
> create database testdb;
> \c testdb
```

Create table containing random data:
```
> create table random_t as
    select s, md5(random()::text)
    from generate_Series(1,50000) s;
```
"""
from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ReadFromDb")\
        .getOrCreate()

    url = 'postgresql://postgres:5432/testdb?user=postgres'
    params = {
        "url": 'jdbc:%s' % url,
        "dbtable": "random_t",
    }

    df = spark.read.format('jdbc').options(**params).load()

    print("count: ", df.count())
    print("dtypes: ", df.dtypes)
