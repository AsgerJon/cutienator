"""
QCollatorSortKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCollatorSortKeyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCollatorSortKeyPrivate = WAIT['QCollatorSortKeyPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCollatorSortKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCollatorSortKey: a plain Python object standing in
  front of one C++ QCollatorSortKey.

  C++ hands a QCollatorSortKey around as a copy, so every C++
  QCollatorSortKey behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCollatorSortKey that has a ritual and that Python
  can call so far, 7 names in all: 'compare', '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCollatorSortKey::QCollatorSortKey(QCollatorSortKey &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCollatorSortKey::~QCollatorSortKey()': the destructor: Python
    removes its C++ QCollatorSortKey by it, and has no other use for it.
  - Qt's 'QCollatorSortKey &QCollatorSortKey::operator=(const
    QCollatorSortKey &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCollatorSortKey &QCollatorSortKey::operator=(QCollatorSortKey
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCollatorSortKey::swap(QCollatorSortKey &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QCollatorSortKey is created at the first use, not by
    'QCollatorSortKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCollatorSortKey back gives a copy the ritual made
    for Python, in a new cute QCollatorSortKey.
  - Each name of Qt's QCollatorSortKey that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCollatorSortKey'

  #  Qt's '~QCollatorSortKey()'. Naming it makes this a value class: Python
  #  owns every C++ QCollatorSortKey behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QCollatorSortKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def compare(self, key: QCollatorSortKey) -> int:
    """
    Calls Qt's 'int QCollatorSortKey::compare(const QCollatorSortKey &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#compare

    Parameters
    ----------

    key : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  int QCollatorSortKey::compare(const QCollatorSortKey &key) const
    return self.uglySide.call(
        'ritual_ZNK16QCollatorSortKey7compareERKS_', self._valueOf(key),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator==(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator==

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator==(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QCollatorSortKeyS1_',
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
  def __ne__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator!=

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator!=(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QCollatorSortKeyS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator<(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator<

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator<(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK16QCollatorSortKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator>(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator>

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator>(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK16QCollatorSortKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator<=

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator<=(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZleRK16QCollatorSortKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QCollatorSortKey) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCollatorSortKey &lhs, const
    QCollatorSortKey &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorsortkey.html#operator>=

    Parameters
    ----------

    rhs : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  bool operator>=(const QCollatorSortKey &lhs, const QCollatorSortKey
    #      &rhs)
    return Rituals.call(
        'ritual_ZgeRK16QCollatorSortKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, other: QCollatorSortKey) -> None:
    """
    Notes what was given, for Qt's 'QCollatorSortKey::QCollatorSortKey(const
    QCollatorSortKey &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollatorsortkey.html#QCollatorSortKey

    Parameters
    ----------

    other : QCollatorSortKey
      Passed on as a value: Qt reads the C++ QCollatorSortKey, which stays
      Python's own.
    """
    #  QCollatorSortKey::QCollatorSortKey(const QCollatorSortKey &other)
    self._noteCreation(QCollatorSortKey, lambda: Rituals.call(
        'ritual_ZN16QCollatorSortKeyC1ERKS_', self._valueOf(other),
    ))

  @overload(QCollatorSortKeyPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QCollatorSortKeyPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCollatorSortKey::QCollatorSortKey(QCollatorSortKeyPrivate *a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollatorsortkey.html#QCollatorSortKey

    Parameters
    ----------

    a0 : Optional[QCollatorSortKeyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCollatorSortKey::QCollatorSortKey(QCollatorSortKeyPrivate *a0)
    self._noteCreation(QCollatorSortKey, lambda: Rituals.call(
        'ritual_ZN16QCollatorSortKeyC1EP23QCollatorSortKeyPrivate',
        self._addressOf(a0),
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
    Qt's 'void QCollatorSortKey::swap(QCollatorSortKey &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCollatorSortKey.swap' has no cute function yet. Qt's 'void "
        "QCollatorSortKey::swap(QCollatorSortKey &other)': takes a type "
        "Python has no way to hand over yet.")
