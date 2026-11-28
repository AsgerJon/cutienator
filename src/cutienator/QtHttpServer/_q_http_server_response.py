"""
QHttpServerResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverresponse.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QHttpServerResponder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QJsonArray, QJsonObject
  from ..QtNetwork import QHttpHeaders
  from . import QHttpServerResponsePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']
  QJsonArray = WAIT['QJsonArray']
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerResponse(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerResponse: a plain Python object standing
  in front of one C++ QHttpServerResponse.

  What exists
  -----------

  Every function of Qt's QHttpServerResponse that has a ritual and that
  Python can call so far, 6 names in all: 'd_func', 'data', 'mimeType',
  'statusCode', 'headers', 'setHeaders'. It can be made from Python, in 6
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHttpServerResponsePrivate *QHttpServerResponse::d_func()
    const': takes in Python what 'QHttpServerResponsePrivate
    *QHttpServerResponse::d_func()' takes.
  - Qt's 'QHttpServerResponse::QHttpServerResponse(QHttpServerResponse
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerResponse
    &QHttpServerResponse::operator=(QHttpServerResponse &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHttpServerResponse::swap(QHttpServerResponse &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QHttpServerResponse::QHttpServerResponse(const QString &data,
    StatusCode status)': takes in Python what
    'QHttpServerResponse::QHttpServerResponse(const char *data, StatusCode
    status)' takes.
  - Qt's 'QHttpServerResponse::QHttpServerResponse(QByteArray &&data,
    StatusCode status)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerResponse::QHttpServerResponse(const QByteArray
    &mimeType, QByteArray &&data, StatusCode status)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QHttpServerResponse::~QHttpServerResponse()': the destructor:
    Python never removes a C++ QHttpServerResponse.
  - Qt's 'QHttpServerResponse QHttpServerResponse::fromFile(const QString
    &fileName)': gives a type Python has no way to take yet.
  - Qt's 'void QHttpServerResponse::setHeaders(QHttpHeaders &&newHeaders)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QHttpServerResponse is created at the first use, not by
    'QHttpServerResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerResponse.
  - Each name of Qt's QHttpServerResponse that has no cute function yet,
    'fromFile', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerResponse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpServerResponse::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponse.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpServerResponse::data() const
    address = self.uglySide.call('ritual_ZNK19QHttpServerResponse4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mimeType(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpServerResponse::mimeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponse.html#mimeType

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpServerResponse::mimeType() const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpServerResponse8mimeTypeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def statusCode(self) -> QHttpServerResponder.StatusCode:
    """
    Calls Qt's 'StatusCode QHttpServerResponse::statusCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#statusCode

    Returns
    -------

    QHttpServerResponder.StatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QHttpServerResponder.StatusCode(number)' gives.
    """
    #  StatusCode QHttpServerResponse::statusCode() const
    return QHttpServerResponder.StatusCode(self.uglySide.call(
        'ritual_ZNK19QHttpServerResponse10statusCodeEv',
    ))

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QHttpServerResponse::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponse.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QHttpServerResponse::headers() const
    address = self.uglySide.call('ritual_ZNK19QHttpServerResponse7headersEv')
    from ..QtNetwork import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHttpHeaders)
  def setHeaders(self, newHeaders: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QHttpServerResponse::setHeaders(const QHttpHeaders
    &newHeaders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#setHeaders

    Parameters
    ----------

    newHeaders : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QHttpServerResponse::setHeaders(const QHttpHeaders &newHeaders)
    self.uglySide.call(
        'ritual_ZN19QHttpServerResponse10setHeadersERK12QHttpHeaders',
        self._valueOf(newHeaders),
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

  @overload(QHttpServerResponder.StatusCode)
  def __init__(self, statusCode: QHttpServerResponder.StatusCode) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(StatusCode statusCode)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    statusCode : QHttpServerResponder.StatusCode
      Passed on as its number.
    """
    #  QHttpServerResponse::QHttpServerResponse(StatusCode statusCode)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1EN20QHttpServerResponder10StatusCo'
        'deE',
        statusCode.value,
    ))

  @overload(str)
  @overload(NoneType)
  @overload(str, QHttpServerResponder.StatusCode)
  @overload(NoneType, QHttpServerResponder.StatusCode)
  def __init__(
      self,
      data: Optional[str],
      status: QHttpServerResponder.StatusCode = (
          QHttpServerResponder.StatusCode.Ok),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(const char *data, StatusCode
    status)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    status : QHttpServerResponder.StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      QHttpServerResponder.StatusCode.Ok.
    """
    #  QHttpServerResponse::QHttpServerResponse(const char *data, StatusCode
    #      status)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1EPKcN20QHttpServerResponder10Statu'
        'sCodeE',
        self._bytesOf(data), status.value,
    ))

  @overload(QByteArray)
  @overload(QByteArray, QHttpServerResponder.StatusCode)
  def __init__(
      self,
      data: QByteArray,
      status: QHttpServerResponder.StatusCode = (
          QHttpServerResponder.StatusCode.Ok),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(const QByteArray &data,
    StatusCode status)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      QHttpServerResponder.StatusCode.Ok.
    """
    #  QHttpServerResponse::QHttpServerResponse(const QByteArray &data,
    #      StatusCode status)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1ERK10QByteArrayN20QHttpServerRespo'
        'nder10StatusCodeE',
        self._valueOf(data), status.value,
    ))

  @overload(QJsonObject)
  @overload(QJsonObject, QHttpServerResponder.StatusCode)
  def __init__(
      self,
      data: QJsonObject,
      status: QHttpServerResponder.StatusCode = (
          QHttpServerResponder.StatusCode.Ok),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(const QJsonObject &data,
    StatusCode status)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    data : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      QHttpServerResponder.StatusCode.Ok.
    """
    #  QHttpServerResponse::QHttpServerResponse(const QJsonObject &data,
    #      StatusCode status)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1ERK11QJsonObjectN20QHttpServerResp'
        'onder10StatusCodeE',
        self._valueOf(data), status.value,
    ))

  @overload(QJsonArray)
  @overload(QJsonArray, QHttpServerResponder.StatusCode)
  def __init__(
      self,
      data: QJsonArray,
      status: QHttpServerResponder.StatusCode = (
          QHttpServerResponder.StatusCode.Ok),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(const QJsonArray &data,
    StatusCode status)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    data : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      QHttpServerResponder.StatusCode.Ok.
    """
    #  QHttpServerResponse::QHttpServerResponse(const QJsonArray &data,
    #      StatusCode status)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1ERK10QJsonArrayN20QHttpServerRespo'
        'nder10StatusCodeE',
        self._valueOf(data), status.value,
    ))

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, QByteArray, QHttpServerResponder.StatusCode)
  def __init__(
      self,
      mimeType: QByteArray,
      data: QByteArray,
      status: QHttpServerResponder.StatusCode = (
          QHttpServerResponder.StatusCode.Ok),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponse::QHttpServerResponse(const QByteArray &mimeType,
    const QByteArray &data, StatusCode status)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponse.html#QHttpServerResponse

    Parameters
    ----------

    mimeType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      QHttpServerResponder.StatusCode.Ok.
    """
    #  QHttpServerResponse::QHttpServerResponse(const QByteArray &mimeType,
    #      const QByteArray &data, StatusCode status)
    self._noteCreation(QHttpServerResponse, lambda: Rituals.call(
        'ritual_ZN19QHttpServerResponseC1ERK10QByteArrayS2_N20QHttpServerRe'
        'sponder10StatusCodeE',
        self._valueOf(mimeType), self._valueOf(data), status.value,
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

  def d_func(self) -> Optional[QHttpServerResponsePrivate]:
    """
    Calls Qt's 'QHttpServerResponsePrivate *QHttpServerResponse::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponse.html#d_func

    Returns
    -------

    Optional[QHttpServerResponsePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerResponsePrivate *QHttpServerResponse::d_func()
    address = self.uglySide.call('ritual_ZN19QHttpServerResponse6d_funcEv')
    from . import QHttpServerResponsePrivate
    return QHttpServerResponsePrivate._cuteAt(address)

  @staticmethod
  def fromFile(*__, **_) -> Never:
    """
    Qt's 'QHttpServerResponse QHttpServerResponse::fromFile(const QString
    &fileName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpServerResponse.fromFile' has no cute function yet. Qt's "
        "'QHttpServerResponse QHttpServerResponse::fromFile(const QString "
        "&fileName)': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponse::swap(QHttpServerResponse &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerResponse.swap' has no cute function yet. Qt's 'void "
        "QHttpServerResponse::swap(QHttpServerResponse &other)': takes a "
        "type Python has no way to hand over yet.")
