def get_chastota(text):

    dictionary_frequency = {}
    text = text.lower()

    for i in text:
        if i.isalpha() or i == " ":
            continue
        else:
            text = text.replace(i, " ")

    text = text.split()

    for word in text:
        if word in dictionary_frequency:
            dictionary_frequency[word] += 1
        else:
            dictionary_frequency[word] = 1
    print(dictionary_frequency)


ishodniy_text = """Applications in Data Analysis
NumPy is a foundational tool for data analysis. It integrates seamlessly with libraries like Pandas, Matplotlib, and Scikit-learn. When working with large datasets, preprocessing tasks such as normalization, reshaping, and handling missing data often rely on NumPy’s capabilities. Additionally, its integration with other libraries makes it a core component of the Python data ecosystem.
In conclusion, mastering NumPy arrays is essential for anyone looking to excel in numerical computing or data analysis. Its efficiency, flexibility, and integration with other tools make it an invaluable asset for Python programmers"""

get_chastota(ishodniy_text)
