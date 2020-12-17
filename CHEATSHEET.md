# Nornir Filtering Cheatsheet

## F filter operators

Below are the `F` filter operators:


Filter EQUALS `eq`
```
site = "site_a"
nr.filter(F(site_type__eq=site))
```

Filter NOT EQUALS
```
site = "site_a"
nr.filter(~F(site_type__eq=site))
```

Filter NOT EQUALS
```
site = "site_a"
nr.filter(~F(site_type__eq=site))
```

F()