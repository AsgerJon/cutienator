"""
QDomNodeList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomNode, QDomNodeListPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNodeListPrivate = WAIT['QDomNodeListPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNodeList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNodeList: a plain Python object standing in front
  of one C++ QDomNodeList.

  C++ hands a QDomNodeList around as a copy, so every C++ QDomNodeList behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNodeList that has a ritual and that Python can
  call so far, 9 names in all: 'item', 'at', 'length', 'count', 'size',
  'isEmpty', '__eq__', '__ne__', 'noexceptLength'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNodeList &QDomNodeList::operator=(const QDomNodeList &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomNodeList::~QDomNodeList()': the destructor: Python removes its
    C++ QDomNodeList by it, and has no other use for it.
  - Qt's 'const_iterator QDomNodeList::begin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QDomNodeList::end() const': gives a type Python has
    no way to take yet.
  - Qt's 'const_iterator QDomNodeList::cbegin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QDomNodeList::cend() const': gives a type Python has
    no way to take yet.
  - Qt's 'const_reverse_iterator QDomNodeList::rbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QDomNodeList::rend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QDomNodeList::crbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QDomNodeList::crend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QDomNodeList::constBegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QDomNodeList::constEnd() const': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QDomNodeList is created at the first use, not by
    'QDomNodeList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNodeList back gives a copy the ritual made for
    Python, in a new cute QDomNodeList.
  - Each name of Qt's QDomNodeList that has no cute function yet, 'begin',
    'cbegin', 'cend', 'constBegin', 'constEnd', 'crbegin', 'crend', 'end',
    'rbegin', 'rend', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNodeList'

  #  Qt's '~QDomNodeList()'. Naming it makes this a value class: Python owns
  #  every C++ QDomNodeList behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDomNodeListD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def item(self, index: int) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNodeList::item(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#item

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNodeList::item(int index) const
    address = self.uglySide.call('ritual_ZNK12QDomNodeList4itemEi', index)
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  @overload(int)
  def at(self, index: int) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNodeList::at(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNodeList::at(int index) const
    address = self.uglySide.call('ritual_ZNK12QDomNodeList2atEi', index)
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  def length(self) -> int:
    """
    Calls Qt's 'int QDomNodeList::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#length
    """
    #  int QDomNodeList::length() const
    return self.uglySide.call('ritual_ZNK12QDomNodeList6lengthEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QDomNodeList::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#count
    """
    #  int QDomNodeList::count() const
    return self.uglySide.call('ritual_ZNK12QDomNodeList5countEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QDomNodeList::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#size
    """
    #  int QDomNodeList::size() const
    return self.uglySide.call('ritual_ZNK12QDomNodeList4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QDomNodeList::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#isEmpty
    """
    #  bool QDomNodeList::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QDomNodeList7isEmptyEv')

  def noexceptLength(self) -> int:
    """
    Calls Qt's 'int QDomNodeList::noexceptLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#noexceptLength
    """
    #  int QDomNodeList::noexceptLength() const
    return self.uglySide.call('ritual_ZNK12QDomNodeList14noexceptLengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QDomNodeList) -> bool:
    """
    Calls Qt's 'bool operator==(const QDomNodeList &lhs, const QDomNodeList
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#operator==

    Parameters
    ----------

    rhs : QDomNodeList
      Passed on as a value: Qt reads the C++ QDomNodeList, which stays
      Python's own.
    """
    #  bool operator==(const QDomNodeList &lhs, const QDomNodeList &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QDomNodeListS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QDomNodeList) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDomNodeList &lhs, const QDomNodeList
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#operator!=

    Parameters
    ----------

    rhs : QDomNodeList
      Passed on as a value: Qt reads the C++ QDomNodeList, which stays
      Python's own.
    """
    #  bool operator!=(const QDomNodeList &lhs, const QDomNodeList &rhs)
    return Rituals.call(
        'ritual_ZneRK12QDomNodeListS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDomNodeList::QDomNodeList()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#QDomNodeList
    """
    #  QDomNodeList::QDomNodeList()
    self._noteCreation(QDomNodeList, lambda: Rituals.call(
        'ritual_ZN12QDomNodeListC1Ev',
    ))

  @overload(THIS)
  def __init__(self, nodeList: QDomNodeList) -> None:
    """
    Notes what was given, for Qt's 'QDomNodeList::QDomNodeList(const
    QDomNodeList &nodeList)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#QDomNodeList

    Parameters
    ----------

    nodeList : QDomNodeList
      Passed on as a value: Qt reads the C++ QDomNodeList, which stays
      Python's own.
    """
    #  QDomNodeList::QDomNodeList(const QDomNodeList &nodeList)
    self._noteCreation(QDomNodeList, lambda: Rituals.call(
        'ritual_ZN12QDomNodeListC1ERKS_', self._valueOf(nodeList),
    ))

  @overload(QDomNodeListPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNodeListPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodeList::QDomNodeList(QDomNodeListPrivate *a0)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelist.html#QDomNodeList

    Parameters
    ----------

    a0 : Optional[QDomNodeListPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNodeList::QDomNodeList(QDomNodeListPrivate *a0)
    self._noteCreation(QDomNodeList, lambda: Rituals.call(
        'ritual_ZN12QDomNodeListC1EP19QDomNodeListPrivate',
        self._addressOf(a0),
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

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::begin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.begin' has no cute function yet. Qt's "
        "'const_iterator QDomNodeList::begin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::cbegin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.cbegin' has no cute function yet. Qt's "
        "'const_iterator QDomNodeList::cbegin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::cend() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.cend' has no cute function yet. Qt's 'const_iterator "
        "QDomNodeList::cend() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::constBegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.constBegin' has no cute function yet. Qt's "
        "'const_iterator QDomNodeList::constBegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::constEnd() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.constEnd' has no cute function yet. Qt's "
        "'const_iterator QDomNodeList::constEnd() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QDomNodeList::crbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QDomNodeList::crbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QDomNodeList::crend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QDomNodeList::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QDomNodeList::end() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.end' has no cute function yet. Qt's 'const_iterator "
        "QDomNodeList::end() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QDomNodeList::rbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QDomNodeList::rbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QDomNodeList::rend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDomNodeList.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator QDomNodeList::rend() const': gives a type "
        "Python has no way to take yet.")
