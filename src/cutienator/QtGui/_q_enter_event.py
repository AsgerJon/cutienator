"""
QEnterEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSinglePointEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QPointF
  from . import QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEnterEvent(QSinglePointEvent):
  """
  The cute side of Qt's QEnterEvent: a plain Python object standing in front
  of one C++ QEnterEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QEnterEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEnterEvent that has a ritual and that Python can
  call so far, 10 names in all: 'clone', 'pos', 'globalPos', 'x', 'y',
  'globalX', 'globalY', 'localPos', 'windowPos', 'screenPos'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEnterEvent::QEnterEvent(const QEnterEvent &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QEnterEvent &QEnterEvent::operator=(const QEnterEvent &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QEnterEvent::~QEnterEvent()': the destructor: Python never removes
    a C++ QEnterEvent.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QEnterEvent is created at the first use, not by
    'QEnterEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEnterEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEnterEvent'

  #  A C++ QEnterEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QEnterEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QEnterEvent]:
    """
    Calls Qt's 'QEnterEvent *QEnterEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#clone

    Returns
    -------

    Optional[QEnterEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEnterEvent *QEnterEvent::clone() const
    ritual = 'ritual_ZNK11QEnterEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QEnterEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QEnterEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QEnterEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QEnterEvent::pos() const
    address = self.uglySide.call('ritual_ZNK11QEnterEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QEnterEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QEnterEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK11QEnterEvent9globalPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QEnterEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#x
    """
    #  int QEnterEvent::x() const
    return self.uglySide.call('ritual_ZNK11QEnterEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QEnterEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#y
    """
    #  int QEnterEvent::y() const
    return self.uglySide.call('ritual_ZNK11QEnterEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QEnterEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#globalX
    """
    #  int QEnterEvent::globalX() const
    return self.uglySide.call('ritual_ZNK11QEnterEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QEnterEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#globalY
    """
    #  int QEnterEvent::globalY() const
    return self.uglySide.call('ritual_ZNK11QEnterEvent7globalYEv')

  def localPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEnterEvent::localPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#localPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEnterEvent::localPos() const
    address = self.uglySide.call('ritual_ZNK11QEnterEvent8localPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def windowPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEnterEvent::windowPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#windowPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEnterEvent::windowPos() const
    address = self.uglySide.call('ritual_ZNK11QEnterEvent9windowPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QEnterEvent::screenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#screenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QEnterEvent::screenPos() const
    address = self.uglySide.call('ritual_ZNK11QEnterEvent9screenPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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

  @overload(QPointF, QPointF, QPointF)
  @overload(QPointF, QPointF, QPointF, QPointingDevice)
  @overload(QPointF, QPointF, QPointF, NoneType)
  def __init__(
      self,
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      device: Optional[QPointingDevice] = ...,
  ) -> None:
    """
    Notes what was given, for Qt's 'QEnterEvent::QEnterEvent(const QPointF
    &localPos, const QPointF &scenePos, const QPointF &globalPos, const
    QPointingDevice *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qenterevent.html#QEnterEvent

    Parameters
    ----------

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: what
      'QPointingDevice.primaryPointingDevice()' gives is then passed on.
    """
    #  QEnterEvent::QEnterEvent(const QPointF &localPos, const QPointF
    #      &scenePos, const QPointF &globalPos, const QPointingDevice
    #      *device)
    if device is ...:
      from . import QPointingDevice
      device = QPointingDevice.primaryPointingDevice()
    self._noteCreation(QEnterEvent, lambda: Rituals.call(
        'ritual_ZN11QEnterEventC1ERK7QPointFS2_S2_PK15QPointingDevice',
        self._valueOf(localPos, 'QPointF'), self._valueOf(scenePos,
        'QPointF'), self._valueOf(globalPos, 'QPointF'),
        self._addressOf(device),
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
