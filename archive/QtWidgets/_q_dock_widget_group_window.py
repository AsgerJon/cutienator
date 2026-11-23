"""
QDockWidgetGroupWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDockWidgetGroupWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChildEvent, QEvent, QMetaObject
  from . import QDockWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetGroupWindow(QWidget):
  """
  The cute side of Qt's QDockWidgetGroupWindow: a plain Python object
  standing in front of one C++ QDockWidgetGroupWindow.

  It is built on the cute 'QWidget', as Qt's QDockWidgetGroupWindow is built
  on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetGroupWindow that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject',
  'hasVisibleDockWidgets', 'childEvent', 'dockWidgets', 'eventFilter'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  25 of the 30 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 leans on
  'QDockWidgetGroupWindow; 4 takes or gives a type that cannot be passed yet;
  3 leans on 'QDockAreaLayoutInfo; 1 a template; 1 declared and nowhere to be
  found; 1 a signal; 1 leans on 'vtable for QDockWidgetGroupWindow', which
  Qt's library does not offer and Qt's source has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QDockWidgetGroupWindow is created at the first use, not by
    'QDockWidgetGroupWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetGroupWindow.
  - Qt tells when it has removed the C++ QDockWidgetGroupWindow. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidgetGroupWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDockWidgetGroupWindow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDockWidgetGroupWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasVisibleDockWidgets(self) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#hasVisibleDockWidgets
    """
    #  bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
    return self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv',
    )

  def dockWidgets(self) -> QList[QDockWidget]:
    """
    Calls Qt's 'QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#dockWidgets

    Returns
    -------

    QList[QDockWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets() const
    address = self.uglySide.call(
        'ritual_ZNK22QDockWidgetGroupWindow11dockWidgetsEv',
    )
    from . import QDockWidget
    return QList[QDockWidget]._cuteOwning(address)

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

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, event: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QDockWidgetGroupWindow::childEvent(QChildEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#childEvent

    Parameters
    ----------

    event : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
    self.uglySide.call(
        'ritual_ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent',
        self._addressOf(event),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetgroupwindow.html#eventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent',
        self._addressOf(obj, 'QObject'), self._addressOf(event),
    )
