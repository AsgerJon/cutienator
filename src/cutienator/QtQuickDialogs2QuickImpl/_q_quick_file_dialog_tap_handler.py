"""
QQuickFileDialogTapHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogTapHandler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtQuick import QQuickTapHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QEventPoint, QPointerEvent
  from ..QtQuick import QQuickDragEvent
  from . import QQuickFileDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickDragEvent = WAIT['QQuickDragEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogTapHandler(QQuickTapHandler):
  """
  The cute side of Qt's QQuickFileDialogTapHandler: a plain Python object
  standing in front of one C++ QQuickFileDialogTapHandler.

  It is built on the cute 'QQuickTapHandler', as Qt's
  QQuickFileDialogTapHandler is built on Qt's QQuickTapHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogTapHandler that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'state',
  'getFileDialogImpl', 'grabFolder', 'getFolderUrlAtPress', 'handleDrag',
  'handleDrop', 'handleContainsDragChanged', 'wantsEventPoint',
  'resetDragData'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileDialogTapHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickFileDialogTapHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFileDialogTapHandler::handleEventPoint(QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickFileDialogTapHandler; 1 leans on 'vtable for
  QQuickFileDialogTapHandler', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickFileDialogTapHandler is created at the first use, not by
    'QQuickFileDialogTapHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogTapHandler.
  - Qt tells when it has removed the C++ QQuickFileDialogTapHandler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFileDialogTapHandler that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickFileDialogTapHandler, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class State(CuteNum):
    """
    The enum 'QQuickFileDialogTapHandler::State' of Qt, with the 5 names Qt
    gives in it.
    """

    Listening = Kee[int](0)
    Tracking = Kee[int](1)
    DraggingStarted = Kee[int](2)
    Dragging = Kee[int](3)
    DraggingFinished = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogTapHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialogTapHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialogTapHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickFileDialogTapHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def getFileDialogImpl(self) -> Optional[QQuickFileDialogImpl]:
    """
    Calls Qt's 'QQuickFileDialogImpl
    *QQuickFileDialogTapHandler::getFileDialogImpl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#getFileDialogImpl

    Returns
    -------

    Optional[QQuickFileDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImpl *QQuickFileDialogTapHandler::getFileDialogImpl()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickFileDialogTapHandler17getFileDialogImplEv',
    )
    from . import QQuickFileDialogImpl
    return QQuickFileDialogImpl._cuteAt(address)

  def getFolderUrlAtPress(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialogTapHandler::getFolderUrlAtPress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialogTapHandler::getFolderUrlAtPress() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickFileDialogTapHandler19getFolderUrlAtPressEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickFileDialogTapHandler::QQuickFileDialogTapHandler(QQuickItem
    *parent)': leans on 'vtable for QQuickFileDialogTapHandler', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickFileDialogTapHandler.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickFileDialogTapHandler::QQuickFileDialogTapHandler(QQuickItem "
        "*parent)': leans on 'vtable for QQuickFileDialogTapHandler', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def state(self) -> State:
    """
    Calls Qt's 'State QQuickFileDialogTapHandler::state()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QQuickFileDialogTapHandler::state()
    return QQuickFileDialogTapHandler.State(self.uglySide.call(
        'ritual_ZN26QQuickFileDialogTapHandler5stateEv',
    ))

  def grabFolder(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogTapHandler::grabFolder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#grabFolder
    """
    #  void QQuickFileDialogTapHandler::grabFolder()
    self.uglySide.call('ritual_ZN26QQuickFileDialogTapHandler10grabFolderEv')

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def handleDrag(self, event: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogTapHandler::handleDrag(QQuickDragEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#handleDrag

    Parameters
    ----------

    event : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogTapHandler::handleDrag(QQuickDragEvent *event)
    self.uglySide.call(
        'ritual_ZN26QQuickFileDialogTapHandler10handleDragEP15QQuickDragEve'
        'nt',
        self._addressOf(event),
    )

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def handleDrop(self, event: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogTapHandler::handleDrop(QQuickDragEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#handleDrop

    Parameters
    ----------

    event : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogTapHandler::handleDrop(QQuickDragEvent *event)
    self.uglySide.call(
        'ritual_ZN26QQuickFileDialogTapHandler10handleDropEP15QQuickDragEve'
        'nt',
        self._addressOf(event),
    )

  def handleContainsDragChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogTapHandler::handleContainsDragChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html
    """
    #  void QQuickFileDialogTapHandler::handleContainsDragChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickFileDialogTapHandler25handleContainsDragChangedEv',
    )

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def wantsEventPoint(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickFileDialogTapHandler::wantsEventPoint(const
    QPointerEvent *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#wantsEventPoint

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickFileDialogTapHandler::wantsEventPoint(const QPointerEvent
    #      *event, const QEventPoint &point)
    ritual = (
        'ritual_ZN26QQuickFileDialogTapHandler15wantsEventPointEPK13QPointe'
        'rEventRK11QEventPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickFileDialogTapHandler15wantsEventPointEPK13Q'
          'PointerEventRK11QEventPoint')
    return self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(point),
    )

  def resetDragData(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogTapHandler::resetDragData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogtaphandler.html#resetDragData
    """
    #  void QQuickFileDialogTapHandler::resetDragData()
    self.uglySide.call(
        'ritual_ZN26QQuickFileDialogTapHandler13resetDragDataEv',
    )
