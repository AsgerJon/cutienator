"""
Qt3DRender::Render::PlatformSurfaceFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/platformsurfacefilter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PlatformSurfaceFilter to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QSurface = WAIT['QSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PlatformSurfaceFilter(QObject):
  """
  The cute side of Qt's Qt3DRender::Render::PlatformSurfaceFilter: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::PlatformSurfaceFilter.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::Render::PlatformSurfaceFilter is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::PlatformSurfaceFilter that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'eventFilter', 'lockSurface', 'releaseSurface', 'isSurfaceValid',
  'markSurfaceAsValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Render::PlatformSurfaceFilter::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::Render::PlatformSurfaceFilter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DRender::Render::PlatformSurfaceFilter::~PlatformSurfaceFilter()':
    the destructor: Python never removes a C++
    Qt3DRender::Render::PlatformSurfaceFilter.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PlatformSurfaceFilter is created at the first
    use, not by 'Qt3DRender::Render::PlatformSurfaceFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::PlatformSurfaceFilter.
  - Qt tells when it has removed the C++
    Qt3DRender::Render::PlatformSurfaceFilter. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's Qt3DRender::Render::PlatformSurfaceFilter that has no
    cute function yet, 'setSurface', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DRender::Render::PlatformSurfaceFilter::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html#tr

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
    #  QString Qt3DRender::Render::PlatformSurfaceFilter::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def lockSurface() -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PlatformSurfaceFilter::lockSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html
    """
    #  void Qt3DRender::Render::PlatformSurfaceFilter::lockSurface()
    Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter11lockSurfaceEv',
    )

  @staticmethod
  def releaseSurface() -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PlatformSurfaceFilter::releaseSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html
    """
    #  void Qt3DRender::Render::PlatformSurfaceFilter::releaseSurface()
    Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter14releaseSurfac'
        'eEv',
    )

  @staticmethod
  @overload(QSurface)
  @overload(NoneType)
  def isSurfaceValid(surface: Optional[QSurface]) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PlatformSurfaceFilter::isSurfaceValid(QSurface
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html

    Parameters
    ----------

    surface : Optional[QSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      Qt3DRender::Render::PlatformSurfaceFilter::isSurfaceValid(QSurface
    #      *surface)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter14isSurfaceVali'
        'dEP8QSurface',
        CuteMixin._addressOf(surface, 'QSurface'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PlatformSurfaceFilter'

  #  A C++ Qt3DRender::Render::PlatformSurfaceFilter Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_PlatformSurfaceFilter'

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
    *Qt3DRender::Render::PlatformSurfaceFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::Render::PlatformSurfaceFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21PlatformSurfaceFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::PlatformSurfaceFilter::PlatformSurfaceFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::Render::PlatformSurfaceFilter::PlatformSurfaceFilter(
    #      QObject *parent)
    self._noteCreation(PlatformSurfaceFilter, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, obj: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(QObject *obj,
    QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(QObject
    #      *obj, QEvent *e)
    ritual = (
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter11eventFilterEP'
        '7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render21PlatformSurfaceFilter11eventFi'
          'lterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(obj, 'QObject'), self._addressOf(e),
    )

  def markSurfaceAsValid(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PlatformSurfaceFilter::markSurfaceAsValid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-platformsurfacefilter.html
    """
    #  void Qt3DRender::Render::PlatformSurfaceFilter::markSurfaceAsValid()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter18markSurfaceAs'
        'ValidEv',
    )

  @staticmethod
  def setSurface(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::PlatformSurfaceFilter::setSurface': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PlatformSurfaceFilter.setSurface' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::PlatformSurfaceFilter::setSurface': a "
        "template: a pattern and no single function.")
