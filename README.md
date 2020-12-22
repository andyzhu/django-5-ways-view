this repo is the result of tutorial at https://learndjango.com/tutorials/hello-world-5-different-ways

1. App + TemplateView
   1. This approach works well for large projects where you want a dedicated pages app for static pages. 
2. Function-Based View
3. No Template
4. No App
   1. We don't have to use apps, actually, if we don't want to. It's possible to create a "Hello World" page solely within our project-level directory.
   2. Directly edit the path in urls.py at the project level
5. Models
   1. A fifth approach would be to use the database to display our "Hello World" message. That involves adding a models.py file and leveraging the built-in DetailView.
      1. create a model
      2. register the model
      3. add a record in the databaseadd urls patterns at app level
      4. add a Template
      5. add a view to read from the database
   
To play around
1. Create VENV
2. install django