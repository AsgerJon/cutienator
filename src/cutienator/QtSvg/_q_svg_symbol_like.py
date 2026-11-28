"""
QSvgSymbolLike binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgSymbolLike to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainter, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgSymbolLike(QSvgStructureNode):
  """
  The cute side of Qt's QSvgSymbolLike: a plain Python object standing in
  front of one C++ QSvgSymbolLike.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgSymbolLike is
  built on Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgSymbolLike that has a ritual and that Python can
  call so far, 9 names in all: 'requiresGroupRendering', 'viewBox', 'rect',
  'refP', 'aspectRatioTransform', 'clipRect', 'overflow',
  'preserveAspectRatios', 'setPainterToRectAndAdjustment'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgSymbolLike::~QSvgSymbolLike()': the destructor: Python never
    removes a C++ QSvgSymbolLike.
  - Qt's 'void QSvgSymbolLike::drawCommand(QPainter *a0, QSvgExtraStates
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgSymbolLike::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgSymbolLike is created at the first use, not by
    'QSvgSymbolLike(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgSymbolLike.
  """

  #  The enums Qt writes inside QSvgSymbolLike, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Overflow(CuteNum, scoped=True):
    """
    The enum 'QSvgSymbolLike::Overflow' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Visible = Kee[int](0)
    Hidden = Kee[int](1)
    Scroll = Kee[int](0)
    Auto = Kee[int](0)

  class PreserveAspectRatio(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QSvgSymbolLike::PreserveAspectRatio' of Qt, with the 13
    names Qt gives in it. Qt names the type of its combinations
    'QSvgSymbolLike::PreserveAspectRatios'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    xMin = 0x1
    xMid = 0x2
    xMax = 0x3
    yMin = 0x4
    yMid = 0x8
    yMax = 0xc
    meet = 0x10
    slice = 0x20
    xMask = 0x3
    yMask = 0xc
    xyMask = 0xf
    meetSliceMask = 0x30

  PreserveAspectRatios = PreserveAspectRatio

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgSymbolLike'

  #  A C++ QSvgSymbolLike Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgSymbolLike'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def requiresGroupRendering(self) -> bool:
    """
    Calls Qt's 'bool QSvgSymbolLike::requiresGroupRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgsymbollike.html#requiresGroupRendering
    """
    #  bool QSvgSymbolLike::requiresGroupRendering() const
    ritual = 'ritual_ZNK14QSvgSymbolLike22requiresGroupRenderingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSvgSymbolLike22requiresGroupRenderingEv'
    return self.uglySide.call(ritual)

  def viewBox(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgSymbolLike::viewBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#viewBox

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgSymbolLike::viewBox() const
    address = self.uglySide.call('ritual_ZNK14QSvgSymbolLike7viewBoxEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgSymbolLike::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgSymbolLike::rect() const
    address = self.uglySide.call('ritual_ZNK14QSvgSymbolLike4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def refP(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgSymbolLike::refP() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#refP

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgSymbolLike::refP() const
    address = self.uglySide.call('ritual_ZNK14QSvgSymbolLike4refPEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def aspectRatioTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QSvgSymbolLike::aspectRatioTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgsymbollike.html#aspectRatioTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QSvgSymbolLike::aspectRatioTransform() const
    address = self.uglySide.call(
        'ritual_ZNK14QSvgSymbolLike20aspectRatioTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgSymbolLike::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgSymbolLike::clipRect() const
    address = self.uglySide.call('ritual_ZNK14QSvgSymbolLike8clipRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def overflow(self) -> Overflow:
    """
    Calls Qt's 'Overflow QSvgSymbolLike::overflow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#overflow

    Returns
    -------

    Overflow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Overflow(number)' gives.
    """
    #  Overflow QSvgSymbolLike::overflow() const
    return QSvgSymbolLike.Overflow(self.uglySide.call(
        'ritual_ZNK14QSvgSymbolLike8overflowEv',
    ))

  def preserveAspectRatios(self) -> PreserveAspectRatios:
    """
    Calls Qt's 'PreserveAspectRatios QSvgSymbolLike::preserveAspectRatios()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgsymbollike.html#preserveAspectRatios

    Returns
    -------

    PreserveAspectRatios
      The value standing for the combination Qt gave back.
    """
    #  PreserveAspectRatios QSvgSymbolLike::preserveAspectRatios() const
    return QSvgSymbolLike.PreserveAspectRatios(self.uglySide.call(
        'ritual_ZNK14QSvgSymbolLike20preserveAspectRatiosEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainter)
  @overload(NoneType)
  def setPainterToRectAndAdjustment(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSvgSymbolLike::setPainterToRectAndAdjustment(QPainter
    *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgsymbollike.html#setPainterToRectAndAdjustment

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgSymbolLike::setPainterToRectAndAdjustment(QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK14QSvgSymbolLike29setPainterToRectAndAdjustmentEP8QPaint'
        'er',
        self._addressOf(p),
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

  @overload(
      QSvgNode, QRectF, QRectF, QPointF, PreserveAspectRatios, Overflow,
  )
  @overload(
      NoneType, QRectF, QRectF, QPointF, PreserveAspectRatios, Overflow,
  )
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QRectF,
      viewBox: QRectF,
      refP: QPointF,
      pAspectRatios: PreserveAspectRatios,
      overflow: Overflow,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgSymbolLike::QSvgSymbolLike(QSvgNode
    *parent, QRectF bounds, QRectF viewBox, QPointF refP,
    QSvgSymbolLike::PreserveAspectRatios pAspectRatios,
    QSvgSymbolLike::Overflow overflow)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbollike.html#QSvgSymbolLike

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

    pAspectRatios : PreserveAspectRatios
      Passed on as its number.

    overflow : Overflow
      Passed on as its number.
    """
    #  QSvgSymbolLike::QSvgSymbolLike(QSvgNode *parent, QRectF bounds, QRectF
    #      viewBox, QPointF refP, QSvgSymbolLike::PreserveAspectRatios
    #      pAspectRatios, QSvgSymbolLike::Overflow overflow)
    self._noteCreation(QSvgSymbolLike, lambda: Rituals.call(
        'ritual_ZN14QSvgSymbolLikeC1EP8QSvgNode6QRectFS2_7QPointF6QFlagsINS'
        '_19PreserveAspectRatioEENS_8OverflowE',
        self._addressOf(parent), self._valueOf(bounds),
        self._valueOf(viewBox), self._valueOf(refP, 'QPointF'),
        pAspectRatios.value, overflow.value,
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
