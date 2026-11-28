"""
QSGTexturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGTexturePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGTexturePrivate(QObjectPrivate):
  """
  The cute side of Qt's QSGTexturePrivate: a plain Python object standing in
  front of one C++ QSGTexturePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSGTexturePrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGTexturePrivate that has a ritual and that Python
  can call so far, 4 names in all: 'q_func', 'get',
  'resetDirtySamplerOptions', 'hasDirtySamplerOptions'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSGTexture *QSGTexturePrivate::q_func() const': takes in
    Python what 'QSGTexture *QSGTexturePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QSGTexturePrivate is created at the first use, not by
    'QSGTexturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGTexturePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGTexture)
  @overload(NoneType)
  def get(t: Optional[QSGTexture]) -> Optional[QSGTexturePrivate]:
    """
    Calls Qt's 'QSGTexturePrivate *QSGTexturePrivate::get(QSGTexture *t)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextureprivate.html#get

    Parameters
    ----------

    t : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGTexturePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexturePrivate *QSGTexturePrivate::get(QSGTexture *t)
    address = Rituals.call(
        'ritual_ZN17QSGTexturePrivate3getEP10QSGTexture',
        CuteMixin._addressOf(t),
    )
    return QSGTexturePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTexturePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasDirtySamplerOptions(self) -> bool:
    """
    Calls Qt's 'bool QSGTexturePrivate::hasDirtySamplerOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextureprivate.html#hasDirtySamplerOptions
    """
    #  bool QSGTexturePrivate::hasDirtySamplerOptions() const
    return self.uglySide.call(
        'ritual_ZNK17QSGTexturePrivate22hasDirtySamplerOptionsEv',
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

  @overload(QSGTexture)
  @overload(NoneType)
  def __init__(self, t: Optional[QSGTexture]) -> None:
    """
    Notes what was given, for Qt's
    'QSGTexturePrivate::QSGTexturePrivate(QSGTexture *t)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextureprivate.html#QSGTexturePrivate

    Parameters
    ----------

    t : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGTexturePrivate::QSGTexturePrivate(QSGTexture *t)
    self._noteCreation(QSGTexturePrivate, lambda: Rituals.call(
        'ritual_ZN17QSGTexturePrivateC1EP10QSGTexture', self._addressOf(t),
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

  def q_func(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGTexturePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtextureprivate.html#q_func

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGTexturePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QSGTexturePrivate6q_funcEv')
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def resetDirtySamplerOptions(self) -> None:
    """
    Calls Qt's 'void QSGTexturePrivate::resetDirtySamplerOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgtextureprivate.html#resetDirtySamplerOptions
    """
    #  void QSGTexturePrivate::resetDirtySamplerOptions()
    self.uglySide.call(
        'ritual_ZN17QSGTexturePrivate24resetDirtySamplerOptionsEv',
    )
