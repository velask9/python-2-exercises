from pprint import pprint
from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator
from CarCollector import CarCollector



# def ex1():
#     people_list = [
#         {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
#         {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#
#     def sort_people(lst, field, direction):
#         if direction == "asc":
#             lst.sort(key=lambda p: p[field])
#         else:
#             lst.sort(key=lambda p: p[field], reverse=True)
#
#     sort_people(people_list, 'weight', 'asc')
#     print(people_list)
#
# ex1()
#



    # def sort_people(people, field, direction):
    #     people.sort(key=lambda p: p[field], reverse=(direction == 'desc'))
    #
    # people_list = [
    #     {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
    #     {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
    #     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    # ]
    #
    # sort_people(people_list, 'weight', 'desc')
    # print(people_list)


# -------------------------------------------------------------------------
# def ex2():
#     people_list = [
#         {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#         {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#
#     def filter_males(people_list):
#         new_list = list(filter(lambda p: p['sex'] =='male', people_list))
#         return new_list
#
#
#
#
#     filtered_list = filter_males(people_list)
#     print(filtered_list)

# ----------------------------------------------------------------------------

# def ex3():
#     people_list = [
#         {'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7},
#         {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
#     ]
#
#     def calc_bmi(people_list):
#         new_people_list = list(map(lambda p: {'id': p['id'], 'name': p['name'], 'weight_kg': p['weight_kg'],
#                                               'height_meters': p['height_meters'],
#                                               'bmi': round(p['weight_kg'] / (p['height_meters'] ** 2), 1)}, people_list))
#         return new_people_list
#
#     new_people_list = calc_bmi(people_list)
#     print(new_people_list)
#


#-----------------------------------------------------------------------------------------------------------------
# def ex4():
#     people_list = [
#         {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
#         {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
#         {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
#     ]
#
#     def get_people():
#         my_list = [p['name'] for p in people_list if p['age'] >= 15]
#         return my_list
#
#     print(get_people())

# ex4()



#----------------------------------------------------------------------------------------------------------

# def ex5():
#     sentence = "This is a test of the emergency broadcast system"
#     word_counter = WordCounter(sentence)
#     print(word_counter.get_word_count())    # Returns the number of all the words.
#     print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
#     print(word_counter.get_longest_word())  # Returns the length of the longest word.
#
# ex5()
#--------------------------------------------------------------------------------------

# def ex6():
#     items = [
#         {"id": 1, "desc": "clock", "price": 1.00},
#         {"id": 2, "desc": "socks", "price": 2.00},
#         {"id": 3, "desc": "razor", "price": 3.00},
#     ]
#     tm = TaxMan(items, "10%")
#     total_with_tax = tm.get_total()
#     print(total_with_tax)
# ex6()
#----------------------------------------------------------------------------------------

# def ex7():
#
#     calculator1 = Calculator(4, 3)
#     calculator1.add()
#     print(calculator1.get_result())
#
#     calculator2 = Calculator(4, 3)
#     calculator2.sub()
#     print(calculator2.get_result())
#
#     calculator3 = Calculator(2, 3)
#     calculator3.mul()
#     print(calculator3.get_result())
#
#     calculator4 = Calculator(8, 2)
#     calculator4.div()
#     print(calculator4.get_result())
#
# ex7()

#---------------------------------------------------------------------

# def ex8():
#
#
#     print(CarCollector.get_data())
#
# ex8()