def main(filepath, column):
  indexer = Index(NGRAM)
  f = codecs.open(filepath, "r", "utf-8")
  lines = f.readlines()

  indexer.load ("./")

  for line in lines:
    print('some text')
    print(line)
    print('another change')
    elems = line.split ("\t")
    indexer.append (''.join (elems[column - 1]))
    print(lines)

if __name__ == "__main__":
  if len(sys.argv) < 8:
    print "usage: ./indexer_update.py UPDATE_TSV_FILE_PATH TARGET_COLUMN_NUM"
    sys.exit(1)

 def get_content_num(self):
    return len(self.contentTable)
