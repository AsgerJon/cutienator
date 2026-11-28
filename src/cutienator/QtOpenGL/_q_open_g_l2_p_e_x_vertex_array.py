"""
QOpenGL2PEXVertexArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGL2PEXVertexArray to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QOpenGLPoint, QOpenGLRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QOpenGL2PEXVertexArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGL2PEXVertexArray: a plain Python object
  standing in front of one C++ QOpenGL2PEXVertexArray.

  What exists
  -----------

  Every function of Qt's QOpenGL2PEXVertexArray that has a ritual and that
  Python can call so far, 10 names in all: 'addRect', 'addQuad', 'addVertex',
  'clear', 'data', 'stopCount', 'boundingRect', 'vertexCount', 'lineToArray',
  'addClosingLine'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpenGL2PEXVertexArray::addPath(const QVectorPath &path,
    GLfloat curveInverseScale, bool outline)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QOpenGL2PEXVertexArray::addCentroid(const QVectorPath &path,
    int subPathIndex)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QOpenGL2PEXVertexArray is created at the first use, not by
    'QOpenGL2PEXVertexArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGL2PEXVertexArray.
  - Each name of Qt's QOpenGL2PEXVertexArray that has no cute function yet,
    'addCentroid', 'addPath', 'stops', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGL2PEXVertexArray'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stopCount(self) -> int:
    """
    Calls Qt's 'int QOpenGL2PEXVertexArray::stopCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#stopCount
    """
    #  int QOpenGL2PEXVertexArray::stopCount() const
    return self.uglySide.call(
        'ritual_ZNK22QOpenGL2PEXVertexArray9stopCountEv',
    )

  def boundingRect(self) -> QOpenGLRect:
    """
    Calls Qt's 'QOpenGLRect QOpenGL2PEXVertexArray::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#boundingRect

    Returns
    -------

    QOpenGLRect
      A new cute QOpenGLRect around the copy Qt gave back. Python owns it.
    """
    #  QOpenGLRect QOpenGL2PEXVertexArray::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK22QOpenGL2PEXVertexArray12boundingRectEv',
    )
    from . import QOpenGLRect
    return QOpenGLRect._cuteOwning(address)

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int QOpenGL2PEXVertexArray::vertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#vertexCount
    """
    #  int QOpenGL2PEXVertexArray::vertexCount() const
    return self.uglySide.call(
        'ritual_ZNK22QOpenGL2PEXVertexArray11vertexCountEv',
    )

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
    Notes what was given, for Qt's
    'QOpenGL2PEXVertexArray::QOpenGL2PEXVertexArray()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#QOpenGL2PEXVertexArray
    """
    #  QOpenGL2PEXVertexArray::QOpenGL2PEXVertexArray()
    self._noteCreation(QOpenGL2PEXVertexArray, lambda: Rituals.call(
        'ritual_ZN22QOpenGL2PEXVertexArrayC1Ev',
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

  @overload(QRectF)
  def addRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::addRect(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#addRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QOpenGL2PEXVertexArray::addRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN22QOpenGL2PEXVertexArray7addRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def addQuad(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::addQuad(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#addQuad

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QOpenGL2PEXVertexArray::addQuad(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN22QOpenGL2PEXVertexArray7addQuadERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float)
  def addVertex(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::addVertex(const GLfloat x, const
    GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#addVertex

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGL2PEXVertexArray::addVertex(const GLfloat x, const GLfloat
    #      y)
    self.uglySide.call(
        'ritual_ZN22QOpenGL2PEXVertexArray9addVertexEff', x, y,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#clear
    """
    #  void QOpenGL2PEXVertexArray::clear()
    self.uglySide.call('ritual_ZN22QOpenGL2PEXVertexArray5clearEv')

  def data(self) -> Optional[QOpenGLPoint]:
    """
    Calls Qt's 'QOpenGLPoint *QOpenGL2PEXVertexArray::data()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#data

    Returns
    -------

    Optional[QOpenGLPoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLPoint *QOpenGL2PEXVertexArray::data()
    address = self.uglySide.call('ritual_ZN22QOpenGL2PEXVertexArray4dataEv')
    from . import QOpenGLPoint
    return QOpenGLPoint._cuteAt(address)

  @overload(float, float)
  def lineToArray(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::lineToArray(const GLfloat x,
    const GLfloat y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#lineToArray

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QOpenGL2PEXVertexArray::lineToArray(const GLfloat x, const
    #      GLfloat y)
    self.uglySide.call(
        'ritual_ZN22QOpenGL2PEXVertexArray11lineToArrayEff', x, y,
    )

  @overload(int)
  def addClosingLine(self, index: int) -> None:
    """
    Calls Qt's 'void QOpenGL2PEXVertexArray::addClosingLine(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2pexvertexarray.html#addClosingLine

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QOpenGL2PEXVertexArray::addClosingLine(int index)
    self.uglySide.call(
        'ritual_ZN22QOpenGL2PEXVertexArray14addClosingLineEi', index,
    )

  @staticmethod
  def addCentroid(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PEXVertexArray::addCentroid(const QVectorPath &path,
    int subPathIndex)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PEXVertexArray.addCentroid' has no cute function yet. "
        "Qt's 'void QOpenGL2PEXVertexArray::addCentroid(const QVectorPath "
        "&path, int subPathIndex)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def addPath(*__, **_) -> Never:
    """
    Qt's 'void QOpenGL2PEXVertexArray::addPath(const QVectorPath &path,
    GLfloat curveInverseScale, bool outline)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGL2PEXVertexArray.addPath' has no cute function yet. Qt's "
        "'void QOpenGL2PEXVertexArray::addPath(const QVectorPath &path, "
        "GLfloat curveInverseScale, bool outline)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def stops(*__, **_) -> Never:
    """
    Qt's 'int *QOpenGL2PEXVertexArray::stops() const': takes or gives a type
    that cannot be passed yet: int *.
    """
    raise NotImplementedError(
        "'QOpenGL2PEXVertexArray.stops' has no cute function yet. Qt's 'int "
        "*QOpenGL2PEXVertexArray::stops() const': takes or gives a type "
        "that cannot be passed yet: int *.")
