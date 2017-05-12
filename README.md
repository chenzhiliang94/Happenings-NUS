# Happenings-NUS
A bot to filter out emails of NUS students

User Stories
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
`* * *` | user | add a floating task | add tasks that need to be done 'some day'
`* * *` | user | add a task with deadlines | know when I must finish the task
`* * *` | user | view all the tasks by the order I added them | be more organised
`* * *` | user | delete a task | get rid of tasks I no longer want to track
`* * *` | user | check a task as done (not deleted) | know I have finished it
`* * *` | user | view a history of all the tasks I have done | check what I have done
`* * *` | new user | view the help guide | know the different commands there are and how to use them
`* * *` | user | edit my tasks | update them
`* * *` | user | undo my last command | undo mistakes/typos
`* * *` | user | add events that have a start and end time | know what my day will be like
`* * *` | user | search for tasks by deadline/description | see what task I entered
`* * *` | user | specify where to keep my tasks (file and folder) | move them around if need be
`* * *` | power user | set tags to tasks | group related tasks by tags
`* * *` | power user | search by tags | know everything I have to do related to that tag
`* *` | user | sort tasks by name, deadline, priority, start date or due date | quickly see what tasks I have to finish first
`* *` | user | list tasks | add deadlines to tasks without deadlines
`* *` | power user | use shortened versions of commands | save time when inputting tasks
`* *` | user | add different priorities to my tasks | know which tasks need to be done first
`* *` | user | list my tasks in priority order | see which tasks have different priorities
`* *` | user | undo multiple commands | revert changes
`* *` | user | enter recurring tasks | enter it just once
`* *` | power user | assign standard commands to my preferred shortcut commands | be familiar with my own  modified commands
`* *` | user | make tasks that have very close deadlines to appear as special priority | remember to complete them
`* *` | user | set notifications for deadlines for my tasks | be notified
`* *` | power user | set how much time it requires to finish a task | know how long I need to start and finish a task and not leave it halfway
`* *` | user | set tasks that are currently underway | be aware of the tasks I am working on
`* *` | user | redo my last action | reverse accidental undo commands
`*` | user | list the tasks that are due soon | meet my deadlines

<h5 align="center">Table 1: List of User Stories</h5>

<br><br>

## 8. Appendix B : Use Cases
<br>

___For all use cases below, the **System** is `ezDo` and the **Actor** is the `user`, unless otherwise specfied.___

<br>

### Use Case: Adding a Task
---


**MSS**

1. User enters command to add task along with relevant arguments.
2. ezDo adds the task and returns a confirmation message.
3. Use case ends.

<br>

**Extensions**

1a. The user enters an invalid command.

> 1a1. ezDo shows an error message and prompts the user to retry. <br>
  1a2. Use case resumes at step 1.

<br>







