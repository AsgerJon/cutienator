"""
QHttpServerResponder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/qhttpserverresponder.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QJsonDocument
  from ..QtNetwork import QHttpHeaders
  from . import QHttpServerResponderPrivate, QHttpServerStream
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']
  QHttpServerStream = WAIT['QHttpServerStream']
  QIODevice = WAIT['QIODevice']
  QJsonDocument = WAIT['QJsonDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerResponder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerResponder: a plain Python object standing
  in front of one C++ QHttpServerResponder.

  What exists
  -----------

  Every function of Qt's QHttpServerResponder that has a ritual and that
  Python can call so far, 6 names in all: 'd_func', 'write',
  'writeBeginChunked', 'writeChunk', 'writeEndChunked', 'isResponseCanceled'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QHttpServerResponderPrivate *QHttpServerResponder::d_func()
    const': takes in Python what 'QHttpServerResponderPrivate
    *QHttpServerResponder::d_func()' takes.
  - Qt's 'QHttpServerResponder::QHttpServerResponder(QHttpServerResponder
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpServerResponder
    &QHttpServerResponder::operator=(QHttpServerResponder &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHttpServerResponder::~QHttpServerResponder()': the destructor:
    Python never removes a C++ QHttpServerResponder.
  - Qt's 'void QHttpServerResponder::swap(QHttpServerResponder &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QHttpServerResponder::sendResponse(const QHttpServerResponse
    &response)': takes a type Python has no way to hand over yet.
  - Qt's 'void QHttpServerResponder::writeBeginChunked(const QHttpHeaders
    &headers, QList<QHttpHeaders::WellKnownHeader> trailerNames, StatusCode
    status)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHttpServerResponder is created at the first use, not by
    'QHttpServerResponder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerResponder.
  - Each name of Qt's QHttpServerResponder that has no cute function yet,
    'sendResponse', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpServerResponder, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StatusCode(CuteNum, scoped=True):
    """
    The enum 'QHttpServerResponder::StatusCode' of Qt, with the 61 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Continue = Kee[int](100)
    SwitchingProtocols = Kee[int](101)
    Processing = Kee[int](102)
    Ok = Kee[int](200)
    Created = Kee[int](201)
    Accepted = Kee[int](202)
    NonAuthoritativeInformation = Kee[int](203)
    NoContent = Kee[int](204)
    ResetContent = Kee[int](205)
    PartialContent = Kee[int](206)
    MultiStatus = Kee[int](207)
    AlreadyReported = Kee[int](208)
    IMUsed = Kee[int](226)
    MultipleChoices = Kee[int](300)
    MovedPermanently = Kee[int](301)
    Found = Kee[int](302)
    SeeOther = Kee[int](303)
    NotModified = Kee[int](304)
    UseProxy = Kee[int](305)
    TemporaryRedirect = Kee[int](307)
    PermanentRedirect = Kee[int](308)
    BadRequest = Kee[int](400)
    Unauthorized = Kee[int](401)
    PaymentRequired = Kee[int](402)
    Forbidden = Kee[int](403)
    NotFound = Kee[int](404)
    MethodNotAllowed = Kee[int](405)
    NotAcceptable = Kee[int](406)
    ProxyAuthenticationRequired = Kee[int](407)
    RequestTimeout = Kee[int](408)
    Conflict = Kee[int](409)
    Gone = Kee[int](410)
    LengthRequired = Kee[int](411)
    PreconditionFailed = Kee[int](412)
    PayloadTooLarge = Kee[int](413)
    UriTooLong = Kee[int](414)
    UnsupportedMediaType = Kee[int](415)
    RequestRangeNotSatisfiable = Kee[int](416)
    ExpectationFailed = Kee[int](417)
    ImATeapot = Kee[int](418)
    MisdirectedRequest = Kee[int](421)
    UnprocessableEntity = Kee[int](422)
    Locked = Kee[int](423)
    FailedDependency = Kee[int](424)
    UpgradeRequired = Kee[int](426)
    PreconditionRequired = Kee[int](428)
    TooManyRequests = Kee[int](429)
    RequestHeaderFieldsTooLarge = Kee[int](431)
    UnavailableForLegalReasons = Kee[int](451)
    InternalServerError = Kee[int](500)
    NotImplemented = Kee[int](501)
    BadGateway = Kee[int](502)
    ServiceUnavailable = Kee[int](503)
    GatewayTimeout = Kee[int](504)
    HttpVersionNotSupported = Kee[int](505)
    VariantAlsoNegotiates = Kee[int](506)
    InsufficientStorage = Kee[int](507)
    LoopDetected = Kee[int](508)
    NotExtended = Kee[int](510)
    NetworkAuthenticationRequired = Kee[int](511)
    NetworkConnectTimeoutError = Kee[int](599)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerResponder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isResponseCanceled(self) -> bool:
    """
    Calls Qt's 'bool QHttpServerResponder::isResponseCanceled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#isResponseCanceled
    """
    #  bool QHttpServerResponder::isResponseCanceled() const
    return self.uglySide.call(
        'ritual_ZNK20QHttpServerResponder18isResponseCanceledEv',
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

  @overload(QHttpServerStream)
  @overload(NoneType)
  def __init__(self, stream: Optional[QHttpServerStream]) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerResponder::QHttpServerResponder(QHttpServerStream *stream)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#QHttpServerResponder

    Parameters
    ----------

    stream : Optional[QHttpServerStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpServerResponder::QHttpServerResponder(QHttpServerStream *stream)
    self._noteCreation(QHttpServerResponder, lambda: Rituals.call(
        'ritual_ZN20QHttpServerResponderC1EP17QHttpServerStream',
        self._addressOf(stream),
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

  def d_func(self) -> Optional[QHttpServerResponderPrivate]:
    """
    Calls Qt's 'QHttpServerResponderPrivate *QHttpServerResponder::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#d_func

    Returns
    -------

    Optional[QHttpServerResponderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpServerResponderPrivate *QHttpServerResponder::d_func()
    address = self.uglySide.call('ritual_ZN20QHttpServerResponder6d_funcEv')
    from . import QHttpServerResponderPrivate
    return QHttpServerResponderPrivate._cuteAt(address)

  @overload(QIODevice, QHttpHeaders)
  @overload(NoneType, QHttpHeaders)
  @overload(QIODevice, QHttpHeaders, StatusCode)
  @overload(NoneType, QHttpHeaders, StatusCode)
  def write(
      self,
      data: Optional[QIODevice],
      headers: QHttpHeaders,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(QIODevice *data, const
    QHttpHeaders &headers, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(QIODevice *data, const QHttpHeaders
    #      &headers, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeEP9QIODeviceRK12QHttpHeadersN'
        'S_10StatusCodeE',
        self._addressOf(data), self._valueOf(headers), status.value,
    )

  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  @overload(QIODevice, QByteArray, StatusCode)
  @overload(NoneType, QByteArray, StatusCode)
  def write(
      self,
      data: Optional[QIODevice],
      mimeType: QByteArray,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(QIODevice *data, const
    QByteArray &mimeType, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mimeType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(QIODevice *data, const QByteArray
    #      &mimeType, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeEP9QIODeviceRK10QByteArrayNS_'
        '10StatusCodeE',
        self._addressOf(data), self._valueOf(mimeType), status.value,
    )

  @overload(QJsonDocument, QHttpHeaders)
  @overload(QJsonDocument, QHttpHeaders, StatusCode)
  def write(
      self,
      document: QJsonDocument,
      headers: QHttpHeaders,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(const QJsonDocument
    &document, const QHttpHeaders &headers, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    document : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(const QJsonDocument &document, const
    #      QHttpHeaders &headers, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeERK13QJsonDocumentRK12QHttpHe'
        'adersNS_10StatusCodeE',
        self._valueOf(document), self._valueOf(headers), status.value,
    )

  @overload(QJsonDocument)
  @overload(QJsonDocument, StatusCode)
  def write(
      self,
      document: QJsonDocument,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(const QJsonDocument
    &document, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    document : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(const QJsonDocument &document,
    #      StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeERK13QJsonDocumentNS_10Status'
        'CodeE',
        self._valueOf(document), status.value,
    )

  @overload(QByteArray, QHttpHeaders)
  @overload(QByteArray, QHttpHeaders, StatusCode)
  def write(
      self,
      data: QByteArray,
      headers: QHttpHeaders,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(const QByteArray &data,
    const QHttpHeaders &headers, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(const QByteArray &data, const
    #      QHttpHeaders &headers, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeERK10QByteArrayRK12QHttpHeade'
        'rsNS_10StatusCodeE',
        self._valueOf(data), self._valueOf(headers), status.value,
    )

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, QByteArray, StatusCode)
  def write(
      self,
      data: QByteArray,
      mimeType: QByteArray,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(const QByteArray &data,
    const QByteArray &mimeType, StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mimeType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(const QByteArray &data, const
    #      QByteArray &mimeType, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeERK10QByteArrayS2_NS_10Status'
        'CodeE',
        self._valueOf(data), self._valueOf(mimeType), status.value,
    )

  @overload(QHttpHeaders)
  @overload(QHttpHeaders, StatusCode)
  def write(
      self,
      headers: QHttpHeaders,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(const QHttpHeaders &headers,
    StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(const QHttpHeaders &headers,
    #      StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeERK12QHttpHeadersNS_10StatusC'
        'odeE',
        self._valueOf(headers), status.value,
    )

  @overload()
  @overload(StatusCode)
  def write(self, status: StatusCode = StatusCode.Ok) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::write(StatusCode status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverresponder.html#write

    Parameters
    ----------

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::write(StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder5writeENS_10StatusCodeE',
        status.value,
    )

  @overload(QHttpHeaders)
  @overload(QHttpHeaders, StatusCode)
  def writeBeginChunked(
      self,
      headers: QHttpHeaders,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::writeBeginChunked(const
    QHttpHeaders &headers, StatusCode status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#writeBeginChunked

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::writeBeginChunked(const QHttpHeaders
    #      &headers, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder17writeBeginChunkedERK12QHttpHeader'
        'sNS_10StatusCodeE',
        self._valueOf(headers), status.value,
    )

  @overload(QByteArray)
  @overload(QByteArray, StatusCode)
  def writeBeginChunked(
      self,
      mimeType: QByteArray,
      status: StatusCode = StatusCode.Ok,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::writeBeginChunked(const QByteArray
    &mimeType, StatusCode status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#writeBeginChunked

    Parameters
    ----------

    mimeType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    status : StatusCode
      Passed on as its number. May be left out, as in Qt: it is then
      StatusCode.Ok.
    """
    #  void QHttpServerResponder::writeBeginChunked(const QByteArray
    #      &mimeType, StatusCode status)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder17writeBeginChunkedERK10QByteArrayN'
        'S_10StatusCodeE',
        self._valueOf(mimeType), status.value,
    )

  @overload(QByteArray)
  def writeChunk(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::writeChunk(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#writeChunk

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpServerResponder::writeChunk(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder10writeChunkERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray, QHttpHeaders)
  def writeEndChunked(
      self,
      data: QByteArray,
      trailers: QHttpHeaders,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::writeEndChunked(const QByteArray
    &data, const QHttpHeaders &trailers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#writeEndChunked

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    trailers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QHttpServerResponder::writeEndChunked(const QByteArray &data,
    #      const QHttpHeaders &trailers)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder15writeEndChunkedERK10QByteArrayRK1'
        '2QHttpHeaders',
        self._valueOf(data), self._valueOf(trailers),
    )

  @overload(QByteArray)
  def writeEndChunked(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpServerResponder::writeEndChunked(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponder.html#writeEndChunked

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpServerResponder::writeEndChunked(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN20QHttpServerResponder15writeEndChunkedERK10QByteArray',
        self._valueOf(data),
    )

  @staticmethod
  def sendResponse(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponder::sendResponse(const QHttpServerResponse
    &response)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerResponder.sendResponse' has no cute function yet. Qt's "
        "'void QHttpServerResponder::sendResponse(const QHttpServerResponse "
        "&response)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponder::swap(QHttpServerResponder &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpServerResponder.swap' has no cute function yet. Qt's 'void "
        "QHttpServerResponder::swap(QHttpServerResponder &other)': takes a "
        "type Python has no way to hand over yet.")
