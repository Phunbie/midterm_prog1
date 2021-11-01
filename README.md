# midterm_prog1
First mlzoomcamp project


## Customer propensity to purchase

### Context

You get many visitors to your website every day, but you know only a small percentage of them are likely to buy from you, while most will perhaps not even return.Propensity modeling allows you to allocate your resources more wisely, resulting in greater efficiencies, while achieving better results. To give an example, think of this: instead of sending an email advertisement where there’s a 0%-100% chance of a user clicking it, with propensity modeling, you can target users with a 50%+ chance of clicking it. Fewer emails, more conversions! Right now you may be spending money to re-market to everyone, but perhaps we could use machine learning to identify the most valuable prospects. Having this important information can also help the marketing department know the kind of email to sent to a particular visitor.


### Instructions on how to run the project

The pickled model is already in all you have to do is run this on your command promt:

1)docker build -t propensity-prediction .

2)docker run -it --rm -p 8181:8181 propensity-prediction:latest

 with this two commands the app will be deployed in a docker container
 
 You can now send a query to this container to recieve prediction whether the customer has the propensity to purchase(true) or not(false) runing
 this: python data.py
