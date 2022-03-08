import smtplib
import imaplib, email

from email.header import decode_header

class Outlook:
      def __init__(
          self,
          email,
          password
      ):
          self.email    = email
          self.password = password
          
          self.server       = smtplib.SMTP('smtp-mail.outlook.com', 587)
          self.email_server = imaplib.IMAP4_SSL("imap.gmail.com")
      
      def setup(
          self,
          subject = "",
          content = "",
      ): 
          self.server.ehlo()
          self.server.starttls()

          self.body = ""
          self.body = "Subject: %s\n%s" % (
               subject,
               content,
          )
      
      def send(
          self,
          target = ""
      ): 
          self.server.login(
               self.email, self.password
          )
          
          if self.body != None or "":
             self.server.sendmail(
                  self.email,

                  target,
                  self.body
             )

      def login( 
          self,
      ):
          if self.email and self.password != "":
             self.email_server.login(
                  self.email, 
                  self.password
             )
          else:
             print('! | Improper Email Provided')
            
      def read(
          self
      ): 
          messages = self.email_server.select("INBOX"), len(self.email_server.select(
                                                                 "INBOX"
          )[0])
        
          emails = []
          emails
        
          for message in messages:
              for item in self.email_server.fetch(
                          str(message), "(RFC822)"
              ):
                  emails += {
                         "subject": "%s" % (decode_header(email.message_from_bytes(item[1]))),
                         "content": "%s" % (item.get_payload(decode = True).decode())
                  }

          if emails != []:
             return emails
