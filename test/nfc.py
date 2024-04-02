import nfc

clf = nfc.ContactlessFrontend()
clf.open('/dev/ttyUSB0')

try:
    target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
    if target:
        tag = nfc.tag.activate(clf, target)
        print(tag)
finally:
    clf.close()
