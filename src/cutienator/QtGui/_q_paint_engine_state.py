"""
QPaintEngineState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import Qt
from . import QPaintEngine, QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from . import QBrush, QFont, QPainterPath, QPen, QRegion, QTransform


class QPaintEngineState(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPaintEngineState: a plain Python object standing in
  front of one C++ QPaintEngineState.

  C++ hands a QPaintEngineState around as a copy, so every C++
  QPaintEngineState behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPaintEngineState that has a ritual and that Python
  can call so far, 18 names in all: 'state', 'pen', 'brush', 'brushOrigin',
  'backgroundBrush', 'backgroundMode', 'font', 'transform', 'clipOperation',
  'clipRegion', 'clipPath', 'isClipEnabled', 'renderHints',
  'compositionMode', 'opacity', 'painter', 'brushNeedsResolving',
  'penNeedsResolving'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPaintEngineState::~QPaintEngineState()': the destructor: Python
    removes its C++ QPaintEngineState by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPaintEngineState is created at the first use, not by
    'QPaintEngineState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPaintEngineState back gives a copy the ritual made
    for Python, in a new cute QPaintEngineState.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEngineState'

  #  Qt's '~QPaintEngineState()'. Naming it makes this a value class: Python
  #  owns every C++ QPaintEngineState behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QPaintEngineStateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> QPaintEngine.DirtyFlags:
    """
    Calls Qt's 'QPaintEngine::DirtyFlags QPaintEngineState::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#state

    Returns
    -------

    QPaintEngine.DirtyFlags
      The value standing for the combination Qt gave back.
    """
    #  QPaintEngine::DirtyFlags QPaintEngineState::state() const
    return QPaintEngine.DirtyFlags(self.uglySide.call(
        'ritual_ZNK17QPaintEngineState5stateEv',
    ))

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QPaintEngineState::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QPaintEngineState::pen() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState3penEv')
    from . import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QPaintEngineState::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QPaintEngineState::brush() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState5brushEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def brushOrigin(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPaintEngineState::brushOrigin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#brushOrigin

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPaintEngineState::brushOrigin() const
    address = self.uglySide.call(
        'ritual_ZNK17QPaintEngineState11brushOriginEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def backgroundBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QPaintEngineState::backgroundBrush() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#backgroundBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QPaintEngineState::backgroundBrush() const
    address = self.uglySide.call(
        'ritual_ZNK17QPaintEngineState15backgroundBrushEv',
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def backgroundMode(self) -> Qt.BGMode:
    """
    Calls Qt's 'Qt::BGMode QPaintEngineState::backgroundMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#backgroundMode

    Returns
    -------

    Qt.BGMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.BGMode(number)' gives.
    """
    #  Qt::BGMode QPaintEngineState::backgroundMode() const
    return Qt.BGMode(self.uglySide.call(
        'ritual_ZNK17QPaintEngineState14backgroundModeEv',
    ))

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QPaintEngineState::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QPaintEngineState::font() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QPaintEngineState::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPaintEngineState::transform() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState9transformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def clipOperation(self) -> Qt.ClipOperation:
    """
    Calls Qt's 'Qt::ClipOperation QPaintEngineState::clipOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#clipOperation

    Returns
    -------

    Qt.ClipOperation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ClipOperation(number)'
      gives.
    """
    #  Qt::ClipOperation QPaintEngineState::clipOperation() const
    return Qt.ClipOperation(self.uglySide.call(
        'ritual_ZNK17QPaintEngineState13clipOperationEv',
    ))

  def clipRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QPaintEngineState::clipRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#clipRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QPaintEngineState::clipRegion() const
    address = self.uglySide.call(
        'ritual_ZNK17QPaintEngineState10clipRegionEv',
    )
    from . import QRegion
    return QRegion._cuteOwning(address)

  def clipPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPaintEngineState::clipPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#clipPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPaintEngineState::clipPath() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState8clipPathEv')
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  def isClipEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngineState::isClipEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#isClipEnabled
    """
    #  bool QPaintEngineState::isClipEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QPaintEngineState13isClipEnabledEv',
    )

  def renderHints(self) -> QPainter.RenderHints:
    """
    Calls Qt's 'QPainter::RenderHints QPaintEngineState::renderHints()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#renderHints

    Returns
    -------

    QPainter.RenderHints
      The value standing for the combination Qt gave back.
    """
    #  QPainter::RenderHints QPaintEngineState::renderHints() const
    return QPainter.RenderHints(self.uglySide.call(
        'ritual_ZNK17QPaintEngineState11renderHintsEv',
    ))

  def compositionMode(self) -> QPainter.CompositionMode:
    """
    Calls Qt's 'QPainter::CompositionMode
    QPaintEngineState::compositionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#compositionMode

    Returns
    -------

    QPainter.CompositionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPainter.CompositionMode(number)' gives.
    """
    #  QPainter::CompositionMode QPaintEngineState::compositionMode() const
    return QPainter.CompositionMode(self.uglySide.call(
        'ritual_ZNK17QPaintEngineState15compositionModeEv',
    ))

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QPaintEngineState::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#opacity
    """
    #  qreal QPaintEngineState::opacity() const
    return self.uglySide.call('ritual_ZNK17QPaintEngineState7opacityEv')

  def painter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QPaintEngineState::painter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintenginestate.html#painter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QPaintEngineState::painter() const
    address = self.uglySide.call('ritual_ZNK17QPaintEngineState7painterEv')
    return QPainter._cuteAt(address)

  def brushNeedsResolving(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngineState::brushNeedsResolving() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#brushNeedsResolving
    """
    #  bool QPaintEngineState::brushNeedsResolving() const
    return self.uglySide.call(
        'ritual_ZNK17QPaintEngineState19brushNeedsResolvingEv',
    )

  def penNeedsResolving(self) -> bool:
    """
    Calls Qt's 'bool QPaintEngineState::penNeedsResolving() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintenginestate.html#penNeedsResolving
    """
    #  bool QPaintEngineState::penNeedsResolving() const
    return self.uglySide.call(
        'ritual_ZNK17QPaintEngineState17penNeedsResolvingEv',
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
