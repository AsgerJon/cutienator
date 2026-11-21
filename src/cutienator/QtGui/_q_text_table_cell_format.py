"""
QTextTableCellFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QTextCharFormat, QTextFrameFormatBorderStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QBrush, QTextFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class QTextTableCellFormat(QTextCharFormat):
  """
  The cute side of Qt's QTextTableCellFormat: a plain Python object standing
  in front of one C++ QTextTableCellFormat.

  It is built on the cute 'QTextCharFormat', as Qt's QTextTableCellFormat is
  built on Qt's QTextCharFormat, and has everything that class has.

  C++ hands a QTextTableCellFormat around as a copy, so every C++
  QTextTableCellFormat behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextTableCellFormat that has a ritual and that
  Python can call so far, 37 names in all: 'isValid', 'setTopPadding',
  'topPadding', 'setBottomPadding', 'bottomPadding', 'setLeftPadding',
  'leftPadding', 'setRightPadding', 'rightPadding', 'setPadding',
  'setTopBorder', 'topBorder', 'setBottomBorder', 'bottomBorder',
  'setLeftBorder', 'leftBorder', 'setRightBorder', 'rightBorder',
  'setBorder', 'setTopBorderStyle', 'topBorderStyle', 'setBottomBorderStyle',
  'bottomBorderStyle', 'setLeftBorderStyle', 'leftBorderStyle',
  'setRightBorderStyle', 'rightBorderStyle', 'setBorderStyle',
  'setTopBorderBrush', 'topBorderBrush', 'setBottomBorderBrush',
  'bottomBorderBrush', 'setLeftBorderBrush', 'leftBorderBrush',
  'setRightBorderBrush', 'rightBorderBrush', 'setBorderBrush'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextTableCellFormat::~QTextTableCellFormat()': the destructor:
    Python removes its C++ QTextTableCellFormat by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 40 functions Qt declares: 1 protected.

  What to expect
  --------------

  - The C++ QTextTableCellFormat is created at the first use, not by
    'QTextTableCellFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextTableCellFormat back gives a copy the ritual
    made for Python, in a new cute QTextTableCellFormat.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextTableCellFormat'

  #  Qt's '~QTextTableCellFormat()'. Naming it makes this a value class:
  #  Python owns every C++ QTextTableCellFormat behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QTextTableCellFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextTableCellFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttablecellformat.html#isValid
    """
    #  bool QTextTableCellFormat::isValid() const
    return self.uglySide.call('ritual_ZNK20QTextTableCellFormat7isValidEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::topPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#topPadding
    """
    #  qreal QTextTableCellFormat::topPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat10topPaddingEv',
    )

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::bottomPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#bottomPadding
    """
    #  qreal QTextTableCellFormat::bottomPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat13bottomPaddingEv',
    )

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::leftPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#leftPadding
    """
    #  qreal QTextTableCellFormat::leftPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat11leftPaddingEv',
    )

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::rightPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#rightPadding
    """
    #  qreal QTextTableCellFormat::rightPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat12rightPaddingEv',
    )

  def topBorder(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::topBorder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#topBorder
    """
    #  qreal QTextTableCellFormat::topBorder() const
    return self.uglySide.call('ritual_ZNK20QTextTableCellFormat9topBorderEv')

  def bottomBorder(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::bottomBorder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#bottomBorder
    """
    #  qreal QTextTableCellFormat::bottomBorder() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat12bottomBorderEv',
    )

  def leftBorder(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::leftBorder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#leftBorder
    """
    #  qreal QTextTableCellFormat::leftBorder() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat10leftBorderEv',
    )

  def rightBorder(self) -> float:
    """
    Calls Qt's 'qreal QTextTableCellFormat::rightBorder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#rightBorder
    """
    #  qreal QTextTableCellFormat::rightBorder() const
    return self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat11rightBorderEv',
    )

  def topBorderStyle(self) -> QTextFrameFormat.BorderStyle:
    """
    Calls Qt's 'QTextFrameFormat::BorderStyle
    QTextTableCellFormat::topBorderStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#topBorderStyle

    Returns
    -------

    QTextFrameFormat.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextFrameFormat.BorderStyle(number)' gives.
    """
    #  QTextFrameFormat::BorderStyle QTextTableCellFormat::topBorderStyle()
    #      const
    return QTextFrameFormatBorderStyle(self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat14topBorderStyleEv',
    ))

  def bottomBorderStyle(self) -> QTextFrameFormat.BorderStyle:
    """
    Calls Qt's 'QTextFrameFormat::BorderStyle
    QTextTableCellFormat::bottomBorderStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#bottomBorderStyle

    Returns
    -------

    QTextFrameFormat.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextFrameFormat.BorderStyle(number)' gives.
    """
    #  QTextFrameFormat::BorderStyle
    #      QTextTableCellFormat::bottomBorderStyle() const
    return QTextFrameFormatBorderStyle(self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat17bottomBorderStyleEv',
    ))

  def leftBorderStyle(self) -> QTextFrameFormat.BorderStyle:
    """
    Calls Qt's 'QTextFrameFormat::BorderStyle
    QTextTableCellFormat::leftBorderStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#leftBorderStyle

    Returns
    -------

    QTextFrameFormat.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextFrameFormat.BorderStyle(number)' gives.
    """
    #  QTextFrameFormat::BorderStyle QTextTableCellFormat::leftBorderStyle()
    #      const
    return QTextFrameFormatBorderStyle(self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat15leftBorderStyleEv',
    ))

  def rightBorderStyle(self) -> QTextFrameFormat.BorderStyle:
    """
    Calls Qt's 'QTextFrameFormat::BorderStyle
    QTextTableCellFormat::rightBorderStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#rightBorderStyle

    Returns
    -------

    QTextFrameFormat.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextFrameFormat.BorderStyle(number)' gives.
    """
    #  QTextFrameFormat::BorderStyle QTextTableCellFormat::rightBorderStyle()
    #      const
    return QTextFrameFormatBorderStyle(self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat16rightBorderStyleEv',
    ))

  def topBorderBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextTableCellFormat::topBorderBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#topBorderBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextTableCellFormat::topBorderBrush() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat14topBorderBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def bottomBorderBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextTableCellFormat::bottomBorderBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#bottomBorderBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextTableCellFormat::bottomBorderBrush() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat17bottomBorderBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def leftBorderBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextTableCellFormat::leftBorderBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#leftBorderBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextTableCellFormat::leftBorderBrush() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat15leftBorderBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def rightBorderBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextTableCellFormat::rightBorderBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#rightBorderBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextTableCellFormat::rightBorderBrush() const
    address = self.uglySide.call(
        'ritual_ZNK20QTextTableCellFormat16rightBorderBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setTopPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setTopPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat13setTopPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat16setBottomPaddingEd', padding,
    )

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setLeftPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat14setLeftPaddingEd', padding,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat15setRightPaddingEd', padding,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat10setPaddingEd', padding,
    )

  @overload(float)
  def setTopBorder(self, width: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setTopBorder(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setTopBorder

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setTopBorder(qreal width)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat12setTopBorderEd', width,
    )

  @overload(float)
  def setBottomBorder(self, width: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setBottomBorder(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBottomBorder

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setBottomBorder(qreal width)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat15setBottomBorderEd', width,
    )

  @overload(float)
  def setLeftBorder(self, width: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setLeftBorder(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setLeftBorder

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setLeftBorder(qreal width)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat13setLeftBorderEd', width,
    )

  @overload(float)
  def setRightBorder(self, width: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setRightBorder(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setRightBorder

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setRightBorder(qreal width)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat14setRightBorderEd', width,
    )

  @overload(float)
  def setBorder(self, width: float) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setBorder(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBorder

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextTableCellFormat::setBorder(qreal width)
    self.uglySide.call('ritual_ZN20QTextTableCellFormat9setBorderEd', width)

  @overload(QTextFrameFormatBorderStyle)
  def setTopBorderStyle(self, style: QTextFrameFormat.BorderStyle) -> None:
    """
    Calls Qt's 'void
    QTextTableCellFormat::setTopBorderStyle(QTextFrameFormat::BorderStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setTopBorderStyle

    Parameters
    ----------

    style : QTextFrameFormat.BorderStyle
      Passed on as its number.
    """
    #  void QTextTableCellFormat::setTopBorderStyle(QTextFrameFormat::
    #      BorderStyle style)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat17setTopBorderStyleEN16QTextFrameFo'
        'rmat11BorderStyleE',
        style.value,
    )

  @overload(QTextFrameFormatBorderStyle)
  def setBottomBorderStyle(
      self,
      style: QTextFrameFormat.BorderStyle,
  ) -> None:
    """
    Calls Qt's 'void
    QTextTableCellFormat::setBottomBorderStyle(QTextFrameFormat::BorderStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBottomBorderStyle

    Parameters
    ----------

    style : QTextFrameFormat.BorderStyle
      Passed on as its number.
    """
    #  void QTextTableCellFormat::setBottomBorderStyle(QTextFrameFormat::
    #      BorderStyle style)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat20setBottomBorderStyleEN16QTextFram'
        'eFormat11BorderStyleE',
        style.value,
    )

  @overload(QTextFrameFormatBorderStyle)
  def setLeftBorderStyle(self, style: QTextFrameFormat.BorderStyle) -> None:
    """
    Calls Qt's 'void
    QTextTableCellFormat::setLeftBorderStyle(QTextFrameFormat::BorderStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setLeftBorderStyle

    Parameters
    ----------

    style : QTextFrameFormat.BorderStyle
      Passed on as its number.
    """
    #  void QTextTableCellFormat::setLeftBorderStyle(QTextFrameFormat::
    #      BorderStyle style)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat18setLeftBorderStyleEN16QTextFrameF'
        'ormat11BorderStyleE',
        style.value,
    )

  @overload(QTextFrameFormatBorderStyle)
  def setRightBorderStyle(self, style: QTextFrameFormat.BorderStyle) -> None:
    """
    Calls Qt's 'void
    QTextTableCellFormat::setRightBorderStyle(QTextFrameFormat::BorderStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setRightBorderStyle

    Parameters
    ----------

    style : QTextFrameFormat.BorderStyle
      Passed on as its number.
    """
    #  void QTextTableCellFormat::setRightBorderStyle(QTextFrameFormat::
    #      BorderStyle style)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat19setRightBorderStyleEN16QTextFrame'
        'Format11BorderStyleE',
        style.value,
    )

  @overload(QTextFrameFormatBorderStyle)
  def setBorderStyle(self, style: QTextFrameFormat.BorderStyle) -> None:
    """
    Calls Qt's 'void
    QTextTableCellFormat::setBorderStyle(QTextFrameFormat::BorderStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBorderStyle

    Parameters
    ----------

    style : QTextFrameFormat.BorderStyle
      Passed on as its number.
    """
    #  void
    #      QTextTableCellFormat::setBorderStyle(QTextFrameFormat::BorderStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat14setBorderStyleEN16QTextFrameForma'
        't11BorderStyleE',
        style.value,
    )

  @overload(QBrush)
  def setTopBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setTopBorderBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setTopBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextTableCellFormat::setTopBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat17setTopBorderBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setBottomBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setBottomBorderBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBottomBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextTableCellFormat::setBottomBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat20setBottomBorderBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setLeftBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setLeftBorderBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setLeftBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextTableCellFormat::setLeftBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat18setLeftBorderBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setRightBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setRightBorderBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setRightBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextTableCellFormat::setRightBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat19setRightBorderBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextTableCellFormat::setBorderBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#setBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextTableCellFormat::setBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN20QTextTableCellFormat14setBorderBrushERK6QBrush',
        self._valueOf(brush),
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
    Notes what was given, for Qt's
    'QTextTableCellFormat::QTextTableCellFormat()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttablecellformat.html#QTextTableCellFormat
    """
    #  QTextTableCellFormat::QTextTableCellFormat()
    self._noteCreation(QTextTableCellFormat, lambda: Rituals.call(
        'ritual_ZN20QTextTableCellFormatC1Ev',
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
