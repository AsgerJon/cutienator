"""
QOpenGLFunctions_4_2_CoreBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpenGLVersionFunctionsBackend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLFunctions_4_2_CoreBackend(QOpenGLVersionFunctionsBackend):
  """
  The cute side of Qt's QOpenGLFunctions_4_2_CoreBackend: a plain Python
  object standing in front of one C++ QOpenGLFunctions_4_2_CoreBackend.

  It is built on the cute 'QOpenGLVersionFunctionsBackend', as Qt's
  QOpenGLFunctions_4_2_CoreBackend is built on Qt's
  QOpenGLVersionFunctionsBackend, and has everything that class has.

  C++ hands a QOpenGLFunctions_4_2_CoreBackend around as a copy, so every C++
  QOpenGLFunctions_4_2_CoreBackend behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_4_2_CoreBackend that has a ritual
  and that Python can call so far, 1 name in all: 'versionStatus'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpenGLFunctions_4_2_CoreBackend::~QOpenGLFunctions_4_2_CoreBackend()':
    the destructor: Python removes its C++ QOpenGLFunctions_4_2_CoreBackend
    by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QOpenGLFunctions_4_2_CoreBackend.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_4_2_CoreBackend is created at the first use, not
    by 'QOpenGLFunctions_4_2_CoreBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFunctions_4_2_CoreBackend back gives a copy
    the ritual made for Python, in a new cute
    QOpenGLFunctions_4_2_CoreBackend.
  - Each name of Qt's QOpenGLFunctions_4_2_CoreBackend that has no cute
    function yet, '__init__', 'init', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QOpenGLFunctions_4_2_CoreBackend, each a
  #  class in here as in C++.

  class Functions(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLFunctions_4_2_CoreBackend::Functions: a
    plain Python object standing in front of one C++
    QOpenGLFunctions_4_2_CoreBackend::Functions.

    C++ hands a QOpenGLFunctions_4_2_CoreBackend::Functions around as a copy,
    so every C++ QOpenGLFunctions_4_2_CoreBackend::Functions behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QOpenGLFunctions_4_2_CoreBackend::Functions yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLFunctions_4_2_CoreBackend::Functions::~Functions()': the
      destructor: Python removes its C++
      QOpenGLFunctions_4_2_CoreBackend::Functions by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QOpenGLFunctions_4_2_CoreBackend::Functions is created at the
      first use, not by 'QOpenGLFunctions_4_2_CoreBackend::Functions(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLFunctions_4_2_CoreBackend::Functions back
      gives a copy the ritual made for Python, in a new cute
      QOpenGLFunctions_4_2_CoreBackend::Functions.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLFunctions_4_2_CoreBackend::Functions'

    #  Qt's '~QOpenGLFunctions_4_2_CoreBackend::Functions()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QOpenGLFunctions_4_2_CoreBackend::Functions behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN32QOpenGLFunctions_4_2_CoreBackend9FunctionsD1Ev')

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

  @staticmethod
  def versionStatus() -> QOpenGLVersionFunctionsBackend.Version:
    """
    Calls Qt's 'Version QOpenGLFunctions_4_2_CoreBackend::versionStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_4_2_corebackend.html

    Returns
    -------

    QOpenGLVersionFunctionsBackend.Version
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLVersionFunctionsBackend.Version(number)' gives.
    """
    #  Version QOpenGLFunctions_4_2_CoreBackend::versionStatus()
    return QOpenGLVersionFunctionsBackend.Version(Rituals.call(
        'ritual_ZN32QOpenGLFunctions_4_2_CoreBackend13versionStatusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_4_2_CoreBackend'

  #  Qt's '~QOpenGLFunctions_4_2_CoreBackend()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLFunctions_4_2_CoreBackend behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QOpenGLFunctions_4_2_CoreBackendD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QOpenGLFunctions_4_2_CoreBackend::QOpenGLFunctions_4_2_CoreBackend(
    QOpenGLContext *c)': leans on 'QOpenGLFunctions_4_2_CoreBackend::init()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_2_CoreBackend.__init__' has no cute function "
        "yet. Qt's "
        "'QOpenGLFunctions_4_2_CoreBackend::QOpenGLFunctions_4_2_CoreBackend"
        "(QOpenGLContext *c)': leans on "
        "'QOpenGLFunctions_4_2_CoreBackend::init()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def init(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFunctions_4_2_CoreBackend::init()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: expected '(' for function-style cast or type construction.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_4_2_CoreBackend.init' has no cute function yet. "
        "Qt's 'void QOpenGLFunctions_4_2_CoreBackend::init()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: expected '(' for function-style cast or type "
        "construction.")
