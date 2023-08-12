from connection import mongo_connect
from models import Author, Quote


def mongo_searcher():
    while True:
        print('''
        This script will prompt you to input commands in the format 'command:value'. Available commands are:
        - 'name:value' - Search and display quotes by author's name.
        - 'tag:value' - Search and display quotes by a specific tag.
        - 'tags:value1,value2' - Search and display quotes by multiple tags (comma-separated).
        - 'exit' - Exit the script.
        '''
              )
        command = input("Input the command: ")
        parts = command.split(':', 1)
        action = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else ''

        if action == 'name':
            author = Author.objects(fullname=value).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("Autor not found.")

        elif action == 'tag':
            quotes = Quote.objects(tags__icontains=value)
            for quote in quotes:
                print(quote.quote)

        elif action == 'tags':
            tags = value.split(',')
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                print(quote.quote)

        elif action == 'exit':
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    mongo_connect()
    mongo_searcher()
