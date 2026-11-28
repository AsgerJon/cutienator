"""
QDBusPendingReplyBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbuspendingreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDBusPendingCall

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaType, QVariant
  from . import QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMessage = WAIT['QDBusMessage']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPendingReplyBase(QDBusPendingCall):
  """
  The cute side of Qt's QDBusPendingReplyBase: a plain Python object standing
  in front of one C++ QDBusPendingReplyBase.

  It is built on the cute 'QDBusPendingCall', as Qt's QDBusPendingReplyBase
  is built on Qt's QDBusPendingCall, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusPendingReplyBase that has a ritual and that
  Python can call so far, 3 names in all: 'assign', 'argumentAt',
  'setMetaTypes'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusPendingReplyBase::~QDBusPendingReplyBase()': the destructor:
    Python never removes a C++ QDBusPendingReplyBase.
  - Qt's 'QDBusPendingReplyBase::QDBusPendingReplyBase(const
    QDBusPendingReplyBase &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QDBusPendingReplyBase &QDBusPendingReplyBase::operator=(const
    QDBusPendingReplyBase &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDBusPendingReplyBase::QDBusPendingReplyBase(QDBusPendingReplyBase
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QDBusPendingReplyBase
    &QDBusPendingReplyBase::operator=(QDBusPendingReplyBase &&a0)':
    assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QDBusPendingReplyBase is created at the first use, not by
    'QDBusPendingReplyBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusPendingReplyBase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusPendingReplyBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def argumentAt(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDBusPendingReplyBase::argumentAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingreplybase.html#argumentAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDBusPendingReplyBase::argumentAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QDBusPendingReplyBase10argumentAtEi', index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QMetaType)
  @overload(int, NoneType)
  def setMetaTypes(self, count: int, metaTypes: Optional[QMetaType]) -> None:
    """
    Calls Qt's 'void QDBusPendingReplyBase::setMetaTypes(int count, const
    QMetaType *metaTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingreplybase.html#setMetaTypes

    Parameters
    ----------

    count : int
      Passed on as it is.

    metaTypes : Optional[QMetaType]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPendingReplyBase::setMetaTypes(int count, const QMetaType
    #      *metaTypes)
    self.uglySide.call(
        'ritual_ZN21QDBusPendingReplyBase12setMetaTypesEiPK9QMetaType',
        count, self._addressOf(metaTypes),
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
    'QDBusPendingReplyBase::QDBusPendingReplyBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingreplybase.html#QDBusPendingReplyBase
    """
    #  QDBusPendingReplyBase::QDBusPendingReplyBase()
    self._noteCreation(QDBusPendingReplyBase, lambda: Rituals.call(
        'ritual_ZN21QDBusPendingReplyBaseC1Ev',
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

  @overload(QDBusPendingCall)
  def assign(self, call: QDBusPendingCall) -> None:
    """
    Calls Qt's 'void QDBusPendingReplyBase::assign(const QDBusPendingCall
    &call)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingreplybase.html#assign

    Parameters
    ----------

    call : QDBusPendingCall
      Passed on as a value: Qt reads the C++ QDBusPendingCall, which stays
      Python's own.
    """
    #  void QDBusPendingReplyBase::assign(const QDBusPendingCall &call)
    self.uglySide.call(
        'ritual_ZN21QDBusPendingReplyBase6assignERK16QDBusPendingCall',
        self._valueOf(call, 'QDBusPendingCall'),
    )

  @overload(QDBusMessage)
  def assign(self, message: QDBusMessage) -> None:
    """
    Calls Qt's 'void QDBusPendingReplyBase::assign(const QDBusMessage
    &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingreplybase.html#assign

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QDBusPendingReplyBase::assign(const QDBusMessage &message)
    self.uglySide.call(
        'ritual_ZN21QDBusPendingReplyBase6assignERK12QDBusMessage',
        self._valueOf(message),
    )
