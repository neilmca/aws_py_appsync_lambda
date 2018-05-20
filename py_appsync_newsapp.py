#START - stuff to put into the Lambda

import logging
import json
#import boto3 #uncomment when on lambda

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig()

CMS_BUCKET = 'neil-appsync-lambda-news-cms'
CMS_KEY = 'cms-content.json'

def handler(event, context):
    
    #In lambda this is read from S3 using boto3 lib - have not installed locally, so cannot run
    
    #read from S3

    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=CMS_BUCKET, Key=CMS_KEY)
    cms_content = response['Body'].read().decode('utf-8')
    cms_content_json = json.loads(cms_content)
    return handler_with_cms_data(event, context, cms_content_json)

def handler_with_cms_data(event, context, cms_content_json):
    logger.info('got event {}'.format(event))
    logger.info('got cms data {}'.format(cms_content_json))

    #extract indexs and articles from CMS content
    indexes = cms_content_json['indexes']
    articles = cms_content_json['articles']

    if event['field'] == 'getList':
        args = event['arguments']
        id = args['id']
        #look in index first
        item = None
        if id in indexes.keys():
            item = indexes[id]
        elif id in articles.keys():
            item = articles[id]
        return item
    else:
        logging.error('unable to resolve field {}'.format(event['field']))
    
    
    logger.error('something went wrong to get here')
    
#END - stuff to put into the Lambda


GET_INDEX = {'field': 'getList', 'arguments': {'id': 'index/top_stories'}}
GET_ARTICLE = {'field': 'getList', 'arguments': {'id': 'article/1'}}

def handler_local(event, context):
    #read from json
    

    with open('cms-content.json') as json_data:
        cms_content_json = json.load(json_data)
  
    handler_with_cms_data(event, context, cms_content_json)


def main():

    #GET INDEX
    resp = handler_local(GET_INDEX, None)
    logging.info(resp)
    #GET ARTICLE
    resp = handler_local(GET_ARTICLE, None)
    logging.info(resp)
    

if __name__ == "__main__":
   main()