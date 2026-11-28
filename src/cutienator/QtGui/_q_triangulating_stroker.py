"""
QTriangulatingStroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTriangulatingStroker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTriangulatingStroker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTriangulatingStroker: a plain Python object standing
  in front of one C++ QTriangulatingStroker.

  What exists
  -----------

  Every function of Qt's QTriangulatingStroker that has a ritual and that
  Python can call so far, 3 names in all: 'vertexCount', 'setInvScale',
  'emitLineSegment'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QTriangulatingStroker::process(const QVectorPath &path, const
    QPen &pen, const QRectF &clip, QPainter::RenderHints hints)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const float *QTriangulatingStroker::vertices() const': gives
    'float', which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::moveTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::lineTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::cubicTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::join(const qreal *pts)': names 'qreal',
    which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::normalVector(float x1, float y1, float
    x2, float y2, float *nx, float *ny)': takes a number to change where it
    is.
  - Qt's 'void QTriangulatingStroker::endCap(const qreal *pts)': names
    'qreal', which has no cute class yet.
  - Qt's 'void QTriangulatingStroker::arcPoints(float cx, float cy, float
    fromX, float fromY, float toX, float toY, QVarLengthArray<float>
    &points)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTriangulatingStroker::endCapOrJoinClosed(const qreal *start,
    const qreal *cur, bool implicitClose, bool endsAtStart)': names 'qreal',
    which has no cute class yet.

  What to expect
  --------------

  - The C++ QTriangulatingStroker is created at the first use, not by
    'QTriangulatingStroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTriangulatingStroker.
  - Each name of Qt's QTriangulatingStroker that has no cute function yet,
    'arcPoints', 'cubicTo', 'endCap', 'endCapOrJoinClosed', 'join', 'lineTo',
    'moveTo', 'normalVector', 'process', 'vertices', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTriangulatingStroker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int QTriangulatingStroker::vertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriangulatingstroker.html#vertexCount
    """
    #  int QTriangulatingStroker::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK21QTriangulatingStroker11vertexCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setInvScale(self, invScale: float) -> None:
    """
    Calls Qt's 'void QTriangulatingStroker::setInvScale(qreal invScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriangulatingstroker.html#setInvScale

    Parameters
    ----------

    invScale : float
      Passed on as it is.
    """
    #  void QTriangulatingStroker::setInvScale(qreal invScale)
    self.uglySide.call(
        'ritual_ZN21QTriangulatingStroker11setInvScaleEd', invScale,
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
    'QTriangulatingStroker::QTriangulatingStroker()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriangulatingstroker.html#QTriangulatingStroker
    """
    #  QTriangulatingStroker::QTriangulatingStroker()
    self._noteCreation(QTriangulatingStroker, lambda: Rituals.call(
        'ritual_ZN21QTriangulatingStrokerC1Ev',
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

  @overload(float, float, float, float)
  def emitLineSegment(
      self,
      x: float,
      y: float,
      nx: float,
      ny: float,
  ) -> None:
    """
    Calls Qt's 'void QTriangulatingStroker::emitLineSegment(float x, float y,
    float nx, float ny)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtriangulatingstroker.html#emitLineSegment

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    nx : float
      Passed on as it is.

    ny : float
      Passed on as it is.
    """
    #  void QTriangulatingStroker::emitLineSegment(float x, float y, float
    #      nx, float ny)
    self.uglySide.call(
        'ritual_ZN21QTriangulatingStroker15emitLineSegmentEffff',
        x, y, nx, ny,
    )

  @staticmethod
  def arcPoints(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::arcPoints(float cx, float cy, float
    fromX, float fromY, float toX, float toY, QVarLengthArray<float>
    &points)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.arcPoints' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::arcPoints(float cx, float cy, float "
        "fromX, float fromY, float toX, float toY, QVarLengthArray<float> "
        "&points)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def cubicTo(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::cubicTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.cubicTo' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::cubicTo(const qreal *pts)': names "
        "'qreal', which has no cute class yet.")

  @staticmethod
  def endCap(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::endCap(const qreal *pts)': names
    'qreal', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.endCap' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::endCap(const qreal *pts)': names "
        "'qreal', which has no cute class yet.")

  @staticmethod
  def endCapOrJoinClosed(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::endCapOrJoinClosed(const qreal *start,
    const qreal *cur, bool implicitClose, bool endsAtStart)': names 'qreal',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.endCapOrJoinClosed' has no cute function "
        "yet. Qt's 'void QTriangulatingStroker::endCapOrJoinClosed(const "
        "qreal *start, const qreal *cur, bool implicitClose, bool "
        "endsAtStart)': names 'qreal', which has no cute class yet.")

  @staticmethod
  def join(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::join(const qreal *pts)': names 'qreal',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.join' has no cute function yet. Qt's 'void "
        "QTriangulatingStroker::join(const qreal *pts)': names 'qreal', "
        "which has no cute class yet.")

  @staticmethod
  def lineTo(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::lineTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.lineTo' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::lineTo(const qreal *pts)': names "
        "'qreal', which has no cute class yet.")

  @staticmethod
  def moveTo(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::moveTo(const qreal *pts)': names
    'qreal', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.moveTo' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::moveTo(const qreal *pts)': names "
        "'qreal', which has no cute class yet.")

  @staticmethod
  def normalVector(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::normalVector(float x1, float y1, float
    x2, float y2, float *nx, float *ny)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.normalVector' has no cute function yet. "
        "Qt's 'void QTriangulatingStroker::normalVector(float x1, float y1, "
        "float x2, float y2, float *nx, float *ny)': takes a number to "
        "change where it is.")

  @staticmethod
  def process(*__, **_) -> Never:
    """
    Qt's 'void QTriangulatingStroker::process(const QVectorPath &path, const
    QPen &pen, const QRectF &clip, QPainter::RenderHints hints)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.process' has no cute function yet. Qt's "
        "'void QTriangulatingStroker::process(const QVectorPath &path, "
        "const QPen &pen, const QRectF &clip, QPainter::RenderHints "
        "hints)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def vertices(*__, **_) -> Never:
    """
    Qt's 'const float *QTriangulatingStroker::vertices() const': gives
    'float', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTriangulatingStroker.vertices' has no cute function yet. Qt's "
        "'const float *QTriangulatingStroker::vertices() const': gives "
        "'float', which has no cute class yet.")
