"""
QLCDNumber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlcdnumber.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLCDNumber(QFrame):
  """
  The cute side of Qt's QLCDNumber: a plain Python object standing in front
  of one C++ QLCDNumber.

  It is built on the cute 'QFrame', as Qt's QLCDNumber is built on Qt's
  QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLCDNumber that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'smallDecimalPoint',
  'digitCount', 'setDigitCount', 'checkOverflow', 'mode', 'setMode',
  'segmentStyle', 'setSegmentStyle', 'value', 'intValue', 'sizeHint',
  'display', 'setHexMode', 'setDecMode', 'setOctMode', 'setBinMode',
  'setSmallDecimalPoint', 'overflow', 'event', 'paintEvent'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLCDNumber::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLCDNumber::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLCDNumber::~QLCDNumber()': the destructor: Python never removes a
    C++ QLCDNumber.
  - Qt's 'QLCDNumberPrivate *QLCDNumber::d_func()': gives
    'QLCDNumberPrivate', which has no cute class yet.
  - Qt's 'const QLCDNumberPrivate *QLCDNumber::d_func() const': gives
    'QLCDNumberPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLCDNumber is created at the first use, not by 'QLCDNumber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLCDNumber.
  - Qt tells when it has removed the C++ QLCDNumber. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QLCDNumber, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """The enum 'QLCDNumber::Mode' of Qt, with the 4 names Qt gives in it."""

    Hex = Kee[int](0)
    Dec = Kee[int](1)
    Oct = Kee[int](2)
    Bin = Kee[int](3)

  class SegmentStyle(CuteNum):
    """
    The enum 'QLCDNumber::SegmentStyle' of Qt, with the 3 names Qt gives in
    it.
    """

    Outline = Kee[int](0)
    Filled = Kee[int](1)
    Flat = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QLCDNumber::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLCDNumber::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QLCDNumber2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLCDNumber'

  #  A C++ QLCDNumber Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLCDNumber'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLCDNumber::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLCDNumber::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QLCDNumber10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def smallDecimalPoint(self) -> bool:
    """
    Calls Qt's 'bool QLCDNumber::smallDecimalPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#smallDecimalPoint
    """
    #  bool QLCDNumber::smallDecimalPoint() const
    return self.uglySide.call('ritual_ZNK10QLCDNumber17smallDecimalPointEv')

  def digitCount(self) -> int:
    """
    Calls Qt's 'int QLCDNumber::digitCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#digitCount
    """
    #  int QLCDNumber::digitCount() const
    return self.uglySide.call('ritual_ZNK10QLCDNumber10digitCountEv')

  @overload(float)
  def checkOverflow(self, num: float) -> bool:
    """
    Calls Qt's 'bool QLCDNumber::checkOverflow(double num) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#checkOverflow

    Parameters
    ----------

    num : float
      Passed on as it is.
    """
    #  bool QLCDNumber::checkOverflow(double num) const
    return self.uglySide.call('ritual_ZNK10QLCDNumber13checkOverflowEd', num)

  @overload(int)
  def checkOverflow(self, num: int) -> bool:
    """
    Calls Qt's 'bool QLCDNumber::checkOverflow(int num) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#checkOverflow

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  bool QLCDNumber::checkOverflow(int num) const
    return self.uglySide.call('ritual_ZNK10QLCDNumber13checkOverflowEi', num)

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QLCDNumber::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QLCDNumber::mode() const
    return QLCDNumber.Mode(self.uglySide.call(
        'ritual_ZNK10QLCDNumber4modeEv',
    ))

  def segmentStyle(self) -> SegmentStyle:
    """
    Calls Qt's 'SegmentStyle QLCDNumber::segmentStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#segmentStyle

    Returns
    -------

    SegmentStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SegmentStyle(number)'
      gives.
    """
    #  SegmentStyle QLCDNumber::segmentStyle() const
    return QLCDNumber.SegmentStyle(self.uglySide.call(
        'ritual_ZNK10QLCDNumber12segmentStyleEv',
    ))

  def value(self) -> float:
    """
    Calls Qt's 'double QLCDNumber::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#value
    """
    #  double QLCDNumber::value() const
    return self.uglySide.call('ritual_ZNK10QLCDNumber5valueEv')

  def intValue(self) -> int:
    """
    Calls Qt's 'int QLCDNumber::intValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#intValue
    """
    #  int QLCDNumber::intValue() const
    return self.uglySide.call('ritual_ZNK10QLCDNumber8intValueEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLCDNumber::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLCDNumber::sizeHint() const
    ritual = 'ritual_ZNK10QLCDNumber8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QLCDNumber8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDigitCount(self, nDigits: int) -> None:
    """
    Calls Qt's 'void QLCDNumber::setDigitCount(int nDigits)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setDigitCount

    Parameters
    ----------

    nDigits : int
      Passed on as it is.
    """
    #  void QLCDNumber::setDigitCount(int nDigits)
    self.uglySide.call('ritual_ZN10QLCDNumber13setDigitCountEi', nDigits)

  @overload(Mode)
  def setMode(self, a0: Mode) -> None:
    """
    Calls Qt's 'void QLCDNumber::setMode(Mode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setMode

    Parameters
    ----------

    a0 : Mode
      Passed on as its number.
    """
    #  void QLCDNumber::setMode(Mode a0)
    self.uglySide.call('ritual_ZN10QLCDNumber7setModeENS_4ModeE', a0.value)

  @overload(SegmentStyle)
  def setSegmentStyle(self, a0: SegmentStyle) -> None:
    """
    Calls Qt's 'void QLCDNumber::setSegmentStyle(SegmentStyle a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setSegmentStyle

    Parameters
    ----------

    a0 : SegmentStyle
      Passed on as its number.
    """
    #  void QLCDNumber::setSegmentStyle(SegmentStyle a0)
    self.uglySide.call(
        'ritual_ZN10QLCDNumber15setSegmentStyleENS_12SegmentStyleE',
        a0.value,
    )

  def setHexMode(self) -> None:
    """
    Calls Qt's 'void QLCDNumber::setHexMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setHexMode
    """
    #  void QLCDNumber::setHexMode()
    self.uglySide.call('ritual_ZN10QLCDNumber10setHexModeEv')

  def setDecMode(self) -> None:
    """
    Calls Qt's 'void QLCDNumber::setDecMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setDecMode
    """
    #  void QLCDNumber::setDecMode()
    self.uglySide.call('ritual_ZN10QLCDNumber10setDecModeEv')

  def setOctMode(self) -> None:
    """
    Calls Qt's 'void QLCDNumber::setOctMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setOctMode
    """
    #  void QLCDNumber::setOctMode()
    self.uglySide.call('ritual_ZN10QLCDNumber10setOctModeEv')

  def setBinMode(self) -> None:
    """
    Calls Qt's 'void QLCDNumber::setBinMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#setBinMode
    """
    #  void QLCDNumber::setBinMode()
    self.uglySide.call('ritual_ZN10QLCDNumber10setBinModeEv')

  @overload(bool)
  def setSmallDecimalPoint(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLCDNumber::setSmallDecimalPoint(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlcdnumber.html#setSmallDecimalPoint

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLCDNumber::setSmallDecimalPoint(bool a0)
    self.uglySide.call('ritual_ZN10QLCDNumber20setSmallDecimalPointEb', a0)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QLCDNumber::QLCDNumber(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#QLCDNumber

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLCDNumber::QLCDNumber(QWidget *parent)
    self._noteCreation(QLCDNumber, lambda: Rituals.call(
        'ritual_ZN10QLCDNumberC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(int)
  @overload(int, QWidget)
  @overload(int, NoneType)
  def __init__(
      self,
      numDigits: int,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLCDNumber::QLCDNumber(uint numDigits,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#QLCDNumber

    Parameters
    ----------

    numDigits : int
      Passed on as it is.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLCDNumber::QLCDNumber(uint numDigits, QWidget *parent)
    self._noteCreation(QLCDNumber, lambda: Rituals.call(
        'ritual_ZN10QLCDNumberC1EjP7QWidget',
        numDigits, self._addressOf(parent),
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

  @overload(str)
  def display(self, str: str) -> None:
    """
    Calls Qt's 'void QLCDNumber::display(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#display

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLCDNumber::display(const QString &str)
    self.uglySide.call('ritual_ZN10QLCDNumber7displayERK7QString', str)

  @overload(int)
  def display(self, num: int) -> None:
    """
    Calls Qt's 'void QLCDNumber::display(int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#display

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QLCDNumber::display(int num)
    self.uglySide.call('ritual_ZN10QLCDNumber7displayEi', num)

  @overload(float)
  def display(self, num: float) -> None:
    """
    Calls Qt's 'void QLCDNumber::display(double num)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#display

    Parameters
    ----------

    num : float
      Passed on as it is.
    """
    #  void QLCDNumber::display(double num)
    self.uglySide.call('ritual_ZN10QLCDNumber7displayEd', num)

  def overflow(self) -> None:
    """
    Calls Qt's 'void QLCDNumber::overflow()'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#overflow
    """
    #  void QLCDNumber::overflow()
    self.uglySide.call('ritual_ZN10QLCDNumber8overflowEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QLCDNumber::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLCDNumber::event(QEvent *e)
    ritual = 'ritual_ZN10QLCDNumber5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QLCDNumber5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QLCDNumber::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlcdnumber.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLCDNumber::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN10QLCDNumber10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QLCDNumber10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))
