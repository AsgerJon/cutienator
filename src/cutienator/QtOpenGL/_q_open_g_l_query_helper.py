"""
QOpenGLQueryHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglqueryhelper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLQueryHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QOpenGLQueryHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLQueryHelper: a plain Python object standing in
  front of one C++ QOpenGLQueryHelper.

  C++ hands a QOpenGLQueryHelper around as a copy, so every C++
  QOpenGLQueryHelper behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLQueryHelper that has a ritual and that Python
  can call so far, 4 names in all: 'glEndQuery', 'glBeginQuery', 'glIsQuery',
  'glQueryCounter'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpenGLQueryHelper::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glGetQueryiv(GLenum target, GLenum pname,
    GLint *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
  - Qt's 'void QOpenGLQueryHelper::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glGetInteger64v(GLenum pname, GLint64
    *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glGetQueryObjectui64v(GLuint id, GLenum
    pname, GLuint64 *params)': takes a number to change where it is.
  - Qt's 'void QOpenGLQueryHelper::glGetQueryObjecti64v(GLuint id, GLenum
    pname, GLint64 *params)': takes a number to change where it is.
  - Qt's 'QOpenGLQueryHelper::~QOpenGLQueryHelper()': the destructor: Python
    removes its C++ QOpenGLQueryHelper by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLQueryHelper is created at the first use, not by
    'QOpenGLQueryHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLQueryHelper back gives a copy the ritual made
    for Python, in a new cute QOpenGLQueryHelper.
  - Each name of Qt's QOpenGLQueryHelper that has no cute function yet,
    'glDeleteQueries', 'glGenQueries', 'glGetInteger64v',
    'glGetQueryObjecti64v', 'glGetQueryObjectiv', 'glGetQueryObjectui64v',
    'glGetQueryObjectuiv', 'glGetQueryiv', holds a function that raises
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
  __qt_class__ = 'QOpenGLQueryHelper'

  #  Qt's '~QOpenGLQueryHelper()'. Naming it makes this a value class: Python
  #  owns every C++ QOpenGLQueryHelper behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QOpenGLQueryHelperD1Ev'

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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLQueryHelper::QOpenGLQueryHelper(QOpenGLContext *context)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglqueryhelper.html#QOpenGLQueryHelper

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLQueryHelper::QOpenGLQueryHelper(QOpenGLContext *context)
    self._noteCreation(QOpenGLQueryHelper, lambda: Rituals.call(
        'ritual_ZN18QOpenGLQueryHelperC1EP14QOpenGLContext',
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

  @overload(int)
  def glEndQuery(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLQueryHelper::glEndQuery(GLenum target)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglqueryhelper.html#glEndQuery

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLQueryHelper::glEndQuery(GLenum target)
    self.uglySide.call('ritual_ZN18QOpenGLQueryHelper10glEndQueryEj', target)

  @overload(int, int)
  def glBeginQuery(self, target: int, id: int) -> None:
    """
    Calls Qt's 'void QOpenGLQueryHelper::glBeginQuery(GLenum target, GLuint
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglqueryhelper.html#glBeginQuery

    Parameters
    ----------

    target : int
      Passed on as it is.

    id : int
      Passed on as it is.
    """
    #  void QOpenGLQueryHelper::glBeginQuery(GLenum target, GLuint id)
    self.uglySide.call(
        'ritual_ZN18QOpenGLQueryHelper12glBeginQueryEjj', target, id,
    )

  @overload(int)
  def glIsQuery(self, id: int) -> int:
    """
    Calls Qt's 'GLboolean QOpenGLQueryHelper::glIsQuery(GLuint id)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglqueryhelper.html#glIsQuery

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  GLboolean QOpenGLQueryHelper::glIsQuery(GLuint id)
    return self.uglySide.call(
        'ritual_ZN18QOpenGLQueryHelper9glIsQueryEj', id,
    )

  @overload(int, int)
  def glQueryCounter(self, id: int, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLQueryHelper::glQueryCounter(GLuint id, GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglqueryhelper.html#glQueryCounter

    Parameters
    ----------

    id : int
      Passed on as it is.

    target : int
      Passed on as it is.
    """
    #  void QOpenGLQueryHelper::glQueryCounter(GLuint id, GLenum target)
    self.uglySide.call(
        'ritual_ZN18QOpenGLQueryHelper14glQueryCounterEjj', id, target,
    )

  @staticmethod
  def glDeleteQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glDeleteQueries(GLsizei n, const GLuint
    *ids)': names 'GLuint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glDeleteQueries' has no cute function yet. "
        "Qt's 'void QOpenGLQueryHelper::glDeleteQueries(GLsizei n, const "
        "GLuint *ids)': names 'GLuint', which has no cute class yet.")

  @staticmethod
  def glGenQueries(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGenQueries(GLsizei n, GLuint *ids)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGenQueries' has no cute function yet. Qt's "
        "'void QOpenGLQueryHelper::glGenQueries(GLsizei n, GLuint *ids)': "
        "takes a number to change where it is.")

  @staticmethod
  def glGetInteger64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetInteger64v(GLenum pname, GLint64
    *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetInteger64v' has no cute function yet. "
        "Qt's 'void QOpenGLQueryHelper::glGetInteger64v(GLenum pname, "
        "GLint64 *params)': takes a number to change where it is.")

  @staticmethod
  def glGetQueryObjecti64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetQueryObjecti64v(GLuint id, GLenum
    pname, GLint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetQueryObjecti64v' has no cute function "
        "yet. Qt's 'void QOpenGLQueryHelper::glGetQueryObjecti64v(GLuint "
        "id, GLenum pname, GLint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryObjectiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetQueryObjectiv(GLuint id, GLenum
    pname, GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetQueryObjectiv' has no cute function yet. "
        "Qt's 'void QOpenGLQueryHelper::glGetQueryObjectiv(GLuint id, "
        "GLenum pname, GLint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryObjectui64v(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetQueryObjectui64v(GLuint id, GLenum
    pname, GLuint64 *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetQueryObjectui64v' has no cute function "
        "yet. Qt's 'void QOpenGLQueryHelper::glGetQueryObjectui64v(GLuint "
        "id, GLenum pname, GLuint64 *params)': takes a number to change "
        "where it is.")

  @staticmethod
  def glGetQueryObjectuiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetQueryObjectuiv(GLuint id, GLenum
    pname, GLuint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetQueryObjectuiv' has no cute function yet. "
        "Qt's 'void QOpenGLQueryHelper::glGetQueryObjectuiv(GLuint id, "
        "GLenum pname, GLuint *params)': takes a number to change where it "
        "is.")

  @staticmethod
  def glGetQueryiv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLQueryHelper::glGetQueryiv(GLenum target, GLenum pname,
    GLint *params)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QOpenGLQueryHelper.glGetQueryiv' has no cute function yet. Qt's "
        "'void QOpenGLQueryHelper::glGetQueryiv(GLenum target, GLenum "
        "pname, GLint *params)': takes a number to change where it is.")
