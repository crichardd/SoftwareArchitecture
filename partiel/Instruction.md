# TodoDone

## What do you need ?

```
I use  post-its on the wall in front of my desk but when I'm traveling 
I don't have my todo list with me any more. 
I would like to have something that allows me to manage my tasks
when I'm on my computer. 
Please note that I like simple things.
```

## What do you need ?
```
I need to be able to manage my todo list everywhere I travel (with my laptop), 
this means that I need to add a new item on my list, mark it done, remove it, 
and list my todos ordored by older to newer.
```

## Do you need to identify precisely one note?
```
No, I don't care. I just need to be able to mark done or delete an existing note
```

## Ok, you said "ordered by date", do you need to see the date
```
No really, just mark the amount of time elapsed since creation, that's just what matters
```

## Ok, that's clear but could you please give us some exemples of what you call "amount of time" ?
```
Yes I mean [22 min old], [3 days old], [1 month old]. That's what you need?
```

## Yes, I see exactly what you mean. Do you think the "old" is needed in this context ? do you want it before or after your todo ?

```
    Ah...yes, right. it doesn't make sense to repeat "old" each time as 
    it's the only date and it's clear in this context. Put it before the todo then. 
```

### Ok Thanks!

Let's recap our discussion with the customer and the whole team in a story(_only first spec is provided, deal with it ;)_)

My persona is *Roger*. Roger use to travel a lot and need to be able to manage it's taks everywhere on his computer in order to get things done (he could use command line apps)

```
As Roger
I want to see the list of my current tasks ordered by date descending
In oder to be able to manage them
```

```
Given It is the '20240310 23:52'
Given I created a note @'20200309 20:30' with 'test1' and
Given I created a note @'20200310 23:12' with 'test2'
When I list my todos
Then I see in the todos that order (from recent to older:

[01][ ] test1 (40 min)
[02][X] test2 (1 day)

```

```
Given I have 2 todos test1 and test2
When  I mark the test1 as done
Then. I see the list of todos with test1 marked done:

[01][X] test1 (40 min)
[02][X] test2 (1 day)
```

**Additional notes from the discussion:**
- all the commands are unique, i call my app with one command and it does one thing (it's not an interactive app)
- the pattern to call the app should be `myapp {command} {arguments}`
- you're free to choose the persistance but it should be simple and without needing any other software (i.e: it couldn't depend on a preinstalled db server in the system)



**Optional Features**:

```
As Roger
I want to export my current tasks in a text report
In oder share what I've done with my team
```

```
Given It is the '20240310 23:52'
Given I todos test1, test2 and test3
And  test2 and test3 are done
When I ask for a report (ex: myapp report done)
Then it should create markdown text file with this content:

# Report
## Tasks done:

- test2 (2024-03-09)
- test3 (2024-03-02)

```

---



## Tech note

* You should have every important piece tested to prove that the app is working without have to run manual tests
* You should use TDD to guide you in your design
* It's better to have a quality working product with a limited of working functionalities than a messy app full of features. 
* Remember that `simplicity is the ultimate sophistication`
