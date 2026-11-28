"""
QSpline3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qspline3dseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QScatter3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from . import QScatterDataProxy, QSpline3DSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QScatterDataProxy = WAIT['QtGraphs:QScatterDataProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpline3DSeries(QScatter3DSeries):
  """
  The cute side of Qt's QSpline3DSeries: a plain Python object standing in
  front of one C++ QSpline3DSeries.

  It is built on the cute 'QScatter3DSeries', as Qt's QSpline3DSeries is
  built on Qt's QScatter3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpline3DSeries that has a ritual and that Python
  can call so far, 21 names in all: 'metaObject', 'tr', 'd_func',
  'setSplineVisible', 'isSplineVisible', 'setSplineTension', 'splineTension',
  'setSplineKnotting', 'splineKnotting', 'setSplineLooping',
  'isSplineLooping', 'setSplineColor', 'splineColor', 'setSplineResolution',
  'splineResolution', 'splineVisibilityChanged', 'splineTensionChanged',
  'splineKnottingChanged', 'splineLoopingChanged', 'splineColorChanged',
  'splineResolutionChanged'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSpline3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSpline3DSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSpline3DSeriesPrivate *QSpline3DSeries::d_func() const':
    takes in Python what 'QSpline3DSeriesPrivate *QSpline3DSeries::d_func()'
    takes.
  - Qt's 'void QSpline3DSeries::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QSpline3DSeries::~QSpline3DSeries()': the destructor: Python never
    removes a C++ QSpline3DSeries.
  - Qt's 'QSpline3DSeries::QSpline3DSeries(QSpline3DSeriesPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 35 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QSpline3DSeries is created at the first use, not by
    'QSpline3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpline3DSeries.
  - Qt tells when it has removed the C++ QSpline3DSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QSpline3DSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qspline3dseries.html#tr

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
    #  QString QSpline3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSpline3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpline3DSeries'

  #  A C++ QSpline3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpline3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSpline3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspline3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSpline3DSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSpline3DSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSplineVisible(self) -> bool:
    """
    Calls Qt's 'bool QSpline3DSeries::isSplineVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#isSplineVisible
    """
    #  bool QSpline3DSeries::isSplineVisible() const
    return self.uglySide.call(
        'ritual_ZNK15QSpline3DSeries15isSplineVisibleEv',
    )

  def splineTension(self) -> float:
    """
    Calls Qt's 'qreal QSpline3DSeries::splineTension() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspline3dseries.html#splineTension
    """
    #  qreal QSpline3DSeries::splineTension() const
    return self.uglySide.call('ritual_ZNK15QSpline3DSeries13splineTensionEv')

  def splineKnotting(self) -> float:
    """
    Calls Qt's 'qreal QSpline3DSeries::splineKnotting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineKnotting
    """
    #  qreal QSpline3DSeries::splineKnotting() const
    return self.uglySide.call(
        'ritual_ZNK15QSpline3DSeries14splineKnottingEv',
    )

  def isSplineLooping(self) -> bool:
    """
    Calls Qt's 'bool QSpline3DSeries::isSplineLooping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#isSplineLooping
    """
    #  bool QSpline3DSeries::isSplineLooping() const
    return self.uglySide.call(
        'ritual_ZNK15QSpline3DSeries15isSplineLoopingEv',
    )

  def splineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSpline3DSeries::splineColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspline3dseries.html#splineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSpline3DSeries::splineColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QSpline3DSeries11splineColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def splineResolution(self) -> int:
    """
    Calls Qt's 'int QSpline3DSeries::splineResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineResolution
    """
    #  int QSpline3DSeries::splineResolution() const
    return self.uglySide.call(
        'ritual_ZNK15QSpline3DSeries16splineResolutionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSplineVisible(self, draw: bool) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineVisible(bool draw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineVisible

    Parameters
    ----------

    draw : bool
      Passed on as it is.
    """
    #  void QSpline3DSeries::setSplineVisible(bool draw)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries16setSplineVisibleEb', draw,
    )

  @overload(float)
  def setSplineTension(self, tension: float) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineTension(qreal tension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineTension

    Parameters
    ----------

    tension : float
      Passed on as it is.
    """
    #  void QSpline3DSeries::setSplineTension(qreal tension)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries16setSplineTensionEd', tension,
    )

  @overload(float)
  def setSplineKnotting(self, knotting: float) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineKnotting(qreal knotting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineKnotting

    Parameters
    ----------

    knotting : float
      Passed on as it is.
    """
    #  void QSpline3DSeries::setSplineKnotting(qreal knotting)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries17setSplineKnottingEd', knotting,
    )

  @overload(bool)
  def setSplineLooping(self, looping: bool) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineLooping(bool looping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineLooping

    Parameters
    ----------

    looping : bool
      Passed on as it is.
    """
    #  void QSpline3DSeries::setSplineLooping(bool looping)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries16setSplineLoopingEb', looping,
    )

  @overload(QColor)
  def setSplineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSpline3DSeries::setSplineColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries14setSplineColorE6QColor',
        self._valueOf(color),
    )

  @overload(int)
  def setSplineResolution(self, resolution: int) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::setSplineResolution(int resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#setSplineResolution

    Parameters
    ----------

    resolution : int
      Passed on as it is.
    """
    #  void QSpline3DSeries::setSplineResolution(int resolution)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries19setSplineResolutionEi', resolution,
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

  @overload(QScatterDataProxy)
  @overload(QScatterDataProxy, QObject)
  @overload(QScatterDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QScatterDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSpline3DSeries::QSpline3DSeries(QScatterDataProxy *dataProxy, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#QSpline3DSeries

    Parameters
    ----------

    dataProxy : Optional[QScatterDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSpline3DSeries::QSpline3DSeries(QScatterDataProxy *dataProxy, QObject
    #      *parent)
    self._noteCreation(QSpline3DSeries, lambda: Rituals.call(
        'ritual_ZN15QSpline3DSeriesC1EP17QScatterDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSpline3DSeries::QSpline3DSeries(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#QSpline3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSpline3DSeries::QSpline3DSeries(QObject *parent)
    self._noteCreation(QSpline3DSeries, lambda: Rituals.call(
        'ritual_ZN15QSpline3DSeriesC1EP7QObject',
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

  def d_func(self) -> Optional[QSpline3DSeriesPrivate]:
    """
    Calls Qt's 'QSpline3DSeriesPrivate *QSpline3DSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qspline3dseries.html#d_func

    Returns
    -------

    Optional[QSpline3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpline3DSeriesPrivate *QSpline3DSeries::d_func()
    address = self.uglySide.call('ritual_ZN15QSpline3DSeries6d_funcEv')
    from . import QSpline3DSeriesPrivate
    return QSpline3DSeriesPrivate._cuteAt(address)

  @overload(bool)
  def splineVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineVisibilityChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineVisibilityChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QSpline3DSeries::splineVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries23splineVisibilityChangedEb', visible,
    )

  @overload(float)
  def splineTensionChanged(self, tension: float) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineTensionChanged(qreal tension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineTensionChanged

    Parameters
    ----------

    tension : float
      Passed on as it is.
    """
    #  void QSpline3DSeries::splineTensionChanged(qreal tension)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries20splineTensionChangedEd', tension,
    )

  @overload(float)
  def splineKnottingChanged(self, knotting: float) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineKnottingChanged(qreal knotting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineKnottingChanged

    Parameters
    ----------

    knotting : float
      Passed on as it is.
    """
    #  void QSpline3DSeries::splineKnottingChanged(qreal knotting)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries21splineKnottingChangedEd', knotting,
    )

  @overload(bool)
  def splineLoopingChanged(self, looping: bool) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineLoopingChanged(bool looping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineLoopingChanged

    Parameters
    ----------

    looping : bool
      Passed on as it is.
    """
    #  void QSpline3DSeries::splineLoopingChanged(bool looping)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries20splineLoopingChangedEb', looping,
    )

  @overload(QColor)
  def splineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSpline3DSeries::splineColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries18splineColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(int)
  def splineResolutionChanged(self, resolution: int) -> None:
    """
    Calls Qt's 'void QSpline3DSeries::splineResolutionChanged(int
    resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspline3dseries.html#splineResolutionChanged

    Parameters
    ----------

    resolution : int
      Passed on as it is.
    """
    #  void QSpline3DSeries::splineResolutionChanged(int resolution)
    self.uglySide.call(
        'ritual_ZN15QSpline3DSeries23splineResolutionChangedEi', resolution,
    )
