"""
Qt3DRender::QParameterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qparameter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QParameterPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QParameterPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QParameterPrivate: a plain Python object
  standing in front of one C++ Qt3DRender::QParameterPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::QParameterPrivate is built on Qt's Qt3DCore::QNodePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QParameterPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func', 'setValue'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QParameter *Qt3DRender::QParameterPrivate::q_func() const':
    takes in Python what 'QParameter
    *Qt3DRender::QParameterPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QParameterPrivate is created at the first use, not by
    'Qt3DRender::QParameterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QParameterPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QParameterPrivate'

  #  A C++ Qt3DRender::QParameterPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QParameterPrivate'

  #  The functions Qt calls itself that Qt3DRender::QParameterPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setValue': (
          ('_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

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

  @overload(QVariant)
  def setValue(self, v: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QParameterPrivate::setValue(const QVariant
    &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qparameterprivate.html#setValue

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QParameterPrivate::setValue(const QVariant &v)
    ritual = 'ritual_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVarian'
          't')
    self.uglySide.call(ritual, self._valueOf(v))

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
    'Qt3DRender::QParameterPrivate::QParameterPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qparameterprivate.html
    """
    #  Qt3DRender::QParameterPrivate::QParameterPrivate()
    self._noteCreation(QParameterPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender17QParameterPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QParameter]:
    """
    Calls Qt's 'QParameter *Qt3DRender::QParameterPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qparameterprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QParameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QParameter *Qt3DRender::QParameterPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender17QParameterPrivate6q_funcEv',
    )
    return Qt3DRender.QParameter._cuteAt(address)
