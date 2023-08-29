# import re

# class EmailAddressParser:
#     def __init__(self, email_string):
#         self.email_string = email_string

#     def parse(self):
#         # Split the email_string using either comma or space as separators.
#         # Remove any leading or trailing whitespace.
#         email_list = re.split(r'[, ]+', self.email_string.strip())

#         # Remove empty strings from the list.
#         email_list = [email for email in email_list if email]

#         # Remove duplicates by converting the list to a set and back to a list.
#         unique_emails = list(set(email_list))

#         # Sort the list of unique emails alphabetically.
#         unique_emails.sort()

#         return unique_emails

# # Example usage
# email_addresses = "john@doe.com, person@somewhere.org"
# parser = EmailAddressParser(email_addresses)
# parsed_emails = parser.parse()
# print(parsed_emails)  # Output: ["john@doe.com", "person@somewhere.org"]

import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Split the email_string using either comma or space as separators.
        # Remove any leading or trailing whitespace.
        email_list = re.split(r'[, ]+', self.email_string.strip())

        # Remove empty strings and non-emails from the list.
        email_list = [email for email in email_list if self.is_valid_email(email)]

        # Remove duplicates by converting the list to a set and back to a list.
        unique_emails = list(set(email_list))

        # Sort the list of unique emails alphabetically.
        unique_emails.sort()

        return unique_emails

    def is_valid_email(self, email):
        # Use a regular expression to check if the string is a valid email address.
        # You might want to use a more comprehensive email validation regex.
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

# Example usage
email_addresses = "talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why"
parser = EmailAddressParser(email_addresses)
parsed_emails = parser.parse()
print(parsed_emails)  # Output: ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"]
