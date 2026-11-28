"""
QQuick3DParticleModelParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleModelParticle to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DObject
from . import QQuick3DParticle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector3D
  from ..QtQml import QQmlComponent
  from ..QtQuick3D import QQuick3DInstancing, QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQmlComponent = WAIT['QQmlComponent']
  QQuick3DNode = WAIT['QQuick3DNode']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleModelParticle(QQuick3DParticle):
  """
  The cute side of Qt's QQuick3DParticleModelParticle: a plain Python object
  standing in front of one C++ QQuick3DParticleModelParticle.

  It is built on the cute 'QQuick3DParticle', as Qt's
  QQuick3DParticleModelParticle is built on Qt's QQuick3DParticle, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleModelParticle that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject', 'tr',
  'delegate', 'instanceTable', 'setDelegate', 'delegateChanged',
  'instanceTableChanged', 'componentComplete', 'itemChange', 'setDepthBias',
  'regenerate', 'handleMaxAmountChanged', 'handleSortModeChanged',
  'clearInstanceTable', 'addInstance', 'commitInstance', 'updateDepthBias'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleModelParticle::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleModelParticle::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleModelParticle is created at the first use, not by
    'QQuick3DParticleModelParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleModelParticle.
  - Qt tells when it has removed the C++ QQuick3DParticleModelParticle. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DParticleModelParticle::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#tr

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
    #  QString QQuick3DParticleModelParticle::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuick3DParticleModelParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleModelParticle'

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
    *QQuick3DParticleModelParticle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleModelParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleModelParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuick3DParticleModelParticle::delegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuick3DParticleModelParticle::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleModelParticle8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def instanceTable(self) -> Optional[QQuick3DInstancing]:
    """
    Calls Qt's 'QQuick3DInstancing
    *QQuick3DParticleModelParticle::instanceTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#instanceTable

    Returns
    -------

    Optional[QQuick3DInstancing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancing *QQuick3DParticleModelParticle::instanceTable()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuick3DParticleModelParticle13instanceTableEv',
    )
    from ..QtQuick3D import QQuick3DInstancing
    return QQuick3DInstancing._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleModelParticle::setDelegate(QQmlComponent
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle11setDelegateEP13QQmlCompo'
        'nent',
        self._addressOf(delegate),
    )

  @overload(float)
  def setDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::setDepthBias(float
    bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#setDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DParticleModelParticle::setDepthBias(float bias)
    ritual = 'ritual_ZN29QQuick3DParticleModelParticle12setDepthBiasEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QQuick3DParticleModelParticle12setDepthBiasEf'
    self.uglySide.call(ritual, bias)

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
    'QQuick3DParticleModelParticle::QQuick3DParticleModelParticle(
    QQuick3DNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleModelParticle::QQuick3DParticleModelParticle(
    #      QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleModelParticle, lambda: Rituals.call(
        'ritual_ZN29QQuick3DParticleModelParticleC1EP12QQuick3DNode',
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

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#delegateChanged
    """
    #  void QQuick3DParticleModelParticle::delegateChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle15delegateChangedEv',
    )

  def instanceTableChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::instanceTableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html
    """
    #  void QQuick3DParticleModelParticle::instanceTableChanged()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle20instanceTableChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html
    """
    #  void QQuick3DParticleModelParticle::componentComplete()
    ritual = 'ritual_ZN29QQuick3DParticleModelParticle17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuick3DParticleModelParticle17componentCompleteE'
          'v')
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      change: QQuick3DObject.ItemChange,
      value: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::itemChange(ItemChange
    change, const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#itemChange

    Parameters
    ----------

    change : QQuick3DObject.ItemChange
      Passed on as its number.

    value : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DParticleModelParticle::itemChange(ItemChange change,
    #      const ItemChangeData &value)
    ritual = (
        'ritual_ZN29QQuick3DParticleModelParticle10itemChangeEN14QQuick3DOb'
        'ject10ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuick3DParticleModelParticle10itemChangeEN14QQui'
          'ck3DObject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def regenerate(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::regenerate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#regenerate
    """
    #  void QQuick3DParticleModelParticle::regenerate()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle10regenerateEv',
    )

  @overload(int)
  def handleMaxAmountChanged(self, amount: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelParticle::handleMaxAmountChanged(int amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleModelParticle::handleMaxAmountChanged(int amount)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle22handleMaxAmountChangedEi',
        amount,
    )

  @overload(QQuick3DParticle.SortMode)
  def handleSortModeChanged(self, mode: QQuick3DParticle.SortMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelParticle::handleSortModeChanged(QQuick3DParticle::
    SortMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html

    Parameters
    ----------

    mode : QQuick3DParticle.SortMode
      Passed on as its number.
    """
    #  void QQuick3DParticleModelParticle::handleSortModeChanged(
    #      QQuick3DParticle::SortMode mode)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle21handleSortModeChangedEN1'
        '6QQuick3DParticle8SortModeE',
        mode.value,
    )

  def clearInstanceTable(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::clearInstanceTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html
    """
    #  void QQuick3DParticleModelParticle::clearInstanceTable()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle18clearInstanceTableEv',
    )

  @overload(QVector3D, QVector3D, QVector3D, QColor, float)
  def addInstance(
      self,
      position: QVector3D,
      scale: QVector3D,
      eulerRotation: QVector3D,
      color: QColor,
      age: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::addInstance(const
    QVector3D &position, const QVector3D &scale, const QVector3D
    &eulerRotation, const QColor &color, float age)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#addInstance

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    age : float
      Passed on as it is.
    """
    #  void QQuick3DParticleModelParticle::addInstance(const QVector3D
    #      &position, const QVector3D &scale, const QVector3D &eulerRotation,
    #      const QColor &color, float age)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle11addInstanceERK9QVector3D'
        'S2_S2_RK6QColorf',
        self._valueOf(position), self._valueOf(scale),
        self._valueOf(eulerRotation), self._valueOf(color), age,
    )

  def commitInstance(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::commitInstance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#commitInstance
    """
    #  void QQuick3DParticleModelParticle::commitInstance()
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle14commitInstanceEv',
    )

  @overload(float)
  def updateDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelParticle::updateDepthBias(float
    bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelparticle.html#updateDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DParticleModelParticle::updateDepthBias(float bias)
    self.uglySide.call(
        'ritual_ZN29QQuick3DParticleModelParticle15updateDepthBiasEf', bias,
    )
