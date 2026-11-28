"""
Qt3DRender::Quick::Scene2DManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dmanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Quick::Scene2DManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene2DManager(QObject):
  """
  The cute side of Qt's Qt3DRender::Quick::Scene2DManager: a plain Python
  object standing in front of one C++ Qt3DRender::Quick::Scene2DManager.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::Quick::Scene2DManager is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Quick::Scene2DManager that has a ritual
  and that Python can call so far, 10 names in all: 'metaObject',
  'requestRender', 'requestRenderSync', 'doRenderSync', 'startIfInitialized',
  'stopAndClean', 'updateSizes', 'setItem', 'event', 'cleanup'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Quick::Scene2DManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::Quick::Scene2DManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::Quick::Scene2DManager::~Scene2DManager()': the
    destructor: Python never removes a C++ Qt3DRender::Quick::Scene2DManager.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Quick::Scene2DManager is created at the first use,
    not by 'Qt3DRender::Quick::Scene2DManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Quick::Scene2DManager.
  - Qt tells when it has removed the C++ Qt3DRender::Quick::Scene2DManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::Quick::Scene2DManager that has no cute
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
  __qt_class__ = 'Qt3DRender::Quick::Scene2DManager'

  #  A C++ Qt3DRender::Quick::Scene2DManager Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Quick_Scene2DManager'

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
    *Qt3DRender::Quick::Scene2DManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::Quick::Scene2DManager::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick14Scene2DManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::setItem(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#setItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Quick::Scene2DManager::setItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager7setItemEP10QQuickItem',
        self._addressOf(item),
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
    Qt's 'Qt3DRender::Quick::Scene2DManager::Scene2DManager(QScene2DPrivate
    *priv)': leans on
    'Qt3DRender::Quick::Scene2DManager::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Quick.Scene2DManager.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DRender::Quick::Scene2DManager::Scene2DManager(QScene2DPrivate "
        "*priv)': leans on "
        "'Qt3DRender::Quick::Scene2DManager::qt_metacall(QMetaObject::Call, "
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

  def requestRender(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::requestRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#requestRender
    """
    #  void Qt3DRender::Quick::Scene2DManager::requestRender()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager13requestRenderEv',
    )

  def requestRenderSync(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::requestRenderSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html
    """
    #  void Qt3DRender::Quick::Scene2DManager::requestRenderSync()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager17requestRenderSyncEv',
    )

  def doRenderSync(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::doRenderSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#doRenderSync
    """
    #  void Qt3DRender::Quick::Scene2DManager::doRenderSync()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager12doRenderSyncEv',
    )

  def startIfInitialized(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DManager::startIfInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html
    """
    #  void Qt3DRender::Quick::Scene2DManager::startIfInitialized()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager18startIfInitializedEv',
    )

  def stopAndClean(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::stopAndClean()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#stopAndClean
    """
    #  void Qt3DRender::Quick::Scene2DManager::stopAndClean()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager12stopAndCleanEv',
    )

  def updateSizes(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::updateSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#updateSizes
    """
    #  void Qt3DRender::Quick::Scene2DManager::updateSizes()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager11updateSizesEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::Scene2DManager::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Quick::Scene2DManager::event(QEvent *e)
    ritual = 'ritual_ZN10Qt3DRender5Quick14Scene2DManager5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender5Quick14Scene2DManager5eventEP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(e))

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DManager::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dmanager.html#cleanup
    """
    #  void Qt3DRender::Quick::Scene2DManager::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick14Scene2DManager7cleanupEv',
    )
