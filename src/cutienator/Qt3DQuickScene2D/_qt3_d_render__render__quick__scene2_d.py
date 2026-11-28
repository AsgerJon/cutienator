"""
Qt3DRender::Render::Quick::Scene2D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::Quick::Scene2D to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene2D(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Quick::Scene2D: a plain Python
  object standing in front of one C++ Qt3DRender::Render::Quick::Scene2D.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Quick::Scene2D is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Quick::Scene2D that has a ritual
  and that Python can call so far, 11 names in all: 'render',
  'initializeRender', 'invalidate', 'cleanup', 'setOutput',
  'initializeSharedObject', 'syncFromFrontEnd', 'syncRenderControl',
  'registerObjectPickerEvents', 'unregisterObjectPickerEvents',
  'handlePickEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Quick::Scene2D::~Scene2D()': the destructor:
    Python never removes a C++ Qt3DRender::Render::Quick::Scene2D.
  - Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::setSharedObject(Qt3DRender::Quick::
    Scene2DSharedObjectPtr sharedObject)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Quick::Scene2D is created at the first use,
    not by 'Qt3DRender::Render::Quick::Scene2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Quick::Scene2D.
  - Each name of Qt's Qt3DRender::Render::Quick::Scene2D that has no cute
    function yet, 'setSharedObject', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::Quick::Scene2D'

  #  A C++ Qt3DRender::Render::Quick::Scene2D Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Quick_Scene2D'

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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setOutput(self, outputId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::setOutput(Qt3DCore::QNodeId
    outputId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html#setOutput

    Parameters
    ----------

    outputId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Quick::Scene2D::setOutput(Qt3DCore::QNodeId
    #      outputId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D9setOutputEN8Qt3DCore7QN'
        'odeIdE',
        self._valueOf(outputId),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::Quick::Scene2D::Scene2D()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html#Scene2D
    """
    #  Qt3DRender::Render::Quick::Scene2D::Scene2D()
    self._noteCreation(Scene2D, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2DC1Ev',
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

  def render(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Quick::Scene2D::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html#render
    """
    #  void Qt3DRender::Render::Quick::Scene2D::render()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render5Quick7Scene2D6renderEv')

  def initializeRender(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Quick::Scene2D::initializeRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html
    """
    #  void Qt3DRender::Render::Quick::Scene2D::initializeRender()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D16initializeRenderEv',
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Quick::Scene2D::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html#invalidate
    """
    #  void Qt3DRender::Render::Quick::Scene2D::invalidate()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D10invalidateEv',
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Quick::Scene2D::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html#cleanup
    """
    #  void Qt3DRender::Render::Quick::Scene2D::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D7cleanupEv',
    )

  def initializeSharedObject(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::initializeSharedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html
    """
    #  void Qt3DRender::Render::Quick::Scene2D::initializeSharedObject()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D22initializeSharedObject'
        'Ev',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render5Quick7Scene2D16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def syncRenderControl(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::syncRenderControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html
    """
    #  void Qt3DRender::Render::Quick::Scene2D::syncRenderControl()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D17syncRenderControlEv',
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def registerObjectPickerEvents(
      self,
      qentity: Optional[Qt3DCore.QEntity],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::Quick::Scene2D::registerObjectPickerEvents(
    Qt3DCore::QEntity *qentity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html

    Parameters
    ----------

    qentity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::Quick::Scene2D::registerObjectPickerEvents(
    #      Qt3DCore::QEntity *qentity)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D26registerObjectPickerEv'
        'entsEPN8Qt3DCore7QEntityE',
        self._addressOf(qentity),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def unregisterObjectPickerEvents(self, entityId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::unregisterObjectPickerEvents(
    Qt3DCore::QNodeId entityId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html

    Parameters
    ----------

    entityId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Quick::Scene2D::unregisterObjectPickerEvents(
    #      Qt3DCore::QNodeId entityId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D28unregisterObjectPicker'
        'EventsEN8Qt3DCore7QNodeIdE',
        self._valueOf(entityId),
    )

  @overload(int, WAIT['Qt3DRender.QPickEvent'])
  @overload(int, NoneType)
  def handlePickEvent(
      self,
      type: int,
      ev: Optional[Qt3DRender.QPickEvent],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Quick::Scene2D::handlePickEvent(int
    type, const QPickEvent *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-quick-scene2d.html

    Parameters
    ----------

    type : int
      Passed on as it is.

    ev : Optional[Qt3DRender.QPickEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Quick::Scene2D::handlePickEvent(int type,
    #      const QPickEvent *ev)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render5Quick7Scene2D15handlePickEventEiPKNS_'
        '10QPickEventE',
        type, self._addressOf(ev),
    )

  @staticmethod
  def setSharedObject(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::Quick::Scene2D::setSharedObject(Qt3DRender::Quick::
    Scene2DSharedObjectPtr sharedObject)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Quick.Scene2D.setSharedObject' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::Quick::Scene2D::setSharedObject(Qt3DRender::Qui"
        "ck::Scene2DSharedObjectPtr sharedObject)': takes a type Python has "
        "no way to hand over yet.")
