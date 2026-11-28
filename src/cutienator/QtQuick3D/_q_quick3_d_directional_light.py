"""
QQuick3DDirectionalLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddirectionallight_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DDirectionalLight to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DAbstractLight, QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DDirectionalLight(QQuick3DAbstractLight):
  """
  The cute side of Qt's QQuick3DDirectionalLight: a plain Python object
  standing in front of one C++ QQuick3DDirectionalLight.

  It is built on the cute 'QQuick3DAbstractLight', as Qt's
  QQuick3DDirectionalLight is built on Qt's QQuick3DAbstractLight, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DDirectionalLight that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr', 'csmSplit1',
  'csmSplit2', 'csmSplit3', 'csmNumSplits', 'csmBlendRatio',
  'lockShadowmapTexels', 'setCsmSplit1', 'setCsmSplit2', 'setCsmSplit3',
  'setCsmNumSplits', 'setCsmBlendRatio', 'setLockShadowmapTexels',
  'csmSplit1Changed', 'csmSplit2Changed', 'csmSplit3Changed',
  'csmNumSplitsChanged', 'csmBlendRatioChanged',
  'lockShadowmapTexelsChanged', 'updateSpatialNode'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DDirectionalLight::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DDirectionalLight::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DDirectionalLight::~QQuick3DDirectionalLight()': the
    destructor: Python never removes a C++ QQuick3DDirectionalLight.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DDirectionalLight is created at the first use, not by
    'QQuick3DDirectionalLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DDirectionalLight.
  - Qt tells when it has removed the C++ QQuick3DDirectionalLight. Every call
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
    Calls Qt's 'QString QQuick3DDirectionalLight::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ddirectionallight.html#tr

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
    #  QString QQuick3DDirectionalLight::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DDirectionalLight2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DDirectionalLight'

  #  A C++ QQuick3DDirectionalLight Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DDirectionalLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DDirectionalLight::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DDirectionalLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def csmSplit1(self) -> float:
    """
    Calls Qt's 'float QQuick3DDirectionalLight::csmSplit1() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit1
    """
    #  float QQuick3DDirectionalLight::csmSplit1() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight9csmSplit1Ev',
    )

  def csmSplit2(self) -> float:
    """
    Calls Qt's 'float QQuick3DDirectionalLight::csmSplit2() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit2
    """
    #  float QQuick3DDirectionalLight::csmSplit2() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight9csmSplit2Ev',
    )

  def csmSplit3(self) -> float:
    """
    Calls Qt's 'float QQuick3DDirectionalLight::csmSplit3() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit3
    """
    #  float QQuick3DDirectionalLight::csmSplit3() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight9csmSplit3Ev',
    )

  def csmNumSplits(self) -> int:
    """
    Calls Qt's 'int QQuick3DDirectionalLight::csmNumSplits() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmNumSplits
    """
    #  int QQuick3DDirectionalLight::csmNumSplits() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight12csmNumSplitsEv',
    )

  def csmBlendRatio(self) -> float:
    """
    Calls Qt's 'float QQuick3DDirectionalLight::csmBlendRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmBlendRatio
    """
    #  float QQuick3DDirectionalLight::csmBlendRatio() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight13csmBlendRatioEv',
    )

  def lockShadowmapTexels(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDirectionalLight::lockShadowmapTexels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#lockShadowmapTexels
    """
    #  bool QQuick3DDirectionalLight::lockShadowmapTexels() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DDirectionalLight19lockShadowmapTexelsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setCsmSplit1(self, newcsmSplit1: float) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setCsmSplit1(float
    newcsmSplit1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#setCsmSplit1

    Parameters
    ----------

    newcsmSplit1 : float
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setCsmSplit1(float newcsmSplit1)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight12setCsmSplit1Ef', newcsmSplit1,
    )

  @overload(float)
  def setCsmSplit2(self, newcsmSplit2: float) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setCsmSplit2(float
    newcsmSplit2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#setCsmSplit2

    Parameters
    ----------

    newcsmSplit2 : float
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setCsmSplit2(float newcsmSplit2)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight12setCsmSplit2Ef', newcsmSplit2,
    )

  @overload(float)
  def setCsmSplit3(self, newcsmSplit3: float) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setCsmSplit3(float
    newcsmSplit3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#setCsmSplit3

    Parameters
    ----------

    newcsmSplit3 : float
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setCsmSplit3(float newcsmSplit3)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight12setCsmSplit3Ef', newcsmSplit3,
    )

  @overload(int)
  def setCsmNumSplits(self, newcsmNumSplits: int) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setCsmNumSplits(int
    newcsmNumSplits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#setCsmNumSplits

    Parameters
    ----------

    newcsmNumSplits : int
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setCsmNumSplits(int newcsmNumSplits)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight15setCsmNumSplitsEi',
        newcsmNumSplits,
    )

  @overload(float)
  def setCsmBlendRatio(self, newcsmBlendRatio: float) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setCsmBlendRatio(float
    newcsmBlendRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#setCsmBlendRatio

    Parameters
    ----------

    newcsmBlendRatio : float
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setCsmBlendRatio(float
    #      newcsmBlendRatio)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight16setCsmBlendRatioEf',
        newcsmBlendRatio,
    )

  @overload(bool)
  def setLockShadowmapTexels(self, newLockShadowmapTexels: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::setLockShadowmapTexels(bool
    newLockShadowmapTexels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html

    Parameters
    ----------

    newLockShadowmapTexels : bool
      Passed on as it is.
    """
    #  void QQuick3DDirectionalLight::setLockShadowmapTexels(bool
    #      newLockShadowmapTexels)
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight22setLockShadowmapTexelsEb',
        newLockShadowmapTexels,
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
    'QQuick3DDirectionalLight::QQuick3DDirectionalLight(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DDirectionalLight::QQuick3DDirectionalLight(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DDirectionalLight, lambda: Rituals.call(
        'ritual_ZN24QQuick3DDirectionalLightC1EP12QQuick3DNode',
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

  def csmSplit1Changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::csmSplit1Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit1Changed
    """
    #  void QQuick3DDirectionalLight::csmSplit1Changed()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight16csmSplit1ChangedEv',
    )

  def csmSplit2Changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::csmSplit2Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit2Changed
    """
    #  void QQuick3DDirectionalLight::csmSplit2Changed()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight16csmSplit2ChangedEv',
    )

  def csmSplit3Changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::csmSplit3Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmSplit3Changed
    """
    #  void QQuick3DDirectionalLight::csmSplit3Changed()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight16csmSplit3ChangedEv',
    )

  def csmNumSplitsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::csmNumSplitsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmNumSplitsChanged
    """
    #  void QQuick3DDirectionalLight::csmNumSplitsChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight19csmNumSplitsChangedEv',
    )

  def csmBlendRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::csmBlendRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#csmBlendRatioChanged
    """
    #  void QQuick3DDirectionalLight::csmBlendRatioChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight20csmBlendRatioChangedEv',
    )

  def lockShadowmapTexelsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDirectionalLight::lockShadowmapTexelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html
    """
    #  void QQuick3DDirectionalLight::lockShadowmapTexelsChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DDirectionalLight26lockShadowmapTexelsChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DDirectionalLight::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddirectionallight.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DDirectionalLight::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN24QQuick3DDirectionalLight17updateSpatialNodeEP21QSSGRend'
        'erGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuick3DDirectionalLight17updateSpatialNodeEP21QS'
          'SGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
