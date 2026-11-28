"""
QRestReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qrestreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRestReply(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRestReply: a plain Python object standing in front
  of one C++ QRestReply.

  What exists
  -----------

  Every function of Qt's QRestReply that has a ritual and that Python can
  call so far, 9 names in all: 'networkReply', 'readBody', 'readText',
  'isSuccess', 'httpStatus', 'isHttpStatusSuccess', 'hasError', 'error',
  'errorString'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRestReply::~QRestReply()': the destructor: Python never removes a
    C++ QRestReply.
  - Qt's 'QRestReply::QRestReply(QRestReply &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QRestReply &QRestReply::operator=(QRestReply &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QRestReply::swap(QRestReply &other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'std::optional<QJsonDocument> QRestReply::readJson(QJsonParseError
    *error)': gives a type Python has no way to take yet.
  - Qt's 'QDebug operator<<(QDebug debug, const QRestReply &reply)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRestReply is created at the first use, not by 'QRestReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRestReply.
  - Each name of Qt's QRestReply that has no cute function yet, 'readJson',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRestReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def networkReply(self) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestReply::networkReply() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#networkReply

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestReply::networkReply() const
    address = self.uglySide.call('ritual_ZNK10QRestReply12networkReplyEv')
    return QNetworkReply._cuteAt(address)

  def isSuccess(self) -> bool:
    """
    Calls Qt's 'bool QRestReply::isSuccess() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#isSuccess
    """
    #  bool QRestReply::isSuccess() const
    return self.uglySide.call('ritual_ZNK10QRestReply9isSuccessEv')

  def httpStatus(self) -> int:
    """
    Calls Qt's 'int QRestReply::httpStatus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#httpStatus
    """
    #  int QRestReply::httpStatus() const
    return self.uglySide.call('ritual_ZNK10QRestReply10httpStatusEv')

  def isHttpStatusSuccess(self) -> bool:
    """
    Calls Qt's 'bool QRestReply::isHttpStatusSuccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestreply.html#isHttpStatusSuccess
    """
    #  bool QRestReply::isHttpStatusSuccess() const
    return self.uglySide.call(
        'ritual_ZNK10QRestReply19isHttpStatusSuccessEv',
    )

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QRestReply::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#hasError
    """
    #  bool QRestReply::hasError() const
    return self.uglySide.call('ritual_ZNK10QRestReply8hasErrorEv')

  def error(self) -> QNetworkReply.NetworkError:
    """
    Calls Qt's 'QNetworkReply::NetworkError QRestReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#error

    Returns
    -------

    QNetworkReply.NetworkError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkReply.NetworkError(number)' gives.
    """
    #  QNetworkReply::NetworkError QRestReply::error() const
    return QNetworkReply.NetworkError(self.uglySide.call(
        'ritual_ZNK10QRestReply5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QRestReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRestReply::errorString() const
    return self.uglySide.call('ritual_ZNK10QRestReply11errorStringEv')

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

  @overload(QNetworkReply)
  @overload(NoneType)
  def __init__(self, reply: Optional[QNetworkReply]) -> None:
    """
    Notes what was given, for Qt's 'QRestReply::QRestReply(QNetworkReply
    *reply)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#QRestReply

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRestReply::QRestReply(QNetworkReply *reply)
    self._noteCreation(QRestReply, lambda: Rituals.call(
        'ritual_ZN10QRestReplyC1EP13QNetworkReply', self._addressOf(reply),
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

  def readBody(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRestReply::readBody()'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#readBody

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRestReply::readBody()
    address = self.uglySide.call('ritual_ZN10QRestReply8readBodyEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def readText(self) -> str:
    """
    Calls Qt's 'QString QRestReply::readText()'.

    Qt's own words: https://doc.qt.io/qt-6/qrestreply.html#readText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRestReply::readText()
    return self.uglySide.call('ritual_ZN10QRestReply8readTextEv')

  @staticmethod
  def readJson(*__, **_) -> Never:
    """
    Qt's 'std::optional<QJsonDocument> QRestReply::readJson(QJsonParseError
    *error)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRestReply.readJson' has no cute function yet. Qt's "
        "'std::optional<QJsonDocument> QRestReply::readJson(QJsonParseError "
        "*error)': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QRestReply::swap(QRestReply &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRestReply.swap' has no cute function yet. Qt's 'void "
        "QRestReply::swap(QRestReply &other)': takes a type Python has no "
        "way to hand over yet.")
