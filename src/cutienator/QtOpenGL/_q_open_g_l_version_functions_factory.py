"""
QOpenGLVersionFunctionsFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctionsfactory.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QOpenGLContext
  from . import QAbstractOpenGLFunctions, QOpenGLVersionProfile
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLVersionProfile = WAIT['QOpenGLVersionProfile']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLVersionFunctionsFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVersionFunctionsFactory: a plain Python object
  standing in front of one C++ QOpenGLVersionFunctionsFactory.

  C++ hands a QOpenGLVersionFunctionsFactory around as a copy, so every C++
  QOpenGLVersionFunctionsFactory behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLVersionFunctionsFactory that has a ritual and
  that Python can call so far, 1 name in all: 'get'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLVersionFunctionsFactory::~QOpenGLVersionFunctionsFactory()':
    the destructor: Python removes its C++ QOpenGLVersionFunctionsFactory by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QOpenGLVersionFunctionsFactory is created at the first use, not
    by 'QOpenGLVersionFunctionsFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLVersionFunctionsFactory back gives a copy the
    ritual made for Python, in a new cute QOpenGLVersionFunctionsFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(QOpenGLVersionProfile)
  @overload(QOpenGLVersionProfile, QOpenGLContext)
  @overload(QOpenGLVersionProfile, NoneType)
  def get(
      versionProfile: Optional[QOpenGLVersionProfile] = None,
      context: Optional[QOpenGLContext] = None,
  ) -> Optional[QAbstractOpenGLFunctions]:
    """
    Calls Qt's 'QAbstractOpenGLFunctions
    *QOpenGLVersionFunctionsFactory::get(const QOpenGLVersionProfile
    &versionProfile, QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionfunctionsfactory.html#get

    Parameters
    ----------

    versionProfile : Optional[QOpenGLVersionProfile]
      Passed on as a value: Qt reads the C++ QOpenGLVersionProfile, which
      stays Python's own. May be left out, as in Qt: a new
      'QOpenGLVersionProfile()' is then passed on.

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAbstractOpenGLFunctions]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOpenGLFunctions *QOpenGLVersionFunctionsFactory::get(const
    #      QOpenGLVersionProfile &versionProfile, QOpenGLContext *context)
    if versionProfile is None:
      from . import QOpenGLVersionProfile
      versionProfile = QOpenGLVersionProfile()
    address = Rituals.call(
        'ritual_ZN30QOpenGLVersionFunctionsFactory3getERK21QOpenGLVersionPr'
        'ofileP14QOpenGLContext',
        CuteMixin._valueOf(versionProfile), CuteMixin._addressOf(context),
    )
    from . import QAbstractOpenGLFunctions
    return QAbstractOpenGLFunctions._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVersionFunctionsFactory'

  #  Qt's '~QOpenGLVersionFunctionsFactory()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLVersionFunctionsFactory behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QOpenGLVersionFunctionsFactoryD1Ev'

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
