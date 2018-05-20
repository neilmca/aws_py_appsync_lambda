import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig()

GET_INDEX = {'field': 'getIndex', 'arguments': {'id': 'top_stories'}}
GET_ARTICLE = {'field': 'getArticle', 'arguments': {'id': '1'}}


def handler(event, context):
    indexes = {
              'top_stories': {
                  'meta': {
                      'type': 'index'
                  },
                  'items' : [
                      {
                          'type' : 'index_card',
                          'title' : 'Royal Wedding',
                          'image' : 'http://bbc.co.uk/123.jpg',
                          'article_link' : '1'
                      },
                      {
                          'type' : 'index_card',
                          'title' : 'Russia',
                          'image' : 'http://bbc.co.uk/123.jpg',
                          'article_link' : '2'
                      }
                  ]
                  
               }
              
              }
    articles = {

        '1' : {
            'meta': {
                      'type': 'article'
                  },
            'items' : [
                      {
                          'type' : 'headline_card',
                          'text' : 'This is a headline'
                      },
                      {
                          'type' : 'main_image_card',
                          'image' : 'http://bbc.co.uk/123.jpg'
                      },
                      {
                          'type' : 'paragraph_card',
                          'text' : 'blah'
                      }

                  ]
            
            },
        '2' : {}
    }

   

    logger.info('got event{}'.format(event))

    if event['field'] == 'getIndex':
        args = event['arguments']
        id = args['id']
        return indexes[str(id)]
    elif event['field'] == 'getArticle':
        args = event['arguments']
        id = args['id']
        return articles[str(id)]
    else:
        logging.error('unable to resolve field {}'.format(event['field']))
    
    
    logger.error('something went wrong to get here')
    

def main():

    #GET INDEX
    resp = handler(GET_INDEX, None)
    logging.info(resp)
    #GET ARTICLE
    resp = handler(GET_ARTICLE, None)
    logging.info(resp)
    

if __name__ == "__main__":
   main()