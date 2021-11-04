import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = set(mails)
        self.domains = set(domains)

    def validate(self, email):
        (name, mail, domain) = re.split('[@.]', email)
        return self.__is_name_valid(name) \
               and self.__is_mail_valid(mail) \
               and self.is_domain_valid(domain)

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def is_domain_valid(self, domain):
        return domain in self.domains


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
