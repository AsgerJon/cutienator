"""
QSSGRenderDataHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderDataHelpers to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSSGRenderNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderNode = WAIT['QSSGRenderNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderDataHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderDataHelpers: a plain Python object standing
  in front of one C++ QSSGRenderDataHelpers.

  C++ hands a QSSGRenderDataHelpers around as a copy, so every C++
  QSSGRenderDataHelpers behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderDataHelpers that has a ritual and that
  Python can call so far, 1 name in all: 'updateGlobalNodeState'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QSSGRenderDataHelpers::calcInstanceTransforms(QSSGRenderNode
    *node, const VersionType version,
    QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
    QSSGGlobalRenderNodeData::InstanceTransformStore &instanceTransforms)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(QSSGRenderNode *node,
    const VersionType version, QSSGGlobalRenderNodeData::GlobalTransformStore
    &globalTransforms, QSSGGlobalRenderNodeData::GlobalOpacityStore
    &globalOpacities)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderDataHelpers::~QSSGRenderDataHelpers()': the destructor:
    Python removes its C++ QSSGRenderDataHelpers by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 1 forbidden; 1 a template; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file.

  What to expect
  --------------

  - The C++ QSSGRenderDataHelpers is created at the first use, not by
    'QSSGRenderDataHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderDataHelpers back gives a copy the ritual
    made for Python, in a new cute QSSGRenderDataHelpers.
  - Each name of Qt's QSSGRenderDataHelpers that has no cute function yet,
    'calcGlobalNodeData', 'calcGlobalVariablesIndexed',
    'calcInstanceTransforms', 'updateGlobalNodeDataIndexed', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderDataHelpers, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class GlobalStateResult(CuteNum):
    """
    The enum 'QSSGRenderDataHelpers::GlobalStateResult' of Qt, with the 4
    names Qt gives in it.
    """

    NULL = Kee[int](0)
    ActiveChanged = Kee[int](1)
    PickableChanged = Kee[int](2)
    TagChanged = Kee[int](4)

  class Strategy(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderDataHelpers::Strategy' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Initial = Kee[int](0)
    Update = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRenderNode, int)
  @overload(NoneType, int)
  def updateGlobalNodeState(
      node: Optional[QSSGRenderNode],
      version: int,
  ) -> GlobalStateResult:
    """
    Calls Qt's 'GlobalStateResult
    QSSGRenderDataHelpers::updateGlobalNodeState(QSSGRenderNode *node, const
    VersionType version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdatahelpers.html#updateGlobalNodeState

    Parameters
    ----------

    node : Optional[QSSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : int
      Passed on as it is.

    Returns
    -------

    GlobalStateResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'GlobalStateResult(number)' gives.
    """
    #  GlobalStateResult
    #      QSSGRenderDataHelpers::updateGlobalNodeState(QSSGRenderNode *node,
    #      const VersionType version)
    return QSSGRenderDataHelpers.GlobalStateResult(Rituals.call(
        'ritual_ZN21QSSGRenderDataHelpers21updateGlobalNodeStateEP14QSSGRen'
        'derNodet',
        CuteMixin._addressOf(node), version,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderDataHelpers'

  #  Qt's '~QSSGRenderDataHelpers()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRenderDataHelpers behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSSGRenderDataHelpersD1Ev'

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
  def calcGlobalNodeData(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderDataHelpers::calcGlobalNodeData': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSSGRenderDataHelpers.calcGlobalNodeData' has no cute function "
        "yet. Qt's 'QSSGRenderDataHelpers::calcGlobalNodeData': a template: "
        "a pattern and no single function.")

  @staticmethod
  def calcGlobalVariablesIndexed(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderDataHelpers::calcGlobalVariablesIndexed(QSSGRenderNode *node,
    const VersionType version, QSSGGlobalRenderNodeData::GlobalTransformStore
    &globalTransforms, QSSGGlobalRenderNodeData::GlobalOpacityStore
    &globalOpacities)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'calcGlobalNodeDataIndexedImpl'.
    """
    raise NotImplementedError(
        "'QSSGRenderDataHelpers.calcGlobalVariablesIndexed' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderDataHelpers::calcGlobalVariablesIndexed(QSSGRenderNode "
        "*node, const VersionType version, "
        "QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms, "
        "QSSGGlobalRenderNodeData::GlobalOpacityStore &globalOpacities)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'calcGlobalNodeDataIndexedImpl'.")

  @staticmethod
  def calcInstanceTransforms(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderDataHelpers::calcInstanceTransforms(QSSGRenderNode
    *node, const VersionType version,
    QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
    QSSGGlobalRenderNodeData::InstanceTransformStore &instanceTransforms)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderDataHelpers.calcInstanceTransforms' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderDataHelpers::calcInstanceTransforms(QSSGRenderNode "
        "*node, const VersionType version, "
        "QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms, "
        "QSSGGlobalRenderNodeData::InstanceTransformStore "
        "&instanceTransforms)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateGlobalNodeDataIndexed(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(QSSGRenderNode *node,
    const VersionType version, QSSGGlobalRenderNodeData::GlobalTransformStore
    &globalTransforms, QSSGGlobalRenderNodeData::GlobalOpacityStore
    &globalOpacities)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderDataHelpers.updateGlobalNodeDataIndexed' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(QSSGRenderNode "
        "*node, const VersionType version, "
        "QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms, "
        "QSSGGlobalRenderNodeData::GlobalOpacityStore &globalOpacities)': "
        "takes a type Python has no way to hand over yet.")
