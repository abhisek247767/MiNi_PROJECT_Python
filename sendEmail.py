import smtplib as s 

ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('abhisekroy169@gmail.com','123456')
subject="test python"
body="I love python"
messege="subject:{}\n\n{}".format(subject,body)
listadd=['royabhisek083@gmail.com','hlo@civo.com',
'it@email.info.org']
ob.sendmail('abhisekroy169@gmail.com', listadd,messege)
print("Send mail !!")
ob.quit()