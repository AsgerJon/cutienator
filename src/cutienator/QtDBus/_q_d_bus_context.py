"""
QDBusContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbuscontext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QDBusError

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDBusConnection, QDBusMessage


class QDBusContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusContext: a plain Python object standing in front
  of one C++ QDBusContext.

  C++ hands a QDBusContext around as a copy, so every C++ QDBusContext behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusContext that has a ritual and that Python can
  call so far, 6 names in all: 'calledFromDBus', 'connection', 'message',
  'isDelayedReply', 'setDelayedReply', 'sendErrorReply'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusContext::~QDBusContext()': the destructor: Python removes its
    C++ QDBusContext by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusContext is created at the first use, not by
    'QDBusContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusContext back gives a copy the ritual made for
    Python, in a new cute QDBusContext.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusContext'

  #  Qt's '~QDBusContext()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusContext behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDBusContextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def calledFromDBus(self) -> bool:
    """
    Calls Qt's 'bool QDBusContext::calledFromDBus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#calledFromDBus
    """
    #  bool QDBusContext::calledFromDBus() const
    return self._callAs(
        'QDBusContext', 'ritual_ZNK12QDBusContext14calledFromDBusEv',
    )

  def connection(self) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusContext::connection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#connection

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusContext::connection() const
    address = self._callAs(
        'QDBusContext', 'ritual_ZNK12QDBusContext10connectionEv',
    )
    from . import QDBusConnection
    return QDBusConnection._cuteOwning(address)

  def message(self) -> QDBusMessage:
    """
    Calls Qt's 'const QDBusMessage &QDBusContext::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#message

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  const QDBusMessage &QDBusContext::message() const
    address = self._callAs(
        'QDBusContext', 'ritual_ZNK12QDBusContext7messageEv',
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  def isDelayedReply(self) -> bool:
    """
    Calls Qt's 'bool QDBusContext::isDelayedReply() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#isDelayedReply
    """
    #  bool QDBusContext::isDelayedReply() const
    return self._callAs(
        'QDBusContext', 'ritual_ZNK12QDBusContext14isDelayedReplyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDelayedReply(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDBusContext::setDelayedReply(bool enable) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#setDelayedReply

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDBusContext::setDelayedReply(bool enable) const
    self._callAs(
        'QDBusContext', 'ritual_ZNK12QDBusContext15setDelayedReplyEb',
        enable,
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
    Notes what was given, for Qt's 'QDBusContext::QDBusContext()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#QDBusContext
    """
    #  QDBusContext::QDBusContext()
    self._noteCreation(QDBusContext, lambda: Rituals.call(
        'ritual_ZN12QDBusContextC1Ev',
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

  @overload(str)
  @overload(str, str)
  def sendErrorReply(self, name: str, msg: str = '') -> None:
    """
    Calls Qt's 'void QDBusContext::sendErrorReply(const QString &name, const
    QString &msg) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#sendErrorReply

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDBusContext::sendErrorReply(const QString &name, const QString
    #      &msg) const
    self._callAs(
        'QDBusContext',
        'ritual_ZNK12QDBusContext14sendErrorReplyERK7QStringS2_',
        name, msg,
    )

  @overload(QDBusError.ErrorType)
  @overload(QDBusError.ErrorType, str)
  def sendErrorReply(
      self,
      type: QDBusError.ErrorType,
      msg: str = '',
  ) -> None:
    """
    Calls Qt's 'void QDBusContext::sendErrorReply(QDBusError::ErrorType type,
    const QString &msg) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuscontext.html#sendErrorReply

    Parameters
    ----------

    type : QDBusError.ErrorType
      Passed on as its number.

    msg : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDBusContext::sendErrorReply(QDBusError::ErrorType type, const
    #      QString &msg) const
    self._callAs(
        'QDBusContext',
        'ritual_ZNK12QDBusContext14sendErrorReplyEN10QDBusError9ErrorTypeER'
        'K7QString',
        type.value, msg,
    )
