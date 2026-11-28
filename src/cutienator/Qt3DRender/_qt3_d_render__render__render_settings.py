"""
Qt3DRender::Render::RenderSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/rendersettings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::RenderSettings to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderSettings(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::RenderSettings: a plain Python
  object standing in front of one C++ Qt3DRender::Render::RenderSettings.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::RenderSettings is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderSettings that has a ritual
  and that Python can call so far, 9 names in all: 'syncFromFrontEnd',
  'activeFrameGraphID', 'renderPolicy', 'pickMethod', 'pickResultMode',
  'faceOrientationPickingMode', 'pickWorldSpaceTolerance', 'capabilities',
  'setActiveFrameGraphId'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderSettings is created at the first use,
    not by 'Qt3DRender::Render::RenderSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderSettings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def activeFrameGraphID(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::RenderSettings::activeFrameGraphID() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DRender::Render::RenderSettings::activeFrameGraphID() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings18activeFrameGraphIDE'
        'v',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def renderPolicy(self) -> Qt3DRender.QRenderSettings.RenderPolicy:
    """
    Calls Qt's 'QRenderSettings::RenderPolicy
    Qt3DRender::Render::RenderSettings::renderPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html#renderPolicy

    Returns
    -------

    Qt3DRender.QRenderSettings.RenderPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QRenderSettings.RenderPolicy(number)' gives.
    """
    #  QRenderSettings::RenderPolicy
    #      Qt3DRender::Render::RenderSettings::renderPolicy() const
    return Qt3DRender.QRenderSettings.RenderPolicy(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings12renderPolicyEv',
    ))

  def pickMethod(self) -> Qt3DRender.QPickingSettings.PickMethod:
    """
    Calls Qt's 'QPickingSettings::PickMethod
    Qt3DRender::Render::RenderSettings::pickMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html#pickMethod

    Returns
    -------

    Qt3DRender.QPickingSettings.PickMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QPickingSettings.PickMethod(number)' gives.
    """
    #  QPickingSettings::PickMethod
    #      Qt3DRender::Render::RenderSettings::pickMethod() const
    return Qt3DRender.QPickingSettings.PickMethod(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings10pickMethodEv',
    ))

  def pickResultMode(self) -> Qt3DRender.QPickingSettings.PickResultMode:
    """
    Calls Qt's 'QPickingSettings::PickResultMode
    Qt3DRender::Render::RenderSettings::pickResultMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html

    Returns
    -------

    Qt3DRender.QPickingSettings.PickResultMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QPickingSettings.PickResultMode(number)' gives.
    """
    #  QPickingSettings::PickResultMode
    #      Qt3DRender::Render::RenderSettings::pickResultMode() const
    return Qt3DRender.QPickingSettings.PickResultMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings14pickResultModeEv',
    ))

  def faceOrientationPickingMode(
      self,
  ) -> Qt3DRender.QPickingSettings.FaceOrientationPickingMode:
    """
    Calls Qt's 'QPickingSettings::FaceOrientationPickingMode
    Qt3DRender::Render::RenderSettings::faceOrientationPickingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html

    Returns
    -------

    Qt3DRender.QPickingSettings.FaceOrientationPickingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QPickingSettings.FaceOrientationPickingMode(number)' gives.
    """
    #  QPickingSettings::FaceOrientationPickingMode
    #      Qt3DRender::Render::RenderSettings::faceOrientationPickingMode()
    #      const
    return Qt3DRender.QPickingSettings.FaceOrientationPickingMode(
        self.uglySide.call(
            'ritual_ZNK10Qt3DRender6Render14RenderSettings26faceOrientation'
            'PickingModeEv',
        ))

  def pickWorldSpaceTolerance(self) -> float:
    """
    Calls Qt's 'float
    Qt3DRender::Render::RenderSettings::pickWorldSpaceTolerance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html
    """
    #  float Qt3DRender::Render::RenderSettings::pickWorldSpaceTolerance()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings23pickWorldSpaceToler'
        'anceEv',
    )

  def capabilities(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::RenderSettings::capabilities()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html#capabilities

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::RenderSettings::capabilities() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderSettings12capabilitiesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setActiveFrameGraphId(
      self,
      frameGraphNodeId: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderSettings::setActiveFrameGraphId(Qt3DCore::
    QNodeId frameGraphNodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html

    Parameters
    ----------

    frameGraphNodeId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderSettings::setActiveFrameGraphId(
    #      Qt3DCore::QNodeId frameGraphNodeId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14RenderSettings21setActiveFrameGraphI'
        'dEN8Qt3DCore7QNodeIdE',
        self._valueOf(frameGraphNodeId),
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
    'Qt3DRender::Render::RenderSettings::RenderSettings()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html
    """
    #  Qt3DRender::Render::RenderSettings::RenderSettings()
    self._noteCreation(RenderSettings, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14RenderSettingsC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderSettings::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersettings.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RenderSettings::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render14RenderSettings16syncFromFrontEndEPKN'
        '8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render14RenderSettings16syncFromFrontE'
          'ndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
