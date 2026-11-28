"""
QCoapSecurityConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapsecurityconfiguration.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from ..QtNetwork import QSslCertificate
  from . import QCoapPrivateKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapPrivateKey = WAIT['QCoapPrivateKey']
  QSslCertificate = WAIT['QSslCertificate']


class QCoapSecurityConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCoapSecurityConfiguration: a plain Python object
  standing in front of one C++ QCoapSecurityConfiguration.

  C++ hands a QCoapSecurityConfiguration around as a copy, so every C++
  QCoapSecurityConfiguration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QCoapSecurityConfiguration that has a ritual and
  that Python can call so far, 12 names in all: 'setPreSharedKeyIdentity',
  'preSharedKeyIdentity', 'setPreSharedKey', 'preSharedKey',
  'setDefaultCipherString', 'defaultCipherString', 'setCaCertificates',
  'caCertificates', 'setLocalCertificateChain', 'localCertificateChain',
  'setPrivateKey', 'privateKey'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapSecurityConfiguration::~QCoapSecurityConfiguration()': the
    destructor: Python removes its C++ QCoapSecurityConfiguration by it, and
    has no other use for it.
  - Qt's 'QCoapSecurityConfiguration::QCoapSecurityConfiguration(
    QCoapSecurityConfiguration &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QCoapSecurityConfiguration
    &QCoapSecurityConfiguration::operator=(QCoapSecurityConfiguration
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCoapSecurityConfiguration
    &QCoapSecurityConfiguration::operator=(const QCoapSecurityConfiguration
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCoapSecurityConfiguration::swap(QCoapSecurityConfiguration
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCoapSecurityConfiguration is created at the first use, not by
    'QCoapSecurityConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapSecurityConfiguration back gives a copy the
    ritual made for Python, in a new cute QCoapSecurityConfiguration.
  - Each name of Qt's QCoapSecurityConfiguration that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QCoapSecurityConfiguration'

  #  Qt's '~QCoapSecurityConfiguration()'. Naming it makes this a value
  #  class: Python owns every C++ QCoapSecurityConfiguration behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QCoapSecurityConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def preSharedKeyIdentity(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapSecurityConfiguration::preSharedKeyIdentity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapSecurityConfiguration::preSharedKeyIdentity() const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration20preSharedKeyIdentityEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def preSharedKey(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapSecurityConfiguration::preSharedKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#preSharedKey

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapSecurityConfiguration::preSharedKey() const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration12preSharedKeyEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def defaultCipherString(self) -> str:
    """
    Calls Qt's 'QString QCoapSecurityConfiguration::defaultCipherString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapSecurityConfiguration::defaultCipherString() const
    return self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration19defaultCipherStringEv',
    )

  def caCertificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QCoapSecurityConfiguration::caCertificates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#caCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QCoapSecurityConfiguration::caCertificates()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration14caCertificatesEv',
    )
    from ..QtNetwork import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  def localCertificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QCoapSecurityConfiguration::localCertificateChain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate>
    #      QCoapSecurityConfiguration::localCertificateChain() const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration21localCertificateChainEv',
    )
    from ..QtNetwork import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  def privateKey(self) -> QCoapPrivateKey:
    """
    Calls Qt's 'QCoapPrivateKey QCoapSecurityConfiguration::privateKey()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#privateKey

    Returns
    -------

    QCoapPrivateKey
      A new cute QCoapPrivateKey around the copy Qt gave back. Python owns
      it.
    """
    #  QCoapPrivateKey QCoapSecurityConfiguration::privateKey() const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapSecurityConfiguration10privateKeyEv',
    )
    from . import QCoapPrivateKey
    return QCoapPrivateKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setPreSharedKeyIdentity(
      self,
      preSharedKeyIdentity: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QCoapSecurityConfiguration::setPreSharedKeyIdentity(const QByteArray
    &preSharedKeyIdentity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Parameters
    ----------

    preSharedKeyIdentity : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapSecurityConfiguration::setPreSharedKeyIdentity(const
    #      QByteArray &preSharedKeyIdentity)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration23setPreSharedKeyIdentityERK1'
        '0QByteArray',
        self._valueOf(preSharedKeyIdentity),
    )

  @overload(QByteArray)
  def setPreSharedKey(self, preSharedKey: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapSecurityConfiguration::setPreSharedKey(const
    QByteArray &preSharedKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#setPreSharedKey

    Parameters
    ----------

    preSharedKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapSecurityConfiguration::setPreSharedKey(const QByteArray
    #      &preSharedKey)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration15setPreSharedKeyERK10QByteAr'
        'ray',
        self._valueOf(preSharedKey),
    )

  @overload(str)
  def setDefaultCipherString(self, cipherString: str) -> None:
    """
    Calls Qt's 'void QCoapSecurityConfiguration::setDefaultCipherString(const
    QString &cipherString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Parameters
    ----------

    cipherString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoapSecurityConfiguration::setDefaultCipherString(const QString
    #      &cipherString)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration22setDefaultCipherStringERK7Q'
        'String',
        cipherString,
    )

  @overload(QList[QSslCertificate])
  def setCaCertificates(self, certificates: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QCoapSecurityConfiguration::setCaCertificates(const
    QList<QSslCertificate> &certificates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#setCaCertificates

    Parameters
    ----------

    certificates : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCoapSecurityConfiguration::setCaCertificates(const
    #      QList<QSslCertificate> &certificates)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration17setCaCertificatesERK5QListI'
        '15QSslCertificateE',
        self._valueOf(certificates),
    )

  @overload(QList[QSslCertificate])
  def setLocalCertificateChain(
      self,
      localChain: QList[QSslCertificate],
  ) -> None:
    """
    Calls Qt's 'void
    QCoapSecurityConfiguration::setLocalCertificateChain(const
    QList<QSslCertificate> &localChain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Parameters
    ----------

    localChain : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCoapSecurityConfiguration::setLocalCertificateChain(const
    #      QList<QSslCertificate> &localChain)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration24setLocalCertificateChainERK'
        '5QListI15QSslCertificateE',
        self._valueOf(localChain),
    )

  @overload(QCoapPrivateKey)
  def setPrivateKey(self, key: QCoapPrivateKey) -> None:
    """
    Calls Qt's 'void QCoapSecurityConfiguration::setPrivateKey(const
    QCoapPrivateKey &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html#setPrivateKey

    Parameters
    ----------

    key : QCoapPrivateKey
      Passed on as a value: Qt reads the C++ QCoapPrivateKey, which stays
      Python's own.
    """
    #  void QCoapSecurityConfiguration::setPrivateKey(const QCoapPrivateKey
    #      &key)
    self.uglySide.call(
        'ritual_ZN26QCoapSecurityConfiguration13setPrivateKeyERK15QCoapPriv'
        'ateKey',
        self._valueOf(key),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCoapSecurityConfiguration::QCoapSecurityConfiguration()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html
    """
    #  QCoapSecurityConfiguration::QCoapSecurityConfiguration()
    self._noteCreation(QCoapSecurityConfiguration, lambda: Rituals.call(
        'ritual_ZN26QCoapSecurityConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCoapSecurityConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'QCoapSecurityConfiguration::QCoapSecurityConfiguration(const
    QCoapSecurityConfiguration &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapsecurityconfiguration.html

    Parameters
    ----------

    other : QCoapSecurityConfiguration
      Passed on as a value: Qt reads the C++ QCoapSecurityConfiguration,
      which stays Python's own.
    """
    #  QCoapSecurityConfiguration::QCoapSecurityConfiguration(const
    #      QCoapSecurityConfiguration &other)
    self._noteCreation(QCoapSecurityConfiguration, lambda: Rituals.call(
        'ritual_ZN26QCoapSecurityConfigurationC1ERKS_', self._valueOf(other),
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
    Qt's 'void QCoapSecurityConfiguration::swap(QCoapSecurityConfiguration
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapSecurityConfiguration.swap' has no cute function yet. Qt's "
        "'void QCoapSecurityConfiguration::swap(QCoapSecurityConfiguration "
        "&other)': takes a type Python has no way to hand over yet.")
