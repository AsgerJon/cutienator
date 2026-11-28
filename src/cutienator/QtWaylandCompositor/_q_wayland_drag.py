"""
QWaylandDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylanddrag.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QWaylandSeat, QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandDrag(QObject):
  """
  The cute side of Qt's QWaylandDrag: a plain Python object standing in front
  of one C++ QWaylandDrag.

  It is built on the cute 'QObject', as Qt's QWaylandDrag is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandDrag that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'icon', 'origin', 'seat',
  'visible', 'dragMove', 'drop', 'cancelDrag', 'iconChanged', 'dragStarted'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandDrag::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandDrag::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandDragPrivate *QWaylandDrag::d_func()': gives
    'QWaylandDragPrivate', which has no cute class yet.
  - Qt's 'const QWaylandDragPrivate *QWaylandDrag::d_func() const': gives
    'QWaylandDragPrivate', which has no cute class yet.
  - Qt's 'void QWaylandDrag::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandDrag is created at the first use, not by
    'QWaylandDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandDrag.
  - Qt tells when it has removed the C++ QWaylandDrag. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QWaylandDrag::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandDrag::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QWaylandDrag2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandDrag'

  #  A C++ QWaylandDrag Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandDrag'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandDrag::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandDrag::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QWaylandDrag10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def icon(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandDrag::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#icon

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandDrag::icon() const
    address = self.uglySide.call('ritual_ZNK12QWaylandDrag4iconEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def origin(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandDrag::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#origin

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandDrag::origin() const
    address = self.uglySide.call('ritual_ZNK12QWaylandDrag6originEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def seat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandDrag::seat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#seat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandDrag::seat() const
    address = self.uglySide.call('ritual_ZNK12QWaylandDrag4seatEv')
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  def visible(self) -> bool:
    """
    Calls Qt's 'bool QWaylandDrag::visible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#visible
    """
    #  bool QWaylandDrag::visible() const
    return self.uglySide.call('ritual_ZNK12QWaylandDrag7visibleEv')

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

  @overload(QWaylandSeat)
  @overload(NoneType)
  def __init__(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Notes what was given, for Qt's 'QWaylandDrag::QWaylandDrag(QWaylandSeat
    *seat)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#QWaylandDrag

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandDrag::QWaylandDrag(QWaylandSeat *seat)
    self._noteCreation(QWaylandDrag, lambda: Rituals.call(
        'ritual_ZN12QWaylandDragC1EP12QWaylandSeat', self._addressOf(seat),
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

  @overload(QWaylandSurface, QPointF)
  @overload(NoneType, QPointF)
  def dragMove(
      self,
      target: Optional[QWaylandSurface],
      pos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWaylandDrag::dragMove(QWaylandSurface *target, const
    QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#dragMove

    Parameters
    ----------

    target : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWaylandDrag::dragMove(QWaylandSurface *target, const QPointF
    #      &pos)
    self.uglySide.call(
        'ritual_ZN12QWaylandDrag8dragMoveEP15QWaylandSurfaceRK7QPointF',
        self._addressOf(target), self._valueOf(pos, 'QPointF'),
    )

  def drop(self) -> None:
    """
    Calls Qt's 'void QWaylandDrag::drop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#drop
    """
    #  void QWaylandDrag::drop()
    self.uglySide.call('ritual_ZN12QWaylandDrag4dropEv')

  def cancelDrag(self) -> None:
    """
    Calls Qt's 'void QWaylandDrag::cancelDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#cancelDrag
    """
    #  void QWaylandDrag::cancelDrag()
    self.uglySide.call('ritual_ZN12QWaylandDrag10cancelDragEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandDrag::iconChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#iconChanged
    """
    #  void QWaylandDrag::iconChanged()
    self.uglySide.call('ritual_ZN12QWaylandDrag11iconChangedEv')

  def dragStarted(self) -> None:
    """
    Calls Qt's 'void QWaylandDrag::dragStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylanddrag.html#dragStarted
    """
    #  void QWaylandDrag::dragStarted()
    self.uglySide.call('ritual_ZN12QWaylandDrag11dragStartedEv')
