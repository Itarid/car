def main(filepath, column):
  indexer = Index(NGRAM)
  f = codecs.open(filepath, "r", "utf-8")
  lines = f.readlines()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "usage: ./indexer_update.py UPDATE_TSV_FILE_PATH TARGET_COLUMN_NUM"
    sys.exit(1)