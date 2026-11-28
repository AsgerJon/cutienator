"""
QQuick3DNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DNodePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
from . import QQuick3DContentLayer, QQuick3DObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaMethod
  from ..QtGui import QMatrix4x4
  from . import QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QMetaMethod = WAIT['QMetaMethod']
  QQuick3DNode = WAIT['QQuick3DNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DNodePrivate(QQuick3DObjectPrivate):
  """
  The cute side of Qt's QQuick3DNodePrivate: a plain Python object standing
  in front of one C++ QQuick3DNodePrivate.

  It is built on the cute 'QQuick3DObjectPrivate', as Qt's
  QQuick3DNodePrivate is built on Qt's QQuick3DObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DNodePrivate that has a ritual and that
  Python can call so far, 12 names in all: 'q_func', 'init',
  'calculateGlobalVariables', 'markSceneTransformDirty',
  'localRotationMatrix', 'sceneRotationMatrix',
  'emitChangesToSceneTransform', 'isSceneTransformRelatedSignal',
  'isDirectionRelatedSignal', 'setIsHiddenInEditor', 'get',
  'setLocalTransform'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuick3DNode *QQuick3DNodePrivate::q_func() const': takes in
    Python what 'QQuick3DNode *QQuick3DNodePrivate::q_func()' takes.
  - Qt's 'QQuick3DNodePrivate::~QQuick3DNodePrivate()': the destructor:
    Python never removes a C++ QQuick3DNodePrivate.

  What to expect
  --------------

  - The C++ QQuick3DNodePrivate is created at the first use, not by
    'QQuick3DNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DNodePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuick3DNode)
  @overload(NoneType)
  def get(node: Optional[QQuick3DNode]) -> Optional[QQuick3DNodePrivate]:
    """
    Calls Qt's 'QQuick3DNodePrivate *QQuick3DNodePrivate::get(QQuick3DNode
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnodeprivate.html#get

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNodePrivate *QQuick3DNodePrivate::get(QQuick3DNode *node)
    address = Rituals.call(
        'ritual_ZN19QQuick3DNodePrivate3getEP12QQuick3DNode',
        CuteMixin._addressOf(node),
    )
    return QQuick3DNodePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DNodePrivate'

  #  A C++ QQuick3DNodePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DNodePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def localRotationMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuick3DNodePrivate::localRotationMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#localRotationMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuick3DNodePrivate::localRotationMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DNodePrivate19localRotationMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def sceneRotationMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuick3DNodePrivate::sceneRotationMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#sceneRotationMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuick3DNodePrivate::sceneRotationMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DNodePrivate19sceneRotationMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QMetaMethod)
  def isSceneTransformRelatedSignal(self, signal: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool QQuick3DNodePrivate::isSceneTransformRelatedSignal(const
    QMetaMethod &signal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool QQuick3DNodePrivate::isSceneTransformRelatedSignal(const
    #      QMetaMethod &signal) const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DNodePrivate29isSceneTransformRelatedSignalERK1'
        '1QMetaMethod',
        self._valueOf(signal),
    )

  @overload(QMetaMethod)
  def isDirectionRelatedSignal(self, signal: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool QQuick3DNodePrivate::isDirectionRelatedSignal(const
    QMetaMethod &signal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#isDirectionRelatedSignal

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool QQuick3DNodePrivate::isDirectionRelatedSignal(const QMetaMethod
    #      &signal) const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DNodePrivate24isDirectionRelatedSignalERK11QMet'
        'aMethod',
        self._valueOf(signal),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsHiddenInEditor(self, isHidden: bool) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::setIsHiddenInEditor(bool
    isHidden)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#setIsHiddenInEditor

    Parameters
    ----------

    isHidden : bool
      Passed on as it is.
    """
    #  void QQuick3DNodePrivate::setIsHiddenInEditor(bool isHidden)
    self.uglySide.call(
        'ritual_ZN19QQuick3DNodePrivate19setIsHiddenInEditorEb', isHidden,
    )

  @overload(QMatrix4x4)
  def setLocalTransform(self, transform: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::setLocalTransform(const QMatrix4x4
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#setLocalTransform

    Parameters
    ----------

    transform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QQuick3DNodePrivate::setLocalTransform(const QMatrix4x4
    #      &transform)
    self.uglySide.call(
        'ritual_ZN19QQuick3DNodePrivate17setLocalTransformERK10QMatrix4x4',
        self._valueOf(transform),
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

  @overload(QSSGRenderGraphObject.Type)
  @overload(QSSGRenderGraphObject.Type, QQuick3DContentLayer.LayerFlag)
  def __init__(
      self,
      t: QSSGRenderGraphObject.Type,
      layerFlag: QQuick3DContentLayer.LayerFlag = (
          QQuick3DContentLayer.LayerFlag.Layer0),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DNodePrivate::QQuick3DNodePrivate(QQuick3DObjectPrivate::Type t,
    QQuick3DContentLayer::LayerFlag layerFlag)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#QQuick3DNodePrivate

    Parameters
    ----------

    t : QSSGRenderGraphObject.Type
      Passed on as its number.

    layerFlag : QQuick3DContentLayer.LayerFlag
      Passed on as its number. May be left out, as in Qt: it is then
      QQuick3DContentLayer.LayerFlag.Layer0.
    """
    #  QQuick3DNodePrivate::QQuick3DNodePrivate(QQuick3DObjectPrivate::Type
    #      t, QQuick3DContentLayer::LayerFlag layerFlag)
    self._noteCreation(QQuick3DNodePrivate, lambda: Rituals.call(
        'ritual_ZN19QQuick3DNodePrivateC1EN21QSSGRenderGraphObject4TypeEN20'
        'QQuick3DContentLayer9LayerFlagE',
        t.value, layerFlag.value,
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

  def q_func(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DNodePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnodeprivate.html#q_func

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DNodePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuick3DNodePrivate6q_funcEv')
    from . import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnodeprivate.html#init
    """
    #  void QQuick3DNodePrivate::init()
    self.uglySide.call('ritual_ZN19QQuick3DNodePrivate4initEv')

  def calculateGlobalVariables(self) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::calculateGlobalVariables()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#calculateGlobalVariables
    """
    #  void QQuick3DNodePrivate::calculateGlobalVariables()
    self.uglySide.call(
        'ritual_ZN19QQuick3DNodePrivate24calculateGlobalVariablesEv',
    )

  def markSceneTransformDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::markSceneTransformDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html#markSceneTransformDirty
    """
    #  void QQuick3DNodePrivate::markSceneTransformDirty()
    self.uglySide.call(
        'ritual_ZN19QQuick3DNodePrivate23markSceneTransformDirtyEv',
    )

  def emitChangesToSceneTransform(self) -> None:
    """
    Calls Qt's 'void QQuick3DNodePrivate::emitChangesToSceneTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnodeprivate.html
    """
    #  void QQuick3DNodePrivate::emitChangesToSceneTransform()
    self.uglySide.call(
        'ritual_ZN19QQuick3DNodePrivate27emitChangesToSceneTransformEv',
    )
