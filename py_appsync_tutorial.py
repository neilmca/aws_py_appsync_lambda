import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig()

GET_POST = {'field': 'getPost', 'arguments': {'id': '3'}}
GET_RELATED_POST = {'field': 'relatedPosts', 'source': {'id': '3'}}

def handler(event, context):
    posts = {
              "1": {"id": "1", "title": "First book", "author": "Author1", "url": "https://amazon.com/"},
              "2": {"id": "2", "title": "Second book", "author": "Author2", "url": "https://amazon.com"},
              "3": {"id": "3", "title": "Third book", "author": "Author3", "url": None },
              "4": {"id": "4", "title": "Fourth book", "author": "Author4", "url": "https://www.amazon.com/"},
              "5": {"id": "5", "title": "Fifth book", "author": "Author5", "url": "https://www.amazon.com/" } 
              }

    relatedPosts = {
              "1": [posts['4']],
              "2": [posts['3'], posts['5']],
              "3": [posts['2'], posts['1']],
              "4": [posts['2'], posts['1']],
              "5": []
          }

    logger.info('got event{}'.format(event))

    if event['field'] == 'getPost':
        args = event['arguments']
        id = args['id']
        return posts[str(id)]
    elif event['field'] == 'allPosts':
        pass
    elif event['field'] == 'relatedPosts':
        src = event['source']
        id = src['id']
        return relatedPosts[str(id)]
    else:
        logging.error('unable to resolve field {}'.format(event.field))
    
    
    logger.error('something went wrong to get here')
    

def main():

    #GET POST
    resp = handler(GET_POST, None)
    logging.info(resp)
    #GET RELATED POSTS
    resp = handler(GET_RELATED_POST, None)
    logging.info(resp)

if __name__ == "__main__":
   main()