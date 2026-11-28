"""
QDBusVirtualObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusvirtualobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDBusConnection, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QDBusMessage = WAIT['QDBusMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusVirtualObject(QObject):
  """
  The cute side of Qt's QDBusVirtualObject: a plain Python object standing in
  front of one C++ QDBusVirtualObject.

  It is built on the cute 'QObject', as Qt's QDBusVirtualObject is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusVirtualObject that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'tr', 'introspect',
  'handleMessage'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusVirtualObject::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDBusVirtualObject::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusVirtualObject::~QDBusVirtualObject()': the destructor: Python
    never removes a C++ QDBusVirtualObject.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDBusVirtualObject is created at the first use, not by
    'QDBusVirtualObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusVirtualObject.
  - Qt tells when it has removed the C++ QDBusVirtualObject. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDBusVirtualObject::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvirtualobject.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusVirtualObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QDBusVirtualObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusVirtualObject'

  #  A C++ QDBusVirtualObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusVirtualObject'

  #  The functions Qt calls itself that QDBusVirtualObject is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'introspect': (
          ('_ZNK18QDBusVirtualObject10introspectERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'handleMessage': (
          ('_ZN18QDBusVirtualObject13handleMessageERK12QDBusMessageRK15QDBu'
           'sConnection',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtDBus:QDBusMessage'),
               ('address', 'value', 'QtDBus:QDBusConnection'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusVirtualObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvirtualobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusVirtualObject::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QDBusVirtualObject10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def introspect(self, path: str) -> str:
    """
    Calls Qt's 'QString QDBusVirtualObject::introspect(const QString &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvirtualobject.html#introspect

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusVirtualObject::introspect(const QString &path) const
    return self.uglySide.call(
        'ritual_ZNK18QDBusVirtualObject10introspectERK7QString', path,
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDBusVirtualObject::QDBusVirtualObject(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusvirtualobject.html#QDBusVirtualObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusVirtualObject::QDBusVirtualObject(QObject *parent)
    self._noteCreation(QDBusVirtualObject, lambda: Rituals.call(
        'ritual_ZN18QDBusVirtualObjectC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QDBusMessage, QDBusConnection)
  def handleMessage(
      self,
      message: QDBusMessage,
      connection: QDBusConnection,
  ) -> bool:
    """
    Calls Qt's 'bool QDBusVirtualObject::handleMessage(const QDBusMessage
    &message, const QDBusConnection &connection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusvirtualobject.html#handleMessage

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.
    """
    #  bool QDBusVirtualObject::handleMessage(const QDBusMessage &message,
    #      const QDBusConnection &connection)
    return self.uglySide.call(
        'ritual_ZN18QDBusVirtualObject13handleMessageERK12QDBusMessageRK15Q'
        'DBusConnection',
        self._valueOf(message), self._valueOf(connection),
    )
