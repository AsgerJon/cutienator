"""
QQuickPopupAnchorsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupanchors_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupAnchorsPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPopupAnchors
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPopupAnchors = WAIT['QQuickPopupAnchors']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupAnchorsPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickPopupAnchorsPrivate: a plain Python object
  standing in front of one C++ QQuickPopupAnchorsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickPopupAnchorsPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopupAnchorsPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'get'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPopupAnchors *QQuickPopupAnchorsPrivate::q_func()
    const': takes in Python what 'QQuickPopupAnchors
    *QQuickPopupAnchorsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickPopupAnchorsPrivate is created at the first use, not by
    'QQuickPopupAnchorsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupAnchorsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPopupAnchors)
  @overload(NoneType)
  def get(
      popupAnchors: Optional[QQuickPopupAnchors],
  ) -> Optional[QQuickPopupAnchorsPrivate]:
    """
    Calls Qt's 'QQuickPopupAnchorsPrivate
    *QQuickPopupAnchorsPrivate::get(QQuickPopupAnchors *popupAnchors)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupanchorsprivate.html#get

    Parameters
    ----------

    popupAnchors : Optional[QQuickPopupAnchors]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPopupAnchorsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupAnchorsPrivate
    #      *QQuickPopupAnchorsPrivate::get(QQuickPopupAnchors *popupAnchors)
    address = Rituals.call(
        'ritual_ZN25QQuickPopupAnchorsPrivate3getEP18QQuickPopupAnchors',
        CuteMixin._addressOf(popupAnchors),
    )
    return QQuickPopupAnchorsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupAnchorsPrivate'

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

  def q_func(self) -> Optional[QQuickPopupAnchors]:
    """
    Calls Qt's 'QQuickPopupAnchors *QQuickPopupAnchorsPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupanchorsprivate.html#q_func

    Returns
    -------

    Optional[QQuickPopupAnchors]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupAnchors *QQuickPopupAnchorsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickPopupAnchorsPrivate6q_funcEv',
    )
    from . import QQuickPopupAnchors
    return QQuickPopupAnchors._cuteAt(address)
