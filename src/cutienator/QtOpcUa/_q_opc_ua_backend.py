"""
QOpcUaBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuabackend_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpcUaBackend to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QOpcUa, QOpcUaClient, QOpcUaMonitoringParameters

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QString, QUrl, QVariant
  from . import QOpcUaApplicationDescription, QOpcUaBrowsePathTarget
  from . import QOpcUaEndpointDescription, QOpcUaErrorState
  from . import QOpcUaExpandedNodeId, QOpcUaHistoryData, QOpcUaHistoryEvent
  from . import QOpcUaHistoryReadRawRequest, QOpcUaReadResult
  from . import QOpcUaReferenceDescription, QOpcUaRelativePathElement
  from . import QOpcUaWriteResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpcUaApplicationDescription = WAIT['QOpcUaApplicationDescription']
  QOpcUaBrowsePathTarget = WAIT['QOpcUaBrowsePathTarget']
  QOpcUaEndpointDescription = WAIT['QOpcUaEndpointDescription']
  QOpcUaErrorState = WAIT['QOpcUaErrorState']
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']
  QOpcUaHistoryData = WAIT['QOpcUaHistoryData']
  QOpcUaHistoryEvent = WAIT['QOpcUaHistoryEvent']
  QOpcUaHistoryReadRawRequest = WAIT['QOpcUaHistoryReadRawRequest']
  QOpcUaReadResult = WAIT['QOpcUaReadResult']
  QOpcUaReferenceDescription = WAIT['QOpcUaReferenceDescription']
  QOpcUaRelativePathElement = WAIT['QOpcUaRelativePathElement']
  QOpcUaWriteResult = WAIT['QOpcUaWriteResult']
  QString = WAIT['QString']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaBackend(QObject):
  """
  The cute side of Qt's QOpcUaBackend: a plain Python object standing in
  front of one C++ QOpcUaBackend.

  It is built on the cute 'QObject', as Qt's QOpcUaBackend is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaBackend that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'nodeAttributeEnumBits',
  'attributeIdToTypeId', 'revisePublishingInterval',
  'verifyEndpointDescription', 'stateAndOrErrorChanged', 'attributesRead',
  'attributeWritten', 'methodCallFinished', 'dataChangeOccurred',
  'eventOccurred', 'monitoringEnableDisable', 'monitoringStatusChanged',
  'browseFinished', 'resolveBrowsePathFinished', 'endpointsRequestFinished',
  'findServersFinished', 'readNodeAttributesFinished',
  'writeNodeAttributesFinished', 'readHistoryDataFinished',
  'addNodeFinished', 'deleteNodeFinished', 'addReferenceFinished',
  'deleteReferenceFinished', 'connectError', 'passwordForPrivateKeyRequired',
  'historyDataAvailable', 'historyEventsAvailable', 'registerNodesFinished',
  'unregisterNodesFinished'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaBackend::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpcUaBackend::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaBackend::~QOpcUaBackend()': the destructor: Python never
    removes a C++ QOpcUaBackend.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpcUaBackend is created at the first use, not by
    'QOpcUaBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaBackend.
  - Qt tells when it has removed the C++ QOpcUaBackend. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QOpcUaBackend::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#tr

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
    #  QString QOpcUaBackend::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QOpcUaBackend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def nodeAttributeEnumBits() -> int:
    """
    Calls Qt's 'size_t QOpcUaBackend::nodeAttributeEnumBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#nodeAttributeEnumBits
    """
    #  size_t QOpcUaBackend::nodeAttributeEnumBits()
    return Rituals.call('ritual_ZN13QOpcUaBackend21nodeAttributeEnumBitsEv')

  @staticmethod
  @overload(QOpcUaEndpointDescription)
  @overload(QOpcUaEndpointDescription, QString)
  @overload(QOpcUaEndpointDescription, NoneType)
  def verifyEndpointDescription(
      endpoint: QOpcUaEndpointDescription,
      message: Optional[QString] = None,
  ) -> QOpcUaClient.ClientError:
    """
    Calls Qt's 'QOpcUaClient::ClientError
    QOpcUaBackend::verifyEndpointDescription(const QOpcUaEndpointDescription
    &endpoint, QString *message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#verifyEndpointDescription

    Parameters
    ----------

    endpoint : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.

    message : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QOpcUaClient.ClientError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaClient.ClientError(number)' gives.
    """
    #  QOpcUaClient::ClientError
    #      QOpcUaBackend::verifyEndpointDescription(const
    #      QOpcUaEndpointDescription &endpoint, QString *message)
    return QOpcUaClient.ClientError(Rituals.call(
        'ritual_ZN13QOpcUaBackend25verifyEndpointDescriptionERK25QOpcUaEndp'
        'ointDescriptionP7QString',
        CuteMixin._valueOf(endpoint), CuteMixin._addressOf(message),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaBackend'

  #  A C++ QOpcUaBackend Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaBackend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaBackend::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaBackend::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QOpcUaBackend10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QOpcUaBackend::QOpcUaBackend()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#QOpcUaBackend
    """
    #  QOpcUaBackend::QOpcUaBackend()
    self._noteCreation(QOpcUaBackend, lambda: Rituals.call(
        'ritual_ZN13QOpcUaBackendC1Ev',
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

  @overload(QOpcUa.NodeAttribute)
  def attributeIdToTypeId(self, attr: QOpcUa.NodeAttribute) -> QOpcUa.Types:
    """
    Calls Qt's 'QOpcUa::Types
    QOpcUaBackend::attributeIdToTypeId(QOpcUa::NodeAttribute attr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#attributeIdToTypeId

    Parameters
    ----------

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    Returns
    -------

    QOpcUa.Types
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.Types(number)'
      gives.
    """
    #  QOpcUa::Types QOpcUaBackend::attributeIdToTypeId(QOpcUa::NodeAttribute
    #      attr)
    return QOpcUa.Types(self.uglySide.call(
        'ritual_ZN13QOpcUaBackend19attributeIdToTypeIdEN6QOpcUa13NodeAttrib'
        'uteE',
        attr.value,
    ))

  @overload(float, float)
  def revisePublishingInterval(
      self,
      requestedValue: float,
      minimumValue: float,
  ) -> float:
    """
    Calls Qt's 'double QOpcUaBackend::revisePublishingInterval(double
    requestedValue, double minimumValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#revisePublishingInterval

    Parameters
    ----------

    requestedValue : float
      Passed on as it is.

    minimumValue : float
      Passed on as it is.
    """
    #  double QOpcUaBackend::revisePublishingInterval(double requestedValue,
    #      double minimumValue)
    return self.uglySide.call(
        'ritual_ZN13QOpcUaBackend24revisePublishingIntervalEdd',
        requestedValue, minimumValue,
    )

  @overload(QOpcUaClient.ClientState, QOpcUaClient.ClientError)
  def stateAndOrErrorChanged(
      self,
      state: QOpcUaClient.ClientState,
      error: QOpcUaClient.ClientError,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::stateAndOrErrorChanged(QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#stateAndOrErrorChanged

    Parameters
    ----------

    state : QOpcUaClient.ClientState
      Passed on as its number.

    error : QOpcUaClient.ClientError
      Passed on as its number.
    """
    #  void QOpcUaBackend::stateAndOrErrorChanged(QOpcUaClient::ClientState
    #      state, QOpcUaClient::ClientError error)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend22stateAndOrErrorChangedEN12QOpcUaClient11'
        'ClientStateENS0_11ClientErrorE',
        state.value, error.value,
    )

  @overload(int, QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def attributesRead(
      self,
      handle: int,
      attributes: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::attributesRead(quint64 handle,
    QList<QOpcUaReadResult> attributes, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#attributesRead

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attributes : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::attributesRead(quint64 handle,
    #      QList<QOpcUaReadResult> attributes, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend14attributesReadEy5QListI16QOpcUaReadResul'
        'tEN6QOpcUa12UaStatusCodeE',
        handle, self._valueOf(attributes), serviceResult.value,
    )

  @overload(int, QOpcUa.NodeAttribute, QVariant, QOpcUa.UaStatusCode)
  def attributeWritten(
      self,
      handle: int,
      attribute: QOpcUa.NodeAttribute,
      value: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::attributeWritten(quint64 handle,
    QOpcUa::NodeAttribute attribute, QVariant value, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#attributeWritten

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attribute : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::attributeWritten(quint64 handle,
    #      QOpcUa::NodeAttribute attribute, QVariant value,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend16attributeWrittenEyN6QOpcUa13NodeAttribut'
        'eE8QVariantNS0_12UaStatusCodeE',
        handle, attribute.value, self._valueOf(value), statusCode.value,
    )

  @overload(int, str, QVariant, QOpcUa.UaStatusCode)
  def methodCallFinished(
      self,
      handle: int,
      methodNodeId: str,
      result: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::methodCallFinished(quint64 handle,
    QString methodNodeId, QVariant result, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#methodCallFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    methodNodeId : str
      Passed on as it is: a QString is made of it for the call.

    result : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::methodCallFinished(quint64 handle, QString
    #      methodNodeId, QVariant result, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend18methodCallFinishedEy7QString8QVariantN6Q'
        'OpcUa12UaStatusCodeE',
        handle, methodNodeId, self._valueOf(result), statusCode.value,
    )

  @overload(int, QOpcUaReadResult)
  def dataChangeOccurred(self, handle: int, res: QOpcUaReadResult) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::dataChangeOccurred(quint64 handle,
    QOpcUaReadResult res)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#dataChangeOccurred

    Parameters
    ----------

    handle : int
      Passed on as it is.

    res : QOpcUaReadResult
      Passed on as a value: Qt reads the C++ QOpcUaReadResult, which stays
      Python's own.
    """
    #  void QOpcUaBackend::dataChangeOccurred(quint64 handle,
    #      QOpcUaReadResult res)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend18dataChangeOccurredEy16QOpcUaReadResult',
        handle, self._valueOf(res),
    )

  @overload(int, QList[QVariant])
  def eventOccurred(self, handle: int, fields: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::eventOccurred(quint64 handle,
    QVariantList fields)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#eventOccurred

    Parameters
    ----------

    handle : int
      Passed on as it is.

    fields : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaBackend::eventOccurred(quint64 handle, QVariantList fields)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend13eventOccurredEy5QListI8QVariantE',
        handle, self._valueOf(fields),
    )

  @overload(int, QOpcUa.NodeAttribute, bool, QOpcUaMonitoringParameters)
  def monitoringEnableDisable(
      self,
      handle: int,
      attr: QOpcUa.NodeAttribute,
      subscribe: bool,
      status: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::monitoringEnableDisable(quint64 handle,
    QOpcUa::NodeAttribute attr, bool subscribe, QOpcUaMonitoringParameters
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#monitoringEnableDisable

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    subscribe : bool
      Passed on as it is.

    status : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaBackend::monitoringEnableDisable(quint64 handle,
    #      QOpcUa::NodeAttribute attr, bool subscribe,
    #      QOpcUaMonitoringParameters status)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend23monitoringEnableDisableEyN6QOpcUa13NodeA'
        'ttributeEb26QOpcUaMonitoringParameters',
        handle, attr.value, subscribe, self._valueOf(status),
    )

  @overload(
      int, QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameters,
      QOpcUaMonitoringParameters,
  )
  def monitoringStatusChanged(
      self,
      handle: int,
      attr: QOpcUa.NodeAttribute,
      items: QOpcUaMonitoringParameters.Parameters,
      param: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::monitoringStatusChanged(quint64 handle,
    QOpcUa::NodeAttribute attr, QOpcUaMonitoringParameters::Parameters items,
    QOpcUaMonitoringParameters param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#monitoringStatusChanged

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    items : QOpcUaMonitoringParameters.Parameters
      Passed on as its number.

    param : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaBackend::monitoringStatusChanged(quint64 handle,
    #      QOpcUa::NodeAttribute attr, QOpcUaMonitoringParameters::Parameters
    #      items, QOpcUaMonitoringParameters param)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend23monitoringStatusChangedEyN6QOpcUa13NodeA'
        'ttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterEES3_',
        handle, attr.value, items.value, self._valueOf(param),
    )

  @overload(int, QList[QOpcUaReferenceDescription], QOpcUa.UaStatusCode)
  def browseFinished(
      self,
      handle: int,
      children: QList[QOpcUaReferenceDescription],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::browseFinished(quint64 handle,
    QList<QOpcUaReferenceDescription> children, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#browseFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    children : QList[QOpcUaReferenceDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::browseFinished(quint64 handle,
    #      QList<QOpcUaReferenceDescription> children, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend14browseFinishedEy5QListI26QOpcUaReference'
        'DescriptionEN6QOpcUa12UaStatusCodeE',
        handle, self._valueOf(children), statusCode.value,
    )

  @overload(
      int, QList[QOpcUaBrowsePathTarget], QList[QOpcUaRelativePathElement],
      QOpcUa.UaStatusCode,
  )
  def resolveBrowsePathFinished(
      self,
      handle: int,
      targets: QList[QOpcUaBrowsePathTarget],
      path: QList[QOpcUaRelativePathElement],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::resolveBrowsePathFinished(quint64 handle,
    const QList<QOpcUaBrowsePathTarget> &targets, const
    QList<QOpcUaRelativePathElement> &path, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#resolveBrowsePathFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    targets : QList[QOpcUaBrowsePathTarget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    path : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::resolveBrowsePathFinished(quint64 handle, const
    #      QList<QOpcUaBrowsePathTarget> &targets, const
    #      QList<QOpcUaRelativePathElement> &path, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend25resolveBrowsePathFinishedEyRK5QListI22QO'
        'pcUaBrowsePathTargetERKS0_I25QOpcUaRelativePathElementEN6QOpcUa12U'
        'aStatusCodeE',
        handle, self._valueOf(targets), self._valueOf(path),
        statusCode.value,
    )

  @overload(QList[QOpcUaEndpointDescription], QOpcUa.UaStatusCode, QUrl)
  def endpointsRequestFinished(
      self,
      endpoints: QList[QOpcUaEndpointDescription],
      statusCode: QOpcUa.UaStatusCode,
      requestUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::endpointsRequestFinished(QList<QOpcUaEndpointDescription>
    endpoints, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#endpointsRequestFinished

    Parameters
    ----------

    endpoints : QList[QOpcUaEndpointDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOpcUaBackend::endpointsRequestFinished(
    #      QList<QOpcUaEndpointDescription> endpoints, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend24endpointsRequestFinishedE5QListI25QOpcUa'
        'EndpointDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
        self._valueOf(endpoints), statusCode.value,
        self._valueOf(requestUrl),
    )

  @overload(QList[QOpcUaApplicationDescription], QOpcUa.UaStatusCode, QUrl)
  def findServersFinished(
      self,
      servers: QList[QOpcUaApplicationDescription],
      statusCode: QOpcUa.UaStatusCode,
      requestUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::findServersFinished(QList<QOpcUaApplicationDescription>
    servers, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#findServersFinished

    Parameters
    ----------

    servers : QList[QOpcUaApplicationDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOpcUaBackend::findServersFinished(
    #      QList<QOpcUaApplicationDescription> servers, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend19findServersFinishedE5QListI28QOpcUaAppli'
        'cationDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
        self._valueOf(servers), statusCode.value, self._valueOf(requestUrl),
    )

  @overload(QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def readNodeAttributesFinished(
      self,
      results: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::readNodeAttributesFinished(QList<QOpcUaReadResult>
    results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#readNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::readNodeAttributesFinished(QList<QOpcUaReadResult>
    #      results, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend26readNodeAttributesFinishedE5QListI16QOpc'
        'UaReadResultEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QList[QOpcUaWriteResult], QOpcUa.UaStatusCode)
  def writeNodeAttributesFinished(
      self,
      results: QList[QOpcUaWriteResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::writeNodeAttributesFinished(QList<QOpcUaWriteResult>
    results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#writeNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaWriteResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::writeNodeAttributesFinished(
    #      QList<QOpcUaWriteResult> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend27writeNodeAttributesFinishedE5QListI17QOp'
        'cUaWriteResultEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(
      int, bool, QOpcUaHistoryReadRawRequest, QList[QOpcUaHistoryData],
      QOpcUa.UaStatusCode,
  )
  def readHistoryDataFinished(
      self,
      handle: int,
      isHandleValid: bool,
      request: QOpcUaHistoryReadRawRequest,
      results: QList[QOpcUaHistoryData],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::readHistoryDataFinished(quint64 handle,
    bool isHandleValid, QOpcUaHistoryReadRawRequest request,
    QList<QOpcUaHistoryData> results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#readHistoryDataFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    isHandleValid : bool
      Passed on as it is.

    request : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.

    results : QList[QOpcUaHistoryData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::readHistoryDataFinished(quint64 handle, bool
    #      isHandleValid, QOpcUaHistoryReadRawRequest request,
    #      QList<QOpcUaHistoryData> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend23readHistoryDataFinishedEyb27QOpcUaHistor'
        'yReadRawRequest5QListI17QOpcUaHistoryDataEN6QOpcUa12UaStatusCodeE',
        handle, isHandleValid, self._valueOf(request),
        self._valueOf(results), serviceResult.value,
    )

  @overload(QOpcUaExpandedNodeId, str, QOpcUa.UaStatusCode)
  def addNodeFinished(
      self,
      requestedNodeId: QOpcUaExpandedNodeId,
      assignedNodeId: str,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::addNodeFinished(QOpcUaExpandedNodeId
    requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#addNodeFinished

    Parameters
    ----------

    requestedNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    assignedNodeId : str
      Passed on as it is: a QString is made of it for the call.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::addNodeFinished(QOpcUaExpandedNodeId
    #      requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend15addNodeFinishedE20QOpcUaExpandedNodeId7Q'
        'StringN6QOpcUa12UaStatusCodeE',
        self._valueOf(requestedNodeId), assignedNodeId, statusCode.value,
    )

  @overload(str, QOpcUa.UaStatusCode)
  def deleteNodeFinished(
      self,
      nodeId: str,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::deleteNodeFinished(QString nodeId,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#deleteNodeFinished

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::deleteNodeFinished(QString nodeId,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend18deleteNodeFinishedE7QStringN6QOpcUa12UaS'
        'tatusCodeE',
        nodeId, statusCode.value,
    )

  @overload(str, str, QOpcUaExpandedNodeId, bool, QOpcUa.UaStatusCode)
  def addReferenceFinished(
      self,
      sourceNodeId: str,
      referenceTypeId: str,
      targetNodeId: QOpcUaExpandedNodeId,
      isForwardReference: bool,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::addReferenceFinished(QString
    sourceNodeId, QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId,
    bool isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#addReferenceFinished

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    isForwardReference : bool
      Passed on as it is.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::addReferenceFinished(QString sourceNodeId, QString
    #      referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend20addReferenceFinishedE7QStringS0_20QOpcUa'
        'ExpandedNodeIdbN6QOpcUa12UaStatusCodeE',
        sourceNodeId, referenceTypeId, self._valueOf(targetNodeId),
        isForwardReference, statusCode.value,
    )

  @overload(str, str, QOpcUaExpandedNodeId, bool, QOpcUa.UaStatusCode)
  def deleteReferenceFinished(
      self,
      sourceNodeId: str,
      referenceTypeId: str,
      targetNodeId: QOpcUaExpandedNodeId,
      isForwardReference: bool,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::deleteReferenceFinished(QString
    sourceNodeId, QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId,
    bool isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#deleteReferenceFinished

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    isForwardReference : bool
      Passed on as it is.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::deleteReferenceFinished(QString sourceNodeId,
    #      QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend23deleteReferenceFinishedE7QStringS0_20QOp'
        'cUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE',
        sourceNodeId, referenceTypeId, self._valueOf(targetNodeId),
        isForwardReference, statusCode.value,
    )

  @overload(QOpcUaErrorState)
  @overload(NoneType)
  def connectError(self, errorState: Optional[QOpcUaErrorState]) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::connectError(QOpcUaErrorState
    *errorState)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuabackend.html#connectError

    Parameters
    ----------

    errorState : Optional[QOpcUaErrorState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaBackend::connectError(QOpcUaErrorState *errorState)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend12connectErrorEP16QOpcUaErrorState',
        self._addressOf(errorState),
    )

  @overload(str, QString, bool)
  @overload(str, NoneType, bool)
  def passwordForPrivateKeyRequired(
      self,
      keyFilePath: str,
      password: Optional[QString],
      previousTryWasInvalid: bool,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::passwordForPrivateKeyRequired(QString
    keyFilePath, QString *password, bool previousTryWasInvalid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#passwordForPrivateKeyRequired

    Parameters
    ----------

    keyFilePath : str
      Passed on as it is: a QString is made of it for the call.

    password : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previousTryWasInvalid : bool
      Passed on as it is.
    """
    #  void QOpcUaBackend::passwordForPrivateKeyRequired(QString keyFilePath,
    #      QString *password, bool previousTryWasInvalid)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend29passwordForPrivateKeyRequiredE7QStringPS'
        '0_b',
        keyFilePath, self._addressOf(password), previousTryWasInvalid,
    )

  @overload(
      QList[QOpcUaHistoryData], QList[QByteArray], QOpcUa.UaStatusCode, int,
  )
  def historyDataAvailable(
      self,
      data: QList[QOpcUaHistoryData],
      continuationPoints: QList[QByteArray],
      serviceResult: QOpcUa.UaStatusCode,
      handle: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::historyDataAvailable(QList<QOpcUaHistoryData> data,
    QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode serviceResult,
    uintptr_t handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#historyDataAvailable

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

    handle : int
      Passed on as it is.
    """
    #  void QOpcUaBackend::historyDataAvailable(QList<QOpcUaHistoryData>
    #      data, QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode
    #      serviceResult, uintptr_t handle)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend20historyDataAvailableE5QListI17QOpcUaHist'
        'oryDataES0_I10QByteArrayEN6QOpcUa12UaStatusCodeEm',
        self._valueOf(data), self._valueOf(continuationPoints),
        serviceResult.value, handle,
    )

  @overload(
      QList[QOpcUaHistoryEvent], QList[QByteArray], QOpcUa.UaStatusCode, int,
  )
  def historyEventsAvailable(
      self,
      data: QList[QOpcUaHistoryEvent],
      continuationPoints: QList[QByteArray],
      serviceResult: QOpcUa.UaStatusCode,
      handle: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaBackend::historyEventsAvailable(QList<QOpcUaHistoryEvent> data,
    QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode serviceResult,
    uintptr_t handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#historyEventsAvailable

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

    handle : int
      Passed on as it is.
    """
    #  void QOpcUaBackend::historyEventsAvailable(QList<QOpcUaHistoryEvent>
    #      data, QList<QByteArray> continuationPoints, QOpcUa::UaStatusCode
    #      serviceResult, uintptr_t handle)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend22historyEventsAvailableE5QListI18QOpcUaHi'
        'storyEventES0_I10QByteArrayEN6QOpcUa12UaStatusCodeEm',
        self._valueOf(data), self._valueOf(continuationPoints),
        serviceResult.value, handle,
    )

  @overload(QStringList, QStringList, QOpcUa.UaStatusCode)
  def registerNodesFinished(
      self,
      nodesToRegister: QStringList,
      registeredNodeIds: QStringList,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::registerNodesFinished(QStringList
    nodesToRegister, QStringList registeredNodeIds, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#registerNodesFinished

    Parameters
    ----------

    nodesToRegister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    registeredNodeIds : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::registerNodesFinished(QStringList nodesToRegister,
    #      QStringList registeredNodeIds, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend21registerNodesFinishedE5QListI7QStringES2'
        '_N6QOpcUa12UaStatusCodeE',
        self._valueOf(nodesToRegister), self._valueOf(registeredNodeIds),
        statusCode.value,
    )

  @overload(QStringList, QOpcUa.UaStatusCode)
  def unregisterNodesFinished(
      self,
      nodesToUnregister: QStringList,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaBackend::unregisterNodesFinished(QStringList
    nodesToUnregister, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabackend.html#unregisterNodesFinished

    Parameters
    ----------

    nodesToUnregister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaBackend::unregisterNodesFinished(QStringList
    #      nodesToUnregister, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN13QOpcUaBackend23unregisterNodesFinishedE5QListI7QStringE'
        'N6QOpcUa12UaStatusCodeE',
        self._valueOf(nodesToUnregister), statusCode.value,
    )
