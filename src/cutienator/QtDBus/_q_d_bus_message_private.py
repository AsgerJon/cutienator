"""
QDBusMessagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusmessage_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMessagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMessage = WAIT['QDBusMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusMessagePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMessagePrivate: a plain Python object standing
  in front of one C++ QDBusMessagePrivate.

  C++ hands a QDBusMessagePrivate around as a copy, so every C++
  QDBusMessagePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMessagePrivate that has a ritual and that
  Python can call so far, 2 names in all: 'createResponseLink', 'isLocal'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusMessagePrivate::~QDBusMessagePrivate()': the destructor:
    Python removes its C++ QDBusMessagePrivate by it, and has no other use
    for it.
  - Qt's 'void QDBusMessagePrivate::setParametersValidated(QDBusMessage &msg,
    bool enable)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 3 leans on 'qdbus_resolve_me(char
  const*)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 1 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDBusMessagePrivate is created at the first use, not by
    'QDBusMessagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMessagePrivate back gives a copy the ritual made
    for Python, in a new cute QDBusMessagePrivate.
  - Each name of Qt's QDBusMessagePrivate that has no cute function yet,
    'fromDBusMessage', 'makeLocal', 'makeLocalReply',
    'setParametersValidated', 'toDBusMessage', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDBusMessage)
  def isLocal(msg: QDBusMessage) -> bool:
    """
    Calls Qt's 'bool QDBusMessagePrivate::isLocal(const QDBusMessage &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmessageprivate.html#isLocal

    Parameters
    ----------

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  bool QDBusMessagePrivate::isLocal(const QDBusMessage &msg)
    return Rituals.call(
        'ritual_ZN19QDBusMessagePrivate7isLocalERK12QDBusMessage',
        CuteMixin._valueOf(msg),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMessagePrivate'

  #  Qt's '~QDBusMessagePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDBusMessagePrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDBusMessagePrivateD1Ev'

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
    'QDBusMessagePrivate::QDBusMessagePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessageprivate.html#QDBusMessagePrivate
    """
    #  QDBusMessagePrivate::QDBusMessagePrivate()
    self._noteCreation(QDBusMessagePrivate, lambda: Rituals.call(
        'ritual_ZN19QDBusMessagePrivateC1Ev',
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

  @overload(THIS)
  @overload(NoneType)
  def createResponseLink(self, call: Optional[QDBusMessagePrivate]) -> None:
    """
    Calls Qt's 'void QDBusMessagePrivate::createResponseLink(const
    QDBusMessagePrivate *call)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmessageprivate.html#createResponseLink

    Parameters
    ----------

    call : Optional[QDBusMessagePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusMessagePrivate::createResponseLink(const QDBusMessagePrivate
    #      *call)
    self.uglySide.call(
        'ritual_ZN19QDBusMessagePrivate18createResponseLinkEPKS_',
        self._addressOf(call),
    )

  @staticmethod
  def fromDBusMessage(*__, **_) -> Never:
    """
    Qt's 'QDBusMessage QDBusMessagePrivate::fromDBusMessage(DBusMessage
    *dmsg, QDBusConnection::ConnectionCapabilities capabilities)': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMessagePrivate.fromDBusMessage' has no cute function yet. "
        "Qt's 'QDBusMessage "
        "QDBusMessagePrivate::fromDBusMessage(DBusMessage *dmsg, "
        "QDBusConnection::ConnectionCapabilities capabilities)': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def makeLocal(*__, **_) -> Never:
    """
    Qt's 'QDBusMessage QDBusMessagePrivate::makeLocal(const
    QDBusConnectionPrivate &conn, const QDBusMessage &asSent)': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMessagePrivate.makeLocal' has no cute function yet. Qt's "
        "'QDBusMessage QDBusMessagePrivate::makeLocal(const "
        "QDBusConnectionPrivate &conn, const QDBusMessage &asSent)': leans "
        "on 'qdbus_resolve_me(char const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def makeLocalReply(*__, **_) -> Never:
    """
    Qt's 'QDBusMessage QDBusMessagePrivate::makeLocalReply(const
    QDBusConnectionPrivate &conn, const QDBusMessage &asSent)': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMessagePrivate.makeLocalReply' has no cute function yet. "
        "Qt's 'QDBusMessage QDBusMessagePrivate::makeLocalReply(const "
        "QDBusConnectionPrivate &conn, const QDBusMessage &asSent)': leans "
        "on 'qdbus_resolve_me(char const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setParametersValidated(*__, **_) -> Never:
    """
    Qt's 'void QDBusMessagePrivate::setParametersValidated(QDBusMessage &msg,
    bool enable)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMessagePrivate.setParametersValidated' has no cute function "
        "yet. Qt's 'void "
        "QDBusMessagePrivate::setParametersValidated(QDBusMessage &msg, "
        "bool enable)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def toDBusMessage(*__, **_) -> Never:
    """
    Qt's 'DBusMessage *QDBusMessagePrivate::toDBusMessage(const QDBusMessage
    &message, QDBusConnection::ConnectionCapabilities capabilities,
    QDBusError *error)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'data'; did you mean 'std::data'?.
    """
    raise NotImplementedError(
        "'QDBusMessagePrivate.toDBusMessage' has no cute function yet. Qt's "
        "'DBusMessage *QDBusMessagePrivate::toDBusMessage(const "
        "QDBusMessage &message, QDBusConnection::ConnectionCapabilities "
        "capabilities, QDBusError *error)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'data'; did you mean "
        "'std::data'?.")
