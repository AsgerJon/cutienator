"""
QOpenGLVertexArrayObjectHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglvertexarrayobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLVertexArrayObjectHelper to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLVertexArrayObjectHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVertexArrayObjectHelper: a plain Python object
  standing in front of one C++ QOpenGLVertexArrayObjectHelper.

  What exists
  -----------

  Every function of Qt's QOpenGLVertexArrayObjectHelper that has a ritual and
  that Python can call so far, 5 names in all: 'initializeFromContext',
  'vertexArrayObjectHelperForContext', 'isValid', 'glBindVertexArray',
  'glIsVertexArray'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpenGLVertexArrayObjectHelper::glGenVertexArrays(GLsizei n,
    GLuint *arrays) const': takes a number to change where it is.
  - Qt's 'void QOpenGLVertexArrayObjectHelper::glDeleteVertexArrays(GLsizei
    n, const GLuint *arrays) const': names 'GLuint', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLVertexArrayObjectHelper is created at the first use, not
    by 'QOpenGLVertexArrayObjectHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLVertexArrayObjectHelper.
  - Each name of Qt's QOpenGLVertexArrayObjectHelper that has no cute
    function yet, 'glDeleteVertexArrays', 'glGenVertexArrays', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def vertexArrayObjectHelperForContext(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLVertexArrayObjectHelper]:
    """
    Calls Qt's 'QOpenGLVertexArrayObjectHelper
    *QOpenGLVertexArrayObjectHelper::vertexArrayObjectHelperForContext(
    QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLVertexArrayObjectHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLVertexArrayObjectHelper *QOpenGLVertexArrayObjectHelper::
    #      vertexArrayObjectHelperForContext(QOpenGLContext *context)
    address = Rituals.call(
        'ritual_ZN30QOpenGLVertexArrayObjectHelper33vertexArrayObjectHelper'
        'ForContextEP14QOpenGLContext',
        CuteMixin._addressOf(context),
    )
    return QOpenGLVertexArrayObjectHelper._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVertexArrayObjectHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVertexArrayObjectHelper::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html#isValid
    """
    #  bool QOpenGLVertexArrayObjectHelper::isValid() const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLVertexArrayObjectHelper7isValidEv',
    )

  @overload(int)
  def glIsVertexArray(self, array: int) -> int:
    """
    Calls Qt's 'GLboolean
    QOpenGLVertexArrayObjectHelper::glIsVertexArray(GLuint array) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLVertexArrayObjectHelper::glIsVertexArray(GLuint
    #      array) const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLVertexArrayObjectHelper15glIsVertexArrayEj',
        array,
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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVertexArrayObjectHelper::QOpenGLVertexArrayObjectHelper(
    QOpenGLContext *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLVertexArrayObjectHelper::QOpenGLVertexArrayObjectHelper(
    #      QOpenGLContext *context)
    self._noteCreation(QOpenGLVertexArrayObjectHelper, lambda: Rituals.call(
        'ritual_ZN30QOpenGLVertexArrayObjectHelperC1EP14QOpenGLContext',
        self._addressOf(context),
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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def initializeFromContext(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void
    QOpenGLVertexArrayObjectHelper::initializeFromContext(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLVertexArrayObjectHelper::initializeFromContext(
    #      QOpenGLContext *context)
    self.uglySide.call(
        'ritual_ZN30QOpenGLVertexArrayObjectHelper21initializeFromContextEP'
        '14QOpenGLContext',
        self._addressOf(context),
    )

  @overload(int)
  def glBindVertexArray(self, array: int) -> None:
    """
    Calls Qt's 'void QOpenGLVertexArrayObjectHelper::glBindVertexArray(GLuint
    array) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobjecthelper.html

    Parameters
    ----------

    array : int
      Passed on as it is.
    """
    #  void QOpenGLVertexArrayObjectHelper::glBindVertexArray(GLuint array)
    #      const
    self.uglySide.call(
        'ritual_ZNK30QOpenGLVertexArrayObjectHelper17glBindVertexArrayEj',
        array,
    )

  @staticmethod
  def glDeleteVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLVertexArrayObjectHelper::glDeleteVertexArrays(GLsizei
    n, const GLuint *arrays) const': names 'GLuint', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLVertexArrayObjectHelper.glDeleteVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLVertexArrayObjectHelper::glDeleteVertexArrays(GLsizei n, "
        "const GLuint *arrays) const': names 'GLuint', which has no cute "
        "class yet.")

  @staticmethod
  def glGenVertexArrays(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLVertexArrayObjectHelper::glGenVertexArrays(GLsizei n,
    GLuint *arrays) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLVertexArrayObjectHelper.glGenVertexArrays' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLVertexArrayObjectHelper::glGenVertexArrays(GLsizei n, "
        "GLuint *arrays) const': takes a number to change where it is.")
