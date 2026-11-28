"""
QOpcUaAuthenticationInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaauthenticationinformation.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpcUaUserTokenPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant


class QOpcUaAuthenticationInformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaAuthenticationInformation: a plain Python
  object standing in front of one C++ QOpcUaAuthenticationInformation.

  C++ hands a QOpcUaAuthenticationInformation around as a copy, so every C++
  QOpcUaAuthenticationInformation behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaAuthenticationInformation that has a ritual
  and that Python can call so far, 6 names in all: '__eq__',
  'setAnonymousAuthentication', 'setUsernameAuthentication',
  'setCertificateAuthentication', 'authenticationData', 'authenticationType'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaAuthenticationInformation
    &QOpcUaAuthenticationInformation::operator=(const
    QOpcUaAuthenticationInformation &a0)': assignment: Python binds a name
    and has no operator for it.
  - Qt's
    'QOpcUaAuthenticationInformation::~QOpcUaAuthenticationInformation()':
    the destructor: Python removes its C++ QOpcUaAuthenticationInformation by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaAuthenticationInformation is created at the first use, not
    by 'QOpcUaAuthenticationInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaAuthenticationInformation back gives a copy the
    ritual made for Python, in a new cute QOpcUaAuthenticationInformation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaAuthenticationInformation'

  #  Qt's '~QOpcUaAuthenticationInformation()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaAuthenticationInformation behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QOpcUaAuthenticationInformationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def authenticationData(self) -> QVariant:
    """
    Calls Qt's 'const QVariant
    &QOpcUaAuthenticationInformation::authenticationData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QOpcUaAuthenticationInformation::authenticationData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QOpcUaAuthenticationInformation18authenticationDataEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def authenticationType(self) -> QOpcUaUserTokenPolicy.TokenType:
    """
    Calls Qt's 'QOpcUaUserTokenPolicy::TokenType
    QOpcUaAuthenticationInformation::authenticationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html

    Returns
    -------

    QOpcUaUserTokenPolicy.TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaUserTokenPolicy.TokenType(number)' gives.
    """
    #  QOpcUaUserTokenPolicy::TokenType
    #      QOpcUaAuthenticationInformation::authenticationType() const
    return QOpcUaUserTokenPolicy.TokenType(self.uglySide.call(
        'ritual_ZNK31QOpcUaAuthenticationInformation18authenticationTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setAnonymousAuthentication(self) -> None:
    """
    Calls Qt's 'void
    QOpcUaAuthenticationInformation::setAnonymousAuthentication()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html
    """
    #  void QOpcUaAuthenticationInformation::setAnonymousAuthentication()
    self.uglySide.call(
        'ritual_ZN31QOpcUaAuthenticationInformation26setAnonymousAuthentica'
        'tionEv',
    )

  @overload(str, str)
  def setUsernameAuthentication(self, username: str, password: str) -> None:
    """
    Calls Qt's 'void
    QOpcUaAuthenticationInformation::setUsernameAuthentication(const QString
    &username, const QString &password)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html

    Parameters
    ----------

    username : str
      Passed on as it is: a QString is made of it for the call.

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAuthenticationInformation::setUsernameAuthentication(const
    #      QString &username, const QString &password)
    self.uglySide.call(
        'ritual_ZN31QOpcUaAuthenticationInformation25setUsernameAuthenticat'
        'ionERK7QStringS2_',
        username, password,
    )

  @overload()
  def setCertificateAuthentication(self) -> None:
    """
    Calls Qt's 'void
    QOpcUaAuthenticationInformation::setCertificateAuthentication()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html
    """
    #  void QOpcUaAuthenticationInformation::setCertificateAuthentication()
    self.uglySide.call(
        'ritual_ZN31QOpcUaAuthenticationInformation28setCertificateAuthenti'
        'cationEv',
    )

  @overload(str, str)
  def setCertificateAuthentication(
      self,
      certificatePath: str,
      privateKeyPath: str,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaAuthenticationInformation::setCertificateAuthentication(const
    QString &certificatePath, const QString &privateKeyPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html

    Parameters
    ----------

    certificatePath : str
      Passed on as it is: a QString is made of it for the call.

    privateKeyPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaAuthenticationInformation::setCertificateAuthentication(
    #      const QString &certificatePath, const QString &privateKeyPath)
    self.uglySide.call(
        'ritual_ZN31QOpcUaAuthenticationInformation28setCertificateAuthenti'
        'cationERK7QStringS2_',
        certificatePath, privateKeyPath,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaAuthenticationInformation) -> bool:
    """
    Calls Qt's 'bool QOpcUaAuthenticationInformation::operator==(const
    QOpcUaAuthenticationInformation &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html#operator==

    Parameters
    ----------

    rhs : QOpcUaAuthenticationInformation
      Passed on as a value: Qt reads the C++ QOpcUaAuthenticationInformation,
      which stays Python's own.
    """
    #  bool QOpcUaAuthenticationInformation::operator==(const
    #      QOpcUaAuthenticationInformation &rhs) const
    return self.uglySide.call(
        'ritual_ZNK31QOpcUaAuthenticationInformationeqERKS_',
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
    'QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html
    """
    #  QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation()
    self._noteCreation(QOpcUaAuthenticationInformation, lambda: Rituals.call(
        'ritual_ZN31QOpcUaAuthenticationInformationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaAuthenticationInformation) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation(const
    QOpcUaAuthenticationInformation &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaauthenticationinformation.html

    Parameters
    ----------

    a0 : QOpcUaAuthenticationInformation
      Passed on as a value: Qt reads the C++ QOpcUaAuthenticationInformation,
      which stays Python's own.
    """
    #  QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation(const
    #      QOpcUaAuthenticationInformation &a0)
    self._noteCreation(QOpcUaAuthenticationInformation, lambda: Rituals.call(
        'ritual_ZN31QOpcUaAuthenticationInformationC1ERKS_',
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
