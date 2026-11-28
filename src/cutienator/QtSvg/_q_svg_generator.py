"""
QSvgGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/qsvggenerator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtGui import QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QRect, QRectF, QSize
  from ..QtGui import QPaintEngine, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgGenerator(QPaintDevice):
  """
  The cute side of Qt's QSvgGenerator: a plain Python object standing in
  front of one C++ QSvgGenerator.

  It is built on the cute 'QPaintDevice', as Qt's QSvgGenerator is built on
  Qt's QPaintDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgGenerator that has a ritual and that Python can
  call so far, 19 names in all: 'title', 'setTitle', 'description',
  'setDescription', 'size', 'setSize', 'viewBox', 'viewBoxF', 'setViewBox',
  'fileName', 'setFileName', 'outputDevice', 'setOutputDevice',
  'setResolution', 'resolution', 'svgVersion', 'paintEngine', 'metric',
  'initPainter'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgGeneratorPrivate *QSvgGenerator::d_func()': gives
    'QSvgGeneratorPrivate', which has no cute class yet.
  - Qt's 'const QSvgGeneratorPrivate *QSvgGenerator::d_func() const': gives
    'QSvgGeneratorPrivate', which has no cute class yet.
  - Qt's 'QSvgGenerator::~QSvgGenerator()': the destructor: Python never
    removes a C++ QSvgGenerator.

  What to expect
  --------------

  - The C++ QSvgGenerator is created at the first use, not by
    'QSvgGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgGenerator.
  - Each name of Qt's QSvgGenerator that has no cute function yet, 'd_func',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSvgGenerator, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SvgVersion(CuteNum, scoped=True):
    """
    The enum 'QSvgGenerator::SvgVersion' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    SvgTiny12 = Kee[int](0)
    Svg11 = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgGenerator'

  #  A C++ QSvgGenerator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgGenerator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def title(self) -> str:
    """
    Calls Qt's 'QString QSvgGenerator::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgGenerator::title() const
    return self.uglySide.call('ritual_ZNK13QSvgGenerator5titleEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QSvgGenerator::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgGenerator::description() const
    return self.uglySide.call('ritual_ZNK13QSvgGenerator11descriptionEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSvgGenerator::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSvgGenerator::size() const
    address = self.uglySide.call('ritual_ZNK13QSvgGenerator4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def viewBox(self) -> QRect:
    """
    Calls Qt's 'QRect QSvgGenerator::viewBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#viewBox

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSvgGenerator::viewBox() const
    address = self.uglySide.call('ritual_ZNK13QSvgGenerator7viewBoxEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewBoxF(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgGenerator::viewBoxF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#viewBoxF

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgGenerator::viewBoxF() const
    address = self.uglySide.call('ritual_ZNK13QSvgGenerator8viewBoxFEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QSvgGenerator::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgGenerator::fileName() const
    return self.uglySide.call('ritual_ZNK13QSvgGenerator8fileNameEv')

  def outputDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QSvgGenerator::outputDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#outputDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QSvgGenerator::outputDevice() const
    address = self.uglySide.call('ritual_ZNK13QSvgGenerator12outputDeviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def resolution(self) -> int:
    """
    Calls Qt's 'int QSvgGenerator::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#resolution
    """
    #  int QSvgGenerator::resolution() const
    return self.uglySide.call('ritual_ZNK13QSvgGenerator10resolutionEv')

  def svgVersion(self) -> SvgVersion:
    """
    Calls Qt's 'SvgVersion QSvgGenerator::svgVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#svgVersion

    Returns
    -------

    SvgVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SvgVersion(number)'
      gives.
    """
    #  SvgVersion QSvgGenerator::svgVersion() const
    return QSvgGenerator.SvgVersion(self.uglySide.call(
        'ritual_ZNK13QSvgGenerator10svgVersionEv',
    ))

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QSvgGenerator::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QSvgGenerator::paintEngine() const
    ritual = 'ritual_ZNK13QSvgGenerator11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSvgGenerator11paintEngineEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QSvgGenerator::metric(QPaintDevice::PaintDeviceMetric
    metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QSvgGenerator::metric(QPaintDevice::PaintDeviceMetric metric)
    #      const
    ritual = (
        'ritual_ZNK13QSvgGenerator6metricEN12QPaintDevice17PaintDeviceMetri'
        'cE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QSvgGenerator6metricEN12QPaintDevice17PaintDevic'
          'eMetricE')
    return self.uglySide.call(ritual, metric.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgGenerator::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN13QSvgGenerator8setTitleERK7QString', title)

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setDescription(const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgGenerator::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator14setDescriptionERK7QString', description,
    )

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSvgGenerator::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator7setSizeERK5QSize', self._valueOf(size),
    )

  @overload(QRect)
  def setViewBox(self, viewBox: QRect) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setViewBox(const QRect &viewBox)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setViewBox

    Parameters
    ----------

    viewBox : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSvgGenerator::setViewBox(const QRect &viewBox)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator10setViewBoxERK5QRect',
        self._valueOf(viewBox),
    )

  @overload(QRectF)
  def setViewBox(self, viewBox: QRectF) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setViewBox(const QRectF &viewBox)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setViewBox

    Parameters
    ----------

    viewBox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgGenerator::setViewBox(const QRectF &viewBox)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator10setViewBoxERK6QRectF',
        self._valueOf(viewBox),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgGenerator::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator11setFileNameERK7QString', fileName,
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setOutputDevice(self, outputDevice: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setOutputDevice(QIODevice
    *outputDevice)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setOutputDevice

    Parameters
    ----------

    outputDevice : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgGenerator::setOutputDevice(QIODevice *outputDevice)
    self.uglySide.call(
        'ritual_ZN13QSvgGenerator15setOutputDeviceEP9QIODevice',
        self._addressOf(outputDevice),
    )

  @overload(int)
  def setResolution(self, dpi: int) -> None:
    """
    Calls Qt's 'void QSvgGenerator::setResolution(int dpi)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#setResolution

    Parameters
    ----------

    dpi : int
      Passed on as it is.
    """
    #  void QSvgGenerator::setResolution(int dpi)
    self.uglySide.call('ritual_ZN13QSvgGenerator13setResolutionEi', dpi)

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
    Notes what was given, for Qt's 'QSvgGenerator::QSvgGenerator()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#QSvgGenerator
    """
    #  QSvgGenerator::QSvgGenerator()
    self._noteCreation(QSvgGenerator, lambda: Rituals.call(
        'ritual_ZN13QSvgGeneratorC1Ev',
    ))

  @overload(SvgVersion)
  def __init__(self, version: SvgVersion) -> None:
    """
    Notes what was given, for Qt's 'QSvgGenerator::QSvgGenerator(SvgVersion
    version)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#QSvgGenerator

    Parameters
    ----------

    version : SvgVersion
      Passed on as its number.
    """
    #  QSvgGenerator::QSvgGenerator(SvgVersion version)
    self._noteCreation(QSvgGenerator, lambda: Rituals.call(
        'ritual_ZN13QSvgGeneratorC1ENS_10SvgVersionE', version.value,
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
  def initPainter(self, a0: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSvgGenerator::initPainter(QPainter *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggenerator.html#initPainter

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgGenerator::initPainter(QPainter *a0) const
    ritual = 'ritual_ZNK13QSvgGenerator11initPainterEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSvgGenerator11initPainterEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QSvgGeneratorPrivate *QSvgGenerator::d_func()': gives
      'QSvgGeneratorPrivate', which has no cute class yet.
    - Qt's 'const QSvgGeneratorPrivate *QSvgGenerator::d_func() const': gives
      'QSvgGeneratorPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSvgGenerator.d_func' has no cute function yet. Qt's "
        "'QSvgGeneratorPrivate *QSvgGenerator::d_func()': gives "
        "'QSvgGeneratorPrivate', which has no cute class yet. Qt's 'const "
        "QSvgGeneratorPrivate *QSvgGenerator::d_func() const': gives "
        "'QSvgGeneratorPrivate', which has no cute class yet.")
