"""
QOpenGLFramebufferObjectFormatPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLFramebufferObjectFormatPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLFramebufferObjectFormatPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLFramebufferObjectFormatPrivate: a plain Python
  object standing in front of one C++ QOpenGLFramebufferObjectFormatPrivate.

  C++ hands a QOpenGLFramebufferObjectFormatPrivate around as a copy, so
  every C++ QOpenGLFramebufferObjectFormatPrivate behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFramebufferObjectFormatPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'equals'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFramebufferObjectFormatPrivate::
    ~QOpenGLFramebufferObjectFormatPrivate()': the destructor: Python removes
    its C++ QOpenGLFramebufferObjectFormatPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpenGLFramebufferObjectFormatPrivate is created at the first
    use, not by 'QOpenGLFramebufferObjectFormatPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFramebufferObjectFormatPrivate back gives a
    copy the ritual made for Python, in a new cute
    QOpenGLFramebufferObjectFormatPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFramebufferObjectFormatPrivate'

  #  Qt's '~QOpenGLFramebufferObjectFormatPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QOpenGLFramebufferObjectFormatPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN37QOpenGLFramebufferObjectFormatPrivateD1Ev'

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
    Notes what was given, for Qt's 'QOpenGLFramebufferObjectFormatPrivate::
    QOpenGLFramebufferObjectFormatPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformatprivate.html
    """
    #  QOpenGLFramebufferObjectFormatPrivate::
    #      QOpenGLFramebufferObjectFormatPrivate()
    self._noteCreation(
        QOpenGLFramebufferObjectFormatPrivate, lambda: Rituals.call(
            'ritual_ZN37QOpenGLFramebufferObjectFormatPrivateC1Ev',
        ))

  @overload(THIS)
  @overload(NoneType)
  def __init__(
      self,
      other: Optional[QOpenGLFramebufferObjectFormatPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLFramebufferObjectFormatPrivate::
    QOpenGLFramebufferObjectFormatPrivate(const
    QOpenGLFramebufferObjectFormatPrivate *other)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformatprivate.html

    Parameters
    ----------

    other : Optional[QOpenGLFramebufferObjectFormatPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLFramebufferObjectFormatPrivate::
    #      QOpenGLFramebufferObjectFormatPrivate(const
    #      QOpenGLFramebufferObjectFormatPrivate *other)
    self._noteCreation(
        QOpenGLFramebufferObjectFormatPrivate, lambda: Rituals.call(
            'ritual_ZN37QOpenGLFramebufferObjectFormatPrivateC1EPKS_',
            self._addressOf(other),
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

  @overload(THIS)
  @overload(NoneType)
  def equals(
      self,
      other: Optional[QOpenGLFramebufferObjectFormatPrivate],
  ) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObjectFormatPrivate::equals(const
    QOpenGLFramebufferObjectFormatPrivate *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformatprivate.html#equals

    Parameters
    ----------

    other : Optional[QOpenGLFramebufferObjectFormatPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFramebufferObjectFormatPrivate::equals(const
    #      QOpenGLFramebufferObjectFormatPrivate *other)
    return self.uglySide.call(
        'ritual_ZN37QOpenGLFramebufferObjectFormatPrivate6equalsEPKS_',
        self._addressOf(other),
    )
