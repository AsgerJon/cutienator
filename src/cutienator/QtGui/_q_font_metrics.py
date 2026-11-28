"""
QFontMetrics binding of the Qt C++
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
  from typing import Never, Optional

  from ..QtCore import QChar, QRect
  from . import QFont, QPaintDevice, QTextOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QFont = WAIT['QFont']
  QPaintDevice = WAIT['QPaintDevice']
  QTextOption = WAIT['QTextOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontMetrics(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontMetrics: a plain Python object standing in front
  of one C++ QFontMetrics.

  C++ hands a QFontMetrics around as a copy, so every C++ QFontMetrics behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontMetrics that has a ritual and that Python can
  call so far, 26 names in all: 'ascent', 'capHeight', 'descent', 'height',
  'leading', 'lineSpacing', 'minLeftBearing', 'minRightBearing', 'maxWidth',
  'xHeight', 'averageCharWidth', 'inFont', 'inFontUcs4', 'leftBearing',
  'rightBearing', 'horizontalAdvance', 'boundingRect', 'tightBoundingRect',
  'elidedText', 'underlinePos', 'overlinePos', 'strikeOutPos', 'lineWidth',
  'fontDpi', '__eq__', '__ne__'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontMetrics::QFontMetrics(QFontMetrics &&a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QFontMetrics::~QFontMetrics()': the destructor: Python removes its
    C++ QFontMetrics by it, and has no other use for it.
  - Qt's 'QFontMetrics &QFontMetrics::operator=(const QFontMetrics &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QFontMetrics &QFontMetrics::operator=(QFontMetrics &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QFontMetrics::swap(QFontMetrics &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QRect QFontMetrics::boundingRect(const QRect &r, int flags, const
    QString &text, int tabstops, int *tabarray) const': takes a number to
    change where it is.
  - Qt's 'QRect QFontMetrics::boundingRect(int x, int y, int w, int h, int
    flags, const QString &text, int tabstops, int *tabarray) const': takes a
    number to change where it is.
  - Qt's 'QSize QFontMetrics::size(int flags, const QString &str, int
    tabstops, int *tabarray) const': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QFontMetrics is created at the first use, not by
    'QFontMetrics(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontMetrics back gives a copy the ritual made for
    Python, in a new cute QFontMetrics.
  - Each name of Qt's QFontMetrics that has no cute function yet, 'size',
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QFontMetrics'

  #  Qt's '~QFontMetrics()'. Naming it makes this a value class: Python owns
  #  every C++ QFontMetrics behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QFontMetricsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def ascent(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#ascent
    """
    #  int QFontMetrics::ascent() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics6ascentEv')

  def capHeight(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#capHeight
    """
    #  int QFontMetrics::capHeight() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics9capHeightEv')

  def descent(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#descent
    """
    #  int QFontMetrics::descent() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics7descentEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#height
    """
    #  int QFontMetrics::height() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics6heightEv')

  def leading(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#leading
    """
    #  int QFontMetrics::leading() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics7leadingEv')

  def lineSpacing(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::lineSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#lineSpacing
    """
    #  int QFontMetrics::lineSpacing() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics11lineSpacingEv')

  def minLeftBearing(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::minLeftBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#minLeftBearing
    """
    #  int QFontMetrics::minLeftBearing() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics14minLeftBearingEv')

  def minRightBearing(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::minRightBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#minRightBearing
    """
    #  int QFontMetrics::minRightBearing() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics15minRightBearingEv')

  def maxWidth(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::maxWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#maxWidth
    """
    #  int QFontMetrics::maxWidth() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics8maxWidthEv')

  def xHeight(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#xHeight
    """
    #  int QFontMetrics::xHeight() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics7xHeightEv')

  def averageCharWidth(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::averageCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#averageCharWidth
    """
    #  int QFontMetrics::averageCharWidth() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics16averageCharWidthEv')

  @overload(QChar)
  def inFont(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool QFontMetrics::inFont(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#inFont

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QFontMetrics::inFont(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics6inFontE5QChar', self._valueOf(a0),
    )

  @overload(int)
  def inFontUcs4(self, ucs4: int) -> bool:
    """
    Calls Qt's 'bool QFontMetrics::inFontUcs4(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#inFontUcs4

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  bool QFontMetrics::inFontUcs4(uint ucs4) const
    return self.uglySide.call('ritual_ZNK12QFontMetrics10inFontUcs4Ej', ucs4)

  @overload(QChar)
  def leftBearing(self, a0: QChar) -> int:
    """
    Calls Qt's 'int QFontMetrics::leftBearing(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#leftBearing

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  int QFontMetrics::leftBearing(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics11leftBearingE5QChar', self._valueOf(a0),
    )

  @overload(QChar)
  def rightBearing(self, a0: QChar) -> int:
    """
    Calls Qt's 'int QFontMetrics::rightBearing(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#rightBearing

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  int QFontMetrics::rightBearing(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics12rightBearingE5QChar', self._valueOf(a0),
    )

  @overload(str)
  @overload(str, int)
  def horizontalAdvance(self, a0: str, len: int = -1) -> int:
    """
    Calls Qt's 'int QFontMetrics::horizontalAdvance(const QString &a0, int
    len) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetrics.html#horizontalAdvance

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    len : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QFontMetrics::horizontalAdvance(const QString &a0, int len) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics17horizontalAdvanceERK7QStringi', a0, len,
    )

  @overload(str, QTextOption)
  def horizontalAdvance(self, a0: str, textOption: QTextOption) -> int:
    """
    Calls Qt's 'int QFontMetrics::horizontalAdvance(const QString &a0, const
    QTextOption &textOption) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetrics.html#horizontalAdvance

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  int QFontMetrics::horizontalAdvance(const QString &a0, const
    #      QTextOption &textOption) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics17horizontalAdvanceERK7QStringRK11QTextOpt'
        'ion',
        a0, self._valueOf(textOption),
    )

  @overload(QChar)
  def horizontalAdvance(self, a0: QChar) -> int:
    """
    Calls Qt's 'int QFontMetrics::horizontalAdvance(QChar a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetrics.html#horizontalAdvance

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  int QFontMetrics::horizontalAdvance(QChar a0) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics17horizontalAdvanceE5QChar',
        self._valueOf(a0),
    )

  @overload(QChar)
  def boundingRect(self, a0: QChar) -> QRect:
    """
    Calls Qt's 'QRect QFontMetrics::boundingRect(QChar a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFontMetrics::boundingRect(QChar a0) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontMetrics12boundingRectE5QChar', self._valueOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(str)
  def boundingRect(self, text: str) -> QRect:
    """
    Calls Qt's 'QRect QFontMetrics::boundingRect(const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFontMetrics::boundingRect(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontMetrics12boundingRectERK7QString', text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(str, QTextOption)
  def boundingRect(self, text: str, textOption: QTextOption) -> QRect:
    """
    Calls Qt's 'QRect QFontMetrics::boundingRect(const QString &text, const
    QTextOption &textOption) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#boundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFontMetrics::boundingRect(const QString &text, const
    #      QTextOption &textOption) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontMetrics12boundingRectERK7QStringRK11QTextOption',
        text, self._valueOf(textOption),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(str)
  def tightBoundingRect(self, text: str) -> QRect:
    """
    Calls Qt's 'QRect QFontMetrics::tightBoundingRect(const QString &text)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetrics.html#tightBoundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFontMetrics::tightBoundingRect(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontMetrics17tightBoundingRectERK7QString', text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(str, QTextOption)
  def tightBoundingRect(self, text: str, textOption: QTextOption) -> QRect:
    """
    Calls Qt's 'QRect QFontMetrics::tightBoundingRect(const QString &text,
    const QTextOption &textOption) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontmetrics.html#tightBoundingRect

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    textOption : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFontMetrics::tightBoundingRect(const QString &text, const
    #      QTextOption &textOption) const
    address = self.uglySide.call(
        'ritual_ZNK12QFontMetrics17tightBoundingRectERK7QStringRK11QTextOpt'
        'ion',
        text, self._valueOf(textOption),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(str, Qt.TextElideMode, int)
  @overload(str, Qt.TextElideMode, int, int)
  def elidedText(
      self,
      text: str,
      mode: Qt.TextElideMode,
      width: int,
      flags: int = 0,
  ) -> str:
    """
    Calls Qt's 'QString QFontMetrics::elidedText(const QString &text,
    Qt::TextElideMode mode, int width, int flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#elidedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    mode : Qt.TextElideMode
      Passed on as its number.

    width : int
      Passed on as it is.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontMetrics::elidedText(const QString &text,
    #      Qt::TextElideMode mode, int width, int flags) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetrics10elidedTextERK7QStringN2Qt13TextElideMode'
        'Eii',
        text, mode.value, width, flags,
    )

  def underlinePos(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::underlinePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#underlinePos
    """
    #  int QFontMetrics::underlinePos() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics12underlinePosEv')

  def overlinePos(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::overlinePos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#overlinePos
    """
    #  int QFontMetrics::overlinePos() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics11overlinePosEv')

  def strikeOutPos(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::strikeOutPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#strikeOutPos
    """
    #  int QFontMetrics::strikeOutPos() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics12strikeOutPosEv')

  def lineWidth(self) -> int:
    """
    Calls Qt's 'int QFontMetrics::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#lineWidth
    """
    #  int QFontMetrics::lineWidth() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics9lineWidthEv')

  def fontDpi(self) -> float:
    """
    Calls Qt's 'qreal QFontMetrics::fontDpi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#fontDpi
    """
    #  qreal QFontMetrics::fontDpi() const
    return self.uglySide.call('ritual_ZNK12QFontMetrics7fontDpiEv')

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
  def __eq__(self, other: QFontMetrics) -> bool:
    """
    Calls Qt's 'bool QFontMetrics::operator==(const QFontMetrics &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#operator==

    Parameters
    ----------

    other : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.
    """
    #  bool QFontMetrics::operator==(const QFontMetrics &other) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetricseqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QFontMetrics) -> bool:
    """
    Calls Qt's 'bool QFontMetrics::operator!=(const QFontMetrics &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#operator!=

    Parameters
    ----------

    other : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.
    """
    #  bool QFontMetrics::operator!=(const QFontMetrics &other) const
    return self.uglySide.call(
        'ritual_ZNK12QFontMetricsneERKS_', self._valueOf(other),
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
  def __init__(self, a0: QFont) -> None:
    """
    Notes what was given, for Qt's 'QFontMetrics::QFontMetrics(const QFont
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QFontMetrics::QFontMetrics(const QFont &a0)
    self._noteCreation(QFontMetrics, lambda: Rituals.call(
        'ritual_ZN12QFontMetricsC1ERK5QFont', self._valueOf(a0),
    ))

  @overload(QFont, QPaintDevice)
  @overload(QFont, NoneType)
  def __init__(self, font: QFont, pd: Optional[QPaintDevice]) -> None:
    """
    Notes what was given, for Qt's 'QFontMetrics::QFontMetrics(const QFont
    &font, const QPaintDevice *pd)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    pd : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QFontMetrics::QFontMetrics(const QFont &font, const QPaintDevice *pd)
    self._noteCreation(QFontMetrics, lambda: Rituals.call(
        'ritual_ZN12QFontMetricsC1ERK5QFontPK12QPaintDevice',
        self._valueOf(font), self._addressOf(pd, 'QPaintDevice'),
    ))

  @overload(THIS)
  def __init__(self, a0: QFontMetrics) -> None:
    """
    Notes what was given, for Qt's 'QFontMetrics::QFontMetrics(const
    QFontMetrics &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontmetrics.html#QFontMetrics

    Parameters
    ----------

    a0 : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.
    """
    #  QFontMetrics::QFontMetrics(const QFontMetrics &a0)
    self._noteCreation(QFontMetrics, lambda: Rituals.call(
        'ritual_ZN12QFontMetricsC1ERKS_', self._valueOf(a0),
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
  def size(*__, **_) -> Never:
    """
    Qt's 'QSize QFontMetrics::size(int flags, const QString &str, int
    tabstops, int *tabarray) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QFontMetrics.size' has no cute function yet. Qt's 'QSize "
        "QFontMetrics::size(int flags, const QString &str, int tabstops, "
        "int *tabarray) const': takes a number to change where it is.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QFontMetrics::swap(QFontMetrics &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFontMetrics.swap' has no cute function yet. Qt's 'void "
        "QFontMetrics::swap(QFontMetrics &other)': takes a type Python has "
        "no way to hand over yet.")
