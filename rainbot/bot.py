import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("EmCWw02kB6OzvsapIiQ7DhaRC", "2tEtWpx0i5JPmv9rtN4PE13udiDuSfQar6Qapkv3rQgNi7ddc7")
auth.set_access_token("4109292376-6IbVa6CslXtpSdwDjqj0XGVgxfL94xZwl5mdFZY", "KWWhmWUyDqJNtEj1kfE8XmZKG53dsVXSqwNBeiMVdMtLS")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
