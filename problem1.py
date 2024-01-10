'''
Given a list of emails and URLs, return a dictionary, where each key is a URL and the value is how many emails have the same domain. Note that the domains begin with  www.  whereas the emails do not, and that emails with domains not in the list of urls should be ignored.
count_email_domains(
emails=['foo@a.com', 'bar@a.com', baz@b.com', 'qux@d.com'],
urls=['www.a.com', 'www.b.com', 'www.c.com'],
)
'''

def count_email_domains(emails, urls):
    domain_counts = {}

    for email in emails:
        # Splitting the email address to get the domain
        domain = email.split('@')[1]

        domain = "www." + domain

        # Checking if the domain is in the list of URLs
        for url in urls:
            if url == domain:
                # Incrementing the count for the corresponding URL
                domain_counts[url] = domain_counts.get(url, 0) + 1
                break

    return domain_counts

# Example usage
emails = ['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
urls = ['www.a.com', 'www.b.com', 'www.c.com']

result = count_email_domains(emails, urls)
print(result)


# Output {'www.a.com': 2, 'www.b.com': 1}
