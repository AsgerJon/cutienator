"""
QPieSlice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qpieslice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont
  from . import QPieSeries, QPieSlicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']

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
  so far, 69 names in all: 'metaObject', 'tr', 'setLabel', 'label',
  'setLabelVisible', 'isLabelVisible', 'setLabelPosition', 'labelPosition',
  'setLabelColor', 'labelColor', 'setLabelFont', 'labelFont',
  'setLabelArmLengthFactor', 'labelArmLengthFactor', 'setColor', 'color',
  'setBorderColor', 'borderColor', 'setBorderWidth', 'borderWidth',
  'setValue', 'value', 'setExploded', 'isExploded',
  'setExplodeDistanceFactor', 'explodeDistanceFactor', 'percentage',
  'startAngle', 'angleSpan', 'series', 'append', 'insert', 'remove', 'clear',
  'at', 'find', 'replace', 'removeMultiple', 'replaceAll', 'take',
  'subSlices', 'subSlicesCount', 'isEmpty', 'subSlicesSum',
  'setSubSlicesRatio', 'subSlicesRatio', 'labelChanged',
  'labelVisibleChanged', 'labelFontChanged', 'labelColorChanged',
  'valueChanged', 'explodedChanged', 'explodeDistanceFactorChanged',
  'percentageChanged', 'startAngleChanged', 'angleSpanChanged',
  'sliceChanged', 'labelPositionChanged', 'labelArmLengthFactorChanged',
  'colorChanged', 'borderColorChanged', 'borderWidthChanged',
  'subSlicesAdded', 'subSlicesRemoved', 'subSlicesReplaced',
  'subSlicesCountChanged', 'subSlicesSumChanged', 'subSlicesRatioChanged',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieSlice::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPieSlice::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPieSlice::~QPieSlice()': the destructor: Python never removes a
    C++ QPieSlice.
  - Qt's 'QQmlListProperty<QPieSlice> QPieSlice::sliceChildren()': gives a
    type Python has no way to take yet.
  - Qt's 'const QPieSlicePrivate *QPieSlice::d_func() const': takes in Python
    what 'QPieSlicePrivate *QPieSlice::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 84 functions Qt declares: 2 not a gap; 2 forbidden.

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
  - Each name of Qt's QPieSlice that has no cute function yet,
    'sliceChildren', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QPieSlice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LabelPosition(CuteNum, scoped=True):
    """
    The enum 'QPieSlice::LabelPosition' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Outside = Kee[int](0)
    InsideHorizontal = Kee[int](1)
    InsideTangential = Kee[int](2)
    InsideNormal = Kee[int](3)

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
  __qt_part__ = 'QtGraphs'

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

  def isLabelVisible(self) -> bool:
    """
    Calls Qt's 'bool QPieSlice::isLabelVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#isLabelVisible
    """
    #  bool QPieSlice::isLabelVisible() const
    return self.uglySide.call('ritual_ZNK9QPieSlice14isLabelVisibleEv')

  def labelColor(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::labelColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::labelColor() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice10labelColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::color() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QPieSlice::borderColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPieSlice::borderColor() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::borderWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#borderWidth
    """
    #  qreal QPieSlice::borderWidth() const
    return self.uglySide.call('ritual_ZNK9QPieSlice11borderWidthEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#value
    """
    #  qreal QPieSlice::value() const
    return self.uglySide.call('ritual_ZNK9QPieSlice5valueEv')

  def isExploded(self) -> bool:
    """
    Calls Qt's 'bool QPieSlice::isExploded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#isExploded
    """
    #  bool QPieSlice::isExploded() const
    return self.uglySide.call('ritual_ZNK9QPieSlice10isExplodedEv')

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

  @overload(int)
  def at(self, index: int) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSlice::at(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSlice::at(qsizetype index) const
    address = self.uglySide.call('ritual_ZNK9QPieSlice2atEx', index)
    return QPieSlice._cuteAt(address)

  @overload(str)
  def find(self, label: str) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSlice::find(const QString &label) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#find

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSlice::find(const QString &label) const
    address = self.uglySide.call(
        'ritual_ZNK9QPieSlice4findERK7QString', label,
    )
    return QPieSlice._cuteAt(address)

  def subSlices(self) -> QList[QPieSlice]:
    """
    Calls Qt's 'QList<QPieSlice *> QPieSlice::subSlices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlices

    Returns
    -------

    QList[QPieSlice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPieSlice *> QPieSlice::subSlices() const
    address = self.uglySide.call('ritual_ZNK9QPieSlice9subSlicesEv')
    return QList[QPieSlice]._cuteOwning(address)

  def subSlicesCount(self) -> int:
    """
    Calls Qt's 'qsizetype QPieSlice::subSlicesCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesCount
    """
    #  qsizetype QPieSlice::subSlicesCount() const
    return self.uglySide.call('ritual_ZNK9QPieSlice14subSlicesCountEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPieSlice::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#isEmpty
    """
    #  bool QPieSlice::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QPieSlice7isEmptyEv')

  def subSlicesSum(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::subSlicesSum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesSum
    """
    #  qreal QPieSlice::subSlicesSum() const
    return self.uglySide.call('ritual_ZNK9QPieSlice12subSlicesSumEv')

  def subSlicesRatio(self) -> float:
    """
    Calls Qt's 'qreal QPieSlice::subSlicesRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesRatio
    """
    #  qreal QPieSlice::subSlicesRatio() const
    return self.uglySide.call('ritual_ZNK9QPieSlice14subSlicesRatioEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QPieSlice::setLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPieSlice::setLabel(const QString &label)
    self.uglySide.call('ritual_ZN9QPieSlice8setLabelERK7QString', label)

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

  @overload(float)
  def setBorderWidth(self, borderWidth: float) -> None:
    """
    Calls Qt's 'void QPieSlice::setBorderWidth(qreal borderWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setBorderWidth

    Parameters
    ----------

    borderWidth : float
      Passed on as it is.
    """
    #  void QPieSlice::setBorderWidth(qreal borderWidth)
    self.uglySide.call('ritual_ZN9QPieSlice14setBorderWidthEd', borderWidth)

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

  @overload(bool)
  def setExploded(self, exploded: bool) -> None:
    """
    Calls Qt's 'void QPieSlice::setExploded(bool exploded)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setExploded

    Parameters
    ----------

    exploded : bool
      Passed on as it is.
    """
    #  void QPieSlice::setExploded(bool exploded)
    self.uglySide.call('ritual_ZN9QPieSlice11setExplodedEb', exploded)

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

  @overload(float)
  def setSubSlicesRatio(self, subSlicesRatio: float) -> None:
    """
    Calls Qt's 'void QPieSlice::setSubSlicesRatio(qreal subSlicesRatio)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#setSubSlicesRatio

    Parameters
    ----------

    subSlicesRatio : float
      Passed on as it is.
    """
    #  void QPieSlice::setSubSlicesRatio(qreal subSlicesRatio)
    self.uglySide.call(
        'ritual_ZN9QPieSlice17setSubSlicesRatioEd', subSlicesRatio,
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
    Notes what was given, for Qt's 'QPieSlice::QPieSlice(const QString
    &label, qreal value, QObject *parent)', which is called at the first use.

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
    #  QPieSlice::QPieSlice(const QString &label, qreal value, QObject
    #      *parent)
    self._noteCreation(QPieSlice, lambda: Rituals.call(
        'ritual_ZN9QPieSliceC1ERK7QStringdP7QObject',
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

  @overload(THIS)
  @overload(NoneType)
  def append(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::append(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#append

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::append(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice6appendEPS_', self._addressOf(slice),
    )

  @overload(QList[WAIT['QtGraphs:QPieSlice']])
  def append(self, slices: QList[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::append(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#append

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QPieSlice::append(const QList<QPieSlice *> &slices)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice6appendERK5QListIPS_E', self._valueOf(slices),
    )

  @overload(str, float)
  def append(self, label: str, value: float) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSlice::append(const QString &label, qreal
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSlice::append(const QString &label, qreal value)
    address = self.uglySide.call(
        'ritual_ZN9QPieSlice6appendERK7QStringd', label, value,
    )
    return QPieSlice._cuteAt(address)

  @overload(int, THIS)
  @overload(int, NoneType)
  def insert(self, index: int, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::insert(qsizetype index, QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::insert(qsizetype index, QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice6insertExPS_', index, self._addressOf(slice),
    )

  @overload(THIS)
  @overload(NoneType)
  def remove(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::remove(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#remove

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::remove(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice6removeEPS_', self._addressOf(slice),
    )

  @overload(int)
  def remove(self, index: int) -> bool:
    """
    Calls Qt's 'bool QPieSlice::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QPieSlice::remove(qsizetype index)
    return self.uglySide.call('ritual_ZN9QPieSlice6removeEx', index)

  def clear(self) -> None:
    """
    Calls Qt's 'void QPieSlice::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#clear
    """
    #  void QPieSlice::clear()
    self.uglySide.call('ritual_ZN9QPieSlice5clearEv')

  @overload(int, THIS)
  @overload(int, NoneType)
  def replace(self, index: int, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::replace(qsizetype index, QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::replace(qsizetype index, QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice7replaceExPS_', index, self._addressOf(slice),
    )

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def replace(
      self,
      oldSlice: Optional[QPieSlice],
      newSlice: Optional[QPieSlice],
  ) -> bool:
    """
    Calls Qt's 'bool QPieSlice::replace(QPieSlice *oldSlice, QPieSlice
    *newSlice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#replace

    Parameters
    ----------

    oldSlice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newSlice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::replace(QPieSlice *oldSlice, QPieSlice *newSlice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice7replaceEPS_S0_',
        self._addressOf(oldSlice), self._addressOf(newSlice),
    )

  @overload(int, int)
  def removeMultiple(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QPieSlice::removeMultiple(qsizetype index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#removeMultiple

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QPieSlice::removeMultiple(qsizetype index, int count)
    self.uglySide.call(
        'ritual_ZN9QPieSlice14removeMultipleExi', index, count,
    )

  @overload(QList[WAIT['QtGraphs:QPieSlice']])
  def replaceAll(self, slices: QList[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::replaceAll(const QList<QPieSlice *>
    &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#replaceAll

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QPieSlice::replaceAll(const QList<QPieSlice *> &slices)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice10replaceAllERK5QListIPS_E',
        self._valueOf(slices),
    )

  @overload(THIS)
  @overload(NoneType)
  def take(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSlice::take(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#take

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSlice::take(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN9QPieSlice4takeEPS_', self._addressOf(slice),
    )

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelChanged
    """
    #  void QPieSlice::labelChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12labelChangedEv')

  def labelVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelVisibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelVisibleChanged
    """
    #  void QPieSlice::labelVisibleChanged()
    self.uglySide.call('ritual_ZN9QPieSlice19labelVisibleChangedEv')

  def labelFontChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelFontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelFontChanged
    """
    #  void QPieSlice::labelFontChanged()
    self.uglySide.call('ritual_ZN9QPieSlice16labelFontChangedEv')

  def labelColorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#labelColorChanged
    """
    #  void QPieSlice::labelColorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice17labelColorChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#valueChanged
    """
    #  void QPieSlice::valueChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12valueChangedEv')

  def explodedChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::explodedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#explodedChanged
    """
    #  void QPieSlice::explodedChanged()
    self.uglySide.call('ritual_ZN9QPieSlice15explodedChangedEv')

  def explodeDistanceFactorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::explodeDistanceFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#explodeDistanceFactorChanged
    """
    #  void QPieSlice::explodeDistanceFactorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice28explodeDistanceFactorChangedEv')

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

  def sliceChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::sliceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#sliceChanged
    """
    #  void QPieSlice::sliceChanged()
    self.uglySide.call('ritual_ZN9QPieSlice12sliceChangedEv')

  def labelPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#labelPositionChanged
    """
    #  void QPieSlice::labelPositionChanged()
    self.uglySide.call('ritual_ZN9QPieSlice20labelPositionChangedEv')

  def labelArmLengthFactorChanged(self) -> None:
    """
    Calls Qt's 'void QPieSlice::labelArmLengthFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#labelArmLengthFactorChanged
    """
    #  void QPieSlice::labelArmLengthFactorChanged()
    self.uglySide.call('ritual_ZN9QPieSlice27labelArmLengthFactorChangedEv')

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

  @overload(QList[WAIT['QtGraphs:QPieSlice']])
  def subSlicesAdded(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesAdded(const QList<QPieSlice *>
    &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesAdded

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSlice::subSlicesAdded(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN9QPieSlice14subSlicesAddedERK5QListIPS_E',
        self._valueOf(slices),
    )

  @overload(QList[WAIT['QtGraphs:QPieSlice']])
  def subSlicesRemoved(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesRemoved(const QList<QPieSlice *>
    &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesRemoved

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSlice::subSlicesRemoved(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN9QPieSlice16subSlicesRemovedERK5QListIPS_E',
        self._valueOf(slices),
    )

  @overload(QList[WAIT['QtGraphs:QPieSlice']])
  def subSlicesReplaced(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesReplaced(const QList<QPieSlice *>
    &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesReplaced

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSlice::subSlicesReplaced(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN9QPieSlice17subSlicesReplacedERK5QListIPS_E',
        self._valueOf(slices),
    )

  @overload(int)
  def subSlicesCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#subSlicesCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QPieSlice::subSlicesCountChanged(qsizetype count)
    self.uglySide.call('ritual_ZN9QPieSlice21subSlicesCountChangedEx', count)

  @overload(float)
  def subSlicesSumChanged(self, sum: float) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesSumChanged(qreal sum)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieslice.html#subSlicesSumChanged

    Parameters
    ----------

    sum : float
      Passed on as it is.
    """
    #  void QPieSlice::subSlicesSumChanged(qreal sum)
    self.uglySide.call('ritual_ZN9QPieSlice19subSlicesSumChangedEd', sum)

  @overload(float)
  def subSlicesRatioChanged(self, newSubSlicesRatio: float) -> None:
    """
    Calls Qt's 'void QPieSlice::subSlicesRatioChanged(qreal
    newSubSlicesRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieslice.html#subSlicesRatioChanged

    Parameters
    ----------

    newSubSlicesRatio : float
      Passed on as it is.
    """
    #  void QPieSlice::subSlicesRatioChanged(qreal newSubSlicesRatio)
    self.uglySide.call(
        'ritual_ZN9QPieSlice21subSlicesRatioChangedEd', newSubSlicesRatio,
    )

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

  @staticmethod
  def sliceChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QPieSlice> QPieSlice::sliceChildren()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPieSlice.sliceChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QPieSlice> QPieSlice::sliceChildren()': gives a "
        "type Python has no way to take yet.")


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
