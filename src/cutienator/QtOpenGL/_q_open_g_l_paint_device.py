"""
QOpenGLPaintDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglpaintdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QOpenGLContext, QPaintEngine
  from . import QOpenGLPaintDevicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QOpenGLPaintDevice(QPaintDevice):
  """
  The cute side of Qt's QOpenGLPaintDevice: a plain Python object standing in
  front of one C++ QOpenGLPaintDevice.

  It is built on the cute 'QPaintDevice', as Qt's QOpenGLPaintDevice is built
  on Qt's QPaintDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLPaintDevice that has a ritual and that Python
  can call so far, 15 names in all: 'd_func', 'devType', 'paintEngine',
  'context', 'size', 'setSize', 'setDevicePixelRatio', 'dotsPerMeterX',
  'dotsPerMeterY', 'setDotsPerMeterX', 'setDotsPerMeterY', 'setPaintFlipped',
  'paintFlipped', 'ensureActiveTarget', 'metric'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLPaintDevicePrivate *QOpenGLPaintDevice::d_func()
    const': takes in Python what 'QOpenGLPaintDevicePrivate
    *QOpenGLPaintDevice::d_func()' takes.
  - Qt's 'QOpenGLPaintDevice::~QOpenGLPaintDevice()': the destructor: Python
    never removes a C++ QOpenGLPaintDevice.
  - Qt's 'QOpenGLPaintDevice::QOpenGLPaintDevice(QOpenGLPaintDevicePrivate
    &dd)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLPaintDevice is created at the first use, not by
    'QOpenGLPaintDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLPaintDevice.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLPaintDevice'

  #  A C++ QOpenGLPaintDevice Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLPaintDevice'

  #  The functions Qt calls itself that QOpenGLPaintDevice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'ensureActiveTarget': (
          ('_ZN18QOpenGLPaintDevice18ensureActiveTargetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def devType(self) -> int:
    """
    Calls Qt's 'int QOpenGLPaintDevice::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#devType
    """
    #  int QOpenGLPaintDevice::devType() const
    ritual = 'ritual_ZNK18QOpenGLPaintDevice7devTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QOpenGLPaintDevice7devTypeEv'
    return self.uglySide.call(ritual)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QOpenGLPaintDevice::paintEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QOpenGLPaintDevice::paintEngine() const
    ritual = 'ritual_ZNK18QOpenGLPaintDevice11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QOpenGLPaintDevice11paintEngineEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def context(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLPaintDevice::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#context

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLPaintDevice::context() const
    address = self.uglySide.call('ritual_ZNK18QOpenGLPaintDevice7contextEv')
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QOpenGLPaintDevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QOpenGLPaintDevice::size() const
    address = self.uglySide.call('ritual_ZNK18QOpenGLPaintDevice4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def dotsPerMeterX(self) -> float:
    """
    Calls Qt's 'qreal QOpenGLPaintDevice::dotsPerMeterX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#dotsPerMeterX
    """
    #  qreal QOpenGLPaintDevice::dotsPerMeterX() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLPaintDevice13dotsPerMeterXEv',
    )

  def dotsPerMeterY(self) -> float:
    """
    Calls Qt's 'qreal QOpenGLPaintDevice::dotsPerMeterY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#dotsPerMeterY
    """
    #  qreal QOpenGLPaintDevice::dotsPerMeterY() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLPaintDevice13dotsPerMeterYEv',
    )

  def paintFlipped(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLPaintDevice::paintFlipped() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#paintFlipped
    """
    #  bool QOpenGLPaintDevice::paintFlipped() const
    return self.uglySide.call(
        'ritual_ZNK18QOpenGLPaintDevice12paintFlippedEv',
    )

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int
    QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric metric)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QOpenGLPaintDevice::metric(QPaintDevice::PaintDeviceMetric metric)
    #      const
    ritual = (
        'ritual_ZNK18QOpenGLPaintDevice6metricEN12QPaintDevice17PaintDevice'
        'MetricE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QOpenGLPaintDevice6metricEN12QPaintDevice17Paint'
          'DeviceMetricE')
    return self.uglySide.call(ritual, metric.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QOpenGLPaintDevice::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN18QOpenGLPaintDevice7setSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(float)
  def setDevicePixelRatio(self, devicePixelRatio: float) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::setDevicePixelRatio(qreal
    devicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDevicePixelRatio

    Parameters
    ----------

    devicePixelRatio : float
      Passed on as it is.
    """
    #  void QOpenGLPaintDevice::setDevicePixelRatio(qreal devicePixelRatio)
    self.uglySide.call(
        'ritual_ZN18QOpenGLPaintDevice19setDevicePixelRatioEd',
        devicePixelRatio,
    )

  @overload(float)
  def setDotsPerMeterX(self, a0: float) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::setDotsPerMeterX(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDotsPerMeterX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QOpenGLPaintDevice::setDotsPerMeterX(qreal a0)
    self.uglySide.call(
        'ritual_ZN18QOpenGLPaintDevice16setDotsPerMeterXEd', a0,
    )

  @overload(float)
  def setDotsPerMeterY(self, a0: float) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::setDotsPerMeterY(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#setDotsPerMeterY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QOpenGLPaintDevice::setDotsPerMeterY(qreal a0)
    self.uglySide.call(
        'ritual_ZN18QOpenGLPaintDevice16setDotsPerMeterYEd', a0,
    )

  @overload(bool)
  def setPaintFlipped(self, flipped: bool) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::setPaintFlipped(bool flipped)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#setPaintFlipped

    Parameters
    ----------

    flipped : bool
      Passed on as it is.
    """
    #  void QOpenGLPaintDevice::setPaintFlipped(bool flipped)
    self.uglySide.call(
        'ritual_ZN18QOpenGLPaintDevice15setPaintFlippedEb', flipped,
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
    'QOpenGLPaintDevice::QOpenGLPaintDevice()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice
    """
    #  QOpenGLPaintDevice::QOpenGLPaintDevice()
    self._noteCreation(QOpenGLPaintDevice, lambda: Rituals.call(
        'ritual_ZN18QOpenGLPaintDeviceC1Ev',
    ))

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLPaintDevice::QOpenGLPaintDevice(const QSize &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QOpenGLPaintDevice::QOpenGLPaintDevice(const QSize &size)
    self._noteCreation(QOpenGLPaintDevice, lambda: Rituals.call(
        'ritual_ZN18QOpenGLPaintDeviceC1ERK5QSize', self._valueOf(size),
    ))

  @overload(int, int)
  def __init__(self, width: int, height: int) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLPaintDevice::QOpenGLPaintDevice(int width, int height)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#QOpenGLPaintDevice

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  QOpenGLPaintDevice::QOpenGLPaintDevice(int width, int height)
    self._noteCreation(QOpenGLPaintDevice, lambda: Rituals.call(
        'ritual_ZN18QOpenGLPaintDeviceC1Eii', width, height,
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

  def d_func(self) -> Optional[QOpenGLPaintDevicePrivate]:
    """
    Calls Qt's 'QOpenGLPaintDevicePrivate *QOpenGLPaintDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpaintdevice.html#d_func

    Returns
    -------

    Optional[QOpenGLPaintDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLPaintDevicePrivate *QOpenGLPaintDevice::d_func()
    address = self.uglySide.call('ritual_ZN18QOpenGLPaintDevice6d_funcEv')
    from . import QOpenGLPaintDevicePrivate
    return QOpenGLPaintDevicePrivate._cuteAt(address)

  def ensureActiveTarget(self) -> None:
    """
    Calls Qt's 'void QOpenGLPaintDevice::ensureActiveTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglpaintdevice.html#ensureActiveTarget
    """
    #  void QOpenGLPaintDevice::ensureActiveTarget()
    ritual = 'ritual_ZN18QOpenGLPaintDevice18ensureActiveTargetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QOpenGLPaintDevice18ensureActiveTargetEv'
    self.uglySide.call(ritual)
