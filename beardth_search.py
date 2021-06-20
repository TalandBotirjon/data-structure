
"""
+ Salom hammaga!
+ Bu faylda graflardan bir tomonlama bog'liq odamlarni bilan bog'lanishni topishni ko'rib chiqamiz.
+ Avvaliga collections methodidan deque metodini import qilib olamiz.
+ So'ngra breadth_search nomli funksiya yaratamiz.
+ Bu funksiyaga qiymat qilib graf, start_node va targetlarni kiritamiz.
+ Graf bu bir tomonlama bog'langan graf yani lug'at.
+ start_node biz shu insonga bog'liq insonlarni ko'rib chiqamiz.
+ target esa start_nodega bog'liq yoki yo'qligini tekshirayotgan inson.
"""
"""
+ Hello everyone!
+ In this file, we’ll look at finding links to one-way related people from graphs.
+ First we import the deque method from the collections method.
+ Then we create a function called breadth_search.
+ We enter a graph, start_node, and targets as values for this function.
+ A graph is a one-way connected graph.
+ start_node we will look at the people connected to this person.
+ target is the person checking whether it depends on start_node.
"""
"""
+ Всем привет!
+ В этом файле мы будем искать ссылки на односторонне связанных людей из графиков.
+ Сначала мы импортируем метод deque из метода коллекций.
+ Затем мы создаем функцию под названием widthth_search.
+ Мы вводим график, start_node и цели как значения для этой функции.
+ Граф - это односторонне связный граф.
+ start_node посмотрим на людей, связанных с этим человеком.
+ target - это человек, проверяющий, зависит ли это от start_node.
"""


from collections import deque   # -- pip install collections 

def breadth_search ( graph, start_node, target ):
  """The entered graph checks whether there is a path from the start_node to the target."""
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person ==target:
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


if __name__ == "__main__":
    graph = {
        'hasan':['ali', 'vali', 'tohir', 'qodir'],
        'ali':['aziza', 'olim', 'zokir', 'shokir'],
        'vali':['botir', 'ziyoda', 'shaxzod'],
        'tohir':['malik', 'mohir', 'mashrab'],
        'olim':['ochil', 'ozod', 'baxrom'],
        'aziza':['akobir', 'alisher'],
        'botir':['aziza', 'akobir', 'mashrab', 'shaxzod', 'ummat', 'farxod'],
        'ziyoda':['aziza', 'qodir'],
        'ummat':['botir', 'farxod', 'maruf', 'baxrom'],
        'mohir':['zokir', 'bekali', 'qurbonmurod']
    }
    print( breadth_search(graph, 'botir', 'baxrom'))
    
    
 "I love Uzbekistan :)"   
   
