"""
QSSGModelHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGModelHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGModelHelpers: a plain Python object standing in
  front of one C++ QSSGModelHelpers.

  C++ hands a QSSGModelHelpers around as a copy, so every C++
  QSSGModelHelpers behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGModelHelpers yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGModelHelpers::setModelMaterials(const QSSGFrameData
    &frameData, QSSGRenderablesId renderablesId, QSSGNodeId model,
    MaterialList materials)': names the enum 'QSSGRenderablesId', whose class
    cannot be named here.
  - Qt's 'void QSSGModelHelpers::setModelMaterials(const QSSGFrameData
    &frameData, QSSGRenderablesId renderablesId, MaterialList materials)':
    names the enum 'QSSGRenderablesId', whose class cannot be named here.
  - Qt's 'QMatrix4x4 QSSGModelHelpers::getGlobalTransform(const QSSGFrameData
    &frameData, QSSGNodeId model, QSSGPrepContextId prepId)': names the enum
    'QSSGNodeId', whose class cannot be named here.
  - Qt's 'QMatrix4x4 QSSGModelHelpers::getLocalTransform(const QSSGFrameData
    &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose class
    cannot be named here.
  - Qt's 'float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData
    &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose class
    cannot be named here.
  - Qt's 'float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData
    &frameData, QSSGNodeId model, QSSGPrepContextId prepId)': names the enum
    'QSSGNodeId', whose class cannot be named here.
  - Qt's 'float QSSGModelHelpers::getLocalOpacity(const QSSGFrameData
    &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose class
    cannot be named here.
  - Qt's 'void QSSGModelHelpers::setGlobalTransform(const QSSGFrameData
    &frameData, QSSGRenderablesId prepId, QSSGNodeId model, const QMatrix4x4
    &transform)': names the enum 'QSSGRenderablesId', whose class cannot be
    named here.
  - Qt's 'void QSSGModelHelpers::setGlobalOpacity(const QSSGFrameData
    &frameData, QSSGRenderablesId renderablesId, QSSGNodeId model, float
    opacity)': names the enum 'QSSGRenderablesId', whose class cannot be
    named here.
  - Qt's 'QSSGModelHelpers::~QSSGModelHelpers()': the destructor: Python
    removes its C++ QSSGModelHelpers by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QSSGModelHelpers is created at the first use, not by
    'QSSGModelHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGModelHelpers back gives a copy the ritual made
    for Python, in a new cute QSSGModelHelpers.
  - Each name of Qt's QSSGModelHelpers that has no cute function yet,
    'getGlobalOpacity', 'getGlobalTransform', 'getLocalOpacity',
    'getLocalTransform', 'setGlobalOpacity', 'setGlobalTransform',
    'setModelMaterials', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGModelHelpers'

  #  Qt's '~QSSGModelHelpers()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGModelHelpers behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSSGModelHelpersD1Ev'

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
  def getGlobalOpacity(*__, **_) -> Never:
    """
    - Qt's 'float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData
      &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose
      class cannot be named here.
    - Qt's 'float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData
      &frameData, QSSGNodeId model, QSSGPrepContextId prepId)': names the
      enum 'QSSGNodeId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.getGlobalOpacity' has no cute function yet. Qt's "
        "'float QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData "
        "&frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose "
        "class cannot be named here. Qt's 'float "
        "QSSGModelHelpers::getGlobalOpacity(const QSSGFrameData &frameData, "
        "QSSGNodeId model, QSSGPrepContextId prepId)': names the enum "
        "'QSSGNodeId', whose class cannot be named here.")

  @staticmethod
  def getGlobalTransform(*__, **_) -> Never:
    """
    Qt's 'QMatrix4x4 QSSGModelHelpers::getGlobalTransform(const QSSGFrameData
    &frameData, QSSGNodeId model, QSSGPrepContextId prepId)': names the enum
    'QSSGNodeId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.getGlobalTransform' has no cute function yet. "
        "Qt's 'QMatrix4x4 QSSGModelHelpers::getGlobalTransform(const "
        "QSSGFrameData &frameData, QSSGNodeId model, QSSGPrepContextId "
        "prepId)': names the enum 'QSSGNodeId', whose class cannot be named "
        "here.")

  @staticmethod
  def getLocalOpacity(*__, **_) -> Never:
    """
    Qt's 'float QSSGModelHelpers::getLocalOpacity(const QSSGFrameData
    &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.getLocalOpacity' has no cute function yet. Qt's "
        "'float QSSGModelHelpers::getLocalOpacity(const QSSGFrameData "
        "&frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose "
        "class cannot be named here.")

  @staticmethod
  def getLocalTransform(*__, **_) -> Never:
    """
    Qt's 'QMatrix4x4 QSSGModelHelpers::getLocalTransform(const QSSGFrameData
    &frameData, QSSGNodeId model)': names the enum 'QSSGNodeId', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.getLocalTransform' has no cute function yet. "
        "Qt's 'QMatrix4x4 QSSGModelHelpers::getLocalTransform(const "
        "QSSGFrameData &frameData, QSSGNodeId model)': names the enum "
        "'QSSGNodeId', whose class cannot be named here.")

  @staticmethod
  def setGlobalOpacity(*__, **_) -> Never:
    """
    Qt's 'void QSSGModelHelpers::setGlobalOpacity(const QSSGFrameData
    &frameData, QSSGRenderablesId renderablesId, QSSGNodeId model, float
    opacity)': names the enum 'QSSGRenderablesId', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.setGlobalOpacity' has no cute function yet. Qt's "
        "'void QSSGModelHelpers::setGlobalOpacity(const QSSGFrameData "
        "&frameData, QSSGRenderablesId renderablesId, QSSGNodeId model, "
        "float opacity)': names the enum 'QSSGRenderablesId', whose class "
        "cannot be named here.")

  @staticmethod
  def setGlobalTransform(*__, **_) -> Never:
    """
    Qt's 'void QSSGModelHelpers::setGlobalTransform(const QSSGFrameData
    &frameData, QSSGRenderablesId prepId, QSSGNodeId model, const QMatrix4x4
    &transform)': names the enum 'QSSGRenderablesId', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.setGlobalTransform' has no cute function yet. "
        "Qt's 'void QSSGModelHelpers::setGlobalTransform(const "
        "QSSGFrameData &frameData, QSSGRenderablesId prepId, QSSGNodeId "
        "model, const QMatrix4x4 &transform)': names the enum "
        "'QSSGRenderablesId', whose class cannot be named here.")

  @staticmethod
  def setModelMaterials(*__, **_) -> Never:
    """
    - Qt's 'void QSSGModelHelpers::setModelMaterials(const QSSGFrameData
      &frameData, QSSGRenderablesId renderablesId, QSSGNodeId model,
      MaterialList materials)': names the enum 'QSSGRenderablesId', whose
      class cannot be named here.
    - Qt's 'void QSSGModelHelpers::setModelMaterials(const QSSGFrameData
      &frameData, QSSGRenderablesId renderablesId, MaterialList materials)':
      names the enum 'QSSGRenderablesId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGModelHelpers.setModelMaterials' has no cute function yet. "
        "Qt's 'void QSSGModelHelpers::setModelMaterials(const QSSGFrameData "
        "&frameData, QSSGRenderablesId renderablesId, QSSGNodeId model, "
        "MaterialList materials)': names the enum 'QSSGRenderablesId', "
        "whose class cannot be named here. Qt's 'void "
        "QSSGModelHelpers::setModelMaterials(const QSSGFrameData "
        "&frameData, QSSGRenderablesId renderablesId, MaterialList "
        "materials)': names the enum 'QSSGRenderablesId', whose class "
        "cannot be named here.")
