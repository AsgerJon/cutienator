"""
QOpenGLExtensionMatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopengl_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QOpenGLExtensionMatcher to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QOpenGLExtensionMatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLExtensionMatcher: a plain Python object
  standing in front of one C++ QOpenGLExtensionMatcher.

  C++ hands a QOpenGLExtensionMatcher around as a copy, so every C++
  QOpenGLExtensionMatcher behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLExtensionMatcher that has a ritual and that
  Python can call so far, 1 name in all: 'match'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSet<QByteArray> QOpenGLExtensionMatcher::extensions() const':
    gives a type Python has no way to take yet.
  - Qt's 'QOpenGLExtensionMatcher::~QOpenGLExtensionMatcher()': the
    destructor: Python removes its C++ QOpenGLExtensionMatcher by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLExtensionMatcher is created at the first use, not by
    'QOpenGLExtensionMatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLExtensionMatcher back gives a copy the ritual
    made for Python, in a new cute QOpenGLExtensionMatcher.
  - Each name of Qt's QOpenGLExtensionMatcher that has no cute function yet,
    'extensions', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLExtensionMatcher'

  #  Qt's '~QOpenGLExtensionMatcher()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLExtensionMatcher behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QOpenGLExtensionMatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def match(self, extension: QByteArray) -> bool:
    """
    Calls Qt's 'bool QOpenGLExtensionMatcher::match(const QByteArray
    &extension) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglextensionmatcher.html#match

    Parameters
    ----------

    extension : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLExtensionMatcher::match(const QByteArray &extension) const
    return self.uglySide.call(
        'ritual_ZNK23QOpenGLExtensionMatcher5matchERK10QByteArray',
        self._valueOf(extension),
    )

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
    'QOpenGLExtensionMatcher::QOpenGLExtensionMatcher()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensionmatcher.html
    """
    #  QOpenGLExtensionMatcher::QOpenGLExtensionMatcher()
    self._noteCreation(QOpenGLExtensionMatcher, lambda: Rituals.call(
        'ritual_ZN23QOpenGLExtensionMatcherC1Ev',
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
  def extensions(*__, **_) -> Never:
    """
    Qt's 'QSet<QByteArray> QOpenGLExtensionMatcher::extensions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLExtensionMatcher.extensions' has no cute function yet. "
        "Qt's 'QSet<QByteArray> QOpenGLExtensionMatcher::extensions() "
        "const': gives a type Python has no way to take yet.")
