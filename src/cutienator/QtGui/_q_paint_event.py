"""
QPaintEvent binding of the Qt C++
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
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from . import QRegion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']


class QPaintEvent(QEvent):
  """
  The cute side of Qt's QPaintEvent: a plain Python object standing in front
  of one C++ QPaintEvent.

  It is built on the cute 'QEvent', as Qt's QPaintEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPaintEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'rect', 'region'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPaintEvent::~QPaintEvent()': the destructor: Python never removes
    a C++ QPaintEvent.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QPaintEvent is created at the first use, not by
    'QPaintEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEvent'

  #  A C++ QPaintEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QPaintEvent]:
    """
    Calls Qt's 'QPaintEvent *QPaintEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintevent.html#clone

    Returns
    -------

    Optional[QPaintEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEvent *QPaintEvent::clone() const
    ritual = 'ritual_ZNK11QPaintEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QPaintEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QPaintEvent._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'const QRect &QPaintEvent::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintevent.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  const QRect &QPaintEvent::rect() const
    address = self.uglySide.call('ritual_ZNK11QPaintEvent4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def region(self) -> QRegion:
    """
    Calls Qt's 'const QRegion &QPaintEvent::region() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintevent.html#region

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  const QRegion &QPaintEvent::region() const
    address = self.uglySide.call('ritual_ZNK11QPaintEvent6regionEv')
    from . import QRegion
    return QRegion._cuteOwning(address)

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

  @overload(QRegion)
  def __init__(self, paintRegion: QRegion) -> None:
    """
    Notes what was given, for Qt's 'QPaintEvent::QPaintEvent(const QRegion
    &paintRegion)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpaintevent.html#QPaintEvent

    Parameters
    ----------

    paintRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  QPaintEvent::QPaintEvent(const QRegion &paintRegion)
    self._noteCreation(QPaintEvent, lambda: Rituals.call(
        'ritual_ZN11QPaintEventC1ERK7QRegion', self._valueOf(paintRegion),
    ))

  @overload(QRect)
  def __init__(self, paintRect: QRect) -> None:
    """
    Notes what was given, for Qt's 'QPaintEvent::QPaintEvent(const QRect
    &paintRect)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpaintevent.html#QPaintEvent

    Parameters
    ----------

    paintRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  QPaintEvent::QPaintEvent(const QRect &paintRect)
    self._noteCreation(QPaintEvent, lambda: Rituals.call(
        'ritual_ZN11QPaintEventC1ERK5QRect', self._valueOf(paintRect),
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
