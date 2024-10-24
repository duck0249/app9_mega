import smtplib
from email.message import EmailMessage
from PIL import Image
import io

password = "lqjavdgzrjdqkuft"

def send_email(image_path):
	email_message = EmailMessage()
	email_message["Subject"] = "New customer showed up!"
	email_message.set_content("Hey, we just saw a new customer.")


	with open(image_path, "rb") as file:
		content = file.read()

	img = Image.open(io.BytesIO(content))

	email_message.add_attachment(content, maintype="image", 
							     subtype=img.format.lower())
	
	gmail = smtplib.SMTP("smtp.gmail.com", 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login("duck0249@gmail.com", password)
	gmail.sendmail("duck0249@gmail.com", "duck0249@gmail.com", 
				    email_message.as_string())
	gmail.quit()

if __name__ == "__main__":
	send_email(image_path="images/image.png")

