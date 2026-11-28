"""
QQuick3DGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/qquick3dgeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtGui import QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DGeometryPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DGeometry(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DGeometry: a plain Python object standing in
  front of one C++ QQuick3DGeometry.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DGeometry is built
  on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DGeometry that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'd_func',
  'vertexData', 'indexData', 'attributeCount', 'attribute', 'primitiveType',
  'boundsMin', 'boundsMax', 'stride', 'setVertexData', 'setIndexData',
  'setStride', 'setBounds', 'setPrimitiveType', 'addAttribute',
  'subsetCount', 'subsetBoundsMin', 'subsetBoundsMax', 'subsetOffset',
  'subsetName', 'addSubset', 'targetData', 'setTargetData',
  'targetAttribute', 'targetAttributeCount', 'addTargetAttribute', 'clear',
  'geometryNodeDirty', 'geometryChanged', 'updateSpatialNode',
  'markAllDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DGeometry::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DGeometry::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DGeometryPrivate *QQuick3DGeometry::d_func() const':
    takes in Python what 'QQuick3DGeometryPrivate
    *QQuick3DGeometry::d_func()' takes.
  - Qt's 'void QQuick3DGeometry::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuick3DGeometry::~QQuick3DGeometry()': the destructor: Python
    never removes a C++ QQuick3DGeometry.
  - Qt's 'void QQuick3DGeometry::addAttribute(Attribute::Semantic semantic,
    int offset, Attribute::ComponentType componentType)': names the enum
    'QQuick3DGeometry::Attribute::Semantic', whose class cannot be named
    here.
  - Qt's 'void QQuick3DGeometry::addTargetAttribute(quint32 targetId,
    Attribute::Semantic semantic, int offset, int stride)': names the enum
    'QQuick3DGeometry::Attribute::Semantic', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 47 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DGeometry is created at the first use, not by
    'QQuick3DGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DGeometry.
  - Qt tells when it has removed the C++ QQuick3DGeometry. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DGeometry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PrimitiveType(CuteNum, scoped=True):
    """
    The enum 'QQuick3DGeometry::PrimitiveType' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Points = Kee[int](0)
    LineStrip = Kee[int](1)
    Lines = Kee[int](2)
    TriangleStrip = Kee[int](3)
    TriangleFan = Kee[int](4)
    Triangles = Kee[int](5)

  #  The classes Qt writes inside QQuick3DGeometry, each a class in here as
  #  in C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DGeometry::Attribute: a plain Python object
    standing in front of one C++ QQuick3DGeometry::Attribute.

    C++ hands a QQuick3DGeometry::Attribute around as a copy, so every C++
    QQuick3DGeometry::Attribute behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuick3DGeometry::Attribute yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DGeometry::Attribute::~Attribute()': the destructor:
      Python removes its C++ QQuick3DGeometry::Attribute by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuick3DGeometry::Attribute is created at the first use, not by
      'QQuick3DGeometry::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DGeometry::Attribute back gives a copy the
      ritual made for Python, in a new cute QQuick3DGeometry::Attribute.
    """

    #  The enums Qt writes inside QQuick3DGeometry::Attribute, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class ComponentType(CuteNum):
      """
      The enum 'QQuick3DGeometry::Attribute::ComponentType' of Qt, with the 4
      names Qt gives in it.
      """

      U16Type = Kee[int](0)
      U32Type = Kee[int](1)
      I32Type = Kee[int](2)
      F32Type = Kee[int](3)

    class Semantic(CuteNum):
      """
      The enum 'QQuick3DGeometry::Attribute::Semantic' of Qt, with the 15
      names Qt gives in it.
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
      TargetPositionSemantic = Kee[int](9)
      TargetNormalSemantic = Kee[int](10)
      TargetTangentSemantic = Kee[int](11)
      TargetBinormalSemantic = Kee[int](12)
      TexCoord1Semantic = Kee[int](13)
      TexCoord0Semantic = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DGeometry::Attribute'

    #  Qt's '~QQuick3DGeometry::Attribute()'. Naming it makes this a value
    #  class: Python owns every C++ QQuick3DGeometry::Attribute behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQuick3DGeometry9AttributeD1Ev'

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

  class TargetAttribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DGeometry::TargetAttribute: a plain Python
    object standing in front of one C++ QQuick3DGeometry::TargetAttribute.

    C++ hands a QQuick3DGeometry::TargetAttribute around as a copy, so every
    C++ QQuick3DGeometry::TargetAttribute behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuick3DGeometry::TargetAttribute yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DGeometry::TargetAttribute::~TargetAttribute()': the
      destructor: Python removes its C++ QQuick3DGeometry::TargetAttribute by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DGeometry::TargetAttribute is created at the first use,
      not by 'QQuick3DGeometry::TargetAttribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DGeometry::TargetAttribute back gives a copy
      the ritual made for Python, in a new cute
      QQuick3DGeometry::TargetAttribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DGeometry::TargetAttribute'

    #  Qt's '~QQuick3DGeometry::TargetAttribute()'. Naming it makes this a
    #  value class: Python owns every C++ QQuick3DGeometry::TargetAttribute
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQuick3DGeometry15TargetAttributeD1Ev'

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

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DGeometry::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DGeometry'

  #  A C++ QQuick3DGeometry Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DGeometry::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def vertexData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuick3DGeometry::vertexData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#vertexData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuick3DGeometry::vertexData() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry10vertexDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def indexData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuick3DGeometry::indexData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#indexData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuick3DGeometry::indexData() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DGeometry9indexDataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def attributeCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::attributeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#attributeCount
    """
    #  int QQuick3DGeometry::attributeCount() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry14attributeCountEv',
    )

  @overload(int)
  def attribute(self, index: int) -> Attribute:
    """
    Calls Qt's 'Attribute QQuick3DGeometry::attribute(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#attribute

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Attribute
      A new cute QQuick3DGeometry::Attribute around the copy Qt gave back.
      Python owns it.
    """
    #  Attribute QQuick3DGeometry::attribute(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry9attributeEi', index,
    )
    return QQuick3DGeometry.Attribute._cuteOwning(address)

  def primitiveType(self) -> PrimitiveType:
    """
    Calls Qt's 'PrimitiveType QQuick3DGeometry::primitiveType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#primitiveType

    Returns
    -------

    PrimitiveType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrimitiveType(number)'
      gives.
    """
    #  PrimitiveType QQuick3DGeometry::primitiveType() const
    return QQuick3DGeometry.PrimitiveType(self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry13primitiveTypeEv',
    ))

  def boundsMin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DGeometry::boundsMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#boundsMin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DGeometry::boundsMin() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DGeometry9boundsMinEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def boundsMax(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DGeometry::boundsMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#boundsMax

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DGeometry::boundsMax() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DGeometry9boundsMaxEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def stride(self) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::stride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#stride
    """
    #  int QQuick3DGeometry::stride() const
    return self.uglySide.call('ritual_ZNK16QQuick3DGeometry6strideEv')

  @overload()
  def subsetCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::subsetCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetCount
    """
    #  int QQuick3DGeometry::subsetCount() const
    return self.uglySide.call('ritual_ZNK16QQuick3DGeometry11subsetCountEv')

  @overload(int)
  def subsetCount(self, subset: int) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::subsetCount(int subset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetCount

    Parameters
    ----------

    subset : int
      Passed on as it is.
    """
    #  int QQuick3DGeometry::subsetCount(int subset) const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry11subsetCountEi', subset,
    )

  @overload(int)
  def subsetBoundsMin(self, subset: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DGeometry::subsetBoundsMin(int subset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetBoundsMin

    Parameters
    ----------

    subset : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DGeometry::subsetBoundsMin(int subset) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry15subsetBoundsMinEi', subset,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def subsetBoundsMax(self, subset: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DGeometry::subsetBoundsMax(int subset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetBoundsMax

    Parameters
    ----------

    subset : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DGeometry::subsetBoundsMax(int subset) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry15subsetBoundsMaxEi', subset,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def subsetOffset(self, subset: int) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::subsetOffset(int subset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetOffset

    Parameters
    ----------

    subset : int
      Passed on as it is.
    """
    #  int QQuick3DGeometry::subsetOffset(int subset) const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry12subsetOffsetEi', subset,
    )

  @overload(int)
  def subsetName(self, subset: int) -> str:
    """
    Calls Qt's 'QString QQuick3DGeometry::subsetName(int subset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#subsetName

    Parameters
    ----------

    subset : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DGeometry::subsetName(int subset) const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry10subsetNameEi', subset,
    )

  def targetData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuick3DGeometry::targetData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#targetData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuick3DGeometry::targetData() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry10targetDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def targetAttribute(self, index: int) -> TargetAttribute:
    """
    Calls Qt's 'TargetAttribute QQuick3DGeometry::targetAttribute(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#targetAttribute

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    TargetAttribute
      A new cute QQuick3DGeometry::TargetAttribute around the copy Qt gave
      back. Python owns it.
    """
    #  TargetAttribute QQuick3DGeometry::targetAttribute(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry15targetAttributeEi', index,
    )
    return QQuick3DGeometry.TargetAttribute._cuteOwning(address)

  def targetAttributeCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DGeometry::targetAttributeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#targetAttributeCount
    """
    #  int QQuick3DGeometry::targetAttributeCount() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DGeometry20targetAttributeCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setVertexData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setVertexData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#setVertexData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setVertexData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry13setVertexDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(int, QByteArray)
  def setVertexData(self, offset: int, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setVertexData(int offset, const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#setVertexData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setVertexData(int offset, const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry13setVertexDataEiRK10QByteArray',
        offset, self._valueOf(data),
    )

  @overload(QByteArray)
  def setIndexData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setIndexData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#setIndexData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setIndexData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry12setIndexDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(int, QByteArray)
  def setIndexData(self, offset: int, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setIndexData(int offset, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#setIndexData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setIndexData(int offset, const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry12setIndexDataEiRK10QByteArray',
        offset, self._valueOf(data),
    )

  @overload(int)
  def setStride(self, stride: int) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setStride(int stride)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#setStride

    Parameters
    ----------

    stride : int
      Passed on as it is.
    """
    #  void QQuick3DGeometry::setStride(int stride)
    self.uglySide.call('ritual_ZN16QQuick3DGeometry9setStrideEi', stride)

  @overload(QVector3D, QVector3D)
  def setBounds(self, min: QVector3D, max: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setBounds(const QVector3D &min, const
    QVector3D &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#setBounds

    Parameters
    ----------

    min : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    max : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setBounds(const QVector3D &min, const QVector3D
    #      &max)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry9setBoundsERK9QVector3DS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(PrimitiveType)
  def setPrimitiveType(self, type: PrimitiveType) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setPrimitiveType(PrimitiveType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#setPrimitiveType

    Parameters
    ----------

    type : PrimitiveType
      Passed on as its number.
    """
    #  void QQuick3DGeometry::setPrimitiveType(PrimitiveType type)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry16setPrimitiveTypeENS_13PrimitiveTypeE',
        type.value,
    )

  @overload(QByteArray)
  def setTargetData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setTargetData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#setTargetData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setTargetData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry13setTargetDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(int, QByteArray)
  def setTargetData(self, offset: int, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::setTargetData(int offset, const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#setTargetData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuick3DGeometry::setTargetData(int offset, const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry13setTargetDataEiRK10QByteArray',
        offset, self._valueOf(data),
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DGeometry::QQuick3DGeometry(QQuick3DObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#QQuick3DGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DGeometry::QQuick3DGeometry(QQuick3DObject *parent)
    self._noteCreation(QQuick3DGeometry, lambda: Rituals.call(
        'ritual_ZN16QQuick3DGeometryC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def d_func(self) -> Optional[QQuick3DGeometryPrivate]:
    """
    Calls Qt's 'QQuick3DGeometryPrivate *QQuick3DGeometry::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#d_func

    Returns
    -------

    Optional[QQuick3DGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DGeometryPrivate *QQuick3DGeometry::d_func()
    address = self.uglySide.call('ritual_ZN16QQuick3DGeometry6d_funcEv')
    from . import QQuick3DGeometryPrivate
    return QQuick3DGeometryPrivate._cuteAt(address)

  @overload(Attribute)
  def addAttribute(self, att: Attribute) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::addAttribute(const Attribute &att)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#addAttribute

    Parameters
    ----------

    att : Attribute
      Passed on as a value: Qt reads the C++ QQuick3DGeometry::Attribute,
      which stays Python's own.
    """
    #  void QQuick3DGeometry::addAttribute(const Attribute &att)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry12addAttributeERKNS_9AttributeE',
        self._valueOf(att),
    )

  @overload(int, int, QVector3D, QVector3D)
  @overload(int, int, QVector3D, QVector3D, str)
  def addSubset(
      self,
      offset: int,
      count: int,
      boundsMin: QVector3D,
      boundsMax: QVector3D,
      name: str = '',
  ) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::addSubset(int offset, int count, const
    QVector3D &boundsMin, const QVector3D &boundsMax, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#addSubset

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    boundsMin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    boundsMax : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QQuick3DGeometry::addSubset(int offset, int count, const
    #      QVector3D &boundsMin, const QVector3D &boundsMax, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry9addSubsetEiiRK9QVector3DS2_RK7QString',
        offset, count, self._valueOf(boundsMin), self._valueOf(boundsMax),
        name,
    )

  @overload(TargetAttribute)
  def addTargetAttribute(self, att: TargetAttribute) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::addTargetAttribute(const
    TargetAttribute &att)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#addTargetAttribute

    Parameters
    ----------

    att : TargetAttribute
      Passed on as a value: Qt reads the C++
      QQuick3DGeometry::TargetAttribute, which stays Python's own.
    """
    #  void QQuick3DGeometry::addTargetAttribute(const TargetAttribute &att)
    self.uglySide.call(
        'ritual_ZN16QQuick3DGeometry18addTargetAttributeERKNS_15TargetAttri'
        'buteE',
        self._valueOf(att),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#clear
    """
    #  void QQuick3DGeometry::clear()
    self.uglySide.call('ritual_ZN16QQuick3DGeometry5clearEv')

  def geometryNodeDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::geometryNodeDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#geometryNodeDirty
    """
    #  void QQuick3DGeometry::geometryNodeDirty()
    self.uglySide.call('ritual_ZN16QQuick3DGeometry17geometryNodeDirtyEv')

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#geometryChanged
    """
    #  void QQuick3DGeometry::geometryChanged()
    self.uglySide.call('ritual_ZN16QQuick3DGeometry15geometryChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometry.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DGeometry::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN16QQuick3DGeometry17updateSpatialNodeEP21QSSGRenderGraphO'
        'bject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DGeometry17updateSpatialNodeEP21QSSGRender'
          'GraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DGeometry::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dgeometry.html#markAllDirty
    """
    #  void QQuick3DGeometry::markAllDirty()
    ritual = 'ritual_ZN16QQuick3DGeometry12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DGeometry12markAllDirtyEv'
    self.uglySide.call(ritual)
