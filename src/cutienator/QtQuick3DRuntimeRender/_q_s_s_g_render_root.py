"""
QSSGRenderRoot binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderroot_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderRoot to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSSGRenderNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderRoot(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderRoot: a plain Python object standing in
  front of one C++ QSSGRenderRoot.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderRoot is built
  on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderRoot that has a ritual and that Python can
  call so far, 6 names in all: 'isDirty', 'markDirty', 'clearDirty',
  'setStartVersion', 'startVersion', 'reindex'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderRoot::~QSSGRenderRoot()': the destructor: Python never
    removes a C++ QSSGRenderRoot.
  - Qt's 'const std::shared_ptr<QSSGGlobalRenderNodeData>
    &QSSGRenderRoot::globalNodeData() const': gives a type Python has no way
    to take yet.
  - Qt's 'QSSGRenderRoot *QSSGRenderRoot::get(QSSGRenderRoot **ref)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGRenderRoot is created at the first use, not by
    'QSSGRenderRoot(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderRoot.
  - Each name of Qt's QSSGRenderRoot that has no cute function yet, 'get',
    'globalNodeData', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderRoot, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderRoot::DirtyFlag' of Qt, with the 1 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    TreeDirty = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderRoot'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DirtyFlag)
  def isDirty(self, dirtyFlag: DirtyFlag) -> bool:
    """
    Calls Qt's 'bool QSSGRenderRoot::isDirty(DirtyFlag dirtyFlag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#isDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  bool QSSGRenderRoot::isDirty(DirtyFlag dirtyFlag) const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRenderRoot7isDirtyENS_9DirtyFlagE', dirtyFlag.value,
    )

  def startVersion(self) -> int:
    """
    Calls Qt's 'VersionType QSSGRenderRoot::startVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#startVersion
    """
    #  VersionType QSSGRenderRoot::startVersion() const
    return self.uglySide.call('ritual_ZNK14QSSGRenderRoot12startVersionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStartVersion(self, startVersion: int) -> None:
    """
    Calls Qt's 'void QSSGRenderRoot::setStartVersion(VersionType
    startVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderroot.html#setStartVersion

    Parameters
    ----------

    startVersion : int
      Passed on as it is.
    """
    #  void QSSGRenderRoot::setStartVersion(VersionType startVersion)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderRoot15setStartVersionEt', startVersion,
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
    Notes what was given, for Qt's 'QSSGRenderRoot::QSSGRenderRoot()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#QSSGRenderRoot
    """
    #  QSSGRenderRoot::QSSGRenderRoot()
    self._noteCreation(QSSGRenderRoot, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderRootC1Ev',
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
  def markDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderRoot::markDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#markDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderRoot::markDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderRoot9markDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderRoot::clearDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#clearDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderRoot::clearDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderRoot10clearDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  def reindex(self) -> None:
    """
    Calls Qt's 'void QSSGRenderRoot::reindex()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderroot.html#reindex
    """
    #  void QSSGRenderRoot::reindex()
    self.uglySide.call('ritual_ZN14QSSGRenderRoot7reindexEv')

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderRoot *QSSGRenderRoot::get(QSSGRenderRoot **ref)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRoot.get' has no cute function yet. Qt's "
        "'QSSGRenderRoot *QSSGRenderRoot::get(QSSGRenderRoot **ref)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def globalNodeData(*__, **_) -> Never:
    """
    Qt's 'const std::shared_ptr<QSSGGlobalRenderNodeData>
    &QSSGRenderRoot::globalNodeData() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRoot.globalNodeData' has no cute function yet. Qt's "
        "'const std::shared_ptr<QSSGGlobalRenderNodeData> "
        "&QSSGRenderRoot::globalNodeData() const': gives a type Python has "
        "no way to take yet.")
