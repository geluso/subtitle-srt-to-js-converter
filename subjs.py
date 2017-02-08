import argparse
import codecs

def parse_subtitles(subtitles):
  while True:
    line = subtitles.readline()
    if line == '':
      break
    line_number = int(line)
    time = subtitles.readline()
    line1 = ""
    line2 = subtitles.readline() 
    while True:
      line = subtitles.readline()
      if (line and not line == "\r\n"):
        line1 = line2
        line2 = line
      else:
        break

    time = time.strip()
    line1 = line1.strip()
    line2 = line2.strip()

    line1 = line1.replace('"', "'")
    line2 = line2.replace('"', "'")

    print "{"
    print "  duration: \"%s\"," % time
    print "  line1: \"%s\"," % line1
    print "  line2: \"%s\"," % line2
    print "},"

def main():
  parser = argparse.ArgumentParser(description="converts .srt files to .js variant.")
  parser.add_argument('subtitles', help="the file containing the subtitles")

  args = parser.parse_args()
  subtitles = codecs.open(args.subtitles, "r", "utf-8-sig")

  print "var SUBTITLES = ["
  parse_subtitles(subtitles)
  print "];"

if __name__ == "__main__":
  main()
