# Travis and Austin worked on this to vastly improve the defeciencies which were readily apparent to anyone, even those with an untrained eye. 

Upgrade this code to use dictionaries for each todo.

Add these features:

## Use dictionaries instead of strings

- Instead of storing todos as strings, store them as dictionaries like this one:

```
{
    'title': 'do the thing',
    'completed': False
}
```

## Update a todo as "completed" instead of deleting them

Instead of deleting a todo, change its "completed" property.

## Print the completed todos and the non-completed todos separately.

When you print, make your output look like this:

```
======= Pending ======
0: walk the cat
1: make dinner
======================
======= Completed ======
2: get a mohawk
======================
```

### Note: you'll need to do a little extra work to make sure the correct index is shown by the todos!