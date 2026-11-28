"""
QStrokerOps binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QStrokerOps to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
  from . import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']


class QStrokerOps(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStrokerOps: a plain Python object standing in front
  of one C++ QStrokerOps.

  What exists
  -----------

  Every function of Qt's QStrokerOps that has a ritual and that Python can
  call so far, 13 names in all: 'end', 'moveTo', 'lineTo', 'cubicTo',
  'clipRect', 'setClipRect', 'setCurveThresholdFromTransform',
  'setCurveThreshold', 'curveThreshold', 'emitMoveTo', 'emitLineTo',
  'emitCubicTo', 'processCurrentSubpath'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStrokerOps::~QStrokerOps()': the destructor: Python never removes
    a C++ QStrokerOps.
  - Qt's 'void QStrokerOps::setMoveToHook(qStrokerMoveToHook moveToHook)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QStrokerOps::setLineToHook(qStrokerLineToHook lineToHook)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QStrokerOps::setCubicToHook(qStrokerCubicToHook cubicToHook)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QStrokerOps::begin(void *customData)': names 'void', which has
    no cute class yet.
  - Qt's 'void QStrokerOps::strokePath(const QPainterPath &path, void *data,
    const QTransform &matrix)': names 'void', which has no cute class yet.
  - Qt's 'void QStrokerOps::strokePolygon(const QPointF *points, int
    pointCount, bool implicit_close, void *data, const QTransform &matrix)':
    names 'void', which has no cute class yet.
  - Qt's 'void QStrokerOps::strokeEllipse(const QRectF &ellipse, void *data,
    const QTransform &matrix)': names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QStrokerOps is created at the first use, not by
    'QStrokerOps(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStrokerOps.
  - Each name of Qt's QStrokerOps that has no cute function yet, 'begin',
    'setCubicToHook', 'setLineToHook', 'setMoveToHook', 'strokeEllipse',
    'strokePath', 'strokePolygon', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QStrokerOps, each a class in here as in
  #  C++.

  class Element(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QStrokerOps::Element: a plain Python object
    standing in front of one C++ QStrokerOps::Element.

    C++ hands a QStrokerOps::Element around as a copy, so every C++
    QStrokerOps::Element behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QStrokerOps::Element that has a ritual and that
    Python can call so far, 3 names in all: 'isMoveTo', 'isLineTo',
    'isCurveTo'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'qfixed2d QStrokerOps::Element::operator qfixed2d()': an operator
      Python has no name for.
    - Qt's 'QStrokerOps::Element::~Element()': the destructor: Python removes
      its C++ QStrokerOps::Element by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QStrokerOps::Element is created at the first use, not by
      'QStrokerOps::Element(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QStrokerOps::Element back gives a copy the ritual
      made for Python, in a new cute QStrokerOps::Element.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QStrokerOps::Element'

    #  Qt's '~QStrokerOps::Element()'. Naming it makes this a value class:
    #  Python owns every C++ QStrokerOps::Element behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QStrokerOps7ElementD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isMoveTo(self) -> bool:
      """
      Calls Qt's 'bool QStrokerOps::Element::isMoveTo() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstrokerops-element.html#isMoveTo
      """
      #  bool QStrokerOps::Element::isMoveTo() const
      return self.uglySide.call('ritual_ZNK11QStrokerOps7Element8isMoveToEv')

    def isLineTo(self) -> bool:
      """
      Calls Qt's 'bool QStrokerOps::Element::isLineTo() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstrokerops-element.html#isLineTo
      """
      #  bool QStrokerOps::Element::isLineTo() const
      return self.uglySide.call('ritual_ZNK11QStrokerOps7Element8isLineToEv')

    def isCurveTo(self) -> bool:
      """
      Calls Qt's 'bool QStrokerOps::Element::isCurveTo() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstrokerops-element.html#isCurveTo
      """
      #  bool QStrokerOps::Element::isCurveTo() const
      return self.uglySide.call(
          'ritual_ZNK11QStrokerOps7Element9isCurveToEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStrokerOps'

  #  A C++ QStrokerOps Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStrokerOps'

  #  The functions Qt calls itself that QStrokerOps is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'begin': (
          'void QStrokerOps::begin(void *)',
      ),
  }

  #  The functions Qt calls itself that QStrokerOps is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'end': (
          ('_ZN11QStrokerOps3endEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'processCurrentSubpath': (
          ('_ZN11QStrokerOps21processCurrentSubpathEv',
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

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QStrokerOps::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QStrokerOps::clipRect() const
    address = self.uglySide.call('ritual_ZNK11QStrokerOps8clipRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def curveThreshold(self) -> float:
    """
    Calls Qt's 'qfixed QStrokerOps::curveThreshold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#curveThreshold
    """
    #  qfixed QStrokerOps::curveThreshold() const
    return self.uglySide.call('ritual_ZNK11QStrokerOps14curveThresholdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setClipRect(self, clip: QRectF) -> None:
    """
    Calls Qt's 'void QStrokerOps::setClipRect(const QRectF &clip)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#setClipRect

    Parameters
    ----------

    clip : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QStrokerOps::setClipRect(const QRectF &clip)
    self.uglySide.call(
        'ritual_ZN11QStrokerOps11setClipRectERK6QRectF', self._valueOf(clip),
    )

  @overload(QTransform)
  def setCurveThresholdFromTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QStrokerOps::setCurveThresholdFromTransform(const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstrokerops.html#setCurveThresholdFromTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QStrokerOps::setCurveThresholdFromTransform(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN11QStrokerOps30setCurveThresholdFromTransformERK10QTransf'
        'orm',
        self._valueOf(transform),
    )

  @overload(float)
  def setCurveThreshold(self, threshold: float) -> None:
    """
    Calls Qt's 'void QStrokerOps::setCurveThreshold(qfixed threshold)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#setCurveThreshold

    Parameters
    ----------

    threshold : float
      Passed on as it is.
    """
    #  void QStrokerOps::setCurveThreshold(qfixed threshold)
    self.uglySide.call(
        'ritual_ZN11QStrokerOps17setCurveThresholdEd', threshold,
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
    Notes what was given, for Qt's 'QStrokerOps::QStrokerOps()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#QStrokerOps
    """
    #  QStrokerOps::QStrokerOps()
    self._noteCreation(QStrokerOps, lambda: Rituals.call(
        'ritual_ZN11QStrokerOpsC1Ev',
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

  def end(self) -> None:
    """
    Calls Qt's 'void QStrokerOps::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#end
    """
    #  void QStrokerOps::end()
    ritual = 'ritual_ZN11QStrokerOps3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QStrokerOps3endEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStrokerOps::moveTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStrokerOps::moveTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN11QStrokerOps6moveToEdd', x, y)

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStrokerOps::lineTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStrokerOps::lineTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN11QStrokerOps6lineToEdd', x, y)

  @overload(float, float, float, float, float, float)
  def cubicTo(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      ex: float,
      ey: float,
  ) -> None:
    """
    Calls Qt's 'void QStrokerOps::cubicTo(qfixed x1, qfixed y1, qfixed x2,
    qfixed y2, qfixed ex, qfixed ey)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#cubicTo

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    ex : float
      Passed on as it is.

    ey : float
      Passed on as it is.
    """
    #  void QStrokerOps::cubicTo(qfixed x1, qfixed y1, qfixed x2, qfixed y2,
    #      qfixed ex, qfixed ey)
    self.uglySide.call(
        'ritual_ZN11QStrokerOps7cubicToEdddddd', x1, y1, x2, y2, ex, ey,
    )

  @overload(float, float)
  def emitMoveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStrokerOps::emitMoveTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#emitMoveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStrokerOps::emitMoveTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN11QStrokerOps10emitMoveToEdd', x, y)

  @overload(float, float)
  def emitLineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QStrokerOps::emitLineTo(qfixed x, qfixed y)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#emitLineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QStrokerOps::emitLineTo(qfixed x, qfixed y)
    self.uglySide.call('ritual_ZN11QStrokerOps10emitLineToEdd', x, y)

  @overload(float, float, float, float, float, float)
  def emitCubicTo(
      self,
      c1x: float,
      c1y: float,
      c2x: float,
      c2y: float,
      ex: float,
      ey: float,
  ) -> None:
    """
    Calls Qt's 'void QStrokerOps::emitCubicTo(qfixed c1x, qfixed c1y, qfixed
    c2x, qfixed c2y, qfixed ex, qfixed ey)'.

    Qt's own words: https://doc.qt.io/qt-6/qstrokerops.html#emitCubicTo

    Parameters
    ----------

    c1x : float
      Passed on as it is.

    c1y : float
      Passed on as it is.

    c2x : float
      Passed on as it is.

    c2y : float
      Passed on as it is.

    ex : float
      Passed on as it is.

    ey : float
      Passed on as it is.
    """
    #  void QStrokerOps::emitCubicTo(qfixed c1x, qfixed c1y, qfixed c2x,
    #      qfixed c2y, qfixed ex, qfixed ey)
    self.uglySide.call(
        'ritual_ZN11QStrokerOps11emitCubicToEdddddd',
        c1x, c1y, c2x, c2y, ex, ey,
    )

  def processCurrentSubpath(self) -> None:
    """
    Calls Qt's 'void QStrokerOps::processCurrentSubpath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstrokerops.html#processCurrentSubpath
    """
    #  void QStrokerOps::processCurrentSubpath()
    self.uglySide.call('ritual_ZN11QStrokerOps21processCurrentSubpathEv')

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::begin(void *customData)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.begin' has no cute function yet. Qt's 'void "
        "QStrokerOps::begin(void *customData)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def setCubicToHook(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::setCubicToHook(qStrokerCubicToHook cubicToHook)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.setCubicToHook' has no cute function yet. Qt's 'void "
        "QStrokerOps::setCubicToHook(qStrokerCubicToHook cubicToHook)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setLineToHook(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::setLineToHook(qStrokerLineToHook lineToHook)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.setLineToHook' has no cute function yet. Qt's 'void "
        "QStrokerOps::setLineToHook(qStrokerLineToHook lineToHook)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setMoveToHook(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::setMoveToHook(qStrokerMoveToHook moveToHook)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.setMoveToHook' has no cute function yet. Qt's 'void "
        "QStrokerOps::setMoveToHook(qStrokerMoveToHook moveToHook)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def strokeEllipse(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::strokeEllipse(const QRectF &ellipse, void *data,
    const QTransform &matrix)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.strokeEllipse' has no cute function yet. Qt's 'void "
        "QStrokerOps::strokeEllipse(const QRectF &ellipse, void *data, "
        "const QTransform &matrix)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def strokePath(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::strokePath(const QPainterPath &path, void *data,
    const QTransform &matrix)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.strokePath' has no cute function yet. Qt's 'void "
        "QStrokerOps::strokePath(const QPainterPath &path, void *data, "
        "const QTransform &matrix)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def strokePolygon(*__, **_) -> Never:
    """
    Qt's 'void QStrokerOps::strokePolygon(const QPointF *points, int
    pointCount, bool implicit_close, void *data, const QTransform &matrix)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStrokerOps.strokePolygon' has no cute function yet. Qt's 'void "
        "QStrokerOps::strokePolygon(const QPointF *points, int pointCount, "
        "bool implicit_close, void *data, const QTransform &matrix)': names "
        "'void', which has no cute class yet.")
