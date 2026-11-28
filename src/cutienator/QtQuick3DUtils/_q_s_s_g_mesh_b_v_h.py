"""
QSSGMeshBVH binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGMeshBVH to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSSGMeshBVHNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGMeshBVH(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMeshBVH: a plain Python object standing in front
  of one C++ QSSGMeshBVH.

  C++ hands a QSSGMeshBVH around as a copy, so every C++ QSSGMeshBVH behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGMeshBVH that has a ritual and that Python can
  call so far, 2 names in all: 'newHandle', 'value'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMeshBVH::~QSSGMeshBVH()': the destructor: Python removes its
    C++ QSSGMeshBVH by it, and has no other use for it.
  - Qt's 'const QSSGMeshBVHTriangles &QSSGMeshBVH::triangles() const': gives
    a type Python has no way to take yet.
  - Qt's 'const QSSGMeshBVHRoots &QSSGMeshBVH::roots() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGMeshBVHNodes &QSSGMeshBVH::nodes() const': gives a type
    Python has no way to take yet.
  - Qt's 'size_t QSSGMeshBVH::getNodeIndex(size_t idx, FallbackIndex op)
    const': names the enum 'QSSGMeshBVHNode::FallbackIndex', whose class
    cannot be named here.
  - Qt's 'QSSGMeshBVHNode &QSSGMeshBVH::mutableValue(qsizetype idx)': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QSSGMeshBVH is created at the first use, not by
    'QSSGMeshBVH(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMeshBVH back gives a copy the ritual made for
    Python, in a new cute QSSGMeshBVH.
  - Each name of Qt's QSSGMeshBVH that has no cute function yet,
    'getNodeIndex', 'mutableValue', 'nodes', 'roots', 'triangles', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMeshBVH'

  #  Qt's '~QSSGMeshBVH()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGMeshBVH behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QSSGMeshBVHD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def value(self, idx: int) -> QSSGMeshBVHNode:
    """
    Calls Qt's 'const QSSGMeshBVHNode &QSSGMeshBVH::value(qsizetype idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmeshbvh.html#value

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QSSGMeshBVHNode
      A new cute QSSGMeshBVHNode around the copy Qt gave back. Python owns
      it.
    """
    #  const QSSGMeshBVHNode &QSSGMeshBVH::value(qsizetype idx) const
    address = self.uglySide.call('ritual_ZNK11QSSGMeshBVH5valueEx', idx)
    return QSSGMeshBVHNode._cuteOwning(address)

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
    Notes what was given, for Qt's 'QSSGMeshBVH::QSSGMeshBVH()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgmeshbvh.html#QSSGMeshBVH
    """
    #  QSSGMeshBVH::QSSGMeshBVH()
    self._noteCreation(QSSGMeshBVH, lambda: Rituals.call(
        'ritual_ZN11QSSGMeshBVHC1Ev',
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

  def newHandle(self) -> QSSGMeshBVHNode.Handle:
    """
    Calls Qt's 'QSSGMeshBVHNode::Handle QSSGMeshBVH::newHandle()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmeshbvh.html#newHandle

    Returns
    -------

    QSSGMeshBVHNode.Handle
      A new cute QSSGMeshBVHNode::Handle around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGMeshBVHNode::Handle QSSGMeshBVH::newHandle()
    address = self.uglySide.call('ritual_ZN11QSSGMeshBVH9newHandleEv')
    return QSSGMeshBVHNode.Handle._cuteOwning(address)

  @staticmethod
  def getNodeIndex(*__, **_) -> Never:
    """
    Qt's 'size_t QSSGMeshBVH::getNodeIndex(size_t idx, FallbackIndex op)
    const': names the enum 'QSSGMeshBVHNode::FallbackIndex', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMeshBVH.getNodeIndex' has no cute function yet. Qt's 'size_t "
        "QSSGMeshBVH::getNodeIndex(size_t idx, FallbackIndex op) const': "
        "names the enum 'QSSGMeshBVHNode::FallbackIndex', whose class "
        "cannot be named here.")

  @staticmethod
  def mutableValue(*__, **_) -> Never:
    """
    Qt's 'QSSGMeshBVHNode &QSSGMeshBVH::mutableValue(qsizetype idx)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVH.mutableValue' has no cute function yet. Qt's "
        "'QSSGMeshBVHNode &QSSGMeshBVH::mutableValue(qsizetype idx)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def nodes(*__, **_) -> Never:
    """
    Qt's 'const QSSGMeshBVHNodes &QSSGMeshBVH::nodes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVH.nodes' has no cute function yet. Qt's 'const "
        "QSSGMeshBVHNodes &QSSGMeshBVH::nodes() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def roots(*__, **_) -> Never:
    """
    Qt's 'const QSSGMeshBVHRoots &QSSGMeshBVH::roots() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVH.roots' has no cute function yet. Qt's 'const "
        "QSSGMeshBVHRoots &QSSGMeshBVH::roots() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def triangles(*__, **_) -> Never:
    """
    Qt's 'const QSSGMeshBVHTriangles &QSSGMeshBVH::triangles() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVH.triangles' has no cute function yet. Qt's 'const "
        "QSSGMeshBVHTriangles &QSSGMeshBVH::triangles() const': gives a "
        "type Python has no way to take yet.")
