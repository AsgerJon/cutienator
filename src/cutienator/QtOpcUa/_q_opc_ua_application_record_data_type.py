"""
QOpcUaApplicationRecordDataType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaapplicationrecorddatatype.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QOpcUaApplicationDescription

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']


class QOpcUaApplicationRecordDataType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaApplicationRecordDataType: a plain Python
  object standing in front of one C++ QOpcUaApplicationRecordDataType.

  C++ hands a QOpcUaApplicationRecordDataType around as a copy, so every C++
  QOpcUaApplicationRecordDataType behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaApplicationRecordDataType that has a ritual
  and that Python can call so far, 15 names in all: '__eq__',
  'setApplicationId', 'applicationId', 'setApplicationType',
  'applicationType', 'setApplicationUri', 'applicationUri',
  'setApplicationNames', 'applicationNames', 'setProductUri', 'productUri',
  'setDiscoveryUrls', 'discoveryUrls', 'setServerCapabilityIdentifiers',
  'serverCapabilityIdentifiers'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaApplicationRecordDataType
    &QOpcUaApplicationRecordDataType::operator=(const
    QOpcUaApplicationRecordDataType &a0)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QVariant QOpcUaApplicationRecordDataType::operator QVariant()
    const': an operator Python has no name for.
  - Qt's
    'QOpcUaApplicationRecordDataType::~QOpcUaApplicationRecordDataType()':
    the destructor: Python removes its C++ QOpcUaApplicationRecordDataType by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaApplicationRecordDataType is created at the first use, not
    by 'QOpcUaApplicationRecordDataType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaApplicationRecordDataType back gives a copy the
    ritual made for Python, in a new cute QOpcUaApplicationRecordDataType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaApplicationRecordDataType'

  #  Qt's '~QOpcUaApplicationRecordDataType()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaApplicationRecordDataType behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QOpcUaApplicationRecordDataTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def applicationId(self) -> str:
    """
    Calls Qt's 'const QString
    &QOpcUaApplicationRecordDataType::applicationId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html#applicationId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QOpcUaApplicationRecordDataType::applicationId() const
    return self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType13applicationIdEv',
    )

  def applicationType(self) -> QOpcUaApplicationDescription.ApplicationType:
    """
    Calls Qt's 'QOpcUaApplicationDescription::ApplicationType
    QOpcUaApplicationRecordDataType::applicationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Returns
    -------

    QOpcUaApplicationDescription.ApplicationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaApplicationDescription.ApplicationType(number)' gives.
    """
    #  QOpcUaApplicationDescription::ApplicationType
    #      QOpcUaApplicationRecordDataType::applicationType() const
    return QOpcUaApplicationDescription.ApplicationType(self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType15applicationTypeEv',
    ))

  def applicationUri(self) -> str:
    """
    Calls Qt's 'const QString
    &QOpcUaApplicationRecordDataType::applicationUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QOpcUaApplicationRecordDataType::applicationUri() const
    return self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType14applicationUriEv',
    )

  def applicationNames(self) -> QList[QOpcUaLocalizedText]:
    """
    Calls Qt's 'const QList<QOpcUaLocalizedText>
    &QOpcUaApplicationRecordDataType::applicationNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Returns
    -------

    QList[QOpcUaLocalizedText]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QOpcUaLocalizedText>
    #      &QOpcUaApplicationRecordDataType::applicationNames() const
    address = self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType16applicationNamesEv',
    )
    from . import QOpcUaLocalizedText
    return QList[QOpcUaLocalizedText]._cuteOwning(address)

  def productUri(self) -> str:
    """
    Calls Qt's 'const QString &QOpcUaApplicationRecordDataType::productUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html#productUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QOpcUaApplicationRecordDataType::productUri() const
    return self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType10productUriEv',
    )

  def discoveryUrls(self) -> QStringList:
    """
    Calls Qt's 'const QList<QString>
    &QOpcUaApplicationRecordDataType::discoveryUrls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html#discoveryUrls

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QString> &QOpcUaApplicationRecordDataType::discoveryUrls()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType13discoveryUrlsEv',
    )
    return QStringList._cuteOwning(address)

  def serverCapabilityIdentifiers(self) -> QStringList:
    """
    Calls Qt's 'const QList<QString>
    &QOpcUaApplicationRecordDataType::serverCapabilityIdentifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QString>
    #      &QOpcUaApplicationRecordDataType::serverCapabilityIdentifiers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataType27serverCapabilityIdent'
        'ifiersEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setApplicationId(self, nodeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationRecordDataType::setApplicationId(const
    QString &nodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationRecordDataType::setApplicationId(const QString
    #      &nodeId)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType16setApplicationIdERK7QS'
        'tring',
        nodeId,
    )

  @overload(QOpcUaApplicationDescription.ApplicationType)
  def setApplicationType(
      self,
      applicationType: QOpcUaApplicationDescription.ApplicationType,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationRecordDataType::setApplicationType(
    QOpcUaApplicationDescription::ApplicationType applicationType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    applicationType : QOpcUaApplicationDescription.ApplicationType
      Passed on as its number.
    """
    #  void QOpcUaApplicationRecordDataType::setApplicationType(
    #      QOpcUaApplicationDescription::ApplicationType applicationType)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType18setApplicationTypeEN28'
        'QOpcUaApplicationDescription15ApplicationTypeE',
        applicationType.value,
    )

  @overload(str)
  def setApplicationUri(self, applicationUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationRecordDataType::setApplicationUri(const
    QString &applicationUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    applicationUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationRecordDataType::setApplicationUri(const QString
    #      &applicationUri)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType17setApplicationUriERK7Q'
        'String',
        applicationUri,
    )

  @overload(QList[QOpcUaLocalizedText])
  def setApplicationNames(
      self,
      applicationNames: QList[QOpcUaLocalizedText],
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaApplicationRecordDataType::setApplicationNames(const
    QList<QOpcUaLocalizedText> &applicationNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    applicationNames : QList[QOpcUaLocalizedText]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaApplicationRecordDataType::setApplicationNames(const
    #      QList<QOpcUaLocalizedText> &applicationNames)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType19setApplicationNamesERK'
        '5QListI19QOpcUaLocalizedTextE',
        self._valueOf(applicationNames),
    )

  @overload(str)
  def setProductUri(self, productUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationRecordDataType::setProductUri(const
    QString &productUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html#setProductUri

    Parameters
    ----------

    productUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationRecordDataType::setProductUri(const QString
    #      &productUri)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType13setProductUriERK7QStri'
        'ng',
        productUri,
    )

  @overload(QStringList)
  def setDiscoveryUrls(self, discoveryUrls: QStringList) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationRecordDataType::setDiscoveryUrls(const
    QList<QString> &discoveryUrls)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    discoveryUrls : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaApplicationRecordDataType::setDiscoveryUrls(const
    #      QList<QString> &discoveryUrls)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType16setDiscoveryUrlsERK5QL'
        'istI7QStringE',
        self._valueOf(discoveryUrls),
    )

  @overload(QStringList)
  def setServerCapabilityIdentifiers(
      self,
      serverCapabilityIdentifiers: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaApplicationRecordDataType::setServerCapabilityIdentifiers(const
    QList<QString> &serverCapabilityIdentifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    serverCapabilityIdentifiers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaApplicationRecordDataType::setServerCapabilityIdentifiers(
    #      const QList<QString> &serverCapabilityIdentifiers)
    self.uglySide.call(
        'ritual_ZN31QOpcUaApplicationRecordDataType30setServerCapabilityIde'
        'ntifiersERK5QListI7QStringE',
        self._valueOf(serverCapabilityIdentifiers),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaApplicationRecordDataType) -> bool:
    """
    Calls Qt's 'bool QOpcUaApplicationRecordDataType::operator==(const
    QOpcUaApplicationRecordDataType &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html#operator==

    Parameters
    ----------

    rhs : QOpcUaApplicationRecordDataType
      Passed on as a value: Qt reads the C++ QOpcUaApplicationRecordDataType,
      which stays Python's own.
    """
    #  bool QOpcUaApplicationRecordDataType::operator==(const
    #      QOpcUaApplicationRecordDataType &rhs) const
    return self.uglySide.call(
        'ritual_ZNK31QOpcUaApplicationRecordDataTypeeqERKS_',
        self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html
    """
    #  QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType()
    self._noteCreation(QOpcUaApplicationRecordDataType, lambda: Rituals.call(
        'ritual_ZN31QOpcUaApplicationRecordDataTypeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaApplicationRecordDataType) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType(const
    QOpcUaApplicationRecordDataType &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationrecorddatatype.html

    Parameters
    ----------

    a0 : QOpcUaApplicationRecordDataType
      Passed on as a value: Qt reads the C++ QOpcUaApplicationRecordDataType,
      which stays Python's own.
    """
    #  QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType(const
    #      QOpcUaApplicationRecordDataType &a0)
    self._noteCreation(QOpcUaApplicationRecordDataType, lambda: Rituals.call(
        'ritual_ZN31QOpcUaApplicationRecordDataTypeC1ERKS_',
        self._valueOf(a0),
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
