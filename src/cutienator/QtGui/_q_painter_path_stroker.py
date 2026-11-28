"""
QPainterPathStroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpainterpath.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPainterPath, QPainterPathStrokerPrivate, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QPen = WAIT['QPen']


class QPainterPathStroker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterPathStroker: a plain Python object standing
  in front of one C++ QPainterPathStroker.

  What exists
  -----------

  Every function of Qt's QPainterPathStroker that has a ritual and that
  Python can call so far, 15 names in all: 'd_func', 'setWidth', 'width',
  'setCapStyle', 'capStyle', 'setJoinStyle', 'joinStyle', 'setMiterLimit',
  'miterLimit', 'setCurveThreshold', 'curveThreshold', 'setDashPattern',
  'setDashOffset', 'dashOffset', 'createStroke'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPainterPathStrokerPrivate *QPainterPathStroker::d_func()
    const': takes in Python what 'QPainterPathStrokerPrivate
    *QPainterPathStroker::d_func()' takes.
  - Qt's 'QPainterPathStroker::~QPainterPathStroker()': the destructor:
    Python never removes a C++ QPainterPathStroker.
  - Qt's 'void QPainterPathStroker::setDashPattern(const QList<qreal>
    &dashPattern)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> QPainterPathStroker::dashPattern() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPainterPathStroker is created at the first use, not by
    'QPainterPathStroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPainterPathStroker.
  - Each name of Qt's QPainterPathStroker that has no cute function yet,
    'dashPattern', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterPathStroker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def width(self) -> float:
    """
    Calls Qt's 'qreal QPainterPathStroker::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathstroker.html#width
    """
    #  qreal QPainterPathStroker::width() const
    return self.uglySide.call('ritual_ZNK19QPainterPathStroker5widthEv')

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QPainterPathStroker::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathstroker.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QPainterPathStroker::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker8capStyleEv',
    ))

  def joinStyle(self) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle QPainterPathStroker::joinStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathstroker.html#joinStyle

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QPainterPathStroker::joinStyle() const
    return Qt.PenJoinStyle(self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker9joinStyleEv',
    ))

  def miterLimit(self) -> float:
    """
    Calls Qt's 'qreal QPainterPathStroker::miterLimit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#miterLimit
    """
    #  qreal QPainterPathStroker::miterLimit() const
    return self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker10miterLimitEv',
    )

  def curveThreshold(self) -> float:
    """
    Calls Qt's 'qreal QPainterPathStroker::curveThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#curveThreshold
    """
    #  qreal QPainterPathStroker::curveThreshold() const
    return self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker14curveThresholdEv',
    )

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QPainterPathStroker::dashOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#dashOffset
    """
    #  qreal QPainterPathStroker::dashOffset() const
    return self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker10dashOffsetEv',
    )

  @overload(QPainterPath)
  def createStroke(self, path: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPathStroker::createStroke(const
    QPainterPath &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#createStroke

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPathStroker::createStroke(const QPainterPath
    #      &path) const
    address = self.uglySide.call(
        'ritual_ZNK19QPainterPathStroker12createStrokeERK12QPainterPath',
        self._valueOf(path),
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathstroker.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QPainterPathStroker::setWidth(qreal width)
    self.uglySide.call('ritual_ZN19QPainterPathStroker8setWidthEd', width)

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, style: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setCapStyle(Qt::PenCapStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setCapStyle

    Parameters
    ----------

    style : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QPainterPathStroker::setCapStyle(Qt::PenCapStyle style)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker11setCapStyleEN2Qt11PenCapStyleE',
        style.value,
    )

  @overload(Qt.PenJoinStyle)
  def setJoinStyle(self, style: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setJoinStyle(Qt::PenJoinStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setJoinStyle

    Parameters
    ----------

    style : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QPainterPathStroker::setJoinStyle(Qt::PenJoinStyle style)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker12setJoinStyleEN2Qt12PenJoinStyleE',
        style.value,
    )

  @overload(float)
  def setMiterLimit(self, length: float) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setMiterLimit(qreal length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setMiterLimit

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void QPainterPathStroker::setMiterLimit(qreal length)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker13setMiterLimitEd', length,
    )

  @overload(float)
  def setCurveThreshold(self, threshold: float) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setCurveThreshold(qreal
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setCurveThreshold

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QPainterPathStroker::setCurveThreshold(qreal threshold)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker17setCurveThresholdEd', threshold,
    )

  @overload(Qt.PenStyle)
  def setDashPattern(self, a0: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setDashPattern(Qt::PenStyle a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setDashPattern

    Parameters
    ----------

    a0 : Qt.PenStyle
      Passed on as its number.
    """
    #  void QPainterPathStroker::setDashPattern(Qt::PenStyle a0)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker14setDashPatternEN2Qt8PenStyleE',
        a0.value,
    )

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QPainterPathStroker::setDashOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QPainterPathStroker::setDashOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN19QPainterPathStroker13setDashOffsetEd', offset,
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
    'QPainterPathStroker::QPainterPathStroker()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#QPainterPathStroker
    """
    #  QPainterPathStroker::QPainterPathStroker()
    self._noteCreation(QPainterPathStroker, lambda: Rituals.call(
        'ritual_ZN19QPainterPathStrokerC1Ev',
    ))

  @overload(QPen)
  def __init__(self, pen: QPen) -> None:
    """
    Notes what was given, for Qt's
    'QPainterPathStroker::QPainterPathStroker(const QPen &pen)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathstroker.html#QPainterPathStroker

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  QPainterPathStroker::QPainterPathStroker(const QPen &pen)
    self._noteCreation(QPainterPathStroker, lambda: Rituals.call(
        'ritual_ZN19QPainterPathStrokerC1ERK4QPen', self._valueOf(pen),
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

  def d_func(self) -> Optional[QPainterPathStrokerPrivate]:
    """
    Calls Qt's 'QPainterPathStrokerPrivate *QPainterPathStroker::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathstroker.html#d_func

    Returns
    -------

    Optional[QPainterPathStrokerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterPathStrokerPrivate *QPainterPathStroker::d_func()
    address = self.uglySide.call('ritual_ZN19QPainterPathStroker6d_funcEv')
    from . import QPainterPathStrokerPrivate
    return QPainterPathStrokerPrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QPainterPathStroker::dashPattern() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPainterPathStroker.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QPainterPathStroker::dashPattern() const': gives a "
        "type Python has no way to take yet.")
