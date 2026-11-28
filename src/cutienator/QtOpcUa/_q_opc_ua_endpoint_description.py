"""
QOpcUaEndpointDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaendpointdescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QOpcUaApplicationDescription, QOpcUaUserTokenPolicy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpcUaApplicationDescription = WAIT['QOpcUaApplicationDescription']
  QOpcUaUserTokenPolicy = WAIT['QOpcUaUserTokenPolicy']


class QOpcUaEndpointDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaEndpointDescription: a plain Python object
  standing in front of one C++ QOpcUaEndpointDescription.

  C++ hands a QOpcUaEndpointDescription around as a copy, so every C++
  QOpcUaEndpointDescription behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaEndpointDescription that has a ritual and that
  Python can call so far, 17 names in all: '__eq__', 'endpointUrl',
  'setEndpointUrl', 'server', 'setServer', 'serverCertificate',
  'setServerCertificate', 'securityMode', 'setSecurityMode',
  'securityPolicy', 'setSecurityPolicy', 'userIdentityTokens',
  'setUserIdentityTokens', 'transportProfileUri', 'setTransportProfileUri',
  'securityLevel', 'setSecurityLevel'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaEndpointDescription
    &QOpcUaEndpointDescription::operator=(const QOpcUaEndpointDescription
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaEndpointDescription::~QOpcUaEndpointDescription()': the
    destructor: Python removes its C++ QOpcUaEndpointDescription by it, and
    has no other use for it.
  - Qt's 'QOpcUaApplicationDescription
    &QOpcUaEndpointDescription::serverRef()': gives a type Python has no way
    to take yet.
  - Qt's 'QList<QOpcUaUserTokenPolicy>
    &QOpcUaEndpointDescription::userIdentityTokensRef()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaEndpointDescription is created at the first use, not by
    'QOpcUaEndpointDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaEndpointDescription back gives a copy the
    ritual made for Python, in a new cute QOpcUaEndpointDescription.
  - Each name of Qt's QOpcUaEndpointDescription that has no cute function
    yet, 'serverRef', 'userIdentityTokensRef', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaEndpointDescription, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class MessageSecurityMode(CuteNum):
    """
    The enum 'QOpcUaEndpointDescription::MessageSecurityMode' of Qt, with the
    4 names Qt gives in it.
    """

    Invalid = Kee[int](0)
    NULL = Kee[int](1)
    Sign = Kee[int](2)
    SignAndEncrypt = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaEndpointDescription'

  #  Qt's '~QOpcUaEndpointDescription()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaEndpointDescription behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaEndpointDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def endpointUrl(self) -> str:
    """
    Calls Qt's 'QString QOpcUaEndpointDescription::endpointUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#endpointUrl

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaEndpointDescription::endpointUrl() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription11endpointUrlEv',
    )

  def server(self) -> QOpcUaApplicationDescription:
    """
    Calls Qt's 'QOpcUaApplicationDescription
    QOpcUaEndpointDescription::server() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#server

    Returns
    -------

    QOpcUaApplicationDescription
      A new cute QOpcUaApplicationDescription around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaApplicationDescription QOpcUaEndpointDescription::server() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription6serverEv',
    )
    from . import QOpcUaApplicationDescription
    return QOpcUaApplicationDescription._cuteOwning(address)

  def serverCertificate(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpcUaEndpointDescription::serverCertificate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#serverCertificate

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpcUaEndpointDescription::serverCertificate() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription17serverCertificateEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def securityMode(self) -> MessageSecurityMode:
    """
    Calls Qt's 'QOpcUaEndpointDescription::MessageSecurityMode
    QOpcUaEndpointDescription::securityMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#securityMode

    Returns
    -------

    MessageSecurityMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'MessageSecurityMode(number)' gives.
    """
    #  QOpcUaEndpointDescription::MessageSecurityMode
    #      QOpcUaEndpointDescription::securityMode() const
    return QOpcUaEndpointDescription.MessageSecurityMode(self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription12securityModeEv',
    ))

  def securityPolicy(self) -> str:
    """
    Calls Qt's 'QString QOpcUaEndpointDescription::securityPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#securityPolicy

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaEndpointDescription::securityPolicy() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription14securityPolicyEv',
    )

  def userIdentityTokens(self) -> QList[QOpcUaUserTokenPolicy]:
    """
    Calls Qt's 'QList<QOpcUaUserTokenPolicy>
    QOpcUaEndpointDescription::userIdentityTokens() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#userIdentityTokens

    Returns
    -------

    QList[QOpcUaUserTokenPolicy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaUserTokenPolicy>
    #      QOpcUaEndpointDescription::userIdentityTokens() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription18userIdentityTokensEv',
    )
    from . import QOpcUaUserTokenPolicy
    return QList[QOpcUaUserTokenPolicy]._cuteOwning(address)

  def transportProfileUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaEndpointDescription::transportProfileUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#transportProfileUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaEndpointDescription::transportProfileUri() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription19transportProfileUriEv',
    )

  def securityLevel(self) -> int:
    """
    Calls Qt's 'quint8 QOpcUaEndpointDescription::securityLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#securityLevel
    """
    #  quint8 QOpcUaEndpointDescription::securityLevel() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescription13securityLevelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setEndpointUrl(self, endpointUrl: str) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setEndpointUrl(const QString
    &endpointUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#setEndpointUrl

    Parameters
    ----------

    endpointUrl : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaEndpointDescription::setEndpointUrl(const QString
    #      &endpointUrl)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription14setEndpointUrlERK7QString',
        endpointUrl,
    )

  @overload(QOpcUaApplicationDescription)
  def setServer(self, server: QOpcUaApplicationDescription) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setServer(const
    QOpcUaApplicationDescription &server)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#setServer

    Parameters
    ----------

    server : QOpcUaApplicationDescription
      Passed on as a value: Qt reads the C++ QOpcUaApplicationDescription,
      which stays Python's own.
    """
    #  void QOpcUaEndpointDescription::setServer(const
    #      QOpcUaApplicationDescription &server)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription9setServerERK28QOpcUaApplicati'
        'onDescription',
        self._valueOf(server),
    )

  @overload(QByteArray)
  def setServerCertificate(self, serverCertificate: QByteArray) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setServerCertificate(const
    QByteArray &serverCertificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html

    Parameters
    ----------

    serverCertificate : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QOpcUaEndpointDescription::setServerCertificate(const QByteArray
    #      &serverCertificate)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription20setServerCertificateERK10QBy'
        'teArray',
        self._valueOf(serverCertificate),
    )

  @overload(MessageSecurityMode)
  def setSecurityMode(self, securityMode: MessageSecurityMode) -> None:
    """
    Calls Qt's 'void
    QOpcUaEndpointDescription::setSecurityMode(QOpcUaEndpointDescription::
    MessageSecurityMode securityMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#setSecurityMode

    Parameters
    ----------

    securityMode : MessageSecurityMode
      Passed on as its number.
    """
    #  void QOpcUaEndpointDescription::setSecurityMode(
    #      QOpcUaEndpointDescription::MessageSecurityMode securityMode)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription15setSecurityModeENS_19Message'
        'SecurityModeE',
        securityMode.value,
    )

  @overload(str)
  def setSecurityPolicy(self, securityPolicy: str) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setSecurityPolicy(const
    QString &securityPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#setSecurityPolicy

    Parameters
    ----------

    securityPolicy : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaEndpointDescription::setSecurityPolicy(const QString
    #      &securityPolicy)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription17setSecurityPolicyERK7QString',
        securityPolicy,
    )

  @overload(QList[QOpcUaUserTokenPolicy])
  def setUserIdentityTokens(
      self,
      userIdentityTokens: QList[QOpcUaUserTokenPolicy],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setUserIdentityTokens(const
    QList<QOpcUaUserTokenPolicy> &userIdentityTokens)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html

    Parameters
    ----------

    userIdentityTokens : QList[QOpcUaUserTokenPolicy]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaEndpointDescription::setUserIdentityTokens(const
    #      QList<QOpcUaUserTokenPolicy> &userIdentityTokens)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription21setUserIdentityTokensERK5QLi'
        'stI21QOpcUaUserTokenPolicyE',
        self._valueOf(userIdentityTokens),
    )

  @overload(str)
  def setTransportProfileUri(self, transportProfileUri: str) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setTransportProfileUri(const
    QString &transportProfileUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html

    Parameters
    ----------

    transportProfileUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaEndpointDescription::setTransportProfileUri(const QString
    #      &transportProfileUri)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription22setTransportProfileUriERK7QS'
        'tring',
        transportProfileUri,
    )

  @overload(int)
  def setSecurityLevel(self, securityLevel: int) -> None:
    """
    Calls Qt's 'void QOpcUaEndpointDescription::setSecurityLevel(quint8
    securityLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#setSecurityLevel

    Parameters
    ----------

    securityLevel : int
      Passed on as it is.
    """
    #  void QOpcUaEndpointDescription::setSecurityLevel(quint8 securityLevel)
    self.uglySide.call(
        'ritual_ZN25QOpcUaEndpointDescription16setSecurityLevelEh',
        securityLevel,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QOpcUaEndpointDescription) -> bool:
    """
    Calls Qt's 'bool QOpcUaEndpointDescription::operator==(const
    QOpcUaEndpointDescription &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html#operator==

    Parameters
    ----------

    a0 : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  bool QOpcUaEndpointDescription::operator==(const
    #      QOpcUaEndpointDescription &a0) const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaEndpointDescriptioneqERKS_', self._valueOf(a0),
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
    'QOpcUaEndpointDescription::QOpcUaEndpointDescription()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html
    """
    #  QOpcUaEndpointDescription::QOpcUaEndpointDescription()
    self._noteCreation(QOpcUaEndpointDescription, lambda: Rituals.call(
        'ritual_ZN25QOpcUaEndpointDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaEndpointDescription) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaEndpointDescription::QOpcUaEndpointDescription(const
    QOpcUaEndpointDescription &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaendpointdescription.html

    Parameters
    ----------

    a0 : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  QOpcUaEndpointDescription::QOpcUaEndpointDescription(const
    #      QOpcUaEndpointDescription &a0)
    self._noteCreation(QOpcUaEndpointDescription, lambda: Rituals.call(
        'ritual_ZN25QOpcUaEndpointDescriptionC1ERKS_', self._valueOf(a0),
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
  def serverRef(*__, **_) -> Never:
    """
    Qt's 'QOpcUaApplicationDescription
    &QOpcUaEndpointDescription::serverRef()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaEndpointDescription.serverRef' has no cute function yet. "
        "Qt's 'QOpcUaApplicationDescription "
        "&QOpcUaEndpointDescription::serverRef()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def userIdentityTokensRef(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUaUserTokenPolicy>
    &QOpcUaEndpointDescription::userIdentityTokensRef()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaEndpointDescription.userIdentityTokensRef' has no cute "
        "function yet. Qt's 'QList<QOpcUaUserTokenPolicy> "
        "&QOpcUaEndpointDescription::userIdentityTokensRef()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QOpcUaEndpointDescription>': the list of
#  QOpcUaEndpointDescription, which 'QList[QOpcUaEndpointDescription]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QOpcUaEndpointDescription.
QList.createKind(
    QOpcUaEndpointDescription, 'value',
    make='ritual_list_make_QOpcUaEndpointDescription',
    add='ritual_list_add_QOpcUaEndpointDescription',
    size='ritual_list_size_QOpcUaEndpointDescription',
    at='ritual_list_at_QOpcUaEndpointDescription',
    drop='ritual_list_drop_QOpcUaEndpointDescription',
)
