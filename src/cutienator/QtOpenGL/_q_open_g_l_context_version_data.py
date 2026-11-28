"""
QOpenGLContextVersionData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglversionfunctions_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLContextVersionData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QOpenGLContextVersionFunctionHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLContextVersionData(QOpenGLContextVersionFunctionHelper):
  """
  The cute side of Qt's QOpenGLContextVersionData: a plain Python object
  standing in front of one C++ QOpenGLContextVersionData.

  It is built on the cute 'QOpenGLContextVersionFunctionHelper', as Qt's
  QOpenGLContextVersionData is built on Qt's
  QOpenGLContextVersionFunctionHelper, and has everything that class has.

  C++ hands a QOpenGLContextVersionData around as a copy, so every C++
  QOpenGLContextVersionData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLContextVersionData that has a ritual and that
  Python can call so far, 1 name in all: 'forContext'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLContextVersionData::~QOpenGLContextVersionData()': the
    destructor: Python removes its C++ QOpenGLContextVersionData by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLContextVersionData is created at the first use, not by
    'QOpenGLContextVersionData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLContextVersionData back gives a copy the
    ritual made for Python, in a new cute QOpenGLContextVersionData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def forContext(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLContextVersionData]:
    """
    Calls Qt's 'QOpenGLContextVersionData
    *QOpenGLContextVersionData::forContext(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextversiondata.html#forContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLContextVersionData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextVersionData
    #      *QOpenGLContextVersionData::forContext(QOpenGLContext *context)
    address = Rituals.call(
        'ritual_ZN25QOpenGLContextVersionData10forContextEP14QOpenGLContext',
        CuteMixin._addressOf(context),
    )
    return QOpenGLContextVersionData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLContextVersionData'

  #  Qt's '~QOpenGLContextVersionData()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLContextVersionData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpenGLContextVersionDataD1Ev'

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
