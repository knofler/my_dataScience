import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    tweet = fp.readlines() 
    print tweet["trends"]
    # dics = fp.readlines()
    # tweets = str(len(fp.readlines()))

	# f = open('test12.txt','w')
	# f.write(str(fp.readlines()))
	# f.close()

    # for tweet in tweets:
    # 	print tweet

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    # lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
