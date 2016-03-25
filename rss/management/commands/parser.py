from django.core.management.base import BaseCommand, CommandError
from rss.models import RssFeed, RssEntries
import feedparser, re



class Command(BaseCommand):
    help = 'Adding RSS feed to Database'

    def handle(self, *args, **options):
        
        obj = RssFeed.objects.all()
        objEn = RssEntries.objects.all()
        
        rss = len(obj)
        
        for x in range(0, rss):
            
            if obj[x].active == True:
                parse = feedparser.parse(RssFeed.objects.get(id=x+1).link)
                length = len(parse)

                for num in range (0, length):
                    rss_id =  RssFeed.objects.get(id=x+1)
                
                    title = parse['items'][num].title
                    link = parse['items'][num].link
                    published = parse['items'][num].published

                    content = parse['items'][num].description 
                    match = re.match('<img.*?src="(.*?)".*?(\/>|<\/img>)', content)
                    
                    if match:
                        image = match.group(1)
                    else:
                        print 'Nema slike'

                    if RssEntries.objects.filter(title=title):
                        pass
                    else:
                        if hasattr(parse['items'][num], 'author'):
                            author = parse['items'][num].author
                            RssEntries.objects.create(title=title, link=link, author=author, image=image, published=published, rss=rss_id)
                            print "Completed"
                        else:
                            RssEntries.objects.create(title=title, link=link,image=image, published=published, rss=rss_id)
                            print "Completed"
                        
            else: 
                pass