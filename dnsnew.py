#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.ResourceRecordSet = ""
      self.Name = ""
      self.Type = ""
      self.TTL = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "ResourceRecordSet":
         print "*****ResourceRecordSet*****"

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "Name":
         print "Name:", self.Name
      elif self.CurrentData == "Type":
         print "Type:", self.Type
         type = self.Type
      elif self.CurrentData == "TTL":
         print "TTL:", self.TTL
         ttl = self.TTL
      self.CurrentData = ""
   
   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "Name":
         self.Name = content
         name = self.Name
      elif self.CurrentData == "Type":
         self.Type = content
      elif self.CurrentData == "TTL":
         self.TTL = content

if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("dnsrecord.xml")

import pyrax

pyrax.set_setting('identity_type', 'rackspace')
pyrax.set_credentials('latamcloud', '5423fbfe44ec45a4b793aab1228e242f')

dns=pyrax.cloud_dns
dom=dns.find(name="ericcavalcanti2.com.br")

dom.add_record({'type': self.Type,
                   'name': self.Name,
                   'ttl': self.TTL,
                   'data': "web-04.signashop.com.br"})