"""
QQuick3DXrVirtualMouse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrvirtualmouse_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrVirtualMouse to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QEvent, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3D import QQuick3DNode
  from . import QQuick3DXrView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DXrView = WAIT['QQuick3DXrView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrVirtualMouse(QObject):
  """
  The cute side of Qt's QQuick3DXrVirtualMouse: a plain Python object
  standing in front of one C++ QQuick3DXrVirtualMouse.

  It is built on the cute 'QObject', as Qt's QQuick3DXrVirtualMouse is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrVirtualMouse that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'rightMouseButton',
  'leftMouseButton', 'middleMouseButton', 'scrollWheelX', 'scrollWheelY',
  'scrollTimerInterval', 'scrollPixelDelta', 'source', 'view', 'enabled',
  'setRightMouseButton', 'setLeftMouseButton', 'setMiddleMouseButton',
  'setScrollWheelX', 'setScrollWheelY', 'setScrollTimerInterval',
  'setScrollPixelDelta', 'setSource', 'setView', 'setEnabled', 'moveEvent',
  'generateWheelEvent', 'rightMouseButtonChanged', 'leftMouseButtonChanged',
  'middleMouseButtonChanged', 'scrollWheelXChanged', 'scrollWheelYChanged',
  'scrollTimerIntervalChanged', 'scrollPixelDeltaChanged', 'sourceChanged',
  'viewChanged', 'enabledChanged', 'generateEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrVirtualMouse::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrVirtualMouse::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 1 leans on
  'QQuick3DXrVirtualMouse; 1 leans on 'vtable for QQuick3DXrVirtualMouse',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QQuick3DXrVirtualMouse is created at the first use, not by
    'QQuick3DXrVirtualMouse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrVirtualMouse.
  - Qt tells when it has removed the C++ QQuick3DXrVirtualMouse. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrVirtualMouse that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrVirtualMouse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrVirtualMouse::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrVirtualMouse::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rightMouseButton(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrVirtualMouse::rightMouseButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#rightMouseButton
    """
    #  bool QQuick3DXrVirtualMouse::rightMouseButton() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse16rightMouseButtonEv',
    )

  def leftMouseButton(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrVirtualMouse::leftMouseButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#leftMouseButton
    """
    #  bool QQuick3DXrVirtualMouse::leftMouseButton() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse15leftMouseButtonEv',
    )

  def middleMouseButton(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrVirtualMouse::middleMouseButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#middleMouseButton
    """
    #  bool QQuick3DXrVirtualMouse::middleMouseButton() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse17middleMouseButtonEv',
    )

  def scrollWheelX(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrVirtualMouse::scrollWheelX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollWheelX
    """
    #  float QQuick3DXrVirtualMouse::scrollWheelX() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse12scrollWheelXEv',
    )

  def scrollWheelY(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrVirtualMouse::scrollWheelY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollWheelY
    """
    #  float QQuick3DXrVirtualMouse::scrollWheelY() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse12scrollWheelYEv',
    )

  def scrollTimerInterval(self) -> int:
    """
    Calls Qt's 'int QQuick3DXrVirtualMouse::scrollTimerInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollTimerInterval
    """
    #  int QQuick3DXrVirtualMouse::scrollTimerInterval() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse19scrollTimerIntervalEv',
    )

  def scrollPixelDelta(self) -> int:
    """
    Calls Qt's 'int QQuick3DXrVirtualMouse::scrollPixelDelta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollPixelDelta
    """
    #  int QQuick3DXrVirtualMouse::scrollPixelDelta() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse16scrollPixelDeltaEv',
    )

  def source(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DXrVirtualMouse::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#source

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DXrVirtualMouse::source() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DXrVirtualMouse6sourceEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def view(self) -> Optional[QQuick3DXrView]:
    """
    Calls Qt's 'QQuick3DXrView *QQuick3DXrVirtualMouse::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#view

    Returns
    -------

    Optional[QQuick3DXrView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrView *QQuick3DXrVirtualMouse::view() const
    address = self.uglySide.call('ritual_ZNK22QQuick3DXrVirtualMouse4viewEv')
    from . import QQuick3DXrView
    return QQuick3DXrView._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrVirtualMouse::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#enabled
    """
    #  bool QQuick3DXrVirtualMouse::enabled() const
    return self.uglySide.call('ritual_ZNK22QQuick3DXrVirtualMouse7enabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRightMouseButton(self, rightMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setRightMouseButton(bool
    rightMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setRightMouseButton

    Parameters
    ----------

    rightMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setRightMouseButton(bool
    #      rightMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse19setRightMouseButtonEb',
        rightMouseButton,
    )

  @overload(bool)
  def setLeftMouseButton(self, leftMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setLeftMouseButton(bool
    leftMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setLeftMouseButton

    Parameters
    ----------

    leftMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setLeftMouseButton(bool leftMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse18setLeftMouseButtonEb',
        leftMouseButton,
    )

  @overload(bool)
  def setMiddleMouseButton(self, middleMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setMiddleMouseButton(bool
    middleMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setMiddleMouseButton

    Parameters
    ----------

    middleMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setMiddleMouseButton(bool
    #      middleMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse20setMiddleMouseButtonEb',
        middleMouseButton,
    )

  @overload(float)
  def setScrollWheelX(self, scrollWheelX: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setScrollWheelX(float
    scrollWheelX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setScrollWheelX

    Parameters
    ----------

    scrollWheelX : float
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setScrollWheelX(float scrollWheelX)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse15setScrollWheelXEf', scrollWheelX,
    )

  @overload(float)
  def setScrollWheelY(self, scrollWheelY: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setScrollWheelY(float
    scrollWheelY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setScrollWheelY

    Parameters
    ----------

    scrollWheelY : float
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setScrollWheelY(float scrollWheelY)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse15setScrollWheelYEf', scrollWheelY,
    )

  @overload(int)
  def setScrollTimerInterval(self, scrollTimerInterval: int) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setScrollTimerInterval(int
    scrollTimerInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setScrollTimerInterval

    Parameters
    ----------

    scrollTimerInterval : int
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setScrollTimerInterval(int
    #      scrollTimerInterval)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse22setScrollTimerIntervalEi',
        scrollTimerInterval,
    )

  @overload(int)
  def setScrollPixelDelta(self, scrollPixelDelta: int) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setScrollPixelDelta(int
    scrollPixelDelta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setScrollPixelDelta

    Parameters
    ----------

    scrollPixelDelta : int
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setScrollPixelDelta(int scrollPixelDelta)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse19setScrollPixelDeltaEi',
        scrollPixelDelta,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setSource(self, source: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setSource(QQuick3DNode
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setSource

    Parameters
    ----------

    source : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrVirtualMouse::setSource(QQuick3DNode *source)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse9setSourceEP12QQuick3DNode',
        self._addressOf(source),
    )

  @overload(QQuick3DXrView)
  @overload(NoneType)
  def setView(self, view: Optional[QQuick3DXrView]) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setView(QQuick3DXrView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setView

    Parameters
    ----------

    view : Optional[QQuick3DXrView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrVirtualMouse::setView(QQuick3DXrView *view)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse7setViewEP14QQuick3DXrView',
        self._addressOf(view),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse10setEnabledEb', enabled,
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
    Qt's 'QQuick3DXrVirtualMouse::QQuick3DXrVirtualMouse(QObject *parent)':
    leans on 'vtable for QQuick3DXrVirtualMouse', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrVirtualMouse.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrVirtualMouse::QQuick3DXrVirtualMouse(QObject *parent)': "
        "leans on 'vtable for QQuick3DXrVirtualMouse', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def moveEvent(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::moveEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#moveEvent
    """
    #  void QQuick3DXrVirtualMouse::moveEvent()
    self.uglySide.call('ritual_ZN22QQuick3DXrVirtualMouse9moveEventEv')

  def generateWheelEvent(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::generateWheelEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#generateWheelEvent
    """
    #  void QQuick3DXrVirtualMouse::generateWheelEvent()
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse18generateWheelEventEv',
    )

  @overload(bool)
  def rightMouseButtonChanged(self, rightMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::rightMouseButtonChanged(bool
    rightMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html

    Parameters
    ----------

    rightMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::rightMouseButtonChanged(bool
    #      rightMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse23rightMouseButtonChangedEb',
        rightMouseButton,
    )

  @overload(bool)
  def leftMouseButtonChanged(self, leftMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::leftMouseButtonChanged(bool
    leftMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#leftMouseButtonChanged

    Parameters
    ----------

    leftMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::leftMouseButtonChanged(bool
    #      leftMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse22leftMouseButtonChangedEb',
        leftMouseButton,
    )

  @overload(bool)
  def middleMouseButtonChanged(self, middleMouseButton: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::middleMouseButtonChanged(bool
    middleMouseButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html

    Parameters
    ----------

    middleMouseButton : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::middleMouseButtonChanged(bool
    #      middleMouseButton)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse24middleMouseButtonChangedEb',
        middleMouseButton,
    )

  @overload(float)
  def scrollWheelXChanged(self, scrollWheelX: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::scrollWheelXChanged(float
    scrollWheelX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollWheelXChanged

    Parameters
    ----------

    scrollWheelX : float
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::scrollWheelXChanged(float scrollWheelX)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse19scrollWheelXChangedEf',
        scrollWheelX,
    )

  @overload(float)
  def scrollWheelYChanged(self, scrollWheelY: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::scrollWheelYChanged(float
    scrollWheelY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#scrollWheelYChanged

    Parameters
    ----------

    scrollWheelY : float
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::scrollWheelYChanged(float scrollWheelY)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse19scrollWheelYChangedEf',
        scrollWheelY,
    )

  @overload(int)
  def scrollTimerIntervalChanged(self, scrollTimerInterval: int) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::scrollTimerIntervalChanged(int
    scrollTimerInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html

    Parameters
    ----------

    scrollTimerInterval : int
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::scrollTimerIntervalChanged(int
    #      scrollTimerInterval)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse26scrollTimerIntervalChangedEi',
        scrollTimerInterval,
    )

  @overload(int)
  def scrollPixelDeltaChanged(self, scrollPixelDelta: int) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::scrollPixelDeltaChanged(int
    scrollPixelDelta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html

    Parameters
    ----------

    scrollPixelDelta : int
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::scrollPixelDeltaChanged(int
    #      scrollPixelDelta)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse23scrollPixelDeltaChangedEi',
        scrollPixelDelta,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def sourceChanged(self, source: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::sourceChanged(QQuick3DNode
    *source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#sourceChanged

    Parameters
    ----------

    source : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrVirtualMouse::sourceChanged(QQuick3DNode *source)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse13sourceChangedEP12QQuick3DNode',
        self._addressOf(source),
    )

  @overload(QQuick3DXrView)
  @overload(NoneType)
  def viewChanged(self, view: Optional[QQuick3DXrView]) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::viewChanged(QQuick3DXrView
    *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#viewChanged

    Parameters
    ----------

    view : Optional[QQuick3DXrView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrVirtualMouse::viewChanged(QQuick3DXrView *view)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse11viewChangedEP14QQuick3DXrView',
        self._addressOf(view),
    )

  @overload(bool)
  def enabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::enabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#enabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DXrVirtualMouse::enabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse14enabledChangedEb', enabled,
    )

  @overload(QEvent.Type)
  @overload(QEvent.Type, Qt.MouseButton)
  def generateEvent(
      self,
      type: QEvent.Type,
      button: Qt.MouseButton = Qt.MouseButton.NoButton,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrVirtualMouse::generateEvent(QEvent::Type type,
    Qt::MouseButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrvirtualmouse.html#generateEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    button : Qt.MouseButton
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MouseButton.NoButton.
    """
    #  void QQuick3DXrVirtualMouse::generateEvent(QEvent::Type type,
    #      Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN22QQuick3DXrVirtualMouse13generateEventEN6QEvent4TypeEN2Q'
        't11MouseButtonE',
        type.value, button.value,
    )
