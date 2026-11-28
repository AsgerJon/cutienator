"""
QV4::SparseArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4sparsearray_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::SparseArray to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SparseArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::SparseArray: a plain Python object standing in
  front of one C++ QV4::SparseArray.

  C++ hands a QV4::SparseArray around as a copy, so every C++
  QV4::SparseArray behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::SparseArray that has a ritual and that Python
  can call so far, 20 names in all: 'rotateLeft', 'rotateRight', 'rebalance',
  'recalcMostLeftNode', 'root', 'deleteNode', 'createNode', 'freeTree',
  'findNode', 'nEntries', 'pop_front', 'push_front', 'pop_back', 'push_back',
  'end', 'begin', 'erase', 'lowerBound', 'upperBound', 'insert'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::SparseArray::~SparseArray()': the destructor: Python removes
    its C++ QV4::SparseArray by it, and has no other use for it.
  - Qt's 'QList<int> QV4::SparseArray::keys() const': gives a type Python has
    no way to take yet.
  - Qt's 'SparseArrayNode *QV4::SparseArray::end()': takes in Python what
    'const SparseArrayNode *QV4::SparseArray::end() const' takes.
  - Qt's 'SparseArrayNode *QV4::SparseArray::begin()': takes in Python what
    'const SparseArrayNode *QV4::SparseArray::begin() const' takes.
  - Qt's 'const SparseArrayNode *QV4::SparseArray::lowerBound(uint key)
    const': takes in Python what 'SparseArrayNode
    *QV4::SparseArray::lowerBound(uint key)' takes.
  - Qt's 'const SparseArrayNode *QV4::SparseArray::upperBound(uint key)
    const': takes in Python what 'SparseArrayNode
    *QV4::SparseArray::upperBound(uint key)' takes.

  What has no ritual
  ------------------

  1 of the 29 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::SparseArray is created at the first use, not by
    'QV4::SparseArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::SparseArray back gives a copy the ritual made
    for Python, in a new cute QV4::SparseArray.
  - Each name of Qt's QV4::SparseArray that has no cute function yet, 'keys',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SparseArray'

  #  Qt's '~QV4::SparseArray()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::SparseArray behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV411SparseArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def root(self) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::root() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#root

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::root() const
    address = self.uglySide.call('ritual_ZNK3QV411SparseArray4rootEv')
    return QV4.SparseArrayNode._cuteAt(address)

  @overload(int)
  def findNode(self, akey: int) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::findNode(uint akey)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#findNode

    Parameters
    ----------

    akey : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::findNode(uint akey) const
    address = self.uglySide.call(
        'ritual_ZNK3QV411SparseArray8findNodeEj', akey,
    )
    return QV4.SparseArrayNode._cuteAt(address)

  def nEntries(self) -> int:
    """
    Calls Qt's 'uint QV4::SparseArray::nEntries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#nEntries
    """
    #  uint QV4::SparseArray::nEntries() const
    return self.uglySide.call('ritual_ZNK3QV411SparseArray8nEntriesEv')

  def end(self) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'const SparseArrayNode *QV4::SparseArray::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#end

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const SparseArrayNode *QV4::SparseArray::end() const
    address = self.uglySide.call('ritual_ZNK3QV411SparseArray3endEv')
    return QV4.SparseArrayNode._cuteAt(address)

  def begin(self) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'const SparseArrayNode *QV4::SparseArray::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#begin

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const SparseArrayNode *QV4::SparseArray::begin() const
    address = self.uglySide.call('ritual_ZNK3QV411SparseArray5beginEv')
    return QV4.SparseArrayNode._cuteAt(address)

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
    Notes what was given, for Qt's 'QV4::SparseArray::SparseArray()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#SparseArray
    """
    #  QV4::SparseArray::SparseArray()
    self._noteCreation(SparseArray, lambda: Rituals.call(
        'ritual_ZN3QV411SparseArrayC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: SparseArray) -> None:
    """
    Notes what was given, for Qt's 'QV4::SparseArray::SparseArray(const
    SparseArray &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#SparseArray

    Parameters
    ----------

    other : SparseArray
      Passed on as a value: Qt reads the C++ QV4::SparseArray, which stays
      Python's own.
    """
    #  QV4::SparseArray::SparseArray(const SparseArray &other)
    self._noteCreation(SparseArray, lambda: Rituals.call(
        'ritual_ZN3QV411SparseArrayC1ERKS0_', self._valueOf(other),
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

  @overload(WAIT['QV4.SparseArrayNode'])
  @overload(NoneType)
  def rotateLeft(self, x: Optional[QV4.SparseArrayNode]) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::rotateLeft(SparseArrayNode *x)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#rotateLeft

    Parameters
    ----------

    x : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArray::rotateLeft(SparseArrayNode *x)
    self.uglySide.call(
        'ritual_ZN3QV411SparseArray10rotateLeftEPNS_15SparseArrayNodeE',
        self._addressOf(x),
    )

  @overload(WAIT['QV4.SparseArrayNode'])
  @overload(NoneType)
  def rotateRight(self, x: Optional[QV4.SparseArrayNode]) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::rotateRight(SparseArrayNode *x)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#rotateRight

    Parameters
    ----------

    x : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArray::rotateRight(SparseArrayNode *x)
    self.uglySide.call(
        'ritual_ZN3QV411SparseArray11rotateRightEPNS_15SparseArrayNodeE',
        self._addressOf(x),
    )

  @overload(WAIT['QV4.SparseArrayNode'])
  @overload(NoneType)
  def rebalance(self, x: Optional[QV4.SparseArrayNode]) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::rebalance(SparseArrayNode *x)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#rebalance

    Parameters
    ----------

    x : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArray::rebalance(SparseArrayNode *x)
    self.uglySide.call(
        'ritual_ZN3QV411SparseArray9rebalanceEPNS_15SparseArrayNodeE',
        self._addressOf(x),
    )

  def recalcMostLeftNode(self) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::recalcMostLeftNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearray.html#recalcMostLeftNode
    """
    #  void QV4::SparseArray::recalcMostLeftNode()
    self.uglySide.call('ritual_ZN3QV411SparseArray18recalcMostLeftNodeEv')

  @overload(WAIT['QV4.SparseArrayNode'])
  @overload(NoneType)
  def deleteNode(self, z: Optional[QV4.SparseArrayNode]) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::deleteNode(SparseArrayNode *z)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#deleteNode

    Parameters
    ----------

    z : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArray::deleteNode(SparseArrayNode *z)
    self.uglySide.call(
        'ritual_ZN3QV411SparseArray10deleteNodeEPNS_15SparseArrayNodeE',
        self._addressOf(z),
    )

  @overload(int, WAIT['QV4.SparseArrayNode'], bool)
  @overload(int, NoneType, bool)
  def createNode(
      self,
      sl: int,
      parent: Optional[QV4.SparseArrayNode],
      left: bool,
  ) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::createNode(uint sl,
    SparseArrayNode *parent, bool left)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#createNode

    Parameters
    ----------

    sl : int
      Passed on as it is.

    parent : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    left : bool
      Passed on as it is.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::createNode(uint sl, SparseArrayNode
    #      *parent, bool left)
    address = self.uglySide.call(
        'ritual_ZN3QV411SparseArray10createNodeEjPNS_15SparseArrayNodeEb',
        sl, self._addressOf(parent), left,
    )
    return QV4.SparseArrayNode._cuteAt(address)

  @overload(WAIT['QV4.SparseArrayNode'], int)
  @overload(NoneType, int)
  def freeTree(
      self,
      root: Optional[QV4.SparseArrayNode],
      alignment: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::freeTree(SparseArrayNode *root, int
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#freeTree

    Parameters
    ----------

    root : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : int
      Passed on as it is.
    """
    #  void QV4::SparseArray::freeTree(SparseArrayNode *root, int alignment)
    self.uglySide.call(
        'ritual_ZN3QV411SparseArray8freeTreeEPNS_15SparseArrayNodeEi',
        self._addressOf(root), alignment,
    )

  def pop_front(self) -> int:
    """
    Calls Qt's 'uint QV4::SparseArray::pop_front()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#pop_front
    """
    #  uint QV4::SparseArray::pop_front()
    return self.uglySide.call('ritual_ZN3QV411SparseArray9pop_frontEv')

  @overload(int)
  def push_front(self, at: int) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::push_front(uint at)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#push_front

    Parameters
    ----------

    at : int
      Passed on as it is.
    """
    #  void QV4::SparseArray::push_front(uint at)
    self.uglySide.call('ritual_ZN3QV411SparseArray10push_frontEj', at)

  @overload(int)
  def pop_back(self, len: int) -> int:
    """
    Calls Qt's 'uint QV4::SparseArray::pop_back(uint len)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#pop_back

    Parameters
    ----------

    len : int
      Passed on as it is.
    """
    #  uint QV4::SparseArray::pop_back(uint len)
    return self.uglySide.call('ritual_ZN3QV411SparseArray8pop_backEj', len)

  @overload(int, int)
  def push_back(self, at: int, len: int) -> None:
    """
    Calls Qt's 'void QV4::SparseArray::push_back(uint at, uint len)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#push_back

    Parameters
    ----------

    at : int
      Passed on as it is.

    len : int
      Passed on as it is.
    """
    #  void QV4::SparseArray::push_back(uint at, uint len)
    self.uglySide.call('ritual_ZN3QV411SparseArray9push_backEjj', at, len)

  @overload(WAIT['QV4.SparseArrayNode'])
  @overload(NoneType)
  def erase(
      self,
      n: Optional[QV4.SparseArrayNode],
  ) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::erase(SparseArrayNode
    *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#erase

    Parameters
    ----------

    n : Optional[QV4.SparseArrayNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::erase(SparseArrayNode *n)
    address = self.uglySide.call(
        'ritual_ZN3QV411SparseArray5eraseEPNS_15SparseArrayNodeE',
        self._addressOf(n),
    )
    return QV4.SparseArrayNode._cuteAt(address)

  @overload(int)
  def lowerBound(self, key: int) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::lowerBound(uint key)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#lowerBound

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::lowerBound(uint key)
    address = self.uglySide.call(
        'ritual_ZN3QV411SparseArray10lowerBoundEj', key,
    )
    return QV4.SparseArrayNode._cuteAt(address)

  @overload(int)
  def upperBound(self, key: int) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::upperBound(uint key)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#upperBound

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::upperBound(uint key)
    address = self.uglySide.call(
        'ritual_ZN3QV411SparseArray10upperBoundEj', key,
    )
    return QV4.SparseArrayNode._cuteAt(address)

  @overload(int)
  def insert(self, akey: int) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::SparseArray::insert(uint akey)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearray.html#insert

    Parameters
    ----------

    akey : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::SparseArray::insert(uint akey)
    address = self.uglySide.call('ritual_ZN3QV411SparseArray6insertEj', akey)
    return QV4.SparseArrayNode._cuteAt(address)

  @staticmethod
  def keys(*__, **_) -> Never:
    """
    Qt's 'QList<int> QV4::SparseArray::keys() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.SparseArray.keys' has no cute function yet. Qt's 'QList<int> "
        "QV4::SparseArray::keys() const': gives a type Python has no way to "
        "take yet.")
