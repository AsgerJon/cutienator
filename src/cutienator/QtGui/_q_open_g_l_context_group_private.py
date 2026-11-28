"""
QOpenGLContextGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLContextGroupPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext, QOpenGLContextGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLContextGroupPrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpenGLContextGroupPrivate: a plain Python object
  standing in front of one C++ QOpenGLContextGroupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QOpenGLContextGroupPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLContextGroupPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'addContext',
  'removeContext', 'cleanup', 'deletePendingResources'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLContextGroup *QOpenGLContextGroupPrivate::q_func()
    const': takes in Python what 'QOpenGLContextGroup
    *QOpenGLContextGroupPrivate::q_func()' takes.
  - Qt's 'QOpenGLContextGroupPrivate::~QOpenGLContextGroupPrivate()': the
    destructor: Python never removes a C++ QOpenGLContextGroupPrivate.

  What to expect
  --------------

  - The C++ QOpenGLContextGroupPrivate is created at the first use, not by
    'QOpenGLContextGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLContextGroupPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLContextGroupPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLContextGroupPrivate::QOpenGLContextGroupPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html
    """
    #  QOpenGLContextGroupPrivate::QOpenGLContextGroupPrivate()
    self._noteCreation(QOpenGLContextGroupPrivate, lambda: Rituals.call(
        'ritual_ZN26QOpenGLContextGroupPrivateC1Ev',
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

  def q_func(self) -> Optional[QOpenGLContextGroup]:
    """
    Calls Qt's 'QOpenGLContextGroup *QOpenGLContextGroupPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html#q_func

    Returns
    -------

    Optional[QOpenGLContextGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextGroup *QOpenGLContextGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLContextGroupPrivate6q_funcEv',
    )
    from . import QOpenGLContextGroup
    return QOpenGLContextGroup._cuteAt(address)

  @overload(QOpenGLContext)
  @overload(NoneType)
  def addContext(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLContextGroupPrivate::addContext(QOpenGLContext
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html#addContext

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextGroupPrivate::addContext(QOpenGLContext *ctx)
    self.uglySide.call(
        'ritual_ZN26QOpenGLContextGroupPrivate10addContextEP14QOpenGLContex'
        't',
        self._addressOf(ctx),
    )

  @overload(QOpenGLContext)
  @overload(NoneType)
  def removeContext(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLContextGroupPrivate::removeContext(QOpenGLContext
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html#removeContext

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextGroupPrivate::removeContext(QOpenGLContext *ctx)
    self.uglySide.call(
        'ritual_ZN26QOpenGLContextGroupPrivate13removeContextEP14QOpenGLCon'
        'text',
        self._addressOf(ctx),
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QOpenGLContextGroupPrivate::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html#cleanup
    """
    #  void QOpenGLContextGroupPrivate::cleanup()
    self.uglySide.call('ritual_ZN26QOpenGLContextGroupPrivate7cleanupEv')

  @overload(QOpenGLContext)
  @overload(NoneType)
  def deletePendingResources(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void
    QOpenGLContextGroupPrivate::deletePendingResources(QOpenGLContext *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroupprivate.html

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextGroupPrivate::deletePendingResources(QOpenGLContext
    #      *ctx)
    self.uglySide.call(
        'ritual_ZN26QOpenGLContextGroupPrivate22deletePendingResourcesEP14Q'
        'OpenGLContext',
        self._addressOf(ctx),
    )
