import sys

if len(sys.argv) != 2:
    print("Usage: python runner.py <url>")
    sys.exit(1)
else:
    from fetch import youtube_transcript
    from trainer import qnaModel
    import threading
    import time
    
    def qna_thread(video_url, question):
        main = youtube_transcript.transcript(video_url)
        result = qnaModel.qna(main, question)
        if result == "Sorry, I do not know the answer to that question.":
            print(result)
        else:
            print('Answer: '+ result[0] + '\nScore: ' + str(result[1]))
    
    print()
    print()
    print()
    
    # Get the arguments from the command line
    video_url = sys.argv[1]
    
    question = input("What is your question?: ")

    # Fetch the YouTube transcript
    main = youtube_transcript.transcript(video_url)
    
    qna_thread = threading.Thread(target=qna_thread, args=(video_url, question))
    qna_thread.start()
   
        
    print("Please wait...")
    
    animation = "|/-\\"
    idx = 0    
    while qna_thread.is_alive() == True:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        
    print()
    print()
    print()
    print()
    
    qna_thread.join()
    
    
    

    
