def increasingnumbers(numbers,True)
    counter = 0
    for i in numbers:
       counter += 1
       if counter == len(numbers) -1 
           break
       if i[counter] < i[counter + 1] and i[counter] > i[counter - 1]:
           return true
        elif i[counter] > i[counter +1] and i[counter] < i[counter - 1]:
            if increasingnumbers([],True):
                increasingnumbers = False
                numbers.remove(i[counter])
            else:
                return False
        elif i[-1] < i[-2]:
            if increasingnumbers([],True):
                numbers.remove(i[counter])
                increasingnumbers(numbers,False) 
            else:
                return False
        elif i[0] > i[1]:
            if  increasingnumbers([],True):
                numbers.remove(i[counter])
                increasingnumbers(numbers,False)
            else:
                return False
            
increasingnumbers([7,8,9,12,10],)
increasingnumbers([7,8,10,12,9],)
increasingnumbers([10,7,8,10],)
