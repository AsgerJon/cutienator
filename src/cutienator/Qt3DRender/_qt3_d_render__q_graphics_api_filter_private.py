"""
Qt3DRender::QGraphicsApiFilterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qgraphicsapifilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QGraphicsApiFilterPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsApiFilterPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DRender::QGraphicsApiFilterPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QGraphicsApiFilterPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DRender::QGraphicsApiFilterPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QGraphicsApiFilterPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'get', 'q_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsApiFilterPrivate
    *Qt3DRender::QGraphicsApiFilterPrivate::get(const QGraphicsApiFilter
    *q)': takes in Python what 'QGraphicsApiFilterPrivate
    *Qt3DRender::QGraphicsApiFilterPrivate::get(QGraphicsApiFilter *q)'
    takes.
  - Qt's 'const QGraphicsApiFilter
    *Qt3DRender::QGraphicsApiFilterPrivate::q_func() const': takes in Python
    what 'QGraphicsApiFilter
    *Qt3DRender::QGraphicsApiFilterPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QGraphicsApiFilterPrivate is created at the first
    use, not by 'Qt3DRender::QGraphicsApiFilterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QGraphicsApiFilterPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QGraphicsApiFilter'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DRender.QGraphicsApiFilter],
  ) -> Optional[QGraphicsApiFilterPrivate]:
    """
    Calls Qt's 'QGraphicsApiFilterPrivate
    *Qt3DRender::QGraphicsApiFilterPrivate::get(QGraphicsApiFilter *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilterprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DRender.QGraphicsApiFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsApiFilterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsApiFilterPrivate
    #      *Qt3DRender::QGraphicsApiFilterPrivate::get(QGraphicsApiFilter *q)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender25QGraphicsApiFilterPrivate3getEPNS_18QGraphi'
        'csApiFilterE',
        CuteMixin._addressOf(q),
    )
    return QGraphicsApiFilterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QGraphicsApiFilterPrivate'

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
    'Qt3DRender::QGraphicsApiFilterPrivate::QGraphicsApiFilterPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilterprivate.html
    """
    #  Qt3DRender::QGraphicsApiFilterPrivate::QGraphicsApiFilterPrivate()
    self._noteCreation(QGraphicsApiFilterPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender25QGraphicsApiFilterPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QGraphicsApiFilter]:
    """
    Calls Qt's 'QGraphicsApiFilter
    *Qt3DRender::QGraphicsApiFilterPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgraphicsapifilterprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QGraphicsApiFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsApiFilter *Qt3DRender::QGraphicsApiFilterPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender25QGraphicsApiFilterPrivate6q_funcEv',
    )
    return Qt3DRender.QGraphicsApiFilter._cuteAt(address)
