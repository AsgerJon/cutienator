"""
QProgressBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qprogressbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QMetaObject
from ..QtCore import QSize
from ._q_widget import QWidget
from ._q_progress_bar_direction import Direction

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProgressBar(QWidget):
  """
  The cute side of Qt's QProgressBar: a plain Python object standing in front
  of one C++ QProgressBar.

  It is built on the cute 'QWidget', as Qt's QProgressBar is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProgressBar that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'minimum', 'maximum',
  'value', 'text', 'setTextVisible', 'isTextVisible', 'alignment',
  'setAlignment', 'sizeHint', 'minimumSizeHint', 'orientation',
  'setInvertedAppearance', 'invertedAppearance', 'setTextDirection',
  'textDirection', 'setFormat', 'resetFormat', 'format', 'reset', 'setRange',
  'setMinimum', 'setMaximum', 'setValue', 'setOrientation'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProgressBar::~QProgressBar()': the destructor: Python never
    removes a C++ QProgressBar.

  What has no ritual
  ------------------

  12 of the 40 functions Qt declares: 3 private; 3 protected; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QProgressBar is created at the first use, not by
    'QProgressBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProgressBar.
  - Qt tells when it has removed the C++ QProgressBar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QProgressBar, and the names Qt has for the
  #  combinations of its flags enums.
  Direction = Direction

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
    Calls Qt's 'QString QProgressBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#tr

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
    #  QString QProgressBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QProgressBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProgressBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QProgressBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QProgressBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QProgressBar10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def minimum(self) -> int:
    """
    Calls Qt's 'int QProgressBar::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#minimum
    """
    #  int QProgressBar::minimum() const
    return self.uglySide.call('ritual_ZNK12QProgressBar7minimumEv')

  def maximum(self) -> int:
    """
    Calls Qt's 'int QProgressBar::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#maximum
    """
    #  int QProgressBar::maximum() const
    return self.uglySide.call('ritual_ZNK12QProgressBar7maximumEv')

  def value(self) -> int:
    """
    Calls Qt's 'int QProgressBar::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#value
    """
    #  int QProgressBar::value() const
    return self.uglySide.call('ritual_ZNK12QProgressBar5valueEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QProgressBar::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProgressBar::text() const
    return self.uglySide.call('ritual_ZNK12QProgressBar4textEv')

  def isTextVisible(self) -> bool:
    """
    Calls Qt's 'bool QProgressBar::isTextVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#isTextVisible
    """
    #  bool QProgressBar::isTextVisible() const
    return self.uglySide.call('ritual_ZNK12QProgressBar13isTextVisibleEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QProgressBar::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QProgressBar::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK12QProgressBar9alignmentEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QProgressBar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QProgressBar::sizeHint() const
    address = self.uglySide.call('ritual_ZNK12QProgressBar8sizeHintEv')
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QProgressBar::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QProgressBar::minimumSizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK12QProgressBar15minimumSizeHintEv',
    )
    return QSize._cuteOwning(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QProgressBar::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QProgressBar::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK12QProgressBar11orientationEv',
    ))

  def invertedAppearance(self) -> bool:
    """
    Calls Qt's 'bool QProgressBar::invertedAppearance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressbar.html#invertedAppearance
    """
    #  bool QProgressBar::invertedAppearance() const
    return self.uglySide.call(
        'ritual_ZNK12QProgressBar18invertedAppearanceEv',
    )

  def textDirection(self) -> Direction:
    """
    Calls Qt's 'QProgressBar::Direction QProgressBar::textDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#textDirection

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  QProgressBar::Direction QProgressBar::textDirection() const
    return Direction(self.uglySide.call(
        'ritual_ZNK12QProgressBar13textDirectionEv',
    ))

  def format(self) -> str:
    """
    Calls Qt's 'QString QProgressBar::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#format

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProgressBar::format() const
    return self.uglySide.call('ritual_ZNK12QProgressBar6formatEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTextVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QProgressBar::setTextVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setTextVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QProgressBar::setTextVisible(bool visible)
    self.uglySide.call('ritual_ZN12QProgressBar14setTextVisibleEb', visible)

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QProgressBar::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QProgressBar::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN12QProgressBar12setAlignmentE6QFlagsIN2Qt13AlignmentFlagE'
        'E',
        alignment.value,
    )

  @overload(bool)
  def setInvertedAppearance(self, invert: bool) -> None:
    """
    Calls Qt's 'void QProgressBar::setInvertedAppearance(bool invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressbar.html#setInvertedAppearance

    Parameters
    ----------

    invert : bool
      Passed on as it is.
    """
    #  void QProgressBar::setInvertedAppearance(bool invert)
    self.uglySide.call(
        'ritual_ZN12QProgressBar21setInvertedAppearanceEb', invert,
    )

  @overload(Direction)
  def setTextDirection(self, textDirection: Direction) -> None:
    """
    Calls Qt's 'void QProgressBar::setTextDirection(QProgressBar::Direction
    textDirection)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setTextDirection

    Parameters
    ----------

    textDirection : Direction
      Passed on as its number.
    """
    #  void QProgressBar::setTextDirection(QProgressBar::Direction
    #      textDirection)
    self.uglySide.call(
        'ritual_ZN12QProgressBar16setTextDirectionENS_9DirectionE',
        textDirection.value,
    )

  @overload(str)
  def setFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QProgressBar::setFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProgressBar::setFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN12QProgressBar9setFormatERK7QString', format,
    )

  @overload(int, int)
  def setRange(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QProgressBar::setRange(int minimum, int maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setRange

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QProgressBar::setRange(int minimum, int maximum)
    self.uglySide.call(
        'ritual_ZN12QProgressBar8setRangeEii', minimum, maximum,
    )

  @overload(int)
  def setMinimum(self, minimum: int) -> None:
    """
    Calls Qt's 'void QProgressBar::setMinimum(int minimum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setMinimum

    Parameters
    ----------

    minimum : int
      Passed on as it is.
    """
    #  void QProgressBar::setMinimum(int minimum)
    self.uglySide.call('ritual_ZN12QProgressBar10setMinimumEi', minimum)

  @overload(int)
  def setMaximum(self, maximum: int) -> None:
    """
    Calls Qt's 'void QProgressBar::setMaximum(int maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setMaximum

    Parameters
    ----------

    maximum : int
      Passed on as it is.
    """
    #  void QProgressBar::setMaximum(int maximum)
    self.uglySide.call('ritual_ZN12QProgressBar10setMaximumEi', maximum)

  @overload(int)
  def setValue(self, value: int) -> None:
    """
    Calls Qt's 'void QProgressBar::setValue(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QProgressBar::setValue(int value)
    self.uglySide.call('ritual_ZN12QProgressBar8setValueEi', value)

  @overload(Qt.Orientation)
  def setOrientation(self, a0: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QProgressBar::setOrientation(Qt::Orientation a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#setOrientation

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.
    """
    #  void QProgressBar::setOrientation(Qt::Orientation a0)
    self.uglySide.call(
        'ritual_ZN12QProgressBar14setOrientationEN2Qt11OrientationE',
        a0.value,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QProgressBar::QProgressBar(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#QProgressBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QProgressBar::QProgressBar(QWidget *parent)
    self._noteCreation(QProgressBar, lambda: Rituals.call(
        'ritual_ZN12QProgressBarC1EP7QWidget', self._addressOf(parent),
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

  def resetFormat(self) -> None:
    """
    Calls Qt's 'void QProgressBar::resetFormat()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#resetFormat
    """
    #  void QProgressBar::resetFormat()
    self.uglySide.call('ritual_ZN12QProgressBar11resetFormatEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QProgressBar::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressbar.html#reset
    """
    #  void QProgressBar::reset()
    self.uglySide.call('ritual_ZN12QProgressBar5resetEv')
