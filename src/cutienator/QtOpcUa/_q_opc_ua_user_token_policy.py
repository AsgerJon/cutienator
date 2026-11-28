"""
QOpcUaUserTokenPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuausertokenpolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QOpcUaUserTokenPolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaUserTokenPolicy: a plain Python object standing
  in front of one C++ QOpcUaUserTokenPolicy.

  C++ hands a QOpcUaUserTokenPolicy around as a copy, so every C++
  QOpcUaUserTokenPolicy behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaUserTokenPolicy that has a ritual and that
  Python can call so far, 11 names in all: '__eq__', 'policyId',
  'setPolicyId', 'tokenType', 'setTokenType', 'issuedTokenType',
  'setIssuedTokenType', 'issuerEndpointUrl', 'setIssuerEndpointUrl',
  'securityPolicy', 'setSecurityPolicy'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaUserTokenPolicy &QOpcUaUserTokenPolicy::operator=(const
    QOpcUaUserTokenPolicy &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaUserTokenPolicy::~QOpcUaUserTokenPolicy()': the destructor:
    Python removes its C++ QOpcUaUserTokenPolicy by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaUserTokenPolicy is created at the first use, not by
    'QOpcUaUserTokenPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaUserTokenPolicy back gives a copy the ritual
    made for Python, in a new cute QOpcUaUserTokenPolicy.
  """

  #  The enums Qt writes inside QOpcUaUserTokenPolicy, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class TokenType(CuteNum):
    """
    The enum 'QOpcUaUserTokenPolicy::TokenType' of Qt, with the 4 names Qt
    gives in it.
    """

    Anonymous = Kee[int](0)
    Username = Kee[int](1)
    Certificate = Kee[int](2)
    IssuedToken = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaUserTokenPolicy'

  #  Qt's '~QOpcUaUserTokenPolicy()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaUserTokenPolicy behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpcUaUserTokenPolicyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def policyId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaUserTokenPolicy::policyId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#policyId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaUserTokenPolicy::policyId() const
    return self.uglySide.call('ritual_ZNK21QOpcUaUserTokenPolicy8policyIdEv')

  def tokenType(self) -> TokenType:
    """
    Calls Qt's 'QOpcUaUserTokenPolicy::TokenType
    QOpcUaUserTokenPolicy::tokenType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#tokenType

    Returns
    -------

    TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TokenType(number)' gives.
    """
    #  QOpcUaUserTokenPolicy::TokenType QOpcUaUserTokenPolicy::tokenType()
    #      const
    return QOpcUaUserTokenPolicy.TokenType(self.uglySide.call(
        'ritual_ZNK21QOpcUaUserTokenPolicy9tokenTypeEv',
    ))

  def issuedTokenType(self) -> str:
    """
    Calls Qt's 'QString QOpcUaUserTokenPolicy::issuedTokenType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#issuedTokenType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaUserTokenPolicy::issuedTokenType() const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaUserTokenPolicy15issuedTokenTypeEv',
    )

  def issuerEndpointUrl(self) -> str:
    """
    Calls Qt's 'QString QOpcUaUserTokenPolicy::issuerEndpointUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#issuerEndpointUrl

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaUserTokenPolicy::issuerEndpointUrl() const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaUserTokenPolicy17issuerEndpointUrlEv',
    )

  def securityPolicy(self) -> str:
    """
    Calls Qt's 'QString QOpcUaUserTokenPolicy::securityPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#securityPolicy

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaUserTokenPolicy::securityPolicy() const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaUserTokenPolicy14securityPolicyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPolicyId(self, policyId: str) -> None:
    """
    Calls Qt's 'void QOpcUaUserTokenPolicy::setPolicyId(const QString
    &policyId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#setPolicyId

    Parameters
    ----------

    policyId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaUserTokenPolicy::setPolicyId(const QString &policyId)
    self.uglySide.call(
        'ritual_ZN21QOpcUaUserTokenPolicy11setPolicyIdERK7QString', policyId,
    )

  @overload(TokenType)
  def setTokenType(self, tokenType: TokenType) -> None:
    """
    Calls Qt's 'void
    QOpcUaUserTokenPolicy::setTokenType(QOpcUaUserTokenPolicy::TokenType
    tokenType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#setTokenType

    Parameters
    ----------

    tokenType : TokenType
      Passed on as its number.
    """
    #  void QOpcUaUserTokenPolicy::setTokenType(QOpcUaUserTokenPolicy::
    #      TokenType tokenType)
    self.uglySide.call(
        'ritual_ZN21QOpcUaUserTokenPolicy12setTokenTypeENS_9TokenTypeE',
        tokenType.value,
    )

  @overload(str)
  def setIssuedTokenType(self, issuedTokenType: str) -> None:
    """
    Calls Qt's 'void QOpcUaUserTokenPolicy::setIssuedTokenType(const QString
    &issuedTokenType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#setIssuedTokenType

    Parameters
    ----------

    issuedTokenType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaUserTokenPolicy::setIssuedTokenType(const QString
    #      &issuedTokenType)
    self.uglySide.call(
        'ritual_ZN21QOpcUaUserTokenPolicy18setIssuedTokenTypeERK7QString',
        issuedTokenType,
    )

  @overload(str)
  def setIssuerEndpointUrl(self, issuerEndpointUrl: str) -> None:
    """
    Calls Qt's 'void QOpcUaUserTokenPolicy::setIssuerEndpointUrl(const
    QString &issuerEndpointUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#setIssuerEndpointUrl

    Parameters
    ----------

    issuerEndpointUrl : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaUserTokenPolicy::setIssuerEndpointUrl(const QString
    #      &issuerEndpointUrl)
    self.uglySide.call(
        'ritual_ZN21QOpcUaUserTokenPolicy20setIssuerEndpointUrlERK7QString',
        issuerEndpointUrl,
    )

  @overload(str)
  def setSecurityPolicy(self, securityPolicy: str) -> None:
    """
    Calls Qt's 'void QOpcUaUserTokenPolicy::setSecurityPolicy(const QString
    &securityPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#setSecurityPolicy

    Parameters
    ----------

    securityPolicy : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaUserTokenPolicy::setSecurityPolicy(const QString
    #      &securityPolicy)
    self.uglySide.call(
        'ritual_ZN21QOpcUaUserTokenPolicy17setSecurityPolicyERK7QString',
        securityPolicy,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QOpcUaUserTokenPolicy) -> bool:
    """
    Calls Qt's 'bool QOpcUaUserTokenPolicy::operator==(const
    QOpcUaUserTokenPolicy &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#operator==

    Parameters
    ----------

    a0 : QOpcUaUserTokenPolicy
      Passed on as a value: Qt reads the C++ QOpcUaUserTokenPolicy, which
      stays Python's own.
    """
    #  bool QOpcUaUserTokenPolicy::operator==(const QOpcUaUserTokenPolicy
    #      &a0) const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaUserTokenPolicyeqERKS_', self._valueOf(a0),
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
    'QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#QOpcUaUserTokenPolicy
    """
    #  QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy()
    self._noteCreation(QOpcUaUserTokenPolicy, lambda: Rituals.call(
        'ritual_ZN21QOpcUaUserTokenPolicyC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaUserTokenPolicy) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy(const QOpcUaUserTokenPolicy
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuausertokenpolicy.html#QOpcUaUserTokenPolicy

    Parameters
    ----------

    a0 : QOpcUaUserTokenPolicy
      Passed on as a value: Qt reads the C++ QOpcUaUserTokenPolicy, which
      stays Python's own.
    """
    #  QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy(const
    #      QOpcUaUserTokenPolicy &a0)
    self._noteCreation(QOpcUaUserTokenPolicy, lambda: Rituals.call(
        'ritual_ZN21QOpcUaUserTokenPolicyC1ERKS_', self._valueOf(a0),
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


#  Qt's 'QList<QOpcUaUserTokenPolicy>': the list of QOpcUaUserTokenPolicy,
#  which 'QList[QOpcUaUserTokenPolicy]' gives. It is made here, so that there
#  is one as soon as there can be a QOpcUaUserTokenPolicy.
QList.createKind(
    QOpcUaUserTokenPolicy, 'value',
    make='ritual_list_make_QOpcUaUserTokenPolicy',
    add='ritual_list_add_QOpcUaUserTokenPolicy',
    size='ritual_list_size_QOpcUaUserTokenPolicy',
    at='ritual_list_at_QOpcUaUserTokenPolicy',
    drop='ritual_list_drop_QOpcUaUserTokenPolicy',
)
