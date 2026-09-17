import re

input_text = """Hello Team!
	I hope this email finds you well. Here are some contact details for your reference:
	John's email is john.doe@example.com, while the support team can be reached at support@company.org. For marketing inquiries, you can contact marketing.department@business-company.co.uk. 
	James also uses an alternate email: james_oreilly@personal-mail.net.
	If you have technical queries, write to tech123@services123.io, or for HR-related matters, email hr_dept2023@corporate.info. For upcoming events, reach out to events@conference-2024.co. 
	Alice’s legacy email is still active: alice.legacy+oldaddress@gmail.com. Developers can be contacted via dev.team@sub.domain-company.com.
	There are also some additional emails: contact@localhost, test.email+symbol@example-server.com, alias@internal.com, random_user@xyz.com, and special_email123@nonstandard.net.
	Please ensure that all emails listed above are added to the internal database and cross-verified with the respective departments.
	Best regards,
	Admin Team """


def val_adress(text):
    adreses = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return adreses


print(val_adress(input_text))
