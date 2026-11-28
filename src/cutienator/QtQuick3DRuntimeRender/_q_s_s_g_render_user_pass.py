"""
QSSGRenderUserPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderUserPass to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderUserPass(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderUserPass: a plain Python object standing in
  front of one C++ QSSGRenderUserPass.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's QSSGRenderUserPass
  is built on Qt's QSSGRenderGraphObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderUserPass that has a ritual and that Python
  can call so far, 6 names in all: 'isDirty', 'markDirty', 'clearDirty',
  'isReady', 'setDependencyIndex', 'resetCommands'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderUserPass::~QSSGRenderUserPass()': the destructor: Python
    never removes a C++ QSSGRenderUserPass.
  - Qt's 'void QSSGRenderUserPass::finalizeShaders(const
    QSSGRenderContextInterface &ctx)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSSGRenderUserPass is created at the first use, not by
    'QSSGRenderUserPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderUserPass.
  - Each name of Qt's QSSGRenderUserPass that has no cute function yet,
    'finalizeShaders', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderUserPass, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderUserPass::DirtyFlag' of Qt, with the 1 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ShaderDirty = Kee[int](1)

  class MaterialModes(CuteNum):
    """
    The enum 'QSSGRenderUserPass::MaterialModes' of Qt, with the 3 names Qt
    gives in it.
    """

    OriginalMaterial = Kee[int](0)
    AugmentMaterial = Kee[int](1)
    OverrideMaterial = Kee[int](2)

  class PassModes(CuteNum):
    """
    The enum 'QSSGRenderUserPass::PassModes' of Qt, with the 4 names Qt gives
    in it.
    """

    UserPass = Kee[int](0)
    SkyboxPass = Kee[int](1)
    Item2DPass = Kee[int](2)
    InfiniteGridPass = Kee[int](3)

  class Role(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderUserPass::Role' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    TopLevel = Kee[int](0)
    SubPass = Kee[int](1)

  class State(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderUserPass::State' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    Ready = Kee[int](1)
    Error = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderUserPass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DirtyFlag)
  def isDirty(self, flag: DirtyFlag) -> bool:
    """
    Calls Qt's 'bool QSSGRenderUserPass::isDirty(DirtyFlag flag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderuserpass.html#isDirty

    Parameters
    ----------

    flag : DirtyFlag
      Passed on as its number.
    """
    #  bool QSSGRenderUserPass::isDirty(DirtyFlag flag) const
    return self.uglySide.call(
        'ritual_ZNK18QSSGRenderUserPass7isDirtyENS_9DirtyFlagE', flag.value,
    )

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderUserPass::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderuserpass.html#isReady
    """
    #  bool QSSGRenderUserPass::isReady() const
    return self.uglySide.call('ritual_ZNK18QSSGRenderUserPass7isReadyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDependencyIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QSSGRenderUserPass::setDependencyIndex(quint32 index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderuserpass.html#setDependencyIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QSSGRenderUserPass::setDependencyIndex(quint32 index)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderUserPass18setDependencyIndexEj', index,
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
    Notes what was given, for Qt's
    'QSSGRenderUserPass::QSSGRenderUserPass()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderuserpass.html#QSSGRenderUserPass
    """
    #  QSSGRenderUserPass::QSSGRenderUserPass()
    self._noteCreation(QSSGRenderUserPass, lambda: Rituals.call(
        'ritual_ZN18QSSGRenderUserPassC1Ev',
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

  @overload(DirtyFlag)
  def markDirty(self, flag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderUserPass::markDirty(DirtyFlag flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderuserpass.html#markDirty

    Parameters
    ----------

    flag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderUserPass::markDirty(DirtyFlag flag)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderUserPass9markDirtyENS_9DirtyFlagE', flag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, flag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderUserPass::clearDirty(DirtyFlag flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderuserpass.html#clearDirty

    Parameters
    ----------

    flag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderUserPass::clearDirty(DirtyFlag flag)
    self.uglySide.call(
        'ritual_ZN18QSSGRenderUserPass10clearDirtyENS_9DirtyFlagE',
        flag.value,
    )

  def resetCommands(self) -> None:
    """
    Calls Qt's 'void QSSGRenderUserPass::resetCommands()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderuserpass.html#resetCommands
    """
    #  void QSSGRenderUserPass::resetCommands()
    self.uglySide.call('ritual_ZN18QSSGRenderUserPass13resetCommandsEv')

  @staticmethod
  def finalizeShaders(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderUserPass::finalizeShaders(const
    QSSGRenderContextInterface &ctx)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderUserPass.finalizeShaders' has no cute function yet. "
        "Qt's 'void QSSGRenderUserPass::finalizeShaders(const "
        "QSSGRenderContextInterface &ctx)': takes a type Python has no way "
        "to hand over yet.")
