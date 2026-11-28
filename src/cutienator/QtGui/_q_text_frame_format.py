"""
QTextFrameFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QTextFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QBrush, QTextLength
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QTextLength = WAIT['QTextLength']


class QTextFrameFormat(QTextFormat):
  """
  The cute side of Qt's QTextFrameFormat: a plain Python object standing in
  front of one C++ QTextFrameFormat.

  It is built on the cute 'QTextFormat', as Qt's QTextFrameFormat is built on
  Qt's QTextFormat, and has everything that class has.

  C++ hands a QTextFrameFormat around as a copy, so every C++
  QTextFrameFormat behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextFrameFormat that has a ritual and that Python
  can call so far, 27 names in all: 'isValid', 'setPosition', 'position',
  'setBorder', 'border', 'setBorderBrush', 'borderBrush', 'setBorderStyle',
  'borderStyle', 'setMargin', 'margin', 'setTopMargin', 'topMargin',
  'setBottomMargin', 'bottomMargin', 'setLeftMargin', 'leftMargin',
  'setRightMargin', 'rightMargin', 'setPadding', 'padding', 'setWidth',
  'width', 'setHeight', 'height', 'setPageBreakPolicy', 'pageBreakPolicy'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QTextFrameFormat
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QTextFrameFormat &a1)': an
    operator between other classes, written inside this one.
  - Qt's 'QTextFrameFormat::~QTextFrameFormat()': the destructor: Python
    removes its C++ QTextFrameFormat by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextFrameFormat is created at the first use, not by
    'QTextFrameFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextFrameFormat back gives a copy the ritual made
    for Python, in a new cute QTextFrameFormat.
  """

  #  The enums Qt writes inside QTextFrameFormat, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BorderStyle(CuteNum):
    """
    The enum 'QTextFrameFormat::BorderStyle' of Qt, with the 11 names Qt
    gives in it.
    """

    BorderStyle_None = Kee[int](0)
    BorderStyle_Dotted = Kee[int](1)
    BorderStyle_Dashed = Kee[int](2)
    BorderStyle_Solid = Kee[int](3)
    BorderStyle_Double = Kee[int](4)
    BorderStyle_DotDash = Kee[int](5)
    BorderStyle_DotDotDash = Kee[int](6)
    BorderStyle_Groove = Kee[int](7)
    BorderStyle_Ridge = Kee[int](8)
    BorderStyle_Inset = Kee[int](9)
    BorderStyle_Outset = Kee[int](10)

  class Position(CuteNum):
    """
    The enum 'QTextFrameFormat::Position' of Qt, with the 3 names Qt gives in
    it.
    """

    InFlow = Kee[int](0)
    FloatLeft = Kee[int](1)
    FloatRight = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFrameFormat'

  #  Qt's '~QTextFrameFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextFrameFormat behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextFrameFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextFrameFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#isValid
    """
    #  bool QTextFrameFormat::isValid() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat7isValidEv')

  def position(self) -> Position:
    """
    Calls Qt's 'Position QTextFrameFormat::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#position

    Returns
    -------

    Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Position(number)' gives.
    """
    #  Position QTextFrameFormat::position() const
    return QTextFrameFormat.Position(self.uglySide.call(
        'ritual_ZNK16QTextFrameFormat8positionEv',
    ))

  def border(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::border() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#border
    """
    #  qreal QTextFrameFormat::border() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat6borderEv')

  def borderBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFrameFormat::borderBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#borderBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFrameFormat::borderBrush() const
    address = self.uglySide.call(
        'ritual_ZNK16QTextFrameFormat11borderBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def borderStyle(self) -> BorderStyle:
    """
    Calls Qt's 'BorderStyle QTextFrameFormat::borderStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#borderStyle

    Returns
    -------

    BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BorderStyle(number)'
      gives.
    """
    #  BorderStyle QTextFrameFormat::borderStyle() const
    return QTextFrameFormat.BorderStyle(self.uglySide.call(
        'ritual_ZNK16QTextFrameFormat11borderStyleEv',
    ))

  def margin(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#margin
    """
    #  qreal QTextFrameFormat::margin() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat6marginEv')

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::topMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#topMargin
    """
    #  qreal QTextFrameFormat::topMargin() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat9topMarginEv')

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::bottomMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#bottomMargin
    """
    #  qreal QTextFrameFormat::bottomMargin() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat12bottomMarginEv')

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::leftMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#leftMargin
    """
    #  qreal QTextFrameFormat::leftMargin() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat10leftMarginEv')

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::rightMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#rightMargin
    """
    #  qreal QTextFrameFormat::rightMargin() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat11rightMarginEv')

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QTextFrameFormat::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#padding
    """
    #  qreal QTextFrameFormat::padding() const
    return self.uglySide.call('ritual_ZNK16QTextFrameFormat7paddingEv')

  def width(self) -> QTextLength:
    """
    Calls Qt's 'QTextLength QTextFrameFormat::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#width

    Returns
    -------

    QTextLength
      A new cute QTextLength around the copy Qt gave back. Python owns it.
    """
    #  QTextLength QTextFrameFormat::width() const
    address = self.uglySide.call('ritual_ZNK16QTextFrameFormat5widthEv')
    from . import QTextLength
    return QTextLength._cuteOwning(address)

  def height(self) -> QTextLength:
    """
    Calls Qt's 'QTextLength QTextFrameFormat::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#height

    Returns
    -------

    QTextLength
      A new cute QTextLength around the copy Qt gave back. Python owns it.
    """
    #  QTextLength QTextFrameFormat::height() const
    address = self.uglySide.call('ritual_ZNK16QTextFrameFormat6heightEv')
    from . import QTextLength
    return QTextLength._cuteOwning(address)

  def pageBreakPolicy(self) -> QTextFormat.PageBreakFlags:
    """
    Calls Qt's 'PageBreakFlags QTextFrameFormat::pageBreakPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#pageBreakPolicy

    Returns
    -------

    QTextFormat.PageBreakFlags
      The value standing for the combination Qt gave back.
    """
    #  PageBreakFlags QTextFrameFormat::pageBreakPolicy() const
    return QTextFormat.PageBreakFlags(self.uglySide.call(
        'ritual_ZNK16QTextFrameFormat15pageBreakPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Position)
  def setPosition(self, f: Position) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setPosition(Position f)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setPosition

    Parameters
    ----------

    f : Position
      Passed on as its number.
    """
    #  void QTextFrameFormat::setPosition(Position f)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat11setPositionENS_8PositionE', f.value,
    )

  @overload(float)
  def setBorder(self, border: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setBorder(qreal border)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setBorder

    Parameters
    ----------

    border : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setBorder(qreal border)
    self.uglySide.call('ritual_ZN16QTextFrameFormat9setBorderEd', border)

  @overload(QBrush)
  def setBorderBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setBorderBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setBorderBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextFrameFormat::setBorderBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat14setBorderBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(BorderStyle)
  def setBorderStyle(self, style: BorderStyle) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setBorderStyle(BorderStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setBorderStyle

    Parameters
    ----------

    style : BorderStyle
      Passed on as its number.
    """
    #  void QTextFrameFormat::setBorderStyle(BorderStyle style)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat14setBorderStyleENS_11BorderStyleE',
        style.value,
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QTextFrameFormat9setMarginEd', margin)

  @overload(float)
  def setTopMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setTopMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setTopMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setTopMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QTextFrameFormat12setTopMarginEd', margin)

  @overload(float)
  def setBottomMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setBottomMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setBottomMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setBottomMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat15setBottomMarginEd', margin,
    )

  @overload(float)
  def setLeftMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setLeftMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setLeftMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setLeftMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat13setLeftMarginEd', margin,
    )

  @overload(float)
  def setRightMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setRightMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setRightMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setRightMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat14setRightMarginEd', margin,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN16QTextFrameFormat10setPaddingEd', padding)

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setWidth(qreal width)
    self.uglySide.call('ritual_ZN16QTextFrameFormat8setWidthEd', width)

  @overload(QTextLength)
  def setWidth(self, length: QTextLength) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setWidth(const QTextLength &length)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setWidth

    Parameters
    ----------

    length : QTextLength
      Passed on as a value: Qt reads the C++ QTextLength, which stays
      Python's own.
    """
    #  void QTextFrameFormat::setWidth(const QTextLength &length)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat8setWidthERK11QTextLength',
        self._valueOf(length),
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QTextFrameFormat::setHeight(qreal height)
    self.uglySide.call('ritual_ZN16QTextFrameFormat9setHeightEd', height)

  @overload(QTextLength)
  def setHeight(self, height: QTextLength) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setHeight(const QTextLength &height)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeformat.html#setHeight

    Parameters
    ----------

    height : QTextLength
      Passed on as a value: Qt reads the C++ QTextLength, which stays
      Python's own.
    """
    #  void QTextFrameFormat::setHeight(const QTextLength &height)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat9setHeightERK11QTextLength',
        self._valueOf(height),
    )

  @overload(QTextFormat.PageBreakFlags)
  def setPageBreakPolicy(self, flags: QTextFormat.PageBreakFlags) -> None:
    """
    Calls Qt's 'void QTextFrameFormat::setPageBreakPolicy(PageBreakFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#setPageBreakPolicy

    Parameters
    ----------

    flags : QTextFormat.PageBreakFlags
      Passed on as its number.
    """
    #  void QTextFrameFormat::setPageBreakPolicy(PageBreakFlags flags)
    self.uglySide.call(
        'ritual_ZN16QTextFrameFormat18setPageBreakPolicyE6QFlagsIN11QTextFo'
        'rmat13PageBreakFlagEE',
        flags.value,
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
    Notes what was given, for Qt's 'QTextFrameFormat::QTextFrameFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#QTextFrameFormat
    """
    #  QTextFrameFormat::QTextFrameFormat()
    self._noteCreation(QTextFrameFormat, lambda: Rituals.call(
        'ritual_ZN16QTextFrameFormatC1Ev',
    ))

  @overload(QTextFormat)
  def __init__(self, fmt: QTextFormat) -> None:
    """
    Notes what was given, for Qt's 'QTextFrameFormat::QTextFrameFormat(const
    QTextFormat &fmt)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeformat.html#QTextFrameFormat

    Parameters
    ----------

    fmt : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  QTextFrameFormat::QTextFrameFormat(const QTextFormat &fmt)
    self._noteCreation(QTextFrameFormat, lambda: Rituals.call(
        'ritual_ZN16QTextFrameFormatC1ERK11QTextFormat', self._valueOf(fmt),
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
