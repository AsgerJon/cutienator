"""
QSvgMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgMarker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QSvgNode, QSvgSymbolLike

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgMarker(QSvgSymbolLike):
  """
  The cute side of Qt's QSvgMarker: a plain Python object standing in front
  of one C++ QSvgMarker.

  It is built on the cute 'QSvgSymbolLike', as Qt's QSvgMarker is built on
  Qt's QSvgSymbolLike, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgMarker that has a ritual and that Python can
  call so far, 4 names in all: 'orientation', 'orientationAngle',
  'markerUnits', 'type'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgMarker::~QSvgMarker()': the destructor: Python never removes a
    C++ QSvgMarker.
  - Qt's 'void QSvgMarker::drawCommand(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgMarker::drawMarkersForNode(QSvgNode *node, QPainter *p,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QRectF QSvgMarker::markersBoundsForNode(const QSvgNode *node,
    QPainter *p, QSvgExtraStates &states)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSvgMarker::drawHelper(const QSvgNode *node, QPainter *p,
    QSvgExtraStates &states, QRectF *boundingRect)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgMarker is created at the first use, not by 'QSvgMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgMarker.
  - Each name of Qt's QSvgMarker that has no cute function yet, 'drawHelper',
    'drawMarkersForNode', 'markersBoundsForNode', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSvgMarker, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MarkerUnits(CuteNum, scoped=True):
    """
    The enum 'QSvgMarker::MarkerUnits' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    StrokeWidth = Kee[int](0)
    UserSpaceOnUse = Kee[int](1)

  class Orientation(CuteNum, scoped=True):
    """
    The enum 'QSvgMarker::Orientation' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Auto = Kee[int](0)
    AutoStartReverse = Kee[int](1)
    Value = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgMarker'

  #  A C++ QSvgMarker Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgMarker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QSvgMarker::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmarker.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QSvgMarker::orientation() const
    return QSvgMarker.Orientation(self.uglySide.call(
        'ritual_ZNK10QSvgMarker11orientationEv',
    ))

  def orientationAngle(self) -> float:
    """
    Calls Qt's 'qreal QSvgMarker::orientationAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmarker.html#orientationAngle
    """
    #  qreal QSvgMarker::orientationAngle() const
    return self.uglySide.call('ritual_ZNK10QSvgMarker16orientationAngleEv')

  def markerUnits(self) -> MarkerUnits:
    """
    Calls Qt's 'MarkerUnits QSvgMarker::markerUnits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmarker.html#markerUnits

    Returns
    -------

    MarkerUnits
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MarkerUnits(number)'
      gives.
    """
    #  MarkerUnits QSvgMarker::markerUnits() const
    return QSvgMarker.MarkerUnits(self.uglySide.call(
        'ritual_ZNK10QSvgMarker11markerUnitsEv',
    ))

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgMarker::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmarker.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgMarker::type() const
    ritual = 'ritual_ZNK10QSvgMarker4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSvgMarker4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

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

  @overload(
      QSvgNode, QRectF, QRectF, QPointF, QSvgSymbolLike.PreserveAspectRatios,
      QSvgSymbolLike.Overflow, Orientation, float, MarkerUnits,
  )
  @overload(
      NoneType, QRectF, QRectF, QPointF, QSvgSymbolLike.PreserveAspectRatios,
      QSvgSymbolLike.Overflow, Orientation, float, MarkerUnits,
  )
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QRectF,
      viewBox: QRectF,
      refP: QPointF,
      pAspectRatios: QSvgSymbolLike.PreserveAspectRatios,
      overflow: QSvgSymbolLike.Overflow,
      orientation: Orientation,
      orientationAngle: float,
      markerUnits: MarkerUnits,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgMarker::QSvgMarker(QSvgNode *parent,
    QRectF bounds, QRectF viewBox, QPointF refP,
    QSvgSymbolLike::PreserveAspectRatios pAspectRatios,
    QSvgSymbolLike::Overflow overflow, Orientation orientation, qreal
    orientationAngle, MarkerUnits markerUnits)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmarker.html#QSvgMarker

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    viewBox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    refP : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pAspectRatios : QSvgSymbolLike.PreserveAspectRatios
      Passed on as its number.

    overflow : QSvgSymbolLike.Overflow
      Passed on as its number.

    orientation : Orientation
      Passed on as its number.

    orientationAngle : float
      Passed on as it is.

    markerUnits : MarkerUnits
      Passed on as its number.
    """
    #  QSvgMarker::QSvgMarker(QSvgNode *parent, QRectF bounds, QRectF
    #      viewBox, QPointF refP, QSvgSymbolLike::PreserveAspectRatios
    #      pAspectRatios, QSvgSymbolLike::Overflow overflow, Orientation
    #      orientation, qreal orientationAngle, MarkerUnits markerUnits)
    self._noteCreation(QSvgMarker, lambda: Rituals.call(
        'ritual_ZN10QSvgMarkerC1EP8QSvgNode6QRectFS2_7QPointF6QFlagsIN14QSv'
        'gSymbolLike19PreserveAspectRatioEENS5_8OverflowENS_11OrientationEd'
        'NS_11MarkerUnitsE',
        self._addressOf(parent), self._valueOf(bounds),
        self._valueOf(viewBox), self._valueOf(refP, 'QPointF'),
        pAspectRatios.value, overflow.value, orientation.value,
        orientationAngle, markerUnits.value,
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

  @staticmethod
  def drawHelper(*__, **_) -> Never:
    """
    Qt's 'void QSvgMarker::drawHelper(const QSvgNode *node, QPainter *p,
    QSvgExtraStates &states, QRectF *boundingRect)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgMarker.drawHelper' has no cute function yet. Qt's 'void "
        "QSvgMarker::drawHelper(const QSvgNode *node, QPainter *p, "
        "QSvgExtraStates &states, QRectF *boundingRect)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def drawMarkersForNode(*__, **_) -> Never:
    """
    Qt's 'void QSvgMarker::drawMarkersForNode(QSvgNode *node, QPainter *p,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgMarker.drawMarkersForNode' has no cute function yet. Qt's "
        "'void QSvgMarker::drawMarkersForNode(QSvgNode *node, QPainter *p, "
        "QSvgExtraStates &states)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def markersBoundsForNode(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgMarker::markersBoundsForNode(const QSvgNode *node,
    QPainter *p, QSvgExtraStates &states)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSvgMarker.markersBoundsForNode' has no cute function yet. Qt's "
        "'QRectF QSvgMarker::markersBoundsForNode(const QSvgNode *node, "
        "QPainter *p, QSvgExtraStates &states)': takes a type Python has no "
        "way to hand over yet.")
