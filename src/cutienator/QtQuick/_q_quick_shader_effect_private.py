"""
QQuickShaderEffectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShaderEffectPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickItem, QQuickItemPrivate, QQuickShaderEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QObject, QRectF, QUrl, QVariant
  from . import QSGShaderEffectNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QObject = WAIT['QObject']
  QRectF = WAIT['QRectF']
  QSGShaderEffectNode = WAIT['QSGShaderEffectNode']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShaderEffectPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickShaderEffectPrivate: a plain Python object
  standing in front of one C++ QQuickShaderEffectPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's
  QQuickShaderEffectPrivate is built on Qt's QQuickItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShaderEffectPrivate that has a ritual and that
  Python can call so far, 19 names in all: 'q_func', 'updatePolish',
  'fragmentShader', 'vertexShader', 'blending', 'setBlending', 'mesh',
  'setMesh', 'cullMode', 'setCullMode', 'supportsAtlasTextures',
  'setSupportsAtlasTextures', 'handleEvent', 'handleGeometryChanged',
  'handleItemChange', 'updateUniformValue', 'sourceDestroyed',
  'markGeometryDirtyAndUpdate', 'markGeometryDirtyAndUpdateIfSupportsAtlas'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickShaderEffect *QQuickShaderEffectPrivate::q_func()
    const': takes in Python what 'QQuickShaderEffect
    *QQuickShaderEffectPrivate::q_func()' takes.
  - Qt's 'QQuickShaderEffectPrivate::~QQuickShaderEffectPrivate()': the
    destructor: Python never removes a C++ QQuickShaderEffectPrivate.
  - Qt's 'bool QQuickShaderEffectPrivate::sourceIsUnique(QQuickItem *source,
    Shader typeToSkip, int indexToSkip) const': names the enum
    'QQuickShaderEffectPrivate::Shader', whose class cannot be named here.

  What has no ritual
  ------------------

  18 of the 40 functions Qt declares: 10 leans on 'QQuickShaderEffectPrivate;
  7 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickShaderEffectPrivate is created at the first use, not by
    'QQuickShaderEffectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShaderEffectPrivate.
  - Each name of Qt's QQuickShaderEffectPrivate that has no cute function
    yet, '__init__', 'clearMappers', 'disconnectSignals',
    'findMappedShaderVariableId', 'handleComponentComplete',
    'handleUpdatePaintNode', 'log', 'maybeUpdateShaders', 'parseLog',
    'propertyChanged', 'setFragmentShader', 'setVertexShader',
    'shaderCodePrepared', 'shaderEffectManager', 'sourceIsUnique', 'status',
    'updateShader', 'updateShaderVars', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShaderEffectPrivate'

  #  A C++ QQuickShaderEffectPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShaderEffectPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fragmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickShaderEffectPrivate::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#fragmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickShaderEffectPrivate::fragmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate14fragmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def vertexShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickShaderEffectPrivate::vertexShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#vertexShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickShaderEffectPrivate::vertexShader() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate12vertexShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def blending(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectPrivate::blending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#blending
    """
    #  bool QQuickShaderEffectPrivate::blending() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate8blendingEv',
    )

  def mesh(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickShaderEffectPrivate::mesh() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#mesh

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickShaderEffectPrivate::mesh() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate4meshEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def cullMode(self) -> QQuickShaderEffect.CullMode:
    """
    Calls Qt's 'QQuickShaderEffect::CullMode
    QQuickShaderEffectPrivate::cullMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#cullMode

    Returns
    -------

    QQuickShaderEffect.CullMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShaderEffect.CullMode(number)' gives.
    """
    #  QQuickShaderEffect::CullMode QQuickShaderEffectPrivate::cullMode()
    #      const
    return QQuickShaderEffect.CullMode(self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate8cullModeEv',
    ))

  def supportsAtlasTextures(self) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectPrivate::supportsAtlasTextures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html
    """
    #  bool QQuickShaderEffectPrivate::supportsAtlasTextures() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickShaderEffectPrivate21supportsAtlasTexturesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setBlending(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::setBlending(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#setBlending

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectPrivate::setBlending(bool enable)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate11setBlendingEb', enable,
    )

  @overload(QVariant)
  def setMesh(self, mesh: QVariant) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::setMesh(const QVariant
    &mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#setMesh

    Parameters
    ----------

    mesh : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickShaderEffectPrivate::setMesh(const QVariant &mesh)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate7setMeshERK8QVariant',
        self._valueOf(mesh),
    )

  @overload(QQuickShaderEffect.CullMode)
  def setCullMode(self, face: QQuickShaderEffect.CullMode) -> None:
    """
    Calls Qt's 'void
    QQuickShaderEffectPrivate::setCullMode(QQuickShaderEffect::CullMode
    face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#setCullMode

    Parameters
    ----------

    face : QQuickShaderEffect.CullMode
      Passed on as its number.
    """
    #  void QQuickShaderEffectPrivate::setCullMode(QQuickShaderEffect::
    #      CullMode face)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate11setCullModeEN18QQuickShaderE'
        'ffect8CullModeE',
        face.value,
    )

  @overload(bool)
  def setSupportsAtlasTextures(self, supports: bool) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::setSupportsAtlasTextures(bool
    supports)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html

    Parameters
    ----------

    supports : bool
      Passed on as it is.
    """
    #  void QQuickShaderEffectPrivate::setSupportsAtlasTextures(bool
    #      supports)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate24setSupportsAtlasTexturesEb',
        supports,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickShaderEffectPrivate::QQuickShaderEffectPrivate()': leans on
    'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate::
    Shader, QUrl const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.__init__' has no cute function yet. "
        "Qt's 'QQuickShaderEffectPrivate::QQuickShaderEffectPrivate()': "
        "leans on "
        "'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate:"
        ":Shader, QUrl const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickShaderEffect]:
    """
    Calls Qt's 'QQuickShaderEffect *QQuickShaderEffectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#q_func

    Returns
    -------

    Optional[QQuickShaderEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShaderEffect *QQuickShaderEffectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate6q_funcEv',
    )
    return QQuickShaderEffect._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#updatePolish
    """
    #  void QQuickShaderEffectPrivate::updatePolish()
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate12updatePolishEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def handleEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::handleEvent(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#handleEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShaderEffectPrivate::handleEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate11handleEventEP6QEvent',
        self._addressOf(a0),
    )

  @overload(QRectF, QRectF)
  def handleGeometryChanged(
      self,
      newGeometry: QRectF,
      oldGeometry: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::handleGeometryChanged(const
    QRectF &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickShaderEffectPrivate::handleGeometryChanged(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate21handleGeometryChangedERK6QRe'
        'ctFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def handleItemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickShaderEffectPrivate::handleItemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#handleItemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void
    #      QQuickShaderEffectPrivate::handleItemChange(QQuickItem::ItemChange
    #      change, const QQuickItem::ItemChangeData &value)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate16handleItemChangeEN10QQuickIt'
        'em10ItemChangeERKNS0_14ItemChangeDataE',
        change.value, self._valueOf(value),
    )

  @overload(QByteArray, QVariant, QSGShaderEffectNode)
  @overload(QByteArray, QVariant, NoneType)
  def updateUniformValue(
      self,
      name: QByteArray,
      value: QVariant,
      node: Optional[QSGShaderEffectNode],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickShaderEffectPrivate::updateUniformValue(const
    QByteArray &name, const QVariant &value, QSGShaderEffectNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#updateUniformValue

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    node : Optional[QSGShaderEffectNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickShaderEffectPrivate::updateUniformValue(const QByteArray
    #      &name, const QVariant &value, QSGShaderEffectNode *node)
    return self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate18updateUniformValueERK10QByte'
        'ArrayRK8QVariantP19QSGShaderEffectNode',
        self._valueOf(name), self._valueOf(value), self._addressOf(node),
    )

  @overload(QObject)
  @overload(NoneType)
  def sourceDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickShaderEffectPrivate::sourceDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html#sourceDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShaderEffectPrivate::sourceDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate15sourceDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def markGeometryDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QQuickShaderEffectPrivate::markGeometryDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html
    """
    #  void QQuickShaderEffectPrivate::markGeometryDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate26markGeometryDirtyAndUpdateEv',
    )

  def markGeometryDirtyAndUpdateIfSupportsAtlas(self) -> None:
    """
    Calls Qt's 'void
    QQuickShaderEffectPrivate::markGeometryDirtyAndUpdateIfSupportsAtlas()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshadereffectprivate.html
    """
    #  void QQuickShaderEffectPrivate::
    #      markGeometryDirtyAndUpdateIfSupportsAtlas()
    self.uglySide.call(
        'ritual_ZN25QQuickShaderEffectPrivate41markGeometryDirtyAndUpdateIf'
        'SupportsAtlasEv',
    )

  @staticmethod
  def clearMappers(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::clearMappers(Shader shaderType)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QtPrivate::EffectSlotMapper'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.clearMappers' has no cute function yet. "
        "Qt's 'void QQuickShaderEffectPrivate::clearMappers(Shader "
        "shaderType)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QtPrivate::EffectSlotMapper'.")

  @staticmethod
  def disconnectSignals(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::disconnectSignals(Shader
    shaderType)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QtPrivate::EffectSlotMapper'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.disconnectSignals' has no cute function "
        "yet. Qt's 'void "
        "QQuickShaderEffectPrivate::disconnectSignals(Shader shaderType)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QtPrivate::EffectSlotMapper'.")

  @staticmethod
  def findMappedShaderVariableId(*__, **_) -> Never:
    """
    - Qt's 'std::optional<int>
      QQuickShaderEffectPrivate::findMappedShaderVariableId(const QByteArray
      &name) const': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: use of undeclared
      identifier 'indexToMappedId'.
    - Qt's 'std::optional<int>
      QQuickShaderEffectPrivate::findMappedShaderVariableId(const QByteArray
      &name, Shader shaderType) const': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'indexToMappedId'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.findMappedShaderVariableId' has no cute "
        "function yet. Qt's 'std::optional<int> "
        "QQuickShaderEffectPrivate::findMappedShaderVariableId(const "
        "QByteArray &name) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'indexToMappedId'. Qt's 'std::optional<int> "
        "QQuickShaderEffectPrivate::findMappedShaderVariableId(const "
        "QByteArray &name, Shader shaderType) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'indexToMappedId'.")

  @staticmethod
  def handleComponentComplete(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::handleComponentComplete()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.handleComponentComplete' has no cute "
        "function yet. Qt's 'void "
        "QQuickShaderEffectPrivate::handleComponentComplete()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def handleUpdatePaintNode(*__, **_) -> Never:
    """
    Qt's 'QSGNode *QQuickShaderEffectPrivate::handleUpdatePaintNode(QSGNode
    *a0, QQuickItem::UpdatePaintNodeData *a1)': leans on
    'QQuickShaderEffectPrivate::shaderCodePrepared(bool,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&,
    QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.handleUpdatePaintNode' has no cute "
        "function yet. Qt's 'QSGNode "
        "*QQuickShaderEffectPrivate::handleUpdatePaintNode(QSGNode *a0, "
        "QQuickItem::UpdatePaintNodeData *a1)': leans on "
        "'QQuickShaderEffectPrivate::shaderCodePrepared(bool, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def log(*__, **_) -> Never:
    """
    Qt's 'QString QQuickShaderEffectPrivate::log() const': leans on
    'QQuickShaderEffectPrivate::shaderCodePrepared(bool,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&,
    QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.log' has no cute function yet. Qt's "
        "'QString QQuickShaderEffectPrivate::log() const': leans on "
        "'QQuickShaderEffectPrivate::shaderCodePrepared(bool, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def maybeUpdateShaders(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::maybeUpdateShaders()': leans on
    'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate::
    Shader, QUrl const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.maybeUpdateShaders' has no cute "
        "function yet. Qt's 'void "
        "QQuickShaderEffectPrivate::maybeUpdateShaders()': leans on "
        "'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate:"
        ":Shader, QUrl const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseLog(*__, **_) -> Never:
    """
    Qt's 'QString QQuickShaderEffectPrivate::parseLog()': leans on
    'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate::
    Shader, QUrl const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.parseLog' has no cute function yet. "
        "Qt's 'QString QQuickShaderEffectPrivate::parseLog()': leans on "
        "'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate:"
        ":Shader, QUrl const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def propertyChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::propertyChanged(int mappedId)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'mappedIdToShaderType'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.propertyChanged' has no cute function "
        "yet. Qt's 'void QQuickShaderEffectPrivate::propertyChanged(int "
        "mappedId)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'mappedIdToShaderType'.")

  @staticmethod
  def setFragmentShader(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::setFragmentShader(const QUrl
    &fileUrl)': leans on
    'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate::
    Shader, QUrl const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.setFragmentShader' has no cute function "
        "yet. Qt's 'void QQuickShaderEffectPrivate::setFragmentShader(const "
        "QUrl &fileUrl)': leans on "
        "'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate:"
        ":Shader, QUrl const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setVertexShader(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::setVertexShader(const QUrl
    &fileUrl)': leans on
    'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate::
    Shader, QUrl const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.setVertexShader' has no cute function "
        "yet. Qt's 'void QQuickShaderEffectPrivate::setVertexShader(const "
        "QUrl &fileUrl)': leans on "
        "'QQuickShaderEffectPrivate::updateShader(QQuickShaderEffectPrivate:"
        ":Shader, QUrl const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def shaderCodePrepared(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::shaderCodePrepared(bool ok,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type typeHint, const QUrl
    &loadUrl, QSGGuiThreadShaderEffectManager::ShaderInfo *result)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'shaderInfoCache'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.shaderCodePrepared' has no cute "
        "function yet. Qt's 'void "
        "QQuickShaderEffectPrivate::shaderCodePrepared(bool ok, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type typeHint, const "
        "QUrl &loadUrl, QSGGuiThreadShaderEffectManager::ShaderInfo "
        "*result)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'shaderInfoCache'.")

  @staticmethod
  def shaderEffectManager(*__, **_) -> Never:
    """
    Qt's 'QSGGuiThreadShaderEffectManager
    *QQuickShaderEffectPrivate::shaderEffectManager() const': leans on
    'QQuickShaderEffectPrivate::shaderCodePrepared(bool,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&,
    QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.shaderEffectManager' has no cute "
        "function yet. Qt's 'QSGGuiThreadShaderEffectManager "
        "*QQuickShaderEffectPrivate::shaderEffectManager() const': leans on "
        "'QQuickShaderEffectPrivate::shaderCodePrepared(bool, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sourceIsUnique(*__, **_) -> Never:
    """
    Qt's 'bool QQuickShaderEffectPrivate::sourceIsUnique(QQuickItem *source,
    Shader typeToSkip, int indexToSkip) const': names the enum
    'QQuickShaderEffectPrivate::Shader', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.sourceIsUnique' has no cute function "
        "yet. Qt's 'bool "
        "QQuickShaderEffectPrivate::sourceIsUnique(QQuickItem *source, "
        "Shader typeToSkip, int indexToSkip) const': names the enum "
        "'QQuickShaderEffectPrivate::Shader', whose class cannot be named "
        "here.")

  @staticmethod
  def status(*__, **_) -> Never:
    """
    Qt's 'QQuickShaderEffect::Status QQuickShaderEffectPrivate::status()
    const': leans on 'QQuickShaderEffectPrivate::shaderCodePrepared(bool,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&,
    QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.status' has no cute function yet. Qt's "
        "'QQuickShaderEffect::Status QQuickShaderEffectPrivate::status() "
        "const': leans on "
        "'QQuickShaderEffectPrivate::shaderCodePrepared(bool, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def updateShader(*__, **_) -> Never:
    """
    Qt's 'bool QQuickShaderEffectPrivate::updateShader(Shader shaderType,
    const QUrl &fileUrl)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'shaderInfoCache'.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.updateShader' has no cute function yet. "
        "Qt's 'bool QQuickShaderEffectPrivate::updateShader(Shader "
        "shaderType, const QUrl &fileUrl)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'shaderInfoCache'.")

  @staticmethod
  def updateShaderVars(*__, **_) -> Never:
    """
    Qt's 'void QQuickShaderEffectPrivate::updateShaderVars(Shader
    shaderType)': leans on
    'QQuickShaderEffectPrivate::shaderCodePrepared(bool,
    QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&,
    QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickShaderEffectPrivate.updateShaderVars' has no cute function "
        "yet. Qt's 'void QQuickShaderEffectPrivate::updateShaderVars(Shader "
        "shaderType)': leans on "
        "'QQuickShaderEffectPrivate::shaderCodePrepared(bool, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo::Type, QUrl const&, "
        "QSGGuiThreadShaderEffectManager::ShaderInfo*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
