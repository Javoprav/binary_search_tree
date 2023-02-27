from src.binary_serch_tree import BinarySearchTree
import pytest

@pytest.fixture
def bst():
  bst = BinarySearchTree()
  bst.insert({'id': 40})
  return bst


@pytest.fixture
def bst_full():
  bst = BinarySearchTree()
  bst.insert({'id': 40})
  bst.insert({'id': 30})
  bst.insert({'id': 25})
  bst.insert({'id': 35})
  bst.insert({'id': 50})
  bst.insert({'id': 45})
  bst.insert({'id': 60})
  return bst