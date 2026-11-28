"""
QQuickTableViewSectionDragHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTableViewSectionDragHandler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QQuickTableViewPointerHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickDragEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickDragEvent = WAIT['QQuickDragEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTableViewSectionDragHandler(QQuickTableViewPointerHandler):
  """
  The cute side of Qt's QQuickTableViewSectionDragHandler: a plain Python
  object standing in front of one C++ QQuickTableViewSectionDragHandler.

  It is built on the cute 'QQuickTableViewPointerHandler', as Qt's
  QQuickTableViewSectionDragHandler is built on Qt's
  QQuickTableViewPointerHandler, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableViewSectionDragHandler that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject',
  'grabSection', 'handleDrag', 'handleDrop', 'handleDragDropAction',
  'setSectionOrientation', 'resetDragData', 'resetSectionOverlay'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTableViewSectionDragHandler::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickTableViewSectionDragHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuickTableViewSectionDragHandler::~QQuickTableViewSectionDragHandler(
    )': the destructor: Python never removes a C++
    QQuickTableViewSectionDragHandler.
  - Qt's 'void
    QQuickTableViewSectionDragHandler::handleEventPoint(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickTableViewSectionDragHandler.

  What to expect
  --------------

  - The C++ QQuickTableViewSectionDragHandler is created at the first use,
    not by 'QQuickTableViewSectionDragHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableViewSectionDragHandler.
  - Qt tells when it has removed the C++ QQuickTableViewSectionDragHandler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTableViewSectionDragHandler that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableViewSectionDragHandler'

  #  A C++ QQuickTableViewSectionDragHandler Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTableViewSectionDragHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickTableViewSectionDragHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTableViewSectionDragHandler::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QQuickTableViewSectionDragHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setSectionOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewSectionDragHandler::setSectionOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickTableViewSectionDragHandler::setSectionOrientation(Qt::
    #      Orientation orientation)
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler21setSectionOrientatio'
        'nEN2Qt11OrientationE',
        orientation.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQuickTableViewSectionDragHandler::QQuickTableViewSectionDragHandler(
    QQuickTableView *view)': leans on
    'QQuickTableViewSectionDragHandler::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTableViewSectionDragHandler.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickTableViewSectionDragHandler::QQuickTableViewSectionDragHandl"
        "er(QQuickTableView *view)': leans on "
        "'QQuickTableViewSectionDragHandler::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def grabSection(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewSectionDragHandler::grabSection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html#grabSection
    """
    #  void QQuickTableViewSectionDragHandler::grabSection()
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler11grabSectionEv',
    )

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def handleDrag(self, event: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewSectionDragHandler::handleDrag(QQuickDragEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html#handleDrag

    Parameters
    ----------

    event : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewSectionDragHandler::handleDrag(QQuickDragEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler10handleDragEP15QQuick'
        'DragEvent',
        self._addressOf(event),
    )

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def handleDrop(self, event: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewSectionDragHandler::handleDrop(QQuickDragEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html#handleDrop

    Parameters
    ----------

    event : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewSectionDragHandler::handleDrop(QQuickDragEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler10handleDropEP15QQuick'
        'DragEvent',
        self._addressOf(event),
    )

  @overload(Qt.DropAction)
  def handleDragDropAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewSectionDragHandler::handleDragDropAction(Qt::DropAction
    action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickTableViewSectionDragHandler::handleDragDropAction(Qt::
    #      DropAction action)
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler20handleDragDropAction'
        'EN2Qt10DropActionE',
        action.value,
    )

  def resetDragData(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewSectionDragHandler::resetDragData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html
    """
    #  void QQuickTableViewSectionDragHandler::resetDragData()
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler13resetDragDataEv',
    )

  def resetSectionOverlay(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewSectionDragHandler::resetSectionOverlay()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewsectiondraghandler.html
    """
    #  void QQuickTableViewSectionDragHandler::resetSectionOverlay()
    self.uglySide.call(
        'ritual_ZN33QQuickTableViewSectionDragHandler19resetSectionOverlayE'
        'v',
    )
