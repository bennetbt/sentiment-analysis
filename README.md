# sentiment-analysis
GitHub Repository for the Sentiment Analysis Service

# Building the container image
Within the sentiment-analysis directory first run:
	docker build --tag docker-analysis .
Then run:
	docker run -d --name analyzer -p 5001:8000 docker-analysis
	
# Using the container image
With the container running, navigate to localhost/5001 to access the analyzer, the analyzer must be running for the gui to fully function
