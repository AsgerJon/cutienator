"""
QQuick3DXrSimpleHapticEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrSimpleHapticEffect to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQuick3DXrAbstractHapticEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DXrSimpleHapticEffect(QQuick3DXrAbstractHapticEffect):
  """
  The cute side of Qt's QQuick3DXrSimpleHapticEffect: a plain Python object
  standing in front of one C++ QQuick3DXrSimpleHapticEffect.

  It is built on the cute 'QQuick3DXrAbstractHapticEffect', as Qt's
  QQuick3DXrSimpleHapticEffect is built on Qt's
  QQuick3DXrAbstractHapticEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrSimpleHapticEffect that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'amplitude',
  'duration', 'frequency', 'amplitudeChanged', 'durationChanged',
  'frequencyChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrSimpleHapticEffect::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DXrSimpleHapticEffect::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 4 leans on
  'QQuick3DXrSimpleHapticEffect; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrSimpleHapticEffect is created at the first use, not by
    'QQuick3DXrSimpleHapticEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrSimpleHapticEffect.
  - Qt tells when it has removed the C++ QQuick3DXrSimpleHapticEffect. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrSimpleHapticEffect that has no cute function
    yet, 'setAmplitude', 'setDuration', 'setFrequency', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrSimpleHapticEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DXrSimpleHapticEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  def amplitude(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrSimpleHapticEffect::amplitude()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#amplitude
    """
    #  float QQuick3DXrSimpleHapticEffect::amplitude()
    return self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv',
    )

  def duration(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrSimpleHapticEffect::duration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#duration
    """
    #  float QQuick3DXrSimpleHapticEffect::duration()
    return self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect8durationEv',
    )

  def frequency(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrSimpleHapticEffect::frequency()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#frequency
    """
    #  float QQuick3DXrSimpleHapticEffect::frequency()
    return self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect9frequencyEv',
    )

  def amplitudeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSimpleHapticEffect::amplitudeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#amplitudeChanged
    """
    #  void QQuick3DXrSimpleHapticEffect::amplitudeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect16amplitudeChangedEv',
    )

  def durationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSimpleHapticEffect::durationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#durationChanged
    """
    #  void QQuick3DXrSimpleHapticEffect::durationChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect15durationChangedEv',
    )

  def frequencyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSimpleHapticEffect::frequencyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrsimplehapticeffect.html#frequencyChanged
    """
    #  void QQuick3DXrSimpleHapticEffect::frequencyChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DXrSimpleHapticEffect16frequencyChangedEv',
    )

  @staticmethod
  def setAmplitude(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSimpleHapticEffect::setAmplitude(float
    newAmplitude)': leans on
    'QQuick3DXrSimpleHapticEffect::amplitudeChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSimpleHapticEffect.setAmplitude' has no cute function "
        "yet. Qt's 'void QQuick3DXrSimpleHapticEffect::setAmplitude(float "
        "newAmplitude)': leans on "
        "'QQuick3DXrSimpleHapticEffect::amplitudeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDuration(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSimpleHapticEffect::setDuration(float newDuration)':
    leans on 'QQuick3DXrSimpleHapticEffect::durationChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSimpleHapticEffect.setDuration' has no cute function "
        "yet. Qt's 'void QQuick3DXrSimpleHapticEffect::setDuration(float "
        "newDuration)': leans on "
        "'QQuick3DXrSimpleHapticEffect::durationChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFrequency(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSimpleHapticEffect::setFrequency(float
    newFrequency)': leans on
    'QQuick3DXrSimpleHapticEffect::frequencyChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSimpleHapticEffect.setFrequency' has no cute function "
        "yet. Qt's 'void QQuick3DXrSimpleHapticEffect::setFrequency(float "
        "newFrequency)': leans on "
        "'QQuick3DXrSimpleHapticEffect::frequencyChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
