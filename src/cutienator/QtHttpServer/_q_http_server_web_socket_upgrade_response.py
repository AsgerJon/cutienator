"""
QHttpServerWebSocketUpgradeResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverwebsocketupgraderesponse.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QHttpServerWebSocketUpgradeResponse(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerWebSocketUpgradeResponse: a plain Python
  object standing in front of one C++ QHttpServerWebSocketUpgradeResponse.

  C++ hands a QHttpServerWebSocketUpgradeResponse around as a copy, so every
  C++ QHttpServerWebSocketUpgradeResponse behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QHttpServerWebSocketUpgradeResponse that has a
  ritual and that Python can call so far, 6 names in all: 'type',
  'denyStatus', 'denyMessage', 'accept', 'deny', 'passToNext'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpServerWebSocketUpgradeResponse::
    QHttpServerWebSocketUpgradeResponse(QHttpServerWebSocketUpgradeResponse
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerWebSocketUpgradeResponse::
    ~QHttpServerWebSocketUpgradeResponse()': the destructor: Python removes
    its C++ QHttpServerWebSocketUpgradeResponse by it, and has no other use
    for it.
  - Qt's 'QHttpServerWebSocketUpgradeResponse
    &QHttpServerWebSocketUpgradeResponse::operator=(const
    QHttpServerWebSocketUpgradeResponse &other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QHttpServerWebSocketUpgradeResponse
    &QHttpServerWebSocketUpgradeResponse::operator=(
    QHttpServerWebSocketUpgradeResponse &&other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'void QHttpServerWebSocketUpgradeResponse::swap(
    QHttpServerWebSocketUpgradeResponse &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 1 not a gap; 1 forbidden.

  What to expect
  --------------

  - The C++ QHttpServerWebSocketUpgradeResponse is created at the first use,
    not by 'QHttpServerWebSocketUpgradeResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerWebSocketUpgradeResponse back gives a copy
    the ritual made for Python, in a new cute
    QHttpServerWebSocketUpgradeResponse.
  - Each name of Qt's QHttpServerWebSocketUpgradeResponse that has no cute
    function yet, 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QHttpServerWebSocketUpgradeResponse, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ResponseType(CuteNum, scoped=True):
    """
    The enum 'QHttpServerWebSocketUpgradeResponse::ResponseType' of Qt, with
    the 3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Accept = Kee[int](0)
    Deny = Kee[int](1)
    PassToNext = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def accept() -> QHttpServerWebSocketUpgradeResponse:
    """
    Calls Qt's 'QHttpServerWebSocketUpgradeResponse
    QHttpServerWebSocketUpgradeResponse::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html#accept

    Returns
    -------

    QHttpServerWebSocketUpgradeResponse
      A new cute QHttpServerWebSocketUpgradeResponse around the copy Qt gave
      back. Python owns it.
    """
    #  QHttpServerWebSocketUpgradeResponse
    #      QHttpServerWebSocketUpgradeResponse::accept()
    address = Rituals.call(
        'ritual_ZN35QHttpServerWebSocketUpgradeResponse6acceptEv',
    )
    return QHttpServerWebSocketUpgradeResponse._cuteOwning(address)

  @staticmethod
  @overload()
  def deny() -> QHttpServerWebSocketUpgradeResponse:
    """
    Calls Qt's 'QHttpServerWebSocketUpgradeResponse
    QHttpServerWebSocketUpgradeResponse::deny()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html#deny

    Returns
    -------

    QHttpServerWebSocketUpgradeResponse
      A new cute QHttpServerWebSocketUpgradeResponse around the copy Qt gave
      back. Python owns it.
    """
    #  QHttpServerWebSocketUpgradeResponse
    #      QHttpServerWebSocketUpgradeResponse::deny()
    address = Rituals.call(
        'ritual_ZN35QHttpServerWebSocketUpgradeResponse4denyEv',
    )
    return QHttpServerWebSocketUpgradeResponse._cuteOwning(address)

  @staticmethod
  @overload(int, QByteArray)
  def deny(
      status: int,
      message: QByteArray,
  ) -> QHttpServerWebSocketUpgradeResponse:
    """
    Calls Qt's 'QHttpServerWebSocketUpgradeResponse
    QHttpServerWebSocketUpgradeResponse::deny(int status, QByteArray
    message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html#deny

    Parameters
    ----------

    status : int
      Passed on as it is.

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QHttpServerWebSocketUpgradeResponse
      A new cute QHttpServerWebSocketUpgradeResponse around the copy Qt gave
      back. Python owns it.
    """
    #  QHttpServerWebSocketUpgradeResponse
    #      QHttpServerWebSocketUpgradeResponse::deny(int status, QByteArray
    #      message)
    address = Rituals.call(
        'ritual_ZN35QHttpServerWebSocketUpgradeResponse4denyEi10QByteArray',
        status, CuteMixin._valueOf(message),
    )
    return QHttpServerWebSocketUpgradeResponse._cuteOwning(address)

  @staticmethod
  def passToNext() -> QHttpServerWebSocketUpgradeResponse:
    """
    Calls Qt's 'QHttpServerWebSocketUpgradeResponse
    QHttpServerWebSocketUpgradeResponse::passToNext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html

    Returns
    -------

    QHttpServerWebSocketUpgradeResponse
      A new cute QHttpServerWebSocketUpgradeResponse around the copy Qt gave
      back. Python owns it.
    """
    #  QHttpServerWebSocketUpgradeResponse
    #      QHttpServerWebSocketUpgradeResponse::passToNext()
    address = Rituals.call(
        'ritual_ZN35QHttpServerWebSocketUpgradeResponse10passToNextEv',
    )
    return QHttpServerWebSocketUpgradeResponse._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerWebSocketUpgradeResponse'

  #  Qt's '~QHttpServerWebSocketUpgradeResponse()'. Naming it makes this a
  #  value class: Python owns every C++ QHttpServerWebSocketUpgradeResponse
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QHttpServerWebSocketUpgradeResponseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> ResponseType:
    """
    Calls Qt's 'ResponseType QHttpServerWebSocketUpgradeResponse::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html#type

    Returns
    -------

    ResponseType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResponseType(number)'
      gives.
    """
    #  ResponseType QHttpServerWebSocketUpgradeResponse::type() const
    return QHttpServerWebSocketUpgradeResponse.ResponseType(
        self.uglySide.call(
            'ritual_ZNK35QHttpServerWebSocketUpgradeResponse4typeEv',
        ))

  def denyStatus(self) -> int:
    """
    Calls Qt's 'int QHttpServerWebSocketUpgradeResponse::denyStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html
    """
    #  int QHttpServerWebSocketUpgradeResponse::denyStatus() const
    return self.uglySide.call(
        'ritual_ZNK35QHttpServerWebSocketUpgradeResponse10denyStatusEv',
    )

  def denyMessage(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray
    &QHttpServerWebSocketUpgradeResponse::denyMessage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QHttpServerWebSocketUpgradeResponse::denyMessage()
    #      const
    address = self.uglySide.call(
        'ritual_ZNKR35QHttpServerWebSocketUpgradeResponse11denyMessageEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QHttpServerWebSocketUpgradeResponse) -> None:
    """
    Notes what was given, for Qt's 'QHttpServerWebSocketUpgradeResponse::
    QHttpServerWebSocketUpgradeResponse(const
    QHttpServerWebSocketUpgradeResponse &other)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html

    Parameters
    ----------

    other : QHttpServerWebSocketUpgradeResponse
      Passed on as a value: Qt reads the C++
      QHttpServerWebSocketUpgradeResponse, which stays Python's own.
    """
    #  QHttpServerWebSocketUpgradeResponse::
    #      QHttpServerWebSocketUpgradeResponse(const
    #      QHttpServerWebSocketUpgradeResponse &other)
    self._noteCreation(
        QHttpServerWebSocketUpgradeResponse, lambda: Rituals.call(
            'ritual_ZN35QHttpServerWebSocketUpgradeResponseC1ERKS_',
            self._valueOf(other),
        ))

  @overload(ResponseType)
  def __init__(self, type: ResponseType) -> None:
    """
    Notes what was given, for Qt's 'QHttpServerWebSocketUpgradeResponse::
    QHttpServerWebSocketUpgradeResponse(ResponseType type)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html

    Parameters
    ----------

    type : ResponseType
      Passed on as its number.
    """
    #  QHttpServerWebSocketUpgradeResponse::
    #      QHttpServerWebSocketUpgradeResponse(ResponseType type)
    self._noteCreation(
        QHttpServerWebSocketUpgradeResponse, lambda: Rituals.call(
            'ritual_ZN35QHttpServerWebSocketUpgradeResponseC1ENS_12Response'
            'TypeE',
            type.value,
        ))

  @overload(ResponseType, int, QByteArray)
  def __init__(
      self,
      type: ResponseType,
      status: int,
      message: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHttpServerWebSocketUpgradeResponse::
    QHttpServerWebSocketUpgradeResponse(ResponseType type, int status,
    QByteArray message)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverwebsocketupgraderesponse.html

    Parameters
    ----------

    type : ResponseType
      Passed on as its number.

    status : int
      Passed on as it is.

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QHttpServerWebSocketUpgradeResponse::
    #      QHttpServerWebSocketUpgradeResponse(ResponseType type, int status,
    #      QByteArray message)
    self._noteCreation(
        QHttpServerWebSocketUpgradeResponse, lambda: Rituals.call(
            'ritual_ZN35QHttpServerWebSocketUpgradeResponseC1ENS_12Response'
            'TypeEi10QByteArray',
            type.value, status, self._valueOf(message),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerWebSocketUpgradeResponse::swap(
    QHttpServerWebSocketUpgradeResponse &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerWebSocketUpgradeResponse.swap' has no cute function "
        "yet. Qt's 'void "
        "QHttpServerWebSocketUpgradeResponse::swap(QHttpServerWebSocketUpgra"
        "deResponse &other)': takes a type Python has no way to hand over "
        "yet.")
