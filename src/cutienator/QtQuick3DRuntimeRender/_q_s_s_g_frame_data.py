"""
QSSGFrameData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSSGLayerRenderData, QSSGRenderContextInterface
  from . import QSSGRhiGraphicsPipelineState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderContextInterface = WAIT['QSSGRenderContextInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGFrameData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGFrameData: a plain Python object standing in
  front of one C++ QSSGFrameData.

  C++ hands a QSSGFrameData around as a copy, so every C++ QSSGFrameData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGFrameData that has a ritual and that Python can
  call so far, 6 names in all: 'scheduleRenderResults', 'getRenderResult',
  'getPipelineState', 'contextInterface', 'clear', 'getCurrent'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Result QSSGFrameData::getRenderResult(QSSGResourceId userPassId,
    AttachmentSelector attachment) const': names the enum 'QSSGResourceId',
    whose class cannot be named here.
  - Qt's 'qsizetype QSSGFrameData::getAttachmentCount(QSSGResourceId
    userPassId) const': names the enum 'QSSGResourceId', whose class cannot
    be named here.
  - Qt's 'QSSGCameraId QSSGFrameData::activeCamera() const': gives the enum
    'QSSGCameraId', whose class cannot be named here.
  - Qt's 'QSSGNodeIdList QSSGFrameData::getLayerNodes(quint32 layerMask,
    TypeMask typeMask) const': gives a type Python has no way to take yet.
  - Qt's 'QSSGNodeIdList QSSGFrameData::getLayerNodes(QSSGCameraId cameraId,
    TypeMask typeMask) const': names the enum 'QSSGCameraId', whose class
    cannot be named here.
  - Qt's 'void QSSGFrameData::scheduleRenderResults(QSSGResourceId
    userPassId) const': names the enum 'QSSGResourceId', whose class cannot
    be named here.
  - Qt's 'QSSGFrameData::~QSSGFrameData()': the destructor: Python removes
    its C++ QSSGFrameData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGFrameData is created at the first use, not by
    'QSSGFrameData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGFrameData back gives a copy the ritual made for
    Python, in a new cute QSSGFrameData.
  - Each name of Qt's QSSGFrameData that has no cute function yet,
    'activeCamera', 'getAttachmentCount', 'getLayerNodes', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGFrameData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AttachmentSelector(CuteNum, scoped=True):
    """
    The enum 'QSSGFrameData::AttachmentSelector' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Attachment0 = Kee[int](0)
    Attachment1 = Kee[int](1)
    Attachment2 = Kee[int](2)
    Attachment3 = Kee[int](3)

  class RenderResult(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QSSGFrameData::RenderResult' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QSSGFrameData::RenderResults'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    AoTexture = 0x0
    DepthTexture = 0x1
    ScreenTexture = 0x2
    NormalTexture = 0x3
    MotionVectorTexture = 0x4

  RenderResults = RenderResult

  #  The classes Qt writes inside QSSGFrameData, each a class in here as in
  #  C++.

  class Result(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGFrameData::Result: a plain Python object
    standing in front of one C++ QSSGFrameData::Result.

    C++ hands a QSSGFrameData::Result around as a copy, so every C++
    QSSGFrameData::Result behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGFrameData::Result yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGFrameData::Result::~Result()': the destructor: Python removes
      its C++ QSSGFrameData::Result by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGFrameData::Result is created at the first use, not by
      'QSSGFrameData::Result(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGFrameData::Result back gives a copy the ritual
      made for Python, in a new cute QSSGFrameData::Result.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGFrameData::Result'

    #  Qt's '~QSSGFrameData::Result()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGFrameData::Result behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGFrameData6ResultD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGFrameData'

  #  Qt's '~QSSGFrameData()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGFrameData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGFrameDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RenderResult)
  def getRenderResult(self, id: RenderResult) -> Result:
    """
    Calls Qt's 'Result QSSGFrameData::getRenderResult(RenderResult id)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgframedata.html#getRenderResult

    Parameters
    ----------

    id : RenderResult
      Passed on as its number.

    Returns
    -------

    Result
      A new cute QSSGFrameData::Result around the copy Qt gave back. Python
      owns it.
    """
    #  Result QSSGFrameData::getRenderResult(RenderResult id) const
    address = self.uglySide.call(
        'ritual_ZNK13QSSGFrameData15getRenderResultENS_12RenderResultE',
        id.value,
    )
    return QSSGFrameData.Result._cuteOwning(address)

  def getPipelineState(self) -> QSSGRhiGraphicsPipelineState:
    """
    Calls Qt's 'QSSGRhiGraphicsPipelineState
    QSSGFrameData::getPipelineState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgframedata.html#getPipelineState

    Returns
    -------

    QSSGRhiGraphicsPipelineState
      A new cute QSSGRhiGraphicsPipelineState around the copy Qt gave back.
      Python owns it.
    """
    #  QSSGRhiGraphicsPipelineState QSSGFrameData::getPipelineState() const
    address = self.uglySide.call(
        'ritual_ZNK13QSSGFrameData16getPipelineStateEv',
    )
    from . import QSSGRhiGraphicsPipelineState
    return QSSGRhiGraphicsPipelineState._cuteOwning(address)

  def contextInterface(self) -> Optional[QSSGRenderContextInterface]:
    """
    Calls Qt's 'QSSGRenderContextInterface *QSSGFrameData::contextInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgframedata.html#contextInterface

    Returns
    -------

    Optional[QSSGRenderContextInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderContextInterface *QSSGFrameData::contextInterface() const
    address = self.uglySide.call(
        'ritual_ZNK13QSSGFrameData16contextInterfaceEv',
    )
    from . import QSSGRenderContextInterface
    return QSSGRenderContextInterface._cuteAt(address)

  def getCurrent(self) -> Optional[QSSGLayerRenderData]:
    """
    Calls Qt's 'QSSGLayerRenderData *QSSGFrameData::getCurrent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgframedata.html#getCurrent

    Returns
    -------

    Optional[QSSGLayerRenderData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLayerRenderData *QSSGFrameData::getCurrent() const
    address = self.uglySide.call('ritual_ZNK13QSSGFrameData10getCurrentEv')
    from . import QSSGLayerRenderData
    return QSSGLayerRenderData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSSGFrameData::QSSGFrameData()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgframedata.html#QSSGFrameData
    """
    #  QSSGFrameData::QSSGFrameData()
    self._noteCreation(QSSGFrameData, lambda: Rituals.call(
        'ritual_ZN13QSSGFrameDataC1Ev',
    ))

  @overload(QSSGRenderContextInterface)
  @overload(NoneType)
  def __init__(self, ctx: Optional[QSSGRenderContextInterface]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGFrameData::QSSGFrameData(QSSGRenderContextInterface *ctx)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgframedata.html#QSSGFrameData

    Parameters
    ----------

    ctx : Optional[QSSGRenderContextInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSSGFrameData::QSSGFrameData(QSSGRenderContextInterface *ctx)
    self._noteCreation(QSSGFrameData, lambda: Rituals.call(
        'ritual_ZN13QSSGFrameDataC1EP26QSSGRenderContextInterface',
        self._addressOf(ctx),
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

  @overload(RenderResults)
  def scheduleRenderResults(self, results: RenderResults) -> None:
    """
    Calls Qt's 'void QSSGFrameData::scheduleRenderResults(RenderResults
    results) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgframedata.html#scheduleRenderResults

    Parameters
    ----------

    results : RenderResults
      Passed on as its number.
    """
    #  void QSSGFrameData::scheduleRenderResults(RenderResults results) const
    self.uglySide.call(
        'ritual_ZNK13QSSGFrameData21scheduleRenderResultsE6QFlagsINS_12Rend'
        'erResultEE',
        results.value,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSSGFrameData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgframedata.html#clear
    """
    #  void QSSGFrameData::clear()
    self.uglySide.call('ritual_ZN13QSSGFrameData5clearEv')

  @staticmethod
  def activeCamera(*__, **_) -> Never:
    """
    Qt's 'QSSGCameraId QSSGFrameData::activeCamera() const': gives the enum
    'QSSGCameraId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGFrameData.activeCamera' has no cute function yet. Qt's "
        "'QSSGCameraId QSSGFrameData::activeCamera() const': gives the enum "
        "'QSSGCameraId', whose class cannot be named here.")

  @staticmethod
  def getAttachmentCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSSGFrameData::getAttachmentCount(QSSGResourceId
    userPassId) const': names the enum 'QSSGResourceId', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QSSGFrameData.getAttachmentCount' has no cute function yet. Qt's "
        "'qsizetype QSSGFrameData::getAttachmentCount(QSSGResourceId "
        "userPassId) const': names the enum 'QSSGResourceId', whose class "
        "cannot be named here.")

  @staticmethod
  def getLayerNodes(*__, **_) -> Never:
    """
    - Qt's 'QSSGNodeIdList QSSGFrameData::getLayerNodes(quint32 layerMask,
      TypeMask typeMask) const': gives a type Python has no way to take yet.
    - Qt's 'QSSGNodeIdList QSSGFrameData::getLayerNodes(QSSGCameraId
      cameraId, TypeMask typeMask) const': names the enum 'QSSGCameraId',
      whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGFrameData.getLayerNodes' has no cute function yet. Qt's "
        "'QSSGNodeIdList QSSGFrameData::getLayerNodes(quint32 layerMask, "
        "TypeMask typeMask) const': gives a type Python has no way to take "
        "yet. Qt's 'QSSGNodeIdList "
        "QSSGFrameData::getLayerNodes(QSSGCameraId cameraId, TypeMask "
        "typeMask) const': names the enum 'QSSGCameraId', whose class "
        "cannot be named here.")
