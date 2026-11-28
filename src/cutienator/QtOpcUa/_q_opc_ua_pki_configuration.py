"""
QOpcUaPkiConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuapkiconfiguration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaApplicationIdentity


class QOpcUaPkiConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaPkiConfiguration: a plain Python object
  standing in front of one C++ QOpcUaPkiConfiguration.

  C++ hands a QOpcUaPkiConfiguration around as a copy, so every C++
  QOpcUaPkiConfiguration behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaPkiConfiguration that has a ritual and that
  Python can call so far, 15 names in all: 'clientCertificateFile',
  'setClientCertificateFile', 'privateKeyFile', 'setPrivateKeyFile',
  'trustListDirectory', 'setTrustListDirectory', 'revocationListDirectory',
  'setRevocationListDirectory', 'issuerListDirectory',
  'setIssuerListDirectory', 'issuerRevocationListDirectory',
  'setIssuerRevocationListDirectory', 'applicationIdentity', 'isPkiValid',
  'isKeyAndCertificateFileSet'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaPkiConfiguration::~QOpcUaPkiConfiguration()': the destructor:
    Python removes its C++ QOpcUaPkiConfiguration by it, and has no other use
    for it.
  - Qt's 'QOpcUaPkiConfiguration &QOpcUaPkiConfiguration::operator=(const
    QOpcUaPkiConfiguration &rhs)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QOpcUaPkiConfiguration is created at the first use, not by
    'QOpcUaPkiConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaPkiConfiguration back gives a copy the ritual
    made for Python, in a new cute QOpcUaPkiConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaPkiConfiguration'

  #  Qt's '~QOpcUaPkiConfiguration()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaPkiConfiguration behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QOpcUaPkiConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clientCertificateFile(self) -> str:
    """
    Calls Qt's 'QString QOpcUaPkiConfiguration::clientCertificateFile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#clientCertificateFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::clientCertificateFile() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration21clientCertificateFileEv',
    )

  def privateKeyFile(self) -> str:
    """
    Calls Qt's 'QString QOpcUaPkiConfiguration::privateKeyFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#privateKeyFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::privateKeyFile() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration14privateKeyFileEv',
    )

  def trustListDirectory(self) -> str:
    """
    Calls Qt's 'QString QOpcUaPkiConfiguration::trustListDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#trustListDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::trustListDirectory() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration18trustListDirectoryEv',
    )

  def revocationListDirectory(self) -> str:
    """
    Calls Qt's 'QString QOpcUaPkiConfiguration::revocationListDirectory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::revocationListDirectory() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration23revocationListDirectoryEv',
    )

  def issuerListDirectory(self) -> str:
    """
    Calls Qt's 'QString QOpcUaPkiConfiguration::issuerListDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#issuerListDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::issuerListDirectory() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration19issuerListDirectoryEv',
    )

  def issuerRevocationListDirectory(self) -> str:
    """
    Calls Qt's 'QString
    QOpcUaPkiConfiguration::issuerRevocationListDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaPkiConfiguration::issuerRevocationListDirectory() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration29issuerRevocationListDirectoryE'
        'v',
    )

  def applicationIdentity(self) -> QOpcUaApplicationIdentity:
    """
    Calls Qt's 'QOpcUaApplicationIdentity
    QOpcUaPkiConfiguration::applicationIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#applicationIdentity

    Returns
    -------

    QOpcUaApplicationIdentity
      A new cute QOpcUaApplicationIdentity around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaApplicationIdentity
    #      QOpcUaPkiConfiguration::applicationIdentity() const
    address = self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration19applicationIdentityEv',
    )
    from . import QOpcUaApplicationIdentity
    return QOpcUaApplicationIdentity._cuteOwning(address)

  def isPkiValid(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaPkiConfiguration::isPkiValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#isPkiValid
    """
    #  bool QOpcUaPkiConfiguration::isPkiValid() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration10isPkiValidEv',
    )

  def isKeyAndCertificateFileSet(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaPkiConfiguration::isKeyAndCertificateFileSet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html
    """
    #  bool QOpcUaPkiConfiguration::isKeyAndCertificateFileSet() const
    return self.uglySide.call(
        'ritual_ZNK22QOpcUaPkiConfiguration26isKeyAndCertificateFileSetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setClientCertificateFile(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaPkiConfiguration::setClientCertificateFile(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setClientCertificateFile(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration24setClientCertificateFileERK7QSt'
        'ring',
        value,
    )

  @overload(str)
  def setPrivateKeyFile(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaPkiConfiguration::setPrivateKeyFile(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#setPrivateKeyFile

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setPrivateKeyFile(const QString &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration17setPrivateKeyFileERK7QString',
        value,
    )

  @overload(str)
  def setTrustListDirectory(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaPkiConfiguration::setTrustListDirectory(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#setTrustListDirectory

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setTrustListDirectory(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration21setTrustListDirectoryERK7QStrin'
        'g',
        value,
    )

  @overload(str)
  def setRevocationListDirectory(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaPkiConfiguration::setRevocationListDirectory(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setRevocationListDirectory(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration26setRevocationListDirectoryERK7Q'
        'String',
        value,
    )

  @overload(str)
  def setIssuerListDirectory(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaPkiConfiguration::setIssuerListDirectory(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#setIssuerListDirectory

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setIssuerListDirectory(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration22setIssuerListDirectoryERK7QStri'
        'ng',
        value,
    )

  @overload(str)
  def setIssuerRevocationListDirectory(self, value: str) -> None:
    """
    Calls Qt's 'void
    QOpcUaPkiConfiguration::setIssuerRevocationListDirectory(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaPkiConfiguration::setIssuerRevocationListDirectory(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN22QOpcUaPkiConfiguration32setIssuerRevocationListDirector'
        'yERK7QString',
        value,
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
    'QOpcUaPkiConfiguration::QOpcUaPkiConfiguration()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#QOpcUaPkiConfiguration
    """
    #  QOpcUaPkiConfiguration::QOpcUaPkiConfiguration()
    self._noteCreation(QOpcUaPkiConfiguration, lambda: Rituals.call(
        'ritual_ZN22QOpcUaPkiConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaPkiConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaPkiConfiguration::QOpcUaPkiConfiguration(const
    QOpcUaPkiConfiguration &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuapkiconfiguration.html#QOpcUaPkiConfiguration

    Parameters
    ----------

    other : QOpcUaPkiConfiguration
      Passed on as a value: Qt reads the C++ QOpcUaPkiConfiguration, which
      stays Python's own.
    """
    #  QOpcUaPkiConfiguration::QOpcUaPkiConfiguration(const
    #      QOpcUaPkiConfiguration &other)
    self._noteCreation(QOpcUaPkiConfiguration, lambda: Rituals.call(
        'ritual_ZN22QOpcUaPkiConfigurationC1ERKS_', self._valueOf(other),
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
