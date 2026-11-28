"""
QQuick3DSGDirectRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DSGDirectRenderer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QQuick3DSceneRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQuick3DSGDirectRenderer(QObject):
  """
  The cute side of Qt's QQuick3DSGDirectRenderer: a plain Python object
  standing in front of one C++ QQuick3DSGDirectRenderer.

  It is built on the cute 'QObject', as Qt's QQuick3DSGDirectRenderer is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSGDirectRenderer that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'renderer',
  'setViewport', 'requestRender', 'setVisibility', 'preSynchronize',
  'prepare', 'render'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSGDirectRenderer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DSGDirectRenderer::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSGDirectRenderer::~QQuick3DSGDirectRenderer()': the
    destructor: Python never removes a C++ QQuick3DSGDirectRenderer.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DSGDirectRenderer.

  What to expect
  --------------

  - The C++ QQuick3DSGDirectRenderer is created at the first use, not by
    'QQuick3DSGDirectRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSGDirectRenderer.
  - Qt tells when it has removed the C++ QQuick3DSGDirectRenderer. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSGDirectRenderer that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSGDirectRenderer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class QQuick3DSGDirectRendererMode(CuteNum):
    """
    The enum 'QQuick3DSGDirectRenderer::QQuick3DSGDirectRendererMode' of Qt,
    with the 2 names Qt gives in it.
    """

    Underlay = Kee[int](0)
    Overlay = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSGDirectRenderer'

  #  A C++ QQuick3DSGDirectRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSGDirectRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSGDirectRenderer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSGDirectRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSGDirectRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setViewport(self, viewport: QRectF) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::setViewport(const QRectF
    &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#setViewport

    Parameters
    ----------

    viewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuick3DSGDirectRenderer::setViewport(const QRectF &viewport)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSGDirectRenderer11setViewportERK6QRectF',
        self._valueOf(viewport),
    )

  @overload(bool)
  def setVisibility(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::setVisibility(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#setVisibility

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuick3DSGDirectRenderer::setVisibility(bool visible)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSGDirectRenderer13setVisibilityEb', visible,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQuick3DSGDirectRenderer::QQuick3DSGDirectRenderer(QQuick3DSceneRenderer
    *renderer, QQuickWindow *window, QQuick3DSGDirectRendererMode mode)':
    leans on 'QQuick3DSGDirectRenderer::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DSGDirectRenderer.__init__' has no cute function yet. Qt's "
        "'QQuick3DSGDirectRenderer::QQuick3DSGDirectRenderer(QQuick3DSceneRe"
        "nderer *renderer, QQuickWindow *window, "
        "QQuick3DSGDirectRendererMode mode)': leans on "
        "'QQuick3DSGDirectRenderer::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def renderer(self) -> Optional[QQuick3DSceneRenderer]:
    """
    Calls Qt's 'QQuick3DSceneRenderer *QQuick3DSGDirectRenderer::renderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#renderer

    Returns
    -------

    Optional[QQuick3DSceneRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneRenderer *QQuick3DSGDirectRenderer::renderer()
    address = self.uglySide.call(
        'ritual_ZN24QQuick3DSGDirectRenderer8rendererEv',
    )
    from . import QQuick3DSceneRenderer
    return QQuick3DSceneRenderer._cuteAt(address)

  def requestRender(self) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::requestRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#requestRender
    """
    #  void QQuick3DSGDirectRenderer::requestRender()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSGDirectRenderer13requestRenderEv',
    )

  def preSynchronize(self) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::preSynchronize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#preSynchronize
    """
    #  void QQuick3DSGDirectRenderer::preSynchronize()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSGDirectRenderer14preSynchronizeEv',
    )

  def prepare(self) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::prepare()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#prepare
    """
    #  void QQuick3DSGDirectRenderer::prepare()
    self.uglySide.call('ritual_ZN24QQuick3DSGDirectRenderer7prepareEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QQuick3DSGDirectRenderer::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgdirectrenderer.html#render
    """
    #  void QQuick3DSGDirectRenderer::render()
    self.uglySide.call('ritual_ZN24QQuick3DSGDirectRenderer6renderEv')
