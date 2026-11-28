"""
QPieSlice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qpieslice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QColor, QFont, QPen
  from . import QPieSeries, QPieSlicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieSlice(QObject):
  """
  The cute side of Qt's QPieSlice: a plain Python object standing in front of
  one C++ QPieSlice.

  It is built on the cute 'QObject', as Qt's QPieSlice is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieSlice that has a ritual and that Python can call
  so far, 56 names in all: 'metaObject', 'tr', 'setLabel', 'label',
  'setValue', 'value', 'setLabelVisible', 'isLabelVisible', 'labelPosition',
  'setLabelPosition', 'setExploded', 'isExploded', 'setPen', 'pen',
  'borderColor', 'setBorderColor', 'borderWidth', 'setBorderWidth',
  'setBrush', 'brush', 'color', 'setColor', 'setLabelBrush', 'labelBrush',
  'labelColor', 'setLabelColor', 'setLabelFont', 'labelFont',
  'setLabelArmLengthFactor', 'labelArmLengthFactor',
  'setExplodeDistanceFactor', 'explodeDistanceFactor', 'percentage',
  'startAngle', 'angleSpan', 'series', 'clicked', 'hovered', 'pressed',
  'released', 'doubleClicked', 'labelChanged', 'valueChanged',
  'labelVisibleChanged', 'penChanged', 'brushChanged', 'labelBrushChanged',
  'labelFontChanged', 'percentageChanged', 'startAngleChanged',
  'angleSpanChanged', 'colorChanged', 'borderColorChanged',
  'borderWidthChanged', 'labelColorChanged', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieSlice::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPieSlice::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPieSlice::~QPieSlice()': the destructor: Python never removes a
    C++ QPieSlice.
  - Qt's 'const QPieSlicePrivate *QPieSlice::d_func() const': takes in Python
    what 'QPieSlicePrivate *QPieSlice::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 66 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPieSlice is created at the first use, not by 'QPieSlice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieSlice.
  - Qt tells when it has removed the C++ QPieSlice. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPieSlice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LabelPosition(CuteNum):
    """
    The enum 'QPieSlice::LabelPosition' of Qt, with the 4 names Qt gives in
    it.
    """

    LabelOutside = Kee[int](0)
    LabelInsideHorizontal = Kee[int](1)
    LabelInsideTangential = Kee[int](2)
    LabelInsideNormal = Kee[int](3)

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
    Calls Qt's 'QString QPieSlice::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#tr

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
    #  QString QPieSlice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QPieSlice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieSlice'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QPieSlice Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieSlice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieSlice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieSlice::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def label(self) -> str:
    """
    Calls Qt's 'QString QPieSlice::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPieSlice::label() const
    return self.uglySide.call('ritual_ZNK9QPieSlice5labelEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#value
    """
    #  qreal QPieSlice::value() const
    return self.uglySide.call('ritual_ZNK9QPieSlice5valueEv')

  def isLabelVisible(self) -> bool:
    """
    Calls Qt's 'bool QPieSlice::isLabelVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#isLabelVisible
    """
    #  bool QPieSlice::isLabelVisible() const
    return self.uglySide.call('ritual_ZNK9QPieSlice14isLabelVisibleEv')

  def isExploded(self) -> bool:
    """
    Calls Qt's 'bool QPieSlice::isExploded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#isExploded
    """
    #  bool QPieSlice::isExploded() const
    return self.uglySide.call('ritual_ZNK9QPieSlice10isExplodedEv')

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QPieSlice::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QPieSlice::pen() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QPieSlice::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QPieSlice::brush() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QPieSlice::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QPieSlice::labelBrush() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice10labelBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QPieSlice::labelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QPieSlice::labelFont() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice9labelFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def labelArmLengthFactor(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::labelArmLengthFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#labelArmLengthFactor
    """
    #  qreal QPieSlice::labelArmLengthFactor() const
    return self.uglySide.call('ritual_ZNK9QPieSlice20labelArmLengthFactorEv')

  def explodeDistanceFactor(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::explodeDistanceFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#explodeDistanceFactor
    """
    #  qreal QPieSlice::explodeDistanceFactor() const
    return self.uglySide.call(
        'ritual_ZNK9QPieSlice21explodeDistanceFactorEv',
    )

  def percentage(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::percentage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#percentage
    """
    #  qreal QPieSlice::percentage() const
    return self.uglySide.call('ritual_ZNK9QPieSlice10percentageEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#startAngle
    """
    #  qreal QPieSlice::startAngle() const
    return self.uglySide.call('ritual_ZNK9QPieSlice10startAngleEv')

  def angleSpan(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::angleSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#angleSpan
    """
    #  qreal QPieSlice::angleSpan() const
    return self.uglySide.call('ritual_ZNK9QPieSlice9angleSpanEv')

  def series(self) -> Optional[QPieSeries]:
    """
    Calls Qt's 'QPieSeries *QPieSlice::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#series

    Returns
    -------

    Optional[QPieSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeries *QPieSlice::series() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice6seriesEv')
    from . import QPieSeries
    return QPieSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabel(QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPieSlice::setLabel(QString label)
    self.uglySide.call('ritual_ZN9QPieSlice8setLabelE7QString', label)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QPieSlice::setValue(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QPieSlice::setValue(qreal value)
    self.uglySide.call('ritual_ZN9QPieSlice8setValueEd', value)

  @overload()
  @overload(bool)
  def setLabelVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabelVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPieSlice::setLabelVisible(bool visible)
    self.uglySide.call('ritual_ZN9QPieSlice15setLabelVisibleEb', visible)

  @overload(LabelPosition)
  def setLabelPosition(self, position: LabelPosition) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelPosition(LabelPosition position)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabelPosition

    Parameters
    ----------

    position : LabelPosition
      Passed on as its number.
    """
    #  void QPieSlice::setLabelPosition(LabelPosition position)
    self.uglySide.call(
        'ritual_ZN9QPieSlice16setLabelPositionENS_13LabelPositionE',
        position.value,
    )

  @overload()
  @overload(bool)
  def setExploded(self, exploded: bool = True) -> None:
    """
    Calls Qt's 'void QPieSlice::setExploded(bool exploded)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setExploded

    Parameters
    ----------

    exploded : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPieSlice::setExploded(bool exploded)
    self.uglySide.call('ritual_ZN9QPieSlice11setExplodedEb', exploded)

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QPieSlice::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QPieSlice::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN9QPieSlice6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QColor)
  def setBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPieSlice::setBorderColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPieSlice::setBorderColor(QColor color)
    self.uglySide.call(
        'ritual_ZN9QPieSlice14setBorderColorE6QColor', self._valueOf(color),
    )

  @overload(int)
  def setBorderWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QPieSlice::setBorderWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setBorderWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QPieSlice::setBorderWidth(int width)
    self.uglySide.call('ritual_ZN9QPieSlice14setBorderWidthEi', width)

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPieSlice::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPieSlice::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN9QPieSlice8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPieSlice::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPieSlice::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN9QPieSlice8setColorE6QColor', self._valueOf(color),
    )

  @overload(QBrush)
  def setLabelBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPieSlice::setLabelBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN9QPieSlice13setLabelBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QColor)
  def setLabelColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabelColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPieSlice::setLabelColor(QColor color)
    self.uglySide.call(
        'ritual_ZN9QPieSlice13setLabelColorE6QColor', self._valueOf(color),
    )

  @overload(QFont)
  def setLabelFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabelFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPieSlice::setLabelFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN9QPieSlice12setLabelFontERK5QFont', self._valueOf(font),
    )

  @overload(float)
  def setLabelArmLengthFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabelArmLengthFactor(qreal factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#setLabelArmLengthFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QPieSlice::setLabelArmLengthFactor(qreal factor)
    self.uglySide.call(
        'ritual_ZN9QPieSlice23setLabelArmLengthFactorEd', factor,
    )

  @overload(float)
  def setExplodeDistanceFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QPieSlice::setExplodeDistanceFactor(qreal factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#setExplodeDistanceFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QPieSlice::setExplodeDistanceFactor(qreal factor)
    self.uglySide.call(
        'ritual_ZN9QPieSlice24setExplodeDistanceFactorEd', factor,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPieSlice::QPieSlice(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#QPieSlice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPieSlice::QPieSlice(QObject *parent)
    self._noteCreation(QPieSlice, lambda: Rituals.call(
        'ritual_ZN9QPieSliceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, float)
  @overload(str, float, QObject)
  @overload(str, float, NoneType)
  def __init__(
      self,
      label: str,
      value: float,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPieSlice::QPieSlice(QString label, qreal
    value, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#QPieSlice

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPieSlice::QPieSlice(QString label, qreal value, QObject *parent)
    self._noteCreation(QPieSlice, lambda: Rituals.call(
        'ritual_ZN9QPieSliceC1E7QStringdP7QObject',
        label, value, self._addressOf(parent, 'QObject'),
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

  def labelPosition(self) -> LabelPosition:
    """
    Calls Qt's 'LabelPosition QPieSlice::labelPosition()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelPosition

    Returns
    -------

    LabelPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelPosition(number)'
      gives.
    """
    #  LabelPosition QPieSlice::labelPosition()
    return QPieSlice.LabelPosition(self.uglySide.call(
        'ritual_ZN9QPieSlice13labelPositionEv',
    ))

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::borderColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::borderColor()
    address = self.uglySide.call('ritual_ZN9QPieSlice11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderWidth(self) -> int:
    """
    Calls Qt's 'int QPieSlice::borderWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderWidth
    """
    #  int QPieSlice::borderWidth()
    return self.uglySide.call('ritual_ZN9QPieSlice11borderWidthEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::color()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::color()
    address = self.uglySide.call('ritual_ZN9QPieSlice5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelColor(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::labelColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::labelColor()
    address = self.uglySide.call('ritual_ZN9QPieSlice10labelColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def clicked(self) -> None:
    """
    Calls Qt's 'void QPieSlice::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#clicked
    """
    #  void QPieSlice::clicked()
    self.uglySide.call('ritual_ZN9QPieSlice7clickedEv')

  @overload(bool)
  def hovered(self, state: bool) -> None:
    """
    Calls Qt's 'void QPieSlice::hovered(bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#hovered

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void QPieSlice::hovered(bool state)
    self.uglySide.call('ritual_ZN9QPieSlice7hoveredEb', state)

  def pressed(self) -> None:
    """
    Calls Qt's 'void QPieSlice::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#pressed
    """
    #  void QPieSlice::pressed()
    self.uglySide.call('ritual_ZN9QPieSlice7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QPieSlice::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#released
    """
    #  void QPieSlice::released()
    self.uglySide.call('ritual_ZN9QPieSlice8releasedEv')

  def doubleClicked(self) -> None:
    """
    Calls Qt's 'void QPieSlice::doubleClicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#doubleClicked
    """
    #  void QPieSlice::doubleClicked()
    self.uglySide.call('ritual_ZN9QPieSlice13doubleClickedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelChanged
    """
    #  void QPieSlice::labelChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12labelChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#valueChanged
    """
    #  void QPieSlice::valueChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12valueChangedEv')

  def labelVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelVisibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelVisibleChanged
    """
    #  void QPieSlice::labelVisibleChanged()
    self.uglySide.call('ritual_ZN9QPieSlice19labelVisibleChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#penChanged
    """
    #  void QPieSlice::penChanged()
    self.uglySide.call('ritual_ZN9QPieSlice10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#brushChanged
    """
    #  void QPieSlice::brushChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12brushChangedEv')

  def labelBrushChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelBrushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelBrushChanged
    """
    #  void QPieSlice::labelBrushChanged()
    self.uglySide.call('ritual_ZN9QPieSlice17labelBrushChangedEv')

  def labelFontChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelFontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelFontChanged
    """
    #  void QPieSlice::labelFontChanged()
    self.uglySide.call('ritual_ZN9QPieSlice16labelFontChangedEv')

  def percentageChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::percentageChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#percentageChanged
    """
    #  void QPieSlice::percentageChanged()
    self.uglySide.call('ritual_ZN9QPieSlice17percentageChangedEv')

  def startAngleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::startAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#startAngleChanged
    """
    #  void QPieSlice::startAngleChanged()
    self.uglySide.call('ritual_ZN9QPieSlice17startAngleChangedEv')

  def angleSpanChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::angleSpanChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#angleSpanChanged
    """
    #  void QPieSlice::angleSpanChanged()
    self.uglySide.call('ritual_ZN9QPieSlice16angleSpanChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#colorChanged
    """
    #  void QPieSlice::colorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12colorChangedEv')

  def borderColorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::borderColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderColorChanged
    """
    #  void QPieSlice::borderColorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice18borderColorChangedEv')

  def borderWidthChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::borderWidthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderWidthChanged
    """
    #  void QPieSlice::borderWidthChanged()
    self.uglySide.call('ritual_ZN9QPieSlice18borderWidthChangedEv')

  def labelColorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelColorChanged
    """
    #  void QPieSlice::labelColorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice17labelColorChangedEv')

  def d_func(self) -> Optional[QPieSlicePrivate]:
    """
    Calls Qt's 'QPieSlicePrivate *QPieSlice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#d_func

    Returns
    -------

    Optional[QPieSlicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlicePrivate *QPieSlice::d_func()
    address = self.uglySide.call('ritual_ZN9QPieSlice6d_funcEv')
    from . import QPieSlicePrivate
    return QPieSlicePrivate._cuteAt(address)


#  Qt's 'QList<QPieSlice *>': the list of QPieSlice, which 'QList[QPieSlice]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QPieSlice.
QList.createKind(
    QPieSlice, 'address',
    make='ritual_list_make_QPieSlice_ptr',
    add='ritual_list_add_QPieSlice_ptr',
    size='ritual_list_size_QPieSlice_ptr',
    at='ritual_list_at_QPieSlice_ptr',
    drop='ritual_list_drop_QPieSlice_ptr',
)
