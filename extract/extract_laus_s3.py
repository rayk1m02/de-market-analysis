import boto3
import io
from extract_laus import extract_laus, series_ids
import pandas as pd

df_lookup, df_data = extract_laus(series_ids)

buffer = io.StringIO()
df_data.to_csv(buffer, index=False)

s3 = boto3.client("s3")
s3.put_object(Bucket="s3-learn-bucket-381492047455-us-west-2-an", Key="raw/laus_data.csv", Body=buffer.getvalue())
print("Uploaded to s3")