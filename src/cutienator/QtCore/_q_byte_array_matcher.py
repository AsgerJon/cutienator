"""
QByteArrayMatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbytearraymatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QByteArrayMatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QByteArrayMatcher: a plain Python object standing in
  front of one C++ QByteArrayMatcher.

  C++ hands a QByteArrayMatcher around as a copy, so every C++
  QByteArrayMatcher behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QByteArrayMatcher that has a ritual and that Python
  can call so far, 3 names in all: 'setPattern', 'indexIn', 'pattern'. It can
  be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QByteArrayMatcher::~QByteArrayMatcher()': the destructor: Python
    removes its C++ QByteArrayMatcher by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QByteArrayMatcher is created at the first use, not by
    'QByteArrayMatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QByteArrayMatcher back gives a copy the ritual made
    for Python, in a new cute QByteArrayMatcher.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QByteArrayMatcher'

  #  Qt's '~QByteArrayMatcher()'. Naming it makes this a value class: Python
  #  owns every C++ QByteArrayMatcher behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QByteArrayMatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, int)
  @overload(NoneType, int)
  @overload(str, int, int)
  @overload(NoneType, int, int)
  def indexIn(self, str: Optional[str], len: int, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayMatcher::indexIn(const char *str,
    qsizetype len, qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearraymatcher.html#indexIn

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QByteArrayMatcher::indexIn(const char *str, qsizetype len,
    #      qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK17QByteArrayMatcher7indexInEPKcxx',
        self._bytesOf(str), len, from_,
    )

  @overload(QByteArrayView)
  @overload(QByteArrayView, int)
  def indexIn(self, data: QByteArrayView, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayMatcher::indexIn(QByteArrayView data,
    qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearraymatcher.html#indexIn

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QByteArrayMatcher::indexIn(QByteArrayView data, qsizetype
    #      from) const
    return self.uglySide.call(
        'ritual_ZNK17QByteArrayMatcher7indexInE14QByteArrayViewx',
        self._valueOf(data), from_,
    )

  def pattern(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArrayMatcher::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearraymatcher.html#pattern

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArrayMatcher::pattern() const
    address = self.uglySide.call('ritual_ZNK17QByteArrayMatcher7patternEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setPattern(self, pattern: QByteArray) -> None:
    """
    Calls Qt's 'void QByteArrayMatcher::setPattern(const QByteArray
    &pattern)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearraymatcher.html#setPattern

    Parameters
    ----------

    pattern : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QByteArrayMatcher::setPattern(const QByteArray &pattern)
    self.uglySide.call(
        'ritual_ZN17QByteArrayMatcher10setPatternERK10QByteArray',
        self._valueOf(pattern),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QByteArrayMatcher::QByteArrayMatcher()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytearraymatcher.html#QByteArrayMatcher
    """
    #  QByteArrayMatcher::QByteArrayMatcher()
    self._noteCreation(QByteArrayMatcher, lambda: Rituals.call(
        'ritual_ZN17QByteArrayMatcherC1Ev',
    ))

  @overload(QByteArray)
  def __init__(self, pattern: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QByteArrayMatcher::QByteArrayMatcher(const QByteArray &pattern)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytearraymatcher.html#QByteArrayMatcher

    Parameters
    ----------

    pattern : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QByteArrayMatcher::QByteArrayMatcher(const QByteArray &pattern)
    self._noteCreation(QByteArrayMatcher, lambda: Rituals.call(
        'ritual_ZN17QByteArrayMatcherC1ERK10QByteArray',
        self._valueOf(pattern),
    ))

  @overload(QByteArrayView)
  def __init__(self, pattern: QByteArrayView) -> None:
    """
    Notes what was given, for Qt's
    'QByteArrayMatcher::QByteArrayMatcher(QByteArrayView pattern)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytearraymatcher.html#QByteArrayMatcher

    Parameters
    ----------

    pattern : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QByteArrayMatcher::QByteArrayMatcher(QByteArrayView pattern)
    self._noteCreation(QByteArrayMatcher, lambda: Rituals.call(
        'ritual_ZN17QByteArrayMatcherC1E14QByteArrayView',
        self._valueOf(pattern),
    ))

  @overload(str)
  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, pattern: Optional[str], length: int = -1) -> None:
    """
    Notes what was given, for Qt's
    'QByteArrayMatcher::QByteArrayMatcher(const char *pattern, qsizetype
    length)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytearraymatcher.html#QByteArrayMatcher

    Parameters
    ----------

    pattern : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QByteArrayMatcher::QByteArrayMatcher(const char *pattern, qsizetype
    #      length)
    self._noteCreation(QByteArrayMatcher, lambda: Rituals.call(
        'ritual_ZN17QByteArrayMatcherC1EPKcx',
        self._bytesOf(pattern), length,
    ))

  @overload(THIS)
  def __init__(self, other: QByteArrayMatcher) -> None:
    """
    Notes what was given, for Qt's
    'QByteArrayMatcher::QByteArrayMatcher(const QByteArrayMatcher &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytearraymatcher.html#QByteArrayMatcher

    Parameters
    ----------

    other : QByteArrayMatcher
      Passed on as a value: Qt reads the C++ QByteArrayMatcher, which stays
      Python's own.
    """
    #  QByteArrayMatcher::QByteArrayMatcher(const QByteArrayMatcher &other)
    self._noteCreation(QByteArrayMatcher, lambda: Rituals.call(
        'ritual_ZN17QByteArrayMatcherC1ERKS_', self._valueOf(other),
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
