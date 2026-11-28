"""
QSSGMesh::MeshInternal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGMesh::MeshInternal to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MeshInternal(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMesh::MeshInternal: a plain Python object
  standing in front of one C++ QSSGMesh::MeshInternal.

  C++ hands a QSSGMesh::MeshInternal around as a copy, so every C++
  QSSGMesh::MeshInternal behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGMesh::MeshInternal that has a ritual and that
  Python can call so far, 15 names in all: 'readFileHeader',
  'writeFileHeader', 'readMeshData', 'writeMeshHeader', 'writeMeshData',
  'getPositionAttrName', 'getNormalAttrName', 'getUV0AttrName',
  'getUV1AttrName', 'getLightmapUVAttrName', 'getTexTanAttrName',
  'getTexBinormalAttrName', 'getColorAttrName', 'getJointAttrName',
  'getWeightAttrName'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'quint32
    QSSGMesh::MeshInternal::byteSizeForComponentType(Mesh::ComponentType
    componentType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
  - Qt's 'QSSGBounds3 QSSGMesh::MeshInternal::calculateSubsetBounds(const
    Mesh::VertexBufferEntry &entry, const QByteArray &vertexBufferData,
    quint32 vertexBufferStride, const QByteArray &indexBufferData,
    Mesh::ComponentType indexComponentType, quint32 subsetCount, quint32
    subsetOffset)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
  - Qt's 'QSSGMesh::MeshInternal::~MeshInternal()': the destructor: Python
    removes its C++ QSSGMesh::MeshInternal by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QSSGMesh::MeshInternal is created at the first use, not by
    'QSSGMesh::MeshInternal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMesh::MeshInternal back gives a copy the ritual
    made for Python, in a new cute QSSGMesh::MeshInternal.
  - Each name of Qt's QSSGMesh::MeshInternal that has no cute function yet,
    'byteSizeForComponentType', 'calculateSubsetBounds', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGMesh::MeshInternal, each a class in
  #  here as in C++.

  class MeshDataHeader(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::MeshInternal::MeshDataHeader: a plain
    Python object standing in front of one C++
    QSSGMesh::MeshInternal::MeshDataHeader.

    C++ hands a QSSGMesh::MeshInternal::MeshDataHeader around as a copy, so
    every C++ QSSGMesh::MeshInternal::MeshDataHeader behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::MeshInternal::MeshDataHeader that has a
    ritual and that Python can call so far, 5 names in all: 'withDefaults',
    'isValid', 'hasLightmapSizeHint', 'hasLodDataHint',
    'hasSeparateTargetBuffer'. None can be made from Python: one comes out of
    a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::MeshInternal::MeshDataHeader::~MeshDataHeader()': the
      destructor: Python removes its C++
      QSSGMesh::MeshInternal::MeshDataHeader by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGMesh::MeshInternal::MeshDataHeader is created at the first
      use, not by 'QSSGMesh::MeshInternal::MeshDataHeader(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::MeshInternal::MeshDataHeader back gives a
      copy the ritual made for Python, in a new cute
      QSSGMesh::MeshInternal::MeshDataHeader.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def withDefaults() -> MeshInternal.MeshDataHeader:
      """
      Calls Qt's 'MeshDataHeader
      QSSGMesh::MeshInternal::MeshDataHeader::withDefaults()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshdataheader.html

      Returns
      -------

      MeshInternal.MeshDataHeader
        A new cute QSSGMesh::MeshInternal::MeshDataHeader around the copy Qt
        gave back. Python owns it.
      """
      #  MeshDataHeader
      #      QSSGMesh::MeshInternal::MeshDataHeader::withDefaults()
      address = Rituals.call(
          'ritual_ZN8QSSGMesh12MeshInternal14MeshDataHeader12withDefaultsEv',
      )
      return MeshInternal.MeshDataHeader._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::MeshInternal::MeshDataHeader'

    #  Qt's '~QSSGMesh::MeshInternal::MeshDataHeader()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGMesh::MeshInternal::MeshDataHeader behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN8QSSGMesh12MeshInternal14MeshDataHeaderD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QSSGMesh::MeshInternal::MeshDataHeader::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshdataheader.html
      """
      #  bool QSSGMesh::MeshInternal::MeshDataHeader::isValid() const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader7isValidEv',
      )

    def hasLightmapSizeHint(self) -> bool:
      """
      Calls Qt's 'bool
      QSSGMesh::MeshInternal::MeshDataHeader::hasLightmapSizeHint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshdataheader.html
      """
      #  bool QSSGMesh::MeshInternal::MeshDataHeader::hasLightmapSizeHint()
      #      const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader19hasLightmapSi'
          'zeHintEv',
      )

    def hasLodDataHint(self) -> bool:
      """
      Calls Qt's 'bool
      QSSGMesh::MeshInternal::MeshDataHeader::hasLodDataHint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshdataheader.html
      """
      #  bool QSSGMesh::MeshInternal::MeshDataHeader::hasLodDataHint() const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader14hasLodDataHin'
          'tEv',
      )

    def hasSeparateTargetBuffer(self) -> bool:
      """
      Calls Qt's 'bool
      QSSGMesh::MeshInternal::MeshDataHeader::hasSeparateTargetBuffer()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshdataheader.html
      """
      #  bool
      #      QSSGMesh::MeshInternal::MeshDataHeader::hasSeparateTargetBuffer(
      #      ) const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal14MeshDataHeader23hasSeparateTa'
          'rgetBufferEv',
      )

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

  class MeshOffsetTracker(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::MeshInternal::MeshOffsetTracker: a plain
    Python object standing in front of one C++
    QSSGMesh::MeshInternal::MeshOffsetTracker.

    C++ hands a QSSGMesh::MeshInternal::MeshOffsetTracker around as a copy,
    so every C++ QSSGMesh::MeshInternal::MeshOffsetTracker behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::MeshInternal::MeshOffsetTracker that has
    a ritual and that Python can call so far, 3 names in all: 'offset',
    'alignedAdvance', 'advance'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::MeshInternal::MeshOffsetTracker::~MeshOffsetTracker()':
      the destructor: Python removes its C++
      QSSGMesh::MeshInternal::MeshOffsetTracker by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGMesh::MeshInternal::MeshOffsetTracker is created at the
      first use, not by 'QSSGMesh::MeshInternal::MeshOffsetTracker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::MeshInternal::MeshOffsetTracker back
      gives a copy the ritual made for Python, in a new cute
      QSSGMesh::MeshInternal::MeshOffsetTracker.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::MeshInternal::MeshOffsetTracker'

    #  Qt's '~QSSGMesh::MeshInternal::MeshOffsetTracker()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGMesh::MeshInternal::MeshOffsetTracker behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTrackerD1Ev')

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

    @overload(int)
    def __init__(self, offset: int) -> None:
      """
      Notes what was given, for Qt's
      'QSSGMesh::MeshInternal::MeshOffsetTracker::MeshOffsetTracker(int
      offset)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshoffsettracker.html

      Parameters
      ----------

      offset : int
        Passed on as it is.
      """
      #  QSSGMesh::MeshInternal::MeshOffsetTracker::MeshOffsetTracker(int
      #      offset)
      self._noteCreation(
          MeshInternal.MeshOffsetTracker, lambda: Rituals.call(
              'ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTrackerC1Ei',
              offset,
          ))

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

    def offset(self) -> int:
      """
      Calls Qt's 'int QSSGMesh::MeshInternal::MeshOffsetTracker::offset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshoffsettracker.html
      """
      #  int QSSGMesh::MeshInternal::MeshOffsetTracker::offset()
      return self.uglySide.call(
          'ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker6offsetEv',
      )

    @overload(int)
    def alignedAdvance(self, advanceAmount: int) -> int:
      """
      Calls Qt's 'quint32
      QSSGMesh::MeshInternal::MeshOffsetTracker::alignedAdvance(int
      advanceAmount)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshoffsettracker.html

      Parameters
      ----------

      advanceAmount : int
        Passed on as it is.
      """
      #  quint32
      #      QSSGMesh::MeshInternal::MeshOffsetTracker::alignedAdvance(int
      #      advanceAmount)
      return self.uglySide.call(
          'ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker14alignedAdva'
          'nceEi',
          advanceAmount,
      )

    @overload(int)
    def advance(self, advanceAmount: int) -> None:
      """
      Calls Qt's 'void QSSGMesh::MeshInternal::MeshOffsetTracker::advance(int
      advanceAmount)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-meshoffsettracker.html

      Parameters
      ----------

      advanceAmount : int
        Passed on as it is.
      """
      #  void QSSGMesh::MeshInternal::MeshOffsetTracker::advance(int
      #      advanceAmount)
      self.uglySide.call(
          'ritual_ZN8QSSGMesh12MeshInternal17MeshOffsetTracker7advanceEi',
          advanceAmount,
      )

  class MultiMeshInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::MeshInternal::MultiMeshInfo: a plain
    Python object standing in front of one C++
    QSSGMesh::MeshInternal::MultiMeshInfo.

    C++ hands a QSSGMesh::MeshInternal::MultiMeshInfo around as a copy, so
    every C++ QSSGMesh::MeshInternal::MultiMeshInfo behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::MeshInternal::MultiMeshInfo that has a
    ritual and that Python can call so far, 2 names in all: 'isValid',
    'withDefaults'. None can be made from Python: one comes out of a function
    of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::MeshInternal::MultiMeshInfo::~MultiMeshInfo()': the
      destructor: Python removes its C++
      QSSGMesh::MeshInternal::MultiMeshInfo by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGMesh::MeshInternal::MultiMeshInfo is created at the first
      use, not by 'QSSGMesh::MeshInternal::MultiMeshInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::MeshInternal::MultiMeshInfo back gives a
      copy the ritual made for Python, in a new cute
      QSSGMesh::MeshInternal::MultiMeshInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def withDefaults() -> MeshInternal.MultiMeshInfo:
      """
      Calls Qt's 'MultiMeshInfo
      QSSGMesh::MeshInternal::MultiMeshInfo::withDefaults()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-multimeshinfo.html

      Returns
      -------

      MeshInternal.MultiMeshInfo
        A new cute QSSGMesh::MeshInternal::MultiMeshInfo around the copy Qt
        gave back. Python owns it.
      """
      #  MultiMeshInfo QSSGMesh::MeshInternal::MultiMeshInfo::withDefaults()
      address = Rituals.call(
          'ritual_ZN8QSSGMesh12MeshInternal13MultiMeshInfo12withDefaultsEv',
      )
      return MeshInternal.MultiMeshInfo._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::MeshInternal::MultiMeshInfo'

    #  Qt's '~QSSGMesh::MeshInternal::MultiMeshInfo()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGMesh::MeshInternal::MultiMeshInfo behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh12MeshInternal13MultiMeshInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QSSGMesh::MeshInternal::MultiMeshInfo::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-multimeshinfo.html#isValid
      """
      #  bool QSSGMesh::MeshInternal::MultiMeshInfo::isValid() const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal13MultiMeshInfo7isValidEv',
      )

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

  class Subset(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::MeshInternal::Subset: a plain Python
    object standing in front of one C++ QSSGMesh::MeshInternal::Subset.

    C++ hands a QSSGMesh::MeshInternal::Subset around as a copy, so every C++
    QSSGMesh::MeshInternal::Subset behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::MeshInternal::Subset that has a ritual
    and that Python can call so far, 1 name in all: 'toMeshSubset'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::MeshInternal::Subset::~Subset()': the destructor:
      Python removes its C++ QSSGMesh::MeshInternal::Subset by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::MeshInternal::Subset is created at the first use, not
      by 'QSSGMesh::MeshInternal::Subset(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::MeshInternal::Subset back gives a copy
      the ritual made for Python, in a new cute
      QSSGMesh::MeshInternal::Subset.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::MeshInternal::Subset'

    #  Qt's '~QSSGMesh::MeshInternal::Subset()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGMesh::MeshInternal::Subset behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh12MeshInternal6SubsetD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def toMeshSubset(self) -> QSSGMesh.Mesh.Subset:
      """
      Calls Qt's 'Mesh::Subset QSSGMesh::MeshInternal::Subset::toMeshSubset()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-meshinternal-subset.html#toMeshSubset

      Returns
      -------

      QSSGMesh.Mesh.Subset
        A new cute QSSGMesh::Mesh::Subset around the copy Qt gave back.
        Python owns it.
      """
      #  Mesh::Subset QSSGMesh::MeshInternal::Subset::toMeshSubset() const
      address = self.uglySide.call(
          'ritual_ZNK8QSSGMesh12MeshInternal6Subset12toMeshSubsetEv',
      )
      return QSSGMesh.Mesh.Subset._cuteOwning(address)

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
  @overload(QIODevice)
  @overload(NoneType)
  def readFileHeader(device: Optional[QIODevice]) -> MultiMeshInfo:
    """
    Calls Qt's 'MultiMeshInfo
    QSSGMesh::MeshInternal::readFileHeader(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#readFileHeader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    MultiMeshInfo
      A new cute QSSGMesh::MeshInternal::MultiMeshInfo around the copy Qt
      gave back. Python owns it.
    """
    #  MultiMeshInfo QSSGMesh::MeshInternal::readFileHeader(QIODevice
    #      *device)
    address = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal14readFileHeaderEP9QIODevice',
        CuteMixin._addressOf(device),
    )
    return QSSGMesh.MeshInternal.MultiMeshInfo._cuteOwning(address)

  @staticmethod
  @overload(QIODevice, MultiMeshInfo)
  @overload(NoneType, MultiMeshInfo)
  def writeFileHeader(
      device: Optional[QIODevice],
      meshFileInfo: MultiMeshInfo,
  ) -> None:
    """
    Calls Qt's 'void QSSGMesh::MeshInternal::writeFileHeader(QIODevice
    *device, const MultiMeshInfo &meshFileInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#writeFileHeader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    meshFileInfo : MultiMeshInfo
      Passed on as a value: Qt reads the C++
      QSSGMesh::MeshInternal::MultiMeshInfo, which stays Python's own.
    """
    #  void QSSGMesh::MeshInternal::writeFileHeader(QIODevice *device, const
    #      MultiMeshInfo &meshFileInfo)
    Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal15writeFileHeaderEP9QIODeviceRKNS0'
        '_13MultiMeshInfoE',
        CuteMixin._addressOf(device), CuteMixin._valueOf(meshFileInfo),
    )

  @staticmethod
  @overload(QIODevice, int, WAIT['QSSGMesh.Mesh'], MeshDataHeader)
  @overload(QIODevice, int, WAIT['QSSGMesh.Mesh'], NoneType)
  @overload(QIODevice, int, NoneType, MeshDataHeader)
  @overload(QIODevice, int, NoneType, NoneType)
  @overload(NoneType, int, WAIT['QSSGMesh.Mesh'], MeshDataHeader)
  @overload(NoneType, int, WAIT['QSSGMesh.Mesh'], NoneType)
  @overload(NoneType, int, NoneType, MeshDataHeader)
  @overload(NoneType, int, NoneType, NoneType)
  def readMeshData(
      device: Optional[QIODevice],
      offset: int,
      mesh: Optional[QSSGMesh.Mesh],
      header: Optional[MeshDataHeader],
  ) -> int:
    """
    Calls Qt's 'quint64 QSSGMesh::MeshInternal::readMeshData(QIODevice
    *device, quint64 offset, Mesh *mesh, MeshDataHeader *header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#readMeshData

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : int
      Passed on as it is.

    mesh : Optional[QSSGMesh.Mesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    header : Optional[MeshDataHeader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quint64 QSSGMesh::MeshInternal::readMeshData(QIODevice *device,
    #      quint64 offset, Mesh *mesh, MeshDataHeader *header)
    return Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal12readMeshDataEP9QIODeviceyPNS_4Me'
        'shEPNS0_14MeshDataHeaderE',
        CuteMixin._addressOf(device), offset, CuteMixin._addressOf(mesh),
        CuteMixin._addressOf(header),
    )

  @staticmethod
  @overload(QIODevice, MeshDataHeader)
  @overload(NoneType, MeshDataHeader)
  def writeMeshHeader(
      device: Optional[QIODevice],
      header: MeshDataHeader,
  ) -> None:
    """
    Calls Qt's 'void QSSGMesh::MeshInternal::writeMeshHeader(QIODevice
    *device, const MeshDataHeader &header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#writeMeshHeader

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    header : MeshDataHeader
      Passed on as a value: Qt reads the C++
      QSSGMesh::MeshInternal::MeshDataHeader, which stays Python's own.
    """
    #  void QSSGMesh::MeshInternal::writeMeshHeader(QIODevice *device, const
    #      MeshDataHeader &header)
    Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal15writeMeshHeaderEP9QIODeviceRKNS0'
        '_14MeshDataHeaderE',
        CuteMixin._addressOf(device), CuteMixin._valueOf(header),
    )

  @staticmethod
  @overload(QIODevice, WAIT['QSSGMesh.Mesh'])
  @overload(NoneType, WAIT['QSSGMesh.Mesh'])
  def writeMeshData(device: Optional[QIODevice], mesh: QSSGMesh.Mesh) -> int:
    """
    Calls Qt's 'quint64 QSSGMesh::MeshInternal::writeMeshData(QIODevice
    *device, const Mesh &mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#writeMeshData

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mesh : QSSGMesh.Mesh
      Passed on as a value: Qt reads the C++ QSSGMesh::Mesh, which stays
      Python's own.
    """
    #  quint64 QSSGMesh::MeshInternal::writeMeshData(QIODevice *device, const
    #      Mesh &mesh)
    return Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal13writeMeshDataEP9QIODeviceRKNS_4M'
        'eshE',
        CuteMixin._addressOf(device), CuteMixin._valueOf(mesh),
    )

  @staticmethod
  def getPositionAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getPositionAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getPositionAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getPositionAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal19getPositionAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getNormalAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getNormalAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getNormalAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getNormalAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal17getNormalAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getUV0AttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getUV0AttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getUV0AttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getUV0AttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal14getUV0AttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getUV1AttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getUV1AttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getUV1AttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getUV1AttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal14getUV1AttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getLightmapUVAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getLightmapUVAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getLightmapUVAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getLightmapUVAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal21getLightmapUVAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getTexTanAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getTexTanAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getTexTanAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getTexTanAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal17getTexTanAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getTexBinormalAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMesh::MeshInternal::getTexBinormalAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getTexBinormalAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getTexBinormalAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal22getTexBinormalAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getColorAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getColorAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getColorAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getColorAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal16getColorAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getJointAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getJointAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getJointAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getJointAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal16getJointAttrNameEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def getWeightAttrName() -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGMesh::MeshInternal::getWeightAttrName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-meshinternal.html#getWeightAttrName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMesh::MeshInternal::getWeightAttrName()
    chars = Rituals.call(
        'ritual_ZN8QSSGMesh12MeshInternal17getWeightAttrNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMesh::MeshInternal'

  #  Qt's '~QSSGMesh::MeshInternal()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGMesh::MeshInternal behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QSSGMesh12MeshInternalD1Ev'

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
  def byteSizeForComponentType(*__, **_) -> Never:
    """
    Qt's 'quint32
    QSSGMesh::MeshInternal::byteSizeForComponentType(Mesh::ComponentType
    componentType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMesh.MeshInternal.byteSizeForComponentType' has no cute "
        "function yet. Qt's 'quint32 "
        "QSSGMesh::MeshInternal::byteSizeForComponentType(Mesh::ComponentTyp"
        "e componentType)': names the enum 'QSSGRenderComponentType', whose "
        "class cannot be named here.")

  @staticmethod
  def calculateSubsetBounds(*__, **_) -> Never:
    """
    Qt's 'QSSGBounds3 QSSGMesh::MeshInternal::calculateSubsetBounds(const
    Mesh::VertexBufferEntry &entry, const QByteArray &vertexBufferData,
    quint32 vertexBufferStride, const QByteArray &indexBufferData,
    Mesh::ComponentType indexComponentType, quint32 subsetCount, quint32
    subsetOffset)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMesh.MeshInternal.calculateSubsetBounds' has no cute function "
        "yet. Qt's 'QSSGBounds3 "
        "QSSGMesh::MeshInternal::calculateSubsetBounds(const "
        "Mesh::VertexBufferEntry &entry, const QByteArray "
        "&vertexBufferData, quint32 vertexBufferStride, const QByteArray "
        "&indexBufferData, Mesh::ComponentType indexComponentType, quint32 "
        "subsetCount, quint32 subsetOffset)': names the enum "
        "'QSSGRenderComponentType', whose class cannot be named here.")
