"""
QSslPreSharedKeyAuthenticator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslpresharedkeyauthenticator.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSslPreSharedKeyAuthenticator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslPreSharedKeyAuthenticator: a plain Python object
  standing in front of one C++ QSslPreSharedKeyAuthenticator.

  C++ hands a QSslPreSharedKeyAuthenticator around as a copy, so every C++
  QSslPreSharedKeyAuthenticator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSslPreSharedKeyAuthenticator that has a ritual and
  that Python can call so far, 10 names in all: 'identityHint',
  'setIdentity', 'identity', 'maximumIdentityLength', 'setPreSharedKey',
  'preSharedKey', 'maximumPreSharedKeyLength', 'isEqual', '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslPreSharedKeyAuthenticator::~QSslPreSharedKeyAuthenticator()':
    the destructor: Python removes its C++ QSslPreSharedKeyAuthenticator by
    it, and has no other use for it.
  - Qt's 'QSslPreSharedKeyAuthenticator
    &QSslPreSharedKeyAuthenticator::operator=(const
    QSslPreSharedKeyAuthenticator &authenticator)': assignment: Python binds
    a name and has no operator for it.
  - Qt's 'QSslPreSharedKeyAuthenticator
    &QSslPreSharedKeyAuthenticator::operator=(QSslPreSharedKeyAuthenticator
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void
    QSslPreSharedKeyAuthenticator::swap(QSslPreSharedKeyAuthenticator
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSslPreSharedKeyAuthenticator is created at the first use, not by
    'QSslPreSharedKeyAuthenticator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslPreSharedKeyAuthenticator back gives a copy the
    ritual made for Python, in a new cute QSslPreSharedKeyAuthenticator.
  - Each name of Qt's QSslPreSharedKeyAuthenticator that has no cute function
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
  __qt_class__ = 'QSslPreSharedKeyAuthenticator'

  #  Qt's '~QSslPreSharedKeyAuthenticator()'. Naming it makes this a value
  #  class: Python owns every C++ QSslPreSharedKeyAuthenticator behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QSslPreSharedKeyAuthenticatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def identityHint(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslPreSharedKeyAuthenticator::identityHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#identityHint

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslPreSharedKeyAuthenticator::identityHint() const
    address = self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator12identityHintEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def identity(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslPreSharedKeyAuthenticator::identity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#identity

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslPreSharedKeyAuthenticator::identity() const
    address = self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator8identityEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def maximumIdentityLength(self) -> int:
    """
    Calls Qt's 'int QSslPreSharedKeyAuthenticator::maximumIdentityLength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html
    """
    #  int QSslPreSharedKeyAuthenticator::maximumIdentityLength() const
    return self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator21maximumIdentityLengthEv',
    )

  def preSharedKey(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslPreSharedKeyAuthenticator::preSharedKey()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#preSharedKey

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslPreSharedKeyAuthenticator::preSharedKey() const
    address = self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator12preSharedKeyEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def maximumPreSharedKeyLength(self) -> int:
    """
    Calls Qt's 'int
    QSslPreSharedKeyAuthenticator::maximumPreSharedKeyLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html
    """
    #  int QSslPreSharedKeyAuthenticator::maximumPreSharedKeyLength() const
    return self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator25maximumPreSharedKeyLeng'
        'thEv',
    )

  @overload(THIS)
  def isEqual(self, other: QSslPreSharedKeyAuthenticator) -> bool:
    """
    Calls Qt's 'bool QSslPreSharedKeyAuthenticator::isEqual(const
    QSslPreSharedKeyAuthenticator &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#isEqual

    Parameters
    ----------

    other : QSslPreSharedKeyAuthenticator
      Passed on as a value: Qt reads the C++ QSslPreSharedKeyAuthenticator,
      which stays Python's own.
    """
    #  bool QSslPreSharedKeyAuthenticator::isEqual(const
    #      QSslPreSharedKeyAuthenticator &other) const
    return self.uglySide.call(
        'ritual_ZNK29QSslPreSharedKeyAuthenticator7isEqualERKS_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setIdentity(self, identity: QByteArray) -> None:
    """
    Calls Qt's 'void QSslPreSharedKeyAuthenticator::setIdentity(const
    QByteArray &identity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#setIdentity

    Parameters
    ----------

    identity : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslPreSharedKeyAuthenticator::setIdentity(const QByteArray
    #      &identity)
    self.uglySide.call(
        'ritual_ZN29QSslPreSharedKeyAuthenticator11setIdentityERK10QByteArr'
        'ay',
        self._valueOf(identity),
    )

  @overload(QByteArray)
  def setPreSharedKey(self, preSharedKey: QByteArray) -> None:
    """
    Calls Qt's 'void QSslPreSharedKeyAuthenticator::setPreSharedKey(const
    QByteArray &preSharedKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#setPreSharedKey

    Parameters
    ----------

    preSharedKey : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslPreSharedKeyAuthenticator::setPreSharedKey(const QByteArray
    #      &preSharedKey)
    self.uglySide.call(
        'ritual_ZN29QSslPreSharedKeyAuthenticator15setPreSharedKeyERK10QByt'
        'eArray',
        self._valueOf(preSharedKey),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QSslPreSharedKeyAuthenticator) -> bool:
    """
    Calls Qt's 'bool operator==(const QSslPreSharedKeyAuthenticator &lhs,
    const QSslPreSharedKeyAuthenticator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#operator==

    Parameters
    ----------

    rhs : QSslPreSharedKeyAuthenticator
      Passed on as a value: Qt reads the C++ QSslPreSharedKeyAuthenticator,
      which stays Python's own.
    """
    #  bool operator==(const QSslPreSharedKeyAuthenticator &lhs, const
    #      QSslPreSharedKeyAuthenticator &rhs)
    return Rituals.call(
        'ritual_ZeqRK29QSslPreSharedKeyAuthenticatorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QSslPreSharedKeyAuthenticator) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSslPreSharedKeyAuthenticator &lhs,
    const QSslPreSharedKeyAuthenticator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html#operator!=

    Parameters
    ----------

    rhs : QSslPreSharedKeyAuthenticator
      Passed on as a value: Qt reads the C++ QSslPreSharedKeyAuthenticator,
      which stays Python's own.
    """
    #  bool operator!=(const QSslPreSharedKeyAuthenticator &lhs, const
    #      QSslPreSharedKeyAuthenticator &rhs)
    return Rituals.call(
        'ritual_ZneRK29QSslPreSharedKeyAuthenticatorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's
    'QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html
    """
    #  QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator()
    self._noteCreation(QSslPreSharedKeyAuthenticator, lambda: Rituals.call(
        'ritual_ZN29QSslPreSharedKeyAuthenticatorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, authenticator: QSslPreSharedKeyAuthenticator) -> None:
    """
    Notes what was given, for Qt's
    'QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator(const
    QSslPreSharedKeyAuthenticator &authenticator)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslpresharedkeyauthenticator.html

    Parameters
    ----------

    authenticator : QSslPreSharedKeyAuthenticator
      Passed on as a value: Qt reads the C++ QSslPreSharedKeyAuthenticator,
      which stays Python's own.
    """
    #  QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator(const
    #      QSslPreSharedKeyAuthenticator &authenticator)
    self._noteCreation(QSslPreSharedKeyAuthenticator, lambda: Rituals.call(
        'ritual_ZN29QSslPreSharedKeyAuthenticatorC1ERKS_',
        self._valueOf(authenticator),
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
    Qt's 'void
    QSslPreSharedKeyAuthenticator::swap(QSslPreSharedKeyAuthenticator
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslPreSharedKeyAuthenticator.swap' has no cute function yet. "
        "Qt's 'void "
        "QSslPreSharedKeyAuthenticator::swap(QSslPreSharedKeyAuthenticator "
        "&other)': takes a type Python has no way to hand over yet.")
