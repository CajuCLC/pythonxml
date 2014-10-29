import lxml.etree as et

xmltext = """
<root>
  <sampleone>
    <fruit>apple</fruit>
  </sampleone>
  <sampletwo>
    <fruit>pear</fruit>
    <fruit>mango</fruit>
    <fruit>kiwi</fruit>
  </sampletwo>
</root>
"""

# tree = et.fromstring(xmltext)
tree = et.parse("dnsrecord.xml")

for Name in tree.xpath('//Name'):
    Name.text = 'rotten %s' % (Name.text,)

print et.tostring(tree, pretty_print=True)