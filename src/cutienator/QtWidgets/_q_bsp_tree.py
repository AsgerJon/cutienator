"""
QBspTree binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QBspTree to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QBspTree(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBspTree: a plain Python object standing in front of
  one C++ QBspTree.

  C++ hands a QBspTree around as a copy, so every C++ QBspTree behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBspTree that has a ritual and that Python can call
  so far, 7 names in all: 'create', 'destroy', 'leafCount', 'insertLeaf',
  'removeLeaf', 'parentIndex', 'firstChildIndex'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QBspTree::init(const QRect &area, NodeType type)': names the
    enum 'QBspTree::Node::Type', whose class cannot be named here.
  - Qt's 'void QBspTree::climbTree(const QRect &rect, callback *function,
    QBspTreeData data)': names 'QBspTree::callback', which has no cute class
    yet.
  - Qt's 'QList<int> &QBspTree::leaf(int i)': gives a type Python has no way
    to take yet.
  - Qt's 'void QBspTree::init(const QRect &area, int depth, NodeType type,
    int index)': names the enum 'QBspTree::Node::Type', whose class cannot be
    named here.
  - Qt's 'void QBspTree::climbTree(const QRect &rect, callback *function,
    QBspTreeData data, int index)': names 'QBspTree::callback', which has no
    cute class yet.
  - Qt's 'void QBspTree::insert(QList<int> &leaf, const QRect &area, uint
    visited, QBspTreeData data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QBspTree::remove(QList<int> &leaf, const QRect &area, uint
    visited, QBspTreeData data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QBspTree::~QBspTree()': the destructor: Python removes its C++
    QBspTree by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QBspTree is created at the first use, not by 'QBspTree(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBspTree back gives a copy the ritual made for
    Python, in a new cute QBspTree.
  - Each name of Qt's QBspTree that has no cute function yet, 'climbTree',
    'init', 'insert', 'leaf', 'remove', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QBspTree, each a class in here as in C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBspTree::Data: a plain Python object standing in
    front of one C++ QBspTree::Data.

    C++ hands a QBspTree::Data around as a copy, so every C++ QBspTree::Data
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QBspTree::Data yet. It can be made from Python, in 1
    way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBspTree::Data::Data(void *p)': names 'void', which has no cute
      class yet.
    - Qt's 'QBspTree::Data::~Data()': the destructor: Python removes its C++
      QBspTree::Data by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QBspTree::Data is created at the first use, not by
      'QBspTree::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBspTree::Data back gives a copy the ritual made
      for Python, in a new cute QBspTree::Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBspTree::Data'

    #  Qt's '~QBspTree::Data()'. Naming it makes this a value class: Python
    #  owns every C++ QBspTree::Data behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN8QBspTree4DataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def __init__(self, n: int) -> None:
      """
      Notes what was given, for Qt's 'QBspTree::Data::Data(int n)', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qbsptree-data.html#Data

      Parameters
      ----------

      n : int
        Passed on as it is.
      """
      #  QBspTree::Data::Data(int n)
      self._noteCreation(QBspTree.Data, lambda: Rituals.call(
          'ritual_ZN8QBspTree4DataC1Ei', n,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Node(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBspTree::Node: a plain Python object standing in
    front of one C++ QBspTree::Node.

    C++ hands a QBspTree::Node around as a copy, so every C++ QBspTree::Node
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QBspTree::Node yet. It can be made from Python, in 1
    way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBspTree::Node::~Node()': the destructor: Python removes its C++
      QBspTree::Node by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QBspTree::Node is created at the first use, not by
      'QBspTree::Node(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBspTree::Node back gives a copy the ritual made
      for Python, in a new cute QBspTree::Node.
    """

    #  The enums Qt writes inside QBspTree::Node, each a class in here as in
    #  C++, and the names Qt has for the combinations of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QBspTree::Node::Type' of Qt, with the 4 names Qt gives in it.
      """

      NULL = Kee[int](0)
      VerticalPlane = Kee[int](1)
      HorizontalPlane = Kee[int](2)
      Both = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBspTree::Node'

    #  Qt's '~QBspTree::Node()'. Naming it makes this a value class: Python
    #  owns every C++ QBspTree::Node behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN8QBspTree4NodeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QBspTree::Node::Node()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qbsptree-node.html#Node
      """
      #  QBspTree::Node::Node()
      self._noteCreation(QBspTree.Node, lambda: Rituals.call(
          'ritual_ZN8QBspTree4NodeC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBspTree'

  #  Qt's '~QBspTree()'. Naming it makes this a value class: Python owns
  #  every C++ QBspTree behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QBspTreeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def leafCount(self) -> int:
    """
    Calls Qt's 'int QBspTree::leafCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#leafCount
    """
    #  int QBspTree::leafCount() const
    return self.uglySide.call('ritual_ZNK8QBspTree9leafCountEv')

  @overload(int)
  def parentIndex(self, i: int) -> int:
    """
    Calls Qt's 'int QBspTree::parentIndex(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#parentIndex

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QBspTree::parentIndex(int i) const
    return self.uglySide.call('ritual_ZNK8QBspTree11parentIndexEi', i)

  @overload(int)
  def firstChildIndex(self, i: int) -> int:
    """
    Calls Qt's 'int QBspTree::firstChildIndex(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#firstChildIndex

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QBspTree::firstChildIndex(int i) const
    return self.uglySide.call('ritual_ZNK8QBspTree15firstChildIndexEi', i)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QBspTree::QBspTree()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#QBspTree
    """
    #  QBspTree::QBspTree()
    self._noteCreation(QBspTree, lambda: Rituals.call(
        'ritual_ZN8QBspTreeC1Ev',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, int)
  def create(self, n: int, d: int = -1) -> None:
    """
    Calls Qt's 'void QBspTree::create(int n, int d)'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#create

    Parameters
    ----------

    n : int
      Passed on as it is.

    d : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QBspTree::create(int n, int d)
    self.uglySide.call('ritual_ZN8QBspTree6createEii', n, d)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QBspTree::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#destroy
    """
    #  void QBspTree::destroy()
    self.uglySide.call('ritual_ZN8QBspTree7destroyEv')

  @overload(QRect, int)
  def insertLeaf(self, r: QRect, i: int) -> None:
    """
    Calls Qt's 'void QBspTree::insertLeaf(const QRect &r, int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#insertLeaf

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    i : int
      Passed on as it is.
    """
    #  void QBspTree::insertLeaf(const QRect &r, int i)
    self.uglySide.call(
        'ritual_ZN8QBspTree10insertLeafERK5QRecti', self._valueOf(r), i,
    )

  @overload(QRect, int)
  def removeLeaf(self, r: QRect, i: int) -> None:
    """
    Calls Qt's 'void QBspTree::removeLeaf(const QRect &r, int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbsptree.html#removeLeaf

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    i : int
      Passed on as it is.
    """
    #  void QBspTree::removeLeaf(const QRect &r, int i)
    self.uglySide.call(
        'ritual_ZN8QBspTree10removeLeafERK5QRecti', self._valueOf(r), i,
    )

  @staticmethod
  def climbTree(*__, **_) -> Never:
    """
    - Qt's 'void QBspTree::climbTree(const QRect &rect, callback *function,
      QBspTreeData data)': names 'QBspTree::callback', which has no cute
      class yet.
    - Qt's 'void QBspTree::climbTree(const QRect &rect, callback *function,
      QBspTreeData data, int index)': names 'QBspTree::callback', which has
      no cute class yet.
    """
    raise NotImplementedError(
        "'QBspTree.climbTree' has no cute function yet. Qt's 'void "
        "QBspTree::climbTree(const QRect &rect, callback *function, "
        "QBspTreeData data)': names 'QBspTree::callback', which has no cute "
        "class yet. Qt's 'void QBspTree::climbTree(const QRect &rect, "
        "callback *function, QBspTreeData data, int index)': names "
        "'QBspTree::callback', which has no cute class yet.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    - Qt's 'void QBspTree::init(const QRect &area, NodeType type)': names the
      enum 'QBspTree::Node::Type', whose class cannot be named here.
    - Qt's 'void QBspTree::init(const QRect &area, int depth, NodeType type,
      int index)': names the enum 'QBspTree::Node::Type', whose class cannot
      be named here.
    """
    raise NotImplementedError(
        "'QBspTree.init' has no cute function yet. Qt's 'void "
        "QBspTree::init(const QRect &area, NodeType type)': names the enum "
        "'QBspTree::Node::Type', whose class cannot be named here. Qt's "
        "'void QBspTree::init(const QRect &area, int depth, NodeType type, "
        "int index)': names the enum 'QBspTree::Node::Type', whose class "
        "cannot be named here.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'void QBspTree::insert(QList<int> &leaf, const QRect &area, uint
    visited, QBspTreeData data)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QBspTree.insert' has no cute function yet. Qt's 'void "
        "QBspTree::insert(QList<int> &leaf, const QRect &area, uint "
        "visited, QBspTreeData data)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def leaf(*__, **_) -> Never:
    """
    Qt's 'QList<int> &QBspTree::leaf(int i)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QBspTree.leaf' has no cute function yet. Qt's 'QList<int> "
        "&QBspTree::leaf(int i)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'void QBspTree::remove(QList<int> &leaf, const QRect &area, uint
    visited, QBspTreeData data)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QBspTree.remove' has no cute function yet. Qt's 'void "
        "QBspTree::remove(QList<int> &leaf, const QRect &area, uint "
        "visited, QBspTreeData data)': takes a type Python has no way to "
        "hand over yet.")
