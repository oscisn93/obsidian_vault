# Product Requirements

## Purpose
The aim of this project is to provide an all-in-one web application with scheduling and task management capabilities to support deep focused work- specifically to support students in creating a customized, flexible study/work schedule and  stay ahead of tasks and deadlines, although the platform is most defintely open to other types of users who may also enjoy its features and capabilities.

## Features

#### Scheduler:

- Users will be able to schedule tasks on a calendar with several modes views including week, month and day view. Once a task is added it can be read,  completed, otherwise updated, or deleted. When a user clicks on a task/event a modal will appear to the side of the task ui component that will shoe the details of the task as well as the option to delete or update. Users must be signed in to add tasks to their calendars.

### Project Manager:

- Users will be able to Create long term projects composed of tasks that will break down larger goals into bite size. Tasks will initially be grouped into a "No Projects" project and can be moved into different projects once a user has created them. Any tasks created in the calendar component will automatically be reflected in the Projects component and vice versa. As with tasks, users will be able to create, read, update, and delete projects, and there are optional deadlines to set reminders in the calendar for critical points in the completion of a goal. Finally, if a project is delted the user will be asked if they would like to delete all its tasks or simply return them to the "No Projects" container.

### Focus Timer:

- Users will be able to see their upcoming tasks in the task list on a Focus page, as soon as they schedule them in their calendar. The focus page will also contain a pomodoro timer component that contains the first tasks, first focus timeblock. Tasks will be broken down into the standard 25 minutes on 5 minutes off "chunks" to the best approximation. Additionally users will be able to adjust the 'chunk' sizes via drag and drop functionality. Users can create and delete timeblocks and if all tiemblocks in a task are deleted, they will be given the option to delete the task or complete it.

