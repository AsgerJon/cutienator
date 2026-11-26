"""
QPaintDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpaintdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from . import QPaintEngine, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintDevice(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPaintDevice: a plain Python object standing in front
  of one C++ QPaintDevice.

  What exists
  -----------

  Every function of Qt's QPaintDevice that has a ritual and that Python can
  call so far, 22 names in all: 'devType', 'paintingActive', 'paintEngine',
  'width', 'height', 'widthMM', 'heightMM', 'logicalDpiX', 'logicalDpiY',
  'physicalDpiX', 'physicalDpiY', 'devicePixelRatio', 'devicePixelRatioF',
  'colorCount', 'depth', 'devicePixelRatioFScale', 'encodeMetricF', 'metric',
  'initPainter', 'redirected', 'sharedPainter', 'getDecodedMetricF'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPaintDevice::~QPaintDevice()': the destructor: Python never
    removes a C++ QPaintDevice.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPaintDevice is created at the first use, not by
    'QPaintDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintDevice.
  """

  #  The enums Qt writes inside QPaintDevice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PaintDeviceMetric(CuteNum):
    """
    The enum 'QPaintDevice::PaintDeviceMetric' of Qt, with the 14 names Qt
    gives in it.
    """

    PdmWidth = Kee[int](1)
    PdmHeight = Kee[int](2)
    PdmWidthMM = Kee[int](3)
    PdmHeightMM = Kee[int](4)
    PdmNumColors = Kee[int](5)
    PdmDepth = Kee[int](6)
    PdmDpiX = Kee[int](7)
    PdmDpiY = Kee[int](8)
    PdmPhysicalDpiX = Kee[int](9)
    PdmPhysicalDpiY = Kee[int](10)
    PdmDevicePixelRatio = Kee[int](11)
    PdmDevicePixelRatioScaled = Kee[int](12)
    PdmDevicePixelRatioF_EncodedA = Kee[int](13)
    PdmDevicePixelRatioF_EncodedB = Kee[int](14)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def devicePixelRatioFScale() -> float:
    """
    Calls Qt's 'qreal QPaintDevice::devicePixelRatioFScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevice.html#devicePixelRatioFScale
    """
    #  qreal QPaintDevice::devicePixelRatioFScale()
    return Rituals.call('ritual_ZN12QPaintDevice22devicePixelRatioFScaleEv')

  @staticmethod
  @overload(PaintDeviceMetric, float)
  def encodeMetricF(metric: PaintDeviceMetric, value: float) -> int:
    """
    Calls Qt's 'int QPaintDevice::encodeMetricF(PaintDeviceMetric metric,
    double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#encodeMetricF

    Parameters
    ----------

    metric : PaintDeviceMetric
      Passed on as its number.

    value : float
      Passed on as it is.
    """
    #  int QPaintDevice::encodeMetricF(PaintDeviceMetric metric, double
    #      value)
    return Rituals.call(
        'ritual_ZN12QPaintDevice13encodeMetricFENS_17PaintDeviceMetricEd',
        metric.value, value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintDevice'

  #  A C++ QPaintDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintDevice'

  #  The functions Qt calls itself that QPaintDevice is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'devType': (
          ('_ZNK12QPaintDevice7devTypeEv',
           ('int', 'number', ''),
           ()),
      ),
      'paintEngine': (
          ('_ZNK12QPaintDevice11paintEngineEv',
           ('address', 'address', 'QtGui:QPaintEngine'),
           ()),
      ),
      'metric': (
          ('_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPaintDevice.PaintDeviceMetric'),
           )),
      ),
      'initPainter': (
          ('_ZNK12QPaintDevice11initPainterEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'redirected': (
          ('_ZNK12QPaintDevice10redirectedEP6QPoint',
           ('address', 'address', 'QtGui:QPaintDevice'),
           (
               ('address', 'address', 'QtCore:QPoint'),
           )),
      ),
      'sharedPainter': (
          ('_ZNK12QPaintDevice13sharedPainterEv',
           ('address', 'address', 'QtGui:QPainter'),
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
    Calls Qt's 'int QPaintDevice::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#devType
    """
    #  int QPaintDevice::devType() const
    ritual = 'ritual_ZNK12QPaintDevice7devTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintDevice7devTypeEv'
    return self._callAs('QPaintDevice', ritual)

  def paintingActive(self) -> bool:
    """
    Calls Qt's 'bool QPaintDevice::paintingActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#paintingActive
    """
    #  bool QPaintDevice::paintingActive() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice14paintingActiveEv',
    )

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPaintDevice::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPaintDevice::paintEngine() const
    address = self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice11paintEngineEv',
    )
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#width
    """
    #  int QPaintDevice::width() const
    return self._callAs('QPaintDevice', 'ritual_ZNK12QPaintDevice5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#height
    """
    #  int QPaintDevice::height() const
    return self._callAs('QPaintDevice', 'ritual_ZNK12QPaintDevice6heightEv')

  def widthMM(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::widthMM() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#widthMM
    """
    #  int QPaintDevice::widthMM() const
    return self._callAs('QPaintDevice', 'ritual_ZNK12QPaintDevice7widthMMEv')

  def heightMM(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::heightMM() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#heightMM
    """
    #  int QPaintDevice::heightMM() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice8heightMMEv',
    )

  def logicalDpiX(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::logicalDpiX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#logicalDpiX
    """
    #  int QPaintDevice::logicalDpiX() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice11logicalDpiXEv',
    )

  def logicalDpiY(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::logicalDpiY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#logicalDpiY
    """
    #  int QPaintDevice::logicalDpiY() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice11logicalDpiYEv',
    )

  def physicalDpiX(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::physicalDpiX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#physicalDpiX
    """
    #  int QPaintDevice::physicalDpiX() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice12physicalDpiXEv',
    )

  def physicalDpiY(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::physicalDpiY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#physicalDpiY
    """
    #  int QPaintDevice::physicalDpiY() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice12physicalDpiYEv',
    )

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPaintDevice::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#devicePixelRatio
    """
    #  qreal QPaintDevice::devicePixelRatio() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice16devicePixelRatioEv',
    )

  def devicePixelRatioF(self) -> float:
    """
    Calls Qt's 'qreal QPaintDevice::devicePixelRatioF() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevice.html#devicePixelRatioF
    """
    #  qreal QPaintDevice::devicePixelRatioF() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice17devicePixelRatioFEv',
    )

  def colorCount(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::colorCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#colorCount
    """
    #  int QPaintDevice::colorCount() const
    return self._callAs(
        'QPaintDevice', 'ritual_ZNK12QPaintDevice10colorCountEv',
    )

  def depth(self) -> int:
    """
    Calls Qt's 'int QPaintDevice::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#depth
    """
    #  int QPaintDevice::depth() const
    return self._callAs('QPaintDevice', 'ritual_ZNK12QPaintDevice5depthEv')

  @overload(PaintDeviceMetric)
  def metric(self, metric: PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPaintDevice::metric(PaintDeviceMetric metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#metric

    Parameters
    ----------

    metric : PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPaintDevice::metric(PaintDeviceMetric metric) const
    ritual = 'ritual_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE'
    return self._callAs('QPaintDevice', ritual, metric.value)

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, offset: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QPaintDevice::redirected(QPoint *offset)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#redirected

    Parameters
    ----------

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
    ritual = 'ritual_ZNK12QPaintDevice10redirectedEP6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintDevice10redirectedEP6QPoint'
    address = self._callAs('QPaintDevice', ritual, self._addressOf(offset))
    return QPaintDevice._cuteAt(address)

  def sharedPainter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QPaintDevice::sharedPainter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#sharedPainter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QPaintDevice::sharedPainter() const
    ritual = 'ritual_ZNK12QPaintDevice13sharedPainterEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintDevice13sharedPainterEv'
    address = self._callAs('QPaintDevice', ritual)
    from . import QPainter
    return QPainter._cuteAt(address)

  @overload(PaintDeviceMetric, PaintDeviceMetric)
  def getDecodedMetricF(
      self,
      metricA: PaintDeviceMetric,
      metricB: PaintDeviceMetric,
  ) -> float:
    """
    Calls Qt's 'double QPaintDevice::getDecodedMetricF(PaintDeviceMetric
    metricA, PaintDeviceMetric metricB) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevice.html#getDecodedMetricF

    Parameters
    ----------

    metricA : PaintDeviceMetric
      Passed on as its number.

    metricB : PaintDeviceMetric
      Passed on as its number.
    """
    #  double QPaintDevice::getDecodedMetricF(PaintDeviceMetric metricA,
    #      PaintDeviceMetric metricB) const
    return self._callAs(
        'QPaintDevice',
        'ritual_ZNK12QPaintDevice17getDecodedMetricFENS_17PaintDeviceMetric'
        'ES0_',
        metricA.value, metricB.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QPaintDevice::QPaintDevice()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#QPaintDevice
    """
    #  QPaintDevice::QPaintDevice()
    self._noteCreation(QPaintDevice, lambda: Rituals.call(
        'ritual_ZN12QPaintDeviceC1Ev',
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

  @overload(QPainter)
  @overload(NoneType)
  def initPainter(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QPaintDevice::initPainter(QPainter *painter) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevice.html#initPainter

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintDevice::initPainter(QPainter *painter) const
    ritual = 'ritual_ZNK12QPaintDevice11initPainterEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QPaintDevice11initPainterEP8QPainter'
    self._callAs('QPaintDevice', ritual, self._addressOf(painter))
