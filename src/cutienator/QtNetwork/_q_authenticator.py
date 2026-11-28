"""
QAuthenticator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qauthenticator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QAuthenticator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAuthenticator: a plain Python object standing in
  front of one C++ QAuthenticator.

  C++ hands a QAuthenticator around as a copy, so every C++ QAuthenticator
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAuthenticator that has a ritual and that Python can
  call so far, 14 names in all: '__eq__', '__ne__', 'user', 'setUser',
  'password', 'setPassword', 'realm', 'setRealm', 'option', 'options',
  'setOption', 'isNull', 'detach', 'clear'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAuthenticator::~QAuthenticator()': the destructor: Python removes
    its C++ QAuthenticator by it, and has no other use for it.
  - Qt's 'QAuthenticator &QAuthenticator::operator=(const QAuthenticator
    &other)': assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  3 of the 21 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QAuthenticator is created at the first use, not by
    'QAuthenticator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAuthenticator back gives a copy the ritual made for
    Python, in a new cute QAuthenticator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAuthenticator'

  #  Qt's '~QAuthenticator()'. Naming it makes this a value class: Python
  #  owns every C++ QAuthenticator behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QAuthenticatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def user(self) -> str:
    """
    Calls Qt's 'QString QAuthenticator::user() const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#user

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAuthenticator::user() const
    return self.uglySide.call('ritual_ZNK14QAuthenticator4userEv')

  def password(self) -> str:
    """
    Calls Qt's 'QString QAuthenticator::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAuthenticator::password() const
    return self.uglySide.call('ritual_ZNK14QAuthenticator8passwordEv')

  def realm(self) -> str:
    """
    Calls Qt's 'QString QAuthenticator::realm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#realm

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAuthenticator::realm() const
    return self.uglySide.call('ritual_ZNK14QAuthenticator5realmEv')

  @overload(str)
  def option(self, opt: str) -> QVariant:
    """
    Calls Qt's 'QVariant QAuthenticator::option(const QString &opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#option

    Parameters
    ----------

    opt : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAuthenticator::option(const QString &opt) const
    address = self.uglySide.call(
        'ritual_ZNK14QAuthenticator6optionERK7QString', opt,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def options(self) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QVariantHash QAuthenticator::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#options

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantHash QAuthenticator::options() const
    address = self.uglySide.call('ritual_ZNK14QAuthenticator7optionsEv')
    from ..QtCore import QVariant
    return QHash[str, QVariant]._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAuthenticator::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#isNull
    """
    #  bool QAuthenticator::isNull() const
    return self.uglySide.call('ritual_ZNK14QAuthenticator6isNullEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUser(self, user: str) -> None:
    """
    Calls Qt's 'void QAuthenticator::setUser(const QString &user)'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#setUser

    Parameters
    ----------

    user : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAuthenticator::setUser(const QString &user)
    self.uglySide.call('ritual_ZN14QAuthenticator7setUserERK7QString', user)

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QAuthenticator::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAuthenticator::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN14QAuthenticator11setPasswordERK7QString', password,
    )

  @overload(str)
  def setRealm(self, realm: str) -> None:
    """
    Calls Qt's 'void QAuthenticator::setRealm(const QString &realm)'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#setRealm

    Parameters
    ----------

    realm : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAuthenticator::setRealm(const QString &realm)
    self.uglySide.call(
        'ritual_ZN14QAuthenticator8setRealmERK7QString', realm,
    )

  @overload(str, QVariant)
  def setOption(self, opt: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QAuthenticator::setOption(const QString &opt, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#setOption

    Parameters
    ----------

    opt : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAuthenticator::setOption(const QString &opt, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN14QAuthenticator9setOptionERK7QStringRK8QVariant',
        opt, self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QAuthenticator) -> bool:
    """
    Calls Qt's 'bool QAuthenticator::operator==(const QAuthenticator &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#operator==

    Parameters
    ----------

    other : QAuthenticator
      Passed on as a value: Qt reads the C++ QAuthenticator, which stays
      Python's own.
    """
    #  bool QAuthenticator::operator==(const QAuthenticator &other) const
    return self.uglySide.call(
        'ritual_ZNK14QAuthenticatoreqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QAuthenticator) -> bool:
    """
    Calls Qt's 'bool QAuthenticator::operator!=(const QAuthenticator &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#operator!=

    Parameters
    ----------

    other : QAuthenticator
      Passed on as a value: Qt reads the C++ QAuthenticator, which stays
      Python's own.
    """
    #  bool QAuthenticator::operator!=(const QAuthenticator &other) const
    return self.uglySide.call(
        'ritual_ZNK14QAuthenticatorneERKS_', self._valueOf(other),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QAuthenticator::QAuthenticator()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#QAuthenticator
    """
    #  QAuthenticator::QAuthenticator()
    self._noteCreation(QAuthenticator, lambda: Rituals.call(
        'ritual_ZN14QAuthenticatorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QAuthenticator) -> None:
    """
    Notes what was given, for Qt's 'QAuthenticator::QAuthenticator(const
    QAuthenticator &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#QAuthenticator

    Parameters
    ----------

    other : QAuthenticator
      Passed on as a value: Qt reads the C++ QAuthenticator, which stays
      Python's own.
    """
    #  QAuthenticator::QAuthenticator(const QAuthenticator &other)
    self._noteCreation(QAuthenticator, lambda: Rituals.call(
        'ritual_ZN14QAuthenticatorC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QAuthenticator::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#detach
    """
    #  void QAuthenticator::detach()
    self.uglySide.call('ritual_ZN14QAuthenticator6detachEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QAuthenticator::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qauthenticator.html#clear
    """
    #  void QAuthenticator::clear()
    self.uglySide.call('ritual_ZN14QAuthenticator5clearEv')
