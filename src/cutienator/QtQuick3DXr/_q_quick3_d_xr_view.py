"""
QQuick3DXrView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QVariant
  from ..QtGui import QVector3D
  from ..QtQuick import QQuickItem
  from ..QtQuick3D import QQuick3DModel, QQuick3DPickResult
  from ..QtQuick3D import QQuick3DRenderStats, QQuick3DSceneEnvironment
  from ..QtQuick3D import QQuick3DViewport
  from . import QQuick3DXrItem, QQuick3DXrManager, QQuick3DXrOrigin
  from . import QQuick3DXrRuntimeInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DSceneEnvironment = WAIT['QQuick3DSceneEnvironment']
  QQuick3DXrItem = WAIT['QQuick3DXrItem']
  QQuick3DXrOrigin = WAIT['QQuick3DXrOrigin']
  QQuickItem = WAIT['QQuickItem']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrView(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DXrView: a plain Python object standing in
  front of one C++ QQuick3DXrView.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DXrView is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrView that has a ritual and that Python can
  call so far, 47 names in all: 'metaObject', 'tr', 'xrOrigin',
  'environment', 'passthroughSupported', 'passthroughEnabled',
  'fixedFoveation', 'setFixedFoveation', 'runtimeInfo',
  'isQuitOnSessionEndEnabled', 'renderStats', 'rayPick', 'rayPickAll',
  'closestPointPick', 'setTouchpoint', 'processTouch', 'touchpointState',
  'referenceSpace', 'setReferenceSpace', 'depthSubmissionEnabled',
  'registerXrItem', 'unregisterXrItem', 'isMultiViewRenderingSupported',
  'multiViewRenderingEnabled', 'xrManager', 'setEnvironment',
  'setPassthroughEnabled', 'setQuitOnSessionEnd',
  'setDepthSubmissionEnabled', 'setXROrigin', 'updateViewportGeometry',
  'handleSessionEnded', 'handleClearColorChanged', 'handleAAChanged', 'init',
  'initializeFailed', 'sessionEnded', 'xrOriginChanged',
  'environmentChanged', 'passthroughEnabledChanged',
  'quitOnSessionEndChanged', 'fixedFoveationChanged', 'frameReady',
  'referenceSpaceChanged', 'depthSubmissionEnabledChanged',
  'multiViewRenderingEnabledChanged', 'view3d'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DXrView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrView::~QQuick3DXrView()': the destructor: Python never
    removes a C++ QQuick3DXrView.
  - Qt's 'bool QQuick3DXrView::handleVirtualTouch(TouchTarget target, const
    QVector3D &pos, TouchState *touchState, QVector3D *offset)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrView is created at the first use, not by
    'QQuick3DXrView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrView.
  - Qt tells when it has removed the C++ QQuick3DXrView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrView that has no cute function yet,
    'handleVirtualTouch', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DXrView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FoveationLevel(CuteNum):
    """
    The enum 'QQuick3DXrView::FoveationLevel' of Qt, with the 4 names Qt
    gives in it.
    """

    NoFoveation = Kee[int](0)
    LowFoveation = Kee[int](1)
    MediumFoveation = Kee[int](2)
    HighFoveation = Kee[int](3)

  class ReferenceSpace(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrView::ReferenceSpace' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    ReferenceSpaceUnknown = Kee[int](0)
    ReferenceSpaceLocal = Kee[int](1)
    ReferenceSpaceStage = Kee[int](2)
    ReferenceSpaceLocalFloor = Kee[int](3)

  #  The classes Qt writes inside QQuick3DXrView, each a class in here as in
  #  C++.

  class TouchState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DXrView::TouchState: a plain Python object
    standing in front of one C++ QQuick3DXrView::TouchState.

    C++ hands a QQuick3DXrView::TouchState around as a copy, so every C++
    QQuick3DXrView::TouchState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuick3DXrView::TouchState yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DXrView::TouchState::~TouchState()': the destructor:
      Python removes its C++ QQuick3DXrView::TouchState by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuick3DXrView::TouchState is created at the first use, not by
      'QQuick3DXrView::TouchState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DXrView::TouchState back gives a copy the
      ritual made for Python, in a new cute QQuick3DXrView::TouchState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DXrView::TouchState'

    #  Qt's '~QQuick3DXrView::TouchState()'. Naming it makes this a value
    #  class: Python owns every C++ QQuick3DXrView::TouchState behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQuick3DXrView10TouchStateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQuick3DXrView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#tr

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
    #  QString QQuick3DXrView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuick3DXrView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrView'

  #  A C++ QQuick3DXrView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xrOrigin(self) -> Optional[QQuick3DXrOrigin]:
    """
    Calls Qt's 'QQuick3DXrOrigin *QQuick3DXrView::xrOrigin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#xrOrigin

    Returns
    -------

    Optional[QQuick3DXrOrigin]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrOrigin *QQuick3DXrView::xrOrigin() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView8xrOriginEv')
    from . import QQuick3DXrOrigin
    return QQuick3DXrOrigin._cuteAt(address)

  def environment(self) -> Optional[QQuick3DSceneEnvironment]:
    """
    Calls Qt's 'QQuick3DSceneEnvironment *QQuick3DXrView::environment()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#environment

    Returns
    -------

    Optional[QQuick3DSceneEnvironment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneEnvironment *QQuick3DXrView::environment() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView11environmentEv')
    from ..QtQuick3D import QQuick3DSceneEnvironment
    return QQuick3DSceneEnvironment._cuteAt(address)

  def passthroughSupported(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::passthroughSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#passthroughSupported
    """
    #  bool QQuick3DXrView::passthroughSupported() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView20passthroughSupportedEv',
    )

  def passthroughEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::passthroughEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#passthroughEnabled
    """
    #  bool QQuick3DXrView::passthroughEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView18passthroughEnabledEv',
    )

  def fixedFoveation(self) -> FoveationLevel:
    """
    Calls Qt's 'FoveationLevel QQuick3DXrView::fixedFoveation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#fixedFoveation

    Returns
    -------

    FoveationLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FoveationLevel(number)'
      gives.
    """
    #  FoveationLevel QQuick3DXrView::fixedFoveation() const
    return QQuick3DXrView.FoveationLevel(self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView14fixedFoveationEv',
    ))

  def runtimeInfo(self) -> Optional[QQuick3DXrRuntimeInfo]:
    """
    Calls Qt's 'QQuick3DXrRuntimeInfo *QQuick3DXrView::runtimeInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#runtimeInfo

    Returns
    -------

    Optional[QQuick3DXrRuntimeInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrRuntimeInfo *QQuick3DXrView::runtimeInfo() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView11runtimeInfoEv')
    from . import QQuick3DXrRuntimeInfo
    return QQuick3DXrRuntimeInfo._cuteAt(address)

  def isQuitOnSessionEndEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::isQuitOnSessionEndEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#isQuitOnSessionEndEnabled
    """
    #  bool QQuick3DXrView::isQuitOnSessionEndEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView25isQuitOnSessionEndEnabledEv',
    )

  def renderStats(self) -> Optional[QQuick3DRenderStats]:
    """
    Calls Qt's 'QQuick3DRenderStats *QQuick3DXrView::renderStats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#renderStats

    Returns
    -------

    Optional[QQuick3DRenderStats]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderStats *QQuick3DXrView::renderStats() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView11renderStatsEv')
    from ..QtQuick3D import QQuick3DRenderStats
    return QQuick3DRenderStats._cuteAt(address)

  @overload(QVector3D, QVector3D)
  def rayPick(
      self,
      origin: QVector3D,
      direction: QVector3D,
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D
    &origin, const QVector3D &direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#rayPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D &origin,
    #      const QVector3D &direction) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView7rayPickERK9QVector3DS2_',
        self._valueOf(origin), self._valueOf(direction),
    )
    from ..QtQuick3D import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QVector3D, QVector3D, QQuick3DModel)
  @overload(QVector3D, QVector3D, NoneType)
  def rayPick(
      self,
      origin: QVector3D,
      direction: QVector3D,
      model: Optional[QQuick3DModel],
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D
    &origin, const QVector3D &direction, QQuick3DModel *model) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#rayPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DXrView::rayPick(const QVector3D &origin,
    #      const QVector3D &direction, QQuick3DModel *model) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView7rayPickERK9QVector3DS2_P13QQuick3DModel',
        self._valueOf(origin), self._valueOf(direction),
        self._addressOf(model),
    )
    from ..QtQuick3D import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QVector3D, QVector3D)
  def rayPickAll(
      self,
      origin: QVector3D,
      direction: QVector3D,
  ) -> QList[QQuick3DPickResult]:
    """
    Calls Qt's 'QList<QQuick3DPickResult> QQuick3DXrView::rayPickAll(const
    QVector3D &origin, const QVector3D &direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#rayPickAll

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QList[QQuick3DPickResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DPickResult> QQuick3DXrView::rayPickAll(const QVector3D
    #      &origin, const QVector3D &direction) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView10rayPickAllERK9QVector3DS2_',
        self._valueOf(origin), self._valueOf(direction),
    )
    from ..QtQuick3D import QQuick3DPickResult
    return QList[QQuick3DPickResult]._cuteOwning(address)

  @overload(QVector3D, float)
  @overload(QVector3D, float, QQuick3DModel)
  @overload(QVector3D, float, NoneType)
  def closestPointPick(
      self,
      origin: QVector3D,
      radius: float,
      model: Optional[QQuick3DModel] = None,
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DXrView::closestPointPick(const
    QVector3D &origin, float radius, QQuick3DModel *model) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#closestPointPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DXrView::closestPointPick(const QVector3D
    #      &origin, float radius, QQuick3DModel *model) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView16closestPointPickERK9QVector3DfP13QQuic'
        'k3DModel',
        self._valueOf(origin), radius, self._addressOf(model),
    )
    from ..QtQuick3D import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(int)
  def touchpointState(self, pointId: int) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQuick3DXrView::touchpointState(int pointId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#touchpointState

    Parameters
    ----------

    pointId : int
      Passed on as it is.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQuick3DXrView::touchpointState(int pointId) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView15touchpointStateEi', pointId,
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def referenceSpace(self) -> ReferenceSpace:
    """
    Calls Qt's 'ReferenceSpace QQuick3DXrView::referenceSpace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#referenceSpace

    Returns
    -------

    ReferenceSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ReferenceSpace(number)'
      gives.
    """
    #  ReferenceSpace QQuick3DXrView::referenceSpace() const
    return QQuick3DXrView.ReferenceSpace(self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView14referenceSpaceEv',
    ))

  def depthSubmissionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::depthSubmissionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#depthSubmissionEnabled
    """
    #  bool QQuick3DXrView::depthSubmissionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView22depthSubmissionEnabledEv',
    )

  def isMultiViewRenderingSupported(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::isMultiViewRenderingSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#isMultiViewRenderingSupported
    """
    #  bool QQuick3DXrView::isMultiViewRenderingSupported() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView29isMultiViewRenderingSupportedEv',
    )

  def multiViewRenderingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::multiViewRenderingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#multiViewRenderingEnabled
    """
    #  bool QQuick3DXrView::multiViewRenderingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DXrView25multiViewRenderingEnabledEv',
    )

  def view3d(self) -> Optional[QQuick3DViewport]:
    """
    Calls Qt's 'QQuick3DViewport *QQuick3DXrView::view3d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#view3d

    Returns
    -------

    Optional[QQuick3DViewport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DViewport *QQuick3DXrView::view3d() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrView6view3dEv')
    from ..QtQuick3D import QQuick3DViewport
    return QQuick3DViewport._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FoveationLevel)
  def setFixedFoveation(self, level: FoveationLevel) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setFixedFoveation(FoveationLevel
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#setFixedFoveation

    Parameters
    ----------

    level : FoveationLevel
      Passed on as its number.
    """
    #  void QQuick3DXrView::setFixedFoveation(FoveationLevel level)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView17setFixedFoveationENS_14FoveationLevelE',
        level.value,
    )

  @overload(QQuickItem, QPointF, int, bool)
  @overload(NoneType, QPointF, int, bool)
  def setTouchpoint(
      self,
      target: Optional[QQuickItem],
      position: QPointF,
      pointId: int,
      active: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setTouchpoint(QQuickItem *target, const
    QPointF &position, int pointId, bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#setTouchpoint

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pointId : int
      Passed on as it is.

    active : bool
      Passed on as it is.
    """
    #  void QQuick3DXrView::setTouchpoint(QQuickItem *target, const QPointF
    #      &position, int pointId, bool active)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView13setTouchpointEP10QQuickItemRK7QPointFib',
        self._addressOf(target), self._valueOf(position, 'QPointF'), pointId,
        active,
    )

  @overload(ReferenceSpace)
  def setReferenceSpace(self, newReferenceSpace: ReferenceSpace) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setReferenceSpace(ReferenceSpace
    newReferenceSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#setReferenceSpace

    Parameters
    ----------

    newReferenceSpace : ReferenceSpace
      Passed on as its number.
    """
    #  void QQuick3DXrView::setReferenceSpace(ReferenceSpace
    #      newReferenceSpace)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView17setReferenceSpaceENS_14ReferenceSpaceE',
        newReferenceSpace.value,
    )

  @overload(QQuick3DSceneEnvironment)
  @overload(NoneType)
  def setEnvironment(
      self,
      environment: Optional[QQuick3DSceneEnvironment],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setEnvironment(QQuick3DSceneEnvironment
    *environment)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#setEnvironment

    Parameters
    ----------

    environment : Optional[QQuick3DSceneEnvironment]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrView::setEnvironment(QQuick3DSceneEnvironment
    #      *environment)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView14setEnvironmentEP24QQuick3DSceneEnvironm'
        'ent',
        self._addressOf(environment),
    )

  @overload(bool)
  def setPassthroughEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setPassthroughEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#setPassthroughEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuick3DXrView::setPassthroughEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView21setPassthroughEnabledEb', enable,
    )

  @overload(bool)
  def setQuitOnSessionEnd(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setQuitOnSessionEnd(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#setQuitOnSessionEnd

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuick3DXrView::setQuitOnSessionEnd(bool enable)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView19setQuitOnSessionEndEb', enable,
    )

  @overload(bool)
  def setDepthSubmissionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setDepthSubmissionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#setDepthSubmissionEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuick3DXrView::setDepthSubmissionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView25setDepthSubmissionEnabledEb', enable,
    )

  @overload(QQuick3DXrOrigin)
  @overload(NoneType)
  def setXROrigin(self, newXrOrigin: Optional[QQuick3DXrOrigin]) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::setXROrigin(QQuick3DXrOrigin
    *newXrOrigin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#setXROrigin

    Parameters
    ----------

    newXrOrigin : Optional[QQuick3DXrOrigin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrView::setXROrigin(QQuick3DXrOrigin *newXrOrigin)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView11setXROriginEP16QQuick3DXrOrigin',
        self._addressOf(newXrOrigin),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuick3DXrView::QQuick3DXrView()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#QQuick3DXrView
    """
    #  QQuick3DXrView::QQuick3DXrView()
    self._noteCreation(QQuick3DXrView, lambda: Rituals.call(
        'ritual_ZN14QQuick3DXrViewC1Ev',
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

  @overload(QVector3D, int)
  def processTouch(self, pos: QVector3D, pointId: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrView::processTouch(const QVector3D &pos,
    int pointId)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#processTouch

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    pointId : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrView::processTouch(const QVector3D &pos, int
    #      pointId)
    address = self.uglySide.call(
        'ritual_ZN14QQuick3DXrView12processTouchERK9QVector3Di',
        self._valueOf(pos), pointId,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QQuick3DXrItem)
  @overload(NoneType)
  def registerXrItem(self, newXrItem: Optional[QQuick3DXrItem]) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::registerXrItem(QQuick3DXrItem
    *newXrItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#registerXrItem

    Parameters
    ----------

    newXrItem : Optional[QQuick3DXrItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrView::registerXrItem(QQuick3DXrItem *newXrItem)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView14registerXrItemEP14QQuick3DXrItem',
        self._addressOf(newXrItem),
    )

  @overload(QQuick3DXrItem)
  @overload(NoneType)
  def unregisterXrItem(self, xrItem: Optional[QQuick3DXrItem]) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::unregisterXrItem(QQuick3DXrItem
    *xrItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#unregisterXrItem

    Parameters
    ----------

    xrItem : Optional[QQuick3DXrItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrView::unregisterXrItem(QQuick3DXrItem *xrItem)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView16unregisterXrItemEP14QQuick3DXrItem',
        self._addressOf(xrItem),
    )

  def xrManager(self) -> Optional[QQuick3DXrManager]:
    """
    Calls Qt's 'QQuick3DXrManager *QQuick3DXrView::xrManager()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#xrManager

    Returns
    -------

    Optional[QQuick3DXrManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrManager *QQuick3DXrView::xrManager()
    address = self.uglySide.call('ritual_ZN14QQuick3DXrView9xrManagerEv')
    from . import QQuick3DXrManager
    return QQuick3DXrManager._cuteAt(address)

  def updateViewportGeometry(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::updateViewportGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#updateViewportGeometry
    """
    #  void QQuick3DXrView::updateViewportGeometry()
    self.uglySide.call('ritual_ZN14QQuick3DXrView22updateViewportGeometryEv')

  def handleSessionEnded(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::handleSessionEnded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#handleSessionEnded
    """
    #  void QQuick3DXrView::handleSessionEnded()
    self.uglySide.call('ritual_ZN14QQuick3DXrView18handleSessionEndedEv')

  def handleClearColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::handleClearColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#handleClearColorChanged
    """
    #  void QQuick3DXrView::handleClearColorChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView23handleClearColorChangedEv',
    )

  def handleAAChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::handleAAChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#handleAAChanged
    """
    #  void QQuick3DXrView::handleAAChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrView15handleAAChangedEv')

  def init(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrView::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#init
    """
    #  bool QQuick3DXrView::init()
    return self.uglySide.call('ritual_ZN14QQuick3DXrView4initEv')

  @overload(str)
  def initializeFailed(self, errorString: str) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::initializeFailed(const QString
    &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#initializeFailed

    Parameters
    ----------

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DXrView::initializeFailed(const QString &errorString)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView16initializeFailedERK7QString',
        errorString,
    )

  def sessionEnded(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::sessionEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#sessionEnded
    """
    #  void QQuick3DXrView::sessionEnded()
    self.uglySide.call('ritual_ZN14QQuick3DXrView12sessionEndedEv')

  def xrOriginChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::xrOriginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#xrOriginChanged
    """
    #  void QQuick3DXrView::xrOriginChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrView15xrOriginChangedEv')

  @overload(QQuick3DSceneEnvironment)
  @overload(NoneType)
  def environmentChanged(
      self,
      environment: Optional[QQuick3DSceneEnvironment],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrView::environmentChanged(QQuick3DSceneEnvironment
    *environment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#environmentChanged

    Parameters
    ----------

    environment : Optional[QQuick3DSceneEnvironment]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrView::environmentChanged(QQuick3DSceneEnvironment
    #      *environment)
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView18environmentChangedEP24QQuick3DSceneEnvi'
        'ronment',
        self._addressOf(environment),
    )

  def passthroughEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::passthroughEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#passthroughEnabledChanged
    """
    #  void QQuick3DXrView::passthroughEnabledChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView25passthroughEnabledChangedEv',
    )

  def quitOnSessionEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::quitOnSessionEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#quitOnSessionEndChanged
    """
    #  void QQuick3DXrView::quitOnSessionEndChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView23quitOnSessionEndChangedEv',
    )

  def fixedFoveationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::fixedFoveationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#fixedFoveationChanged
    """
    #  void QQuick3DXrView::fixedFoveationChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrView21fixedFoveationChangedEv')

  def frameReady(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::frameReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrview.html#frameReady
    """
    #  void QQuick3DXrView::frameReady()
    self.uglySide.call('ritual_ZN14QQuick3DXrView10frameReadyEv')

  def referenceSpaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::referenceSpaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#referenceSpaceChanged
    """
    #  void QQuick3DXrView::referenceSpaceChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrView21referenceSpaceChangedEv')

  def depthSubmissionEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::depthSubmissionEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html#depthSubmissionEnabledChanged
    """
    #  void QQuick3DXrView::depthSubmissionEnabledChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView29depthSubmissionEnabledChangedEv',
    )

  def multiViewRenderingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrView::multiViewRenderingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrview.html
    """
    #  void QQuick3DXrView::multiViewRenderingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrView32multiViewRenderingEnabledChangedEv',
    )

  @staticmethod
  def handleVirtualTouch(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrView::handleVirtualTouch(TouchTarget target, const
    QVector3D &pos, TouchState *touchState, QVector3D *offset)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrView.handleVirtualTouch' has no cute function yet. Qt's "
        "'bool QQuick3DXrView::handleVirtualTouch(TouchTarget target, const "
        "QVector3D &pos, TouchState *touchState, QVector3D *offset)': takes "
        "a type Python has no way to hand over yet.")
