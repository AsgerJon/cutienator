"""
CachedShader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglshadercache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means CachedShader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from ..QtGui import QOpenGLContext
  from . import QOpenGLShaderProgram
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLShaderProgram = WAIT['QOpenGLShaderProgram']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CachedShader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's CachedShader: a plain Python object standing in front
  of one C++ CachedShader.

  C++ hands a CachedShader around as a copy, so every C++ CachedShader behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's CachedShader that has a ritual and that Python can
  call so far, 3 names in all: 'isCached', 'load', 'store'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'CachedShader::~CachedShader()': the destructor: Python removes its
    C++ CachedShader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ CachedShader is created at the first use, not by
    'CachedShader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a CachedShader back gives a copy the ritual made for
    Python, in a new cute CachedShader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CachedShader'

  #  Qt's '~CachedShader()'. Naming it makes this a value class: Python owns
  #  every C++ CachedShader behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12CachedShaderD1Ev'

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

  @overload(QByteArray, QByteArray)
  def __init__(self, a0: QByteArray, a1: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'CachedShader::CachedShader(const
    QByteArray &a0, const QByteArray &a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/cachedshader.html#CachedShader

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  CachedShader::CachedShader(const QByteArray &a0, const QByteArray &a1)
    self._noteCreation(CachedShader, lambda: Rituals.call(
        'ritual_ZN12CachedShaderC1ERK10QByteArrayS2_',
        self._valueOf(a0), self._valueOf(a1),
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

  def isCached(self) -> bool:
    """
    Calls Qt's 'bool CachedShader::isCached()'.

    Qt's own words: https://doc.qt.io/qt-6/cachedshader.html#isCached
    """
    #  bool CachedShader::isCached()
    return self.uglySide.call('ritual_ZN12CachedShader8isCachedEv')

  @overload(QOpenGLShaderProgram, QOpenGLContext)
  @overload(QOpenGLShaderProgram, NoneType)
  @overload(NoneType, QOpenGLContext)
  @overload(NoneType, NoneType)
  def load(
      self,
      a0: Optional[QOpenGLShaderProgram],
      a1: Optional[QOpenGLContext],
  ) -> bool:
    """
    Calls Qt's 'bool CachedShader::load(QOpenGLShaderProgram *a0,
    QOpenGLContext *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/cachedshader.html#load

    Parameters
    ----------

    a0 : Optional[QOpenGLShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool CachedShader::load(QOpenGLShaderProgram *a0, QOpenGLContext *a1)
    return self.uglySide.call(
        'ritual_ZN12CachedShader4loadEP20QOpenGLShaderProgramP14QOpenGLCont'
        'ext',
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QOpenGLShaderProgram, QOpenGLContext)
  @overload(QOpenGLShaderProgram, NoneType)
  @overload(NoneType, QOpenGLContext)
  @overload(NoneType, NoneType)
  def store(
      self,
      a0: Optional[QOpenGLShaderProgram],
      a1: Optional[QOpenGLContext],
  ) -> bool:
    """
    Calls Qt's 'bool CachedShader::store(QOpenGLShaderProgram *a0,
    QOpenGLContext *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/cachedshader.html#store

    Parameters
    ----------

    a0 : Optional[QOpenGLShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool CachedShader::store(QOpenGLShaderProgram *a0, QOpenGLContext *a1)
    return self.uglySide.call(
        'ritual_ZN12CachedShader5storeEP20QOpenGLShaderProgramP14QOpenGLCon'
        'text',
        self._addressOf(a0), self._addressOf(a1),
    )
