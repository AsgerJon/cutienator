"""
QQuickFrictionAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickfriction_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFrictionAffector to be private: it declares the class in a
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


class QQuickFrictionAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickFrictionAffector: a plain Python object
  standing in front of one C++ QQuickFrictionAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickFrictionAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFrictionAffector that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'factor',
  'threshold', 'affectParticle', 'factorChanged', 'thresholdChanged',
  'setFactor', 'setThreshold'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFrictionAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFrictionAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFrictionAffector is created at the first use, not by
    'QQuickFrictionAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFrictionAffector.
  - Qt tells when it has removed the C++ QQuickFrictionAffector. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickFrictionAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfrictionaffector.html#tr

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
    #  QString QQuickFrictionAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickFrictionAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFrictionAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFrictionAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFrictionAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickFrictionAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def factor(self) -> float:
    """
    Calls Qt's 'qreal QQuickFrictionAffector::factor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfrictionaffector.html#factor
    """
    #  qreal QQuickFrictionAffector::factor() const
    return self.uglySide.call('ritual_ZNK22QQuickFrictionAffector6factorEv')

  def threshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickFrictionAffector::threshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#threshold
    """
    #  qreal QQuickFrictionAffector::threshold() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickFrictionAffector9thresholdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFactor(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickFrictionAffector::setFactor(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#setFactor

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickFrictionAffector::setFactor(qreal arg)
    self.uglySide.call('ritual_ZN22QQuickFrictionAffector9setFactorEd', arg)

  @overload(float)
  def setThreshold(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickFrictionAffector::setThreshold(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#setThreshold

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickFrictionAffector::setThreshold(qreal arg)
    self.uglySide.call(
        'ritual_ZN22QQuickFrictionAffector12setThresholdEd', arg,
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
    'QQuickFrictionAffector::QQuickFrictionAffector(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#QQuickFrictionAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFrictionAffector::QQuickFrictionAffector(QQuickItem *parent)
    self._noteCreation(QQuickFrictionAffector, lambda: Rituals.call(
        'ritual_ZN22QQuickFrictionAffectorC1EP10QQuickItem',
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
    Calls Qt's 'bool
    QQuickFrictionAffector::affectParticle(QQuickParticleData *d, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickFrictionAffector::affectParticle(QQuickParticleData *d,
    #      qreal dt)
    ritual = (
        'ritual_ZN22QQuickFrictionAffector14affectParticleEP18QQuickParticl'
        'eDatad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickFrictionAffector14affectParticleEP18QQuickP'
          'articleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(float)
  def factorChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickFrictionAffector::factorChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#factorChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickFrictionAffector::factorChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN22QQuickFrictionAffector13factorChangedEd', arg,
    )

  @overload(float)
  def thresholdChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickFrictionAffector::thresholdChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfrictionaffector.html#thresholdChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickFrictionAffector::thresholdChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN22QQuickFrictionAffector16thresholdChangedEd', arg,
    )
