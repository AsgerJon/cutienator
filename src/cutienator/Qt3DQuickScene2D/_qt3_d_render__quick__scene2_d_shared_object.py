"""
Qt3DRender::Quick::Scene2DSharedObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dsharedobject_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Quick::Scene2DSharedObject to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene2DSharedObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Quick::Scene2DSharedObject: a plain
  Python object standing in front of one C++
  Qt3DRender::Quick::Scene2DSharedObject.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Quick::Scene2DSharedObject that has a
  ritual and that Python can call so far, 16 names in all: 'isInitialized',
  'setInitialized', 'isQuitting', 'setQuitting', 'requestQuit',
  'requestInvalidate', 'requestRender', 'isSyncRequested',
  'clearSyncRequest', 'wait', 'wake', 'isPrepared', 'setPrepared',
  'disallowRender', 'canRender', 'cleanup'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Quick::Scene2DSharedObject::~Scene2DSharedObject()':
    the destructor: Python never removes a C++
    Qt3DRender::Quick::Scene2DSharedObject.

  What to expect
  --------------

  - The C++ Qt3DRender::Quick::Scene2DSharedObject is created at the first
    use, not by 'Qt3DRender::Quick::Scene2DSharedObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Quick::Scene2DSharedObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Quick::Scene2DSharedObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::Scene2DSharedObject::isInitialized()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  bool Qt3DRender::Quick::Scene2DSharedObject::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject13isInitializedEv',
    )

  def isQuitting(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::Scene2DSharedObject::isQuitting()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  bool Qt3DRender::Quick::Scene2DSharedObject::isQuitting() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject10isQuittingEv',
    )

  def isSyncRequested(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Quick::Scene2DSharedObject::isSyncRequested() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  bool Qt3DRender::Quick::Scene2DSharedObject::isSyncRequested() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject15isSyncRequested'
        'Ev',
    )

  def isPrepared(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::Scene2DSharedObject::isPrepared()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  bool Qt3DRender::Quick::Scene2DSharedObject::isPrepared() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject10isPreparedEv',
    )

  def canRender(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Quick::Scene2DSharedObject::canRender()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  bool Qt3DRender::Quick::Scene2DSharedObject::canRender() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender5Quick19Scene2DSharedObject9canRenderEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setInitialized(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DSharedObject::setInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::setInitialized()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject14setInitializedEv',
    )

  def setQuitting(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::setQuitting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::setQuitting()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11setQuittingEv',
    )

  def setPrepared(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::setPrepared()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::setPrepared()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11setPreparedEv',
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

  @overload(WAIT['Qt3DRender.Quick.Scene2DManager'])
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[Qt3DRender.Quick.Scene2DManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Quick::Scene2DSharedObject::Scene2DSharedObject(
    Scene2DManager *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Quick.Scene2DManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Quick::Scene2DSharedObject::Scene2DSharedObject(
    #      Scene2DManager *manager)
    self._noteCreation(Scene2DSharedObject, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObjectC1EPNS0_14Scene2DM'
        'anagerE',
        self._addressOf(manager),
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

  def requestQuit(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::requestQuit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::requestQuit()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject11requestQuitEv',
    )

  def requestInvalidate(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DSharedObject::requestInvalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::requestInvalidate()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject17requestInvalidat'
        'eEv',
    )

  @overload(bool)
  def requestRender(self, sync: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DSharedObject::requestRender(bool sync)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html

    Parameters
    ----------

    sync : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::requestRender(bool sync)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject13requestRenderEb',
        sync,
    )

  def clearSyncRequest(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DSharedObject::clearSyncRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::clearSyncRequest()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject16clearSyncRequest'
        'Ev',
    )

  def wait(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::wait()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html#wait
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::wait()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject4waitEv',
    )

  def wake(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::wake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html#wake
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::wake()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject4wakeEv',
    )

  def disallowRender(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Quick::Scene2DSharedObject::disallowRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::disallowRender()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject14disallowRenderEv',
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Quick::Scene2DSharedObject::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2dsharedobject.html#cleanup
    """
    #  void Qt3DRender::Quick::Scene2DSharedObject::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick19Scene2DSharedObject7cleanupEv',
    )
