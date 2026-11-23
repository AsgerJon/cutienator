"""
QFontMetricsF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qfontmetrics.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar, QRectF
  from . import QFont, QFontMetrics, QPaintDevice, QTextOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QFont = WAIT['QFont']
  QFontMetrics = WAIT['QFontMetrics']
  QPaintDevice = WAIT['QPaintDevice']
  QTextOption = WAIT['QTextOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontMetricsF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontMetricsF: a plain Python object standing in
  front of one C++ QFontMetricsF.

  C++ hands a QFontMetricsF around as a copy, so every C++ QFontMetricsF
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontMetricsF that has a ritual and that Python can
  call so far, 26 names in all: 'ascent', 'capHeight', 'descent', 'height',
  'leading', 'lineSpacing', 'minLeftBearing', 'minRightBearing', 'maxWidth',
  'xHeight', 'averageCharWidth', 'inFont', 'inFontUcs4', 'leftBearing',
  'rightBearing', 'horizontalAdvance', 'boundingRect', 'tightBoundingRect',
  'elidedText', 'underlinePos', 'overlinePos', 'strikeOutPos', 'lineWidth',
  'fontDpi', '__eq__', '__ne__'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontMetricsF::~QFontMetricsF()': the destructor: Python removes
    its C++ QFontMetricsF by it, and has no other use for it.
  - Qt's 'QRectF QFontMetricsF::boundingRect(const QRectF &r, int flags,
    const QString &string, int tabstops, int *tabarray) const': takes a
    number to change where it is.
  - Qt's 'QSizeF QFontMetricsF::size(int flags, const QString &str, int
    tabstops, int *tabarray) const': takes a number to change where it is.

  What has no ritual
  ------------------

  5 of the 43 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QFontMetricsF is created at the first use, not by
    'QFontMetricsF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontMetricsF back gives a copy the ritual made for
    Python, in a new cute QFontMetricsF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontMetricsF'

  #  Qt's '~QFontMetricsF()'. Naming it makes this a value class: Python owns
  #  every C++ QFontMetricsF behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QFontMetricsFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#ascent
    """
    #  qreal QFontMetricsF::ascent() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF6ascentEv')

  def capHeight(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#capHeight
    """
    #  qreal QFontMetricsF::capHeight() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF9capHeightEv')

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#descent
    """
    #  qreal QFontMetricsF::descent() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF7descentEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#height
    """
    #  qreal QFontMetricsF::height() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF6heightEv')

  def leading(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#leading
    """
    #  qreal QFontMetricsF::leading() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF7leadingEv')

  def lineSpacing(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::lineSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#lineSpacing
    """
    #  qreal QFontMetricsF::lineSpacing() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF11lineSpacingEv')

  def minLeftBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::minLeftBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#minLeftBearing
    """
    #  qreal QFontMetricsF::minLeftBearing() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF14minLeftBearingEv')

  def minRightBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::minRightBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#minRightBearing
    """
    #  qreal QFontMetricsF::minRightBearing() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF15minRightBearingEv')

  def maxWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::maxWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#maxWidth
    """
    #  qreal QFontMetricsF::maxWidth() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF8maxWidthEv')

  def xHeight(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#xHeight
    """
    #  qreal QFontMetricsF::xHeight() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF7xHeightEv')

  def averageCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::averageCharWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#averageCharWidth
    """
    #  qreal QFontMetricsF::averageCharWidth() const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF16averageCharWidthEv',
    )

  @overload(QChar)
  def inFont(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool QFontMetricsF::inFont(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#inFont

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QFontMetricsF::inFont(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF6inFontE5QChar', self._valueOf(a0),
    )

  @overload(int)
  def inFontUcs4(self, ucs4: int) -> bool:
    """
    Calls Qt's 'bool QFontMetricsF::inFontUcs4(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#inFontUcs4

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  bool QFontMetricsF::inFontUcs4(uint ucs4) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF10inFontUcs4Ej', ucs4,
    )

  @overload(QChar)
  def leftBearing(self, a0: QChar) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::leftBearing(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#leftBearing

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  qreal QFontMetricsF::leftBearing(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF11leftBearingE5QChar', self._valueOf(a0),
    )

  @overload(QChar)
  def rightBearing(self, a0: QChar) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::rightBearing(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#rightBearing

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  qreal QFontMetricsF::rightBearing(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF12rightBearingE5QChar', self._valueOf(a0),
    )

  @overload(str)
  @overload(str, int)
  def horizontalAdvance(self, string: str, length: int = -1) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::horizontalAdvance(const QString &string,
    int length) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#horizontalAdvance

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  qreal QFontMetricsF::horizontalAdvance(const QString &string, int
    #      length) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF17horizontalAdvanceERK7QStringi',
        string, length,
    )

  @overload(QChar)
  def horizontalAdvance(self, a0: QChar) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::horizontalAdvance(QChar a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#horizontalAdvance

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  qreal QFontMetricsF::horizontalAdvance(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF17horizontalAdvanceE5QChar',
        self._valueOf(a0),
    )

  @overload(str, QTextOption)
  def horizontalAdvance(self, string: str, textOption: QTextOption) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::horizontalAdvance(const QString &string,
    const QTextOption &textOption) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#horizontalAdvance

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  qreal QFontMetricsF::horizontalAdvance(const QString &string, const
    #      QTextOption &textOption) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF17horizontalAdvanceERK7QStringRK11QTextOp'
        'tion',
        string, self._valueOf(textOption),
    )

  @overload(str)
  def boundingRect(self, string: str) -> QRectF:
    """
    Calls Qt's 'QRectF QFontMetricsF::boundingRect(const QString &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#boundingRect

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QFontMetricsF::boundingRect(const QString &string) const
    address = self.uglySide.call(
        'ritual_ZNK13QFontMetricsF12boundingRectERK7QString', string,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, QTextOption)
  def boundingRect(self, text: str, textOption: QTextOption) -> QRectF:
    """
    Calls Qt's 'QRectF QFontMetricsF::boundingRect(const QString &text, const
    QTextOption &textOption) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#boundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QFontMetricsF::boundingRect(const QString &text, const
    #      QTextOption &textOption) const
    address = self.uglySide.call(
        'ritual_ZNK13QFontMetricsF12boundingRectERK7QStringRK11QTextOption',
        text, self._valueOf(textOption),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QChar)
  def boundingRect(self, a0: QChar) -> QRectF:
    """
    Calls Qt's 'QRectF QFontMetricsF::boundingRect(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#boundingRect

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QFontMetricsF::boundingRect(QChar a0) const
    address = self.uglySide.call(
        'ritual_ZNK13QFontMetricsF12boundingRectE5QChar', self._valueOf(a0),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str)
  def tightBoundingRect(self, text: str) -> QRectF:
    """
    Calls Qt's 'QRectF QFontMetricsF::tightBoundingRect(const QString &text)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#tightBoundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QFontMetricsF::tightBoundingRect(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK13QFontMetricsF17tightBoundingRectERK7QString', text,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, QTextOption)
  def tightBoundingRect(self, text: str, textOption: QTextOption) -> QRectF:
    """
    Calls Qt's 'QRectF QFontMetricsF::tightBoundingRect(const QString &text,
    const QTextOption &textOption) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetricsf.html#tightBoundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QFontMetricsF::tightBoundingRect(const QString &text, const
    #      QTextOption &textOption) const
    address = self.uglySide.call(
        'ritual_ZNK13QFontMetricsF17tightBoundingRectERK7QStringRK11QTextOp'
        'tion',
        text, self._valueOf(textOption),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str, Qt.TextElideMode, float)
  @overload(str, Qt.TextElideMode, float, int)
  def elidedText(
      self,
      text: str,
      mode: Qt.TextElideMode,
      width: float,
      flags: int = 0,
  ) -> str:
    """
    Calls Qt's 'QString QFontMetricsF::elidedText(const QString &text,
    Qt::TextElideMode mode, qreal width, int flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#elidedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    mode : Qt.TextElideMode
      Passed on as its number.

    width : float
      Passed on as it is.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontMetricsF::elidedText(const QString &text,
    #      Qt::TextElideMode mode, qreal width, int flags) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsF10elidedTextERK7QStringN2Qt13TextElideMod'
        'eEdi',
        text, mode.value, width, flags,
    )

  def underlinePos(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::underlinePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#underlinePos
    """
    #  qreal QFontMetricsF::underlinePos() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF12underlinePosEv')

  def overlinePos(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::overlinePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#overlinePos
    """
    #  qreal QFontMetricsF::overlinePos() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF11overlinePosEv')

  def strikeOutPos(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::strikeOutPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#strikeOutPos
    """
    #  qreal QFontMetricsF::strikeOutPos() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF12strikeOutPosEv')

  def lineWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#lineWidth
    """
    #  qreal QFontMetricsF::lineWidth() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF9lineWidthEv')

  def fontDpi(self) -> float:
    """
    Calls Qt's 'qreal QFontMetricsF::fontDpi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#fontDpi
    """
    #  qreal QFontMetricsF::fontDpi() const
    return self.uglySide.call('ritual_ZNK13QFontMetricsF7fontDpiEv')

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
  def __eq__(self, other: QFontMetricsF) -> bool:
    """
    Calls Qt's 'bool QFontMetricsF::operator==(const QFontMetricsF &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#operator==

    Parameters
    ----------

    other : QFontMetricsF
      Passed on as a value: Qt reads the C++ QFontMetricsF, which stays
      Python's own.
    """
    #  bool QFontMetricsF::operator==(const QFontMetricsF &other) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsFeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QFontMetricsF) -> bool:
    """
    Calls Qt's 'bool QFontMetricsF::operator!=(const QFontMetricsF &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#operator!=

    Parameters
    ----------

    other : QFontMetricsF
      Passed on as a value: Qt reads the C++ QFontMetricsF, which stays
      Python's own.
    """
    #  bool QFontMetricsF::operator!=(const QFontMetricsF &other) const
    return self.uglySide.call(
        'ritual_ZNK13QFontMetricsFneERKS_', self._valueOf(other),
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

  @overload(QFont)
  def __init__(self, font: QFont) -> None:
    """
    Notes what was given, for Qt's 'QFontMetricsF::QFontMetricsF(const QFont
    &font)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#QFontMetricsF

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QFontMetricsF::QFontMetricsF(const QFont &font)
    self._noteCreation(QFontMetricsF, lambda: Rituals.call(
        'ritual_ZN13QFontMetricsFC1ERK5QFont', self._valueOf(font),
    ))

  @overload(QFont, QPaintDevice)
  @overload(QFont, NoneType)
  def __init__(self, font: QFont, pd: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's 'QFontMetricsF::QFontMetricsF(const QFont
    &font, const QPaintDevice *pd)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#QFontMetricsF

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    pd : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFontMetricsF::QFontMetricsF(const QFont &font, const QPaintDevice
    #      *pd)
    self._noteCreation(QFontMetricsF, lambda: Rituals.call(
        'ritual_ZN13QFontMetricsFC1ERK5QFontPK12QPaintDevice',
        self._valueOf(font), self._addressOf(pd, 'QPaintDevice'),
    ))

  @overload(QFontMetrics)
  def __init__(self, a0: QFontMetrics) -> None:
    """
    Notes what was given, for Qt's 'QFontMetricsF::QFontMetricsF(const
    QFontMetrics &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#QFontMetricsF

    Parameters
    ----------

    a0 : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.
    """
    #  QFontMetricsF::QFontMetricsF(const QFontMetrics &a0)
    self._noteCreation(QFontMetricsF, lambda: Rituals.call(
        'ritual_ZN13QFontMetricsFC1ERK12QFontMetrics', self._valueOf(a0),
    ))

  @overload(THIS)
  def __init__(self, a0: QFontMetricsF) -> None:
    """
    Notes what was given, for Qt's 'QFontMetricsF::QFontMetricsF(const
    QFontMetricsF &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetricsf.html#QFontMetricsF

    Parameters
    ----------

    a0 : QFontMetricsF
      Passed on as a value: Qt reads the C++ QFontMetricsF, which stays
      Python's own.
    """
    #  QFontMetricsF::QFontMetricsF(const QFontMetricsF &a0)
    self._noteCreation(QFontMetricsF, lambda: Rituals.call(
        'ritual_ZN13QFontMetricsFC1ERKS_', self._valueOf(a0),
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
