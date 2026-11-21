"""
QGraphicsSceneResizeEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGraphicsSceneEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']


class QGraphicsSceneResizeEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneResizeEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneResizeEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneResizeEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneResizeEvent that has a ritual and that
  Python can call so far, 4 names in all: 'oldSize', 'setOldSize', 'newSize',
  'setNewSize'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneResizeEvent::~QGraphicsSceneResizeEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneResizeEvent.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 private; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneResizeEvent is created at the first use, not by
    'QGraphicsSceneResizeEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneResizeEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneResizeEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def oldSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsSceneResizeEvent::oldSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneresizeevent.html#oldSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsSceneResizeEvent::oldSize() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsSceneResizeEvent7oldSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def newSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsSceneResizeEvent::newSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneresizeevent.html#newSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsSceneResizeEvent::newSize() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsSceneResizeEvent7newSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  def setOldSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneResizeEvent::setOldSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneresizeevent.html#setOldSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsSceneResizeEvent::setOldSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN25QGraphicsSceneResizeEvent10setOldSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(QSizeF)
  def setNewSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneResizeEvent::setNewSize(const QSizeF
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneresizeevent.html#setNewSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsSceneResizeEvent::setNewSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN25QGraphicsSceneResizeEvent10setNewSizeERK6QSizeF',
        self._valueOf(size),
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
    'QGraphicsSceneResizeEvent::QGraphicsSceneResizeEvent()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssceneresizeevent.html
    """
    #  QGraphicsSceneResizeEvent::QGraphicsSceneResizeEvent()
    self._noteCreation(QGraphicsSceneResizeEvent, lambda: Rituals.call(
        'ritual_ZN25QGraphicsSceneResizeEventC1Ev',
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
