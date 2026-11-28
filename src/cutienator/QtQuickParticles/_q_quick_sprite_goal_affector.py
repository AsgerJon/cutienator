"""
QQuickSpriteGoalAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickspritegoal_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSpriteGoalAffector to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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
  from ..QtQuick import QQuickStochasticEngine
  from . import QQuickParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickStochasticEngine = WAIT['QQuickStochasticEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSpriteGoalAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickSpriteGoalAffector: a plain Python object
  standing in front of one C++ QQuickSpriteGoalAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickSpriteGoalAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSpriteGoalAffector that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'goalState',
  'jump', 'systemStates', 'affectParticle', 'goalStateChanged',
  'jumpChanged', 'systemStatesChanged', 'setGoalState', 'setJump',
  'setSystemStates', 'updateStateIndex'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSpriteGoalAffector::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickSpriteGoalAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSpriteGoalAffector is created at the first use, not by
    'QQuickSpriteGoalAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSpriteGoalAffector.
  - Qt tells when it has removed the C++ QQuickSpriteGoalAffector. Every call
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
    Calls Qt's 'QString QQuickSpriteGoalAffector::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritegoalaffector.html#tr

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
    #  QString QQuickSpriteGoalAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickSpriteGoalAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSpriteGoalAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSpriteGoalAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSpriteGoalAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSpriteGoalAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def goalState(self) -> str:
    """
    Calls Qt's 'QString QQuickSpriteGoalAffector::goalState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#goalState

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSpriteGoalAffector::goalState() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickSpriteGoalAffector9goalStateEv',
    )

  def jump(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteGoalAffector::jump() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspritegoalaffector.html#jump
    """
    #  bool QQuickSpriteGoalAffector::jump() const
    return self.uglySide.call('ritual_ZNK24QQuickSpriteGoalAffector4jumpEv')

  def systemStates(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpriteGoalAffector::systemStates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#systemStates
    """
    #  bool QQuickSpriteGoalAffector::systemStates() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickSpriteGoalAffector12systemStatesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setGoalState(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::setGoalState(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#setGoalState

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteGoalAffector::setGoalState(const QString &arg)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector12setGoalStateERK7QString', arg,
    )

  @overload(bool)
  def setJump(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::setJump(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#setJump

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteGoalAffector::setJump(bool arg)
    self.uglySide.call('ritual_ZN24QQuickSpriteGoalAffector7setJumpEb', arg)

  @overload(bool)
  def setSystemStates(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::setSystemStates(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#setSystemStates

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteGoalAffector::setSystemStates(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector15setSystemStatesEb', arg,
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
    'QQuickSpriteGoalAffector::QQuickSpriteGoalAffector(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpriteGoalAffector::QQuickSpriteGoalAffector(QQuickItem *parent)
    self._noteCreation(QQuickSpriteGoalAffector, lambda: Rituals.call(
        'ritual_ZN24QQuickSpriteGoalAffectorC1EP10QQuickItem',
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
    QQuickSpriteGoalAffector::affectParticle(QQuickParticleData *d, qreal
    dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickSpriteGoalAffector::affectParticle(QQuickParticleData *d,
    #      qreal dt)
    ritual = (
        'ritual_ZN24QQuickSpriteGoalAffector14affectParticleEP18QQuickParti'
        'cleDatad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickSpriteGoalAffector14affectParticleEP18QQuic'
          'kParticleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(str)
  def goalStateChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::goalStateChanged(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#goalStateChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSpriteGoalAffector::goalStateChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector16goalStateChangedERK7QString',
        arg,
    )

  @overload(bool)
  def jumpChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::jumpChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#jumpChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteGoalAffector::jumpChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector11jumpChangedEb', arg,
    )

  @overload(bool)
  def systemStatesChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSpriteGoalAffector::systemStatesChanged(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#systemStatesChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSpriteGoalAffector::systemStatesChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector19systemStatesChangedEb', arg,
    )

  @overload(QQuickStochasticEngine)
  @overload(NoneType)
  def updateStateIndex(self, e: Optional[QQuickStochasticEngine]) -> None:
    """
    Calls Qt's 'void
    QQuickSpriteGoalAffector::updateStateIndex(QQuickStochasticEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspritegoalaffector.html#updateStateIndex

    Parameters
    ----------

    e : Optional[QQuickStochasticEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpriteGoalAffector::updateStateIndex(QQuickStochasticEngine
    #      *e)
    self.uglySide.call(
        'ritual_ZN24QQuickSpriteGoalAffector16updateStateIndexEP22QQuickSto'
        'chasticEngine',
        self._addressOf(e),
    )
