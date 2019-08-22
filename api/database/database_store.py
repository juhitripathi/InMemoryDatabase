class DatabaseStore:

    def __init__():
        self.database = {}

    def create_collection(self, collection_name):
        if collection_name in database:
            return 'Collection already exists. Please select different name.'
        else:
            database[collection_name] = []
            return 'Collection successfully added.'

    def create_document(self, collection_name, document):
        if not collection_name in database:
            return 'Collection does not exist.'
        else:
            database[collection_name].append(document)
            return 'Document successfully added.'

    def search_store(self, collection_name, search_key, search_value):
        if not collection_name in database:
            return 'Collection does not exist.'
        else:
            search_result = [document for document in database[collection_name] if search_key in document and search_value == document[search_key]]
            return search_result

    def modify_object(self, collection_name, search_key, old_value, new_value):
        if not collection_name in database:
            return 'Collection does not exist.'
        else:
            for i in database[collection_name]
                if search_key in i and old_value == i[search_key]:
                    i[search_key] = new_value
                    continue
        return 'Document successfully updated.'

    def get_collection_size(self, collection_name):
        if not collection_name in database:
            return 'Collection does not exist.'
        else:
            return len(database[collection_name])

    def get_document_size(self, collection_name, search_key, search_value):
        if not collection_name in database:
            return 'Collection does not exist.'
        else:
            for i in database[collection_name]
                if search_key in i and search_value == i[search_key]:
                    return len(i)
