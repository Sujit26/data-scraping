from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from scraper.scraper.spiders.spider1 import TheodoSpider
from data_scraper.models import Blog
from scripts.beautifull import BrickSetSpider

brickSetSpider = BrickSetSpider()
class BlogApiView(APIView):

    def get(self,request,tag):

        blogList = brickSetSpider.start_requests(tag)
        for blog in blogList:
            
            obj,_ = Blog.objects.get_or_create(title = blog['title'])
            if(_):
                print(blog)
            if(not _):
                print(blog['title'], " is present")
                if tag not in obj.tag:
                #     print(tag," is present database")
                # else:
                #     # print(tag," is not present database")
                    obj.tag = obj.tag +","+tag

            obj.name = blog['name']
            obj.date = blog['date']
            obj.short_desciption = blog['short_desciption']
            obj.responses = blog["responses"]
            obj.read_time = blog["read_time"]
            obj.save()
            obj.refresh_from_db()
    
        # Blog.refresh_from_db(fields=tag)
        if(tag=="blog"):
            data = Blog.objects.all()
        else:
            data = Blog.objects.all().filter(tag__icontains=tag)

        
        serializer = BlogSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)



# # connect scrapyd service
# scrapyd = ScrapydAPI('http://localhost:6800')

# def is_valid_url(url):
#     validate = URLValidator()
#     try:
#         validate(url) # check if url format is valid
#     except ValidationError:
#         return False

#     return True

# import json

# @csrf_exempt
# @require_http_methods(['POST', 'GET']) # only get and post
# def crawl(request):
#     # Post requests are for new crawling tasks
#     if request.method == 'POST':

#          # take url comes from client. (From an input may be?)
        
#         received_json_data = json.loads(request.body.decode("utf-8"))
#         tag = received_json_data['url']
#         # url  = "https://medium.com/tag/database"
#         url = 'https://google.com'
#         print("url:",url)
#         if not url:
#             return JsonResponse({'error': 'Missing  args'})
        
#         if not is_valid_url(url):
#             return JsonResponse({'error': 'URL is invalid'})
        
#         domain = urlparse(url).netloc # parse the url and extract the domain
#         unique_id = str(uuid4()) # create a unique ID. 
        
#         # This is the custom settings for scrapy spider. 
#         # We can send anything we want to use it inside spiders and pipelines. 
#         # I mean, anything
#         settings = {
#             'unique_id': unique_id, # unique ID for each record for DB
#             'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
#         }

#         # Here we schedule a new crawling task from scrapyd. 
#         # Notice that settings is a special argument name. 
#         # But we can pass other arguments, though.
#         # This returns a ID which belongs and will be belong to this task
#         # We are goint to use that to check task's status.
#         task = scrapyd.schedule('default', 'icrawler', 
#             settings=settings, url=url, domain=domain,tag=tag)

#         return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started' })

#     # Get requests are for getting result of a specific crawling task
#     elif request.method == 'GET':
#         # We were passed these from past request above. Remember ?
#         # They were trying to survive in client side.
#         # Now they are here again, thankfully. <3
#         # We passed them back to here to check the status of crawling
#         # And if crawling is completed, we respond back with a crawled data.
#         task_id = request.GET.get('task_id', None)
#         unique_id = request.GET.get('unique_id', None)

#         if not task_id or not unique_id:
#             return JsonResponse({'error': 'Missing args'})

#         # Here we check status of crawling that just started a few seconds ago.
#         # If it is finished, we can query from database and get results
#         # If it is not finished we can return active status
#         # Possible results are -> pending, running, finished
#         status = scrapyd.job_status('default', task_id)
#         if status == 'finished':
#             try:
#                 # this is the unique_id that we created even before crawling started.
#                 item = Blog.objects.get(unique_id=unique_id) 
#                 return JsonResponse({'data': item.to_dict['data']})
#             except Exception as e:
#                 return JsonResponse({'error': str(e)})
#         else:
#             return JsonResponse({'status': status})