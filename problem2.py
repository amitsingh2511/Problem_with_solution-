# Find the domain of each email]

def find_email_domains(emails):
    domains = [email.split('@')[1] for email in emails]
    return domains

# Example usage
input_emails = ['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
output_domains = find_email_domains(input_emails)
unique_domains = list(set(output_domains))
print(unique_domains)

# Output ['a.com','d.com','b.com']


#Find the domain of each url

# Simply remove the 'www.'
def find_url_domains(urls):
    domains = [url.lstrip('www.') for url in urls]
    return domains

input_urls = ['www.a.com', 'www.b.com', 'www.c.com']
output_domains = find_url_domains(input_urls)
print(output_domains)

# Output ['a.com','b.com','c.com']

# Count the number of times each URl while ignoring the ones that do not matter 

def count_domains(domain_list, valid_domains):
    domain_counts = {domain: 0 for domain in valid_domains}

    for domain in domain_list:
        if domain in domain_counts:
            domain_counts[domain] += 1

    return domain_counts

input_domains = ['a.com', 'a.com', 'b.com', 'd.com']
valid_domains = ['a.com', 'b.com', 'c.com']

result = count_domains(input_domains, valid_domains)
print(result)

# Output {'a.com':2,'b.com':1,'c.com':0}


# Return the dictionary with the 'www' attached 

def attach_www(dictionary):
    result = {'www.' + key: value for key, value in dictionary.items()}
    return result

input_dict = {'a.com': 2, 'b.com': 1, 'c.com': 0}

result = attach_www(input_dict)
print(result)

# Output {'www.a.com':2, 'www.b.com':1, 'www.c.com':0}

