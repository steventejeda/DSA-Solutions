from collections import defaultdict

def subDomainCount(cpdomains):
    counts = defaultdict(int)

    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)

        single_domain = domain.split('.')

        for i in range(len(single_domain)):
            counts['.'.join(single_domain[i:])] += count
    
    return [f"{count} {domain}" for domain, count in counts.items()]

print(subDomainCount(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))