"""
QQuickPressHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpresshandler_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPressHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTimerEvent
  from ..QtGui import QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPressHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickPressHandler: a plain Python object standing in
  front of one C++ QQuickPressHandler.

  What exists
  -----------

  Every function of Qt's QQuickPressHandler that has a ritual and that Python
  can call so far, 6 names in all: 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'timerEvent', 'clearDelayedMouseEvent', 'isActive'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QQuickPressHandler::isSignalConnected(QQuickItem *item, const
    char *signalName, int &signalIndex)': takes a number to change where it
    is.

  What to expect
  --------------

  - The C++ QQuickPressHandler is created at the first use, not by
    'QQuickPressHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPressHandler.
  - Each name of Qt's QQuickPressHandler that has no cute function yet,
    'isSignalConnected', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPressHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPressHandler::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpresshandler.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPressHandler::mousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickPressHandler15mousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPressHandler::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpresshandler.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPressHandler::mouseMoveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickPressHandler14mouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPressHandler::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpresshandler.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPressHandler::mouseReleaseEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickPressHandler17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickPressHandler::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpresshandler.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPressHandler::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickPressHandler10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  def clearDelayedMouseEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPressHandler::clearDelayedMouseEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpresshandler.html#clearDelayedMouseEvent
    """
    #  void QQuickPressHandler::clearDelayedMouseEvent()
    self.uglySide.call(
        'ritual_ZN18QQuickPressHandler22clearDelayedMouseEventEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickPressHandler::isActive()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpresshandler.html#isActive
    """
    #  bool QQuickPressHandler::isActive()
    return self.uglySide.call('ritual_ZN18QQuickPressHandler8isActiveEv')

  @staticmethod
  def isSignalConnected(*__, **_) -> Never:
    """
    Qt's 'bool QQuickPressHandler::isSignalConnected(QQuickItem *item, const
    char *signalName, int &signalIndex)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QQuickPressHandler.isSignalConnected' has no cute function yet. "
        "Qt's 'bool QQuickPressHandler::isSignalConnected(QQuickItem *item, "
        "const char *signalName, int &signalIndex)': takes a number to "
        "change where it is.")
