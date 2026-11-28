"""
QPhysicsMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPhysicsMaterial to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPhysicsMaterial(QObject):
  """
  The cute side of Qt's QPhysicsMaterial: a plain Python object standing in
  front of one C++ QPhysicsMaterial.

  It is built on the cute 'QObject', as Qt's QPhysicsMaterial is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPhysicsMaterial that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'staticFriction',
  'setStaticFriction', 'dynamicFriction', 'setDynamicFriction',
  'restitution', 'setRestitution', 'staticFrictionChanged',
  'dynamicFrictionChanged', 'restitutionChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPhysicsMaterial::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPhysicsMaterial::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPhysicsMaterial is created at the first use, not by
    'QPhysicsMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPhysicsMaterial.
  - Qt tells when it has removed the C++ QPhysicsMaterial. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPhysicsMaterial::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsmaterial.html#tr

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
    #  QString QPhysicsMaterial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPhysicsMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPhysicsMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPhysicsMaterial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPhysicsMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPhysicsMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def staticFriction(self) -> float:
    """
    Calls Qt's 'float QPhysicsMaterial::staticFriction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#staticFriction
    """
    #  float QPhysicsMaterial::staticFriction() const
    return self.uglySide.call(
        'ritual_ZNK16QPhysicsMaterial14staticFrictionEv',
    )

  def dynamicFriction(self) -> float:
    """
    Calls Qt's 'float QPhysicsMaterial::dynamicFriction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#dynamicFriction
    """
    #  float QPhysicsMaterial::dynamicFriction() const
    return self.uglySide.call(
        'ritual_ZNK16QPhysicsMaterial15dynamicFrictionEv',
    )

  def restitution(self) -> float:
    """
    Calls Qt's 'float QPhysicsMaterial::restitution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsmaterial.html#restitution
    """
    #  float QPhysicsMaterial::restitution() const
    return self.uglySide.call('ritual_ZNK16QPhysicsMaterial11restitutionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStaticFriction(self, staticFriction: float) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::setStaticFriction(float
    staticFriction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#setStaticFriction

    Parameters
    ----------

    staticFriction : float
      Passed on as it is.
    """
    #  void QPhysicsMaterial::setStaticFriction(float staticFriction)
    self.uglySide.call(
        'ritual_ZN16QPhysicsMaterial17setStaticFrictionEf', staticFriction,
    )

  @overload(float)
  def setDynamicFriction(self, dynamicFriction: float) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::setDynamicFriction(float
    dynamicFriction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#setDynamicFriction

    Parameters
    ----------

    dynamicFriction : float
      Passed on as it is.
    """
    #  void QPhysicsMaterial::setDynamicFriction(float dynamicFriction)
    self.uglySide.call(
        'ritual_ZN16QPhysicsMaterial18setDynamicFrictionEf', dynamicFriction,
    )

  @overload(float)
  def setRestitution(self, restitution: float) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::setRestitution(float restitution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#setRestitution

    Parameters
    ----------

    restitution : float
      Passed on as it is.
    """
    #  void QPhysicsMaterial::setRestitution(float restitution)
    self.uglySide.call(
        'ritual_ZN16QPhysicsMaterial14setRestitutionEf', restitution,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPhysicsMaterial::QPhysicsMaterial(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#QPhysicsMaterial

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPhysicsMaterial::QPhysicsMaterial(QObject *parent)
    self._noteCreation(QPhysicsMaterial, lambda: Rituals.call(
        'ritual_ZN16QPhysicsMaterialC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def staticFrictionChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::staticFrictionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#staticFrictionChanged
    """
    #  void QPhysicsMaterial::staticFrictionChanged()
    self.uglySide.call(
        'ritual_ZN16QPhysicsMaterial21staticFrictionChangedEv',
    )

  def dynamicFrictionChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::dynamicFrictionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#dynamicFrictionChanged
    """
    #  void QPhysicsMaterial::dynamicFrictionChanged()
    self.uglySide.call(
        'ritual_ZN16QPhysicsMaterial22dynamicFrictionChangedEv',
    )

  def restitutionChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsMaterial::restitutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsmaterial.html#restitutionChanged
    """
    #  void QPhysicsMaterial::restitutionChanged()
    self.uglySide.call('ritual_ZN16QPhysicsMaterial18restitutionChangedEv')
