FILEPATH = "content.txt"

def get_content(filepath=FILEPATH):
    """Opens the existing Todos
    1 arg which is the filepath, defaults to todos.txt
    """
    with open(filepath, "r") as file_local:
        articles_local = file_local.readlines()
    return articles_local


def write_content(articles_local, filepath=FILEPATH):
    """Writes to the existing Todos
      2 params which are a list to add to the todos file and
      the filepath which defaults to todos.txt
      """
    with open(filepath, "w") as file:
        file.writelines(articles_local)