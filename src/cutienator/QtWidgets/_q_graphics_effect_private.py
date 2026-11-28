"""
QGraphicsEffectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsEffectPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGraphicsEffect, QGraphicsEffectSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsEffectSource = WAIT['QGraphicsEffectSource']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsEffectPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsEffectPrivate: a plain Python object
  standing in front of one C++ QGraphicsEffectPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGraphicsEffectPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsEffectPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func',
  'setGraphicsEffectSource'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsEffect *QGraphicsEffectPrivate::q_func() const':
    takes in Python what 'QGraphicsEffect *QGraphicsEffectPrivate::q_func()'
    takes.
  - Qt's 'QGraphicsEffectPrivate::~QGraphicsEffectPrivate()': the destructor:
    Python never removes a C++ QGraphicsEffectPrivate.

  What to expect
  --------------

  - The C++ QGraphicsEffectPrivate is created at the first use, not by
    'QGraphicsEffectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsEffectPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsEffectPrivate'

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

  @overload(QGraphicsEffectSource)
  @overload(NoneType)
  def setGraphicsEffectSource(
      self,
      newSource: Optional[QGraphicsEffectSource],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsEffectPrivate::setGraphicsEffectSource(QGraphicsEffectSource
    *newSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectprivate.html

    Parameters
    ----------

    newSource : Optional[QGraphicsEffectSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsEffectPrivate::setGraphicsEffectSource(
    #      QGraphicsEffectSource *newSource)
    self.uglySide.call(
        'ritual_ZN22QGraphicsEffectPrivate23setGraphicsEffectSourceEP21QGra'
        'phicsEffectSource',
        self._addressOf(newSource),
    )

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
    'QGraphicsEffectPrivate::QGraphicsEffectPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectprivate.html#QGraphicsEffectPrivate
    """
    #  QGraphicsEffectPrivate::QGraphicsEffectPrivate()
    self._noteCreation(QGraphicsEffectPrivate, lambda: Rituals.call(
        'ritual_ZN22QGraphicsEffectPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsEffect]:
    """
    Calls Qt's 'QGraphicsEffect *QGraphicsEffectPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsEffect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEffect *QGraphicsEffectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGraphicsEffectPrivate6q_funcEv',
    )
    from . import QGraphicsEffect
    return QGraphicsEffect._cuteAt(address)
