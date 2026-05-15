FROM python:3.14.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# TODO: Figure out how to call api from docker container and run ui locally?

#COPY api_numpy.py .
#RUN apt-get update && apt-get install -y curl unzip && \
 #   curl -L -o ./datasets.zip  https://www.kaggle.com/api/v1/datasets/download/bismasajjad/global-ai-job-market-and-salary-trends-2025 && \
  #  unzip datasets.zip -d datasets && \
   # rm datasets.zip
CMD ["python3", "-c","\
    #import api_numpy;\
    #dataframe = api_numpy.apply_transformations('datasets/ai_job_dataset.csv', 'datasets/ai_job_dataset1.csv');\
    #dataframe.to_csv('numpy_ai_job_datasets.csv', index=False);\
    "]
