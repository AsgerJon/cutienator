"""
QAbstractScrollAreaScrollBarContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractScrollAreaScrollBarContainer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractScrollAreaScrollBarContainer(QWidget):
  """
  The cute side of Qt's QAbstractScrollAreaScrollBarContainer: a plain Python
  object standing in front of one C++ QAbstractScrollAreaScrollBarContainer.

  It is built on the cute 'QWidget', as Qt's
  QAbstractScrollAreaScrollBarContainer is built on Qt's QWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractScrollAreaScrollBarContainer that has a
  ritual and that Python can call so far, 3 names in all: 'addWidget',
  'widgets', 'scrollBarLayoutIndex'. It can be made from Python, in 1 way;
  see '__init__'.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QAbstractScrollAreaScrollBarContainer is created at the first
    use, not by 'QAbstractScrollAreaScrollBarContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractScrollAreaScrollBarContainer.
  - Qt tells when it has removed the C++
    QAbstractScrollAreaScrollBarContainer. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside QAbstractScrollAreaScrollBarContainer, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class LogicalPosition(CuteNum):
    """
    The enum 'QAbstractScrollAreaScrollBarContainer::LogicalPosition' of Qt,
    with the 2 names Qt gives in it.
    """

    LogicalLeft = Kee[int](1)
    LogicalRight = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractScrollAreaScrollBarContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scrollBarLayoutIndex(self) -> int:
    """
    Calls Qt's 'int
    QAbstractScrollAreaScrollBarContainer::scrollBarLayoutIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareascrollbarcontainer.html
    """
    #  int QAbstractScrollAreaScrollBarContainer::scrollBarLayoutIndex()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QAbstractScrollAreaScrollBarContainer20scrollBarLayout'
        'IndexEv',
    )

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

  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QWidget],
  ) -> None:
    """
    Notes what was given, for Qt's 'QAbstractScrollAreaScrollBarContainer::
    QAbstractScrollAreaScrollBarContainer(Qt::Orientation orientation,
    QWidget *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareascrollbarcontainer.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractScrollAreaScrollBarContainer::
    #      QAbstractScrollAreaScrollBarContainer(Qt::Orientation orientation,
    #      QWidget *parent)
    self._noteCreation(
        QAbstractScrollAreaScrollBarContainer, lambda: Rituals.call(
            'ritual_ZN37QAbstractScrollAreaScrollBarContainerC1EN2Qt11Orien'
            'tationEP7QWidget',
            orientation.value, self._addressOf(parent),
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

  @overload(QWidget, LogicalPosition)
  @overload(NoneType, LogicalPosition)
  def addWidget(
      self,
      widget: Optional[QWidget],
      position: LogicalPosition,
  ) -> None:
    """
    Calls Qt's 'void QAbstractScrollAreaScrollBarContainer::addWidget(QWidget
    *widget, LogicalPosition position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareascrollbarcontainer.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : LogicalPosition
      Passed on as its number.
    """
    #  void QAbstractScrollAreaScrollBarContainer::addWidget(QWidget *widget,
    #      LogicalPosition position)
    self.uglySide.call(
        'ritual_ZN37QAbstractScrollAreaScrollBarContainer9addWidgetEP7QWidg'
        'etNS_15LogicalPositionE',
        self._addressOf(widget), position.value,
    )

  @overload(LogicalPosition)
  def widgets(self, position: LogicalPosition) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    QAbstractScrollAreaScrollBarContainer::widgets(LogicalPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollareascrollbarcontainer.html#widgets

    Parameters
    ----------

    position : LogicalPosition
      Passed on as its number.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList
    #      QAbstractScrollAreaScrollBarContainer::widgets(LogicalPosition
    #      position)
    address = self.uglySide.call(
        'ritual_ZN37QAbstractScrollAreaScrollBarContainer7widgetsENS_15Logi'
        'calPositionE',
        position.value,
    )
    return QList[QWidget]._cuteOwning(address)
