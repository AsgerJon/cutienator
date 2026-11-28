"""
QOpenGLVersionFunctionsStorage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpenGLVersionFunctionsStorage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVersionFunctionsStorage: a plain Python object
  standing in front of one C++ QOpenGLVersionFunctionsStorage.

  C++ hands a QOpenGLVersionFunctionsStorage around as a copy, so every C++
  QOpenGLVersionFunctionsStorage behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QOpenGLVersionFunctionsStorage yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLVersionFunctionsStorage::~QOpenGLVersionFunctionsStorage()':
    the destructor: Python removes its C++ QOpenGLVersionFunctionsStorage by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on
  'QOpenGLFunctions_1_0_CoreBackend.

  What to expect
  --------------

  - The C++ QOpenGLVersionFunctionsStorage is created at the first use, not
    by 'QOpenGLVersionFunctionsStorage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLVersionFunctionsStorage back gives a copy the
    ritual made for Python, in a new cute QOpenGLVersionFunctionsStorage.
  - Each name of Qt's QOpenGLVersionFunctionsStorage that has no cute
    function yet, 'backend', holds a function that raises
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
  __qt_class__ = 'QOpenGLVersionFunctionsStorage'

  #  Qt's '~QOpenGLVersionFunctionsStorage()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLVersionFunctionsStorage behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QOpenGLVersionFunctionsStorageD1Ev'

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
    'QOpenGLVersionFunctionsStorage::QOpenGLVersionFunctionsStorage()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionfunctionsstorage.html
    """
    #  QOpenGLVersionFunctionsStorage::QOpenGLVersionFunctionsStorage()
    self._noteCreation(QOpenGLVersionFunctionsStorage, lambda: Rituals.call(
        'ritual_ZN30QOpenGLVersionFunctionsStorageC1Ev',
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
  def backend(*__, **_) -> Never:
    """
    Qt's 'QOpenGLVersionFunctionsBackend
    *QOpenGLVersionFunctionsStorage::backend(QOpenGLContext *context,
    QOpenGLVersionFunctionsBackend::Version v)': leans on
    'QOpenGLFunctions_1_0_CoreBackend::init()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOpenGLVersionFunctionsStorage.backend' has no cute function yet. "
        "Qt's 'QOpenGLVersionFunctionsBackend "
        "*QOpenGLVersionFunctionsStorage::backend(QOpenGLContext *context, "
        "QOpenGLVersionFunctionsBackend::Version v)': leans on "
        "'QOpenGLFunctions_1_0_CoreBackend::init()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
