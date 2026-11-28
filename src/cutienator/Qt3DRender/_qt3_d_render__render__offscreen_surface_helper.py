"""
Qt3DRender::Render::OffscreenSurfaceHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/offscreensurfacehelper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::OffscreenSurfaceHelper to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QOffscreenSurface

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class OffscreenSurfaceHelper(QObject):
  """
  The cute side of Qt's Qt3DRender::Render::OffscreenSurfaceHelper: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::OffscreenSurfaceHelper.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::Render::OffscreenSurfaceHelper is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::OffscreenSurfaceHelper that has
  a ritual and that Python can call so far, 4 names in all: 'metaObject',
  'tr', 'offscreenSurface', 'createOffscreenSurface'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Render::OffscreenSurfaceHelper::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::Render::OffscreenSurfaceHelper::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::OffscreenSurfaceHelper is created at the
    first use, not by 'Qt3DRender::Render::OffscreenSurfaceHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::OffscreenSurfaceHelper.
  - Qt tells when it has removed the C++
    Qt3DRender::Render::OffscreenSurfaceHelper. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::OffscreenSurfaceHelper::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-offscreensurfacehelper.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::OffscreenSurfaceHelper::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::OffscreenSurfaceHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DRender::Render::OffscreenSurfaceHelper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-offscreensurfacehelper.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::Render::OffscreenSurfaceHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22OffscreenSurfaceHelper10metaObjectE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offscreenSurface(self) -> Optional[QOffscreenSurface]:
    """
    Calls Qt's 'QOffscreenSurface
    *Qt3DRender::Render::OffscreenSurfaceHelper::offscreenSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-offscreensurfacehelper.html

    Returns
    -------

    Optional[QOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOffscreenSurface
    #      *Qt3DRender::Render::OffscreenSurfaceHelper::offscreenSurface()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22OffscreenSurfaceHelper16offscreenSu'
        'rfaceEv',
    )
    from ..QtGui import QOffscreenSurface
    return QOffscreenSurface._cuteAt(address)

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

  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'])
  @overload(NoneType)
  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'], QObject)
  @overload(WAIT['Qt3DRender.Render.AbstractRenderer'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      renderer: Optional[Qt3DRender.Render.AbstractRenderer],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::OffscreenSurfaceHelper::OffscreenSurfaceHelper(
    AbstractRenderer *renderer, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-offscreensurfacehelper.html

    Parameters
    ----------

    renderer : Optional[Qt3DRender.Render.AbstractRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::Render::OffscreenSurfaceHelper::
    #      OffscreenSurfaceHelper(AbstractRenderer *renderer, QObject
    #      *parent)
    self._noteCreation(OffscreenSurfaceHelper, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelperC1EPNS0_16Abst'
        'ractRendererEP7QObject',
        self._addressOf(renderer), self._addressOf(parent, 'QObject'),
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

  def createOffscreenSurface(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::OffscreenSurfaceHelper::createOffscreenSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-offscreensurfacehelper.html
    """
    #  void Qt3DRender::Render::OffscreenSurfaceHelper::
    #      createOffscreenSurface()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper22createOffscr'
        'eenSurfaceEv',
    )
