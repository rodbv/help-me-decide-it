# Help Me Decide It!

![Unit Tests](https://github.com/rodbv/help-me-decide-it/actions/workflows/run_tests.yaml/badge.svg)

This application helps you decide which tasks to prioritize, based on [Eisenhower's Matrix](https://todoist.com/productivity-methods/eisenhower-matrix).

<img width="575" alt="einsehower-matrix" src="https://user-images.githubusercontent.com/882489/163001298-9cfd28db-375f-4864-a805-c5f0f42532d7.png">

## Using relative comparisons to come up with a general priority

A **Task** is one thing that we want to prioritize. In the diagram above, they would be the post-id cards.

To distribute the tasks on the quadrants, we must assign two values to them: their **Importance** and **Urgency**.

Since it's sometimes hard to assign these values independently, we will do a system in which we compare tasks two by two. For example, given a task `A` and task `B`, we will pick which one is the most important, and the most urgent (it may be the same task, or maybe one is more important but the other is more urgent).

<img width="1103" alt="comparison" src="https://user-images.githubusercontent.com/882489/163005222-609ca4c0-6633-4a2b-8840-276f49bb7ded.png">

Once these comparisons are done, which task will have an overall value of importance and urgency, which will allow us to place them in the quadrants as we see on the diagram.

## Generating a task list from the priority values

Having the tasks placed on the quadrant, we will use a distance function to transform a 2D diagram into a sorted list of tasks, which can be assigned to a backlog etc.

That is achieved by measuring the Euclidian distance of each task to the point of maximum urgency and importance (red dot on the diagram). Note in the diagram that by measuring these distances, we
came up with the task order of `E`, then `I`, then `F`

<img width="853" alt="prioritization" src="https://user-images.githubusercontent.com/882489/163001286-500f6ab2-ee4d-426c-a47e-e1e1de236714.png">
