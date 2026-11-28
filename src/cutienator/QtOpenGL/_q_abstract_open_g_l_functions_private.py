"""
QAbstractOpenGLFunctionsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext
  from . import QAbstractOpenGLFunctions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractOpenGLFunctions = WAIT['QAbstractOpenGLFunctions']
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOpenGLFunctionsPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractOpenGLFunctionsPrivate: a plain Python
  object standing in front of one C++ QAbstractOpenGLFunctionsPrivate.

  C++ hands a QAbstractOpenGLFunctionsPrivate around as a copy, so every C++
  QAbstractOpenGLFunctionsPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QAbstractOpenGLFunctionsPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'insertExternalFunctions',
  'removeExternalFunctions', 'get'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QAbstractOpenGLFunctionsPrivate::~QAbstractOpenGLFunctionsPrivate()':
    the destructor: Python removes its C++ QAbstractOpenGLFunctionsPrivate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on
  'QOpenGLFunctions_1_0_CoreBackend.

  What to expect
  --------------

  - The C++ QAbstractOpenGLFunctionsPrivate is created at the first use, not
    by 'QAbstractOpenGLFunctionsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAbstractOpenGLFunctionsPrivate back gives a copy the
    ritual made for Python, in a new cute QAbstractOpenGLFunctionsPrivate.
  - Each name of Qt's QAbstractOpenGLFunctionsPrivate that has no cute
    function yet, 'functionsBackend', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext, QAbstractOpenGLFunctions)
  @overload(QOpenGLContext, NoneType)
  @overload(NoneType, QAbstractOpenGLFunctions)
  @overload(NoneType, NoneType)
  def insertExternalFunctions(
      context: Optional[QOpenGLContext],
      f: Optional[QAbstractOpenGLFunctions],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOpenGLFunctionsPrivate::insertExternalFunctions(QOpenGLContext
    *context, QAbstractOpenGLFunctions *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctionsprivate.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Optional[QAbstractOpenGLFunctions]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOpenGLFunctionsPrivate::insertExternalFunctions(
    #      QOpenGLContext *context, QAbstractOpenGLFunctions *f)
    Rituals.call(
        'ritual_ZN31QAbstractOpenGLFunctionsPrivate23insertExternalFunction'
        'sEP14QOpenGLContextP24QAbstractOpenGLFunctions',
        CuteMixin._addressOf(context), CuteMixin._addressOf(f),
    )

  @staticmethod
  @overload(QOpenGLContext, QAbstractOpenGLFunctions)
  @overload(QOpenGLContext, NoneType)
  @overload(NoneType, QAbstractOpenGLFunctions)
  @overload(NoneType, NoneType)
  def removeExternalFunctions(
      context: Optional[QOpenGLContext],
      f: Optional[QAbstractOpenGLFunctions],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOpenGLFunctionsPrivate::removeExternalFunctions(QOpenGLContext
    *context, QAbstractOpenGLFunctions *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctionsprivate.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Optional[QAbstractOpenGLFunctions]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOpenGLFunctionsPrivate::removeExternalFunctions(
    #      QOpenGLContext *context, QAbstractOpenGLFunctions *f)
    Rituals.call(
        'ritual_ZN31QAbstractOpenGLFunctionsPrivate23removeExternalFunction'
        'sEP14QOpenGLContextP24QAbstractOpenGLFunctions',
        CuteMixin._addressOf(context), CuteMixin._addressOf(f),
    )

  @staticmethod
  @overload(QAbstractOpenGLFunctions)
  @overload(NoneType)
  def get(
      q: Optional[QAbstractOpenGLFunctions],
  ) -> Optional[QAbstractOpenGLFunctionsPrivate]:
    """
    Calls Qt's 'QAbstractOpenGLFunctionsPrivate
    *QAbstractOpenGLFunctionsPrivate::get(QAbstractOpenGLFunctions *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctionsprivate.html#get

    Parameters
    ----------

    q : Optional[QAbstractOpenGLFunctions]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractOpenGLFunctionsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOpenGLFunctionsPrivate
    #      *QAbstractOpenGLFunctionsPrivate::get(QAbstractOpenGLFunctions *q)
    address = Rituals.call(
        'ritual_ZN31QAbstractOpenGLFunctionsPrivate3getEP24QAbstractOpenGLF'
        'unctions',
        CuteMixin._addressOf(q),
    )
    return QAbstractOpenGLFunctionsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOpenGLFunctionsPrivate'

  #  Qt's '~QAbstractOpenGLFunctionsPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QAbstractOpenGLFunctionsPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QAbstractOpenGLFunctionsPrivateD1Ev'

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
    'QAbstractOpenGLFunctionsPrivate::QAbstractOpenGLFunctionsPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctionsprivate.html
    """
    #  QAbstractOpenGLFunctionsPrivate::QAbstractOpenGLFunctionsPrivate()
    self._noteCreation(QAbstractOpenGLFunctionsPrivate, lambda: Rituals.call(
        'ritual_ZN31QAbstractOpenGLFunctionsPrivateC1Ev',
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
  def functionsBackend(*__, **_) -> Never:
    """
    Qt's 'QOpenGLVersionFunctionsBackend
    *QAbstractOpenGLFunctionsPrivate::functionsBackend(QOpenGLContext
    *context, QOpenGLVersionFunctionsBackend::Version v)': leans on
    'QOpenGLFunctions_1_0_CoreBackend::init()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractOpenGLFunctionsPrivate.functionsBackend' has no cute "
        "function yet. Qt's 'QOpenGLVersionFunctionsBackend "
        "*QAbstractOpenGLFunctionsPrivate::functionsBackend(QOpenGLContext "
        "*context, QOpenGLVersionFunctionsBackend::Version v)': leans on "
        "'QOpenGLFunctions_1_0_CoreBackend::init()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
