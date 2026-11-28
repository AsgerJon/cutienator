"""
QtPrivate::BindingStatusOrList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QtPrivate::BindingStatusOrList to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBindingStatus, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBindingStatus = WAIT['QBindingStatus']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BindingStatusOrList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::BindingStatusOrList: a plain Python object
  standing in front of one C++ QtPrivate::BindingStatusOrList.

  What exists
  -----------

  Every function of Qt's QtPrivate::BindingStatusOrList that has a ritual and
  that Python can call so far, 8 names in all:
  'addObjectUnlessAlreadyStatus', 'removeObject', 'setStatusAndClearList',
  'isBindingStatus', 'isList', 'isNull', 'bindingStatus',
  'encodeBindingStatus'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::BindingStatusOrList::BindingStatusOrList(List *list)':
    names 'QtPrivate::BindingStatusOrList::List', which has no cute class
    yet.
  - Qt's 'QtPrivate::BindingStatusOrList::~BindingStatusOrList()': the
    destructor: Python never removes a C++ QtPrivate::BindingStatusOrList.
  - Qt's 'List *QtPrivate::BindingStatusOrList::list() const': gives
    'std::vector<QObject *>', which has no cute class yet.
  - Qt's 'List *QtPrivate::BindingStatusOrList::decodeList(quintptr ptr)':
    gives 'std::vector<QObject *>', which has no cute class yet.
  - Qt's 'quintptr QtPrivate::BindingStatusOrList::encodeList(List *list)':
    names 'QtPrivate::BindingStatusOrList::List', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QtPrivate::BindingStatusOrList is created at the first use, not
    by 'QtPrivate::BindingStatusOrList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::BindingStatusOrList.
  - Each name of Qt's QtPrivate::BindingStatusOrList that has no cute
    function yet, 'decodeList', 'encodeList', 'list', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def isBindingStatus(data: int) -> bool:
    """
    Calls Qt's 'bool QtPrivate::BindingStatusOrList::isBindingStatus(quintptr
    data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html#isBindingStatus

    Parameters
    ----------

    data : int
      Passed on as it is.
    """
    #  bool QtPrivate::BindingStatusOrList::isBindingStatus(quintptr data)
    return Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList15isBindingStatusEy', data,
    )

  @staticmethod
  @overload(int)
  def isList(data: int) -> bool:
    """
    Calls Qt's 'bool QtPrivate::BindingStatusOrList::isList(quintptr data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html#isList

    Parameters
    ----------

    data : int
      Passed on as it is.
    """
    #  bool QtPrivate::BindingStatusOrList::isList(quintptr data)
    return Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList6isListEy', data,
    )

  @staticmethod
  @overload(int)
  def isNull(data: int) -> bool:
    """
    Calls Qt's 'bool QtPrivate::BindingStatusOrList::isNull(quintptr data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html#isNull

    Parameters
    ----------

    data : int
      Passed on as it is.
    """
    #  bool QtPrivate::BindingStatusOrList::isNull(quintptr data)
    return Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList6isNullEy', data,
    )

  @staticmethod
  @overload(QBindingStatus)
  @overload(NoneType)
  def encodeBindingStatus(status: Optional[QBindingStatus]) -> int:
    """
    Calls Qt's 'quintptr
    QtPrivate::BindingStatusOrList::encodeBindingStatus(QBindingStatus
    *status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html

    Parameters
    ----------

    status : Optional[QBindingStatus]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quintptr
    #      QtPrivate::BindingStatusOrList::encodeBindingStatus(QBindingStatus
    #      *status)
    return Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList19encodeBindingStatusEP14Q'
        'BindingStatus',
        CuteMixin._addressOf(status),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::BindingStatusOrList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bindingStatus(self) -> Optional[QBindingStatus]:
    """
    Calls Qt's 'QBindingStatus
    *QtPrivate::BindingStatusOrList::bindingStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html#bindingStatus

    Returns
    -------

    Optional[QBindingStatus]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBindingStatus *QtPrivate::BindingStatusOrList::bindingStatus() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate19BindingStatusOrList13bindingStatusEv',
    )
    from . import QBindingStatus
    return QBindingStatus._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBindingStatus)
  @overload(NoneType)
  def setStatusAndClearList(self, status: Optional[QBindingStatus]) -> None:
    """
    Calls Qt's 'void
    QtPrivate::BindingStatusOrList::setStatusAndClearList(QBindingStatus
    *status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html

    Parameters
    ----------

    status : Optional[QBindingStatus]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::BindingStatusOrList::setStatusAndClearList(
    #      QBindingStatus *status)
    self.uglySide.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList21setStatusAndClearListEP1'
        '4QBindingStatus',
        self._addressOf(status),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::BindingStatusOrList::BindingStatusOrList()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html
    """
    #  QtPrivate::BindingStatusOrList::BindingStatusOrList()
    self._noteCreation(BindingStatusOrList, lambda: Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrListC1Ev',
    ))

  @overload(QBindingStatus)
  @overload(NoneType)
  def __init__(self, status: Optional[QBindingStatus]) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::BindingStatusOrList::BindingStatusOrList(QBindingStatus
    *status)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html

    Parameters
    ----------

    status : Optional[QBindingStatus]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtPrivate::BindingStatusOrList::BindingStatusOrList(QBindingStatus
    #      *status)
    self._noteCreation(BindingStatusOrList, lambda: Rituals.call(
        'ritual_ZN9QtPrivate19BindingStatusOrListC1EP14QBindingStatus',
        self._addressOf(status),
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

  @overload(QObject)
  @overload(NoneType)
  def addObjectUnlessAlreadyStatus(
      self,
      object: Optional[QObject],
  ) -> Optional[QBindingStatus]:
    """
    Calls Qt's 'QBindingStatus
    *QtPrivate::BindingStatusOrList::addObjectUnlessAlreadyStatus(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBindingStatus]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBindingStatus
    #      *QtPrivate::BindingStatusOrList::addObjectUnlessAlreadyStatus(
    #      QObject *object)
    address = self.uglySide.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList28addObjectUnlessAlreadySt'
        'atusEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QBindingStatus
    return QBindingStatus._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def removeObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QtPrivate::BindingStatusOrList::removeObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-bindingstatusorlist.html#removeObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::BindingStatusOrList::removeObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN9QtPrivate19BindingStatusOrList12removeObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @staticmethod
  def decodeList(*__, **_) -> Never:
    """
    Qt's 'List *QtPrivate::BindingStatusOrList::decodeList(quintptr ptr)':
    gives 'std::vector<QObject *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.BindingStatusOrList.decodeList' has no cute function "
        "yet. Qt's 'List "
        "*QtPrivate::BindingStatusOrList::decodeList(quintptr ptr)': gives "
        "'std::vector<QObject *>', which has no cute class yet.")

  @staticmethod
  def encodeList(*__, **_) -> Never:
    """
    Qt's 'quintptr QtPrivate::BindingStatusOrList::encodeList(List *list)':
    names 'QtPrivate::BindingStatusOrList::List', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.BindingStatusOrList.encodeList' has no cute function "
        "yet. Qt's 'quintptr "
        "QtPrivate::BindingStatusOrList::encodeList(List *list)': names "
        "'QtPrivate::BindingStatusOrList::List', which has no cute class "
        "yet.")

  @staticmethod
  def list(*__, **_) -> Never:
    """
    Qt's 'List *QtPrivate::BindingStatusOrList::list() const': gives
    'std::vector<QObject *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.BindingStatusOrList.list' has no cute function yet. "
        "Qt's 'List *QtPrivate::BindingStatusOrList::list() const': gives "
        "'std::vector<QObject *>', which has no cute class yet.")
