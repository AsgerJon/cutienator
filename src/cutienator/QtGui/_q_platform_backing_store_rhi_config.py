"""
QPlatformBackingStoreRhiConfig binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QPlatformBackingStoreRhiConfig(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformBackingStoreRhiConfig: a plain Python object
  standing in front of one C++ QPlatformBackingStoreRhiConfig.

  C++ hands a QPlatformBackingStoreRhiConfig around as a copy, so every C++
  QPlatformBackingStoreRhiConfig behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPlatformBackingStoreRhiConfig that has a ritual and
  that Python can call so far, 7 names in all: 'isEnabled', 'setEnabled',
  'api', 'setApi', 'isDebugLayerEnabled', 'setDebugLayer', '__eq__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformBackingStoreRhiConfig::~QPlatformBackingStoreRhiConfig()':
    the destructor: Python removes its C++ QPlatformBackingStoreRhiConfig by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlatformBackingStoreRhiConfig is created at the first use, not
    by 'QPlatformBackingStoreRhiConfig(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformBackingStoreRhiConfig back gives a copy the
    ritual made for Python, in a new cute QPlatformBackingStoreRhiConfig.
  """

  #  The enums Qt writes inside QPlatformBackingStoreRhiConfig, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Api(CuteNum):
    """
    The enum 'QPlatformBackingStoreRhiConfig::Api' of Qt, with the 6 names Qt
    gives in it.
    """

    OpenGL = Kee[int](0)
    Metal = Kee[int](1)
    Vulkan = Kee[int](2)
    D3D11 = Kee[int](3)
    D3D12 = Kee[int](4)
    Null = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformBackingStoreRhiConfig'

  #  Qt's '~QPlatformBackingStoreRhiConfig()'. Naming it makes this a value
  #  class: Python owns every C++ QPlatformBackingStoreRhiConfig behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QPlatformBackingStoreRhiConfigD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPlatformBackingStoreRhiConfig::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#isEnabled
    """
    #  bool QPlatformBackingStoreRhiConfig::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK30QPlatformBackingStoreRhiConfig9isEnabledEv',
    )

  def api(self) -> Api:
    """
    Calls Qt's 'Api QPlatformBackingStoreRhiConfig::api() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#api

    Returns
    -------

    Api
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Api(number)' gives.
    """
    #  Api QPlatformBackingStoreRhiConfig::api() const
    return QPlatformBackingStoreRhiConfig.Api(self.uglySide.call(
        'ritual_ZNK30QPlatformBackingStoreRhiConfig3apiEv',
    ))

  def isDebugLayerEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPlatformBackingStoreRhiConfig::isDebugLayerEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html
    """
    #  bool QPlatformBackingStoreRhiConfig::isDebugLayerEnabled() const
    return self.uglySide.call(
        'ritual_ZNK30QPlatformBackingStoreRhiConfig19isDebugLayerEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPlatformBackingStoreRhiConfig::setEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#setEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPlatformBackingStoreRhiConfig::setEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN30QPlatformBackingStoreRhiConfig10setEnabledEb', enable,
    )

  @overload(Api)
  def setApi(self, api: Api) -> None:
    """
    Calls Qt's 'void QPlatformBackingStoreRhiConfig::setApi(Api api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#setApi

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  void QPlatformBackingStoreRhiConfig::setApi(Api api)
    self.uglySide.call(
        'ritual_ZN30QPlatformBackingStoreRhiConfig6setApiENS_3ApiE',
        api.value,
    )

  @overload(bool)
  def setDebugLayer(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPlatformBackingStoreRhiConfig::setDebugLayer(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#setDebugLayer

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPlatformBackingStoreRhiConfig::setDebugLayer(bool enable)
    self.uglySide.call(
        'ritual_ZN30QPlatformBackingStoreRhiConfig13setDebugLayerEb', enable,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QPlatformBackingStoreRhiConfig) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlatformBackingStoreRhiConfig &a,
    const QPlatformBackingStoreRhiConfig &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html#operator==

    Parameters
    ----------

    b : QPlatformBackingStoreRhiConfig
      Passed on as a value: Qt reads the C++ QPlatformBackingStoreRhiConfig,
      which stays Python's own.
    """
    #  bool operator==(const QPlatformBackingStoreRhiConfig &a, const
    #      QPlatformBackingStoreRhiConfig &b)
    return Rituals.call(
        'ritual_ZeqRK30QPlatformBackingStoreRhiConfigS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html
    """
    #  QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig()
    self._noteCreation(QPlatformBackingStoreRhiConfig, lambda: Rituals.call(
        'ritual_ZN30QPlatformBackingStoreRhiConfigC1Ev',
    ))

  @overload(Api)
  def __init__(self, api: Api) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig(Api
    api)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformbackingstorerhiconfig.html

    Parameters
    ----------

    api : Api
      Passed on as its number.
    """
    #  QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig(Api
    #      api)
    self._noteCreation(QPlatformBackingStoreRhiConfig, lambda: Rituals.call(
        'ritual_ZN30QPlatformBackingStoreRhiConfigC1ENS_3ApiE', api.value,
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
