"""
QOpenGLVersionFunctionsBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

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


class QOpenGLVersionFunctionsBackend(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVersionFunctionsBackend: a plain Python object
  standing in front of one C++ QOpenGLVersionFunctionsBackend.

  C++ hands a QOpenGLVersionFunctionsBackend around as a copy, so every C++
  QOpenGLVersionFunctionsBackend behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QOpenGLVersionFunctionsBackend yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLVersionFunctionsBackend::~QOpenGLVersionFunctionsBackend()':
    the destructor: Python removes its C++ QOpenGLVersionFunctionsBackend by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLVersionFunctionsBackend is created at the first use, not
    by 'QOpenGLVersionFunctionsBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLVersionFunctionsBackend back gives a copy the
    ritual made for Python, in a new cute QOpenGLVersionFunctionsBackend.
  """

  #  The enums Qt writes inside QOpenGLVersionFunctionsBackend, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Version(CuteNum):
    """
    The enum 'QOpenGLVersionFunctionsBackend::Version' of Qt, with the 28
    names Qt gives in it.
    """

    OpenGL_1_0_Core = Kee[int](0)
    OpenGL_1_1_Core = Kee[int](1)
    OpenGL_1_2_Core = Kee[int](2)
    OpenGL_1_3_Core = Kee[int](3)
    OpenGL_1_4_Core = Kee[int](4)
    OpenGL_1_5_Core = Kee[int](5)
    OpenGL_2_0_Core = Kee[int](6)
    OpenGL_2_1_Core = Kee[int](7)
    OpenGL_3_0_Core = Kee[int](8)
    OpenGL_3_1_Core = Kee[int](9)
    OpenGL_3_2_Core = Kee[int](10)
    OpenGL_3_3_Core = Kee[int](11)
    OpenGL_4_0_Core = Kee[int](12)
    OpenGL_4_1_Core = Kee[int](13)
    OpenGL_4_2_Core = Kee[int](14)
    OpenGL_4_3_Core = Kee[int](15)
    OpenGL_4_4_Core = Kee[int](16)
    OpenGL_4_5_Core = Kee[int](17)
    OpenGL_1_0_Deprecated = Kee[int](18)
    OpenGL_1_1_Deprecated = Kee[int](19)
    OpenGL_1_2_Deprecated = Kee[int](20)
    OpenGL_1_3_Deprecated = Kee[int](21)
    OpenGL_1_4_Deprecated = Kee[int](22)
    OpenGL_2_0_Deprecated = Kee[int](23)
    OpenGL_3_0_Deprecated = Kee[int](24)
    OpenGL_3_3_Deprecated = Kee[int](25)
    OpenGL_4_5_Deprecated = Kee[int](26)
    OpenGLVersionBackendCount = Kee[int](27)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVersionFunctionsBackend'

  #  Qt's '~QOpenGLVersionFunctionsBackend()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLVersionFunctionsBackend behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QOpenGLVersionFunctionsBackendD1Ev'

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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVersionFunctionsBackend::QOpenGLVersionFunctionsBackend(
    QOpenGLContext *ctx)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionfunctionsbackend.html

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLVersionFunctionsBackend::QOpenGLVersionFunctionsBackend(
    #      QOpenGLContext *ctx)
    self._noteCreation(QOpenGLVersionFunctionsBackend, lambda: Rituals.call(
        'ritual_ZN30QOpenGLVersionFunctionsBackendC1EP14QOpenGLContext',
        self._addressOf(ctx),
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
