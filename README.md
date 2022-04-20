# hushHush Recruiter &#8594; An automated recruiting solution

## Introduction

A fictional company called Doodle is looking to automate the recruting process of developers and wants an in-house solution to select the best candidates.

This repository presents a solution to Doodle's problem. 

Our application retrieves data about possible candidates from various sources _(see sources below)_ and classifies the candidates as selected for an interview or not. If a candidate is selected then an email is sent with a link to an interface with coding questions.

---

## How does our selection algorithm work?

We used a combination of unsupervised learning and supervised learning to train the model.

First we implemented clustering to classify our users into two distinct categories, selected for interview and not selected. Then we proceeded to train a supervised model using logistic regression that would predict if a user was selected or not based on the labeled created through clustering.

---

## What are our sources for potential candidates?

The sources and API calls we used to get our developers were the following:
| Source | API Documentation |
| ------ | ----------------- |
| Stackoverflow | [api.stackexchange.com/docs/users][stackoverflow] |

---

## Where was the data stored?

The retrieved data used to select candidates was stored in Mongodb Atlas. 

The answers candidates gave in the coding questions from the interface were stored in an Sqlite database.

Mongodb was chosen given that the API calls return JSON files, which is an ideal format for this NoSQL database. It also allows for cloud storage with Atlas, and has great integration with Python through the py-mongo library.

Sqlite provides a simple SQL database to store our structured information, the interface users and their answers.

---

## How was the project management done?

Our team used github projects to keep track of tasks and responsabilities. We divided our work the following way:

![workload]

*Legend:*

✅ &rarr; responsible; ✔ &rarr; helped; ❌ &rarr; not involved.

---

## What can be improved?

Our current application has lots of potential improvements, these are a few of them:
- Select candidates from more data sources;
- Have a code coverage of 80% for unit tests;
- Connect both databases;
- Have a page in the interface for the recruiting manager to acess the answers;
- Be able to email the candidates directly from the interface;
- Landing page thanking candidates for the submission;
- More appealing timer.

## File Navigation:

> Website: `Folder with everything related to the interface`

> preprocessing_tests: `Different tests and trials done while in the preprocessing phase, can be ignored`

> presentation: `The presentation was done in Markdown, all the code is provided there`

> utils: `Folder with the MongoDB setup`

> github.py: `Calls the github API and stores the data in MongoDB -> WORK IN PROGRESS`

> main.py: `Starts running the interface. It will run on the local machine`

> preprocessing.py: `Handles data preprocessing, creates and fits the model, at the end returns a dataframe with selected candidates`

> send_email.py: `Reads MongoDB collection selected_candidates and sends them an email with the interface link`

> stackoverflow.py: `Calls the stackoverflow API and stores the data in MongoDB`

> store_candidates.py: `Imports preprocessing.py and then stores the returned candidates in a new MongoDB collection called selected_candidates`


[//]: # (These are reference links they get stripped out when the markdown processor does its job)

   [stackoverflow]: <https://api.stackexchange.com/docs/users>
   [github]: <https://docs.github.com/en/rest/reference/users>
   [workload]: <https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7e79a89f-d59c-45b9-ac76-242251c8f41d/workload.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220317T183318Z&X-Amz-Expires=86400&X-Amz-Signature=9dd9d7d7e1a970ab6590592da3777f619d2dfd795f808aa31d8e6ba96548e1f6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22workload.png%22&x-id=GetObject>
   