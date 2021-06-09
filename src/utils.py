from debug import Debug
import nltk
class Utils:
    @staticmethod
    def traverse_nltk_tree(nltk_tree):
        for subtree in nltk_tree.subtrees():
            if type(subtree) == nltk.tree.Tree:
                Debug.info("{} has a type of {}".format(subtree, type(subtree)))
                traverse_nltk_tree(subtree)
