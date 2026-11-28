"""
QQuick3DEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3deffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DEffect to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DSceneManager, QQuick3DShaderUtilsTextureInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DShaderUtilsTextureInput = WAIT['QQuick3DShaderUtilsTextureInput']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DEffect(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DEffect: a plain Python object standing in
  front of one C++ QQuick3DEffect.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DEffect is built
  on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DEffect that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'effectChainDirty',
  'updateSpatialNode', 'itemChange', 'onPropertyDirty', 'onTextureDirty',
  'onPassDirty', 'setDynamicTextureMap', 'updateSceneManager'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DEffect::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DEffect::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderPass>
    QQuick3DEffect::passes()': gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DEffect::qmlAppendPass(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list,
    QQuick3DShaderUtilsRenderPass *pass)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
  - Qt's 'QQuick3DShaderUtilsRenderPass *QQuick3DEffect::qmlPassAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no
    cute class yet.
  - Qt's 'qsizetype QQuick3DEffect::qmlPassCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
  - Qt's 'void QQuick3DEffect::qmlPassClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
  - Qt's 'void QQuick3DEffect::markDirty(QQuick3DEffect::Dirty type)': names
    the enum 'QQuick3DEffect::Dirty', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DEffect is created at the first use, not by
    'QQuick3DEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DEffect.
  - Qt tells when it has removed the C++ QQuick3DEffect. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DEffect that has no cute function yet,
    'markDirty', 'passes', 'qmlAppendPass', 'qmlPassAt', 'qmlPassClear',
    'qmlPassCount', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuick3DEffect::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#tr

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
    #  QString QQuick3DEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuick3DEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DEffect::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DEffect10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DShaderUtilsTextureInput)
  @overload(NoneType)
  def setDynamicTextureMap(
      self,
      textureMap: Optional[QQuick3DShaderUtilsTextureInput],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DEffect::setDynamicTextureMap(QQuick3DShaderUtilsTextureInput
    *textureMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3deffect.html#setDynamicTextureMap

    Parameters
    ----------

    textureMap : Optional[QQuick3DShaderUtilsTextureInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DEffect::setDynamicTextureMap(
    #      QQuick3DShaderUtilsTextureInput *textureMap)
    self.uglySide.call(
        'ritual_ZN14QQuick3DEffect20setDynamicTextureMapEP31QQuick3DShaderU'
        'tilsTextureInput',
        self._addressOf(textureMap),
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DEffect::QQuick3DEffect(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#QQuick3DEffect

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DEffect::QQuick3DEffect(QQuick3DObject *parent)
    self._noteCreation(QQuick3DEffect, lambda: Rituals.call(
        'ritual_ZN14QQuick3DEffectC1EP14QQuick3DObject',
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

  def effectChainDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::effectChainDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3deffect.html#effectChainDirty
    """
    #  void QQuick3DEffect::effectChainDirty()
    self.uglySide.call('ritual_ZN14QQuick3DEffect16effectChainDirtyEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DEffect::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3deffect.html#updateSpatialNode

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
    #      *QQuick3DEffect::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN14QQuick3DEffect17updateSpatialNodeEP21QSSGRenderGraphObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DEffect17updateSpatialNodeEP21QSSGRenderGr'
          'aphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::itemChange(QQuick3DObject::ItemChange
    a0, const QQuick3DObject::ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DEffect::itemChange(QQuick3DObject::ItemChange a0, const
    #      QQuick3DObject::ItemChangeData &a1)
    ritual = (
        'ritual_ZN14QQuick3DEffect10itemChangeEN14QQuick3DObject10ItemChang'
        'eERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DEffect10itemChangeEN14QQuick3DObject10Ite'
          'mChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def onPropertyDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::onPropertyDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3deffect.html#onPropertyDirty
    """
    #  void QQuick3DEffect::onPropertyDirty()
    self.uglySide.call('ritual_ZN14QQuick3DEffect15onPropertyDirtyEv')

  def onTextureDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::onTextureDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#onTextureDirty
    """
    #  void QQuick3DEffect::onTextureDirty()
    self.uglySide.call('ritual_ZN14QQuick3DEffect14onTextureDirtyEv')

  def onPassDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::onPassDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3deffect.html#onPassDirty
    """
    #  void QQuick3DEffect::onPassDirty()
    self.uglySide.call('ritual_ZN14QQuick3DEffect11onPassDirtyEv')

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DEffect::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3deffect.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DEffect::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN14QQuick3DEffect18updateSceneManagerEP20QQuick3DSceneMana'
        'ger',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DEffect::markDirty(QQuick3DEffect::Dirty type)': names
    the enum 'QQuick3DEffect::Dirty', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.markDirty' has no cute function yet. Qt's 'void "
        "QQuick3DEffect::markDirty(QQuick3DEffect::Dirty type)': names the "
        "enum 'QQuick3DEffect::Dirty', whose class cannot be named here.")

  @staticmethod
  def passes(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderPass>
    QQuick3DEffect::passes()': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.passes' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderPass> "
        "QQuick3DEffect::passes()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def qmlAppendPass(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DEffect::qmlAppendPass(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list,
    QQuick3DShaderUtilsRenderPass *pass)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.qmlAppendPass' has no cute function yet. Qt's "
        "'void "
        "QQuick3DEffect::qmlAppendPass(QQmlListProperty<QQuick3DShaderUtilsR"
        "enderPass> *list, QQuick3DShaderUtilsRenderPass *pass)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlPassAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DShaderUtilsRenderPass *QQuick3DEffect::qmlPassAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.qmlPassAt' has no cute function yet. Qt's "
        "'QQuick3DShaderUtilsRenderPass "
        "*QQuick3DEffect::qmlPassAt(QQmlListProperty<QQuick3DShaderUtilsRend"
        "erPass> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlPassClear(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DEffect::qmlPassClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.qmlPassClear' has no cute function yet. Qt's 'void "
        "QQuick3DEffect::qmlPassClear(QQmlListProperty<QQuick3DShaderUtilsRe"
        "nderPass> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlPassCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DEffect::qmlPassCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderPass> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DEffect.qmlPassCount' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuick3DEffect::qmlPassCount(QQmlListProperty<QQuick3DShaderUtilsRe"
        "nderPass> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderPass>', which has no "
        "cute class yet.")
