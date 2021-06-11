import nltk

class Utils:
    @staticmethod
    def traverse_nltk_tree(user_input):
        cont = []
        current = []
        for i in user_input:
            
            if type(i) == nltk.Tree:
                current.append(" ".join([token for token, pos in i.leaves()]))
            if current:
                entity = " ".join(current)
                if entity not in cont:
                    cont.append(entity)
                    current = []
            else:
                continue
            return cont
        Debug.info("FOUND BIRTH MONTH - {}".format(birth_month))
