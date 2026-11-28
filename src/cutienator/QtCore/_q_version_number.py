"""
QVersionNumber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qversionnumber.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVersionNumber(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVersionNumber: a plain Python object standing in
  front of one C++ QVersionNumber.

  C++ hands a QVersionNumber around as a copy, so every C++ QVersionNumber
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVersionNumber that has a ritual and that Python can
  call so far, 18 names in all: 'isNull', 'isNormalized', 'majorVersion',
  'minorVersion', 'microVersion', 'normalized', 'segmentAt', 'segmentCount',
  'isPrefixOf', 'compare', 'commonPrefix', 'toString', '__eq__', '__ne__',
  '__lt__', '__gt__', '__le__', '__ge__'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVersionNumber::QVersionNumber(std::initializer_list<int> args)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QVersionNumber::QVersionNumber(QSpan<const int> args)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<int> QVersionNumber::segments() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::begin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::end() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::cbegin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::cend() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_reverse_iterator QVersionNumber::rbegin() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_reverse_iterator QVersionNumber::rend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QVersionNumber::crbegin() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_reverse_iterator QVersionNumber::crend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::constBegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QVersionNumber::constEnd() const': gives a type
    Python has no way to take yet.
  - Qt's 'QVersionNumber QVersionNumber::fromString(QAnyStringView string,
    qsizetype *suffixIndex)': takes a number to change where it is.
  - Qt's 'QDataStream &operator>>(QDataStream &in, QVersionNumber &version)':
    an operator between other classes, written inside this one.
  - Qt's 'QVersionNumber::~QVersionNumber()': the destructor: Python removes
    its C++ QVersionNumber by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 41 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QVersionNumber is created at the first use, not by
    'QVersionNumber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVersionNumber back gives a copy the ritual made for
    Python, in a new cute QVersionNumber.
  - Each name of Qt's QVersionNumber that has no cute function yet, 'begin',
    'cbegin', 'cend', 'constBegin', 'constEnd', 'crbegin', 'crend', 'end',
    'fromString', 'rbegin', 'rend', 'segments', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def compare(v1: QVersionNumber, v2: QVersionNumber) -> int:
    """
    Calls Qt's 'int QVersionNumber::compare(const QVersionNumber &v1, const
    QVersionNumber &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#compare

    Parameters
    ----------

    v1 : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.

    v2 : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  int QVersionNumber::compare(const QVersionNumber &v1, const
    #      QVersionNumber &v2)
    return Rituals.call(
        'ritual_ZN14QVersionNumber7compareERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  @staticmethod
  @overload(THIS, THIS)
  def commonPrefix(v1: QVersionNumber, v2: QVersionNumber) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QVersionNumber::commonPrefix(const
    QVersionNumber &v1, const QVersionNumber &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#commonPrefix

    Parameters
    ----------

    v1 : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.

    v2 : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QVersionNumber::commonPrefix(const QVersionNumber &v1,
    #      const QVersionNumber &v2)
    address = Rituals.call(
        'ritual_ZN14QVersionNumber12commonPrefixERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )
    return QVersionNumber._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVersionNumber'

  #  Qt's '~QVersionNumber()'. Naming it makes this a value class: Python
  #  owns every C++ QVersionNumber behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QVersionNumberD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QVersionNumber::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#isNull
    """
    #  bool QVersionNumber::isNull() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber6isNullEv')

  def isNormalized(self) -> bool:
    """
    Calls Qt's 'bool QVersionNumber::isNormalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#isNormalized
    """
    #  bool QVersionNumber::isNormalized() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber12isNormalizedEv')

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QVersionNumber::majorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#majorVersion
    """
    #  int QVersionNumber::majorVersion() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber12majorVersionEv')

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QVersionNumber::minorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#minorVersion
    """
    #  int QVersionNumber::minorVersion() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber12minorVersionEv')

  def microVersion(self) -> int:
    """
    Calls Qt's 'int QVersionNumber::microVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#microVersion
    """
    #  int QVersionNumber::microVersion() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber12microVersionEv')

  def normalized(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QVersionNumber::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#normalized

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QVersionNumber::normalized() const
    address = self.uglySide.call('ritual_ZNK14QVersionNumber10normalizedEv')
    return QVersionNumber._cuteOwning(address)

  @overload(int)
  def segmentAt(self, index: int) -> int:
    """
    Calls Qt's 'int QVersionNumber::segmentAt(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#segmentAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QVersionNumber::segmentAt(qsizetype index) const
    return self.uglySide.call(
        'ritual_ZNK14QVersionNumber9segmentAtEx', index,
    )

  def segmentCount(self) -> int:
    """
    Calls Qt's 'qsizetype QVersionNumber::segmentCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#segmentCount
    """
    #  qsizetype QVersionNumber::segmentCount() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber12segmentCountEv')

  @overload(THIS)
  def isPrefixOf(self, other: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool QVersionNumber::isPrefixOf(const QVersionNumber &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#isPrefixOf

    Parameters
    ----------

    other : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool QVersionNumber::isPrefixOf(const QVersionNumber &other) const
    return self.uglySide.call(
        'ritual_ZNK14QVersionNumber10isPrefixOfERKS_', self._valueOf(other),
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString QVersionNumber::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVersionNumber::toString() const
    return self.uglySide.call('ritual_ZNK14QVersionNumber8toStringEv')

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
  def __eq__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator==(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator==

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator==(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QVersionNumberS1_',
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
  def __ne__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator!=(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator!=

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator!=(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZneRK14QVersionNumberS1_',
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
  def __lt__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator<(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator<

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator<(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZltRK14QVersionNumberS1_',
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
  def __gt__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator>(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator>

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator>(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZgtRK14QVersionNumberS1_',
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
  def __le__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator<=(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator<=

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator<=(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZleRK14QVersionNumberS1_',
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
  def __ge__(self, rhs: QVersionNumber) -> bool:
    """
    Calls Qt's 'bool operator>=(const QVersionNumber &lhs, const
    QVersionNumber &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#operator>=

    Parameters
    ----------

    rhs : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  bool operator>=(const QVersionNumber &lhs, const QVersionNumber &rhs)
    return Rituals.call(
        'ritual_ZgeRK14QVersionNumberS1_',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QVersionNumber::QVersionNumber()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#QVersionNumber
    """
    #  QVersionNumber::QVersionNumber()
    self._noteCreation(QVersionNumber, lambda: Rituals.call(
        'ritual_ZN14QVersionNumberC1Ev',
    ))

  @overload(int)
  def __init__(self, maj: int) -> None:
    """
    Notes what was given, for Qt's 'QVersionNumber::QVersionNumber(int maj)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#QVersionNumber

    Parameters
    ----------

    maj : int
      Passed on as it is.
    """
    #  QVersionNumber::QVersionNumber(int maj)
    self._noteCreation(QVersionNumber, lambda: Rituals.call(
        'ritual_ZN14QVersionNumberC1Ei', maj,
    ))

  @overload(int, int)
  def __init__(self, maj: int, min: int) -> None:
    """
    Notes what was given, for Qt's 'QVersionNumber::QVersionNumber(int maj,
    int min)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#QVersionNumber

    Parameters
    ----------

    maj : int
      Passed on as it is.

    min : int
      Passed on as it is.
    """
    #  QVersionNumber::QVersionNumber(int maj, int min)
    self._noteCreation(QVersionNumber, lambda: Rituals.call(
        'ritual_ZN14QVersionNumberC1Eii', maj, min,
    ))

  @overload(int, int, int)
  def __init__(self, maj: int, min: int, mic: int) -> None:
    """
    Notes what was given, for Qt's 'QVersionNumber::QVersionNumber(int maj,
    int min, int mic)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qversionnumber.html#QVersionNumber

    Parameters
    ----------

    maj : int
      Passed on as it is.

    min : int
      Passed on as it is.

    mic : int
      Passed on as it is.
    """
    #  QVersionNumber::QVersionNumber(int maj, int min, int mic)
    self._noteCreation(QVersionNumber, lambda: Rituals.call(
        'ritual_ZN14QVersionNumberC1Eiii', maj, min, mic,
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
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::begin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.begin' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::begin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::cbegin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.cbegin' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::cbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::cend() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.cend' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::cend() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::constBegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.constBegin' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::constBegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::constEnd() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.constEnd' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::constEnd() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QVersionNumber::crbegin() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QVersionNumber::crbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QVersionNumber::crend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QVersionNumber::crend() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QVersionNumber::end() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.end' has no cute function yet. Qt's "
        "'const_iterator QVersionNumber::end() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def fromString(*__, **_) -> Never:
    """
    - Qt's 'QVersionNumber QVersionNumber::fromString(QAnyStringView string,
      qsizetype *suffixIndex)': takes a number to change where it is.
    - Qt's 'QVersionNumber::fromString': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QVersionNumber.fromString' has no cute function yet. Qt's "
        "'QVersionNumber QVersionNumber::fromString(QAnyStringView string, "
        "qsizetype *suffixIndex)': takes a number to change where it is. "
        "Qt's 'QVersionNumber::fromString': a template: a pattern and no "
        "single function.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QVersionNumber::rbegin() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QVersionNumber::rbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QVersionNumber::rend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator QVersionNumber::rend() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def segments(*__, **_) -> Never:
    """
    Qt's 'QList<int> QVersionNumber::segments() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVersionNumber.segments' has no cute function yet. Qt's "
        "'QList<int> QVersionNumber::segments() const': gives a type Python "
        "has no way to take yet.")


#  Qt's 'QList<QVersionNumber>': the list of QVersionNumber, which
#  'QList[QVersionNumber]' gives. It is made here, so that there is one as
#  soon as there can be a QVersionNumber.
QList.createKind(
    QVersionNumber, 'value',
    make='ritual_list_make_QVersionNumber',
    add='ritual_list_add_QVersionNumber',
    size='ritual_list_size_QVersionNumber',
    at='ritual_list_at_QVersionNumber',
    drop='ritual_list_drop_QVersionNumber',
)


#  Qt's 'QMap<QString, QVersionNumber>': the QMap from text to
#  QVersionNumber, which 'QMap[str, QVersionNumber]' gives. It is completed
#  here, in the file of the class of its values.
QMap.createKind(
    str, QVersionNumber, 'value',
    make='ritual_map_make_QMap_QString_QVersionNumber',
    put='ritual_map_put_QMap_QString_QVersionNumber',
    size='ritual_map_size_QMap_QString_QVersionNumber',
    key='ritual_map_key_QMap_QString_QVersionNumber',
    value='ritual_map_value_QMap_QString_QVersionNumber',
    has='ritual_map_has_QMap_QString_QVersionNumber',
    get='ritual_map_get_QMap_QString_QVersionNumber',
    drop='ritual_map_drop_QMap_QString_QVersionNumber',
)
