"""
QAccessibleViewportInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QAccessibleViewportInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleViewportInterface: a plain Python object
  standing in front of one C++ QAccessibleViewportInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleViewportInterface that has a ritual and
  that Python can call so far, 5 names in all: 'contentSize', 'position',
  'viewportSize', 'isIndexed', 'setPosition'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleViewportInterface::~QAccessibleViewportInterface()': the
    destructor: Python never removes a C++ QAccessibleViewportInterface.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one.

  What to expect
  --------------

  - The C++ QAccessibleViewportInterface is created at the first use, not by
    'QAccessibleViewportInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleViewportInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleViewportInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleViewportInterface::contentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#contentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleViewportInterface::contentSize() const
    address = self.uglySide.call(
        'ritual_ZNK28QAccessibleViewportInterface11contentSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QAccessibleViewportInterface::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QAccessibleViewportInterface::position() const
    address = self.uglySide.call(
        'ritual_ZNK28QAccessibleViewportInterface8positionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def viewportSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleViewportInterface::viewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#viewportSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleViewportInterface::viewportSize() const
    address = self.uglySide.call(
        'ritual_ZNK28QAccessibleViewportInterface12viewportSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isIndexed(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleViewportInterface::isIndexed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#isIndexed
    """
    #  bool QAccessibleViewportInterface::isIndexed() const
    return self.uglySide.call(
        'ritual_ZNK28QAccessibleViewportInterface9isIndexedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPosition(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QAccessibleViewportInterface::setPosition(QPointF
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#setPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAccessibleViewportInterface::setPosition(QPointF position)
    self.uglySide.call(
        'ritual_ZN28QAccessibleViewportInterface11setPositionE7QPointF',
        self._valueOf(position),
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
