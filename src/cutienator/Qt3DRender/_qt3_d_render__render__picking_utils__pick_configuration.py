"""
Qt3DRender::Render::PickingUtils::PickConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PickingUtils::PickConfiguration to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
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


class PickConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::PickingUtils::PickConfiguration:
  a plain Python object standing in front of one C++
  Qt3DRender::Render::PickingUtils::PickConfiguration.

  C++ hands a Qt3DRender::Render::PickingUtils::PickConfiguration around as a
  copy, so every C++ Qt3DRender::Render::PickingUtils::PickConfiguration
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DRender::Render::PickingUtils::PickConfiguration
  yet. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::PickingUtils::PickConfiguration::~PickConfiguration(
    )': the destructor: Python removes its C++
    Qt3DRender::Render::PickingUtils::PickConfiguration by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickingUtils::PickConfiguration is created at
    the first use, not by
    'Qt3DRender::Render::PickingUtils::PickConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::PickingUtils::PickConfiguration
    back gives a copy the ritual made for Python, in a new cute
    Qt3DRender::Render::PickingUtils::PickConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PickingUtils::PickConfiguration'

  #  Qt's '~Qt3DRender::Render::PickingUtils::PickConfiguration()'. Naming it
  #  makes this a value class: Python owns every C++
  #  Qt3DRender::Render::PickingUtils::PickConfiguration behind a cute one,
  #  and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render12PickingUtils17PickConfigurationD1Ev')

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

  @overload(
      WAIT['Qt3DRender.Render.FrameGraphNode'],
      WAIT['Qt3DRender.Render.RenderSettings'],
  )
  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'], NoneType)
  @overload(NoneType, WAIT['Qt3DRender.Render.RenderSettings'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      frameGraphRoot: Optional[Qt3DRender.Render.FrameGraphNode],
      renderSettings: Optional[Qt3DRender.Render.RenderSettings],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::PickingUtils::PickConfiguration::PickConfiguration(
    FrameGraphNode *frameGraphRoot, RenderSettings *renderSettings)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-pickconfiguration.html

    Parameters
    ----------

    frameGraphRoot : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderSettings : Optional[Qt3DRender.Render.RenderSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::PickingUtils::PickConfiguration::
    #      PickConfiguration(FrameGraphNode *frameGraphRoot, RenderSettings
    #      *renderSettings)
    self._noteCreation(PickConfiguration, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12PickingUtils17PickConfigurationC1EPN'
        'S0_14FrameGraphNodeEPNS0_14RenderSettingsE',
        self._addressOf(frameGraphRoot), self._addressOf(renderSettings),
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
