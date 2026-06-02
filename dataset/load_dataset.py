import kagglehub

# Download latest version
path = kagglehub.dataset_download("dhruvb2028/credit-card-fraud-dataset")

print("Path to dataset files:", path)