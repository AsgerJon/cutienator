"""
QOpenGLFunctions_1_3_DeprecatedBackend binding of the Qt C++
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


class QOpenGLFunctions_1_3_DeprecatedBackend(QOpenGLVersionFunctionsBackend):
  """
  The cute side of Qt's QOpenGLFunctions_1_3_DeprecatedBackend: a plain
  Python object standing in front of one C++
  QOpenGLFunctions_1_3_DeprecatedBackend.

  It is built on the cute 'QOpenGLVersionFunctionsBackend', as Qt's
  QOpenGLFunctions_1_3_DeprecatedBackend is built on Qt's
  QOpenGLVersionFunctionsBackend, and has everything that class has.

  C++ hands a QOpenGLFunctions_1_3_DeprecatedBackend around as a copy, so
  every C++ QOpenGLFunctions_1_3_DeprecatedBackend behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFunctions_1_3_DeprecatedBackend that has a
  ritual and that Python can call so far, 1 name in all: 'versionStatus'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFunctions_1_3_DeprecatedBackend::
    ~QOpenGLFunctions_1_3_DeprecatedBackend()': the destructor: Python
    removes its C++ QOpenGLFunctions_1_3_DeprecatedBackend by it, and has no
    other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QOpenGLFunctions_1_3_DeprecatedBackend.

  What to expect
  --------------

  - The C++ QOpenGLFunctions_1_3_DeprecatedBackend is created at the first
    use, not by 'QOpenGLFunctions_1_3_DeprecatedBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFunctions_1_3_DeprecatedBackend back gives a
    copy the ritual made for Python, in a new cute
    QOpenGLFunctions_1_3_DeprecatedBackend.
  - Each name of Qt's QOpenGLFunctions_1_3_DeprecatedBackend that has no cute
    function yet, '__init__', 'init', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QOpenGLFunctions_1_3_DeprecatedBackend,
  #  each a class in here as in C++.

  class Functions(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLFunctions_1_3_DeprecatedBackend::Functions:
    a plain Python object standing in front of one C++
    QOpenGLFunctions_1_3_DeprecatedBackend::Functions.

    C++ hands a QOpenGLFunctions_1_3_DeprecatedBackend::Functions around as a
    copy, so every C++ QOpenGLFunctions_1_3_DeprecatedBackend::Functions
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QOpenGLFunctions_1_3_DeprecatedBackend::Functions
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLFunctions_1_3_DeprecatedBackend::Functions::~Functions()':
      the destructor: Python removes its C++
      QOpenGLFunctions_1_3_DeprecatedBackend::Functions by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QOpenGLFunctions_1_3_DeprecatedBackend::Functions is created at
      the first use, not by
      'QOpenGLFunctions_1_3_DeprecatedBackend::Functions(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLFunctions_1_3_DeprecatedBackend::Functions
      back gives a copy the ritual made for Python, in a new cute
      QOpenGLFunctions_1_3_DeprecatedBackend::Functions.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLFunctions_1_3_DeprecatedBackend::Functions'

    #  Qt's '~QOpenGLFunctions_1_3_DeprecatedBackend::Functions()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QOpenGLFunctions_1_3_DeprecatedBackend::Functions behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN38QOpenGLFunctions_1_3_DeprecatedBackend9FunctionsD1Ev')

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
    Calls Qt's 'Version
    QOpenGLFunctions_1_3_DeprecatedBackend::versionStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglfunctions_1_3_deprecatedbackend.html

    Returns
    -------

    QOpenGLVersionFunctionsBackend.Version
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLVersionFunctionsBackend.Version(number)' gives.
    """
    #  Version QOpenGLFunctions_1_3_DeprecatedBackend::versionStatus()
    return QOpenGLVersionFunctionsBackend.Version(Rituals.call(
        'ritual_ZN38QOpenGLFunctions_1_3_DeprecatedBackend13versionStatusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFunctions_1_3_DeprecatedBackend'

  #  Qt's '~QOpenGLFunctions_1_3_DeprecatedBackend()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QOpenGLFunctions_1_3_DeprecatedBackend behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN38QOpenGLFunctions_1_3_DeprecatedBackendD1Ev'

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
    Qt's 'QOpenGLFunctions_1_3_DeprecatedBackend::
    QOpenGLFunctions_1_3_DeprecatedBackend(QOpenGLContext *c)': leans on
    'QOpenGLFunctions_1_3_DeprecatedBackend::init()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_3_DeprecatedBackend.__init__' has no cute "
        "function yet. Qt's "
        "'QOpenGLFunctions_1_3_DeprecatedBackend::QOpenGLFunctions_1_3_Depre"
        "catedBackend(QOpenGLContext *c)': leans on "
        "'QOpenGLFunctions_1_3_DeprecatedBackend::init()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Qt's 'void QOpenGLFunctions_1_3_DeprecatedBackend::init()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: expected '(' for function-style cast or type construction.
    """
    raise NotImplementedError(
        "'QOpenGLFunctions_1_3_DeprecatedBackend.init' has no cute function "
        "yet. Qt's 'void QOpenGLFunctions_1_3_DeprecatedBackend::init()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: expected '(' for function-style "
        "cast or type construction.")
