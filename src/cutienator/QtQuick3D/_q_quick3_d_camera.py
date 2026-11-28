"""
QQuick3DCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcamera_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DCamera to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DCamera(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DCamera: a plain Python object standing in
  front of one C++ QQuick3DCamera.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DCamera is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DCamera that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'mapToViewport',
  'mapFromViewport', 'lookAt', 'updateGlobalVariables',
  'frustumCullingEnabled', 'lookAtNode', 'levelOfDetailBias',
  'setFrustumCullingEnabled', 'setLookAtNode', 'setLevelOfDetailBias',
  'frustumCullingEnabledChanged', 'lookAtNodeChanged',
  'levelOfDetailBiasChanged', 'updateSpatialNode', 'updateLookAt'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DCamera::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DCamera::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DCamera::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuick3DCamera::QQuick3DCamera(QQuick3DNodePrivate &dd,
    QQuick3DNode *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DCamera is created at the first use, not by
    'QQuick3DCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DCamera.
  - Qt tells when it has removed the C++ QQuick3DCamera. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DCamera that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString QQuick3DCamera::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#tr

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
    #  QString QQuick3DCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuick3DCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DCamera::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DCamera::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DCamera10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QVector3D)
  def mapToViewport(self, scenePos: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DCamera::mapToViewport(const QVector3D
    &scenePos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#mapToViewport

    Parameters
    ----------

    scenePos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DCamera::mapToViewport(const QVector3D &scenePos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DCamera13mapToViewportERK9QVector3D',
        self._valueOf(scenePos),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D, float, float)
  def mapToViewport(
      self,
      scenePos: QVector3D,
      width: float,
      height: float,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DCamera::mapToViewport(const QVector3D
    &scenePos, qreal width, qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#mapToViewport

    Parameters
    ----------

    scenePos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DCamera::mapToViewport(const QVector3D &scenePos,
    #      qreal width, qreal height)
    address = self.uglySide.call(
        'ritual_ZN14QQuick3DCamera13mapToViewportERK9QVector3Ddd',
        self._valueOf(scenePos), width, height,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def mapFromViewport(self, viewportPos: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DCamera::mapFromViewport(const QVector3D
    &viewportPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#mapFromViewport

    Parameters
    ----------

    viewportPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DCamera::mapFromViewport(const QVector3D
    #      &viewportPos) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DCamera15mapFromViewportERK9QVector3D',
        self._valueOf(viewportPos),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D, float, float)
  def mapFromViewport(
      self,
      viewportPos: QVector3D,
      width: float,
      height: float,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DCamera::mapFromViewport(const QVector3D
    &viewportPos, qreal width, qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#mapFromViewport

    Parameters
    ----------

    viewportPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DCamera::mapFromViewport(const QVector3D
    #      &viewportPos, qreal width, qreal height)
    address = self.uglySide.call(
        'ritual_ZN14QQuick3DCamera15mapFromViewportERK9QVector3Ddd',
        self._valueOf(viewportPos), width, height,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def frustumCullingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DCamera::frustumCullingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#frustumCullingEnabled
    """
    #  bool QQuick3DCamera::frustumCullingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DCamera21frustumCullingEnabledEv',
    )

  def lookAtNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DCamera::lookAtNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#lookAtNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DCamera::lookAtNode() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DCamera10lookAtNodeEv')
    return QQuick3DNode._cuteAt(address)

  def levelOfDetailBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DCamera::levelOfDetailBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#levelOfDetailBias
    """
    #  float QQuick3DCamera::levelOfDetailBias() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DCamera17levelOfDetailBiasEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFrustumCullingEnabled(self, frustumCullingEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::setFrustumCullingEnabled(bool
    frustumCullingEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#setFrustumCullingEnabled

    Parameters
    ----------

    frustumCullingEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DCamera::setFrustumCullingEnabled(bool
    #      frustumCullingEnabled)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera24setFrustumCullingEnabledEb',
        frustumCullingEnabled,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setLookAtNode(self, node: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::setLookAtNode(QQuick3DNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#setLookAtNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DCamera::setLookAtNode(QQuick3DNode *node)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera13setLookAtNodeEP12QQuick3DNode',
        self._addressOf(node),
    )

  @overload(float)
  def setLevelOfDetailBias(self, newLevelOFDetailBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::setLevelOfDetailBias(float
    newLevelOFDetailBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#setLevelOfDetailBias

    Parameters
    ----------

    newLevelOFDetailBias : float
      Passed on as it is.
    """
    #  void QQuick3DCamera::setLevelOfDetailBias(float newLevelOFDetailBias)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera20setLevelOfDetailBiasEf',
        newLevelOFDetailBias,
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
    Qt's 'QQuick3DCamera::QQuick3DCamera(QQuick3DNodePrivate &dd,
    QQuick3DNode *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DCamera.__init__' has no cute function yet. Qt's "
        "'QQuick3DCamera::QQuick3DCamera(QQuick3DNodePrivate &dd, "
        "QQuick3DNode *parent)': takes a type Python has no way to hand "
        "over yet.")

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

  @overload(QVector3D)
  def lookAt(self, scenePos: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::lookAt(const QVector3D &scenePos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#lookAt

    Parameters
    ----------

    scenePos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DCamera::lookAt(const QVector3D &scenePos)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera6lookAtERK9QVector3D',
        self._valueOf(scenePos),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def lookAt(self, node: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::lookAt(QQuick3DNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#lookAt

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DCamera::lookAt(QQuick3DNode *node)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera6lookAtEP12QQuick3DNode',
        self._addressOf(node),
    )

  @overload(QRectF)
  def updateGlobalVariables(self, inViewport: QRectF) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::updateGlobalVariables(const QRectF
    &inViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#updateGlobalVariables

    Parameters
    ----------

    inViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuick3DCamera::updateGlobalVariables(const QRectF &inViewport)
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera21updateGlobalVariablesERK6QRectF',
        self._valueOf(inViewport),
    )

  def frustumCullingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::frustumCullingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#frustumCullingEnabledChanged
    """
    #  void QQuick3DCamera::frustumCullingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera28frustumCullingEnabledChangedEv',
    )

  def lookAtNodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::lookAtNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#lookAtNodeChanged
    """
    #  void QQuick3DCamera::lookAtNodeChanged()
    self.uglySide.call('ritual_ZN14QQuick3DCamera17lookAtNodeChangedEv')

  def levelOfDetailBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::levelOfDetailBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#levelOfDetailBiasChanged
    """
    #  void QQuick3DCamera::levelOfDetailBiasChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DCamera24levelOfDetailBiasChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DCamera::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcamera.html#updateSpatialNode

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
    #      *QQuick3DCamera::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN14QQuick3DCamera17updateSpatialNodeEP21QSSGRenderGraphObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DCamera17updateSpatialNodeEP21QSSGRenderGr'
          'aphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def updateLookAt(self) -> None:
    """
    Calls Qt's 'void QQuick3DCamera::updateLookAt()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcamera.html#updateLookAt
    """
    #  void QQuick3DCamera::updateLookAt()
    self.uglySide.call('ritual_ZN14QQuick3DCamera12updateLookAtEv')
