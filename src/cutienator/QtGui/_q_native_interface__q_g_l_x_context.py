"""
QNativeInterface::QGLXContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qopenglcontext_platform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGLXContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::QGLXContext: a plain Python object
  standing in front of one C++ QNativeInterface::QGLXContext.

  What exists
  -----------

  No function of Qt's QNativeInterface::QGLXContext yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::QGLXContext::~QGLXContext()': the destructor:
    Python never removes a C++ QNativeInterface::QGLXContext.
  - Qt's 'QOpenGLContext
    *QNativeInterface::QGLXContext::fromNative(GLXContext configBasedContext,
    QOpenGLContext *shareContext)': names 'struct __GLXcontextRec', which has
    no cute class yet.
  - Qt's 'QOpenGLContext
    *QNativeInterface::QGLXContext::fromNative(GLXContext visualBasedContext,
    void *visualInfo, QOpenGLContext *shareContext)': names 'struct
    __GLXcontextRec', which has no cute class yet.
  - Qt's 'GLXContext QNativeInterface::QGLXContext::nativeContext() const':
    gives 'struct __GLXcontextRec', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::QGLXContext is created at the first use, not by
    'QNativeInterface::QGLXContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::QGLXContext.
  - Each name of Qt's QNativeInterface::QGLXContext that has no cute function
    yet, 'fromNative', 'nativeContext', holds a function that raises
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
  __qt_class__ = 'QNativeInterface::QGLXContext'

  #  A C++ QNativeInterface::QGLXContext Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_QGLXContext'

  #  The functions Qt calls itself that QNativeInterface::QGLXContext is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeContext': (
          'GLXContext QNativeInterface::QGLXContext::nativeContext() const',
      ),
  }

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
    'QNativeInterface::QGLXContext::QGLXContext()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qglxcontext.html#QGLXContext
    """
    #  QNativeInterface::QGLXContext::QGLXContext()
    self._noteCreation(QGLXContext, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface11QGLXContextC1Ev',
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

  @staticmethod
  def fromNative(*__, **_) -> Never:
    """
    - Qt's 'QOpenGLContext
      *QNativeInterface::QGLXContext::fromNative(GLXContext
      configBasedContext, QOpenGLContext *shareContext)': names 'struct
      __GLXcontextRec', which has no cute class yet.
    - Qt's 'QOpenGLContext
      *QNativeInterface::QGLXContext::fromNative(GLXContext
      visualBasedContext, void *visualInfo, QOpenGLContext *shareContext)':
      names 'struct __GLXcontextRec', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QGLXContext.fromNative' has no cute function "
        "yet. Qt's 'QOpenGLContext "
        "*QNativeInterface::QGLXContext::fromNative(GLXContext "
        "configBasedContext, QOpenGLContext *shareContext)': names 'struct "
        "__GLXcontextRec', which has no cute class yet. Qt's "
        "'QOpenGLContext "
        "*QNativeInterface::QGLXContext::fromNative(GLXContext "
        "visualBasedContext, void *visualInfo, QOpenGLContext "
        "*shareContext)': names 'struct __GLXcontextRec', which has no cute "
        "class yet.")

  @staticmethod
  def nativeContext(*__, **_) -> Never:
    """
    Qt's 'GLXContext QNativeInterface::QGLXContext::nativeContext() const':
    gives 'struct __GLXcontextRec', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QGLXContext.nativeContext' has no cute function "
        "yet. Qt's 'GLXContext "
        "QNativeInterface::QGLXContext::nativeContext() const': gives "
        "'struct __GLXcontextRec', which has no cute class yet.")
