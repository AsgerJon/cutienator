"""
QSSGGlobalRenderNodeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGGlobalRenderNodeData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QThreadPool
  from . import QSSGRenderRoot
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderRoot = WAIT['QSSGRenderRoot']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGGlobalRenderNodeData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGGlobalRenderNodeData: a plain Python object
  standing in front of one C++ QSSGGlobalRenderNodeData.

  What exists
  -----------

  Every function of Qt's QSSGGlobalRenderNodeData that has a ritual and that
  Python can call so far, 10 names in all: 'reindex', 'invalidate',
  'version', 'stateGeneration', 'bumpStateGeneration', 'nodeCount',
  'storageSize', 'threadPool', 'collectNodes', 'updateGlobalState'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGGlobalRenderNodeData::~QSSGGlobalRenderNodeData()': the
    destructor: Python never removes a C++ QSSGGlobalRenderNodeData.
  - Qt's 'QMatrix4x4
    QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h,
    const QMatrix4x4 &defaultValue) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QMatrix4x4
    QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix4x4 QSSGGlobalRenderNodeData::getGlobalTransform(const
    QSSGRenderNode &node) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'float
    QSSGGlobalRenderNodeData::getGlobalOpacity(QSSGRenderNodeHandle h, float
    defaultValue) const': takes a type Python has no way to hand over yet.
  - Qt's 'float QSSGGlobalRenderNodeData::getGlobalOpacity(const
    QSSGRenderNode &node) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'InstanceTransforms
    QSSGGlobalRenderNodeData::getInstanceTransforms(QSSGRenderNodeHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'InstanceTransforms
    QSSGGlobalRenderNodeData::getInstanceTransforms(const QSSGRenderNode
    &node) const': takes a type Python has no way to hand over yet.
  - Qt's 'LayerNodeView
    QSSGGlobalRenderNodeData::getLayerNodeView(QSSGRenderLayerHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'LayerNodeView QSSGGlobalRenderNodeData::getLayerNodeView(const
    QSSGRenderLayer &layer) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSSGGlobalRenderNodeData is created at the first use, not by
    'QSSGGlobalRenderNodeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGGlobalRenderNodeData.
  - Each name of Qt's QSSGGlobalRenderNodeData that has no cute function yet,
    'getGlobalOpacity', 'getGlobalTransform', 'getInstanceTransforms',
    'getLayerNodeView', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QSSGGlobalRenderNodeData, each a class in
  #  here as in C++.

  class InstanceTransforms(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGGlobalRenderNodeData::InstanceTransforms: a
    plain Python object standing in front of one C++
    QSSGGlobalRenderNodeData::InstanceTransforms.

    C++ hands a QSSGGlobalRenderNodeData::InstanceTransforms around as a
    copy, so every C++ QSSGGlobalRenderNodeData::InstanceTransforms behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGGlobalRenderNodeData::InstanceTransforms yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGGlobalRenderNodeData::InstanceTransforms::~InstanceTransforms()':
      the destructor: Python removes its C++
      QSSGGlobalRenderNodeData::InstanceTransforms by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QSSGGlobalRenderNodeData::InstanceTransforms is created at the
      first use, not by 'QSSGGlobalRenderNodeData::InstanceTransforms(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGGlobalRenderNodeData::InstanceTransforms back
      gives a copy the ritual made for Python, in a new cute
      QSSGGlobalRenderNodeData::InstanceTransforms.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGGlobalRenderNodeData::InstanceTransforms'

    #  Qt's '~QSSGGlobalRenderNodeData::InstanceTransforms()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QSSGGlobalRenderNodeData::InstanceTransforms behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QSSGGlobalRenderNodeData18InstanceTransformsD1Ev')

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

  class LayerNodeSection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGGlobalRenderNodeData::LayerNodeSection: a plain
    Python object standing in front of one C++
    QSSGGlobalRenderNodeData::LayerNodeSection.

    C++ hands a QSSGGlobalRenderNodeData::LayerNodeSection around as a copy,
    so every C++ QSSGGlobalRenderNodeData::LayerNodeSection behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGGlobalRenderNodeData::LayerNodeSection yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGGlobalRenderNodeData::LayerNodeSection::~LayerNodeSection()':
      the destructor: Python removes its C++
      QSSGGlobalRenderNodeData::LayerNodeSection by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGGlobalRenderNodeData::LayerNodeSection is created at the
      first use, not by 'QSSGGlobalRenderNodeData::LayerNodeSection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGGlobalRenderNodeData::LayerNodeSection back
      gives a copy the ritual made for Python, in a new cute
      QSSGGlobalRenderNodeData::LayerNodeSection.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGGlobalRenderNodeData::LayerNodeSection'

    #  Qt's '~QSSGGlobalRenderNodeData::LayerNodeSection()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGGlobalRenderNodeData::LayerNodeSection behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QSSGGlobalRenderNodeData16LayerNodeSectionD1Ev')

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
  __qt_class__ = 'QSSGGlobalRenderNodeData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def version(self) -> int:
    """
    Calls Qt's 'VersionType QSSGGlobalRenderNodeData::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#version
    """
    #  VersionType QSSGGlobalRenderNodeData::version() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGGlobalRenderNodeData7versionEv',
    )

  def stateGeneration(self) -> int:
    """
    Calls Qt's 'VersionType QSSGGlobalRenderNodeData::stateGeneration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#stateGeneration
    """
    #  VersionType QSSGGlobalRenderNodeData::stateGeneration() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGGlobalRenderNodeData15stateGenerationEv',
    )

  def nodeCount(self) -> int:
    """
    Calls Qt's 'size_t QSSGGlobalRenderNodeData::nodeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#nodeCount
    """
    #  size_t QSSGGlobalRenderNodeData::nodeCount() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGGlobalRenderNodeData9nodeCountEv',
    )

  def storageSize(self) -> int:
    """
    Calls Qt's 'size_t QSSGGlobalRenderNodeData::storageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#storageSize
    """
    #  size_t QSSGGlobalRenderNodeData::storageSize() const
    return self.uglySide.call(
        'ritual_ZNK24QSSGGlobalRenderNodeData11storageSizeEv',
    )

  def threadPool(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QSSGGlobalRenderNodeData::threadPool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#threadPool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QSSGGlobalRenderNodeData::threadPool() const
    address = self.uglySide.call(
        'ritual_ZNK24QSSGGlobalRenderNodeData10threadPoolEv',
    )
    from ..QtCore import QThreadPool
    return QThreadPool._cuteAt(address)

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

  @overload(QSSGRenderRoot)
  @overload(NoneType)
  def __init__(self, root: Optional[QSSGRenderRoot]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGGlobalRenderNodeData::QSSGGlobalRenderNodeData(QSSGRenderRoot
    *root)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html

    Parameters
    ----------

    root : Optional[QSSGRenderRoot]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSSGGlobalRenderNodeData::QSSGGlobalRenderNodeData(QSSGRenderRoot
    #      *root)
    self._noteCreation(QSSGGlobalRenderNodeData, lambda: Rituals.call(
        'ritual_ZN24QSSGGlobalRenderNodeDataC1EP14QSSGRenderRoot',
        self._addressOf(root),
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

  def reindex(self) -> None:
    """
    Calls Qt's 'void QSSGGlobalRenderNodeData::reindex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#reindex
    """
    #  void QSSGGlobalRenderNodeData::reindex()
    self.uglySide.call('ritual_ZN24QSSGGlobalRenderNodeData7reindexEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSSGGlobalRenderNodeData::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#invalidate
    """
    #  void QSSGGlobalRenderNodeData::invalidate()
    self.uglySide.call('ritual_ZN24QSSGGlobalRenderNodeData10invalidateEv')

  def bumpStateGeneration(self) -> None:
    """
    Calls Qt's 'void QSSGGlobalRenderNodeData::bumpStateGeneration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#bumpStateGeneration
    """
    #  void QSSGGlobalRenderNodeData::bumpStateGeneration()
    self.uglySide.call(
        'ritual_ZN24QSSGGlobalRenderNodeData19bumpStateGenerationEv',
    )

  @overload(QSSGRenderRoot)
  @overload(NoneType)
  def collectNodes(self, rootNode: Optional[QSSGRenderRoot]) -> None:
    """
    Calls Qt's 'void QSSGGlobalRenderNodeData::collectNodes(QSSGRenderRoot
    *rootNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#collectNodes

    Parameters
    ----------

    rootNode : Optional[QSSGRenderRoot]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGGlobalRenderNodeData::collectNodes(QSSGRenderRoot *rootNode)
    self.uglySide.call(
        'ritual_ZN24QSSGGlobalRenderNodeData12collectNodesEP14QSSGRenderRoo'
        't',
        self._addressOf(rootNode),
    )

  def updateGlobalState(self) -> None:
    """
    Calls Qt's 'void QSSGGlobalRenderNodeData::updateGlobalState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgglobalrendernodedata.html#updateGlobalState
    """
    #  void QSSGGlobalRenderNodeData::updateGlobalState()
    self.uglySide.call(
        'ritual_ZN24QSSGGlobalRenderNodeData17updateGlobalStateEv',
    )

  @staticmethod
  def getGlobalOpacity(*__, **_) -> Never:
    """
    - Qt's 'float
      QSSGGlobalRenderNodeData::getGlobalOpacity(QSSGRenderNodeHandle h,
      float defaultValue) const': takes a type Python has no way to hand over
      yet.
    - Qt's 'float QSSGGlobalRenderNodeData::getGlobalOpacity(const
      QSSGRenderNode &node) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGGlobalRenderNodeData.getGlobalOpacity' has no cute function "
        "yet. Qt's 'float "
        "QSSGGlobalRenderNodeData::getGlobalOpacity(QSSGRenderNodeHandle h, "
        "float defaultValue) const': takes a type Python has no way to hand "
        "over yet. Qt's 'float "
        "QSSGGlobalRenderNodeData::getGlobalOpacity(const QSSGRenderNode "
        "&node) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getGlobalTransform(*__, **_) -> Never:
    """
    - Qt's 'QMatrix4x4
      QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h,
      const QMatrix4x4 &defaultValue) const': takes a type Python has no way
      to hand over yet.
    - Qt's 'QMatrix4x4
      QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'QMatrix4x4 QSSGGlobalRenderNodeData::getGlobalTransform(const
      QSSGRenderNode &node) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGGlobalRenderNodeData.getGlobalTransform' has no cute function "
        "yet. Qt's 'QMatrix4x4 "
        "QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle "
        "h, const QMatrix4x4 &defaultValue) const': takes a type Python has "
        "no way to hand over yet. Qt's 'QMatrix4x4 "
        "QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle "
        "h) const': takes a type Python has no way to hand over yet. Qt's "
        "'QMatrix4x4 QSSGGlobalRenderNodeData::getGlobalTransform(const "
        "QSSGRenderNode &node) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getInstanceTransforms(*__, **_) -> Never:
    """
    - Qt's 'InstanceTransforms
      QSSGGlobalRenderNodeData::getInstanceTransforms(QSSGRenderNodeHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'InstanceTransforms
      QSSGGlobalRenderNodeData::getInstanceTransforms(const QSSGRenderNode
      &node) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGGlobalRenderNodeData.getInstanceTransforms' has no cute "
        "function yet. Qt's 'InstanceTransforms "
        "QSSGGlobalRenderNodeData::getInstanceTransforms(QSSGRenderNodeHandl"
        "e h) const': takes a type Python has no way to hand over yet. Qt's "
        "'InstanceTransforms "
        "QSSGGlobalRenderNodeData::getInstanceTransforms(const "
        "QSSGRenderNode &node) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getLayerNodeView(*__, **_) -> Never:
    """
    - Qt's 'LayerNodeView
      QSSGGlobalRenderNodeData::getLayerNodeView(QSSGRenderLayerHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'LayerNodeView QSSGGlobalRenderNodeData::getLayerNodeView(const
      QSSGRenderLayer &layer) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGGlobalRenderNodeData.getLayerNodeView' has no cute function "
        "yet. Qt's 'LayerNodeView "
        "QSSGGlobalRenderNodeData::getLayerNodeView(QSSGRenderLayerHandle "
        "h) const': takes a type Python has no way to hand over yet. Qt's "
        "'LayerNodeView QSSGGlobalRenderNodeData::getLayerNodeView(const "
        "QSSGRenderLayer &layer) const': takes a type Python has no way to "
        "hand over yet.")
