"""
QQuickAgeAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickage_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAgeAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAgeAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickAgeAffector: a plain Python object standing in
  front of one C++ QQuickAgeAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's QQuickAgeAffector
  is built on Qt's QQuickParticleAffector, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAgeAffector that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'lifeLeft',
  'advancePosition', 'affectParticle', 'lifeLeftChanged',
  'advancePositionChanged', 'setLifeLeft', 'setAdvancePosition'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAgeAffector::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickAgeAffector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAgeAffector is created at the first use, not by
    'QQuickAgeAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAgeAffector.
  - Qt tells when it has removed the C++ QQuickAgeAffector. Every call on the
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
    Calls Qt's 'QString QQuickAgeAffector::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickageaffector.html#tr

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
    #  QString QQuickAgeAffector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickAgeAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAgeAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAgeAffector::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickageaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAgeAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickAgeAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lifeLeft(self) -> int:
    """
    Calls Qt's 'int QQuickAgeAffector::lifeLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickageaffector.html#lifeLeft
    """
    #  int QQuickAgeAffector::lifeLeft() const
    return self.uglySide.call('ritual_ZNK17QQuickAgeAffector8lifeLeftEv')

  def advancePosition(self) -> bool:
    """
    Calls Qt's 'bool QQuickAgeAffector::advancePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#advancePosition
    """
    #  bool QQuickAgeAffector::advancePosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickAgeAffector15advancePositionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLifeLeft(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAgeAffector::setLifeLeft(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickageaffector.html#setLifeLeft

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAgeAffector::setLifeLeft(int arg)
    self.uglySide.call('ritual_ZN17QQuickAgeAffector11setLifeLeftEi', arg)

  @overload(bool)
  def setAdvancePosition(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAgeAffector::setAdvancePosition(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#setAdvancePosition

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAgeAffector::setAdvancePosition(bool arg)
    self.uglySide.call(
        'ritual_ZN17QQuickAgeAffector18setAdvancePositionEb', arg,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAgeAffector::QQuickAgeAffector(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#QQuickAgeAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAgeAffector::QQuickAgeAffector(QQuickItem *parent)
    self._noteCreation(QQuickAgeAffector, lambda: Rituals.call(
        'ritual_ZN17QQuickAgeAffectorC1EP10QQuickItem',
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

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickAgeAffector::affectParticle(QQuickParticleData *d,
    qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickAgeAffector::affectParticle(QQuickParticleData *d, qreal
    #      dt)
    ritual = (
        'ritual_ZN17QQuickAgeAffector14affectParticleEP18QQuickParticleData'
        'd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickAgeAffector14affectParticleEP18QQuickPartic'
          'leDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(int)
  def lifeLeftChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAgeAffector::lifeLeftChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#lifeLeftChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAgeAffector::lifeLeftChanged(int arg)
    self.uglySide.call(
        'ritual_ZN17QQuickAgeAffector15lifeLeftChangedEi', arg,
    )

  @overload(bool)
  def advancePositionChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAgeAffector::advancePositionChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickageaffector.html#advancePositionChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAgeAffector::advancePositionChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN17QQuickAgeAffector22advancePositionChangedEb', arg,
    )
