"""
QAreaSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qareaseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor
  from . import QXYSeries
  from ..QtCharts import QAreaSeriesPrivate
  from ..QtQuickShapes import QQuickShapeGradient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']
  QXYSeries = WAIT['QtGraphs:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAreaSeries(QAbstractSeries):
  """
  The cute side of Qt's QAreaSeries: a plain Python object standing in front
  of one C++ QAreaSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QAreaSeries is built on
  Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAreaSeries that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'tr', 'type', 'color',
  'setColor', 'selectedColor', 'setSelectedColor', 'borderColor',
  'setBorderColor', 'selectedBorderColor', 'setSelectedBorderColor',
  'borderWidth', 'setBorderWidth', 'isSelected', 'setSelected',
  'upperSeries', 'setUpperSeries', 'lowerSeries', 'setLowerSeries',
  'gradient', 'setGradient', 'selectedGradient', 'setSelectedGradient',
  'colorChanged', 'selectedColorChanged', 'borderColorChanged',
  'selectedBorderColorChanged', 'borderWidthChanged', 'selectedChanged',
  'upperSeriesChanged', 'lowerSeriesChanged', 'gradientChanged',
  'selectedGradientChanged', 'clicked', 'doubleClicked', 'pressed',
  'released', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAreaSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAreaSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAreaSeries::~QAreaSeries()': the destructor: Python never removes
    a C++ QAreaSeries.
  - Qt's 'QAreaSeries::QAreaSeries(QAreaSeriesPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QAreaSeriesPrivate *QAreaSeries::d_func() const': takes in
    Python what 'QAreaSeriesPrivate *QAreaSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAreaSeries is created at the first use, not by
    'QAreaSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAreaSeries.
  - Qt tells when it has removed the C++ QAreaSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QAreaSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#tr

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
    #  QString QAreaSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QAreaSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAreaSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAreaSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAreaSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAreaSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAreaSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QAreaSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QAreaSeries::type() const
    ritual = 'ritual_ZNK11QAreaSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QAreaSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::color() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::selectedColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#selectedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::selectedColor() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries13selectedColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::borderColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::borderColor() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedBorderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAreaSeries::selectedBorderColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#selectedBorderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAreaSeries::selectedBorderColor() const
    address = self.uglySide.call(
        'ritual_ZNK11QAreaSeries19selectedBorderColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal QAreaSeries::borderWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#borderWidth
    """
    #  qreal QAreaSeries::borderWidth() const
    return self.uglySide.call('ritual_ZNK11QAreaSeries11borderWidthEv')

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QAreaSeries::isSelected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#isSelected
    """
    #  bool QAreaSeries::isSelected() const
    return self.uglySide.call('ritual_ZNK11QAreaSeries10isSelectedEv')

  def upperSeries(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QAreaSeries::upperSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#upperSeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QAreaSeries::upperSeries() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11upperSeriesEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  def lowerSeries(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QAreaSeries::lowerSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#lowerSeries

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QAreaSeries::lowerSeries() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries11lowerSeriesEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  def gradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QAreaSeries::gradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#gradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QAreaSeries::gradient() const
    address = self.uglySide.call('ritual_ZNK11QAreaSeries8gradientEv')
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def selectedGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QAreaSeries::selectedGradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#selectedGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QAreaSeries::selectedGradient() const
    address = self.uglySide.call(
        'ritual_ZNK11QAreaSeries16selectedGradientEv',
    )
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries8setColorE6QColor', self._valueOf(newColor),
    )

  @overload(QColor)
  def setSelectedColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setSelectedColor(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setSelectedColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setSelectedColor(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries16setSelectedColorE6QColor',
        self._valueOf(newColor),
    )

  @overload(QColor)
  def setBorderColor(self, newBorderColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setBorderColor(QColor newBorderColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setBorderColor

    Parameters
    ----------

    newBorderColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setBorderColor(QColor newBorderColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setBorderColorE6QColor',
        self._valueOf(newBorderColor),
    )

  @overload(QColor)
  def setSelectedBorderColor(self, newSelectedBorderColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::setSelectedBorderColor(QColor
    newSelectedBorderColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setSelectedBorderColor

    Parameters
    ----------

    newSelectedBorderColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::setSelectedBorderColor(QColor
    #      newSelectedBorderColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries22setSelectedBorderColorE6QColor',
        self._valueOf(newSelectedBorderColor),
    )

  @overload(float)
  def setBorderWidth(self, newBorderWidth: float) -> None:
    """
    Calls Qt's 'void QAreaSeries::setBorderWidth(qreal newBorderWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setBorderWidth

    Parameters
    ----------

    newBorderWidth : float
      Passed on as it is.
    """
    #  void QAreaSeries::setBorderWidth(qreal newBorderWidth)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setBorderWidthEd', newBorderWidth,
    )

  @overload(bool)
  def setSelected(self, newSelected: bool) -> None:
    """
    Calls Qt's 'void QAreaSeries::setSelected(bool newSelected)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setSelected

    Parameters
    ----------

    newSelected : bool
      Passed on as it is.
    """
    #  void QAreaSeries::setSelected(bool newSelected)
    self.uglySide.call('ritual_ZN11QAreaSeries11setSelectedEb', newSelected)

  @overload(QXYSeries)
  @overload(NoneType)
  def setUpperSeries(self, newUpperSeries: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void QAreaSeries::setUpperSeries(QXYSeries *newUpperSeries)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setUpperSeries

    Parameters
    ----------

    newUpperSeries : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setUpperSeries(QXYSeries *newUpperSeries)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setUpperSeriesEP9QXYSeries',
        self._addressOf(newUpperSeries),
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def setLowerSeries(self, newLowerSeries: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void QAreaSeries::setLowerSeries(QXYSeries *newLowerSeries)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setLowerSeries

    Parameters
    ----------

    newLowerSeries : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setLowerSeries(QXYSeries *newLowerSeries)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries14setLowerSeriesEP9QXYSeries',
        self._addressOf(newLowerSeries),
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setGradient(self, newGradient: Optional[QQuickShapeGradient]) -> None:
    """
    Calls Qt's 'void QAreaSeries::setGradient(QQuickShapeGradient
    *newGradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#setGradient

    Parameters
    ----------

    newGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setGradient(QQuickShapeGradient *newGradient)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries11setGradientEP19QQuickShapeGradient',
        self._addressOf(newGradient),
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setSelectedGradient(
      self,
      newSelectedGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QAreaSeries::setSelectedGradient(QQuickShapeGradient
    *newSelectedGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#setSelectedGradient

    Parameters
    ----------

    newSelectedGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::setSelectedGradient(QQuickShapeGradient
    #      *newSelectedGradient)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries19setSelectedGradientEP19QQuickShapeGradient',
        self._addressOf(newSelectedGradient),
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
    Notes what was given, for Qt's 'QAreaSeries::QAreaSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#QAreaSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAreaSeries::QAreaSeries(QObject *parent)
    self._noteCreation(QAreaSeries, lambda: Rituals.call(
        'ritual_ZN11QAreaSeriesC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QColor)
  def colorChanged(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::colorChanged(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#colorChanged

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::colorChanged(QColor newColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries12colorChangedE6QColor',
        self._valueOf(newColor),
    )

  @overload(QColor)
  def selectedColorChanged(self, newSelectedColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::selectedColorChanged(QColor
    newSelectedColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#selectedColorChanged

    Parameters
    ----------

    newSelectedColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::selectedColorChanged(QColor newSelectedColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries20selectedColorChangedE6QColor',
        self._valueOf(newSelectedColor),
    )

  @overload(QColor)
  def borderColorChanged(self, newBorderColor: QColor) -> None:
    """
    Calls Qt's 'void QAreaSeries::borderColorChanged(QColor newBorderColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#borderColorChanged

    Parameters
    ----------

    newBorderColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::borderColorChanged(QColor newBorderColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries18borderColorChangedE6QColor',
        self._valueOf(newBorderColor),
    )

  @overload(QColor)
  def selectedBorderColorChanged(
      self,
      newSelectedBorderColor: QColor,
  ) -> None:
    """
    Calls Qt's 'void QAreaSeries::selectedBorderColorChanged(QColor
    newSelectedBorderColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#selectedBorderColorChanged

    Parameters
    ----------

    newSelectedBorderColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAreaSeries::selectedBorderColorChanged(QColor
    #      newSelectedBorderColor)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries26selectedBorderColorChangedE6QColor',
        self._valueOf(newSelectedBorderColor),
    )

  def borderWidthChanged(self) -> None:
    """
    Calls Qt's 'void QAreaSeries::borderWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#borderWidthChanged
    """
    #  void QAreaSeries::borderWidthChanged()
    self.uglySide.call('ritual_ZN11QAreaSeries18borderWidthChangedEv')

  def selectedChanged(self) -> None:
    """
    Calls Qt's 'void QAreaSeries::selectedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#selectedChanged
    """
    #  void QAreaSeries::selectedChanged()
    self.uglySide.call('ritual_ZN11QAreaSeries15selectedChangedEv')

  def upperSeriesChanged(self) -> None:
    """
    Calls Qt's 'void QAreaSeries::upperSeriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#upperSeriesChanged
    """
    #  void QAreaSeries::upperSeriesChanged()
    self.uglySide.call('ritual_ZN11QAreaSeries18upperSeriesChangedEv')

  def lowerSeriesChanged(self) -> None:
    """
    Calls Qt's 'void QAreaSeries::lowerSeriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#lowerSeriesChanged
    """
    #  void QAreaSeries::lowerSeriesChanged()
    self.uglySide.call('ritual_ZN11QAreaSeries18lowerSeriesChangedEv')

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def gradientChanged(
      self,
      newGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QAreaSeries::gradientChanged(QQuickShapeGradient
    *newGradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#gradientChanged

    Parameters
    ----------

    newGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::gradientChanged(QQuickShapeGradient *newGradient)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries15gradientChangedEP19QQuickShapeGradient',
        self._addressOf(newGradient),
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def selectedGradientChanged(
      self,
      newGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QAreaSeries::selectedGradientChanged(QQuickShapeGradient
    *newGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qareaseries.html#selectedGradientChanged

    Parameters
    ----------

    newGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAreaSeries::selectedGradientChanged(QQuickShapeGradient
    #      *newGradient)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries23selectedGradientChangedEP19QQuickShapeGrad'
        'ient',
        self._addressOf(newGradient),
    )

  @overload(QPoint)
  def clicked(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QAreaSeries::clicked(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#clicked

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAreaSeries::clicked(QPoint point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries7clickedE6QPoint', self._valueOf(point),
    )

  @overload(QPoint)
  def doubleClicked(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QAreaSeries::doubleClicked(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#doubleClicked

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAreaSeries::doubleClicked(QPoint point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries13doubleClickedE6QPoint',
        self._valueOf(point),
    )

  @overload(QPoint)
  def pressed(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QAreaSeries::pressed(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#pressed

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAreaSeries::pressed(QPoint point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries7pressedE6QPoint', self._valueOf(point),
    )

  @overload(QPoint)
  def released(self, point: QPoint) -> None:
    """
    Calls Qt's 'void QAreaSeries::released(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#released

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAreaSeries::released(QPoint point)
    self.uglySide.call(
        'ritual_ZN11QAreaSeries8releasedE6QPoint', self._valueOf(point),
    )

  def d_func(self) -> Optional[QAreaSeriesPrivate]:
    """
    Calls Qt's 'QAreaSeriesPrivate *QAreaSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qareaseries.html#d_func

    Returns
    -------

    Optional[QAreaSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAreaSeriesPrivate *QAreaSeries::d_func()
    address = self.uglySide.call('ritual_ZN11QAreaSeries6d_funcEv')
    from ..QtCharts import QAreaSeriesPrivate
    return QAreaSeriesPrivate._cuteAt(address)
