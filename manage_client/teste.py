from jose import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJqb2huQGdtYWlsLmNvbSIsImV4cCI6MTcxMzg3MDI2MX0.poYR6jg98Y0EI8js4EoNklPdQOEjupq47EPTGpqZJTk"

SECRET_KEY="27d6489583a70f80386ee6bb57ac9d610ddb714748fa997e70360ee50a0393f8"

decode = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

print(decode)