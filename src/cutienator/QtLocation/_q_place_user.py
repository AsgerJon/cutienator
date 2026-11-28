"""
QPlaceUser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceuser.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlaceUser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceUser: a plain Python object standing in front
  of one C++ QPlaceUser.

  C++ hands a QPlaceUser around as a copy, so every C++ QPlaceUser behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceUser that has a ritual and that Python can
  call so far, 7 names in all: '__eq__', '__ne__', 'userId', 'setUserId',
  'name', 'setName', 'isEqual'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceUser::QPlaceUser(QPlaceUser &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QPlaceUser::~QPlaceUser()': the destructor: Python removes its C++
    QPlaceUser by it, and has no other use for it.
  - Qt's 'QPlaceUser &QPlaceUser::operator=(const QPlaceUser &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceUser &QPlaceUser::operator=(QPlaceUser &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QPlaceUser::swap(QPlaceUser &other)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceUser is created at the first use, not by 'QPlaceUser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceUser back gives a copy the ritual made for
    Python, in a new cute QPlaceUser.
  - Each name of Qt's QPlaceUser that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceUser'

  #  Qt's '~QPlaceUser()'. Naming it makes this a value class: Python owns
  #  every C++ QPlaceUser behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QPlaceUserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def userId(self) -> str:
    """
    Calls Qt's 'QString QPlaceUser::userId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#userId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceUser::userId() const
    return self.uglySide.call('ritual_ZNK10QPlaceUser6userIdEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlaceUser::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceUser::name() const
    return self.uglySide.call('ritual_ZNK10QPlaceUser4nameEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceUser) -> bool:
    """
    Calls Qt's 'bool QPlaceUser::isEqual(const QPlaceUser &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#isEqual

    Parameters
    ----------

    other : QPlaceUser
      Passed on as a value: Qt reads the C++ QPlaceUser, which stays Python's
      own.
    """
    #  bool QPlaceUser::isEqual(const QPlaceUser &other) const
    return self.uglySide.call(
        'ritual_ZNK10QPlaceUser7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUserId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlaceUser::setUserId(const QString &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#setUserId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceUser::setUserId(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN10QPlaceUser9setUserIdERK7QString', identifier,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QPlaceUser::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceUser::setName(const QString &name)
    self.uglySide.call('ritual_ZN10QPlaceUser7setNameERK7QString', name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceUser) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceUser &lhs, const QPlaceUser
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#operator==

    Parameters
    ----------

    rhs : QPlaceUser
      Passed on as a value: Qt reads the C++ QPlaceUser, which stays Python's
      own.
    """
    #  bool operator==(const QPlaceUser &lhs, const QPlaceUser &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QPlaceUserS1_',
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
  def __ne__(self, rhs: QPlaceUser) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceUser &lhs, const QPlaceUser
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#operator!=

    Parameters
    ----------

    rhs : QPlaceUser
      Passed on as a value: Qt reads the C++ QPlaceUser, which stays Python's
      own.
    """
    #  bool operator!=(const QPlaceUser &lhs, const QPlaceUser &rhs)
    return Rituals.call(
        'ritual_ZneRK10QPlaceUserS1_',
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
    Notes what was given, for Qt's 'QPlaceUser::QPlaceUser()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#QPlaceUser
    """
    #  QPlaceUser::QPlaceUser()
    self._noteCreation(QPlaceUser, lambda: Rituals.call(
        'ritual_ZN10QPlaceUserC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceUser) -> None:
    """
    Notes what was given, for Qt's 'QPlaceUser::QPlaceUser(const QPlaceUser
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceuser.html#QPlaceUser

    Parameters
    ----------

    other : QPlaceUser
      Passed on as a value: Qt reads the C++ QPlaceUser, which stays Python's
      own.
    """
    #  QPlaceUser::QPlaceUser(const QPlaceUser &other)
    self._noteCreation(QPlaceUser, lambda: Rituals.call(
        'ritual_ZN10QPlaceUserC1ERKS_', self._valueOf(other),
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
    Qt's 'void QPlaceUser::swap(QPlaceUser &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceUser.swap' has no cute function yet. Qt's 'void "
        "QPlaceUser::swap(QPlaceUser &other)': takes a type Python has no "
        "way to hand over yet.")
