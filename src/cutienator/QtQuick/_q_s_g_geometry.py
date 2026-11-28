"""
QSGGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsggeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGGeometry: a plain Python object standing in front
  of one C++ QSGGeometry.

  What exists
  -----------

  Every function of Qt's QSGGeometry that has a ritual and that Python can
  call so far, 29 names in all: 'defaultAttributes_Point2D',
  'defaultAttributes_TexturedPoint2D', 'defaultAttributes_ColoredPoint2D',
  'setDrawingMode', 'drawingMode', 'allocate', 'vertexCount',
  'setVertexCount', 'vertexDataAsPoint2D', 'vertexDataAsTexturedPoint2D',
  'vertexDataAsColoredPoint2D', 'indexType', 'indexCount', 'setIndexCount',
  'sizeOfIndex', 'attributeCount', 'attributes', 'sizeOfVertex',
  'updateRectGeometry', 'updateTexturedRectGeometry',
  'updateColoredRectGeometry', 'setIndexDataPattern', 'indexDataPattern',
  'setVertexDataPattern', 'vertexDataPattern', 'markIndexDataDirty',
  'markVertexDataDirty', 'lineWidth', 'setLineWidth'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGeometry::~QSGGeometry()': the destructor: Python never removes
    a C++ QSGGeometry.
  - Qt's 'void *QSGGeometry::vertexData()': gives 'void', which has no cute
    class yet.
  - Qt's 'const void *QSGGeometry::vertexData() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const Point2D *QSGGeometry::vertexDataAsPoint2D() const': takes in
    Python what 'Point2D *QSGGeometry::vertexDataAsPoint2D()' takes.
  - Qt's 'const TexturedPoint2D *QSGGeometry::vertexDataAsTexturedPoint2D()
    const': takes in Python what 'TexturedPoint2D
    *QSGGeometry::vertexDataAsTexturedPoint2D()' takes.
  - Qt's 'const ColoredPoint2D *QSGGeometry::vertexDataAsColoredPoint2D()
    const': takes in Python what 'ColoredPoint2D
    *QSGGeometry::vertexDataAsColoredPoint2D()' takes.
  - Qt's 'void *QSGGeometry::indexData()': gives 'void', which has no cute
    class yet.
  - Qt's 'const void *QSGGeometry::indexData() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const uint *QSGGeometry::indexDataAsUInt() const': gives 'unsigned
    int', which has no cute class yet.
  - Qt's 'const quint16 *QSGGeometry::indexDataAsUShort() const': gives
    'unsigned short', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 46 functions Qt declares: 4 forbidden; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QSGGeometry is created at the first use, not by
    'QSGGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGGeometry.
  - Each name of Qt's QSGGeometry that has no cute function yet, 'indexData',
    'indexDataAsUInt', 'indexDataAsUShort', 'vertexData', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSGGeometry, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AttributeType(CuteNum):
    """
    The enum 'QSGGeometry::AttributeType' of Qt, with the 6 names Qt gives in
    it.
    """

    UnknownAttribute = Kee[int](0)
    PositionAttribute = Kee[int](1)
    ColorAttribute = Kee[int](2)
    TexCoordAttribute = Kee[int](3)
    TexCoord1Attribute = Kee[int](4)
    TexCoord2Attribute = Kee[int](5)

  class DataPattern(CuteNum):
    """
    The enum 'QSGGeometry::DataPattern' of Qt, with the 4 names Qt gives in
    it.
    """

    AlwaysUploadPattern = Kee[int](0)
    StreamPattern = Kee[int](1)
    DynamicPattern = Kee[int](2)
    StaticPattern = Kee[int](3)

  class DrawingMode(CuteNum):
    """
    The enum 'QSGGeometry::DrawingMode' of Qt, with the 7 names Qt gives in
    it.
    """

    DrawPoints = Kee[int](0)
    DrawLines = Kee[int](1)
    DrawLineLoop = Kee[int](2)
    DrawLineStrip = Kee[int](3)
    DrawTriangles = Kee[int](4)
    DrawTriangleStrip = Kee[int](5)
    DrawTriangleFan = Kee[int](6)

  class Type(CuteNum):
    """
    The enum 'QSGGeometry::Type' of Qt, with the 11 names Qt gives in it.
    """

    ByteType = Kee[int](5120)
    UnsignedByteType = Kee[int](5121)
    ShortType = Kee[int](5122)
    UnsignedShortType = Kee[int](5123)
    IntType = Kee[int](5124)
    UnsignedIntType = Kee[int](5125)
    FloatType = Kee[int](5126)
    Bytes2Type = Kee[int](5127)
    Bytes3Type = Kee[int](5128)
    Bytes4Type = Kee[int](5129)
    DoubleType = Kee[int](5130)

  #  The classes Qt writes inside QSGGeometry, each a class in here as in
  #  C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGeometry::Attribute: a plain Python object
    standing in front of one C++ QSGGeometry::Attribute.

    C++ hands a QSGGeometry::Attribute around as a copy, so every C++
    QSGGeometry::Attribute behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSGGeometry::Attribute that has a ritual and that
    Python can call so far, 1 name in all: 'create'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Attribute QSGGeometry::Attribute::createWithAttributeType(int
      pos, int tupleSize, int primitiveType, AttributeType attributeType)':
      names the enum 'QSGGeometry::AttributeType', whose class cannot be
      named here.
    - Qt's 'QSGGeometry::Attribute::~Attribute()': the destructor: Python
      removes its C++ QSGGeometry::Attribute by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSGGeometry::Attribute is created at the first use, not by
      'QSGGeometry::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGeometry::Attribute back gives a copy the ritual
      made for Python, in a new cute QSGGeometry::Attribute.
    - Each name of Qt's QSGGeometry::Attribute that has no cute function yet,
      'createWithAttributeType', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(int, int, int)
    @overload(int, int, int, bool)
    def create(
        pos: int,
        tupleSize: int,
        primitiveType: int,
        isPosition: bool = False,
    ) -> QSGGeometry.Attribute:
      """
      Calls Qt's 'Attribute QSGGeometry::Attribute::create(int pos, int
      tupleSize, int primitiveType, bool isPosition)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsggeometry-attribute.html#create

      Parameters
      ----------

      pos : int
        Passed on as it is.

      tupleSize : int
        Passed on as it is.

      primitiveType : int
        Passed on as it is.

      isPosition : bool
        Passed on as it is. May be left out, as in Qt: it is then False.

      Returns
      -------

      QSGGeometry.Attribute
        A new cute QSGGeometry::Attribute around the copy Qt gave back.
        Python owns it.
      """
      #  Attribute QSGGeometry::Attribute::create(int pos, int tupleSize, int
      #      primitiveType, bool isPosition)
      address = Rituals.call(
          'ritual_ZN11QSGGeometry9Attribute6createEiiib',
          pos, tupleSize, primitiveType, isPosition,
      )
      return QSGGeometry.Attribute._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGeometry::Attribute'

    #  Qt's '~QSGGeometry::Attribute()'. Naming it makes this a value class:
    #  Python owns every C++ QSGGeometry::Attribute behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QSGGeometry9AttributeD1Ev'

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

    @staticmethod
    def createWithAttributeType(*__, **_) -> Never:
      """
      Qt's 'Attribute QSGGeometry::Attribute::createWithAttributeType(int
      pos, int tupleSize, int primitiveType, AttributeType attributeType)':
      names the enum 'QSGGeometry::AttributeType', whose class cannot be
      named here.
      """
      raise NotImplementedError(
          "'QSGGeometry.Attribute.createWithAttributeType' has no cute "
          "function yet. Qt's 'Attribute "
          "QSGGeometry::Attribute::createWithAttributeType(int pos, int "
          "tupleSize, int primitiveType, AttributeType attributeType)': "
          "names the enum 'QSGGeometry::AttributeType', whose class cannot "
          "be named here.")

  class AttributeSet(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGeometry::AttributeSet: a plain Python object
    standing in front of one C++ QSGGeometry::AttributeSet.

    C++ hands a QSGGeometry::AttributeSet around as a copy, so every C++
    QSGGeometry::AttributeSet behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSGGeometry::AttributeSet yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGeometry::AttributeSet::~AttributeSet()': the destructor:
      Python removes its C++ QSGGeometry::AttributeSet by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGGeometry::AttributeSet is created at the first use, not by
      'QSGGeometry::AttributeSet(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGeometry::AttributeSet back gives a copy the
      ritual made for Python, in a new cute QSGGeometry::AttributeSet.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGeometry::AttributeSet'

    #  Qt's '~QSGGeometry::AttributeSet()'. Naming it makes this a value
    #  class: Python owns every C++ QSGGeometry::AttributeSet behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QSGGeometry12AttributeSetD1Ev'

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

  class ColoredPoint2D(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGeometry::ColoredPoint2D: a plain Python object
    standing in front of one C++ QSGGeometry::ColoredPoint2D.

    C++ hands a QSGGeometry::ColoredPoint2D around as a copy, so every C++
    QSGGeometry::ColoredPoint2D behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSGGeometry::ColoredPoint2D that has a ritual and
    that Python can call so far, 1 name in all: 'set'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGeometry::ColoredPoint2D::~ColoredPoint2D()': the destructor:
      Python removes its C++ QSGGeometry::ColoredPoint2D by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGGeometry::ColoredPoint2D is created at the first use, not by
      'QSGGeometry::ColoredPoint2D(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGeometry::ColoredPoint2D back gives a copy the
      ritual made for Python, in a new cute QSGGeometry::ColoredPoint2D.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGeometry::ColoredPoint2D'

    #  Qt's '~QSGGeometry::ColoredPoint2D()'. Naming it makes this a value
    #  class: Python owns every C++ QSGGeometry::ColoredPoint2D behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QSGGeometry14ColoredPoint2DD1Ev'

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

    @overload(float, float, int, int, int, int)
    def set(
        self,
        nx: float,
        ny: float,
        nr: int,
        ng: int,
        nb: int,
        na: int,
    ) -> None:
      """
      Calls Qt's 'void QSGGeometry::ColoredPoint2D::set(float nx, float ny,
      uchar nr, uchar ng, uchar nb, uchar na)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsggeometry-coloredpoint2d.html#set

      Parameters
      ----------

      nx : float
        Passed on as it is.

      ny : float
        Passed on as it is.

      nr : int
        Passed on as it is.

      ng : int
        Passed on as it is.

      nb : int
        Passed on as it is.

      na : int
        Passed on as it is.
      """
      #  void QSGGeometry::ColoredPoint2D::set(float nx, float ny, uchar nr,
      #      uchar ng, uchar nb, uchar na)
      self.uglySide.call(
          'ritual_ZN11QSGGeometry14ColoredPoint2D3setEffhhhh',
          nx, ny, nr, ng, nb, na,
      )

  class Point2D(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGeometry::Point2D: a plain Python object
    standing in front of one C++ QSGGeometry::Point2D.

    C++ hands a QSGGeometry::Point2D around as a copy, so every C++
    QSGGeometry::Point2D behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSGGeometry::Point2D that has a ritual and that
    Python can call so far, 1 name in all: 'set'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGeometry::Point2D::~Point2D()': the destructor: Python removes
      its C++ QSGGeometry::Point2D by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGGeometry::Point2D is created at the first use, not by
      'QSGGeometry::Point2D(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGeometry::Point2D back gives a copy the ritual
      made for Python, in a new cute QSGGeometry::Point2D.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGeometry::Point2D'

    #  Qt's '~QSGGeometry::Point2D()'. Naming it makes this a value class:
    #  Python owns every C++ QSGGeometry::Point2D behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QSGGeometry7Point2DD1Ev'

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

    @overload(float, float)
    def set(self, nx: float, ny: float) -> None:
      """
      Calls Qt's 'void QSGGeometry::Point2D::set(float nx, float ny)'.

      Qt's own words: https://doc.qt.io/qt-6/qsggeometry-point2d.html#set

      Parameters
      ----------

      nx : float
        Passed on as it is.

      ny : float
        Passed on as it is.
      """
      #  void QSGGeometry::Point2D::set(float nx, float ny)
      self.uglySide.call('ritual_ZN11QSGGeometry7Point2D3setEff', nx, ny)

  class TexturedPoint2D(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGGeometry::TexturedPoint2D: a plain Python object
    standing in front of one C++ QSGGeometry::TexturedPoint2D.

    C++ hands a QSGGeometry::TexturedPoint2D around as a copy, so every C++
    QSGGeometry::TexturedPoint2D behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSGGeometry::TexturedPoint2D that has a ritual and
    that Python can call so far, 1 name in all: 'set'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGGeometry::TexturedPoint2D::~TexturedPoint2D()': the
      destructor: Python removes its C++ QSGGeometry::TexturedPoint2D by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QSGGeometry::TexturedPoint2D is created at the first use, not
      by 'QSGGeometry::TexturedPoint2D(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGGeometry::TexturedPoint2D back gives a copy the
      ritual made for Python, in a new cute QSGGeometry::TexturedPoint2D.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGGeometry::TexturedPoint2D'

    #  Qt's '~QSGGeometry::TexturedPoint2D()'. Naming it makes this a value
    #  class: Python owns every C++ QSGGeometry::TexturedPoint2D behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QSGGeometry15TexturedPoint2DD1Ev'

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

    @overload(float, float, float, float)
    def set(self, nx: float, ny: float, ntx: float, nty: float) -> None:
      """
      Calls Qt's 'void QSGGeometry::TexturedPoint2D::set(float nx, float ny,
      float ntx, float nty)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsggeometry-texturedpoint2d.html#set

      Parameters
      ----------

      nx : float
        Passed on as it is.

      ny : float
        Passed on as it is.

      ntx : float
        Passed on as it is.

      nty : float
        Passed on as it is.
      """
      #  void QSGGeometry::TexturedPoint2D::set(float nx, float ny, float
      #      ntx, float nty)
      self.uglySide.call(
          'ritual_ZN11QSGGeometry15TexturedPoint2D3setEffff',
          nx, ny, ntx, nty,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultAttributes_Point2D() -> AttributeSet:
    """
    Calls Qt's 'const AttributeSet
    &QSGGeometry::defaultAttributes_Point2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#defaultAttributes_Point2D

    Returns
    -------

    AttributeSet
      A new cute QSGGeometry::AttributeSet around the copy Qt gave back.
      Python owns it.
    """
    #  const AttributeSet &QSGGeometry::defaultAttributes_Point2D()
    address = Rituals.call(
        'ritual_ZN11QSGGeometry25defaultAttributes_Point2DEv',
    )
    return QSGGeometry.AttributeSet._cuteOwning(address)

  @staticmethod
  def defaultAttributes_TexturedPoint2D() -> AttributeSet:
    """
    Calls Qt's 'const AttributeSet
    &QSGGeometry::defaultAttributes_TexturedPoint2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#defaultAttributes_TexturedPoint2D

    Returns
    -------

    AttributeSet
      A new cute QSGGeometry::AttributeSet around the copy Qt gave back.
      Python owns it.
    """
    #  const AttributeSet &QSGGeometry::defaultAttributes_TexturedPoint2D()
    address = Rituals.call(
        'ritual_ZN11QSGGeometry33defaultAttributes_TexturedPoint2DEv',
    )
    return QSGGeometry.AttributeSet._cuteOwning(address)

  @staticmethod
  def defaultAttributes_ColoredPoint2D() -> AttributeSet:
    """
    Calls Qt's 'const AttributeSet
    &QSGGeometry::defaultAttributes_ColoredPoint2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#defaultAttributes_ColoredPoint2D

    Returns
    -------

    AttributeSet
      A new cute QSGGeometry::AttributeSet around the copy Qt gave back.
      Python owns it.
    """
    #  const AttributeSet &QSGGeometry::defaultAttributes_ColoredPoint2D()
    address = Rituals.call(
        'ritual_ZN11QSGGeometry32defaultAttributes_ColoredPoint2DEv',
    )
    return QSGGeometry.AttributeSet._cuteOwning(address)

  @staticmethod
  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def updateRectGeometry(g: Optional[QSGGeometry], rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGGeometry::updateRectGeometry(QSGGeometry *g, const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#updateRectGeometry

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGGeometry::updateRectGeometry(QSGGeometry *g, const QRectF
    #      &rect)
    Rituals.call(
        'ritual_ZN11QSGGeometry18updateRectGeometryEPS_RK6QRectF',
        CuteMixin._addressOf(g), CuteMixin._valueOf(rect),
    )

  @staticmethod
  @overload(THIS, QRectF, QRectF)
  @overload(NoneType, QRectF, QRectF)
  def updateTexturedRectGeometry(
      g: Optional[QSGGeometry],
      rect: QRectF,
      sourceRect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QSGGeometry::updateTexturedRectGeometry(QSGGeometry *g,
    const QRectF &rect, const QRectF &sourceRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#updateTexturedRectGeometry

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGGeometry::updateTexturedRectGeometry(QSGGeometry *g, const
    #      QRectF &rect, const QRectF &sourceRect)
    Rituals.call(
        'ritual_ZN11QSGGeometry26updateTexturedRectGeometryEPS_RK6QRectFS3_',
        CuteMixin._addressOf(g), CuteMixin._valueOf(rect),
        CuteMixin._valueOf(sourceRect),
    )

  @staticmethod
  @overload(THIS, QRectF)
  @overload(NoneType, QRectF)
  def updateColoredRectGeometry(
      g: Optional[QSGGeometry],
      rect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QSGGeometry::updateColoredRectGeometry(QSGGeometry *g,
    const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#updateColoredRectGeometry

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGGeometry::updateColoredRectGeometry(QSGGeometry *g, const
    #      QRectF &rect)
    Rituals.call(
        'ritual_ZN11QSGGeometry25updateColoredRectGeometryEPS_RK6QRectF',
        CuteMixin._addressOf(g), CuteMixin._valueOf(rect),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def drawingMode(self) -> int:
    """
    Calls Qt's 'unsigned int QSGGeometry::drawingMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#drawingMode
    """
    #  unsigned int QSGGeometry::drawingMode() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry11drawingModeEv')

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::vertexCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#vertexCount
    """
    #  int QSGGeometry::vertexCount() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry11vertexCountEv')

  def indexType(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::indexType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#indexType
    """
    #  int QSGGeometry::indexType() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry9indexTypeEv')

  def indexCount(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::indexCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#indexCount
    """
    #  int QSGGeometry::indexCount() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry10indexCountEv')

  def sizeOfIndex(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::sizeOfIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#sizeOfIndex
    """
    #  int QSGGeometry::sizeOfIndex() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry11sizeOfIndexEv')

  def attributeCount(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::attributeCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#attributeCount
    """
    #  int QSGGeometry::attributeCount() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry14attributeCountEv')

  def attributes(self) -> Optional[Attribute]:
    """
    Calls Qt's 'const Attribute *QSGGeometry::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#attributes

    Returns
    -------

    Optional[Attribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Attribute *QSGGeometry::attributes() const
    address = self.uglySide.call('ritual_ZNK11QSGGeometry10attributesEv')
    return QSGGeometry.Attribute._cuteAt(address)

  def sizeOfVertex(self) -> int:
    """
    Calls Qt's 'int QSGGeometry::sizeOfVertex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#sizeOfVertex
    """
    #  int QSGGeometry::sizeOfVertex() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry12sizeOfVertexEv')

  def indexDataPattern(self) -> DataPattern:
    """
    Calls Qt's 'DataPattern QSGGeometry::indexDataPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#indexDataPattern

    Returns
    -------

    DataPattern
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DataPattern(number)'
      gives.
    """
    #  DataPattern QSGGeometry::indexDataPattern() const
    return QSGGeometry.DataPattern(self.uglySide.call(
        'ritual_ZNK11QSGGeometry16indexDataPatternEv',
    ))

  def vertexDataPattern(self) -> DataPattern:
    """
    Calls Qt's 'DataPattern QSGGeometry::vertexDataPattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#vertexDataPattern

    Returns
    -------

    DataPattern
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DataPattern(number)'
      gives.
    """
    #  DataPattern QSGGeometry::vertexDataPattern() const
    return QSGGeometry.DataPattern(self.uglySide.call(
        'ritual_ZNK11QSGGeometry17vertexDataPatternEv',
    ))

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QSGGeometry::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#lineWidth
    """
    #  float QSGGeometry::lineWidth() const
    return self.uglySide.call('ritual_ZNK11QSGGeometry9lineWidthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDrawingMode(self, mode: int) -> None:
    """
    Calls Qt's 'void QSGGeometry::setDrawingMode(unsigned int mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#setDrawingMode

    Parameters
    ----------

    mode : int
      Passed on as it is.
    """
    #  void QSGGeometry::setDrawingMode(unsigned int mode)
    self.uglySide.call('ritual_ZN11QSGGeometry14setDrawingModeEj', mode)

  @overload(int)
  def setVertexCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSGGeometry::setVertexCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#setVertexCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSGGeometry::setVertexCount(int count)
    self.uglySide.call('ritual_ZN11QSGGeometry14setVertexCountEi', count)

  @overload(int)
  def setIndexCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSGGeometry::setIndexCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#setIndexCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSGGeometry::setIndexCount(int count)
    self.uglySide.call('ritual_ZN11QSGGeometry13setIndexCountEi', count)

  @overload(DataPattern)
  def setIndexDataPattern(self, p: DataPattern) -> None:
    """
    Calls Qt's 'void QSGGeometry::setIndexDataPattern(DataPattern p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#setIndexDataPattern

    Parameters
    ----------

    p : DataPattern
      Passed on as its number.
    """
    #  void QSGGeometry::setIndexDataPattern(DataPattern p)
    self.uglySide.call(
        'ritual_ZN11QSGGeometry19setIndexDataPatternENS_11DataPatternE',
        p.value,
    )

  @overload(DataPattern)
  def setVertexDataPattern(self, p: DataPattern) -> None:
    """
    Calls Qt's 'void QSGGeometry::setVertexDataPattern(DataPattern p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#setVertexDataPattern

    Parameters
    ----------

    p : DataPattern
      Passed on as its number.
    """
    #  void QSGGeometry::setVertexDataPattern(DataPattern p)
    self.uglySide.call(
        'ritual_ZN11QSGGeometry20setVertexDataPatternENS_11DataPatternE',
        p.value,
    )

  @overload(float)
  def setLineWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QSGGeometry::setLineWidth(float w)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#setLineWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QSGGeometry::setLineWidth(float w)
    self.uglySide.call('ritual_ZN11QSGGeometry12setLineWidthEf', w)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AttributeSet, int)
  @overload(AttributeSet, int, int)
  @overload(AttributeSet, int, int, int)
  def __init__(
      self,
      attribs: AttributeSet,
      vertexCount: int,
      indexCount: int = 0,
      indexType: int = 5123,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSGGeometry::QSGGeometry(const
    QSGGeometry::AttributeSet &attribs, int vertexCount, int indexCount, int
    indexType)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#QSGGeometry

    Parameters
    ----------

    attribs : AttributeSet
      Passed on as a value: Qt reads the C++ QSGGeometry::AttributeSet, which
      stays Python's own.

    vertexCount : int
      Passed on as it is.

    indexCount : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    indexType : int
      Passed on as it is. May be left out, as in Qt: it is then 5123.
    """
    #  QSGGeometry::QSGGeometry(const QSGGeometry::AttributeSet &attribs, int
    #      vertexCount, int indexCount, int indexType)
    self._noteCreation(QSGGeometry, lambda: Rituals.call(
        'ritual_ZN11QSGGeometryC1ERKNS_12AttributeSetEiii',
        self._valueOf(attribs), vertexCount, indexCount, indexType,
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

  @overload(int)
  @overload(int, int)
  def allocate(self, vertexCount: int, indexCount: int = 0) -> None:
    """
    Calls Qt's 'void QSGGeometry::allocate(int vertexCount, int indexCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometry.html#allocate

    Parameters
    ----------

    vertexCount : int
      Passed on as it is.

    indexCount : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QSGGeometry::allocate(int vertexCount, int indexCount)
    self.uglySide.call(
        'ritual_ZN11QSGGeometry8allocateEii', vertexCount, indexCount,
    )

  def vertexDataAsPoint2D(self) -> Optional[Point2D]:
    """
    Calls Qt's 'Point2D *QSGGeometry::vertexDataAsPoint2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#vertexDataAsPoint2D

    Returns
    -------

    Optional[Point2D]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Point2D *QSGGeometry::vertexDataAsPoint2D()
    address = self.uglySide.call(
        'ritual_ZN11QSGGeometry19vertexDataAsPoint2DEv',
    )
    return QSGGeometry.Point2D._cuteAt(address)

  def vertexDataAsTexturedPoint2D(self) -> Optional[TexturedPoint2D]:
    """
    Calls Qt's 'TexturedPoint2D *QSGGeometry::vertexDataAsTexturedPoint2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#vertexDataAsTexturedPoint2D

    Returns
    -------

    Optional[TexturedPoint2D]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TexturedPoint2D *QSGGeometry::vertexDataAsTexturedPoint2D()
    address = self.uglySide.call(
        'ritual_ZN11QSGGeometry27vertexDataAsTexturedPoint2DEv',
    )
    return QSGGeometry.TexturedPoint2D._cuteAt(address)

  def vertexDataAsColoredPoint2D(self) -> Optional[ColoredPoint2D]:
    """
    Calls Qt's 'ColoredPoint2D *QSGGeometry::vertexDataAsColoredPoint2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#vertexDataAsColoredPoint2D

    Returns
    -------

    Optional[ColoredPoint2D]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ColoredPoint2D *QSGGeometry::vertexDataAsColoredPoint2D()
    address = self.uglySide.call(
        'ritual_ZN11QSGGeometry26vertexDataAsColoredPoint2DEv',
    )
    return QSGGeometry.ColoredPoint2D._cuteAt(address)

  def markIndexDataDirty(self) -> None:
    """
    Calls Qt's 'void QSGGeometry::markIndexDataDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#markIndexDataDirty
    """
    #  void QSGGeometry::markIndexDataDirty()
    self.uglySide.call('ritual_ZN11QSGGeometry18markIndexDataDirtyEv')

  def markVertexDataDirty(self) -> None:
    """
    Calls Qt's 'void QSGGeometry::markVertexDataDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometry.html#markVertexDataDirty
    """
    #  void QSGGeometry::markVertexDataDirty()
    self.uglySide.call('ritual_ZN11QSGGeometry19markVertexDataDirtyEv')

  @staticmethod
  def indexData(*__, **_) -> Never:
    """
    - Qt's 'void *QSGGeometry::indexData()': gives 'void', which has no cute
      class yet.
    - Qt's 'const void *QSGGeometry::indexData() const': gives 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGGeometry.indexData' has no cute function yet. Qt's 'void "
        "*QSGGeometry::indexData()': gives 'void', which has no cute class "
        "yet. Qt's 'const void *QSGGeometry::indexData() const': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def indexDataAsUInt(*__, **_) -> Never:
    """
    - Qt's 'const uint *QSGGeometry::indexDataAsUInt() const': gives
      'unsigned int', which has no cute class yet.
    - Qt's 'uint *QSGGeometry::indexDataAsUInt()': takes or gives a type that
      cannot be passed yet: uint *.
    """
    raise NotImplementedError(
        "'QSGGeometry.indexDataAsUInt' has no cute function yet. Qt's "
        "'const uint *QSGGeometry::indexDataAsUInt() const': gives "
        "'unsigned int', which has no cute class yet. Qt's 'uint "
        "*QSGGeometry::indexDataAsUInt()': takes or gives a type that "
        "cannot be passed yet: uint *.")

  @staticmethod
  def indexDataAsUShort(*__, **_) -> Never:
    """
    - Qt's 'const quint16 *QSGGeometry::indexDataAsUShort() const': gives
      'unsigned short', which has no cute class yet.
    - Qt's 'quint16 *QSGGeometry::indexDataAsUShort()': takes or gives a type
      that cannot be passed yet: quint16 *.
    """
    raise NotImplementedError(
        "'QSGGeometry.indexDataAsUShort' has no cute function yet. Qt's "
        "'const quint16 *QSGGeometry::indexDataAsUShort() const': gives "
        "'unsigned short', which has no cute class yet. Qt's 'quint16 "
        "*QSGGeometry::indexDataAsUShort()': takes or gives a type that "
        "cannot be passed yet: quint16 *.")

  @staticmethod
  def vertexData(*__, **_) -> Never:
    """
    - Qt's 'void *QSGGeometry::vertexData()': gives 'void', which has no cute
      class yet.
    - Qt's 'const void *QSGGeometry::vertexData() const': gives 'void', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGGeometry.vertexData' has no cute function yet. Qt's 'void "
        "*QSGGeometry::vertexData()': gives 'void', which has no cute class "
        "yet. Qt's 'const void *QSGGeometry::vertexData() const': gives "
        "'void', which has no cute class yet.")
