"""
QQmlSslConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlSslConfiguration to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtNetwork import QSsl, QSslSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from ..QtNetwork import QSslConfiguration
  from . import QQmlSslKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlSslKey = WAIT['QQmlSslKey']
  QSslConfiguration = WAIT['QSslConfiguration']


class QQmlSslConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSslConfiguration: a plain Python object standing
  in front of one C++ QQmlSslConfiguration.

  C++ hands a QQmlSslConfiguration around as a copy, so every C++
  QQmlSslConfiguration behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSslConfiguration that has a ritual and that
  Python can call so far, 19 names in all: 'setCertificateFiles',
  'setPrivateKey', 'ciphers', 'protocol', 'peerVerifyMode',
  'peerVerifyDepth', 'sessionTicket', 'sslOptionFlags', 'configuration',
  'setProtocol', 'setPeerVerifyMode', 'setPeerVerifyDepth', 'setCiphers',
  'setSessionTicket', 'setSslOptionFlags', '__eq__', '__ne__',
  'setSslOptionsList', 'setCiphersList'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QSsl::SslOption> QQmlSslConfiguration::sslOptions() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQmlSslConfiguration::setSslOptions(const
    QList<QSsl::SslOption> &options)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlSslConfiguration::~QQmlSslConfiguration()': the destructor:
    Python removes its C++ QQmlSslConfiguration by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlSslConfiguration is created at the first use, not by
    'QQmlSslConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSslConfiguration back gives a copy the ritual
    made for Python, in a new cute QQmlSslConfiguration.
  - Each name of Qt's QQmlSslConfiguration that has no cute function yet,
    'setSslOptions', 'sslOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSslConfiguration'

  #  Qt's '~QQmlSslConfiguration()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSslConfiguration behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlSslConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def ciphers(self) -> str:
    """
    Calls Qt's 'QString QQmlSslConfiguration::ciphers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslconfiguration.html#ciphers

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSslConfiguration::ciphers() const
    return self.uglySide.call('ritual_ZNK20QQmlSslConfiguration7ciphersEv')

  def protocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QQmlSslConfiguration::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslconfiguration.html#protocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QQmlSslConfiguration::protocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK20QQmlSslConfiguration8protocolEv',
    ))

  def peerVerifyMode(self) -> QSslSocket.PeerVerifyMode:
    """
    Calls Qt's 'QSslSocket::PeerVerifyMode
    QQmlSslConfiguration::peerVerifyMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#peerVerifyMode

    Returns
    -------

    QSslSocket.PeerVerifyMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSslSocket.PeerVerifyMode(number)' gives.
    """
    #  QSslSocket::PeerVerifyMode QQmlSslConfiguration::peerVerifyMode()
    #      const
    return QSslSocket.PeerVerifyMode(self.uglySide.call(
        'ritual_ZNK20QQmlSslConfiguration14peerVerifyModeEv',
    ))

  def peerVerifyDepth(self) -> int:
    """
    Calls Qt's 'int QQmlSslConfiguration::peerVerifyDepth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#peerVerifyDepth
    """
    #  int QQmlSslConfiguration::peerVerifyDepth() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlSslConfiguration15peerVerifyDepthEv',
    )

  def sessionTicket(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlSslConfiguration::sessionTicket() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#sessionTicket

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlSslConfiguration::sessionTicket() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlSslConfiguration13sessionTicketEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def sslOptionFlags(self) -> QSsl.SslOptions:
    """
    Calls Qt's 'QSsl::SslOptions QQmlSslConfiguration::sslOptionFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#sslOptionFlags

    Returns
    -------

    QSsl.SslOptions
      The value standing for the combination Qt gave back.
    """
    #  QSsl::SslOptions QQmlSslConfiguration::sslOptionFlags() const
    return QSsl.SslOptions(self.uglySide.call(
        'ritual_ZNK20QQmlSslConfiguration14sslOptionFlagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setCertificateFiles(self, certificateFiles: QStringList) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setCertificateFiles(const
    QStringList &certificateFiles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setCertificateFiles

    Parameters
    ----------

    certificateFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlSslConfiguration::setCertificateFiles(const QStringList
    #      &certificateFiles)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration19setCertificateFilesERK5QListI7QSt'
        'ringE',
        self._valueOf(certificateFiles),
    )

  @overload(QQmlSslKey)
  def setPrivateKey(self, privateKey: QQmlSslKey) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setPrivateKey(const QQmlSslKey
    &privateKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setPrivateKey

    Parameters
    ----------

    privateKey : QQmlSslKey
      Passed on as a value: Qt reads the C++ QQmlSslKey, which stays Python's
      own.
    """
    #  void QQmlSslConfiguration::setPrivateKey(const QQmlSslKey &privateKey)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration13setPrivateKeyERK10QQmlSslKey',
        self._valueOf(privateKey),
    )

  @overload(QSsl.SslProtocol)
  def setProtocol(self, protocol: QSsl.SslProtocol) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setProtocol(QSsl::SslProtocol
    protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setProtocol

    Parameters
    ----------

    protocol : QSsl.SslProtocol
      Passed on as its number.
    """
    #  void QQmlSslConfiguration::setProtocol(QSsl::SslProtocol protocol)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration11setProtocolEN4QSsl11SslProtocolE',
        protocol.value,
    )

  @overload(QSslSocket.PeerVerifyMode)
  def setPeerVerifyMode(self, mode: QSslSocket.PeerVerifyMode) -> None:
    """
    Calls Qt's 'void
    QQmlSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setPeerVerifyMode

    Parameters
    ----------

    mode : QSslSocket.PeerVerifyMode
      Passed on as its number.
    """
    #  void
    #      QQmlSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration17setPeerVerifyModeEN10QSslSocket14'
        'PeerVerifyModeE',
        mode.value,
    )

  @overload(int)
  def setPeerVerifyDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setPeerVerifyDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setPeerVerifyDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QQmlSslConfiguration::setPeerVerifyDepth(int depth)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration18setPeerVerifyDepthEi', depth,
    )

  @overload(str)
  def setCiphers(self, ciphers: str) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setCiphers(const QString
    &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setCiphers

    Parameters
    ----------

    ciphers : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSslConfiguration::setCiphers(const QString &ciphers)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration10setCiphersERK7QString', ciphers,
    )

  @overload(QByteArray)
  def setSessionTicket(self, sessionTicket: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setSessionTicket(const QByteArray
    &sessionTicket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setSessionTicket

    Parameters
    ----------

    sessionTicket : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlSslConfiguration::setSessionTicket(const QByteArray
    #      &sessionTicket)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration16setSessionTicketERK10QByteArray',
        self._valueOf(sessionTicket),
    )

  @overload(QSsl.SslOptions)
  def setSslOptionFlags(self, options: QSsl.SslOptions) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setSslOptionFlags(QSsl::SslOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setSslOptionFlags

    Parameters
    ----------

    options : QSsl.SslOptions
      Passed on as its number.
    """
    #  void QQmlSslConfiguration::setSslOptionFlags(QSsl::SslOptions options)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration17setSslOptionFlagsE6QFlagsIN4QSsl9'
        'SslOptionEE',
        options.value,
    )

  @overload(QSslConfiguration)
  def setSslOptionsList(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setSslOptionsList(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setSslOptionsList

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QQmlSslConfiguration::setSslOptionsList(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration17setSslOptionsListERK17QSslConfigu'
        'ration',
        self._valueOf(configuration),
    )

  @overload(QSslConfiguration)
  def setCiphersList(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QQmlSslConfiguration::setCiphersList(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#setCiphersList

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QQmlSslConfiguration::setCiphersList(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration14setCiphersListERK17QSslConfigurat'
        'ion',
        self._valueOf(configuration),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rval: QQmlSslConfiguration) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlSslConfiguration &lval, const
    QQmlSslConfiguration &rval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#operator==

    Parameters
    ----------

    rval : QQmlSslConfiguration
      Passed on as a value: Qt reads the C++ QQmlSslConfiguration, which
      stays Python's own.
    """
    #  bool operator==(const QQmlSslConfiguration &lval, const
    #      QQmlSslConfiguration &rval)
    return Rituals.call(
        'ritual_ZeqRK20QQmlSslConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rval),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rval: QQmlSslConfiguration) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlSslConfiguration &lval, const
    QQmlSslConfiguration &rval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#operator!=

    Parameters
    ----------

    rval : QQmlSslConfiguration
      Passed on as a value: Qt reads the C++ QQmlSslConfiguration, which
      stays Python's own.
    """
    #  bool operator!=(const QQmlSslConfiguration &lval, const
    #      QQmlSslConfiguration &rval)
    return Rituals.call(
        'ritual_ZneRK20QQmlSslConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rval),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def configuration(self) -> QSslConfiguration:
    """
    Calls Qt's 'const QSslConfiguration
    QQmlSslConfiguration::configuration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsslconfiguration.html#configuration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  const QSslConfiguration QQmlSslConfiguration::configuration()
    address = self.uglySide.call(
        'ritual_ZN20QQmlSslConfiguration13configurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  @staticmethod
  def setSslOptions(*__, **_) -> Never:
    """
    Qt's 'void QQmlSslConfiguration::setSslOptions(const
    QList<QSsl::SslOption> &options)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlSslConfiguration.setSslOptions' has no cute function yet. "
        "Qt's 'void QQmlSslConfiguration::setSslOptions(const "
        "QList<QSsl::SslOption> &options)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def sslOptions(*__, **_) -> Never:
    """
    Qt's 'QList<QSsl::SslOption> QQmlSslConfiguration::sslOptions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSslConfiguration.sslOptions' has no cute function yet. Qt's "
        "'QList<QSsl::SslOption> QQmlSslConfiguration::sslOptions() const': "
        "gives a type Python has no way to take yet.")
