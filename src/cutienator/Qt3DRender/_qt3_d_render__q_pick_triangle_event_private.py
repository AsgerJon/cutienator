"""
Qt3DRender::QPickTriangleEventPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qpicktriangleevent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QPickTriangleEventPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPickTriangleEventPrivate(Qt3DRender.QPickEventPrivate):
  """
  The cute side of Qt's Qt3DRender::QPickTriangleEventPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QPickTriangleEventPrivate.

  It is built on the cute 'Qt3DRender::QPickEventPrivate', as Qt's
  Qt3DRender::QPickTriangleEventPrivate is built on Qt's
  Qt3DRender::QPickEventPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPickTriangleEventPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'get', 'clone'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::QPickTriangleEventPrivate is created at the first
    use, not by 'Qt3DRender::QPickTriangleEventPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPickTriangleEventPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QPickTriangleEvent'])
  @overload(NoneType)
  def get(
      ev: Optional[Qt3DRender.QPickTriangleEvent],
  ) -> Optional[QPickTriangleEventPrivate]:
    """
    Calls Qt's 'const QPickTriangleEventPrivate
    *Qt3DRender::QPickTriangleEventPrivate::get(const QPickTriangleEvent
    *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleeventprivate.html#get

    Parameters
    ----------

    ev : Optional[Qt3DRender.QPickTriangleEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPickTriangleEventPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPickTriangleEventPrivate
    #      *Qt3DRender::QPickTriangleEventPrivate::get(const
    #      QPickTriangleEvent *ev)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender25QPickTriangleEventPrivate3getEPKNS_18QPickT'
        'riangleEventE',
        CuteMixin._addressOf(ev),
    )
    return QPickTriangleEventPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPickTriangleEventPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[Qt3DRender.QPickTriangleEvent]:
    """
    Calls Qt's 'QPickTriangleEvent
    *Qt3DRender::QPickTriangleEventPrivate::clone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleeventprivate.html#clone

    Returns
    -------

    Optional[Qt3DRender.QPickTriangleEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPickTriangleEvent *Qt3DRender::QPickTriangleEventPrivate::clone()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender25QPickTriangleEventPrivate5cloneEv',
    )
    return Qt3DRender.QPickTriangleEvent._cuteAt(address)

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
    'Qt3DRender::QPickTriangleEventPrivate::QPickTriangleEventPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpicktriangleeventprivate.html
    """
    #  Qt3DRender::QPickTriangleEventPrivate::QPickTriangleEventPrivate()
    self._noteCreation(QPickTriangleEventPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender25QPickTriangleEventPrivateC1Ev',
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
