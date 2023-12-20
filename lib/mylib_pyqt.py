# Select specific Item
def select_list(liste,index):
        try:
                if index >=0:
                        liste.setCurrentItem(liste.item(index))
                else:
                        liste.setCurrentItem(liste.item(liste.count()+index))
        except:
                pass
def setSelectedByText_list(liste,text): select_list(liste,indexOfText_list(liste,text))
def setSelectedFirstItem_list(liste): select_list(liste, 0)
def setSelectedLastItem_list(liste): select_list(liste, -1)



# Get Index
def indexOfSelected_list(liste): 
        try:
                return indexOfItem_list(liste,liste.selectedItems()[0])
        except:
                pass
        return False
def indexOfItem_list(liste,item):
        found = False
        for x in range(0,liste.count()):
                if not found and liste.item(x) == item: 
                        found=x
        return found

def indexOfText_list(liste,text):
        try:
                a = itemTexts_list(liste)
                for x in range(0,len(a)):
                        if text == a[x]:
                                return x
        except:
                pass
        return False



# Get List Children
def itemTexts_list(liste): return [x.text() for x in items_list(liste)]
def items_list(liste): return [liste.item(x) for x in range(0,liste.count())]



# Remove
def removeItem_list(liste,item):
       # try:
                saveItems = [x.text() for x in items_list(liste) if x != item]
                liste.clear()
                for x in saveItems: 
                        liste.addItem(x)
      #  except:
            #    pass

def removeSelected_list(liste): removeItem_list(liste,liste.selectedItems()[0])

def removeItemPreserveSelection_list(liste,item): # Tries to preserve the selected Item 
        try:
                selIndex = indexOfSelected_list(liste)
                remIndex = indexOfItem_list(liste,item)
                removeItem_list(liste,item)
                if selIndex != remIndex: liste.setCurrentItem(liste.item(selIndex))
        except:
                pass


def getTextOfSelected_list(liste):
        try:
            return liste.selectedItems()[0].text()
        except:
            return ""

