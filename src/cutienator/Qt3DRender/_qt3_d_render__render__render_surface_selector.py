"""
Qt3DRender::Render::RenderSurfaceSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/rendersurfaceselector_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::RenderSurfaceSelector to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderSurfaceSelector(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::RenderSurfaceSelector: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::RenderSurfaceSelector.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::RenderSurfaceSelector is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderSurfaceSelector that has a
  ritual and that Python can call so far, 7 names in all: 'renderTargetSize',
  'setRenderTargetSize', 'syncFromFrontEnd', 'surface', 'width', 'height',
  'devicePixelRatio'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderSurfaceSelector is created at the first
    use, not by 'Qt3DRender::Render::RenderSurfaceSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderSurfaceSelector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderSurfaceSelector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def renderTargetSize(self) -> QSize:
    """
    Calls Qt's 'QSize
    Qt3DRender::Render::RenderSurfaceSelector::renderTargetSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DRender::Render::RenderSurfaceSelector::renderTargetSize()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector16renderTarget'
        'SizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def surface(self) -> Optional[QSurface]:
    """
    Calls Qt's 'QSurface
    *Qt3DRender::Render::RenderSurfaceSelector::surface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html

    Returns
    -------

    Optional[QSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface *Qt3DRender::Render::RenderSurfaceSelector::surface() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector7surfaceEv',
    )
    from ..QtGui import QSurface
    return QSurface._cuteAt(address)

  def width(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::RenderSurfaceSelector::width()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html#width
    """
    #  int Qt3DRender::Render::RenderSurfaceSelector::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::RenderSurfaceSelector::height()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html
    """
    #  int Qt3DRender::Render::RenderSurfaceSelector::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector6heightEv',
    )

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float
    Qt3DRender::Render::RenderSurfaceSelector::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html
    """
    #  float Qt3DRender::Render::RenderSurfaceSelector::devicePixelRatio()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector16devicePixelR'
        'atioEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setRenderTargetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderSurfaceSelector::setRenderTargetSize(const
    QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::Render::RenderSurfaceSelector::setRenderTargetSize(
    #      const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render21RenderSurfaceSelector19setRenderTarg'
        'etSizeERK5QSize',
        self._valueOf(size),
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
    'Qt3DRender::Render::RenderSurfaceSelector::RenderSurfaceSelector()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html
    """
    #  Qt3DRender::Render::RenderSurfaceSelector::RenderSurfaceSelector()
    self._noteCreation(RenderSurfaceSelector, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render21RenderSurfaceSelectorC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderSurfaceSelector::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendersurfaceselector.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RenderSurfaceSelector::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render21RenderSurfaceSelector16syncFromFront'
        'EndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render21RenderSurfaceSelector16syncFro'
          'mFrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
