"""
QResizeEvent binding of the Qt C++
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

  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QResizeEvent(QEvent):
  """
  The cute side of Qt's QResizeEvent: a plain Python object standing in front
  of one C++ QResizeEvent.

  It is built on the cute 'QEvent', as Qt's QResizeEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QResizeEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'size', 'oldSize'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QResizeEvent::~QResizeEvent()': the destructor: Python never
    removes a C++ QResizeEvent.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QResizeEvent is created at the first use, not by
    'QResizeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QResizeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QResizeEvent'

  #  A C++ QResizeEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QResizeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QResizeEvent]:
    """
    Calls Qt's 'QResizeEvent *QResizeEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresizeevent.html#clone

    Returns
    -------

    Optional[QResizeEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QResizeEvent *QResizeEvent::clone() const
    ritual = 'ritual_ZNK12QResizeEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QResizeEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QResizeEvent._cuteAt(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'const QSize &QResizeEvent::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresizeevent.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  const QSize &QResizeEvent::size() const
    address = self.uglySide.call('ritual_ZNK12QResizeEvent4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def oldSize(self) -> QSize:
    """
    Calls Qt's 'const QSize &QResizeEvent::oldSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresizeevent.html#oldSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  const QSize &QResizeEvent::oldSize() const
    address = self.uglySide.call('ritual_ZNK12QResizeEvent7oldSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload(QSize, QSize)
  def __init__(self, size: QSize, oldSize: QSize) -> None:
    """
    Notes what was given, for Qt's 'QResizeEvent::QResizeEvent(const QSize
    &size, const QSize &oldSize)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qresizeevent.html#QResizeEvent

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    oldSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QResizeEvent::QResizeEvent(const QSize &size, const QSize &oldSize)
    self._noteCreation(QResizeEvent, lambda: Rituals.call(
        'ritual_ZN12QResizeEventC1ERK5QSizeS2_',
        self._valueOf(size), self._valueOf(oldSize),
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
