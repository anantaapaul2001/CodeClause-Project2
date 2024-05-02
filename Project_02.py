import hashlib

class URLShorterner:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        url_hash = hashlib.sha256(long_url.encode()).hexdigest()[:8]

        #store the mapping of the shortened url
        self.url_map[url_hash] =long_url

        #construct short url using base url and hash 
        short_url = f"http://short.url/{url_hash}"

        return short_url
    
    def restore_url(self, short_url):

        #extract the hash from short url
        url_hash = short_url.split("/")[-1]

        #retrieve the original url 
        original_url= self.url_map.get(url_hash, None)

        return original_url
    
#example:

shortener = URLShorterner()
long_url ="http://www.example.com/this/is/a/very/long/url"
short_url = shortener.shorten_url(long_url)
print("Shortened URL: ", short_url)


#restore the orginal url 
restored_url = shortener.restore_url(short_url)
print("Restored URL: ", restored_url)
