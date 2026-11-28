"""
Qt3DRender::Scene3DItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3ditem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Scene3DItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore
from ..QtQuick import QQuickItem
from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QMouseEvent
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene3DItem(QQuickItem):
  """
  The cute side of Qt's Qt3DRender::Scene3DItem: a plain Python object
  standing in front of one C++ Qt3DRender::Scene3DItem.

  It is built on the cute 'QQuickItem', as Qt's Qt3DRender::Scene3DItem is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Scene3DItem that has a ritual and that
  Python can call so far, 29 names in all: 'metaObject', 'aspects', 'entity',
  'multisample', 'setItemAreaAndDevicePixelRatio', 'isHoverEnabled',
  'cameraAspectRatioMode', 'compositingMode', 'setAspects', 'setEntity',
  'setCameraAspectRatioMode', 'setHoverEnabled', 'setCompositingMode',
  'aspectsChanged', 'entityChanged', 'multisampleChanged',
  'cameraAspectRatioModeChanged', 'hoverEnabledChanged',
  'compositingModeChanged', 'applyRootEntityChange', 'requestUpdate',
  'prepareQt3DFrame', 'updatePaintNode', 'setWindowSurface',
  'updateCameraAspectRatio', 'mousePressEvent', 'needsRender',
  'updateWindowSurface', 'applyAspects'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Scene3DItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::Scene3DItem::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::Scene3DItem::~Scene3DItem()': the destructor: Python
    never removes a C++ Qt3DRender::Scene3DItem.

  What has no ritual
  ------------------

  7 of the 39 functions Qt declares: 4 leans on 'Qt3DRender; 2 not a gap; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DRender::Scene3DItem is created at the first use, not by
    'Qt3DRender::Scene3DItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Scene3DItem.
  - Qt tells when it has removed the C++ Qt3DRender::Scene3DItem. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::Scene3DItem that has no cute function yet,
    '__init__', 'setCameraAspectModeHelper', 'setMultisample', 'synchronize',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside Qt3DRender::Scene3DItem, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CameraAspectRatioMode(CuteNum):
    """
    The enum 'Qt3DRender::Scene3DItem::CameraAspectRatioMode' of Qt, with the
    2 names Qt gives in it.
    """

    AutomaticAspectRatio = Kee[int](0)
    UserAspectRatio = Kee[int](1)

  class CompositingMode(CuteNum):
    """
    The enum 'Qt3DRender::Scene3DItem::CompositingMode' of Qt, with the 2
    names Qt gives in it.
    """

    FBO = Kee[int](0)
    Underlay = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Scene3DItem'

  #  A C++ Qt3DRender::Scene3DItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Scene3DItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::Scene3DItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::Scene3DItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def aspects(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::Scene3DItem::aspects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#aspects

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::Scene3DItem::aspects() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem7aspectsEv',
    )
    return QStringList._cuteOwning(address)

  def entity(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::Scene3DItem::entity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#entity

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::Scene3DItem::entity() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem6entityEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def multisample(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DItem::multisample() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#multisample
    """
    #  bool Qt3DRender::Scene3DItem::multisample() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem11multisampleEv',
    )

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DItem::isHoverEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#isHoverEnabled
    """
    #  bool Qt3DRender::Scene3DItem::isHoverEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem14isHoverEnabledEv',
    )

  def cameraAspectRatioMode(self) -> CameraAspectRatioMode:
    """
    Calls Qt's 'CameraAspectRatioMode
    Qt3DRender::Scene3DItem::cameraAspectRatioMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#cameraAspectRatioMode

    Returns
    -------

    CameraAspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CameraAspectRatioMode(number)' gives.
    """
    #  CameraAspectRatioMode Qt3DRender::Scene3DItem::cameraAspectRatioMode()
    #      const
    return Scene3DItem.CameraAspectRatioMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem21cameraAspectRatioModeEv',
    ))

  def compositingMode(self) -> CompositingMode:
    """
    Calls Qt's 'CompositingMode Qt3DRender::Scene3DItem::compositingMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#compositingMode

    Returns
    -------

    CompositingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompositingMode(number)'
      gives.
    """
    #  CompositingMode Qt3DRender::Scene3DItem::compositingMode() const
    return Scene3DItem.CompositingMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender11Scene3DItem15compositingModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize, float)
  def setItemAreaAndDevicePixelRatio(
      self,
      area: QSize,
      devicePixelRatio: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Scene3DItem::setItemAreaAndDevicePixelRatio(QSize area, qreal
    devicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html

    Parameters
    ----------

    area : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    devicePixelRatio : float
      Passed on as it is.
    """
    #  void Qt3DRender::Scene3DItem::setItemAreaAndDevicePixelRatio(QSize
    #      area, qreal devicePixelRatio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem30setItemAreaAndDevicePixelRatio'
        'E5QSized',
        self._valueOf(area), devicePixelRatio,
    )

  @overload(QStringList)
  def setAspects(self, aspects: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::setAspects(const QStringList
    &aspects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#setAspects

    Parameters
    ----------

    aspects : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::Scene3DItem::setAspects(const QStringList &aspects)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem10setAspectsERK5QListI7QStringE',
        self._valueOf(aspects),
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::setEntity(Qt3DCore::QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#setEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DItem::setEntity(Qt3DCore::QEntity *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem9setEntityEPN8Qt3DCore7QEntityE',
        self._addressOf(entity),
    )

  @overload(CameraAspectRatioMode)
  def setCameraAspectRatioMode(self, mode: CameraAspectRatioMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Scene3DItem::setCameraAspectRatioMode(CameraAspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html

    Parameters
    ----------

    mode : CameraAspectRatioMode
      Passed on as its number.
    """
    #  void Qt3DRender::Scene3DItem::setCameraAspectRatioMode(
    #      CameraAspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem24setCameraAspectRatioModeENS0_2'
        '1CameraAspectRatioModeE',
        mode.value,
    )

  @overload(bool)
  def setHoverEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::setHoverEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#setHoverEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Scene3DItem::setHoverEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem15setHoverEnabledEb', enabled,
    )

  @overload(CompositingMode)
  def setCompositingMode(self, mode: CompositingMode) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Scene3DItem::setCompositingMode(CompositingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#setCompositingMode

    Parameters
    ----------

    mode : CompositingMode
      Passed on as its number.
    """
    #  void Qt3DRender::Scene3DItem::setCompositingMode(CompositingMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem18setCompositingModeENS0_15Compo'
        'sitingModeE',
        mode.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def setWindowSurface(self, rootObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::setWindowSurface(QObject
    *rootObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#setWindowSurface

    Parameters
    ----------

    rootObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DItem::setWindowSurface(QObject *rootObject)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem16setWindowSurfaceEP7QObject',
        self._addressOf(rootObject, 'QObject'),
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
    Qt's 'Qt3DRender::Scene3DItem::Scene3DItem(QQuickItem *parent)': leans on
    'Qt3DRender::Scene3DItem::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DItem.__init__' has no cute function yet. Qt's "
        "'Qt3DRender::Scene3DItem::Scene3DItem(QQuickItem *parent)': leans "
        "on 'Qt3DRender::Scene3DItem::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def aspectsChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::aspectsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#aspectsChanged
    """
    #  void Qt3DRender::Scene3DItem::aspectsChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem14aspectsChangedEv',
    )

  def entityChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::entityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#entityChanged
    """
    #  void Qt3DRender::Scene3DItem::entityChanged()
    self.uglySide.call('ritual_ZN10Qt3DRender11Scene3DItem13entityChangedEv')

  def multisampleChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::multisampleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#multisampleChanged
    """
    #  void Qt3DRender::Scene3DItem::multisampleChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem18multisampleChangedEv',
    )

  @overload(CameraAspectRatioMode)
  def cameraAspectRatioModeChanged(
      self,
      mode: CameraAspectRatioMode,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::cameraAspectRatioModeChanged(
    CameraAspectRatioMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html

    Parameters
    ----------

    mode : CameraAspectRatioMode
      Passed on as its number.
    """
    #  void Qt3DRender::Scene3DItem::cameraAspectRatioModeChanged(
    #      CameraAspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem28cameraAspectRatioModeChangedEN'
        'S0_21CameraAspectRatioModeE',
        mode.value,
    )

  def hoverEnabledChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::hoverEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#hoverEnabledChanged
    """
    #  void Qt3DRender::Scene3DItem::hoverEnabledChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem19hoverEnabledChangedEv',
    )

  def compositingModeChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::compositingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#compositingModeChanged
    """
    #  void Qt3DRender::Scene3DItem::compositingModeChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem22compositingModeChangedEv',
    )

  def applyRootEntityChange(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::applyRootEntityChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#applyRootEntityChange
    """
    #  void Qt3DRender::Scene3DItem::applyRootEntityChange()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem21applyRootEntityChangeEv',
    )

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#requestUpdate
    """
    #  void Qt3DRender::Scene3DItem::requestUpdate()
    self.uglySide.call('ritual_ZN10Qt3DRender11Scene3DItem13requestUpdateEv')

  def prepareQt3DFrame(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DItem::prepareQt3DFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#prepareQt3DFrame
    """
    #  bool Qt3DRender::Scene3DItem::prepareQt3DFrame()
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem16prepareQt3DFrameEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      node: Optional[QSGNode],
      nodeData: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *Qt3DRender::Scene3DItem::updatePaintNode(QSGNode
    *node, UpdatePaintNodeData *nodeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#updatePaintNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nodeData : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *Qt3DRender::Scene3DItem::updatePaintNode(QSGNode *node,
    #      UpdatePaintNodeData *nodeData)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem15updatePaintNodeEP7QSGNodePN10Q'
        'QuickItem19UpdatePaintNodeDataE',
        self._addressOf(node, 'QSGNode'), self._addressOf(nodeData),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def updateCameraAspectRatio(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::updateCameraAspectRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html
    """
    #  void Qt3DRender::Scene3DItem::updateCameraAspectRatio()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem23updateCameraAspectRatioEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DItem::mousePressEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN10Qt3DRender11Scene3DItem15mousePressEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender11Scene3DItem15mousePressEventEP11QMous'
          'eEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(WAIT['Qt3DRender.QRenderAspect'])
  @overload(NoneType)
  def needsRender(
      self,
      renderAspect: Optional[Qt3DRender.QRenderAspect],
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DItem::needsRender(QRenderAspect
    *renderAspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#needsRender

    Parameters
    ----------

    renderAspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Scene3DItem::needsRender(QRenderAspect *renderAspect)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem11needsRenderEPNS_13QRenderAspec'
        'tE',
        self._addressOf(renderAspect),
    )

  def updateWindowSurface(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::updateWindowSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#updateWindowSurface
    """
    #  void Qt3DRender::Scene3DItem::updateWindowSurface()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11Scene3DItem19updateWindowSurfaceEv',
    )

  def applyAspects(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DItem::applyAspects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3ditem.html#applyAspects
    """
    #  void Qt3DRender::Scene3DItem::applyAspects()
    self.uglySide.call('ritual_ZN10Qt3DRender11Scene3DItem12applyAspectsEv')

  @staticmethod
  def setCameraAspectModeHelper(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Scene3DItem::setCameraAspectModeHelper()': leans
    on 'Qt3DRender::Scene3DItem::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DItem.setCameraAspectModeHelper' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Scene3DItem::setCameraAspectModeHelper()': leans on "
        "'Qt3DRender::Scene3DItem::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setMultisample(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Scene3DItem::setMultisample(bool enable)': leans
    on 'Qt3DRender::Scene3DItem::multisampleChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DItem.setMultisample' has no cute function yet. "
        "Qt's 'void Qt3DRender::Scene3DItem::setMultisample(bool enable)': "
        "leans on 'Qt3DRender::Scene3DItem::multisampleChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def synchronize(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Scene3DItem::synchronize()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'AspectEngineDestroyer'.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DItem.synchronize' has no cute function yet. "
        "Qt's 'void Qt3DRender::Scene3DItem::synchronize()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'AspectEngineDestroyer'.")
