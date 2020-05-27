import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email", "password")
message = "Hey developer the model is ready and giving good accuracy"
s.sendmail("gauravbiyani63@gmail.com", "alphabeast70@gmail.com", message)
print("Mail Sent")
s.quit() 
