## Current goal: an investigation into SQL work using Python

Currently, the best way (I found) to programatically generate SQL
with Python and retrieve the results as usable dataframes use 
pypika and pandas:


```
data = pd.read_sql(
    str(pypika.Query
            .from_("table1")
            .select('col1', 'col2')
            .limit(10)
        ),
    sql_con
)
```

Equivalent code in R's dbplyr:

``` 
data <- tbl(sql_con, "table1") %>% 
	select(col1, col2) %>% 
	limit(10) %>% 
	collect
```

TODO: add better examples

Pypika solution is less seamless, but it also seems that rough edges could 
be removed with just a little work. 

This is the current goal: implement all immediately obvious changes to move python's 
current best as close to R's current best. 

## Future goals
* Implement optional SQL result caching 
  - based on generated SQL
* Store table metadata locally
  - this allows to invalidate queries before sending them for execution
* Implement heterogenous data sources 
  - joining local data with remote is only possible by moving data either one way or 
	the other. This can be impossible for large tables, but feasible (even default) for 
	small. 
  
