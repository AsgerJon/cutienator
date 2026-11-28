"""
VertexIndexer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/vertexindexer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means VertexIndexer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class VertexIndexer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's VertexIndexer: a plain Python object standing in
  front of one C++ VertexIndexer.

  C++ hands a VertexIndexer around as a copy, so every C++ VertexIndexer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's VertexIndexer yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool VertexIndexer::getSimilarVertexIndex_fast(const PackedVertex
    &packed, QMap<PackedVertex, GLuint> &VertexToOutIndex, GLuint &result)':
    takes a type Python has no way to hand over yet.
  - Qt's 'VertexIndexer::~VertexIndexer()': the destructor: Python removes
    its C++ VertexIndexer by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ VertexIndexer is created at the first use, not by
    'VertexIndexer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a VertexIndexer back gives a copy the ritual made for
    Python, in a new cute VertexIndexer.
  - Each name of Qt's VertexIndexer that has no cute function yet,
    'getSimilarVertexIndex_fast', 'indexVBO', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside VertexIndexer, each a class in here as in
  #  C++.

  class PackedVertex(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's VertexIndexer::PackedVertex: a plain Python object
    standing in front of one C++ VertexIndexer::PackedVertex.

    C++ hands a VertexIndexer::PackedVertex around as a copy, so every C++
    VertexIndexer::PackedVertex behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's VertexIndexer::PackedVertex that has a ritual and
    that Python can call so far, 1 name in all: '__lt__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'VertexIndexer::PackedVertex::~PackedVertex()': the destructor:
      Python removes its C++ VertexIndexer::PackedVertex by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ VertexIndexer::PackedVertex is created at the first use, not by
      'VertexIndexer::PackedVertex(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a VertexIndexer::PackedVertex back gives a copy the
      ritual made for Python, in a new cute VertexIndexer::PackedVertex.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'VertexIndexer::PackedVertex'

    #  Qt's '~VertexIndexer::PackedVertex()'. Naming it makes this a value
    #  class: Python owns every C++ VertexIndexer::PackedVertex behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13VertexIndexer12PackedVertexD1Ev'

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

    @overload(THIS)
    def __lt__(self, that: VertexIndexer.PackedVertex) -> bool:
      """
      Calls Qt's 'bool VertexIndexer::PackedVertex::operator<(const
      PackedVertex that) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/vertexindexer-packedvertex.html#operator<

      Parameters
      ----------

      that : VertexIndexer.PackedVertex
        Passed on as a value: Qt reads the C++ VertexIndexer::PackedVertex,
        which stays Python's own.
      """
      #  bool VertexIndexer::PackedVertex::operator<(const PackedVertex that)
      #      const
      return self.uglySide.call(
          'ritual_ZNK13VertexIndexer12PackedVertexltES0_',
          self._valueOf(that),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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
  __qt_class__ = 'VertexIndexer'

  #  Qt's '~VertexIndexer()'. Naming it makes this a value class: Python owns
  #  every C++ VertexIndexer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13VertexIndexerD1Ev'

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
  def getSimilarVertexIndex_fast(*__, **_) -> Never:
    """
    Qt's 'bool VertexIndexer::getSimilarVertexIndex_fast(const PackedVertex
    &packed, QMap<PackedVertex, GLuint> &VertexToOutIndex, GLuint &result)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'VertexIndexer.getSimilarVertexIndex_fast' has no cute function "
        "yet. Qt's 'bool VertexIndexer::getSimilarVertexIndex_fast(const "
        "PackedVertex &packed, QMap<PackedVertex, GLuint> "
        "&VertexToOutIndex, GLuint &result)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def indexVBO(*__, **_) -> Never:
    """
    Qt's 'void VertexIndexer::indexVBO(const QList<QVector3D> &in_vertices,
    const QList<QVector2D> &in_uvs, const QList<QVector3D> &in_normals,
    QList<GLuint> &out_indices, QList<QVector3D> &out_vertices,
    QList<QVector2D> &out_uvs, QList<QVector3D> &out_normals)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'unique_vertices'.
    """
    raise NotImplementedError(
        "'VertexIndexer.indexVBO' has no cute function yet. Qt's 'void "
        "VertexIndexer::indexVBO(const QList<QVector3D> &in_vertices, const "
        "QList<QVector2D> &in_uvs, const QList<QVector3D> &in_normals, "
        "QList<GLuint> &out_indices, QList<QVector3D> &out_vertices, "
        "QList<QVector2D> &out_uvs, QList<QVector3D> &out_normals)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'unique_vertices'.")
