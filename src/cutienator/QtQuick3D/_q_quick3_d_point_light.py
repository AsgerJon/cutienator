"""
QQuick3DPointLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpointlight_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DPointLight to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QQuick3DPointLight(QQuick3DAbstractLight):
  """
  The cute side of Qt's QQuick3DPointLight: a plain Python object standing in
  front of one C++ QQuick3DPointLight.

  It is built on the cute 'QQuick3DAbstractLight', as Qt's QQuick3DPointLight
  is built on Qt's QQuick3DAbstractLight, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DPointLight that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'constantFade',
  'linearFade', 'quadraticFade', 'setConstantFade', 'setLinearFade',
  'setQuadraticFade', 'constantFadeChanged', 'linearFadeChanged',
  'quadraticFadeChanged', 'updateSpatialNode'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DPointLight::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DPointLight::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DPointLight::~QQuick3DPointLight()': the destructor: Python
    never removes a C++ QQuick3DPointLight.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DPointLight is created at the first use, not by
    'QQuick3DPointLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DPointLight.
  - Qt tells when it has removed the C++ QQuick3DPointLight. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DPointLight::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpointlight.html#tr

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
    #  QString QQuick3DPointLight::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuick3DPointLight2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPointLight'

  #  A C++ QQuick3DPointLight Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DPointLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DPointLight::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpointlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DPointLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DPointLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def constantFade(self) -> float:
    """
    Calls Qt's 'float QQuick3DPointLight::constantFade() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#constantFade
    """
    #  float QQuick3DPointLight::constantFade() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DPointLight12constantFadeEv',
    )

  def linearFade(self) -> float:
    """
    Calls Qt's 'float QQuick3DPointLight::linearFade() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpointlight.html#linearFade
    """
    #  float QQuick3DPointLight::linearFade() const
    return self.uglySide.call('ritual_ZNK18QQuick3DPointLight10linearFadeEv')

  def quadraticFade(self) -> float:
    """
    Calls Qt's 'float QQuick3DPointLight::quadraticFade() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#quadraticFade
    """
    #  float QQuick3DPointLight::quadraticFade() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DPointLight13quadraticFadeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setConstantFade(self, constantFade: float) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::setConstantFade(float
    constantFade)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#setConstantFade

    Parameters
    ----------

    constantFade : float
      Passed on as it is.
    """
    #  void QQuick3DPointLight::setConstantFade(float constantFade)
    self.uglySide.call(
        'ritual_ZN18QQuick3DPointLight15setConstantFadeEf', constantFade,
    )

  @overload(float)
  def setLinearFade(self, linearFade: float) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::setLinearFade(float linearFade)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#setLinearFade

    Parameters
    ----------

    linearFade : float
      Passed on as it is.
    """
    #  void QQuick3DPointLight::setLinearFade(float linearFade)
    self.uglySide.call(
        'ritual_ZN18QQuick3DPointLight13setLinearFadeEf', linearFade,
    )

  @overload(float)
  def setQuadraticFade(self, quadraticFade: float) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::setQuadraticFade(float
    quadraticFade)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#setQuadraticFade

    Parameters
    ----------

    quadraticFade : float
      Passed on as it is.
    """
    #  void QQuick3DPointLight::setQuadraticFade(float quadraticFade)
    self.uglySide.call(
        'ritual_ZN18QQuick3DPointLight16setQuadraticFadeEf', quadraticFade,
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
    'QQuick3DPointLight::QQuick3DPointLight(QQuick3DNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#QQuick3DPointLight

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DPointLight::QQuick3DPointLight(QQuick3DNode *parent)
    self._noteCreation(QQuick3DPointLight, lambda: Rituals.call(
        'ritual_ZN18QQuick3DPointLightC1EP12QQuick3DNode',
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

  def constantFadeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::constantFadeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#constantFadeChanged
    """
    #  void QQuick3DPointLight::constantFadeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DPointLight19constantFadeChangedEv',
    )

  def linearFadeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::linearFadeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#linearFadeChanged
    """
    #  void QQuick3DPointLight::linearFadeChanged()
    self.uglySide.call('ritual_ZN18QQuick3DPointLight17linearFadeChangedEv')

  def quadraticFadeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPointLight::quadraticFadeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#quadraticFadeChanged
    """
    #  void QQuick3DPointLight::quadraticFadeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DPointLight20quadraticFadeChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DPointLight::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpointlight.html#updateSpatialNode

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
    #      *QQuick3DPointLight::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN18QQuick3DPointLight17updateSpatialNodeEP21QSSGRenderGrap'
        'hObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuick3DPointLight17updateSpatialNodeEP21QSSGRend'
          'erGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
