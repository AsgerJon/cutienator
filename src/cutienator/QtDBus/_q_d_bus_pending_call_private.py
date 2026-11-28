"""
QDBusPendingCallPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusPendingCallPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType
  from . import QDBusConnectionPrivate, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnectionPrivate = WAIT['QDBusConnectionPrivate']
  QDBusMessage = WAIT['QDBusMessage']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPendingCallPrivate(QSharedData):
  """
  The cute side of Qt's QDBusPendingCallPrivate: a plain Python object
  standing in front of one C++ QDBusPendingCallPrivate.

  It is built on the cute 'QSharedData', as Qt's QDBusPendingCallPrivate is
  built on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusPendingCallPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'waitForFinished', 'setMetaTypes',
  'checkReceivedSignature'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 1 leans on 'qdbus_resolve_me(char
  const*)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 1 leans on 'QDBusPendingCallWatcherHelper;
  1 leans on 'qDBusParametersForMethod(QMetaMethod const&, QList<QMetaType>&,
  QString&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusPendingCallPrivate is created at the first use, not by
    'QDBusPendingCallPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusPendingCallPrivate.
  - Each name of Qt's QDBusPendingCallPrivate that has no cute function yet,
    'setReplyCallback', 'waitForFinishedWithGui', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusPendingCallPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QMetaType)
  @overload(int, NoneType)
  def setMetaTypes(self, count: int, types: Optional[QMetaType]) -> None:
    """
    Calls Qt's 'void QDBusPendingCallPrivate::setMetaTypes(int count, const
    QMetaType *types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallprivate.html#setMetaTypes

    Parameters
    ----------

    count : int
      Passed on as it is.

    types : Optional[QMetaType]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusPendingCallPrivate::setMetaTypes(int count, const QMetaType
    #      *types)
    self.uglySide.call(
        'ritual_ZN23QDBusPendingCallPrivate12setMetaTypesEiPK9QMetaType',
        count, self._addressOf(types),
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

  @overload(QDBusMessage, QDBusConnectionPrivate)
  @overload(QDBusMessage, NoneType)
  def __init__(
      self,
      sent: QDBusMessage,
      connection: Optional[QDBusConnectionPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusPendingCallPrivate::QDBusPendingCallPrivate(const QDBusMessage
    &sent, QDBusConnectionPrivate *connection)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallprivate.html

    Parameters
    ----------

    sent : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    connection : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusPendingCallPrivate::QDBusPendingCallPrivate(const QDBusMessage
    #      &sent, QDBusConnectionPrivate *connection)
    self._noteCreation(QDBusPendingCallPrivate, lambda: Rituals.call(
        'ritual_ZN23QDBusPendingCallPrivateC1ERK12QDBusMessageP22QDBusConne'
        'ctionPrivate',
        self._valueOf(sent), self._addressOf(connection),
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

  def waitForFinished(self) -> None:
    """
    Calls Qt's 'void QDBusPendingCallPrivate::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallprivate.html#waitForFinished
    """
    #  void QDBusPendingCallPrivate::waitForFinished()
    self.uglySide.call(
        'ritual_ZN23QDBusPendingCallPrivate15waitForFinishedEv',
    )

  def checkReceivedSignature(self) -> None:
    """
    Calls Qt's 'void QDBusPendingCallPrivate::checkReceivedSignature()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallprivate.html
    """
    #  void QDBusPendingCallPrivate::checkReceivedSignature()
    self.uglySide.call(
        'ritual_ZN23QDBusPendingCallPrivate22checkReceivedSignatureEv',
    )

  @staticmethod
  def setReplyCallback(*__, **_) -> Never:
    """
    Qt's 'bool QDBusPendingCallPrivate::setReplyCallback(QObject *target,
    const char *member)': leans on 'qDBusParametersForMethod(QMetaMethod
    const&, QList<QMetaType>&, QString&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusPendingCallPrivate.setReplyCallback' has no cute function "
        "yet. Qt's 'bool QDBusPendingCallPrivate::setReplyCallback(QObject "
        "*target, const char *member)': leans on "
        "'qDBusParametersForMethod(QMetaMethod const&, QList<QMetaType>&, "
        "QString&)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def waitForFinishedWithGui(*__, **_) -> Never:
    """
    Qt's 'void QDBusPendingCallPrivate::waitForFinishedWithGui()': leans on
    'QDBusPendingCallWatcherHelper::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusPendingCallPrivate.waitForFinishedWithGui' has no cute "
        "function yet. Qt's 'void "
        "QDBusPendingCallPrivate::waitForFinishedWithGui()': leans on "
        "'QDBusPendingCallWatcherHelper::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
