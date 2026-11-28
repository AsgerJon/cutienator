"""
QTextBlockFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import Qt
from . import QTextFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTextBlockFormat(QTextFormat):
  """
  The cute side of Qt's QTextBlockFormat: a plain Python object standing in
  front of one C++ QTextBlockFormat.

  It is built on the cute 'QTextFormat', as Qt's QTextBlockFormat is built on
  Qt's QTextFormat, and has everything that class has.

  C++ hands a QTextBlockFormat around as a copy, so every C++
  QTextBlockFormat behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextBlockFormat that has a ritual and that Python
  can call so far, 26 names in all: 'isValid', 'setAlignment', 'alignment',
  'setTopMargin', 'topMargin', 'setBottomMargin', 'bottomMargin',
  'setLeftMargin', 'leftMargin', 'setRightMargin', 'rightMargin',
  'setTextIndent', 'textIndent', 'setIndent', 'indent', 'setHeadingLevel',
  'headingLevel', 'setLineHeight', 'lineHeight', 'lineHeightType',
  'setNonBreakableLines', 'nonBreakableLines', 'setPageBreakPolicy',
  'pageBreakPolicy', 'setMarker', 'marker'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QTextBlockFormat::setTabPositions(const
    QList<QTextOption::Tab> &tabs)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QList<QTextOption::Tab> QTextBlockFormat::tabPositions() const':
    gives a type Python has no way to take yet.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QTextBlockFormat
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QTextBlockFormat &a1)': an
    operator between other classes, written inside this one.
  - Qt's 'QTextBlockFormat::~QTextBlockFormat()': the destructor: Python
    removes its C++ QTextBlockFormat by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextBlockFormat is created at the first use, not by
    'QTextBlockFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextBlockFormat back gives a copy the ritual made
    for Python, in a new cute QTextBlockFormat.
  - Each name of Qt's QTextBlockFormat that has no cute function yet,
    'setTabPositions', 'tabPositions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextBlockFormat, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LineHeightTypes(CuteNum):
    """
    The enum 'QTextBlockFormat::LineHeightTypes' of Qt, with the 5 names Qt
    gives in it.
    """

    SingleHeight = Kee[int](0)
    ProportionalHeight = Kee[int](1)
    FixedHeight = Kee[int](2)
    MinimumHeight = Kee[int](3)
    LineDistanceHeight = Kee[int](4)

  class MarkerType(CuteNum, scoped=True):
    """
    The enum 'QTextBlockFormat::MarkerType' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoMarker = Kee[int](0)
    Unchecked = Kee[int](1)
    Checked = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBlockFormat'

  #  Qt's '~QTextBlockFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextBlockFormat behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextBlockFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextBlockFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#isValid
    """
    #  bool QTextBlockFormat::isValid() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat7isValidEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QTextBlockFormat::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QTextBlockFormat::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat9alignmentEv',
    ))

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::topMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#topMargin
    """
    #  qreal QTextBlockFormat::topMargin() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat9topMarginEv')

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::bottomMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#bottomMargin
    """
    #  qreal QTextBlockFormat::bottomMargin() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat12bottomMarginEv')

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::leftMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#leftMargin
    """
    #  qreal QTextBlockFormat::leftMargin() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat10leftMarginEv')

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::rightMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#rightMargin
    """
    #  qreal QTextBlockFormat::rightMargin() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat11rightMarginEv')

  def textIndent(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::textIndent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#textIndent
    """
    #  qreal QTextBlockFormat::textIndent() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat10textIndentEv')

  def indent(self) -> int:
    """
    Calls Qt's 'int QTextBlockFormat::indent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#indent
    """
    #  int QTextBlockFormat::indent() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat6indentEv')

  def headingLevel(self) -> int:
    """
    Calls Qt's 'int QTextBlockFormat::headingLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#headingLevel
    """
    #  int QTextBlockFormat::headingLevel() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat12headingLevelEv')

  @overload(float, float)
  def lineHeight(self, scriptLineHeight: float, scaling: float) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::lineHeight(qreal scriptLineHeight,
    qreal scaling) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#lineHeight

    Parameters
    ----------

    scriptLineHeight : float
      Passed on as it is.

    scaling : float
      Passed on as it is.
    """
    #  qreal QTextBlockFormat::lineHeight(qreal scriptLineHeight, qreal
    #      scaling) const
    return self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat10lineHeightEdd',
        scriptLineHeight, scaling,
    )

  @overload()
  def lineHeight(self) -> float:
    """
    Calls Qt's 'qreal QTextBlockFormat::lineHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#lineHeight
    """
    #  qreal QTextBlockFormat::lineHeight() const
    return self.uglySide.call('ritual_ZNK16QTextBlockFormat10lineHeightEv')

  def lineHeightType(self) -> int:
    """
    Calls Qt's 'int QTextBlockFormat::lineHeightType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#lineHeightType
    """
    #  int QTextBlockFormat::lineHeightType() const
    return self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat14lineHeightTypeEv',
    )

  def nonBreakableLines(self) -> bool:
    """
    Calls Qt's 'bool QTextBlockFormat::nonBreakableLines() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#nonBreakableLines
    """
    #  bool QTextBlockFormat::nonBreakableLines() const
    return self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat17nonBreakableLinesEv',
    )

  def pageBreakPolicy(self) -> QTextFormat.PageBreakFlags:
    """
    Calls Qt's 'PageBreakFlags QTextBlockFormat::pageBreakPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#pageBreakPolicy

    Returns
    -------

    QTextFormat.PageBreakFlags
      The value standing for the combination Qt gave back.
    """
    #  PageBreakFlags QTextBlockFormat::pageBreakPolicy() const
    return QTextFormat.PageBreakFlags(self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat15pageBreakPolicyEv',
    ))

  def marker(self) -> MarkerType:
    """
    Calls Qt's 'MarkerType QTextBlockFormat::marker() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#marker

    Returns
    -------

    MarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MarkerType(number)'
      gives.
    """
    #  MarkerType QTextBlockFormat::marker() const
    return QTextBlockFormat.MarkerType(self.uglySide.call(
        'ritual_ZNK16QTextBlockFormat6markerEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QTextBlockFormat::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat12setAlignmentE6QFlagsIN2Qt13AlignmentF'
        'lagEE',
        alignment.value,
    )

  @overload(float)
  def setTopMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setTopMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#setTopMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextBlockFormat::setTopMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QTextBlockFormat12setTopMarginEd', margin)

  @overload(float)
  def setBottomMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setBottomMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setBottomMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextBlockFormat::setBottomMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat15setBottomMarginEd', margin,
    )

  @overload(float)
  def setLeftMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setLeftMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setLeftMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextBlockFormat::setLeftMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat13setLeftMarginEd', margin,
    )

  @overload(float)
  def setRightMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setRightMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setRightMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextBlockFormat::setRightMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat14setRightMarginEd', margin,
    )

  @overload(float)
  def setTextIndent(self, aindent: float) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setTextIndent(qreal aindent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setTextIndent

    Parameters
    ----------

    aindent : float
      Passed on as it is.
    """
    #  void QTextBlockFormat::setTextIndent(qreal aindent)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat13setTextIndentEd', aindent,
    )

  @overload(int)
  def setIndent(self, indent: int) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setIndent(int indent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#setIndent

    Parameters
    ----------

    indent : int
      Passed on as it is.
    """
    #  void QTextBlockFormat::setIndent(int indent)
    self.uglySide.call('ritual_ZN16QTextBlockFormat9setIndentEi', indent)

  @overload(int)
  def setHeadingLevel(self, alevel: int) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setHeadingLevel(int alevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setHeadingLevel

    Parameters
    ----------

    alevel : int
      Passed on as it is.
    """
    #  void QTextBlockFormat::setHeadingLevel(int alevel)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat15setHeadingLevelEi', alevel,
    )

  @overload(float, int)
  def setLineHeight(self, height: float, heightType: int) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setLineHeight(qreal height, int
    heightType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setLineHeight

    Parameters
    ----------

    height : float
      Passed on as it is.

    heightType : int
      Passed on as it is.
    """
    #  void QTextBlockFormat::setLineHeight(qreal height, int heightType)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat13setLineHeightEdi', height, heightType,
    )

  @overload(bool)
  def setNonBreakableLines(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setNonBreakableLines(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setNonBreakableLines

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextBlockFormat::setNonBreakableLines(bool b)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat20setNonBreakableLinesEb', b,
    )

  @overload(QTextFormat.PageBreakFlags)
  def setPageBreakPolicy(self, flags: QTextFormat.PageBreakFlags) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setPageBreakPolicy(PageBreakFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#setPageBreakPolicy

    Parameters
    ----------

    flags : QTextFormat.PageBreakFlags
      Passed on as its number.
    """
    #  void QTextBlockFormat::setPageBreakPolicy(PageBreakFlags flags)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat18setPageBreakPolicyE6QFlagsIN11QTextFo'
        'rmat13PageBreakFlagEE',
        flags.value,
    )

  @overload(MarkerType)
  def setMarker(self, marker: MarkerType) -> None:
    """
    Calls Qt's 'void QTextBlockFormat::setMarker(MarkerType marker)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockformat.html#setMarker

    Parameters
    ----------

    marker : MarkerType
      Passed on as its number.
    """
    #  void QTextBlockFormat::setMarker(MarkerType marker)
    self.uglySide.call(
        'ritual_ZN16QTextBlockFormat9setMarkerENS_10MarkerTypeE',
        marker.value,
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
    Notes what was given, for Qt's 'QTextBlockFormat::QTextBlockFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#QTextBlockFormat
    """
    #  QTextBlockFormat::QTextBlockFormat()
    self._noteCreation(QTextBlockFormat, lambda: Rituals.call(
        'ritual_ZN16QTextBlockFormatC1Ev',
    ))

  @overload(QTextFormat)
  def __init__(self, fmt: QTextFormat) -> None:
    """
    Notes what was given, for Qt's 'QTextBlockFormat::QTextBlockFormat(const
    QTextFormat &fmt)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockformat.html#QTextBlockFormat

    Parameters
    ----------

    fmt : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  QTextBlockFormat::QTextBlockFormat(const QTextFormat &fmt)
    self._noteCreation(QTextBlockFormat, lambda: Rituals.call(
        'ritual_ZN16QTextBlockFormatC1ERK11QTextFormat', self._valueOf(fmt),
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
  def setTabPositions(*__, **_) -> Never:
    """
    Qt's 'void QTextBlockFormat::setTabPositions(const
    QList<QTextOption::Tab> &tabs)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QTextBlockFormat.setTabPositions' has no cute function yet. Qt's "
        "'void QTextBlockFormat::setTabPositions(const "
        "QList<QTextOption::Tab> &tabs)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def tabPositions(*__, **_) -> Never:
    """
    Qt's 'QList<QTextOption::Tab> QTextBlockFormat::tabPositions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextBlockFormat.tabPositions' has no cute function yet. Qt's "
        "'QList<QTextOption::Tab> QTextBlockFormat::tabPositions() const': "
        "gives a type Python has no way to take yet.")
