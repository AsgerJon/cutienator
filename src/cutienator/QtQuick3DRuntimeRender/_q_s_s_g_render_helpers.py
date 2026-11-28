"""
QSSGRenderHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderHelpers: a plain Python object standing in
  front of one C++ QSSGRenderHelpers.

  C++ hands a QSSGRenderHelpers around as a copy, so every C++
  QSSGRenderHelpers behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGRenderHelpers yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderablesId QSSGRenderHelpers::createRenderables(const
    QSSGFrameData &frameData, QSSGPrepContextId prepId, const QSSGNodeIdList
    &nodes, CreateFlags flags)': names the enum 'QSSGPrepContextId', whose
    class cannot be named here.
  - Qt's 'QSSGPrepContextId QSSGRenderHelpers::prepareForRender(const
    QSSGFrameData &frameData, const QSSGRenderExtension &ext, QSSGCameraId
    cameraId, quint32 slot)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGPrepResultId QSSGRenderHelpers::commit(const QSSGFrameData
    &frameData, QSSGPrepContextId prepId, QSSGRenderablesId renderablesId,
    float lodThreshold)': names the enum 'QSSGPrepContextId', whose class
    cannot be named here.
  - Qt's 'void QSSGRenderHelpers::prepareRenderables(const QSSGFrameData
    &frameData, QSSGPrepResultId prepId, QRhiRenderPassDescriptor
    *renderPassDescriptor, QSSGRhiGraphicsPipelineState &ps,
    QSSGRenderablesFilters filter)': names the enum 'QSSGPrepResultId', whose
    class cannot be named here.
  - Qt's 'void QSSGRenderHelpers::renderRenderables(const QSSGFrameData
    &frameData, QSSGPrepResultId prepId)': names the enum 'QSSGPrepResultId',
    whose class cannot be named here.
  - Qt's 'QSSGRenderHelpers::~QSSGRenderHelpers()': the destructor: Python
    removes its C++ QSSGRenderHelpers by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderHelpers is created at the first use, not by
    'QSSGRenderHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderHelpers back gives a copy the ritual made
    for Python, in a new cute QSSGRenderHelpers.
  - Each name of Qt's QSSGRenderHelpers that has no cute function yet,
    'commit', 'createRenderables', 'prepareForRender', 'prepareRenderables',
    'renderRenderables', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderHelpers, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CreateFlag(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QSSGRenderHelpers::CreateFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QSSGRenderHelpers::CreateFlags'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NULL = 0x0
    Recurse = 0x1
    Steal = 0x2

  CreateFlags = CreateFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderHelpers'

  #  Qt's '~QSSGRenderHelpers()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGRenderHelpers behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSSGRenderHelpersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSSGRenderHelpers::QSSGRenderHelpers()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderhelpers.html#QSSGRenderHelpers
    """
    #  QSSGRenderHelpers::QSSGRenderHelpers()
    self._noteCreation(QSSGRenderHelpers, lambda: Rituals.call(
        'ritual_ZN17QSSGRenderHelpersC1Ev',
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

  @staticmethod
  def commit(*__, **_) -> Never:
    """
    Qt's 'QSSGPrepResultId QSSGRenderHelpers::commit(const QSSGFrameData
    &frameData, QSSGPrepContextId prepId, QSSGRenderablesId renderablesId,
    float lodThreshold)': names the enum 'QSSGPrepContextId', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGRenderHelpers.commit' has no cute function yet. Qt's "
        "'QSSGPrepResultId QSSGRenderHelpers::commit(const QSSGFrameData "
        "&frameData, QSSGPrepContextId prepId, QSSGRenderablesId "
        "renderablesId, float lodThreshold)': names the enum "
        "'QSSGPrepContextId', whose class cannot be named here.")

  @staticmethod
  def createRenderables(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderablesId QSSGRenderHelpers::createRenderables(const
    QSSGFrameData &frameData, QSSGPrepContextId prepId, const QSSGNodeIdList
    &nodes, CreateFlags flags)': names the enum 'QSSGPrepContextId', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGRenderHelpers.createRenderables' has no cute function yet. "
        "Qt's 'QSSGRenderablesId QSSGRenderHelpers::createRenderables(const "
        "QSSGFrameData &frameData, QSSGPrepContextId prepId, const "
        "QSSGNodeIdList &nodes, CreateFlags flags)': names the enum "
        "'QSSGPrepContextId', whose class cannot be named here.")

  @staticmethod
  def prepareForRender(*__, **_) -> Never:
    """
    Qt's 'QSSGPrepContextId QSSGRenderHelpers::prepareForRender(const
    QSSGFrameData &frameData, const QSSGRenderExtension &ext, QSSGCameraId
    cameraId, quint32 slot)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRenderHelpers.prepareForRender' has no cute function yet. "
        "Qt's 'QSSGPrepContextId QSSGRenderHelpers::prepareForRender(const "
        "QSSGFrameData &frameData, const QSSGRenderExtension &ext, "
        "QSSGCameraId cameraId, quint32 slot)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def prepareRenderables(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderHelpers::prepareRenderables(const QSSGFrameData
    &frameData, QSSGPrepResultId prepId, QRhiRenderPassDescriptor
    *renderPassDescriptor, QSSGRhiGraphicsPipelineState &ps,
    QSSGRenderablesFilters filter)': names the enum 'QSSGPrepResultId', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGRenderHelpers.prepareRenderables' has no cute function yet. "
        "Qt's 'void QSSGRenderHelpers::prepareRenderables(const "
        "QSSGFrameData &frameData, QSSGPrepResultId prepId, "
        "QRhiRenderPassDescriptor *renderPassDescriptor, "
        "QSSGRhiGraphicsPipelineState &ps, QSSGRenderablesFilters filter)': "
        "names the enum 'QSSGPrepResultId', whose class cannot be named "
        "here.")

  @staticmethod
  def renderRenderables(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderHelpers::renderRenderables(const QSSGFrameData
    &frameData, QSSGPrepResultId prepId)': names the enum 'QSSGPrepResultId',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGRenderHelpers.renderRenderables' has no cute function yet. "
        "Qt's 'void QSSGRenderHelpers::renderRenderables(const "
        "QSSGFrameData &frameData, QSSGPrepResultId prepId)': names the "
        "enum 'QSSGPrepResultId', whose class cannot be named here.")
