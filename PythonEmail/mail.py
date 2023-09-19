import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Pengaturan email pengirim
sender_email = "helloyoel7@gmail.com"
sender_password = "QWERTYuiop"

# Pengaturan email penerima
receiver_email = "yoelagustinus7@gmail.com"

# Subjek email
subject = "Test Sending Email attachment PDF using Python"

# Isi email (opsional)
body = "Ini adalah body email dengan lampiran PDF yang dikirim dengan menggunakan Python."

# Lokasi berkas PDF yang akan dilampirkan
pdf_file_path = "file_send.pdf"

# Membaca berkas PDF
with open(pdf_file_path, "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Membuat pesan email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Menambahkan isi email
msg.attach(MIMEText(body, "plain"))

# Menambahkan lampiran PDF
pdf_attachment = MIMEApplication(pdf_data, _subtype="pdf")
pdf_attachment.add_header("content-disposition", "attachment", filename="file.pdf")
msg.attach(pdf_attachment)

# Mengirim email menggunakan SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email berhasil terkirim.")
except Exception as e:
    print("Email gagal terkirim:", str(e))