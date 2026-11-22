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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QKeyCombination
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyCombination = WAIT['QKeyCombination']


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
  call so far, 17 names in all: 'count', 'isEmpty', 'toString', 'fromString',
  'listFromString', 'listToString', 'matches', 'mnemonic', 'keyBindings',
  '__getitem__', '__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__',
  'isDetached'. It can be made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeySequence::~QKeySequence()': the destructor: Python removes its
    C++ QKeySequence by it, and has no other use for it.
  - Qt's 'QVariant QKeySequence::operator QVariant() const': an operator
    Python has no name for.

  What has no ritual
  ------------------

  12 of the 37 functions Qt declares: 6 takes or gives a type that cannot be
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

  #  The enums Qt writes inside QKeySequence, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SequenceFormat(CuteNum):
    """
    The enum 'QKeySequence::SequenceFormat' of Qt, with the 2 names Qt gives
    in it.
    """

    NativeText = Kee[int](0)
    PortableText = Kee[int](1)

  class SequenceMatch(CuteNum):
    """
    The enum 'QKeySequence::SequenceMatch' of Qt, with the 3 names Qt gives
    in it.
    """

    NoMatch = Kee[int](0)
    PartialMatch = Kee[int](1)
    ExactMatch = Kee[int](2)

  class StandardKey(CuteNum):
    """
    The enum 'QKeySequence::StandardKey' of Qt, with the 71 names Qt gives in
    it.
    """

    UnknownKey = Kee[int](0)
    HelpContents = Kee[int](1)
    WhatsThis = Kee[int](2)
    Open = Kee[int](3)
    Close = Kee[int](4)
    Save = Kee[int](5)
    New = Kee[int](6)
    Delete = Kee[int](7)
    Cut = Kee[int](8)
    Copy = Kee[int](9)
    Paste = Kee[int](10)
    Undo = Kee[int](11)
    Redo = Kee[int](12)
    Back = Kee[int](13)
    Forward = Kee[int](14)
    Refresh = Kee[int](15)
    ZoomIn = Kee[int](16)
    ZoomOut = Kee[int](17)
    Print = Kee[int](18)
    AddTab = Kee[int](19)
    NextChild = Kee[int](20)
    PreviousChild = Kee[int](21)
    Find = Kee[int](22)
    FindNext = Kee[int](23)
    FindPrevious = Kee[int](24)
    Replace = Kee[int](25)
    SelectAll = Kee[int](26)
    Bold = Kee[int](27)
    Italic = Kee[int](28)
    Underline = Kee[int](29)
    MoveToNextChar = Kee[int](30)
    MoveToPreviousChar = Kee[int](31)
    MoveToNextWord = Kee[int](32)
    MoveToPreviousWord = Kee[int](33)
    MoveToNextLine = Kee[int](34)
    MoveToPreviousLine = Kee[int](35)
    MoveToNextPage = Kee[int](36)
    MoveToPreviousPage = Kee[int](37)
    MoveToStartOfLine = Kee[int](38)
    MoveToEndOfLine = Kee[int](39)
    MoveToStartOfBlock = Kee[int](40)
    MoveToEndOfBlock = Kee[int](41)
    MoveToStartOfDocument = Kee[int](42)
    MoveToEndOfDocument = Kee[int](43)
    SelectNextChar = Kee[int](44)
    SelectPreviousChar = Kee[int](45)
    SelectNextWord = Kee[int](46)
    SelectPreviousWord = Kee[int](47)
    SelectNextLine = Kee[int](48)
    SelectPreviousLine = Kee[int](49)
    SelectNextPage = Kee[int](50)
    SelectPreviousPage = Kee[int](51)
    SelectStartOfLine = Kee[int](52)
    SelectEndOfLine = Kee[int](53)
    SelectStartOfBlock = Kee[int](54)
    SelectEndOfBlock = Kee[int](55)
    SelectStartOfDocument = Kee[int](56)
    SelectEndOfDocument = Kee[int](57)
    DeleteStartOfWord = Kee[int](58)
    DeleteEndOfWord = Kee[int](59)
    DeleteEndOfLine = Kee[int](60)
    InsertParagraphSeparator = Kee[int](61)
    InsertLineSeparator = Kee[int](62)
    SaveAs = Kee[int](63)
    Preferences = Kee[int](64)
    Quit = Kee[int](65)
    FullScreen = Kee[int](66)
    Deselect = Kee[int](67)
    DeleteCompleteLine = Kee[int](68)
    Backspace = Kee[int](69)
    Cancel = Kee[int](70)

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
  @overload(str, SequenceFormat)
  def listFromString(
      str: str,
      format: SequenceFormat = SequenceFormat.PortableText,
  ) -> QList[QKeySequence]:
    """
    Calls Qt's 'QList<QKeySequence> QKeySequence::listFromString(const
    QString &str, SequenceFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#listFromString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    format : SequenceFormat
      Passed on as its number. May be left out, as in Qt: it is then
      SequenceFormat.PortableText.

    Returns
    -------

    QList[QKeySequence]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeySequence> QKeySequence::listFromString(const QString &str,
    #      SequenceFormat format)
    address = Rituals.call(
        'ritual_ZN12QKeySequence14listFromStringERK7QStringNS_14SequenceFor'
        'matE',
        str, format.value,
    )
    return QList[QKeySequence]._cuteOwning(address)

  @staticmethod
  @overload(QList[WAIT['QKeySequence']])
  @overload(QList[WAIT['QKeySequence']], SequenceFormat)
  def listToString(
      list: QList[QKeySequence],
      format: SequenceFormat = SequenceFormat.PortableText,
  ) -> str:
    """
    Calls Qt's 'QString QKeySequence::listToString(const QList<QKeySequence>
    &list, SequenceFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#listToString

    Parameters
    ----------

    list : QList[QKeySequence]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    format : SequenceFormat
      Passed on as its number. May be left out, as in Qt: it is then
      SequenceFormat.PortableText.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QKeySequence::listToString(const QList<QKeySequence> &list,
    #      SequenceFormat format)
    return Rituals.call(
        'ritual_ZN12QKeySequence12listToStringERK5QListIS_ENS_14SequenceFor'
        'matE',
        CuteMixin._valueOf(list), format.value,
    )

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

  @staticmethod
  @overload(StandardKey)
  def keyBindings(key: StandardKey) -> QList[QKeySequence]:
    """
    Calls Qt's 'QList<QKeySequence> QKeySequence::keyBindings(StandardKey
    key)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#keyBindings

    Parameters
    ----------

    key : StandardKey
      Passed on as its number.

    Returns
    -------

    QList[QKeySequence]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeySequence> QKeySequence::keyBindings(StandardKey key)
    address = Rituals.call(
        'ritual_ZN12QKeySequence11keyBindingsENS_11StandardKeyE', key.value,
    )
    return QList[QKeySequence]._cuteOwning(address)

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
    return QKeySequence.SequenceMatch(self.uglySide.call(
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

  @overload(int)
  def __getitem__(self, i: int) -> QKeyCombination:
    """
    Calls Qt's 'QKeyCombination QKeySequence::operator[](uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QKeyCombination
      A new cute QKeyCombination around the copy Qt gave back. Python owns
      it.
    """
    #  QKeyCombination QKeySequence::operator[](uint i) const
    address = self.uglySide.call('ritual_ZNK12QKeySequenceixEj', i)
    from ..QtCore import QKeyCombination
    return QKeyCombination._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, other: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator==(const QKeySequence &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator==

    Parameters
    ----------

    other : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator==(const QKeySequence &other) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequenceeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator!=(const QKeySequence &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator!=

    Parameters
    ----------

    other : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator!=(const QKeySequence &other) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequenceneERKS_', self._valueOf(other),
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
  def __lt__(self, ks: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator<(const QKeySequence &ks) const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator<

    Parameters
    ----------

    ks : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator<(const QKeySequence &ks) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequenceltERKS_', self._valueOf(ks),
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
  def __gt__(self, other: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator>(const QKeySequence &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator>

    Parameters
    ----------

    other : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator>(const QKeySequence &other) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequencegtERKS_', self._valueOf(other),
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
  def __le__(self, other: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator<=(const QKeySequence &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator<=

    Parameters
    ----------

    other : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator<=(const QKeySequence &other) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequenceleERKS_', self._valueOf(other),
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
  def __ge__(self, other: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QKeySequence::operator>=(const QKeySequence &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#operator>=

    Parameters
    ----------

    other : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QKeySequence::operator>=(const QKeySequence &other) const
    return self.uglySide.call(
        'ritual_ZNK12QKeySequencegeERKS_', self._valueOf(other),
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

  @overload(
      QKeyCombination, QKeyCombination, QKeyCombination, QKeyCombination,
  )
  def __init__(
      self,
      k1: QKeyCombination,
      k2: QKeyCombination,
      k3: QKeyCombination,
      k4: QKeyCombination,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QKeySequence::QKeySequence(QKeyCombination k1, QKeyCombination k2,
    QKeyCombination k3, QKeyCombination k4)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequence.html#QKeySequence

    Parameters
    ----------

    k1 : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.

    k2 : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.

    k3 : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.

    k4 : QKeyCombination
      Passed on as a value: Qt reads the C++ QKeyCombination, which stays
      Python's own.
    """
    #  QKeySequence::QKeySequence(QKeyCombination k1, QKeyCombination k2,
    #      QKeyCombination k3, QKeyCombination k4)
    self._noteCreation(QKeySequence, lambda: Rituals.call(
        'ritual_ZN12QKeySequenceC1E15QKeyCombinationS0_S0_S0_',
        self._valueOf(k1), self._valueOf(k2), self._valueOf(k3),
        self._valueOf(k4),
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


#  Qt's 'QList<QKeySequence>': the list of QKeySequence, which
#  'QList[QKeySequence]' gives. It is made here, so that there is one as soon
#  as there can be a QKeySequence.
QList.createKind(
    QKeySequence, 'value',
    make='ritual_list_make_QKeySequence',
    add='ritual_list_add_QKeySequence',
    size='ritual_list_size_QKeySequence',
    at='ritual_list_at_QKeySequence',
    drop='ritual_list_drop_QKeySequence',
)
