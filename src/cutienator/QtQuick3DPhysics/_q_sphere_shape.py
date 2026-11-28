"""
QSphereShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qsphereshape_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSphereShape to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractCollisionShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSphereShape(QAbstractCollisionShape):
  """
  The cute side of Qt's QSphereShape: a plain Python object standing in front
  of one C++ QSphereShape.

  It is built on the cute 'QAbstractCollisionShape', as Qt's QSphereShape is
  built on Qt's QAbstractCollisionShape, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSphereShape that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'diameter',
  'isStaticShape', 'setDiameter', 'diameterChanged', 'updatePhysXGeometry'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSphereShape::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSphereShape::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSphereShape::~QSphereShape()': the destructor: Python never
    removes a C++ QSphereShape.
  - Qt's 'physx::PxGeometry *QSphereShape::getPhysXGeometry()': gives
    'physx::PxGeometry', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSphereShape is created at the first use, not by
    'QSphereShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSphereShape.
  - Qt tells when it has removed the C++ QSphereShape. Every call on the cute
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
    Calls Qt's 'QString QSphereShape::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#tr

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
    #  QString QSphereShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QSphereShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSphereShape'

  #  A C++ QSphereShape Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSphereShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSphereShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSphereShape::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QSphereShape10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def diameter(self) -> float:
    """
    Calls Qt's 'float QSphereShape::diameter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#diameter
    """
    #  float QSphereShape::diameter() const
    return self.uglySide.call('ritual_ZNK12QSphereShape8diameterEv')

  def isStaticShape(self) -> bool:
    """
    Calls Qt's 'bool QSphereShape::isStaticShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#isStaticShape
    """
    #  bool QSphereShape::isStaticShape() const
    ritual = 'ritual_ZNK12QSphereShape13isStaticShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QSphereShape13isStaticShapeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDiameter(self, diameter: float) -> None:
    """
    Calls Qt's 'void QSphereShape::setDiameter(float diameter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#setDiameter

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void QSphereShape::setDiameter(float diameter)
    self.uglySide.call('ritual_ZN12QSphereShape11setDiameterEf', diameter)

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
    Notes what was given, for Qt's 'QSphereShape::QSphereShape()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#QSphereShape
    """
    #  QSphereShape::QSphereShape()
    self._noteCreation(QSphereShape, lambda: Rituals.call(
        'ritual_ZN12QSphereShapeC1Ev',
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
  def diameterChanged(self, diameter: float) -> None:
    """
    Calls Qt's 'void QSphereShape::diameterChanged(float diameter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsphereshape.html#diameterChanged

    Parameters
    ----------

    diameter : float
      Passed on as it is.
    """
    #  void QSphereShape::diameterChanged(float diameter)
    self.uglySide.call(
        'ritual_ZN12QSphereShape15diameterChangedEf', diameter,
    )

  def updatePhysXGeometry(self) -> None:
    """
    Calls Qt's 'void QSphereShape::updatePhysXGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsphereshape.html#updatePhysXGeometry
    """
    #  void QSphereShape::updatePhysXGeometry()
    self.uglySide.call('ritual_ZN12QSphereShape19updatePhysXGeometryEv')
