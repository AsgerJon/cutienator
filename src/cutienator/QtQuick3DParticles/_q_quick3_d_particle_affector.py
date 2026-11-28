"""
QQuick3DParticleAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleaffector_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleAffector to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuick3DParticle, QQuick3DParticleData
  from . import QQuick3DParticleDataCurrent, QQuick3DParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticle = WAIT['QQuick3DParticle']
  QQuick3DParticleData = WAIT['QQuick3DParticleData']
  QQuick3DParticleDataCurrent = WAIT['QQuick3DParticleDataCurrent']
  QQuick3DParticleSystem = WAIT['QQuick3DParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleAffector(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DParticleAffector: a plain Python object
  standing in front of one C++ QQuick3DParticleAffector.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DParticleAffector is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleAffector that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'system',
  'enabled', 'appendParticle', 'particleCount', 'particle', 'clearParticles',
  'replaceParticle', 'removeLastParticle', 'setSystem', 'setEnabled',
  'update', 'systemChanged', 'enabledChanged', 'componentComplete',
  'prepareToAffect', 'affectParticle'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleAffector::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DParticleAffector::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuick3DParticleAffector::~QQuick3DParticleAffector()': the
    destructor: Python never removes a C++ QQuick3DParticleAffector.
  - Qt's 'QQmlListProperty<QQuick3DParticle>
    QQuick3DParticleAffector::particles()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DParticleAffector::appendParticle(
    QQmlListProperty<QQuick3DParticle> *a0, QQuick3DParticle *a1)': names
    'QQmlListProperty<QQuick3DParticle>', which has no cute class yet.
  - Qt's 'qsizetype QQuick3DParticleAffector::particleCount(
    QQmlListProperty<QQuick3DParticle> *a0)': names
    'QQmlListProperty<QQuick3DParticle>', which has no cute class yet.
  - Qt's 'QQuick3DParticle
    *QQuick3DParticleAffector::particle(QQmlListProperty<QQuick3DParticle>
    *a0, qsizetype a1)': names 'QQmlListProperty<QQuick3DParticle>', which
    has no cute class yet.
  - Qt's 'void QQuick3DParticleAffector::clearParticles(
    QQmlListProperty<QQuick3DParticle> *a0)': names
    'QQmlListProperty<QQuick3DParticle>', which has no cute class yet.
  - Qt's 'void QQuick3DParticleAffector::replaceParticle(
    QQmlListProperty<QQuick3DParticle> *a0, qsizetype a1, QQuick3DParticle
    *a2)': names 'QQmlListProperty<QQuick3DParticle>', which has no cute
    class yet.
  - Qt's 'void QQuick3DParticleAffector::removeLastParticle(
    QQmlListProperty<QQuick3DParticle> *a0)': names
    'QQmlListProperty<QQuick3DParticle>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleAffector is created at the first use, not by
    'QQuick3DParticleAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleAffector.
  - Qt tells when it has removed the C++ QQuick3DParticleAffector. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleAffector that has no cute function yet,
    'particles', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuick3DParticleAffector::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleaffector.html#tr

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
    #  QString QQuick3DParticleAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DParticleAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleAffector'

  #  A C++ QQuick3DParticleAffector Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleAffector'

  #  The functions Qt calls itself that QQuick3DParticleAffector is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'prepareToAffect': (
          ('_ZN24QQuick3DParticleAffector15prepareToAffectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'affectParticle': (
          ('_ZN24QQuick3DParticleAffector14affectParticleERK20QQuick3DParti'
           'cleDataP27QQuick3DParticleDataCurrentf',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'QtQuick3DParticles:QQuick3DParticleData'),
               ('address', 'address',
                'QtQuick3DParticles:QQuick3DParticleDataCurrent'),
               ('float', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def system(self) -> Optional[QQuick3DParticleSystem]:
    """
    Calls Qt's 'QQuick3DParticleSystem *QQuick3DParticleAffector::system()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#system

    Returns
    -------

    Optional[QQuick3DParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleSystem *QQuick3DParticleAffector::system() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleAffector6systemEv',
    )
    from . import QQuick3DParticleSystem
    return QQuick3DParticleSystem._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleAffector::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#enabled
    """
    #  bool QQuick3DParticleAffector::enabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleAffector7enabledEv',
    )

  def particleCount(self) -> int:
    """
    Calls Qt's 'qsizetype QQuick3DParticleAffector::particleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#particleCount
    """
    #  qsizetype QQuick3DParticleAffector::particleCount() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleAffector13particleCountEv',
    )

  @overload(int)
  def particle(self, a0: int) -> Optional[QQuick3DParticle]:
    """
    Calls Qt's 'QQuick3DParticle
    *QQuick3DParticleAffector::particle(qsizetype a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#particle

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DParticle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticle *QQuick3DParticleAffector::particle(qsizetype a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DParticleAffector8particleEx', a0,
    )
    from . import QQuick3DParticle
    return QQuick3DParticle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DParticleSystem)
  @overload(NoneType)
  def setSystem(self, system: Optional[QQuick3DParticleSystem]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleAffector::setSystem(QQuick3DParticleSystem *system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#setSystem

    Parameters
    ----------

    system : Optional[QQuick3DParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleAffector::setSystem(QQuick3DParticleSystem
    #      *system)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector9setSystemEP22QQuick3DParticleS'
        'ystem',
        self._addressOf(system),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleAffector::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector10setEnabledEb', enabled,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleAffector::QQuick3DParticleAffector(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleAffector::QQuick3DParticleAffector(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DParticleAffector, lambda: Rituals.call(
        'ritual_ZN24QQuick3DParticleAffectorC1EP12QQuick3DNode',
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

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def appendParticle(self, a0: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleAffector::appendParticle(QQuick3DParticle *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#appendParticle

    Parameters
    ----------

    a0 : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleAffector::appendParticle(QQuick3DParticle *a0)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector14appendParticleEP16QQuick3DPar'
        'ticle',
        self._addressOf(a0),
    )

  def clearParticles(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::clearParticles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#clearParticles
    """
    #  void QQuick3DParticleAffector::clearParticles()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector14clearParticlesEv',
    )

  @overload(int, QQuick3DParticle)
  @overload(int, NoneType)
  def replaceParticle(self, a0: int, a1: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::replaceParticle(qsizetype a0,
    QQuick3DParticle *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#replaceParticle

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleAffector::replaceParticle(qsizetype a0,
    #      QQuick3DParticle *a1)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector15replaceParticleExP16QQuick3DP'
        'article',
        a0, self._addressOf(a1),
    )

  def removeLastParticle(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::removeLastParticle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#removeLastParticle
    """
    #  void QQuick3DParticleAffector::removeLastParticle()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector18removeLastParticleEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#update
    """
    #  void QQuick3DParticleAffector::update()
    self.uglySide.call('ritual_ZN24QQuick3DParticleAffector6updateEv')

  def systemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::systemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#systemChanged
    """
    #  void QQuick3DParticleAffector::systemChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector13systemChangedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#enabledChanged
    """
    #  void QQuick3DParticleAffector::enabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector14enabledChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#componentComplete
    """
    #  void QQuick3DParticleAffector::componentComplete()
    ritual = 'ritual_ZN24QQuick3DParticleAffector17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuick3DParticleAffector17componentCompleteEv'
    self.uglySide.call(ritual)

  def prepareToAffect(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::prepareToAffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#prepareToAffect
    """
    #  void QQuick3DParticleAffector::prepareToAffect()
    ritual = 'ritual_ZN24QQuick3DParticleAffector15prepareToAffectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuick3DParticleAffector15prepareToAffectEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleData, QQuick3DParticleDataCurrent, float)
  @overload(QQuick3DParticleData, NoneType, float)
  def affectParticle(
      self,
      sd: QQuick3DParticleData,
      d: Optional[QQuick3DParticleDataCurrent],
      time: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleAffector::affectParticle(const
    QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleaffector.html#affectParticle

    Parameters
    ----------

    sd : QQuick3DParticleData
      Passed on as a value: Qt reads the C++ QQuick3DParticleData, which
      stays Python's own.

    d : Optional[QQuick3DParticleDataCurrent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleAffector::affectParticle(const
    #      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float
    #      time)
    self.uglySide.call(
        'ritual_ZN24QQuick3DParticleAffector14affectParticleERK20QQuick3DPa'
        'rticleDataP27QQuick3DParticleDataCurrentf',
        self._valueOf(sd), self._addressOf(d), time,
    )

  @staticmethod
  def particles(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DParticle>
    QQuick3DParticleAffector::particles()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleAffector.particles' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuick3DParticle> "
        "QQuick3DParticleAffector::particles()': gives a type Python has no "
        "way to take yet.")
