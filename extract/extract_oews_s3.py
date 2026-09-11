import boto3
import io
from extract_oews import con

df_oews_data = con.execute("SELECT * FROM raw_oews_data").df()

buffer = io.StringIO()
df_oews_data.to_csv(buffer, index=False)

s3 = boto3.client("s3")
s3.put_object(Bucket="s3-learn-bucket-381492047455-us-west-2-an", Key="raw/oews/oews_data.csv", Body=buffer.getvalue())
print("Uploaded oews_data to s3")