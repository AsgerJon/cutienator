"""
Qt3DInput::QAxisSetting binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qaxissetting.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAxisSetting(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DInput::QAxisSetting: a plain Python object
  standing in front of one C++ Qt3DInput::QAxisSetting.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DInput::QAxisSetting
  is built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAxisSetting that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'deadZoneRadius', 'isSmoothEnabled', 'setDeadZoneRadius',
  'setSmoothEnabled', 'deadZoneRadiusChanged', 'smoothChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAxisSetting::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QAxisSetting::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAxisSetting::~QAxisSetting()': the destructor: Python
    never removes a C++ Qt3DInput::QAxisSetting.
  - Qt's 'QList<int> Qt3DInput::QAxisSetting::axes() const': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DInput::QAxisSetting::setAxes(const QList<int> &axes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DInput::QAxisSetting::axesChanged(const QList<int> &axes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QAxisSettingPrivate *Qt3DInput::QAxisSetting::d_func()
    const': takes in Python what 'QAxisSettingPrivate
    *Qt3DInput::QAxisSetting::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAxisSetting is created at the first use, not by
    'Qt3DInput::QAxisSetting(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAxisSetting.
  - Qt tells when it has removed the C++ Qt3DInput::QAxisSetting. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAxisSetting that has no cute function yet,
    'axes', 'axesChanged', 'setAxes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DInput::QAxisSetting::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DInput::QAxisSetting::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput12QAxisSetting2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAxisSetting'

  #  A C++ Qt3DInput::QAxisSetting Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAxisSetting'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QAxisSetting::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAxisSetting::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QAxisSetting10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def deadZoneRadius(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QAxisSetting::deadZoneRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#deadZoneRadius
    """
    #  float Qt3DInput::QAxisSetting::deadZoneRadius() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QAxisSetting14deadZoneRadiusEv',
    )

  def isSmoothEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QAxisSetting::isSmoothEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#isSmoothEnabled
    """
    #  bool Qt3DInput::QAxisSetting::isSmoothEnabled() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput12QAxisSetting15isSmoothEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDeadZoneRadius(self, deadZoneRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisSetting::setDeadZoneRadius(float
    deadZoneRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#setDeadZoneRadius

    Parameters
    ----------

    deadZoneRadius : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisSetting::setDeadZoneRadius(float deadZoneRadius)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QAxisSetting17setDeadZoneRadiusEf',
        deadZoneRadius,
    )

  @overload(bool)
  def setSmoothEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisSetting::setSmoothEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#setSmoothEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisSetting::setSmoothEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QAxisSetting16setSmoothEnabledEb', enabled,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAxisSetting::QAxisSetting(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#QAxisSetting

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QAxisSetting::QAxisSetting(Qt3DCore::QNode *parent)
    self._noteCreation(QAxisSetting, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput12QAxisSettingC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(float)
  def deadZoneRadiusChanged(self, deadZoneRadius: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisSetting::deadZoneRadiusChanged(float
    deadZoneRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#deadZoneRadiusChanged

    Parameters
    ----------

    deadZoneRadius : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisSetting::deadZoneRadiusChanged(float
    #      deadZoneRadius)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QAxisSetting21deadZoneRadiusChangedEf',
        deadZoneRadius,
    )

  @overload(bool)
  def smoothChanged(self, smooth: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxisSetting::smoothChanged(bool smooth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#smoothChanged

    Parameters
    ----------

    smooth : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QAxisSetting::smoothChanged(bool smooth)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput12QAxisSetting13smoothChangedEb', smooth,
    )

  def d_func(self) -> Optional[Qt3DInput.QAxisSettingPrivate]:
    """
    Calls Qt's 'QAxisSettingPrivate *Qt3DInput::QAxisSetting::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxissetting.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAxisSettingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAxisSettingPrivate *Qt3DInput::QAxisSetting::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput12QAxisSetting6d_funcEv',
    )
    return Qt3DInput.QAxisSettingPrivate._cuteAt(address)

  @staticmethod
  def axes(*__, **_) -> Never:
    """
    Qt's 'QList<int> Qt3DInput::QAxisSetting::axes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAxisSetting.axes' has no cute function yet. Qt's "
        "'QList<int> Qt3DInput::QAxisSetting::axes() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def axesChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QAxisSetting::axesChanged(const QList<int> &axes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAxisSetting.axesChanged' has no cute function yet. "
        "Qt's 'void Qt3DInput::QAxisSetting::axesChanged(const QList<int> "
        "&axes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setAxes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::QAxisSetting::setAxes(const QList<int> &axes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAxisSetting.setAxes' has no cute function yet. Qt's "
        "'void Qt3DInput::QAxisSetting::setAxes(const QList<int> &axes)': "
        "takes a type Python has no way to hand over yet.")
