"""
Qt3DRender::Scene3DRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3drenderer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Scene3DRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import Qt3DRender
from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtQuick import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scene3DRenderer(QObject):
  """
  The cute side of Qt's Qt3DRender::Scene3DRenderer: a plain Python object
  standing in front of one C++ Qt3DRender::Scene3DRenderer.

  It is built on the cute 'QObject', as Qt's Qt3DRender::Scene3DRenderer is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Scene3DRenderer that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'sgNode',
  'allowRender', 'setCompositingMode', 'setSkipFrame', 'setMultisample',
  'setBoundingSize', 'multisample', 'boundingSize', 'isYUp',
  'beforeSynchronize', 'setWindow', 'hasShutdown', 'renderAspect',
  'shutdown'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Scene3DRenderer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::Scene3DRenderer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::Scene3DRenderer::~Scene3DRenderer()': the destructor:
    Python never removes a C++ Qt3DRender::Scene3DRenderer.

  What has no ritual
  ------------------

  7 of the 25 functions Qt declares: 2 not a gap; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied; 2 leans on
  'Qt3DRender; 1 leans on 'vtable for Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Scene3DRenderer is created at the first use, not by
    'Qt3DRender::Scene3DRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Scene3DRenderer.
  - Qt tells when it has removed the C++ Qt3DRender::Scene3DRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::Scene3DRenderer that has no cute function
    yet, '__init__', 'init', 'setCleanerHelper', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Scene3DRenderer'

  #  A C++ Qt3DRender::Scene3DRenderer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Scene3DRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::Scene3DRenderer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::Scene3DRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sgNode(self) -> Optional[Qt3DRender.Scene3DSGNode]:
    """
    Calls Qt's 'Scene3DSGNode *Qt3DRender::Scene3DRenderer::sgNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#sgNode

    Returns
    -------

    Optional[Qt3DRender.Scene3DSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Scene3DSGNode *Qt3DRender::Scene3DRenderer::sgNode() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer6sgNodeEv',
    )
    return Qt3DRender.Scene3DSGNode._cuteAt(address)

  def multisample(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DRenderer::multisample() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#multisample
    """
    #  bool Qt3DRender::Scene3DRenderer::multisample() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer11multisampleEv',
    )

  def boundingSize(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DRender::Scene3DRenderer::boundingSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#boundingSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DRender::Scene3DRenderer::boundingSize() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer12boundingSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isYUp(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DRenderer::isYUp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#isYUp
    """
    #  bool Qt3DRender::Scene3DRenderer::isYUp() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer5isYUpEv',
    )

  def hasShutdown(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Scene3DRenderer::hasShutdown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#hasShutdown
    """
    #  bool Qt3DRender::Scene3DRenderer::hasShutdown() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer11hasShutdownEv',
    )

  def renderAspect(self) -> Optional[Qt3DRender.QRenderAspect]:
    """
    Calls Qt's 'QRenderAspect *Qt3DRender::Scene3DRenderer::renderAspect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#renderAspect

    Returns
    -------

    Optional[Qt3DRender.QRenderAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspect *Qt3DRender::Scene3DRenderer::renderAspect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15Scene3DRenderer12renderAspectEv',
    )
    return Qt3DRender.QRenderAspect._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.Scene3DItem.CompositingMode)
  def setCompositingMode(
      self,
      mode: Qt3DRender.Scene3DItem.CompositingMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Scene3DRenderer::setCompositingMode(Scene3DItem::
    CompositingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#setCompositingMode

    Parameters
    ----------

    mode : Qt3DRender.Scene3DItem.CompositingMode
      Passed on as its number.
    """
    #  void Qt3DRender::Scene3DRenderer::setCompositingMode(Scene3DItem::
    #      CompositingMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer18setCompositingModeENS_11Sc'
        'ene3DItem15CompositingModeE',
        mode.value,
    )

  @overload(bool)
  def setSkipFrame(self, skip: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::setSkipFrame(bool skip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#setSkipFrame

    Parameters
    ----------

    skip : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Scene3DRenderer::setSkipFrame(bool skip)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer12setSkipFrameEb', skip,
    )

  @overload(bool)
  def setMultisample(self, multisample: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::setMultisample(bool
    multisample)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#setMultisample

    Parameters
    ----------

    multisample : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Scene3DRenderer::setMultisample(bool multisample)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer14setMultisampleEb',
        multisample,
    )

  @overload(QSize)
  def setBoundingSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::setBoundingSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#setBoundingSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Qt3DRender::Scene3DRenderer::setBoundingSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer15setBoundingSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::setWindow(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Scene3DRenderer::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer9setWindowEP12QQuickWindow',
        self._addressOf(window),
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
    Qt's 'Qt3DRender::Scene3DRenderer::Scene3DRenderer()': leans on
    'Qt3DRender::Scene3DRenderer::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DRenderer.__init__' has no cute function yet. "
        "Qt's 'Qt3DRender::Scene3DRenderer::Scene3DRenderer()': leans on "
        "'Qt3DRender::Scene3DRenderer::qt_metacall(QMetaObject::Call, int, "
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

  def allowRender(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::allowRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#allowRender
    """
    #  void Qt3DRender::Scene3DRenderer::allowRender()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer11allowRenderEv',
    )

  def beforeSynchronize(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::beforeSynchronize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#beforeSynchronize
    """
    #  void Qt3DRender::Scene3DRenderer::beforeSynchronize()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15Scene3DRenderer17beforeSynchronizeEv',
    )

  def shutdown(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Scene3DRenderer::shutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-scene3drenderer.html#shutdown
    """
    #  void Qt3DRender::Scene3DRenderer::shutdown()
    self.uglySide.call('ritual_ZN10Qt3DRender15Scene3DRenderer8shutdownEv')

  @staticmethod
  def init(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DRender::Scene3DRenderer::init(Scene3DItem *item,
      Qt3DCore::QAspectEngine *aspectEngine, QRenderAspect *renderAspect)':
      cannot be called and cannot be called through the meta-object and
      cannot be copied: no header file has its code, Qt's source does not
      mark it or its class for use from outside Qt or writes it 'inline' or
      nowhere, and it is no signal, slot or invokable function giving back
      nothing, of a class built on QObject, and Qt's source has no code for
      it that could be told from the rest.
    - Qt's 'void Qt3DRender::Scene3DRenderer::init(Qt3DCore::QAspectEngine
      *aspectEngine, QRenderAspect *renderAspect)': leans on 'vtable for
      Qt3DRender::Scene3DRenderer::GLRenderer', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DRenderer.init' has no cute function yet. Qt's "
        "'void Qt3DRender::Scene3DRenderer::init(Scene3DItem *item, "
        "Qt3DCore::QAspectEngine *aspectEngine, QRenderAspect "
        "*renderAspect)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's 'void "
        "Qt3DRender::Scene3DRenderer::init(Qt3DCore::QAspectEngine "
        "*aspectEngine, QRenderAspect *renderAspect)': leans on 'vtable for "
        "Qt3DRender::Scene3DRenderer::GLRenderer', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setCleanerHelper(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Scene3DRenderer::setCleanerHelper(Scene3DCleaner
    *cleaner)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.Scene3DRenderer.setCleanerHelper' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Scene3DRenderer::setCleanerHelper(Scene3DCleaner "
        "*cleaner)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
