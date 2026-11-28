"""
QAccessibilityHintsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qaccessibilityhints_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAccessibilityHintsPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccessibilityHints
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibilityHints = WAIT['QAccessibilityHints']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibilityHintsPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAccessibilityHintsPrivate: a plain Python object
  standing in front of one C++ QAccessibilityHintsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAccessibilityHintsPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibilityHintsPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func',
  'updateContrastPreference', 'updateMotionPreference', 'get'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAccessibilityHints *QAccessibilityHintsPrivate::q_func()
    const': takes in Python what 'QAccessibilityHints
    *QAccessibilityHintsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAccessibilityHintsPrivate is created at the first use, not by
    'QAccessibilityHintsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibilityHintsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAccessibilityHints)
  @overload(NoneType)
  def get(
      q: Optional[QAccessibilityHints],
  ) -> Optional[QAccessibilityHintsPrivate]:
    """
    Calls Qt's 'QAccessibilityHintsPrivate
    *QAccessibilityHintsPrivate::get(QAccessibilityHints *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhintsprivate.html#get

    Parameters
    ----------

    q : Optional[QAccessibilityHints]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAccessibilityHintsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibilityHintsPrivate
    #      *QAccessibilityHintsPrivate::get(QAccessibilityHints *q)
    address = Rituals.call(
        'ritual_ZN26QAccessibilityHintsPrivate3getEP19QAccessibilityHints',
        CuteMixin._addressOf(q),
    )
    return QAccessibilityHintsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibilityHintsPrivate'

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

  def q_func(self) -> Optional[QAccessibilityHints]:
    """
    Calls Qt's 'QAccessibilityHints *QAccessibilityHintsPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhintsprivate.html#q_func

    Returns
    -------

    Optional[QAccessibilityHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibilityHints *QAccessibilityHintsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QAccessibilityHintsPrivate6q_funcEv',
    )
    from . import QAccessibilityHints
    return QAccessibilityHints._cuteAt(address)

  @overload(Qt.ContrastPreference)
  def updateContrastPreference(
      self,
      contrastPreference: Qt.ContrastPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibilityHintsPrivate::updateContrastPreference(Qt::
    ContrastPreference contrastPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhintsprivate.html

    Parameters
    ----------

    contrastPreference : Qt.ContrastPreference
      Passed on as its number.
    """
    #  void QAccessibilityHintsPrivate::updateContrastPreference(Qt::
    #      ContrastPreference contrastPreference)
    self.uglySide.call(
        'ritual_ZN26QAccessibilityHintsPrivate24updateContrastPreferenceEN2'
        'Qt18ContrastPreferenceE',
        contrastPreference.value,
    )

  @overload(Qt.MotionPreference)
  def updateMotionPreference(
      self,
      motionPreference: Qt.MotionPreference,
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibilityHintsPrivate::updateMotionPreference(Qt::MotionPreference
    motionPreference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibilityhintsprivate.html

    Parameters
    ----------

    motionPreference : Qt.MotionPreference
      Passed on as its number.
    """
    #  void QAccessibilityHintsPrivate::updateMotionPreference(Qt::
    #      MotionPreference motionPreference)
    self.uglySide.call(
        'ritual_ZN26QAccessibilityHintsPrivate22updateMotionPreferenceEN2Qt'
        '16MotionPreferenceE',
        motionPreference.value,
    )
