"""
QQmlNotifierEndpoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlnotifierendpoint_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlNotifierEndpoint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlNotifier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlNotifier = WAIT['QQmlNotifier']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlNotifierEndpoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNotifierEndpoint: a plain Python object standing
  in front of one C++ QQmlNotifierEndpoint.

  C++ hands a QQmlNotifierEndpoint around as a copy, so every C++
  QQmlNotifierEndpoint behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlNotifierEndpoint that has a ritual and that
  Python can call so far, 11 names in all: 'isConnected', 'disconnect',
  'isNotifying', 'cancelNotify', 'signalIndex', 'callbackType',
  'nextEndpoint', 'sender', 'setSender', 'senderAsObject',
  'senderAsNotifier'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlNotifierEndpoint::~QQmlNotifierEndpoint()': the destructor:
    Python removes its C++ QQmlNotifierEndpoint by it, and has no other use
    for it.
  - Qt's 'void QQmlNotifierEndpoint::startNotifying(qintptr
    *originalSenderPtr)': takes a number to change where it is.
  - Qt's 'void QQmlNotifierEndpoint::stopNotifying(qintptr
    *originalSenderPtr)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QQmlNotifierEndpoint is created at the first use, not by
    'QQmlNotifierEndpoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlNotifierEndpoint back gives a copy the ritual
    made for Python, in a new cute QQmlNotifierEndpoint.
  - Each name of Qt's QQmlNotifierEndpoint that has no cute function yet,
    'startNotifying', 'stopNotifying', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlNotifierEndpoint, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Callback(CuteNum):
    """
    The enum 'QQmlNotifierEndpoint::Callback' of Qt, with the 7 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    QQmlBoundSignal = Kee[int](1)
    QQmlJavaScriptExpressionGuard = Kee[int](2)
    QQmlVMEMetaObjectEndpoint = Kee[int](3)
    QQmlUnbindableToUnbindableGuard = Kee[int](4)
    QQmlUnbindableToBindableGuard = Kee[int](5)
    QQmlDirtyReferenceObject = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlNotifierEndpoint'

  #  Qt's '~QQmlNotifierEndpoint()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlNotifierEndpoint behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlNotifierEndpointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def isConnected(self) -> bool:
    """
    Calls Qt's 'bool QQmlNotifierEndpoint::isConnected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#isConnected
    """
    #  bool QQmlNotifierEndpoint::isConnected() const
    return self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint11isConnectedEv',
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def isConnected(
      self,
      source: Optional[QObject],
      sourceSignal: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlNotifierEndpoint::isConnected(QObject *source, int
    sourceSignal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#isConnected

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceSignal : int
      Passed on as it is.
    """
    #  bool QQmlNotifierEndpoint::isConnected(QObject *source, int
    #      sourceSignal) const
    return self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint11isConnectedEP7QObjecti',
        self._addressOf(source, 'QObject'), sourceSignal,
    )

  @overload(QQmlNotifier)
  @overload(NoneType)
  def isConnected(self, a0: Optional[QQmlNotifier]) -> bool:
    """
    Calls Qt's 'bool QQmlNotifierEndpoint::isConnected(QQmlNotifier *a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#isConnected

    Parameters
    ----------

    a0 : Optional[QQmlNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlNotifierEndpoint::isConnected(QQmlNotifier *a0) const
    return self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint11isConnectedEP12QQmlNotifier',
        self._addressOf(a0),
    )

  def isNotifying(self) -> bool:
    """
    Calls Qt's 'bool QQmlNotifierEndpoint::isNotifying() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#isNotifying
    """
    #  bool QQmlNotifierEndpoint::isNotifying() const
    return self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint11isNotifyingEv',
    )

  def signalIndex(self) -> int:
    """
    Calls Qt's 'int QQmlNotifierEndpoint::signalIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#signalIndex
    """
    #  int QQmlNotifierEndpoint::signalIndex() const
    return self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint11signalIndexEv',
    )

  def callbackType(self) -> Callback:
    """
    Calls Qt's 'Callback QQmlNotifierEndpoint::callbackType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#callbackType

    Returns
    -------

    Callback
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Callback(number)' gives.
    """
    #  Callback QQmlNotifierEndpoint::callbackType() const
    return QQmlNotifierEndpoint.Callback(self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint12callbackTypeEv',
    ))

  def nextEndpoint(self) -> Optional[QQmlNotifierEndpoint]:
    """
    Calls Qt's 'QQmlNotifierEndpoint *QQmlNotifierEndpoint::nextEndpoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#nextEndpoint

    Returns
    -------

    Optional[QQmlNotifierEndpoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlNotifierEndpoint *QQmlNotifierEndpoint::nextEndpoint() const
    address = self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint12nextEndpointEv',
    )
    return QQmlNotifierEndpoint._cuteAt(address)

  def sender(self) -> int:
    """
    Calls Qt's 'qintptr QQmlNotifierEndpoint::sender() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#sender
    """
    #  qintptr QQmlNotifierEndpoint::sender() const
    return self._callAs(
        'QQmlNotifierEndpoint', 'ritual_ZNK20QQmlNotifierEndpoint6senderEv',
    )

  def senderAsObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlNotifierEndpoint::senderAsObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#senderAsObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlNotifierEndpoint::senderAsObject() const
    address = self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint14senderAsObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def senderAsNotifier(self) -> Optional[QQmlNotifier]:
    """
    Calls Qt's 'QQmlNotifier *QQmlNotifierEndpoint::senderAsNotifier()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#senderAsNotifier

    Returns
    -------

    Optional[QQmlNotifier]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlNotifier *QQmlNotifierEndpoint::senderAsNotifier() const
    address = self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZNK20QQmlNotifierEndpoint16senderAsNotifierEv',
    )
    from . import QQmlNotifier
    return QQmlNotifier._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSender(self, sender: int) -> None:
    """
    Calls Qt's 'void QQmlNotifierEndpoint::setSender(qintptr sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#setSender

    Parameters
    ----------

    sender : int
      Passed on as it is.
    """
    #  void QQmlNotifierEndpoint::setSender(qintptr sender)
    self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZN20QQmlNotifierEndpoint9setSenderEx',
        sender,
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

  @overload(Callback)
  def __init__(self, callback: Callback) -> None:
    """
    Notes what was given, for Qt's
    'QQmlNotifierEndpoint::QQmlNotifierEndpoint(Callback callback)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#QQmlNotifierEndpoint

    Parameters
    ----------

    callback : Callback
      Passed on as its number.
    """
    #  QQmlNotifierEndpoint::QQmlNotifierEndpoint(Callback callback)
    self._noteCreation(QQmlNotifierEndpoint, lambda: Rituals.call(
        'ritual_ZN20QQmlNotifierEndpointC1ENS_8CallbackE', callback.value,
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

  def disconnect(self) -> None:
    """
    Calls Qt's 'void QQmlNotifierEndpoint::disconnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#disconnect
    """
    #  void QQmlNotifierEndpoint::disconnect()
    self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZN20QQmlNotifierEndpoint10disconnectEv',
    )

  def cancelNotify(self) -> None:
    """
    Calls Qt's 'void QQmlNotifierEndpoint::cancelNotify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifierendpoint.html#cancelNotify
    """
    #  void QQmlNotifierEndpoint::cancelNotify()
    self._callAs(
        'QQmlNotifierEndpoint',
        'ritual_ZN20QQmlNotifierEndpoint12cancelNotifyEv',
    )

  @staticmethod
  def startNotifying(*__, **_) -> Never:
    """
    Qt's 'void QQmlNotifierEndpoint::startNotifying(qintptr
    *originalSenderPtr)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlNotifierEndpoint.startNotifying' has no cute function yet. "
        "Qt's 'void QQmlNotifierEndpoint::startNotifying(qintptr "
        "*originalSenderPtr)': takes a number to change where it is.")

  @staticmethod
  def stopNotifying(*__, **_) -> Never:
    """
    Qt's 'void QQmlNotifierEndpoint::stopNotifying(qintptr
    *originalSenderPtr)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlNotifierEndpoint.stopNotifying' has no cute function yet. "
        "Qt's 'void QQmlNotifierEndpoint::stopNotifying(qintptr "
        "*originalSenderPtr)': takes a number to change where it is.")
