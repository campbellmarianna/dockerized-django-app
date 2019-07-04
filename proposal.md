# Workout App Proposal
This is a mobile app backend that will be modeled after the program StringLifts. The functionality of this app will keep track of your workout and the history of your workouts.

**Due Date:** Friday, July 5

## Schedule

A **daily outline** to assist in planning my sprint:

* **Thursday, 20**: Write API tests.
* **Friday, 21**: Continue writing API tests.
* **Sunday 23**: Implement API.
* **Monday 24**: Implement API.
* **Tuesday 25**: Implement API.
* **Wednesday 26**: Documentation and deployment.

Later Plan
- Implement Improve functionality of app to add checkbox for reps and add RESTful API Friday
- Finish up tests and Deploy Sunday
- Create README and integrate an open source API (already made workouts) Monday

### Project Notes:
- Rep (repetition) is one complete motion of an exercise
- A set is a group of consecutive repetitions
- For example, you can say, "I did two sets of ten reps on the chest press."
- One can create a (instance of a) workout for each day
- Django third party plugin

#### Research Materials
- https://stronglifts.com/
- https://www.dummies.com/health/exercise/weights/weight-training-how-many-reps-and-sets-to-do/

# More Notes
- How should I represent time
- How can I access reps in a set?
- set.
- workout.set.reps.count()
- to get one use id
- use unicode function
- have detail of workout
- What do you mean when you say no secrets exposed?
- dj-database-url
- addon Postgres
- python-dotenv
