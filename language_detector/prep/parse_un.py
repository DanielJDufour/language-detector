from xml.etree import ElementTree
from os.path import dirname, realpath

directory_of_sources = dirname(realpath(__file__)) + "/sources/" 


d = {}
d['AR'] = "Arabic"
d['EN'] = "English"
d['ES'] = "Spanish"
d['FR'] = "French"
d['RU'] = "Russian"
d['ZH'] = "Mandarin"

filepath = '/tmp/uncorpora_plain_20090831.tmx'
count = 0
for event, elem in ElementTree.iterparse(filepath, events=('start', 'end', 'start-ns', 'end-ns')):
    if event == "start":
        print event, elem
        if elem.tag == "tu":
            uid = elem.attrib['tuid']
        if elem.tag == "tuv":
            language = elem.attrib['{http://www.w3.org/XML/1998/namespace}lang']
        if elem.tag == "seg":
            text = elem.text
            print language, "text is", text
            if text and len(text) > 200:
                with open(directory_of_sources + d[language] + "/" + uid, "wb") as f:
                    f.write(text.encode("utf-8"))

    count += 1
    if count == 50000:
        break
