import lxml.etree as et

tree = et.parse("dns.xml")

for type in tree.xpath('//Type'):
    type.text = '%s' % (type.text,)
for name in tree.xpath('//Name'):
    name.text = '%s' % (name.text,)
for ttl in tree.xpath('//TTL'):
    ttl.text = '%s' % (ttl.text,)
for cname in tree.xpath('//Cname'):
    cname.text = '%s' % (cname.text,)

print type.text
print name.text
print ttl.text
print cname.text

import pyrax
import pyrax.exceptions as exc

pyrax.set_setting('identity_type', 'rackspace')
pyrax.set_credentials('USER', 'API')

dns = pyrax.cloud_dns
domain_name = "ericcavalcanti.com.br"
todel = name.text

# Check if domain exists.
try:
	dom=dns.find(name=domain_name)
except pyrax.exceptions.NotFound:
	print("The domain name "+domain_name+" was not found")
	sys.exit()

# Checks if record really exists and then delete.
try:
  record = dom.find_record(type.text, name=name.text)
  print("Deleting Record: "+record.id+"\tRecord Name: "+record.name+"")
  record = dom.get_record(record.id)
  record.delete()

# Error if record doesn't exist.
except pyrax.exceptions.DomainRecordNotFound:
  print("Record "+name.text+" was not found.")
  print("Exiting now")
