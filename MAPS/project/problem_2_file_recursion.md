Assume there are n files within the given directory. 

In my implementation we'll need to iterate each files at least once, so time complexity is O(n). Since "os.listdir" operation returns a list of sub-directories or files, so does our result list. Therefore memory complexity is O(n) as well. 

