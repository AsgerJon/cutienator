"""
QOpenGLContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLContextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QOpenGLContext, QPlatformOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QOpenGLContext = WAIT['QOpenGLContext']
  QPlatformOpenGLContext = WAIT['QPlatformOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLContextPrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpenGLContextPrivate: a plain Python object standing
  in front of one C++ QOpenGLContextPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QOpenGLContextPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLContextPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'adopt',
  'setCurrentContext', 'maxTextureSize', 'get', 'toggleMakeCurrentTracker',
  'cleanMakeCurrentTracker', '_q_screenDestroyed'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLContext *QOpenGLContextPrivate::q_func() const': takes
    in Python what 'QOpenGLContext *QOpenGLContextPrivate::q_func()' takes.
  - Qt's 'QOpenGLContextPrivate::~QOpenGLContextPrivate()': the destructor:
    Python never removes a C++ QOpenGLContextPrivate.

  What to expect
  --------------

  - The C++ QOpenGLContextPrivate is created at the first use, not by
    'QOpenGLContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLContextPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def setCurrentContext(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext
    *QOpenGLContextPrivate::setCurrentContext(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html#setCurrentContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext
    #      *QOpenGLContextPrivate::setCurrentContext(QOpenGLContext *context)
    address = Rituals.call(
        'ritual_ZN21QOpenGLContextPrivate17setCurrentContextEP14QOpenGLCont'
        'ext',
        CuteMixin._addressOf(context),
    )
    from . import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def get(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLContextPrivate]:
    """
    Calls Qt's 'QOpenGLContextPrivate
    *QOpenGLContextPrivate::get(QOpenGLContext *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontextprivate.html#get

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextPrivate *QOpenGLContextPrivate::get(QOpenGLContext
    #      *context)
    address = Rituals.call(
        'ritual_ZN21QOpenGLContextPrivate3getEP14QOpenGLContext',
        CuteMixin._addressOf(context),
    )
    return QOpenGLContextPrivate._cuteAt(address)

  @staticmethod
  @overload(QOpenGLContext, bool)
  @overload(NoneType, bool)
  def toggleMakeCurrentTracker(
      context: Optional[QOpenGLContext],
      value: bool,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLContextPrivate::toggleMakeCurrentTracker(QOpenGLContext *context,
    bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : bool
      Passed on as it is.
    """
    #  bool QOpenGLContextPrivate::toggleMakeCurrentTracker(QOpenGLContext
    #      *context, bool value)
    return Rituals.call(
        'ritual_ZN21QOpenGLContextPrivate24toggleMakeCurrentTrackerEP14QOpe'
        'nGLContextb',
        CuteMixin._addressOf(context), value,
    )

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def cleanMakeCurrentTracker(context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void
    QOpenGLContextPrivate::cleanMakeCurrentTracker(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html#cleanMakeCurrentTracker

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextPrivate::cleanMakeCurrentTracker(QOpenGLContext
    #      *context)
    Rituals.call(
        'ritual_ZN21QOpenGLContextPrivate23cleanMakeCurrentTrackerEP14QOpen'
        'GLContext',
        CuteMixin._addressOf(context),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLContextPrivate'

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
    'QOpenGLContextPrivate::QOpenGLContextPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html#QOpenGLContextPrivate
    """
    #  QOpenGLContextPrivate::QOpenGLContextPrivate()
    self._noteCreation(QOpenGLContextPrivate, lambda: Rituals.call(
        'ritual_ZN21QOpenGLContextPrivateC1Ev',
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

  def q_func(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLContextPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontextprivate.html#q_func

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLContextPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QOpenGLContextPrivate6q_funcEv')
    from . import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  @overload(QPlatformOpenGLContext)
  @overload(NoneType)
  def adopt(self, a0: Optional[QPlatformOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLContextPrivate::adopt(QPlatformOpenGLContext
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontextprivate.html#adopt

    Parameters
    ----------

    a0 : Optional[QPlatformOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextPrivate::adopt(QPlatformOpenGLContext *a0)
    self.uglySide.call(
        'ritual_ZN21QOpenGLContextPrivate5adoptEP22QPlatformOpenGLContext',
        self._addressOf(a0),
    )

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int QOpenGLContextPrivate::maxTextureSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html#maxTextureSize
    """
    #  int QOpenGLContextPrivate::maxTextureSize()
    return self.uglySide.call(
        'ritual_ZN21QOpenGLContextPrivate14maxTextureSizeEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def _q_screenDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QOpenGLContextPrivate::_q_screenDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextprivate.html#_q_screenDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContextPrivate::_q_screenDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN21QOpenGLContextPrivate18_q_screenDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )
