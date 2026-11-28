"""
QOpenGLSharedResourceGuard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLSharedResourceGuard to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QOpenGLSharedResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLSharedResourceGuard(QOpenGLSharedResource):
  """
  The cute side of Qt's QOpenGLSharedResourceGuard: a plain Python object
  standing in front of one C++ QOpenGLSharedResourceGuard.

  It is built on the cute 'QOpenGLSharedResource', as Qt's
  QOpenGLSharedResourceGuard is built on Qt's QOpenGLSharedResource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLSharedResourceGuard that has a ritual and
  that Python can call so far, 3 names in all: 'id', 'invalidateResource',
  'freeResource'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpenGLSharedResourceGuard::QOpenGLSharedResourceGuard(QOpenGLContext
    *context, GLuint id, FreeResourceFunc func)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QOpenGLSharedResourceGuard::~QOpenGLSharedResourceGuard()': the
    destructor: Python never removes a C++ QOpenGLSharedResourceGuard.

  What to expect
  --------------

  - The C++ QOpenGLSharedResourceGuard is created at the first use, not by
    'QOpenGLSharedResourceGuard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLSharedResourceGuard.
  - Each name of Qt's QOpenGLSharedResourceGuard that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLSharedResourceGuard'

  #  A C++ QOpenGLSharedResourceGuard Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLSharedResourceGuard'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLSharedResourceGuard::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglsharedresourceguard.html#id
    """
    #  GLuint QOpenGLSharedResourceGuard::id() const
    return self.uglySide.call('ritual_ZNK26QOpenGLSharedResourceGuard2idEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QOpenGLSharedResourceGuard::QOpenGLSharedResourceGuard(QOpenGLContext
    *context, GLuint id, FreeResourceFunc func)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpenGLSharedResourceGuard.__init__' has no cute function yet. "
        "Qt's "
        "'QOpenGLSharedResourceGuard::QOpenGLSharedResourceGuard(QOpenGLCont"
        "ext *context, GLuint id, FreeResourceFunc func)': takes a type "
        "Python has no way to hand over yet.")

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

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGLSharedResourceGuard::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglsharedresourceguard.html#invalidateResource
    """
    #  void QOpenGLSharedResourceGuard::invalidateResource()
    ritual = 'ritual_ZN26QOpenGLSharedResourceGuard18invalidateResourceEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QOpenGLSharedResourceGuard18invalidateResourceEv')
    self.uglySide.call(ritual)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLSharedResourceGuard::freeResource(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglsharedresourceguard.html#freeResource

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLSharedResourceGuard::freeResource(QOpenGLContext *context)
    ritual = (
        'ritual_ZN26QOpenGLSharedResourceGuard12freeResourceEP14QOpenGLCont'
        'ext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QOpenGLSharedResourceGuard12freeResourceEP14QOpen'
          'GLContext')
    self.uglySide.call(ritual, self._addressOf(context))
