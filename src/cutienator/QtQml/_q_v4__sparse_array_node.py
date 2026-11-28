"""
QV4::SparseArrayNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::SparseArrayNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SparseArrayNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::SparseArrayNode: a plain Python object standing
  in front of one C++ QV4::SparseArrayNode.

  C++ hands a QV4::SparseArrayNode around as a copy, so every C++
  QV4::SparseArrayNode behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::SparseArrayNode that has a ritual and that
  Python can call so far, 10 names in all: 'nextNode', 'previousNode',
  'color', 'setColor', 'parent', 'setParent', 'key', 'copy', 'lowerBound',
  'upperBound'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SparseArrayNode *QV4::SparseArrayNode::nextNode()': takes in Python
    what 'const SparseArrayNode *QV4::SparseArrayNode::nextNode() const'
    takes.
  - Qt's 'SparseArrayNode *QV4::SparseArrayNode::previousNode()': takes in
    Python what 'const SparseArrayNode *QV4::SparseArrayNode::previousNode()
    const' takes.
  - Qt's 'QV4::SparseArrayNode::~SparseArrayNode()': the destructor: Python
    removes its C++ QV4::SparseArrayNode by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::SparseArrayNode is created at the first use, not by
    'QV4::SparseArrayNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::SparseArrayNode back gives a copy the ritual
    made for Python, in a new cute QV4::SparseArrayNode.
  """

  #  The enums Qt writes inside QV4::SparseArrayNode, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Color(CuteNum):
    """
    The enum 'QV4::SparseArrayNode::Color' of Qt, with the 2 names Qt gives
    in it.
    """

    Red = Kee[int](0)
    Black = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SparseArrayNode'

  #  Qt's '~QV4::SparseArrayNode()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::SparseArrayNode behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV415SparseArrayNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nextNode(self) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'const SparseArrayNode *QV4::SparseArrayNode::nextNode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#nextNode

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const SparseArrayNode *QV4::SparseArrayNode::nextNode() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415SparseArrayNode8nextNodeEv',
    )
    return SparseArrayNode._cuteAt(address)

  def previousNode(self) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'const SparseArrayNode *QV4::SparseArrayNode::previousNode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraynode.html#previousNode

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const SparseArrayNode *QV4::SparseArrayNode::previousNode() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415SparseArrayNode12previousNodeEv',
    )
    return SparseArrayNode._cuteAt(address)

  def color(self) -> Color:
    """
    Calls Qt's 'Color QV4::SparseArrayNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#color

    Returns
    -------

    Color
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Color(number)' gives.
    """
    #  Color QV4::SparseArrayNode::color() const
    return SparseArrayNode.Color(self.uglySide.call(
        'ritual_ZNK3QV415SparseArrayNode5colorEv',
    ))

  def parent(self) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArrayNode::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#parent

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArrayNode::parent() const
    address = self.uglySide.call('ritual_ZNK3QV415SparseArrayNode6parentEv')
    return SparseArrayNode._cuteAt(address)

  def key(self) -> int:
    """
    Calls Qt's 'uint QV4::SparseArrayNode::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#key
    """
    #  uint QV4::SparseArrayNode::key() const
    return self.uglySide.call('ritual_ZNK3QV415SparseArrayNode3keyEv')

  @overload(WAIT['QV4.SparseArray'])
  @overload(NoneType)
  def copy(self, d: Optional[QV4.SparseArray]) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArrayNode::copy(SparseArray *d)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#copy

    Parameters
    ----------

    d : Optional[QV4.SparseArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArrayNode::copy(SparseArray *d) const
    address = self.uglySide.call(
        'ritual_ZNK3QV415SparseArrayNode4copyEPNS_11SparseArrayE',
        self._addressOf(d),
    )
    return SparseArrayNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Color)
  def setColor(self, c: Color) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayNode::setColor(Color c)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#setColor

    Parameters
    ----------

    c : Color
      Passed on as its number.
    """
    #  void QV4::SparseArrayNode::setColor(Color c)
    self.uglySide.call(
        'ritual_ZN3QV415SparseArrayNode8setColorENS0_5ColorE', c.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, pp: Optional[SparseArrayNode]) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayNode::setParent(SparseArrayNode *pp)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraynode.html#setParent

    Parameters
    ----------

    pp : Optional[SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArrayNode::setParent(SparseArrayNode *pp)
    self.uglySide.call(
        'ritual_ZN3QV415SparseArrayNode9setParentEPS0_', self._addressOf(pp),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def lowerBound(self, key: int) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArrayNode::lowerBound(uint key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraynode.html#lowerBound

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArrayNode::lowerBound(uint key)
    address = self.uglySide.call(
        'ritual_ZN3QV415SparseArrayNode10lowerBoundEj', key,
    )
    return SparseArrayNode._cuteAt(address)

  @overload(int)
  def upperBound(self, key: int) -> Optional[SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArrayNode::upperBound(uint key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraynode.html#upperBound

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    Optional[SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArrayNode::upperBound(uint key)
    address = self.uglySide.call(
        'ritual_ZN3QV415SparseArrayNode10upperBoundEj', key,
    )
    return SparseArrayNode._cuteAt(address)
