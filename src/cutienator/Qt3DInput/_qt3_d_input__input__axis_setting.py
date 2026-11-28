"""
Qt3DInput::Input::AxisSetting binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/axissetting_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::AxisSetting to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AxisSetting(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::AxisSetting: a plain Python object
  standing in front of one C++ Qt3DInput::Input::AxisSetting.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::AxisSetting is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::AxisSetting that has a ritual and
  that Python can call so far, 4 names in all: 'cleanup', 'deadZoneRadius',
  'isSmoothEnabled', 'syncFromFrontEnd'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> Qt3DInput::Input::AxisSetting::axes() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::AxisSetting is created at the first use, not by
    'Qt3DInput::Input::AxisSetting(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::AxisSetting.
  - Each name of Qt's Qt3DInput::Input::AxisSetting that has no cute function
    yet, 'axes', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'Qt3DInput::Input::AxisSetting'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def deadZoneRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::AxisSetting::deadZoneRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axissetting.html#deadZoneRadius
    """
    #  float Qt3DInput::Input::AxisSetting::deadZoneRadius() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11AxisSetting14deadZoneRadiusEv',
    )

  def isSmoothEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::AxisSetting::isSmoothEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axissetting.html#isSmoothEnabled
    """
    #  bool Qt3DInput::Input::AxisSetting::isSmoothEnabled() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11AxisSetting15isSmoothEnabledEv',
    )

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
    'Qt3DInput::Input::AxisSetting::AxisSetting()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axissetting.html#AxisSetting
    """
    #  Qt3DInput::Input::AxisSetting::AxisSetting()
    self._noteCreation(AxisSetting, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input11AxisSettingC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::AxisSetting::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axissetting.html#cleanup
    """
    #  void Qt3DInput::Input::AxisSetting::cleanup()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input11AxisSetting7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::AxisSetting::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-axissetting.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::AxisSetting::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def axes(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DInput::Input::AxisSetting::axes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.AxisSetting.axes' has no cute function yet. Qt's "
        "'QList<int> Qt3DInput::Input::AxisSetting::axes() const': gives a "
        "type Python has no way to take yet.")
