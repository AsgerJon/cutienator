"""
QScreenOrientationChangeEvent binding of the Qt C++
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
from ..QtCore import Qt, QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScreenOrientationChangeEvent(QEvent):
  """
  The cute side of Qt's QScreenOrientationChangeEvent: a plain Python object
  standing in front of one C++ QScreenOrientationChangeEvent.

  It is built on the cute 'QEvent', as Qt's QScreenOrientationChangeEvent is
  built on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScreenOrientationChangeEvent that has a ritual and
  that Python can call so far, 3 names in all: 'clone', 'screen',
  'orientation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScreenOrientationChangeEvent::QScreenOrientationChangeEvent(const
    QScreenOrientationChangeEvent &a0)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QScreenOrientationChangeEvent
    &QScreenOrientationChangeEvent::operator=(const
    QScreenOrientationChangeEvent &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QScreenOrientationChangeEvent::~QScreenOrientationChangeEvent()':
    the destructor: Python never removes a C++ QScreenOrientationChangeEvent.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QScreenOrientationChangeEvent is created at the first use, not by
    'QScreenOrientationChangeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScreenOrientationChangeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScreenOrientationChangeEvent'

  #  A C++ QScreenOrientationChangeEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScreenOrientationChangeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QScreenOrientationChangeEvent]:
    """
    Calls Qt's 'QScreenOrientationChangeEvent
    *QScreenOrientationChangeEvent::clone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreenorientationchangeevent.html#clone

    Returns
    -------

    Optional[QScreenOrientationChangeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreenOrientationChangeEvent *QScreenOrientationChangeEvent::clone()
    #      const
    ritual = 'ritual_ZNK29QScreenOrientationChangeEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QScreenOrientationChangeEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QScreenOrientationChangeEvent._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QScreenOrientationChangeEvent::screen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreenorientationchangeevent.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QScreenOrientationChangeEvent::screen() const
    address = self.uglySide.call(
        'ritual_ZNK29QScreenOrientationChangeEvent6screenEv',
    )
    from . import QScreen
    return QScreen._cuteAt(address)

  def orientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation
    QScreenOrientationChangeEvent::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreenorientationchangeevent.html#orientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QScreenOrientationChangeEvent::orientation()
    #      const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK29QScreenOrientationChangeEvent11orientationEv',
    ))

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

  @overload(QScreen, Qt.ScreenOrientation)
  @overload(NoneType, Qt.ScreenOrientation)
  def __init__(
      self,
      screen: Optional[QScreen],
      orientation: Qt.ScreenOrientation,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScreenOrientationChangeEvent::QScreenOrientationChangeEvent(QScreen
    *screen, Qt::ScreenOrientation orientation)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreenorientationchangeevent.html

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  QScreenOrientationChangeEvent::QScreenOrientationChangeEvent(QScreen
    #      *screen, Qt::ScreenOrientation orientation)
    self._noteCreation(QScreenOrientationChangeEvent, lambda: Rituals.call(
        'ritual_ZN29QScreenOrientationChangeEventC1EP7QScreenN2Qt17ScreenOr'
        'ientationE',
        self._addressOf(screen), orientation.value,
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
