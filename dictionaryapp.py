#forgive me for the mess with the comments
#program by mambo zulu ....
outer_list = []
tuples_list = []

n = eval (input("how many product are you entering: "))

for i in range (n):
    inner_list = []
#making list of lists
    for j in range (1):
        prod_name = input ("Product name: ")
        prod_price = eval (input("product price: "))
        inner_list.append(prod_name)#will be used as dict_key
        inner_list.append(prod_price)#will be used as dict_val
    outer_list.append(inner_list)

for item in outer_list:
    tupelised_item = tuple(item)#converting inner lists to tuples
    tuples_list.append(tupelised_item)

prod_dict = dict (tuples_list) #converting tuples to dictionary
print (prod_dict)# dictionary that stores  
                 # the prod_name as key and prod_price as dict_val
