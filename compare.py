import os, sys
from datetime import datetime
from hashlib import md5

class FileCompare(object):
    def __init__(self, source, destination):
        self.files_list = []
        self.not_found = {}
        self.mis_match = {}
        self.matched = True
        self.source = source
        self.destination = destination
        self.get_files()
        self.compare()

    def get_files(self):
        for path, dirs, files in os.walk(self.source):
            for directory in dirs:
                self.files_list.append(os.path.join(path, directory))
            for source_file in files:
                self.files_list.append(os.path.join(path, source_file))

    def compare(self):
        for source_path in self.files_list:
            dest_path = os.path.join(source_path.replace(self.source, self.destination))
            if os.path.exists(dest_path):
                if os.path.isfile(dest_path):
                    source_size = os.path.getsize(source_path)
                    dest_size = os.path.getsize(dest_path)
                    if not os.path.getsize(source_path) == os.path.getsize(dest_path):
                        self.matched = False
                        self.mis_match[source_path] = {
                            "source": source_path,
                            "source_size": source_size,
                            "dest": dest_path,
                            "dest_size": dest_size,
                        }
            else:
                self.matched = False
                self.not_found[source_path] = dest_path

    def get_report(self):
        output_Str = "\n"*2 + "Summary Report\n" + "="*14 + "\n"*2 + "*"*62 + "\n"*2 + "Source Path: " \
            + self.source + "\n" + "Destination Path: " + self.destination + "\n"*2 + "*"*62 + "\n"*2
        not_found = ""
        mis_match = ""
        if self.matched == True:
            output_Str += "Success! Everything matched.\n"
        else:
            if self.not_found:
                not_found += "Missing Files\n" + "="*36 + "\n"
                for key, value in self.not_found.iteritems():
                    not_found += value + "\n"
                output_Str += not_found + "\n"*2
            if self.mis_match:
                mis_match += "Mismatched Files | Source | Source Size (KB)| Destination | Destination Size(KB)\n" + "="*80 + "\n"
                for key, value in self.mis_match.iteritems():
                    mis_match += value['source'] + " - " + str(value['source_size']/1024.0) + " : " + value['dest'] + " - " + str(value['dest_size']/1024.0) + "\n"
                output_Str += mis_match
        return output_Str

if __name__ == '__main__':
    source = ""
    destination = ""
    try:
        source = sys.argv[1]
        destination = sys.argv[2]
        compare = FileCompare(source, destination)
        print compare.get_report()
    except IndexError:
        print "Source and Destination required. eg: python compare.py /path/to/source /path/to/destination"
    except Exception as e:
        print e