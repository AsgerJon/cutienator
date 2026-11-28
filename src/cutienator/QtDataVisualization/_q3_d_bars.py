"""
Q3DBars binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dbars.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QWindow
from . import QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
  from ..QtGui import QSurfaceFormat
  from . import Q3DBarsPrivate, QAbstract3DAxis, QBar3DSeries
  from . import QCategory3DAxis, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtDataVisualization:QAbstract3DAxis']
  QBar3DSeries = WAIT['QtDataVisualization:QBar3DSeries']
  QCategory3DAxis = WAIT['QtDataVisualization:QCategory3DAxis']
  QSizeF = WAIT['QSizeF']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QValue3DAxis = WAIT['QtDataVisualization:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DBars(QAbstract3DGraph):
  """
  The cute side of Qt's Q3DBars: a plain Python object standing in front of
  one C++ Q3DBars.

  It is built on the cute 'QAbstract3DGraph', as Qt's Q3DBars is built on
  Qt's QAbstract3DGraph, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DBars that has a ritual and that Python can call
  so far, 43 names in all: 'metaObject', 'tr', 'setPrimarySeries',
  'primarySeries', 'addSeries', 'removeSeries', 'insertSeries', 'seriesList',
  'setMultiSeriesUniform', 'isMultiSeriesUniform', 'setBarThickness',
  'barThickness', 'setBarSpacing', 'barSpacing', 'setBarSpacingRelative',
  'isBarSpacingRelative', 'setBarSeriesMargin', 'barSeriesMargin',
  'setRowAxis', 'rowAxis', 'setColumnAxis', 'columnAxis', 'setValueAxis',
  'valueAxis', 'addAxis', 'releaseAxis', 'axes', 'selectedSeries',
  'setFloorLevel', 'floorLevel', 'multiSeriesUniformChanged',
  'barThicknessChanged', 'barSpacingChanged', 'barSpacingRelativeChanged',
  'barSeriesMarginChanged', 'rowAxisChanged', 'columnAxisChanged',
  'valueAxisChanged', 'primarySeriesChanged', 'selectedSeriesChanged',
  'floorLevelChanged', 'dptr', 'dptrc'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DBars::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Q3DBars::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'Q3DBars::~Q3DBars()': the destructor: Python never removes a C++
    Q3DBars.

  What has no ritual
  ------------------

  4 of the 51 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DBars is created at the first use, not by 'Q3DBars(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DBars.
  - Qt tells when it has removed the C++ Q3DBars. Every call on the cute
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
    Calls Qt's 'QString Q3DBars::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#tr

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
    #  QString Q3DBars::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7Q3DBars2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DBars'

  #  A C++ Q3DBars Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DBars'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DBars::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DBars::metaObject() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def primarySeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Q3DBars::primarySeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#primarySeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Q3DBars::primarySeries() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars13primarySeriesEv')
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def seriesList(self) -> QList[QBar3DSeries]:
    """
    Calls Qt's 'QList<QBar3DSeries *> Q3DBars::seriesList() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#seriesList

    Returns
    -------

    QList[QBar3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBar3DSeries *> Q3DBars::seriesList() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars10seriesListEv')
    from . import QBar3DSeries
    return QList[QBar3DSeries]._cuteOwning(address)

  def isMultiSeriesUniform(self) -> bool:
    """
    Calls Qt's 'bool Q3DBars::isMultiSeriesUniform() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#isMultiSeriesUniform
    """
    #  bool Q3DBars::isMultiSeriesUniform() const
    return self.uglySide.call('ritual_ZNK7Q3DBars20isMultiSeriesUniformEv')

  def barThickness(self) -> float:
    """
    Calls Qt's 'float Q3DBars::barThickness() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#barThickness
    """
    #  float Q3DBars::barThickness() const
    return self.uglySide.call('ritual_ZNK7Q3DBars12barThicknessEv')

  def barSpacing(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Q3DBars::barSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#barSpacing

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Q3DBars::barSpacing() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars10barSpacingEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isBarSpacingRelative(self) -> bool:
    """
    Calls Qt's 'bool Q3DBars::isBarSpacingRelative() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#isBarSpacingRelative
    """
    #  bool Q3DBars::isBarSpacingRelative() const
    return self.uglySide.call('ritual_ZNK7Q3DBars20isBarSpacingRelativeEv')

  def barSeriesMargin(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Q3DBars::barSeriesMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#barSeriesMargin

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Q3DBars::barSeriesMargin() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars15barSeriesMarginEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def rowAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *Q3DBars::rowAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#rowAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *Q3DBars::rowAxis() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars7rowAxisEv')
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def columnAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *Q3DBars::columnAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#columnAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *Q3DBars::columnAxis() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars10columnAxisEv')
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def valueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DBars::valueAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#valueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DBars::valueAxis() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars9valueAxisEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QAbstract3DAxis]:
    """
    Calls Qt's 'QList<QAbstract3DAxis *> Q3DBars::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#axes

    Returns
    -------

    QList[QAbstract3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DAxis *> Q3DBars::axes() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars4axesEv')
    from . import QAbstract3DAxis
    return QList[QAbstract3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Q3DBars::selectedSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#selectedSeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Q3DBars::selectedSeries() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars14selectedSeriesEv')
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def floorLevel(self) -> float:
    """
    Calls Qt's 'float Q3DBars::floorLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#floorLevel
    """
    #  float Q3DBars::floorLevel() const
    return self.uglySide.call('ritual_ZNK7Q3DBars10floorLevelEv')

  def dptrc(self) -> Optional[Q3DBarsPrivate]:
    """
    Calls Qt's 'const Q3DBarsPrivate *Q3DBars::dptrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#dptrc

    Returns
    -------

    Optional[Q3DBarsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Q3DBarsPrivate *Q3DBars::dptrc() const
    address = self.uglySide.call('ritual_ZNK7Q3DBars5dptrcEv')
    from . import Q3DBarsPrivate
    return Q3DBarsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBar3DSeries)
  @overload(NoneType)
  def setPrimarySeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::setPrimarySeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setPrimarySeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::setPrimarySeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars16setPrimarySeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def setMultiSeriesUniform(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Q3DBars::setMultiSeriesUniform(bool uniform)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setMultiSeriesUniform

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Q3DBars::setMultiSeriesUniform(bool uniform)
    self.uglySide.call('ritual_ZN7Q3DBars21setMultiSeriesUniformEb', uniform)

  @overload(float)
  def setBarThickness(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void Q3DBars::setBarThickness(float thicknessRatio)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setBarThickness

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void Q3DBars::setBarThickness(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN7Q3DBars15setBarThicknessEf', thicknessRatio,
    )

  @overload(QSizeF)
  def setBarSpacing(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBars::setBarSpacing(const QSizeF &spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setBarSpacing

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBars::setBarSpacing(const QSizeF &spacing)
    self.uglySide.call(
        'ritual_ZN7Q3DBars13setBarSpacingERK6QSizeF', self._valueOf(spacing),
    )

  @overload(bool)
  def setBarSpacingRelative(self, relative: bool) -> None:
    """
    Calls Qt's 'void Q3DBars::setBarSpacingRelative(bool relative)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setBarSpacingRelative

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void Q3DBars::setBarSpacingRelative(bool relative)
    self.uglySide.call(
        'ritual_ZN7Q3DBars21setBarSpacingRelativeEb', relative,
    )

  @overload(QSizeF)
  def setBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBars::setBarSeriesMargin(const QSizeF &margin)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBars::setBarSeriesMargin(const QSizeF &margin)
    self.uglySide.call(
        'ritual_ZN7Q3DBars18setBarSeriesMarginERK6QSizeF',
        self._valueOf(margin),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::setRowAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::setColumnAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars13setColumnAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def setFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DBars::setFloorLevel(float level)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#setFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DBars::setFloorLevel(float level)
    self.uglySide.call('ritual_ZN7Q3DBars13setFloorLevelEf', level)

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
  @overload(QSurfaceFormat)
  @overload(NoneType)
  @overload(QSurfaceFormat, QWindow)
  @overload(QSurfaceFormat, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      format: Optional[QSurfaceFormat] = None,
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Q3DBars::Q3DBars(const QSurfaceFormat
    *format, QWindow *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#Q3DBars

    Parameters
    ----------

    format : Optional[QSurfaceFormat]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DBars::Q3DBars(const QSurfaceFormat *format, QWindow *parent)
    self._noteCreation(Q3DBars, lambda: Rituals.call(
        'ritual_ZN7Q3DBarsC1EPK14QSurfaceFormatP7QWindow',
        self._addressOf(format), self._addressOf(parent),
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

  @overload(QBar3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::addSeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#addSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::addSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars9addSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::removeSeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#removeSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::removeSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars12removeSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(int, QBar3DSeries)
  @overload(int, NoneType)
  def insertSeries(self, index: int, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::insertSeries(int index, QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::insertSeries(int index, QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars12insertSeriesEiP12QBar3DSeries',
        index, self._addressOf(series),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::addAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::addAxis(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars7addAxisEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::releaseAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::releaseAxis(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars11releaseAxisEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def multiSeriesUniformChanged(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Q3DBars::multiSeriesUniformChanged(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbars.html#multiSeriesUniformChanged

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Q3DBars::multiSeriesUniformChanged(bool uniform)
    self.uglySide.call(
        'ritual_ZN7Q3DBars25multiSeriesUniformChangedEb', uniform,
    )

  @overload(float)
  def barThicknessChanged(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void Q3DBars::barThicknessChanged(float thicknessRatio)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#barThicknessChanged

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void Q3DBars::barThicknessChanged(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN7Q3DBars19barThicknessChangedEf', thicknessRatio,
    )

  @overload(QSizeF)
  def barSpacingChanged(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBars::barSpacingChanged(const QSizeF &spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#barSpacingChanged

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBars::barSpacingChanged(const QSizeF &spacing)
    self.uglySide.call(
        'ritual_ZN7Q3DBars17barSpacingChangedERK6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def barSpacingRelativeChanged(self, relative: bool) -> None:
    """
    Calls Qt's 'void Q3DBars::barSpacingRelativeChanged(bool relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbars.html#barSpacingRelativeChanged

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void Q3DBars::barSpacingRelativeChanged(bool relative)
    self.uglySide.call(
        'ritual_ZN7Q3DBars25barSpacingRelativeChangedEb', relative,
    )

  @overload(QSizeF)
  def barSeriesMarginChanged(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBars::barSeriesMarginChanged(const QSizeF &margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbars.html#barSeriesMarginChanged

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBars::barSeriesMarginChanged(const QSizeF &margin)
    self.uglySide.call(
        'ritual_ZN7Q3DBars22barSeriesMarginChangedERK6QSizeF',
        self._valueOf(margin),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def rowAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::rowAxisChanged(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#rowAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::rowAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars14rowAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def columnAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::columnAxisChanged(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#columnAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::columnAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars17columnAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def valueAxisChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBars::valueAxisChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#valueAxisChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::valueAxisChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN7Q3DBars16valueAxisChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def primarySeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::primarySeriesChanged(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#primarySeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::primarySeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars20primarySeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBars::selectedSeriesChanged(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBars::selectedSeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN7Q3DBars21selectedSeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(float)
  def floorLevelChanged(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DBars::floorLevelChanged(float level)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#floorLevelChanged

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DBars::floorLevelChanged(float level)
    self.uglySide.call('ritual_ZN7Q3DBars17floorLevelChangedEf', level)

  def dptr(self) -> Optional[Q3DBarsPrivate]:
    """
    Calls Qt's 'Q3DBarsPrivate *Q3DBars::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbars.html#dptr

    Returns
    -------

    Optional[Q3DBarsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DBarsPrivate *Q3DBars::dptr()
    address = self.uglySide.call('ritual_ZN7Q3DBars4dptrEv')
    from . import Q3DBarsPrivate
    return Q3DBarsPrivate._cuteAt(address)
