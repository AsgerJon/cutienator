"""
QQuickTransformPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTransformPrivate to be private: it declares the class in a
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

  from . import QQuickTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTransform = WAIT['QQuickTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTransformPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickTransformPrivate: a plain Python object
  standing in front of one C++ QQuickTransformPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickTransformPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTransformPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTransform *QQuickTransformPrivate::q_func() const':
    takes in Python what 'QQuickTransform *QQuickTransformPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickTransformPrivate is created at the first use, not by
    'QQuickTransformPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTransformPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTransform)
  @overload(NoneType)
  def get(
      transform: Optional[QQuickTransform],
  ) -> Optional[QQuickTransformPrivate]:
    """
    Calls Qt's 'QQuickTransformPrivate
    *QQuickTransformPrivate::get(QQuickTransform *transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransformprivate.html#get

    Parameters
    ----------

    transform : Optional[QQuickTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTransformPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransformPrivate *QQuickTransformPrivate::get(QQuickTransform
    #      *transform)
    address = Rituals.call(
        'ritual_ZN22QQuickTransformPrivate3getEP15QQuickTransform',
        CuteMixin._addressOf(transform),
    )
    return QQuickTransformPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTransformPrivate'

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
    'QQuickTransformPrivate::QQuickTransformPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransformprivate.html#QQuickTransformPrivate
    """
    #  QQuickTransformPrivate::QQuickTransformPrivate()
    self._noteCreation(QQuickTransformPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickTransformPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTransform]:
    """
    Calls Qt's 'QQuickTransform *QQuickTransformPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransformprivate.html#q_func

    Returns
    -------

    Optional[QQuickTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransform *QQuickTransformPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTransformPrivate6q_funcEv',
    )
    from . import QQuickTransform
    return QQuickTransform._cuteAt(address)
