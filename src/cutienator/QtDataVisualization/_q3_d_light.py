"""
Q3DLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dlight.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import Q3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DLight(Q3DObject):
  """
  The cute side of Qt's Q3DLight: a plain Python object standing in front of
  one C++ Q3DLight.

  It is built on the cute 'Q3DObject', as Qt's Q3DLight is built on Qt's
  Q3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DLight that has a ritual and that Python can call
  so far, 5 names in all: 'metaObject', 'tr', 'setAutoPosition',
  'isAutoPosition', 'autoPositionChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DLight::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Q3DLight::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DLight::~Q3DLight()': the destructor: Python never removes a C++
    Q3DLight.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DLight is created at the first use, not by 'Q3DLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DLight.
  - Qt tells when it has removed the C++ Q3DLight. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString Q3DLight::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#tr

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
    #  QString Q3DLight::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Q3DLight2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DLight'

  #  A C++ Q3DLight Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DLight::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DLight::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Q3DLight10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoPosition(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Q3DLight::setAutoPosition(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#setAutoPosition

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Q3DLight::setAutoPosition(bool enabled)
    self.uglySide.call('ritual_ZN8Q3DLight15setAutoPositionEb', enabled)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'Q3DLight::Q3DLight(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#Q3DLight

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DLight::Q3DLight(QObject *parent)
    self._noteCreation(Q3DLight, lambda: Rituals.call(
        'ritual_ZN8Q3DLightC1EP7QObject', self._addressOf(parent, 'QObject'),
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

  def isAutoPosition(self) -> bool:
    """
    Calls Qt's 'bool Q3DLight::isAutoPosition()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#isAutoPosition
    """
    #  bool Q3DLight::isAutoPosition()
    return self.uglySide.call('ritual_ZN8Q3DLight14isAutoPositionEv')

  @overload(bool)
  def autoPositionChanged(self, autoPosition: bool) -> None:
    """
    Calls Qt's 'void Q3DLight::autoPositionChanged(bool autoPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dlight.html#autoPositionChanged

    Parameters
    ----------

    autoPosition : bool
      Passed on as it is.
    """
    #  void Q3DLight::autoPositionChanged(bool autoPosition)
    self.uglySide.call(
        'ritual_ZN8Q3DLight19autoPositionChangedEb', autoPosition,
    )
