"""
Qt3DRender::QRenderCapabilitiesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrendercapabilities_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QRenderCapabilitiesPrivate to be private: it declares
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


class QRenderCapabilitiesPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderCapabilitiesPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::QRenderCapabilitiesPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DRender::QRenderCapabilitiesPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderCapabilitiesPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'q_func', 'get',
  'toString'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRenderCapabilities
    *Qt3DRender::QRenderCapabilitiesPrivate::q_func() const': takes in Python
    what 'QRenderCapabilities
    *Qt3DRender::QRenderCapabilitiesPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderCapabilitiesPrivate is created at the first
    use, not by 'Qt3DRender::QRenderCapabilitiesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderCapabilitiesPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QRenderCapabilities'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DRender.QRenderCapabilities],
  ) -> Optional[QRenderCapabilitiesPrivate]:
    """
    Calls Qt's 'const QRenderCapabilitiesPrivate
    *Qt3DRender::QRenderCapabilitiesPrivate::get(const QRenderCapabilities
    *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilitiesprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DRender.QRenderCapabilities]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRenderCapabilitiesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRenderCapabilitiesPrivate
    #      *Qt3DRender::QRenderCapabilitiesPrivate::get(const
    #      QRenderCapabilities *q)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivate3getEPKNS_19QRend'
        'erCapabilitiesE',
        CuteMixin._addressOf(q),
    )
    return QRenderCapabilitiesPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderCapabilitiesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRenderCapabilitiesPrivate::toString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilitiesprivate.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRenderCapabilitiesPrivate::toString() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender26QRenderCapabilitiesPrivate8toStringEv',
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
    'Qt3DRender::QRenderCapabilitiesPrivate::QRenderCapabilitiesPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilitiesprivate.html
    """
    #  Qt3DRender::QRenderCapabilitiesPrivate::QRenderCapabilitiesPrivate()
    self._noteCreation(QRenderCapabilitiesPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QRenderCapabilities]:
    """
    Calls Qt's 'QRenderCapabilities
    *Qt3DRender::QRenderCapabilitiesPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilitiesprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QRenderCapabilities]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCapabilities *Qt3DRender::QRenderCapabilitiesPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender26QRenderCapabilitiesPrivate6q_funcEv',
    )
    return Qt3DRender.QRenderCapabilities._cuteAt(address)
