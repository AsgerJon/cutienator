"""
QNativeInterface::QEGLContext binding of the Qt C++
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


class QEGLContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::QEGLContext: a plain Python object
  standing in front of one C++ QNativeInterface::QEGLContext.

  What exists
  -----------

  Every function of Qt's QNativeInterface::QEGLContext that has a ritual and
  that Python can call so far, 1 name in all: 'invalidateContext'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::QEGLContext::~QEGLContext()': the destructor:
    Python never removes a C++ QNativeInterface::QEGLContext.
  - Qt's 'QOpenGLContext
    *QNativeInterface::QEGLContext::fromNative(EGLContext context, EGLDisplay
    display, QOpenGLContext *shareContext)': names 'void', which has no cute
    class yet.
  - Qt's 'EGLContext QNativeInterface::QEGLContext::nativeContext() const':
    gives 'void', which has no cute class yet.
  - Qt's 'EGLConfig QNativeInterface::QEGLContext::config() const': gives
    'void', which has no cute class yet.
  - Qt's 'EGLDisplay QNativeInterface::QEGLContext::display() const': gives
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QNativeInterface::QEGLContext is created at the first use, not by
    'QNativeInterface::QEGLContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::QEGLContext.
  - Each name of Qt's QNativeInterface::QEGLContext that has no cute function
    yet, 'config', 'display', 'fromNative', 'nativeContext', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::QEGLContext'

  #  A C++ QNativeInterface::QEGLContext Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_QEGLContext'

  #  The functions Qt calls itself that QNativeInterface::QEGLContext is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeContext': (
          'EGLContext QNativeInterface::QEGLContext::nativeContext() const',
      ),
      'config': (
          'EGLConfig QNativeInterface::QEGLContext::config() const',
      ),
      'display': (
          'EGLDisplay QNativeInterface::QEGLContext::display() const',
      ),
  }

  #  The functions Qt calls itself that QNativeInterface::QEGLContext is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'invalidateContext': (
          ('_ZN16QNativeInterface11QEGLContext17invalidateContextEv',
           ('nothing', 'nothing', ''),
           ()),
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
    'QNativeInterface::QEGLContext::QEGLContext()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qeglcontext.html#QEGLContext
    """
    #  QNativeInterface::QEGLContext::QEGLContext()
    self._noteCreation(QEGLContext, lambda: Rituals.call(
        'ritual_ZN16QNativeInterface11QEGLContextC1Ev',
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

  def invalidateContext(self) -> None:
    """
    Calls Qt's 'void QNativeInterface::QEGLContext::invalidateContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-qeglcontext.html
    """
    #  void QNativeInterface::QEGLContext::invalidateContext()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface11QEGLContext17invalidateContextEv',
    )

  @staticmethod
  def config(*__, **_) -> Never:
    """
    Qt's 'EGLConfig QNativeInterface::QEGLContext::config() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QEGLContext.config' has no cute function yet. "
        "Qt's 'EGLConfig QNativeInterface::QEGLContext::config() const': "
        "gives 'void', which has no cute class yet.")

  @staticmethod
  def display(*__, **_) -> Never:
    """
    Qt's 'EGLDisplay QNativeInterface::QEGLContext::display() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QEGLContext.display' has no cute function yet. "
        "Qt's 'EGLDisplay QNativeInterface::QEGLContext::display() const': "
        "gives 'void', which has no cute class yet.")

  @staticmethod
  def fromNative(*__, **_) -> Never:
    """
    Qt's 'QOpenGLContext
    *QNativeInterface::QEGLContext::fromNative(EGLContext context, EGLDisplay
    display, QOpenGLContext *shareContext)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QEGLContext.fromNative' has no cute function "
        "yet. Qt's 'QOpenGLContext "
        "*QNativeInterface::QEGLContext::fromNative(EGLContext context, "
        "EGLDisplay display, QOpenGLContext *shareContext)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def nativeContext(*__, **_) -> Never:
    """
    Qt's 'EGLContext QNativeInterface::QEGLContext::nativeContext() const':
    gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QEGLContext.nativeContext' has no cute function "
        "yet. Qt's 'EGLContext "
        "QNativeInterface::QEGLContext::nativeContext() const': gives "
        "'void', which has no cute class yet.")
