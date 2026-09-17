import re
from datetime import datetime

input_text = """ On February 14, 2022, a long-awaited meeting took place between two organizations that had been planning a joint project for years. The discussions continued well into the evening, and by 23.03.2022, a draft agreement was ready for review. Despite some setbacks over the summer, significant progress was made, culminating in a final decision on 10.11.2022 to proceed with the implementation phase.
	The following year saw rapid development, with major milestones achieved by January 15, 2023, and 04.04.2023. However, an unexpected delay arose on July 19, 2023, prompting a reassessment of the project timeline. Adjustments were made, and by 30.09.2023, the team was back on track, ready for the next phase of the initiative."""


def standart(text):
    pattern = r"\b(?:\d{2}\.\d{2}\.\d{4}|[A-Z][a-z]+\s+\d{1,2},\s+\d{4})\b"
    all_dates = re.findall(pattern, text)

    form_dates = []
    for ish_dates in all_dates:
        if "." in ish_dates:
            form_dates.append(ish_dates)
        else:
            dt = datetime.strptime(ish_dates, "%B %d, %Y")
            form_dates.append(dt.strftime("%d.%m.%Y"))

    return form_dates


print(standart(input_text))
