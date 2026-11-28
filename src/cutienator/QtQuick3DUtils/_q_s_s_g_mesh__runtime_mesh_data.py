"""
QSSGMesh::RuntimeMeshData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGMesh::RuntimeMeshData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class RuntimeMeshData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMesh::RuntimeMeshData: a plain Python object
  standing in front of one C++ QSSGMesh::RuntimeMeshData.

  C++ hands a QSSGMesh::RuntimeMeshData around as a copy, so every C++
  QSSGMesh::RuntimeMeshData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGMesh::RuntimeMeshData that has a ritual and that
  Python can call so far, 3 names in all: 'clear', 'clearVertexAndIndex',
  'clearTarget'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMesh::RuntimeMeshData::~RuntimeMeshData()': the destructor:
    Python removes its C++ QSSGMesh::RuntimeMeshData by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QSSGMesh::RuntimeMeshData is created at the first use, not by
    'QSSGMesh::RuntimeMeshData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMesh::RuntimeMeshData back gives a copy the
    ritual made for Python, in a new cute QSSGMesh::RuntimeMeshData.
  """

  #  The classes Qt writes inside QSSGMesh::RuntimeMeshData, each a class in
  #  here as in C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::RuntimeMeshData::Attribute: a plain
    Python object standing in front of one C++
    QSSGMesh::RuntimeMeshData::Attribute.

    C++ hands a QSSGMesh::RuntimeMeshData::Attribute around as a copy, so
    every C++ QSSGMesh::RuntimeMeshData::Attribute behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGMesh::RuntimeMeshData::Attribute that has a
    ritual and that Python can call so far, 1 name in all: 'componentCount'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::RuntimeMeshData::Attribute::~Attribute()': the
      destructor: Python removes its C++ QSSGMesh::RuntimeMeshData::Attribute
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGMesh::RuntimeMeshData::Attribute is created at the first
      use, not by 'QSSGMesh::RuntimeMeshData::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::RuntimeMeshData::Attribute back gives a
      copy the ritual made for Python, in a new cute
      QSSGMesh::RuntimeMeshData::Attribute.
    """

    #  The enums Qt writes inside QSSGMesh::RuntimeMeshData::Attribute, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Semantic(CuteNum):
      """
      The enum 'QSSGMesh::RuntimeMeshData::Attribute::Semantic' of Qt, with
      the 11 names Qt gives in it.
      """

      IndexSemantic = Kee[int](0)
      PositionSemantic = Kee[int](1)
      NormalSemantic = Kee[int](2)
      TexCoordSemantic = Kee[int](3)
      TangentSemantic = Kee[int](4)
      BinormalSemantic = Kee[int](5)
      JointSemantic = Kee[int](6)
      WeightSemantic = Kee[int](7)
      ColorSemantic = Kee[int](8)
      TexCoord1Semantic = Kee[int](9)
      TexCoord0Semantic = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::RuntimeMeshData::Attribute'

    #  Qt's '~QSSGMesh::RuntimeMeshData::Attribute()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QSSGMesh::RuntimeMeshData::Attribute behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN8QSSGMesh15RuntimeMeshData9AttributeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def componentCount(self) -> int:
      """
      Calls Qt's 'int QSSGMesh::RuntimeMeshData::Attribute::componentCount()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmesh-runtimemeshdata-attribute.html
      """
      #  int QSSGMesh::RuntimeMeshData::Attribute::componentCount() const
      return self.uglySide.call(
          'ritual_ZNK8QSSGMesh15RuntimeMeshData9Attribute14componentCountEv',
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

  class TargetAttribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMesh::RuntimeMeshData::TargetAttribute: a plain
    Python object standing in front of one C++
    QSSGMesh::RuntimeMeshData::TargetAttribute.

    C++ hands a QSSGMesh::RuntimeMeshData::TargetAttribute around as a copy,
    so every C++ QSSGMesh::RuntimeMeshData::TargetAttribute behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGMesh::RuntimeMeshData::TargetAttribute yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGMesh::RuntimeMeshData::TargetAttribute::~TargetAttribute()':
      the destructor: Python removes its C++
      QSSGMesh::RuntimeMeshData::TargetAttribute by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGMesh::RuntimeMeshData::TargetAttribute is created at the
      first use, not by 'QSSGMesh::RuntimeMeshData::TargetAttribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMesh::RuntimeMeshData::TargetAttribute back
      gives a copy the ritual made for Python, in a new cute
      QSSGMesh::RuntimeMeshData::TargetAttribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMesh::RuntimeMeshData::TargetAttribute'

    #  Qt's '~QSSGMesh::RuntimeMeshData::TargetAttribute()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGMesh::RuntimeMeshData::TargetAttribute behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN8QSSGMesh15RuntimeMeshData15TargetAttributeD1Ev')

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
  __qt_class__ = 'QSSGMesh::RuntimeMeshData'

  #  Qt's '~QSSGMesh::RuntimeMeshData()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGMesh::RuntimeMeshData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QSSGMesh15RuntimeMeshDataD1Ev'

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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSSGMesh::RuntimeMeshData::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-runtimemeshdata.html#clear
    """
    #  void QSSGMesh::RuntimeMeshData::clear()
    self.uglySide.call('ritual_ZN8QSSGMesh15RuntimeMeshData5clearEv')

  def clearVertexAndIndex(self) -> None:
    """
    Calls Qt's 'void QSSGMesh::RuntimeMeshData::clearVertexAndIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-runtimemeshdata.html#clearVertexAndIndex
    """
    #  void QSSGMesh::RuntimeMeshData::clearVertexAndIndex()
    self.uglySide.call(
        'ritual_ZN8QSSGMesh15RuntimeMeshData19clearVertexAndIndexEv',
    )

  def clearTarget(self) -> None:
    """
    Calls Qt's 'void QSSGMesh::RuntimeMeshData::clearTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmesh-runtimemeshdata.html#clearTarget
    """
    #  void QSSGMesh::RuntimeMeshData::clearTarget()
    self.uglySide.call('ritual_ZN8QSSGMesh15RuntimeMeshData11clearTargetEv')
