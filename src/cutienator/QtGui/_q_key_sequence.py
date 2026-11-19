"""
QKeySequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qkeysequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_key_sequence_sequence_format import SequenceFormat
from ._q_key_sequence_sequence_match import SequenceMatch
from ._q_key_sequence_standard_key import StandardKey


class QKeySequence(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QKeySequence: a plain Python object standing in front
  of one C++ QKeySequence.

  C++ hands a QKeySequence around as a copy, so every C++ QKeySequence behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QKeySequence that has a ritual and that Python can
  call so far, 7 names in all: 'count', 'isEmpty', 'toString', 'fromString',
  'matches', 'mnemonic', 'isDetached'. It can be made from Python, in 5 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeySequence::QKeySequence(QKeyCombination k1, QKeyCombination k2,
    QKeyCombination k3, QKeyCombination k4)': names 'QKeyCombination', which
    has no cute class yet.
  - Qt's 'QKeySequence::~QKeySequence()': the destructor: Python removes its
    C++ QKeySequence by it, and has no other use for it.
  - Qt's 'QVariant QKeySequence::operator QVariant() const': an operator,
    which is not reflected yet.
  - Qt's 'QKeyCombination QKeySequence::operator[](uint i) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator==(const QKeySequence &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator!=(const QKeySequence &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator<(const QKeySequence &ks) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator>(const QKeySequence &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator<=(const QKeySequence &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QKeySequence::operator>=(const QKeySequence &other) const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  13 of the 35 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 4 private; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QKeySequence is created at the first use, not by
    'QKeySequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QKeySequence back gives a copy the ritual made for
    Python, in a new cute QKeySequence.
  """

  #  The enums Qt writes inside QKeySequence, and the names Qt has for the
  #  combinations of its flags enums.
  SequenceFormat = SequenceFormat
  SequenceMatch = SequenceMatch
  StandardKey = StandardKey

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(str, SequenceFormat)
  def fromString(
      str: str,
      format: SequenceFormat = SequenceFormat.PortableText,
  ) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QKeySequence::fromString(const QString &str,
    SequenceFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#fromString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    format : SequenceFormat
      Passed on as its number. May be left out, as in Qt: it is then
      SequenceFormat.PortableText.

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QKeySequence::fromString(const QString &str,
    #      SequenceFormat format)
    address = Rituals.call(
        'ritual_ZN12QKeySequence10fromStringERK7QStringNS_14SequenceFormatE',
        str, format.value,
    )
    return QKeySequence._cuteOwning(address)

  @staticmethod
  @overload(str)
  def mnemonic(text: str) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QKeySequence::mnemonic(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#mnemonic

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QKeySequence::mnemonic(const QString &text)
    address = Rituals.call(
        'ritual_ZN12QKeySequence8mnemonicERK7QString', text,
    )
    return QKeySequence._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeySequence'

  #  Qt's '~QKeySequence()'. Naming it makes this a value class: Python owns
  #  every C++ QKeySequence behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QKeySequenceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QKeySequence::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#count
    """
    #  int QKeySequence::count() const
    return self.uglySide.call('ritual_ZNK12QKeySequence5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QKeySequence::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#isEmpty
    """
    #  bool QKeySequence::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QKeySequence7isEmptyEv')

  @overload()
  @overload(SequenceFormat)
  def toString(
      self,
      format: SequenceFormat = SequenceFormat.PortableText,
  ) -> str:
    """
    Calls Qt's 'QString QKeySequence::toString(SequenceFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#toString

    Parameters
    ----------

    format : SequenceFormat
      Passed on as its number. May be left out, as in Qt: it is then
      SequenceFormat.PortableText.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QKeySequence::toString(SequenceFormat format) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequence8toStringENS_14SequenceFormatE',
        format.value,
    )

  @overload(THIS)
  def matches(self, seq: QKeySequence) -> SequenceMatch:
    """
    Calls Qt's 'SequenceMatch QKeySequence::matches(const QKeySequence &seq)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#matches

    Parameters
    ----------

    seq : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    Returns
    -------

    SequenceMatch
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SequenceMatch(number)'
      gives.
    """
    #  SequenceMatch QKeySequence::matches(const QKeySequence &seq) const
    return SequenceMatch(self.uglySide.call(
        'ritual_ZNK12QKeySequence7matchesERKS_', self._valueOf(seq),
    ))

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QKeySequence::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#isDetached
    """
    #  bool QKeySequence::isDetached() const
    return self.uglySide.call('ritual_ZNK12QKeySequence10isDetachedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QKeySequence::QKeySequence()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence
    """
    #  QKeySequence::QKeySequence()
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1Ev',
    ))

  @overload(str)
  @overload(str, SequenceFormat)
  def __init__(
      self,
      key: str,
      format: SequenceFormat = SequenceFormat.NativeText,
  ) -> None:
    """
    Notes what was given, for Qt's 'QKeySequence::QKeySequence(const QString
    &key, SequenceFormat format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    format : SequenceFormat
      Passed on as its number. May be left out, as in Qt: it is then
      SequenceFormat.NativeText.
    """
    #  QKeySequence::QKeySequence(const QString &key, SequenceFormat format)
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1ERK7QStringNS_14SequenceFormatE',
        key, format.value,
    ))

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def __init__(self, k1: int, k2: int = 0, k3: int = 0, k4: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QKeySequence::QKeySequence(int k1, int
    k2, int k3, int k4)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence

    Parameters
    ----------

    k1 : int
      Passed on as it is.

    k2 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    k3 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    k4 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QKeySequence::QKeySequence(int k1, int k2, int k3, int k4)
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1Eiiii', k1, k2, k3, k4,
    ))

  @overload(THIS)
  def __init__(self, ks: QKeySequence) -> None:
    """
    Notes what was given, for Qt's 'QKeySequence::QKeySequence(const
    QKeySequence &ks)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence

    Parameters
    ----------

    ks : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  QKeySequence::QKeySequence(const QKeySequence &ks)
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1ERKS_', self._valueOf(ks),
    ))

  @overload(StandardKey)
  def __init__(self, key: StandardKey) -> None:
    """
    Notes what was given, for Qt's 'QKeySequence::QKeySequence(StandardKey
    key)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence

    Parameters
    ----------

    key : StandardKey
      Passed on as its number.
    """
    #  QKeySequence::QKeySequence(StandardKey key)
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1ENS_11StandardKeyE', key.value,
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
