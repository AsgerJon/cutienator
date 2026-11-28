"""
QOpcUaApplicationDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaapplicationdescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']


class QOpcUaApplicationDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaApplicationDescription: a plain Python object
  standing in front of one C++ QOpcUaApplicationDescription.

  C++ hands a QOpcUaApplicationDescription around as a copy, so every C++
  QOpcUaApplicationDescription behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaApplicationDescription that has a ritual and
  that Python can call so far, 15 names in all: '__eq__', 'applicationUri',
  'setApplicationUri', 'productUri', 'setProductUri', 'applicationName',
  'setApplicationName', 'applicationType', 'setApplicationType',
  'gatewayServerUri', 'setGatewayServerUri', 'discoveryProfileUri',
  'setDiscoveryProfileUri', 'discoveryUrls', 'setDiscoveryUrls'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaApplicationDescription
    &QOpcUaApplicationDescription::operator=(const
    QOpcUaApplicationDescription &a0)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QOpcUaApplicationDescription::~QOpcUaApplicationDescription()': the
    destructor: Python removes its C++ QOpcUaApplicationDescription by it,
    and has no other use for it.
  - Qt's 'QList<QString> &QOpcUaApplicationDescription::discoveryUrlsRef()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaApplicationDescription is created at the first use, not by
    'QOpcUaApplicationDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaApplicationDescription back gives a copy the
    ritual made for Python, in a new cute QOpcUaApplicationDescription.
  - Each name of Qt's QOpcUaApplicationDescription that has no cute function
    yet, 'discoveryUrlsRef', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaApplicationDescription, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ApplicationType(CuteNum):
    """
    The enum 'QOpcUaApplicationDescription::ApplicationType' of Qt, with the
    4 names Qt gives in it.
    """

    Server = Kee[int](0)
    Client = Kee[int](1)
    ClientAndServer = Kee[int](2)
    DiscoveryServer = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaApplicationDescription'

  #  Qt's '~QOpcUaApplicationDescription()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaApplicationDescription behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QOpcUaApplicationDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def applicationUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationDescription::applicationUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#applicationUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationDescription::applicationUri() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription14applicationUriEv',
    )

  def productUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationDescription::productUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#productUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationDescription::productUri() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription10productUriEv',
    )

  def applicationName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText
    QOpcUaApplicationDescription::applicationName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#applicationName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaApplicationDescription::applicationName()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription15applicationNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def applicationType(self) -> ApplicationType:
    """
    Calls Qt's 'QOpcUaApplicationDescription::ApplicationType
    QOpcUaApplicationDescription::applicationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#applicationType

    Returns
    -------

    ApplicationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ApplicationType(number)'
      gives.
    """
    #  QOpcUaApplicationDescription::ApplicationType
    #      QOpcUaApplicationDescription::applicationType() const
    return QOpcUaApplicationDescription.ApplicationType(self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription15applicationTypeEv',
    ))

  def gatewayServerUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationDescription::gatewayServerUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#gatewayServerUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationDescription::gatewayServerUri() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription16gatewayServerUriEv',
    )

  def discoveryProfileUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationDescription::discoveryProfileUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationDescription::discoveryProfileUri() const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription19discoveryProfileUriEv',
    )

  def discoveryUrls(self) -> QStringList:
    """
    Calls Qt's 'QList<QString> QOpcUaApplicationDescription::discoveryUrls()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#discoveryUrls

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QOpcUaApplicationDescription::discoveryUrls() const
    address = self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescription13discoveryUrlsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setApplicationUri(self, applicationUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setApplicationUri(const
    QString &applicationUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    applicationUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationDescription::setApplicationUri(const QString
    #      &applicationUri)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription17setApplicationUriERK7QStr'
        'ing',
        applicationUri,
    )

  @overload(str)
  def setProductUri(self, productUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setProductUri(const
    QString &productUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#setProductUri

    Parameters
    ----------

    productUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationDescription::setProductUri(const QString
    #      &productUri)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription13setProductUriERK7QString',
        productUri,
    )

  @overload(QOpcUaLocalizedText)
  def setApplicationName(self, applicationName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setApplicationName(const
    QOpcUaLocalizedText &applicationName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    applicationName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaApplicationDescription::setApplicationName(const
    #      QOpcUaLocalizedText &applicationName)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription18setApplicationNameERK19QO'
        'pcUaLocalizedText',
        self._valueOf(applicationName),
    )

  @overload(ApplicationType)
  def setApplicationType(self, applicationType: ApplicationType) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setApplicationType(
    QOpcUaApplicationDescription::ApplicationType applicationType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    applicationType : ApplicationType
      Passed on as its number.
    """
    #  void QOpcUaApplicationDescription::setApplicationType(
    #      QOpcUaApplicationDescription::ApplicationType applicationType)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription18setApplicationTypeENS_15A'
        'pplicationTypeE',
        applicationType.value,
    )

  @overload(str)
  def setGatewayServerUri(self, gatewayServerUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setGatewayServerUri(const
    QString &gatewayServerUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    gatewayServerUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationDescription::setGatewayServerUri(const QString
    #      &gatewayServerUri)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription19setGatewayServerUriERK7QS'
        'tring',
        gatewayServerUri,
    )

  @overload(str)
  def setDiscoveryProfileUri(self, discoveryProfileUri: str) -> None:
    """
    Calls Qt's 'void
    QOpcUaApplicationDescription::setDiscoveryProfileUri(const QString
    &discoveryProfileUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    discoveryProfileUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationDescription::setDiscoveryProfileUri(const
    #      QString &discoveryProfileUri)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription22setDiscoveryProfileUriERK'
        '7QString',
        discoveryProfileUri,
    )

  @overload(QStringList)
  def setDiscoveryUrls(self, discoveryUrls: QStringList) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationDescription::setDiscoveryUrls(const
    QList<QString> &discoveryUrls)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#setDiscoveryUrls

    Parameters
    ----------

    discoveryUrls : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaApplicationDescription::setDiscoveryUrls(const
    #      QList<QString> &discoveryUrls)
    self.uglySide.call(
        'ritual_ZN28QOpcUaApplicationDescription16setDiscoveryUrlsERK5QList'
        'I7QStringE',
        self._valueOf(discoveryUrls),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QOpcUaApplicationDescription) -> bool:
    """
    Calls Qt's 'bool QOpcUaApplicationDescription::operator==(const
    QOpcUaApplicationDescription &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html#operator==

    Parameters
    ----------

    a0 : QOpcUaApplicationDescription
      Passed on as a value: Qt reads the C++ QOpcUaApplicationDescription,
      which stays Python's own.
    """
    #  bool QOpcUaApplicationDescription::operator==(const
    #      QOpcUaApplicationDescription &a0) const
    return self.uglySide.call(
        'ritual_ZNK28QOpcUaApplicationDescriptioneqERKS_', self._valueOf(a0),
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
    'QOpcUaApplicationDescription::QOpcUaApplicationDescription()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html
    """
    #  QOpcUaApplicationDescription::QOpcUaApplicationDescription()
    self._noteCreation(QOpcUaApplicationDescription, lambda: Rituals.call(
        'ritual_ZN28QOpcUaApplicationDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaApplicationDescription) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaApplicationDescription::QOpcUaApplicationDescription(const
    QOpcUaApplicationDescription &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationdescription.html

    Parameters
    ----------

    a0 : QOpcUaApplicationDescription
      Passed on as a value: Qt reads the C++ QOpcUaApplicationDescription,
      which stays Python's own.
    """
    #  QOpcUaApplicationDescription::QOpcUaApplicationDescription(const
    #      QOpcUaApplicationDescription &a0)
    self._noteCreation(QOpcUaApplicationDescription, lambda: Rituals.call(
        'ritual_ZN28QOpcUaApplicationDescriptionC1ERKS_', self._valueOf(a0),
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
  def discoveryUrlsRef(*__, **_) -> Never:
    """
    Qt's 'QList<QString> &QOpcUaApplicationDescription::discoveryUrlsRef()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaApplicationDescription.discoveryUrlsRef' has no cute "
        "function yet. Qt's 'QList<QString> "
        "&QOpcUaApplicationDescription::discoveryUrlsRef()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QOpcUaApplicationDescription>': the list of
#  QOpcUaApplicationDescription, which 'QList[QOpcUaApplicationDescription]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QOpcUaApplicationDescription.
QList.createKind(
    QOpcUaApplicationDescription, 'value',
    make='ritual_list_make_QOpcUaApplicationDescription',
    add='ritual_list_add_QOpcUaApplicationDescription',
    size='ritual_list_size_QOpcUaApplicationDescription',
    at='ritual_list_at_QOpcUaApplicationDescription',
    drop='ritual_list_drop_QOpcUaApplicationDescription',
)
