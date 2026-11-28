"""
QOpcUaHistoryReadResponseImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponseimpl_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOpcUaHistoryReadResponseImpl to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpcUa, QOpcUaHistoryReadResponse

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QOpcUaHistoryData, QOpcUaHistoryEvent
  from . import QOpcUaHistoryReadEventRequest, QOpcUaHistoryReadRawRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpcUaHistoryData = WAIT['QOpcUaHistoryData']
  QOpcUaHistoryEvent = WAIT['QOpcUaHistoryEvent']
  QOpcUaHistoryReadEventRequest = WAIT['QOpcUaHistoryReadEventRequest']
  QOpcUaHistoryReadRawRequest = WAIT['QOpcUaHistoryReadRawRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaHistoryReadResponseImpl(QObject):
  """
  The cute side of Qt's QOpcUaHistoryReadResponseImpl: a plain Python object
  standing in front of one C++ QOpcUaHistoryReadResponseImpl.

  It is built on the cute 'QObject', as Qt's QOpcUaHistoryReadResponseImpl is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryReadResponseImpl that has a ritual and
  that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'hasMoreData', 'readMoreData', 'state', 'releaseContinuationPoints',
  'data', 'events', 'serviceResult', 'handleDataAvailable',
  'handleEventsAvailable', 'handleRequestError', 'handle',
  'historyReadRawRequested', 'historyReadEventsRequested',
  'readHistoryDataFinished', 'readHistoryEventsFinished', 'stateChanged',
  'setState', 'createReadRawRequestWithContinuationPoints',
  'createEventRequestWithContinuationPoints'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaHistoryReadResponseImpl::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QOpcUaHistoryReadResponseImpl::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaHistoryReadResponseImpl::~QOpcUaHistoryReadResponseImpl()':
    the destructor: Python never removes a C++ QOpcUaHistoryReadResponseImpl.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaHistoryReadResponseImpl is created at the first use, not by
    'QOpcUaHistoryReadResponseImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaHistoryReadResponseImpl.
  - Qt tells when it has removed the C++ QOpcUaHistoryReadResponseImpl. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QOpcUaHistoryReadResponseImpl::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#tr

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
    #  QString QOpcUaHistoryReadResponseImpl::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryReadResponseImpl'

  #  A C++ QOpcUaHistoryReadResponseImpl Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaHistoryReadResponseImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QOpcUaHistoryReadResponseImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaHistoryReadResponseImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasMoreData(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadResponseImpl::hasMoreData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#hasMoreData
    """
    #  bool QOpcUaHistoryReadResponseImpl::hasMoreData() const
    return self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl11hasMoreDataEv',
    )

  def state(self) -> QOpcUaHistoryReadResponse.State:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse::State
    QOpcUaHistoryReadResponseImpl::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#state

    Returns
    -------

    QOpcUaHistoryReadResponse.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaHistoryReadResponse.State(number)' gives.
    """
    #  QOpcUaHistoryReadResponse::State
    #      QOpcUaHistoryReadResponseImpl::state() const
    return QOpcUaHistoryReadResponse.State(self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl5stateEv',
    ))

  def data(self) -> QList[QOpcUaHistoryData]:
    """
    Calls Qt's 'QList<QOpcUaHistoryData>
    QOpcUaHistoryReadResponseImpl::data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#data

    Returns
    -------

    QList[QOpcUaHistoryData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaHistoryData> QOpcUaHistoryReadResponseImpl::data() const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl4dataEv',
    )
    from . import QOpcUaHistoryData
    return QList[QOpcUaHistoryData]._cuteOwning(address)

  def events(self) -> QList[QOpcUaHistoryEvent]:
    """
    Calls Qt's 'QList<QOpcUaHistoryEvent>
    QOpcUaHistoryReadResponseImpl::events() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#events

    Returns
    -------

    QList[QOpcUaHistoryEvent]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaHistoryEvent> QOpcUaHistoryReadResponseImpl::events()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl6eventsEv',
    )
    from . import QOpcUaHistoryEvent
    return QList[QOpcUaHistoryEvent]._cuteOwning(address)

  def serviceResult(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode
    QOpcUaHistoryReadResponseImpl::serviceResult() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#serviceResult

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaHistoryReadResponseImpl::serviceResult()
    #      const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl13serviceResultEv',
    ))

  def handle(self) -> int:
    """
    Calls Qt's 'quint64 QOpcUaHistoryReadResponseImpl::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#handle
    """
    #  quint64 QOpcUaHistoryReadResponseImpl::handle() const
    return self.uglySide.call(
        'ritual_ZNK29QOpcUaHistoryReadResponseImpl6handleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaHistoryReadResponse.State)
  def setState(self, state: QOpcUaHistoryReadResponse.State) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::setState(QOpcUaHistoryReadResponse::State
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#setState

    Parameters
    ----------

    state : QOpcUaHistoryReadResponse.State
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponseImpl::setState(
    #      QOpcUaHistoryReadResponse::State state)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl8setStateEN25QOpcUaHistory'
        'ReadResponse5StateE',
        state.value,
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

  @overload(QOpcUaHistoryReadRawRequest)
  def __init__(self, request: QOpcUaHistoryReadRawRequest) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
    QOpcUaHistoryReadRawRequest &request)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    request : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.
    """
    #  QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
    #      QOpcUaHistoryReadRawRequest &request)
    self._noteCreation(QOpcUaHistoryReadResponseImpl, lambda: Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImplC1ERK27QOpcUaHistoryReadRa'
        'wRequest',
        self._valueOf(request),
    ))

  @overload(QOpcUaHistoryReadEventRequest)
  def __init__(self, request: QOpcUaHistoryReadEventRequest) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
    QOpcUaHistoryReadEventRequest &request)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    request : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.
    """
    #  QOpcUaHistoryReadResponseImpl::QOpcUaHistoryReadResponseImpl(const
    #      QOpcUaHistoryReadEventRequest &request)
    self._noteCreation(QOpcUaHistoryReadResponseImpl, lambda: Rituals.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImplC1ERK29QOpcUaHistoryReadEv'
        'entRequest',
        self._valueOf(request),
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

  def readMoreData(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaHistoryReadResponseImpl::readMoreData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#readMoreData
    """
    #  bool QOpcUaHistoryReadResponseImpl::readMoreData()
    return self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl12readMoreDataEv',
    )

  def releaseContinuationPoints(self) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaHistoryReadResponseImpl::releaseContinuationPoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html
    """
    #  bool QOpcUaHistoryReadResponseImpl::releaseContinuationPoints()
    return self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl25releaseContinuationPoint'
        'sEv',
    )

  @overload(
      QList[QOpcUaHistoryData], QList[QByteArray], QOpcUa.UaStatusCode, int,
  )
  def handleDataAvailable(
      self,
      data: QList[QOpcUaHistoryData],
      continuationPoints: QList[QByteArray],
      serviceResult: QOpcUa.UaStatusCode,
      responseHandle: int,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadResponseImpl::handleDataAvailable(const
    QList<QOpcUaHistoryData> &data, const QList<QByteArray>
    &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
    responseHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    data : QList[QOpcUaHistoryData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    continuationPoints : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.

    responseHandle : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadResponseImpl::handleDataAvailable(const
    #      QList<QOpcUaHistoryData> &data, const QList<QByteArray>
    #      &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
    #      responseHandle)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl19handleDataAvailableERK5Q'
        'ListI17QOpcUaHistoryDataERKS0_I10QByteArrayEN6QOpcUa12UaStatusCode'
        'Ey',
        self._valueOf(data), self._valueOf(continuationPoints),
        serviceResult.value, responseHandle,
    )

  @overload(
      QList[QOpcUaHistoryEvent], QList[QByteArray], QOpcUa.UaStatusCode, int,
  )
  def handleEventsAvailable(
      self,
      data: QList[QOpcUaHistoryEvent],
      continuationPoints: QList[QByteArray],
      serviceResult: QOpcUa.UaStatusCode,
      responseHandle: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::handleEventsAvailable(const
    QList<QOpcUaHistoryEvent> &data, const QList<QByteArray>
    &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
    responseHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    data : QList[QOpcUaHistoryEvent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    continuationPoints : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.

    responseHandle : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadResponseImpl::handleEventsAvailable(const
    #      QList<QOpcUaHistoryEvent> &data, const QList<QByteArray>
    #      &continuationPoints, QOpcUa::UaStatusCode serviceResult, quint64
    #      responseHandle)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl21handleEventsAvailableERK'
        '5QListI18QOpcUaHistoryEventERKS0_I10QByteArrayEN6QOpcUa12UaStatusC'
        'odeEy',
        self._valueOf(data), self._valueOf(continuationPoints),
        serviceResult.value, responseHandle,
    )

  @overload(int)
  def handleRequestError(self, requestHandle: int) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::handleRequestError(quint64
    requestHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    requestHandle : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadResponseImpl::handleRequestError(quint64
    #      requestHandle)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl18handleRequestErrorEy',
        requestHandle,
    )

  @overload(QOpcUaHistoryReadRawRequest, QList[QByteArray], bool, int)
  def historyReadRawRequested(
      self,
      request: QOpcUaHistoryReadRawRequest,
      continuationPoints: QList[QByteArray],
      releaseContinuationPoints: bool,
      handle: int,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadResponseImpl::historyReadRawRequested(
    QOpcUaHistoryReadRawRequest request, QList<QByteArray>
    continuationPoints, bool releaseContinuationPoints, quint64 handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    request : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.

    continuationPoints : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    releaseContinuationPoints : bool
      Passed on as it is.

    handle : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadResponseImpl::historyReadRawRequested(
    #      QOpcUaHistoryReadRawRequest request, QList<QByteArray>
    #      continuationPoints, bool releaseContinuationPoints, quint64
    #      handle)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl23historyReadRawRequestedE'
        '27QOpcUaHistoryReadRawRequest5QListI10QByteArrayEby',
        self._valueOf(request), self._valueOf(continuationPoints),
        releaseContinuationPoints, handle,
    )

  @overload(QOpcUaHistoryReadEventRequest, QList[QByteArray], bool, int)
  def historyReadEventsRequested(
      self,
      request: QOpcUaHistoryReadEventRequest,
      continuationPoints: QList[QByteArray],
      releaseContinuationPoints: bool,
      handle: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::historyReadEventsRequested(
    QOpcUaHistoryReadEventRequest request, QList<QByteArray>
    continuationPoints, bool releaseContinuationPoints, quint64 handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    request : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.

    continuationPoints : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    releaseContinuationPoints : bool
      Passed on as it is.

    handle : int
      Passed on as it is.
    """
    #  void QOpcUaHistoryReadResponseImpl::historyReadEventsRequested(
    #      QOpcUaHistoryReadEventRequest request, QList<QByteArray>
    #      continuationPoints, bool releaseContinuationPoints, quint64
    #      handle)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl26historyReadEventsRequest'
        'edE29QOpcUaHistoryReadEventRequest5QListI10QByteArrayEby',
        self._valueOf(request), self._valueOf(continuationPoints),
        releaseContinuationPoints, handle,
    )

  @overload(QList[QOpcUaHistoryData], QOpcUa.UaStatusCode)
  def readHistoryDataFinished(
      self,
      results: QList[QOpcUaHistoryData],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaHistoryReadResponseImpl::readHistoryDataFinished(
    QList<QOpcUaHistoryData> results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    results : QList[QOpcUaHistoryData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponseImpl::readHistoryDataFinished(
    #      QList<QOpcUaHistoryData> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl23readHistoryDataFinishedE'
        '5QListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QList[QOpcUaHistoryEvent], QOpcUa.UaStatusCode)
  def readHistoryEventsFinished(
      self,
      results: QList[QOpcUaHistoryEvent],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::readHistoryEventsFinished(
    QList<QOpcUaHistoryEvent> results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Parameters
    ----------

    results : QList[QOpcUaHistoryEvent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponseImpl::readHistoryEventsFinished(
    #      QList<QOpcUaHistoryEvent> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl25readHistoryEventsFinishe'
        'dE5QListI18QOpcUaHistoryEventEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QOpcUaHistoryReadResponse.State)
  def stateChanged(self, state: QOpcUaHistoryReadResponse.State) -> None:
    """
    Calls Qt's 'void
    QOpcUaHistoryReadResponseImpl::stateChanged(QOpcUaHistoryReadResponse::
    State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html#stateChanged

    Parameters
    ----------

    state : QOpcUaHistoryReadResponse.State
      Passed on as its number.
    """
    #  void QOpcUaHistoryReadResponseImpl::stateChanged(
    #      QOpcUaHistoryReadResponse::State state)
    self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl12stateChangedEN25QOpcUaHi'
        'storyReadResponse5StateE',
        state.value,
    )

  def createReadRawRequestWithContinuationPoints(
      self,
  ) -> QOpcUaHistoryReadRawRequest:
    """
    Calls Qt's 'QOpcUaHistoryReadRawRequest QOpcUaHistoryReadResponseImpl::
    createReadRawRequestWithContinuationPoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Returns
    -------

    QOpcUaHistoryReadRawRequest
      A new cute QOpcUaHistoryReadRawRequest around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaHistoryReadRawRequest QOpcUaHistoryReadResponseImpl::
    #      createReadRawRequestWithContinuationPoints()
    address = self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl42createReadRawRequestWith'
        'ContinuationPointsEv',
    )
    from . import QOpcUaHistoryReadRawRequest
    return QOpcUaHistoryReadRawRequest._cuteOwning(address)

  def createEventRequestWithContinuationPoints(
      self,
  ) -> QOpcUaHistoryReadEventRequest:
    """
    Calls Qt's 'QOpcUaHistoryReadEventRequest
    QOpcUaHistoryReadResponseImpl::createEventRequestWithContinuationPoints(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseimpl.html

    Returns
    -------

    QOpcUaHistoryReadEventRequest
      A new cute QOpcUaHistoryReadEventRequest around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaHistoryReadEventRequest QOpcUaHistoryReadResponseImpl::
    #      createEventRequestWithContinuationPoints()
    address = self.uglySide.call(
        'ritual_ZN29QOpcUaHistoryReadResponseImpl40createEventRequestWithCo'
        'ntinuationPointsEv',
    )
    from . import QOpcUaHistoryReadEventRequest
    return QOpcUaHistoryReadEventRequest._cuteOwning(address)
