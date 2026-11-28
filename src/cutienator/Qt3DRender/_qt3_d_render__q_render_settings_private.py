"""
Qt3DRender::QRenderSettingsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrendersettings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QRenderSettingsPrivate to be private: it declares the
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


class QRenderSettingsPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderSettingsPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderSettingsPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QRenderSettingsPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderSettingsPrivate that has a ritual
  and that Python can call so far, 7 names in all: 'init', 'invalidateFrame',
  '_q_onPickingMethodChanged', '_q_onPickResultModeChanged',
  '_q_onFaceOrientationPickingModeChanged',
  '_q_onWorldSpaceToleranceChanged', 'q_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRenderSettings *Qt3DRender::QRenderSettingsPrivate::q_func()
    const': takes in Python what 'QRenderSettings
    *Qt3DRender::QRenderSettingsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderSettingsPrivate is created at the first use,
    not by 'Qt3DRender::QRenderSettingsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderSettingsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderSettingsPrivate'

  #  A C++ Qt3DRender::QRenderSettingsPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderSettingsPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderSettingsPrivate::QRenderSettingsPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html
    """
    #  Qt3DRender::QRenderSettingsPrivate::QRenderSettingsPrivate()
    self._noteCreation(QRenderSettingsPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivateC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderSettingsPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html#init
    """
    #  void Qt3DRender::QRenderSettingsPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate4initEv',
    )

  def invalidateFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderSettingsPrivate::invalidateFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html
    """
    #  void Qt3DRender::QRenderSettingsPrivate::invalidateFrame()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate15invalidateFrameEv',
    )

  @overload(Qt3DRender.QPickingSettings.PickMethod)
  def _q_onPickingMethodChanged(
      self,
      pickMethod: Qt3DRender.QPickingSettings.PickMethod,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettingsPrivate::_q_onPickingMethodChanged(
    QPickingSettings::PickMethod pickMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html

    Parameters
    ----------

    pickMethod : Qt3DRender.QPickingSettings.PickMethod
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderSettingsPrivate::_q_onPickingMethodChanged(
    #      QPickingSettings::PickMethod pickMethod)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate25_q_onPickingMethodC'
        'hangedENS_16QPickingSettings10PickMethodE',
        pickMethod.value,
    )

  @overload(Qt3DRender.QPickingSettings.PickResultMode)
  def _q_onPickResultModeChanged(
      self,
      pickResultMode: Qt3DRender.QPickingSettings.PickResultMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettingsPrivate::_q_onPickResultModeChanged(
    QPickingSettings::PickResultMode pickResultMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html

    Parameters
    ----------

    pickResultMode : Qt3DRender.QPickingSettings.PickResultMode
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderSettingsPrivate::_q_onPickResultModeChanged(
    #      QPickingSettings::PickResultMode pickResultMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate26_q_onPickResultMode'
        'ChangedENS_16QPickingSettings14PickResultModeE',
        pickResultMode.value,
    )

  @overload(Qt3DRender.QPickingSettings.FaceOrientationPickingMode)
  def _q_onFaceOrientationPickingModeChanged(
      self,
      faceOrientationPickingMode: Qt3DRender.QPickingSettings.FaceOrientationPickingMode,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderSettingsPrivate::
    _q_onFaceOrientationPickingModeChanged(QPickingSettings::
    FaceOrientationPickingMode faceOrientationPickingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html

    Parameters
    ----------

    faceOrientationPickingMode : Qt3DRender.QPickingSettings.FaceOrientationPickingMode
      Passed on as its number.
    """
    #  void Qt3DRender::QRenderSettingsPrivate::
    #      _q_onFaceOrientationPickingModeChanged(QPickingSettings::
    #      FaceOrientationPickingMode faceOrientationPickingMode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate38_q_onFaceOrientatio'
        'nPickingModeChangedENS_16QPickingSettings26FaceOrientationPickingM'
        'odeE',
        faceOrientationPickingMode.value,
    )

  @overload(float)
  def _q_onWorldSpaceToleranceChanged(
      self,
      worldSpaceTolerance: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderSettingsPrivate::_q_onWorldSpaceToleranceChanged(float
    worldSpaceTolerance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html

    Parameters
    ----------

    worldSpaceTolerance : float
      Passed on as it is.
    """
    #  void Qt3DRender::QRenderSettingsPrivate::
    #      _q_onWorldSpaceToleranceChanged(float worldSpaceTolerance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate31_q_onWorldSpaceTole'
        'ranceChangedEf',
        worldSpaceTolerance,
    )

  def q_func(self) -> Optional[Qt3DRender.QRenderSettings]:
    """
    Calls Qt's 'QRenderSettings
    *Qt3DRender::QRenderSettingsPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendersettingsprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QRenderSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderSettings *Qt3DRender::QRenderSettingsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender22QRenderSettingsPrivate6q_funcEv',
    )
    return Qt3DRender.QRenderSettings._cuteAt(address)
