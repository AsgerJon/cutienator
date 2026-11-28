"""
QOpenGLProgramBinarySupportCheck binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLProgramBinarySupportCheck to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QOpenGLSharedResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLProgramBinarySupportCheck(QOpenGLSharedResource):
  """
  The cute side of Qt's QOpenGLProgramBinarySupportCheck: a plain Python
  object standing in front of one C++ QOpenGLProgramBinarySupportCheck.

  It is built on the cute 'QOpenGLSharedResource', as Qt's
  QOpenGLProgramBinarySupportCheck is built on Qt's QOpenGLSharedResource,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLProgramBinarySupportCheck that has a ritual
  and that Python can call so far, 3 names in all: 'invalidateResource',
  'freeResource', 'isSupported'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QOpenGLProgramBinarySupportCheck is created at the first use, not
    by 'QOpenGLProgramBinarySupportCheck(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLProgramBinarySupportCheck.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLProgramBinarySupportCheck'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSupported(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLProgramBinarySupportCheck::isSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarysupportcheck.html#isSupported
    """
    #  bool QOpenGLProgramBinarySupportCheck::isSupported() const
    return self.uglySide.call(
        'ritual_ZNK32QOpenGLProgramBinarySupportCheck11isSupportedEv',
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
    'QOpenGLProgramBinarySupportCheck::QOpenGLProgramBinarySupportCheck(
    QOpenGLContext *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarysupportcheck.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLProgramBinarySupportCheck::
    #      QOpenGLProgramBinarySupportCheck(QOpenGLContext *context)
    self._noteCreation(
        QOpenGLProgramBinarySupportCheck, lambda: Rituals.call(
            'ritual_ZN32QOpenGLProgramBinarySupportCheckC1EP14QOpenGLContex'
            't',
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

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGLProgramBinarySupportCheck::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarysupportcheck.html
    """
    #  void QOpenGLProgramBinarySupportCheck::invalidateResource()
    ritual = (
        'ritual_ZN32QOpenGLProgramBinarySupportCheck18invalidateResourceEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QOpenGLProgramBinarySupportCheck18invalidateResou'
          'rceEv')
    self.uglySide.call(ritual)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, a0: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void
    QOpenGLProgramBinarySupportCheck::freeResource(QOpenGLContext *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglprogrambinarysupportcheck.html#freeResource

    Parameters
    ----------

    a0 : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLProgramBinarySupportCheck::freeResource(QOpenGLContext
    #      *a0)
    ritual = (
        'ritual_ZN32QOpenGLProgramBinarySupportCheck12freeResourceEP14QOpen'
        'GLContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QOpenGLProgramBinarySupportCheck12freeResourceEP1'
          '4QOpenGLContext')
    self.uglySide.call(ritual, self._addressOf(a0))
