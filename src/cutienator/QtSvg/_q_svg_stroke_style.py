"""
QSvgStrokeStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgStrokeStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QBrush, QPen
  from . import QSvgPaintServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class QSvgStrokeStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgStrokeStyle: a plain Python object standing in
  front of one C++ QSvgStrokeStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgStrokeStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgStrokeStyle around as a copy, so every C++ QSvgStrokeStyle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgStrokeStyle that has a ritual and that Python
  can call so far, 15 names in all: 'type', 'setStroke', 'setDashArrayNone',
  'setDashOffset', 'setLineCap', 'setLineJoin', 'setMiterLimit',
  'setOpacity', 'setWidth', 'width', 'setVectorEffect', 'paintServer',
  'setPaintStyleId', 'paintStyleId', 'stroke'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgStrokeStyle::~QSvgStrokeStyle()': the destructor: Python
    removes its C++ QSvgStrokeStyle by it, and has no other use for it.
  - Qt's 'void QSvgStrokeStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgStrokeStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgStrokeStyle::setPaintServer(QSvgPaintServerSharedPtr
    paintServer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgStrokeStyle::setDashArray(const QList<qreal> &dashes)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgStrokeStyle is created at the first use, not by
    'QSvgStrokeStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgStrokeStyle back gives a copy the ritual made for
    Python, in a new cute QSvgStrokeStyle.
  - Each name of Qt's QSvgStrokeStyle that has no cute function yet,
    'setDashArray', 'setPaintServer', holds a function that raises
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
  __qt_class__ = 'QSvgStrokeStyle'

  #  A C++ QSvgStrokeStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgStrokeStyle'

  #  Qt's '~QSvgStrokeStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgStrokeStyle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSvgStrokeStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgStrokeStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgStrokeStyle::type() const
    ritual = 'ritual_ZNK15QSvgStrokeStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgStrokeStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def paintServer(self) -> Optional[QSvgPaintServer]:
    """
    Calls Qt's 'QSvgPaintServer *QSvgStrokeStyle::paintServer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#paintServer

    Returns
    -------

    Optional[QSvgPaintServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgPaintServer *QSvgStrokeStyle::paintServer() const
    address = self.uglySide.call(
        'ritual_ZNK15QSvgStrokeStyle11paintServerEv',
    )
    from . import QSvgPaintServer
    return QSvgPaintServer._cuteAt(address)

  def paintStyleId(self) -> str:
    """
    Calls Qt's 'QString QSvgStrokeStyle::paintStyleId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#paintStyleId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgStrokeStyle::paintStyleId() const
    return self.uglySide.call('ritual_ZNK15QSvgStrokeStyle12paintStyleIdEv')

  def stroke(self) -> QPen:
    """
    Calls Qt's 'QPen QSvgStrokeStyle::stroke() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#stroke

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QSvgStrokeStyle::stroke() const
    address = self.uglySide.call('ritual_ZNK15QSvgStrokeStyle6strokeEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBrush)
  def setStroke(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setStroke(QBrush brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setStroke

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QSvgStrokeStyle::setStroke(QBrush brush)
    self.uglySide.call(
        'ritual_ZN15QSvgStrokeStyle9setStrokeE6QBrush', self._valueOf(brush),
    )

  def setDashArrayNone(self) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setDashArrayNone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstrokestyle.html#setDashArrayNone
    """
    #  void QSvgStrokeStyle::setDashArrayNone()
    self.uglySide.call('ritual_ZN15QSvgStrokeStyle16setDashArrayNoneEv')

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setDashOffset(qreal offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QSvgStrokeStyle::setDashOffset(qreal offset)
    self.uglySide.call('ritual_ZN15QSvgStrokeStyle13setDashOffsetEd', offset)

  @overload(Qt.PenCapStyle)
  def setLineCap(self, cap: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setLineCap(Qt::PenCapStyle cap)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setLineCap

    Parameters
    ----------

    cap : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QSvgStrokeStyle::setLineCap(Qt::PenCapStyle cap)
    self.uglySide.call(
        'ritual_ZN15QSvgStrokeStyle10setLineCapEN2Qt11PenCapStyleE',
        cap.value,
    )

  @overload(Qt.PenJoinStyle)
  def setLineJoin(self, join: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setLineJoin(Qt::PenJoinStyle join)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setLineJoin

    Parameters
    ----------

    join : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QSvgStrokeStyle::setLineJoin(Qt::PenJoinStyle join)
    self.uglySide.call(
        'ritual_ZN15QSvgStrokeStyle11setLineJoinEN2Qt12PenJoinStyleE',
        join.value,
    )

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setMiterLimit(qreal limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QSvgStrokeStyle::setMiterLimit(qreal limit)
    self.uglySide.call('ritual_ZN15QSvgStrokeStyle13setMiterLimitEd', limit)

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSvgStrokeStyle::setOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN15QSvgStrokeStyle10setOpacityEd', opacity)

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QSvgStrokeStyle::setWidth(qreal width)
    self.uglySide.call('ritual_ZN15QSvgStrokeStyle8setWidthEd', width)

  @overload(bool)
  def setVectorEffect(self, nonScalingStroke: bool) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setVectorEffect(bool
    nonScalingStroke)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstrokestyle.html#setVectorEffect

    Parameters
    ----------

    nonScalingStroke : bool
      Passed on as it is.
    """
    #  void QSvgStrokeStyle::setVectorEffect(bool nonScalingStroke)
    self.uglySide.call(
        'ritual_ZN15QSvgStrokeStyle15setVectorEffectEb', nonScalingStroke,
    )

  @overload(str)
  def setPaintStyleId(self, Id: str) -> None:
    """
    Calls Qt's 'void QSvgStrokeStyle::setPaintStyleId(const QString &Id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstrokestyle.html#setPaintStyleId

    Parameters
    ----------

    Id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgStrokeStyle::setPaintStyleId(const QString &Id)
    self.uglySide.call(
        'ritual_ZN15QSvgStrokeStyle15setPaintStyleIdERK7QString', Id,
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
    Notes what was given, for Qt's 'QSvgStrokeStyle::QSvgStrokeStyle()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstrokestyle.html#QSvgStrokeStyle
    """
    #  QSvgStrokeStyle::QSvgStrokeStyle()
    self._noteCreation(QSvgStrokeStyle, lambda: Rituals.call(
        'ritual_ZN15QSvgStrokeStyleC1Ev',
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

  def width(self) -> float:
    """
    Calls Qt's 'qreal QSvgStrokeStyle::width()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstrokestyle.html#width
    """
    #  qreal QSvgStrokeStyle::width()
    return self.uglySide.call('ritual_ZN15QSvgStrokeStyle5widthEv')

  @staticmethod
  def setDashArray(*__, **_) -> Never:
    """
    Qt's 'void QSvgStrokeStyle::setDashArray(const QList<qreal> &dashes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgStrokeStyle.setDashArray' has no cute function yet. Qt's "
        "'void QSvgStrokeStyle::setDashArray(const QList<qreal> &dashes)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPaintServer(*__, **_) -> Never:
    """
    Qt's 'void QSvgStrokeStyle::setPaintServer(QSvgPaintServerSharedPtr
    paintServer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgStrokeStyle.setPaintServer' has no cute function yet. Qt's "
        "'void QSvgStrokeStyle::setPaintServer(QSvgPaintServerSharedPtr "
        "paintServer)': takes a type Python has no way to hand over yet.")
