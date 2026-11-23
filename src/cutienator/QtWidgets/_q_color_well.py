"""
QColorWell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcolorwell_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QColorWell to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWellArray

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QMouseEvent, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColorWell(QWellArray):
  """
  The cute side of Qt's QColorWell: a plain Python object standing in front
  of one C++ QColorWell.

  It is built on the cute 'QWellArray', as Qt's QColorWell is built on Qt's
  QWellArray, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QColorWell that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'paintCellContents',
  'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'dragEnterEvent',
  'dragLeaveEvent', 'dragMoveEvent', 'dropEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found; 1 leans on
  'QColorWell; 1 leans on 'QWellArray.

  What to expect
  --------------

  - The C++ QColorWell is created at the first use, not by 'QColorWell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorWell.
  - Qt tells when it has removed the C++ QColorWell. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorWell'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QColorWell::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QColorWell::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QColorWell10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QPainter, int, int, QRect)
  @overload(NoneType, int, int, QRect)
  def paintCellContents(
      self,
      a0: Optional[QPainter],
      row: int,
      col: int,
      a3: QRect,
  ) -> None:
    """
    Calls Qt's 'void QColorWell::paintCellContents(QPainter *a0, int row, int
    col, const QRect &a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#paintCellContents

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    a3 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QColorWell::paintCellContents(QPainter *a0, int row, int col,
    #      const QRect &a3)
    ritual = 'ritual_ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRect'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QColorWell17paintCellContentsEP8QPainteriiRK5QRec'
          't')
    self.uglySide.call(
        ritual, self._addressOf(a0), row, col, self._valueOf(a3),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::mousePressEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN10QColorWell15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::mouseMoveEvent(QMouseEvent *e)
    ritual = 'ritual_ZN10QColorWell14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::mouseReleaseEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::mouseReleaseEvent(QMouseEvent *e)
    ritual = 'ritual_ZN10QColorWell17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, e: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::dragEnterEvent(QDragEnterEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#dragEnterEvent

    Parameters
    ----------

    e : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::dragEnterEvent(QDragEnterEvent *e)
    ritual = 'ritual_ZN10QColorWell14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell14dragEnterEventEP15QDragEnterEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::dragLeaveEvent(QDragLeaveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#dragLeaveEvent

    Parameters
    ----------

    e : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::dragLeaveEvent(QDragLeaveEvent *e)
    ritual = 'ritual_ZN10QColorWell14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell14dragLeaveEventEP15QDragLeaveEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::dragMoveEvent(QDragMoveEvent *e)
    ritual = 'ritual_ZN10QColorWell13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QColorWell13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QColorWell::dropEvent(QDropEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorwell.html#dropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColorWell::dropEvent(QDropEvent *e)
    self.uglySide.call(
        'ritual_ZN10QColorWell9dropEventEP10QDropEvent', self._addressOf(e),
    )
