"""
QGraphicsSceneBspTree binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_bsp_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsSceneBspTree to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QGraphicsSceneBspTree(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsSceneBspTree: a plain Python object standing
  in front of one C++ QGraphicsSceneBspTree.

  C++ hands a QGraphicsSceneBspTree around as a copy, so every C++
  QGraphicsSceneBspTree behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneBspTree that has a ritual and that
  Python can call so far, 7 names in all: 'initialize', 'clear', 'leafCount',
  'firstChildIndex', 'parentIndex', 'debug', 'rectForIndex'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneBspTree::~QGraphicsSceneBspTree()': the destructor:
    Python removes its C++ QGraphicsSceneBspTree by it, and has no other use
    for it.
  - Qt's 'void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem *>
    &items)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 3 leans on 'void QGraphicsSceneBspTree;
  1 a template.

  What to expect
  --------------

  - The C++ QGraphicsSceneBspTree is created at the first use, not by
    'QGraphicsSceneBspTree(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsSceneBspTree back gives a copy the ritual
    made for Python, in a new cute QGraphicsSceneBspTree.
  - Each name of Qt's QGraphicsSceneBspTree that has no cute function yet,
    'climbTree', 'insertItem', 'items', 'removeItem', 'removeItems', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QGraphicsSceneBspTree, each a class in here
  #  as in C++.

  class Node(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsSceneBspTree::Node: a plain Python object
    standing in front of one C++ QGraphicsSceneBspTree::Node.

    C++ hands a QGraphicsSceneBspTree::Node around as a copy, so every C++
    QGraphicsSceneBspTree::Node behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QGraphicsSceneBspTree::Node yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsSceneBspTree::Node::~Node()': the destructor: Python
      removes its C++ QGraphicsSceneBspTree::Node by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGraphicsSceneBspTree::Node is created at the first use, not by
      'QGraphicsSceneBspTree::Node(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsSceneBspTree::Node back gives a copy the
      ritual made for Python, in a new cute QGraphicsSceneBspTree::Node.
    """

    #  The enums Qt writes inside QGraphicsSceneBspTree::Node, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class Type(CuteNum):
      """
      The enum 'QGraphicsSceneBspTree::Node::Type' of Qt, with the 3 names Qt
      gives in it.
      """

      Horizontal = Kee[int](0)
      Vertical = Kee[int](1)
      Leaf = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsSceneBspTree::Node'

    #  Qt's '~QGraphicsSceneBspTree::Node()'. Naming it makes this a value
    #  class: Python owns every C++ QGraphicsSceneBspTree::Node behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QGraphicsSceneBspTree4NodeD1Ev'

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
  __qt_class__ = 'QGraphicsSceneBspTree'

  #  Qt's '~QGraphicsSceneBspTree()'. Naming it makes this a value class:
  #  Python owns every C++ QGraphicsSceneBspTree behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QGraphicsSceneBspTreeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def leafCount(self) -> int:
    """
    Calls Qt's 'int QGraphicsSceneBspTree::leafCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#leafCount
    """
    #  int QGraphicsSceneBspTree::leafCount() const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsSceneBspTree9leafCountEv',
    )

  @overload(int)
  def firstChildIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QGraphicsSceneBspTree::firstChildIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#firstChildIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QGraphicsSceneBspTree::firstChildIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsSceneBspTree15firstChildIndexEi', index,
    )

  @overload(int)
  def parentIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QGraphicsSceneBspTree::parentIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#parentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QGraphicsSceneBspTree::parentIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsSceneBspTree11parentIndexEi', index,
    )

  @overload(int)
  def debug(self, index: int) -> str:
    """
    Calls Qt's 'QString QGraphicsSceneBspTree::debug(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#debug

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsSceneBspTree::debug(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsSceneBspTree5debugEi', index,
    )

  @overload(int)
  def rectForIndex(self, index: int) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsSceneBspTree::rectForIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#rectForIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsSceneBspTree::rectForIndex(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsSceneBspTree12rectForIndexEi', index,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QGraphicsSceneBspTree::QGraphicsSceneBspTree()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#QGraphicsSceneBspTree
    """
    #  QGraphicsSceneBspTree::QGraphicsSceneBspTree()
    self._noteCreation(QGraphicsSceneBspTree, lambda: Rituals.call(
        'ritual_ZN21QGraphicsSceneBspTreeC1Ev',
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

  @overload(QRectF, int)
  def initialize(self, rect: QRectF, depth: int) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTree::initialize(const QRectF &rect,
    int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#initialize

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    depth : int
      Passed on as it is.
    """
    #  void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth)
    self.uglySide.call(
        'ritual_ZN21QGraphicsSceneBspTree10initializeERK6QRectFi',
        self._valueOf(rect), depth,
    )

  @overload(QRectF, int, int)
  def initialize(self, rect: QRectF, depth: int, index: int) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTree::initialize(const QRectF &rect,
    int depth, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#initialize

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    depth : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QGraphicsSceneBspTree::initialize(const QRectF &rect, int depth,
    #      int index)
    self.uglySide.call(
        'ritual_ZN21QGraphicsSceneBspTree10initializeERK6QRectFii',
        self._valueOf(rect), depth, index,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QGraphicsSceneBspTree::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscenebsptree.html#clear
    """
    #  void QGraphicsSceneBspTree::clear()
    self.uglySide.call('ritual_ZN21QGraphicsSceneBspTree5clearEv')

  @staticmethod
  def climbTree(*__, **_) -> Never:
    """
    Qt's 'QGraphicsSceneBspTree::climbTree': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTree.climbTree' has no cute function yet. Qt's "
        "'QGraphicsSceneBspTree::climbTree': a template: a pattern and no "
        "single function.")

  @staticmethod
  def insertItem(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTree::insertItem(QGraphicsItem *item, const
    QRectF &rect)': leans on 'void
    QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::insertItem(
    QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::
    insertItem(QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTree.insertItem' has no cute function yet. Qt's "
        "'void QGraphicsSceneBspTree::insertItem(QGraphicsItem *item, const "
        "QRectF &rect)': leans on 'void "
        "QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::insertItem("
        "QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree:"
        ":insertItem(QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def items(*__, **_) -> Never:
    """
    Qt's 'QList<QGraphicsItem *> QGraphicsSceneBspTree::items(const QRectF
    &rect, bool onlyTopLevelItems) const': leans on 'void
    QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::items(QRectF
    const&, bool)
    const::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::items(
    QRectF const&, bool) const::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF
    const&, int) const', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTree.items' has no cute function yet. Qt's "
        "'QList<QGraphicsItem *> QGraphicsSceneBspTree::items(const QRectF "
        "&rect, bool onlyTopLevelItems) const': leans on 'void "
        "QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::items(QRect"
        "F const&, bool) "
        "const::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::i"
        "tems(QRectF const&, bool) "
        "const::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def removeItem(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTree::removeItem(QGraphicsItem *item, const
    QRectF &rect)': leans on 'void
    QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::removeItem(
    QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree::
    removeItem(QGraphicsItem*, QRectF
    const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTree.removeItem' has no cute function yet. Qt's "
        "'void QGraphicsSceneBspTree::removeItem(QGraphicsItem *item, const "
        "QRectF &rect)': leans on 'void "
        "QGraphicsSceneBspTree::climbTree<QGraphicsSceneBspTree::removeItem("
        "QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}>(QGraphicsSceneBspTree:"
        ":removeItem(QGraphicsItem*, QRectF "
        "const&)::{lambda(QList<QGraphicsItem*>*)#1}&&, QRectF const&, int) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def removeItems(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem *>
    &items)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsSceneBspTree.removeItems' has no cute function yet. Qt's "
        "'void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem "
        "*> &items)': takes a type Python has no way to hand over yet.")
