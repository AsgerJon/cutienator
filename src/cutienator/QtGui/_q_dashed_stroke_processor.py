"""
QDashedStrokeProcessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDashedStrokeProcessor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QPainterPath

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDashedStrokeProcessor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDashedStrokeProcessor: a plain Python object
  standing in front of one C++ QDashedStrokeProcessor.

  What exists
  -----------

  Every function of Qt's QDashedStrokeProcessor that has a ritual and that
  Python can call so far, 3 names in all: 'addElement', 'elementCount',
  'setInvScale'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDashedStrokeProcessor::process(const QVectorPath &path, const
    QPen &pen, const QRectF &clip, QPainter::RenderHints hints)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPainterPath::ElementType *QDashedStrokeProcessor::elementTypes()
    const': gives 'QPainterPath::ElementType', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QDashedStrokeProcessor is created at the first use, not by
    'QDashedStrokeProcessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDashedStrokeProcessor.
  - Each name of Qt's QDashedStrokeProcessor that has no cute function yet,
    'elementTypes', 'points', 'process', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDashedStrokeProcessor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementCount(self) -> int:
    """
    Calls Qt's 'int QDashedStrokeProcessor::elementCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdashedstrokeprocessor.html#elementCount
    """
    #  int QDashedStrokeProcessor::elementCount() const
    return self.uglySide.call(
        'ritual_ZNK22QDashedStrokeProcessor12elementCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setInvScale(self, invScale: float) -> None:
    """
    Calls Qt's 'void QDashedStrokeProcessor::setInvScale(qreal invScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdashedstrokeprocessor.html#setInvScale

    Parameters
    ----------

    invScale : float
      Passed on as it is.
    """
    #  void QDashedStrokeProcessor::setInvScale(qreal invScale)
    self.uglySide.call(
        'ritual_ZN22QDashedStrokeProcessor11setInvScaleEd', invScale,
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
    'QDashedStrokeProcessor::QDashedStrokeProcessor()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdashedstrokeprocessor.html#QDashedStrokeProcessor
    """
    #  QDashedStrokeProcessor::QDashedStrokeProcessor()
    self._noteCreation(QDashedStrokeProcessor, lambda: Rituals.call(
        'ritual_ZN22QDashedStrokeProcessorC1Ev',
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

  @overload(QPainterPath.ElementType, float, float)
  def addElement(
      self,
      type: QPainterPath.ElementType,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void
    QDashedStrokeProcessor::addElement(QPainterPath::ElementType type, qreal
    x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdashedstrokeprocessor.html#addElement

    Parameters
    ----------

    type : QPainterPath.ElementType
      Passed on as its number.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QDashedStrokeProcessor::addElement(QPainterPath::ElementType
    #      type, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN22QDashedStrokeProcessor10addElementEN12QPainterPath11Ele'
        'mentTypeEdd',
        type.value, x, y,
    )

  @staticmethod
  def elementTypes(*__, **_) -> Never:
    """
    Qt's 'QPainterPath::ElementType *QDashedStrokeProcessor::elementTypes()
    const': gives 'QPainterPath::ElementType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDashedStrokeProcessor.elementTypes' has no cute function yet. "
        "Qt's 'QPainterPath::ElementType "
        "*QDashedStrokeProcessor::elementTypes() const': gives "
        "'QPainterPath::ElementType', which has no cute class yet.")

  @staticmethod
  def points(*__, **_) -> Never:
    """
    Qt's 'qreal *QDashedStrokeProcessor::points() const': takes or gives a
    type that cannot be passed yet: qreal *.
    """
    raise NotImplementedError(
        "'QDashedStrokeProcessor.points' has no cute function yet. Qt's "
        "'qreal *QDashedStrokeProcessor::points() const': takes or gives a "
        "type that cannot be passed yet: qreal *.")

  @staticmethod
  def process(*__, **_) -> Never:
    """
    Qt's 'void QDashedStrokeProcessor::process(const QVectorPath &path, const
    QPen &pen, const QRectF &clip, QPainter::RenderHints hints)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDashedStrokeProcessor.process' has no cute function yet. Qt's "
        "'void QDashedStrokeProcessor::process(const QVectorPath &path, "
        "const QPen &pen, const QRectF &clip, QPainter::RenderHints "
        "hints)': takes a type Python has no way to hand over yet.")
