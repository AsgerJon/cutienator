"""
QOpcUaGdsClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuagdsclient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QOpcUaApplicationIdentity, QOpcUaApplicationRecordDataType
  from . import QOpcUaEndpointDescription, QOpcUaPkiConfiguration
  from . import QOpcUaX509DistinguishedName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaApplicationIdentity = WAIT['QOpcUaApplicationIdentity']
  QOpcUaApplicationRecordDataType = WAIT['QOpcUaApplicationRecordDataType']
  QOpcUaEndpointDescription = WAIT['QOpcUaEndpointDescription']
  QOpcUaPkiConfiguration = WAIT['QOpcUaPkiConfiguration']
  QOpcUaX509DistinguishedName = WAIT['QOpcUaX509DistinguishedName']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaGdsClient(QObject):
  """
  The cute side of Qt's QOpcUaGdsClient: a plain Python object standing in
  front of one C++ QOpcUaGdsClient.

  It is built on the cute 'QObject', as Qt's QOpcUaGdsClient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaGdsClient that has a ritual and that Python
  can call so far, 32 names in all: 'metaObject', 'tr', 'setBackend',
  'backend', 'setEndpoint', 'endpoint', 'setPkiConfiguration',
  'pkiConfiguration', 'setApplicationIdentity', 'applicationIdentity',
  'setApplicationRecord', 'applicationRecord', 'applicationId',
  'setCertificateSigningRequestPresets',
  'distinguishedNameCertificateSigningRequestPreset',
  'dnsCertificateSigningRequestPreset', 'setCertificateCheckInterval',
  'certificateCheckInterval', 'setTrustListUpdateInterval',
  'trustListUpdateInterval', 'error', 'state', 'start',
  'unregisterApplication', 'stateChanged', 'errorChanged',
  'applicationRegistered', 'certificateGroupsReceived',
  'certificateUpdateRequired', 'certificateUpdated', 'unregistered',
  'trustListUpdated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaGdsClient::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpcUaGdsClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaGdsClientPrivate *QOpcUaGdsClient::d_func()': gives
    'QOpcUaGdsClientPrivate', which has no cute class yet.
  - Qt's 'const QOpcUaGdsClientPrivate *QOpcUaGdsClient::d_func() const':
    gives 'QOpcUaGdsClientPrivate', which has no cute class yet.
  - Qt's 'QOpcUaGdsClient::~QOpcUaGdsClient()': the destructor: Python never
    removes a C++ QOpcUaGdsClient.
  - Qt's 'void
    QOpcUaGdsClient::authenticationRequired(QOpcUaAuthenticationInformation
    &authInfo)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaGdsClient is created at the first use, not by
    'QOpcUaGdsClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaGdsClient.
  - Qt tells when it has removed the C++ QOpcUaGdsClient. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaGdsClient that has no cute function yet,
    'authenticationRequired', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaGdsClient, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QOpcUaGdsClient::Error' of Qt, with the 9 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoError = Kee[int](0)
    InvalidBackend = Kee[int](1)
    InvalidEndpoint = Kee[int](2)
    ConnectionError = Kee[int](3)
    DirectoryNodeNotFound = Kee[int](4)
    FailedToRegisterApplication = Kee[int](5)
    FailedToUnregisterApplication = Kee[int](6)
    FailedToGetCertificateStatus = Kee[int](7)
    FailedToGetCertificate = Kee[int](8)

  class State(CuteNum, scoped=True):
    """
    The enum 'QOpcUaGdsClient::State' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Idle = Kee[int](0)
    BackendInstantiated = Kee[int](1)
    Connecting = Kee[int](2)
    Connected = Kee[int](3)
    RegisteringApplication = Kee[int](4)
    ApplicationRegistered = Kee[int](5)
    Error = Kee[int](6)

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
    Calls Qt's 'QString QOpcUaGdsClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#tr

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
    #  QString QOpcUaGdsClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QOpcUaGdsClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaGdsClient'

  #  A C++ QOpcUaGdsClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaGdsClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaGdsClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaGdsClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QOpcUaGdsClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def backend(self) -> str:
    """
    Calls Qt's 'const QString &QOpcUaGdsClient::backend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#backend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QOpcUaGdsClient::backend() const
    return self.uglySide.call('ritual_ZNK15QOpcUaGdsClient7backendEv')

  def endpoint(self) -> QOpcUaEndpointDescription:
    """
    Calls Qt's 'const QOpcUaEndpointDescription &QOpcUaGdsClient::endpoint()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#endpoint

    Returns
    -------

    QOpcUaEndpointDescription
      A new cute QOpcUaEndpointDescription around the copy Qt gave back.
      Python owns it.
    """
    #  const QOpcUaEndpointDescription &QOpcUaGdsClient::endpoint() const
    address = self.uglySide.call('ritual_ZNK15QOpcUaGdsClient8endpointEv')
    from . import QOpcUaEndpointDescription
    return QOpcUaEndpointDescription._cuteOwning(address)

  def pkiConfiguration(self) -> QOpcUaPkiConfiguration:
    """
    Calls Qt's 'const QOpcUaPkiConfiguration
    &QOpcUaGdsClient::pkiConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#pkiConfiguration

    Returns
    -------

    QOpcUaPkiConfiguration
      A new cute QOpcUaPkiConfiguration around the copy Qt gave back. Python
      owns it.
    """
    #  const QOpcUaPkiConfiguration &QOpcUaGdsClient::pkiConfiguration()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient16pkiConfigurationEv',
    )
    from . import QOpcUaPkiConfiguration
    return QOpcUaPkiConfiguration._cuteOwning(address)

  def applicationIdentity(self) -> QOpcUaApplicationIdentity:
    """
    Calls Qt's 'const QOpcUaApplicationIdentity
    &QOpcUaGdsClient::applicationIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#applicationIdentity

    Returns
    -------

    QOpcUaApplicationIdentity
      A new cute QOpcUaApplicationIdentity around the copy Qt gave back.
      Python owns it.
    """
    #  const QOpcUaApplicationIdentity
    #      &QOpcUaGdsClient::applicationIdentity() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient19applicationIdentityEv',
    )
    from . import QOpcUaApplicationIdentity
    return QOpcUaApplicationIdentity._cuteOwning(address)

  def applicationRecord(self) -> QOpcUaApplicationRecordDataType:
    """
    Calls Qt's 'const QOpcUaApplicationRecordDataType
    &QOpcUaGdsClient::applicationRecord() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#applicationRecord

    Returns
    -------

    QOpcUaApplicationRecordDataType
      A new cute QOpcUaApplicationRecordDataType around the copy Qt gave
      back. Python owns it.
    """
    #  const QOpcUaApplicationRecordDataType
    #      &QOpcUaGdsClient::applicationRecord() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient17applicationRecordEv',
    )
    from . import QOpcUaApplicationRecordDataType
    return QOpcUaApplicationRecordDataType._cuteOwning(address)

  def applicationId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaGdsClient::applicationId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#applicationId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGdsClient::applicationId() const
    return self.uglySide.call('ritual_ZNK15QOpcUaGdsClient13applicationIdEv')

  def distinguishedNameCertificateSigningRequestPreset(
      self,
  ) -> QOpcUaX509DistinguishedName:
    """
    Calls Qt's 'const QOpcUaX509DistinguishedName
    &QOpcUaGdsClient::distinguishedNameCertificateSigningRequestPreset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html

    Returns
    -------

    QOpcUaX509DistinguishedName
      A new cute QOpcUaX509DistinguishedName around the copy Qt gave back.
      Python owns it.
    """
    #  const QOpcUaX509DistinguishedName &QOpcUaGdsClient::
    #      distinguishedNameCertificateSigningRequestPreset() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient48distinguishedNameCertificateSigningRe'
        'questPresetEv',
    )
    from . import QOpcUaX509DistinguishedName
    return QOpcUaX509DistinguishedName._cuteOwning(address)

  def dnsCertificateSigningRequestPreset(self) -> str:
    """
    Calls Qt's 'const QString
    &QOpcUaGdsClient::dnsCertificateSigningRequestPreset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QOpcUaGdsClient::dnsCertificateSigningRequestPreset()
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient34dnsCertificateSigningRequestPresetEv',
    )

  def certificateCheckInterval(self) -> int:
    """
    Calls Qt's 'int QOpcUaGdsClient::certificateCheckInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#certificateCheckInterval
    """
    #  int QOpcUaGdsClient::certificateCheckInterval() const
    return self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient24certificateCheckIntervalEv',
    )

  def trustListUpdateInterval(self) -> int:
    """
    Calls Qt's 'int QOpcUaGdsClient::trustListUpdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#trustListUpdateInterval
    """
    #  int QOpcUaGdsClient::trustListUpdateInterval() const
    return self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient23trustListUpdateIntervalEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QOpcUaGdsClient::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QOpcUaGdsClient::error() const
    return QOpcUaGdsClient.Error(self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient5errorEv',
    ))

  def state(self) -> State:
    """
    Calls Qt's 'State QOpcUaGdsClient::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QOpcUaGdsClient::state() const
    return QOpcUaGdsClient.State(self.uglySide.call(
        'ritual_ZNK15QOpcUaGdsClient5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setBackend(self, backend: str) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setBackend(const QString &backend)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#setBackend

    Parameters
    ----------

    backend : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaGdsClient::setBackend(const QString &backend)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient10setBackendERK7QString', backend,
    )

  @overload(QOpcUaEndpointDescription)
  def setEndpoint(self, endpoint: QOpcUaEndpointDescription) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setEndpoint(const
    QOpcUaEndpointDescription &endpoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#setEndpoint

    Parameters
    ----------

    endpoint : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  void QOpcUaGdsClient::setEndpoint(const QOpcUaEndpointDescription
    #      &endpoint)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient11setEndpointERK25QOpcUaEndpointDescript'
        'ion',
        self._valueOf(endpoint),
    )

  @overload(QOpcUaPkiConfiguration)
  def setPkiConfiguration(self, pkiConfig: QOpcUaPkiConfiguration) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setPkiConfiguration(const
    QOpcUaPkiConfiguration &pkiConfig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#setPkiConfiguration

    Parameters
    ----------

    pkiConfig : QOpcUaPkiConfiguration
      Passed on as a value: Qt reads the C++ QOpcUaPkiConfiguration, which
      stays Python's own.
    """
    #  void QOpcUaGdsClient::setPkiConfiguration(const QOpcUaPkiConfiguration
    #      &pkiConfig)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient19setPkiConfigurationERK22QOpcUaPkiConfi'
        'guration',
        self._valueOf(pkiConfig),
    )

  @overload(QOpcUaApplicationIdentity)
  def setApplicationIdentity(
      self,
      appIdentity: QOpcUaApplicationIdentity,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setApplicationIdentity(const
    QOpcUaApplicationIdentity &appIdentity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#setApplicationIdentity

    Parameters
    ----------

    appIdentity : QOpcUaApplicationIdentity
      Passed on as a value: Qt reads the C++ QOpcUaApplicationIdentity, which
      stays Python's own.
    """
    #  void QOpcUaGdsClient::setApplicationIdentity(const
    #      QOpcUaApplicationIdentity &appIdentity)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient22setApplicationIdentityERK25QOpcUaAppli'
        'cationIdentity',
        self._valueOf(appIdentity),
    )

  @overload(QOpcUaApplicationRecordDataType)
  def setApplicationRecord(
      self,
      appRecord: QOpcUaApplicationRecordDataType,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setApplicationRecord(const
    QOpcUaApplicationRecordDataType &appRecord)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#setApplicationRecord

    Parameters
    ----------

    appRecord : QOpcUaApplicationRecordDataType
      Passed on as a value: Qt reads the C++ QOpcUaApplicationRecordDataType,
      which stays Python's own.
    """
    #  void QOpcUaGdsClient::setApplicationRecord(const
    #      QOpcUaApplicationRecordDataType &appRecord)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient20setApplicationRecordERK31QOpcUaApplica'
        'tionRecordDataType',
        self._valueOf(appRecord),
    )

  @overload(QOpcUaX509DistinguishedName, str)
  def setCertificateSigningRequestPresets(
      self,
      dn: QOpcUaX509DistinguishedName,
      dns: str,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaGdsClient::setCertificateSigningRequestPresets(const
    QOpcUaX509DistinguishedName &dn, const QString &dns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html

    Parameters
    ----------

    dn : QOpcUaX509DistinguishedName
      Passed on as a value: Qt reads the C++ QOpcUaX509DistinguishedName,
      which stays Python's own.

    dns : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaGdsClient::setCertificateSigningRequestPresets(const
    #      QOpcUaX509DistinguishedName &dn, const QString &dns)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient35setCertificateSigningRequestPresetsERK'
        '27QOpcUaX509DistinguishedNameRK7QString',
        self._valueOf(dn), dns,
    )

  @overload(int)
  def setCertificateCheckInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setCertificateCheckInterval(int
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#setCertificateCheckInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QOpcUaGdsClient::setCertificateCheckInterval(int interval)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient27setCertificateCheckIntervalEi',
        interval,
    )

  @overload(int)
  def setTrustListUpdateInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::setTrustListUpdateInterval(int
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#setTrustListUpdateInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QOpcUaGdsClient::setTrustListUpdateInterval(int interval)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient26setTrustListUpdateIntervalEi', interval,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaGdsClient::QOpcUaGdsClient(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#QOpcUaGdsClient

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpcUaGdsClient::QOpcUaGdsClient(QObject *parent)
    self._noteCreation(QOpcUaGdsClient, lambda: Rituals.call(
        'ritual_ZN15QOpcUaGdsClientC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#start
    """
    #  void QOpcUaGdsClient::start()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient5startEv')

  def unregisterApplication(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::unregisterApplication()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#unregisterApplication
    """
    #  void QOpcUaGdsClient::unregisterApplication()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient21unregisterApplicationEv')

  @overload(State)
  def stateChanged(self, state: State) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::stateChanged(State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#stateChanged

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QOpcUaGdsClient::stateChanged(State state)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient12stateChangedENS_5StateE', state.value,
    )

  @overload(Error)
  def errorChanged(self, error: Error) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::errorChanged(Error error)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#errorChanged

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QOpcUaGdsClient::errorChanged(Error error)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient12errorChangedENS_5ErrorE', error.value,
    )

  def applicationRegistered(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::applicationRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#applicationRegistered
    """
    #  void QOpcUaGdsClient::applicationRegistered()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient21applicationRegisteredEv')

  @overload(QStringList)
  def certificateGroupsReceived(
      self,
      certificateGroups: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::certificateGroupsReceived(QStringList
    certificateGroups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#certificateGroupsReceived

    Parameters
    ----------

    certificateGroups : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaGdsClient::certificateGroupsReceived(QStringList
    #      certificateGroups)
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient25certificateGroupsReceivedE5QListI7QStr'
        'ingE',
        self._valueOf(certificateGroups),
    )

  def certificateUpdateRequired(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::certificateUpdateRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#certificateUpdateRequired
    """
    #  void QOpcUaGdsClient::certificateUpdateRequired()
    self.uglySide.call(
        'ritual_ZN15QOpcUaGdsClient25certificateUpdateRequiredEv',
    )

  def certificateUpdated(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::certificateUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#certificateUpdated
    """
    #  void QOpcUaGdsClient::certificateUpdated()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient18certificateUpdatedEv')

  def unregistered(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::unregistered()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuagdsclient.html#unregistered
    """
    #  void QOpcUaGdsClient::unregistered()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient12unregisteredEv')

  def trustListUpdated(self) -> None:
    """
    Calls Qt's 'void QOpcUaGdsClient::trustListUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagdsclient.html#trustListUpdated
    """
    #  void QOpcUaGdsClient::trustListUpdated()
    self.uglySide.call('ritual_ZN15QOpcUaGdsClient16trustListUpdatedEv')

  @staticmethod
  def authenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaGdsClient::authenticationRequired(QOpcUaAuthenticationInformation
    &authInfo)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaGdsClient.authenticationRequired' has no cute function yet. "
        "Qt's 'void "
        "QOpcUaGdsClient::authenticationRequired(QOpcUaAuthenticationInforma"
        "tion &authInfo)': takes a type Python has no way to hand over yet.")
