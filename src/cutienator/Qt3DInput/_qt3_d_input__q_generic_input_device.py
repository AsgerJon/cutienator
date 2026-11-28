"""
Qt3DInput::QGenericInputDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qgenericinputdevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::QGenericInputDevice to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGenericInputDevice(Qt3DInput.QAbstractPhysicalDevice):
  """
  The cute side of Qt's Qt3DInput::QGenericInputDevice: a plain Python object
  standing in front of one C++ Qt3DInput::QGenericInputDevice.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDevice', as Qt's
  Qt3DInput::QGenericInputDevice is built on Qt's
  Qt3DInput::QAbstractPhysicalDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QGenericInputDevice that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'axesMap',
  'setAxesMap', 'buttonsMap', 'setButtonsMap', 'axesMapChanged',
  'buttonsMapChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QGenericInputDevice::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QGenericInputDevice::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QGenericInputDevice is created at the first use, not
    by 'Qt3DInput::QGenericInputDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QGenericInputDevice.
  - Qt tells when it has removed the C++ Qt3DInput::QGenericInputDevice.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DInput::QGenericInputDevice::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#tr

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
    #  QString Qt3DInput::QGenericInputDevice::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput19QGenericInputDevice2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QGenericInputDevice'

  #  A C++ Qt3DInput::QGenericInputDevice Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QGenericInputDevice'

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
    *Qt3DInput::QGenericInputDevice::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QGenericInputDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput19QGenericInputDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axesMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap Qt3DInput::QGenericInputDevice::axesMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#axesMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap Qt3DInput::QGenericInputDevice::axesMap() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput19QGenericInputDevice7axesMapEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def buttonsMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap Qt3DInput::QGenericInputDevice::buttonsMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#buttonsMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap Qt3DInput::QGenericInputDevice::buttonsMap() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput19QGenericInputDevice10buttonsMapEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setAxesMap(self, axesMap: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGenericInputDevice::setAxesMap(const
    QVariantMap &axesMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#setAxesMap

    Parameters
    ----------

    axesMap : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void Qt3DInput::QGenericInputDevice::setAxesMap(const QVariantMap
    #      &axesMap)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput19QGenericInputDevice10setAxesMapERK4QMapI7QStr'
        'ing8QVariantE',
        self._valueOf(axesMap),
    )

  @overload(QMap[str, QVariant])
  def setButtonsMap(self, buttonsMap: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGenericInputDevice::setButtonsMap(const
    QVariantMap &buttonsMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#setButtonsMap

    Parameters
    ----------

    buttonsMap : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void Qt3DInput::QGenericInputDevice::setButtonsMap(const QVariantMap
    #      &buttonsMap)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput19QGenericInputDevice13setButtonsMapERK4QMapI7Q'
        'String8QVariantE',
        self._valueOf(buttonsMap),
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
    'Qt3DInput::QGenericInputDevice::QGenericInputDevice(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QGenericInputDevice::QGenericInputDevice(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QGenericInputDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput19QGenericInputDeviceC1EPN8Qt3DCore5QNodeE',
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

  def axesMapChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGenericInputDevice::axesMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html#axesMapChanged
    """
    #  void Qt3DInput::QGenericInputDevice::axesMapChanged()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput19QGenericInputDevice14axesMapChangedEv',
    )

  def buttonsMapChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::QGenericInputDevice::buttonsMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qgenericinputdevice.html
    """
    #  void Qt3DInput::QGenericInputDevice::buttonsMapChanged()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput19QGenericInputDevice17buttonsMapChangedEv',
    )
