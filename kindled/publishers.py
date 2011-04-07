import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


class SmtpEmailPublisher(object):

    """ SMTP Email Publisher """

    _DESCRIPTION = "SMTP Email Publisher"

    logger = None


    def __init__(self, logger=None):

        """ Constructor """

        self.logger = logger

        self.logger.debug(self._DESCRIPTION)

    
    def publish(self, cfg):

        """ Publish """

        self.logger.debug("Publishing...")
    
        """

        msg = MIMEMultipart()

        msg["From"] = config.get("smtp_from_address")
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject

        msg.attach(MIMEText(text))
    
        if attachments is None: attachments = []
        
        for attachment in attachments:
            
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(attachment, "rb").read())
            Encoders.encode_base64(part)
            part.add_header("Content-Disposition", 'attachment; filename="%s"' % os.path.basename(attachment))
            msg.attach(part)
        
        mailServer = smtplib.SMTP(config.get("smtp_host"), int(config.get("smtp_port")))
        if(bool(config.get("smtp_start_tls")) == True):
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
        mailServer.login(config.get("smtp_username"), config.get("smtp_password"))
        mailServer.sendmail(config.get("smtp_username"), recipients, msg.as_string())
        mailServer.close()

        """
