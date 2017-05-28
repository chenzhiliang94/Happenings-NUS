# Happenings-NUS
## 1. About
Tired of reading through countless NUS emails only to find out that a fraction of them are actually useful to you? Behold **Happenings@NUS**! **Happenings@NUS** is a telegram bot that filters your NUS email so that you will be notified of the contents of emails without ever opening them! In short, **Happenings@NUS** reads your NUS email and conducts some Natural Language Processing to divide emails into a few subcategories - 'Recruitments', 'Talks', 'Workshops', 'Internship Opportunities' and 'Others'. Subseqeuntly, **Happenings@NUS** will summarise these emails and push an one-liner notification to your telegram account!
<br>
More remarkably, you can instruct **Happenings@NUS** to only notify you of a certain type of emails. For example, if I am only interested in workshops and talks, I can set up the bot to only send me email summaries of emails containing workshops and talks! Amazing!

## 2. User Stories
<br>

Table 1 describes the user stories relevant to Happenings@NUS.
<br>

> **Priorities:**
> * High (must have) - `* * *`
> * Medium (nice to have)  - `* *`
> * Low (unlikely to have) - `*`

<br>

Priority | As a ... | I want to ... | So that I can...
-------- | :-------- | :--------- | :-----------
`* * *` | new user | view the help guide | know the functionalities of Happenings@NUS and how to use them
`* * *` | user | view the summary of NUS emails related to events, recruitment and internships to my inbox | only open emails which I'm interested in
`* * *` | user | filter the bot to only inform me of a certain category of emails | be informed of types of email that I am currently interested in
`* * ` | power user | add events to my calendar through the bot | mark them as events of interest
`* * ` | power user | search for events through the bot | find certain events

<h5 align="center">Table 1: List of User Stories</h5>

<br><br>

## 3. Use Cases
<br>

___For all use cases below, the **System** is `Happenings@NUS` and the **Actor** is the `user`, unless otherwise specfied.___

<br>

### 3.1 Use Case 1: Initialising Happenings@NUS
---

**MSS**

1. User enters /start
2. HappeningsBot gives a brief summary of the bot's functions and commands 
3. HappeningsBot provides a url link for user to grant the bot access to his/her account 
4. User enters his/her NUS email and password
5. HappeningsBot asks for user's interest in specific categories of emails(Events, recruitment, internships)
6. User chooses one or more types of emails choice
7. Use case ends

**Extensions**

1a. User enteres an invalid command
1b. The bot replies with an error message, followed by a list of correct available commands
3b. Use case ends

<br>

### 3.2 Use Case 2: Changing Categories
---

**MSS**
2. User enters /changeCategory
3. HappeningsBot reply with available choices of categories
4. User chooses caterogies of emails
5. HappeningsBot shows confirmation message
3. Use case ends

<br>

### 3.3 Use Case 3: Invalid Commands
---

**MSS**
1. User enteres an invalid command
2. The bot replies with an error message, followed by a list of available commands
3. Use case ends

<br>

### 3.4 Use Case 4: Hibernating the Bot
---

**MSS**
1. User enters /hibernate
2. HappeningsBot shows confirmation message of hibernation
3. Use case ends

### 3.5 Use Case 4: Resuming the Bot
---

**MSS**
1. User enters /resume
2. HappeningsBot shows confirmation message of resumation
3. Use case ends







