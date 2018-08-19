## WeRateDogs Twitter Data Analysis

The dataset that I will be wrangling (and analyzing and visualizing) is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog.

1. Gather data from 3 difference sources.
	- Twitter data in cvs file provided by Udacity
	- Image prediction data from Udacity servers
	- Additional twitter data via API
2. Assess visually and programmatically for data quality and tidiness issues.
3. Clean and fix data.
4. Analyze data.

### Data

`twitter-archive-enhanced.csv`: twitter data
	- basic tweet data
	- each tweet's text
	- rating numerator
	- rating denominator
	- dog name
	- dog "stage" (i.e. doggo, floofer, pupper, and puppo)

`image_predictions.tsv`: image prediction data
	- #1 to #3 of prediction for the image in the tweet
	- #1 to #3 of confidence of the algorithm
	- #1 to #3 of predicted a breed of dog

`tweet_json.txt`: additional twitter data via API


### Questions to answer
- How good the image prediction algorithm was to predict dog images?
- Are top breeds of dogs associated with rating?
- Which variables are associated with retweets and favorite counts?

### Findings and Summary
- <a href="https://github.com/ayumiohashi/udacity-data-analyst/blob/master/06-twitter-data-analysis/twitter-data-analysis.ipynb">Findings</a>
- <a href="
https://github.com/ayumiohashi/udacity-data-analyst/blob/master/06-twitter-data-analysis/reports/analysis-summary.pdfSummary">Summary</a>
