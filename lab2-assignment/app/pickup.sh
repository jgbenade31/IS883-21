export PROJECT_ID=$(gcloud config get-value core/project)
export CLOUD_STORAGE_BUCKET=${PROJECT_ID}
export GOOGLE_APPLICATION_CREDENTIALS=~/ass1-key.json
source env/bin/activate