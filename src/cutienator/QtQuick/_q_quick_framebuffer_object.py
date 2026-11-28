"""
QQuickFramebufferObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickframebufferobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from . import QSGNode, QSGTextureProvider
  from ..QtOpenGL import QOpenGLFramebufferObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFramebufferObject(QQuickItem):
  """
  The cute side of Qt's QQuickFramebufferObject: a plain Python object
  standing in front of one C++ QQuickFramebufferObject.

  It is built on the cute 'QQuickItem', as Qt's QQuickFramebufferObject is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFramebufferObject that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'textureFollowsItemSize', 'setTextureFollowsItemSize', 'mirrorVertically',
  'setMirrorVertically', 'createRenderer', 'isTextureProvider',
  'textureProvider', 'releaseResources', 'geometryChange', 'updatePaintNode',
  'textureFollowsItemSizeChanged', 'mirrorVerticallyChanged',
  'invalidateSceneGraph'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFramebufferObject::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFramebufferObject::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFramebufferObjectPrivate *QQuickFramebufferObject::d_func()':
    gives 'QQuickFramebufferObjectPrivate', which has no cute class yet.
  - Qt's 'const QQuickFramebufferObjectPrivate
    *QQuickFramebufferObject::d_func() const': gives
    'QQuickFramebufferObjectPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQuickFramebufferObject is created at the first use, not by
    'QQuickFramebufferObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFramebufferObject.
  - Qt tells when it has removed the C++ QQuickFramebufferObject. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFramebufferObject that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QQuickFramebufferObject, each a class in
  #  here as in C++.

  class Renderer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickFramebufferObject::Renderer: a plain Python
    object standing in front of one C++ QQuickFramebufferObject::Renderer.

    What exists
    -----------

    Every function of Qt's QQuickFramebufferObject::Renderer that has a
    ritual and that Python can call so far, 6 names in all: 'render',
    'createFramebufferObject', 'synchronize', 'framebufferObject', 'update',
    'invalidateFramebufferObject'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickFramebufferObject::Renderer::~Renderer()': the destructor:
      Python never removes a C++ QQuickFramebufferObject::Renderer.

    What to expect
    --------------

    - The C++ QQuickFramebufferObject::Renderer is created at the first use,
      not by 'QQuickFramebufferObject::Renderer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQuickFramebufferObject::Renderer.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuickFramebufferObject = WAIT['QQuickFramebufferObject']
      QSize = WAIT['QSize']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickFramebufferObject::Renderer'

    #  A C++ QQuickFramebufferObject::Renderer Python makes is of a C++ class
    #  of ours, in which Python can take functions over. This ritual hands
    #  one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuickFramebufferObject_Renderer'

    #  The functions Qt calls itself that QQuickFramebufferObject::Renderer
    #  is the first to declare. A class of a program built on it can write
    #  one anew, and Qt then calls that. For each name: the key C++ knows the
    #  function by, what it gives, and what it takes.
    __virtual_functions__ = {
        'render': (
            ('_ZN23QQuickFramebufferObject8Renderer6renderEv',
             ('nothing', 'nothing', ''),
             ()),
        ),
        'createFramebufferObject': (
            ('_ZN23QQuickFramebufferObject8Renderer23createFramebufferObjec'
             'tERK5QSize',
             ('address', 'address', 'QtOpenGL:QOpenGLFramebufferObject'),
             (
                 ('address', 'value', 'QtCore:QSize'),
             )),
        ),
        'synchronize': (
            ('_ZN23QQuickFramebufferObject8Renderer11synchronizeEPS_',
             ('nothing', 'nothing', ''),
             (
                 ('address', 'address', 'QtQuick:QQuickFramebufferObject'),
             )),
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def framebufferObject(self) -> Optional[QOpenGLFramebufferObject]:
      """
      Calls Qt's 'QOpenGLFramebufferObject
      *QQuickFramebufferObject::Renderer::framebufferObject() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html

      Returns
      -------

      Optional[QOpenGLFramebufferObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QOpenGLFramebufferObject
      #      *QQuickFramebufferObject::Renderer::framebufferObject() const
      address = self.uglySide.call(
          'ritual_ZNK23QQuickFramebufferObject8Renderer17framebufferObjectE'
          'v',
      )
      from ..QtOpenGL import QOpenGLFramebufferObject
      return QOpenGLFramebufferObject._cuteAt(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickFramebufferObject::Renderer::Renderer()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html#Renderer
      """
      #  QQuickFramebufferObject::Renderer::Renderer()
      self._noteCreation(
          QQuickFramebufferObject.Renderer, lambda: Rituals.call(
              'ritual_ZN23QQuickFramebufferObject8RendererC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def render(self) -> None:
      """
      Calls Qt's 'void QQuickFramebufferObject::Renderer::render()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html#render
      """
      #  void QQuickFramebufferObject::Renderer::render()
      self.uglySide.call(
          'ritual_ZN23QQuickFramebufferObject8Renderer6renderEv',
      )

    @overload(QSize)
    def createFramebufferObject(
        self,
        size: QSize,
    ) -> Optional[QOpenGLFramebufferObject]:
      """
      Calls Qt's 'QOpenGLFramebufferObject
      *QQuickFramebufferObject::Renderer::createFramebufferObject(const QSize
      &size)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html

      Parameters
      ----------

      size : QSize
        Passed on as a value: Qt reads the C++ QSize, which stays Python's
        own.

      Returns
      -------

      Optional[QOpenGLFramebufferObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QOpenGLFramebufferObject
      #      *QQuickFramebufferObject::Renderer::createFramebufferObject(
      #      const QSize &size)
      ritual = (
          'ritual_ZN23QQuickFramebufferObject8Renderer23createFramebufferOb'
          'jectERK5QSize')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN23QQuickFramebufferObject8Renderer23createFramebu'
            'fferObjectERK5QSize')
      address = self.uglySide.call(ritual, self._valueOf(size))
      from ..QtOpenGL import QOpenGLFramebufferObject
      return QOpenGLFramebufferObject._cuteAt(address)

    @overload(QQuickFramebufferObject)
    @overload(NoneType)
    def synchronize(self, a0: Optional[QQuickFramebufferObject]) -> None:
      """
      Calls Qt's 'void
      QQuickFramebufferObject::Renderer::synchronize(QQuickFramebufferObject
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html

      Parameters
      ----------

      a0 : Optional[QQuickFramebufferObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QQuickFramebufferObject::Renderer::synchronize(
      #      QQuickFramebufferObject *a0)
      ritual = 'ritual_ZN23QQuickFramebufferObject8Renderer11synchronizeEPS_'
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN23QQuickFramebufferObject8Renderer11synchronizeEP'
            'S_')
      self.uglySide.call(ritual, self._addressOf(a0))

    def update(self) -> None:
      """
      Calls Qt's 'void QQuickFramebufferObject::Renderer::update()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html#update
      """
      #  void QQuickFramebufferObject::Renderer::update()
      self.uglySide.call(
          'ritual_ZN23QQuickFramebufferObject8Renderer6updateEv',
      )

    def invalidateFramebufferObject(self) -> None:
      """
      Calls Qt's 'void
      QQuickFramebufferObject::Renderer::invalidateFramebufferObject()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickframebufferobject-renderer.html
      """
      #  void
      #      QQuickFramebufferObject::Renderer::invalidateFramebufferObject()
      self.uglySide.call(
          'ritual_ZN23QQuickFramebufferObject8Renderer27invalidateFramebuff'
          'erObjectEv',
      )

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
    Calls Qt's 'QString QQuickFramebufferObject::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframebufferobject.html#tr

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
    #  QString QQuickFramebufferObject::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickFramebufferObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFramebufferObject'

  #  The functions Qt calls itself that QQuickFramebufferObject is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createRenderer': (
          ('_ZNK23QQuickFramebufferObject14createRendererEv',
           ('address', 'address',
            'QtQuick:QQuickFramebufferObject.Renderer'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFramebufferObject::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFramebufferObject::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickFramebufferObject10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureFollowsItemSize(self) -> bool:
    """
    Calls Qt's 'bool QQuickFramebufferObject::textureFollowsItemSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html
    """
    #  bool QQuickFramebufferObject::textureFollowsItemSize() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickFramebufferObject22textureFollowsItemSizeEv',
    )

  def mirrorVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickFramebufferObject::mirrorVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#mirrorVertically
    """
    #  bool QQuickFramebufferObject::mirrorVertically() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickFramebufferObject16mirrorVerticallyEv',
    )

  def createRenderer(self) -> Optional[Renderer]:
    """
    Calls Qt's 'Renderer *QQuickFramebufferObject::createRenderer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#createRenderer

    Returns
    -------

    Optional[Renderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Renderer *QQuickFramebufferObject::createRenderer() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickFramebufferObject14createRendererEv',
    )
    return QQuickFramebufferObject.Renderer._cuteAt(address)

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuickFramebufferObject::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#isTextureProvider
    """
    #  bool QQuickFramebufferObject::isTextureProvider() const
    ritual = 'ritual_ZNK23QQuickFramebufferObject17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickFramebufferObject17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider
    *QQuickFramebufferObject::textureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuickFramebufferObject::textureProvider() const
    ritual = 'ritual_ZNK23QQuickFramebufferObject15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickFramebufferObject15textureProviderEv'
    address = self.uglySide.call(ritual)
    from . import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTextureFollowsItemSize(self, follows: bool) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::setTextureFollowsItemSize(bool
    follows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html

    Parameters
    ----------

    follows : bool
      Passed on as it is.
    """
    #  void QQuickFramebufferObject::setTextureFollowsItemSize(bool follows)
    self.uglySide.call(
        'ritual_ZN23QQuickFramebufferObject25setTextureFollowsItemSizeEb',
        follows,
    )

  @overload(bool)
  def setMirrorVertically(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::setMirrorVertically(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#setMirrorVertically

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickFramebufferObject::setMirrorVertically(bool enable)
    self.uglySide.call(
        'ritual_ZN23QQuickFramebufferObject19setMirrorVerticallyEb', enable,
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
    Qt's 'QQuickFramebufferObject::QQuickFramebufferObject(QQuickItem
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQuickFramebufferObject.__init__' has no cute function yet. Qt's "
        "'QQuickFramebufferObject::QQuickFramebufferObject(QQuickItem "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#releaseResources
    """
    #  void QQuickFramebufferObject::releaseResources()
    ritual = 'ritual_ZN23QQuickFramebufferObject16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickFramebufferObject16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickFramebufferObject::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN23QQuickFramebufferObject14geometryChangeERK6QRectFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickFramebufferObject14geometryChangeERK6QRectF'
          'S2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickFramebufferObject::updatePaintNode(QSGNode
    *a0, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickFramebufferObject::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN23QQuickFramebufferObject15updatePaintNodeEP7QSGNodePN10Q'
        'QuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickFramebufferObject15updatePaintNodeEP7QSGNod'
          'ePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(bool)
  def textureFollowsItemSizeChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void
    QQuickFramebufferObject::textureFollowsItemSizeChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickFramebufferObject::textureFollowsItemSizeChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickFramebufferObject29textureFollowsItemSizeChangedE'
        'b',
        a0,
    )

  @overload(bool)
  def mirrorVerticallyChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::mirrorVerticallyChanged(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickFramebufferObject::mirrorVerticallyChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickFramebufferObject23mirrorVerticallyChangedEb', a0,
    )

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickFramebufferObject::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframebufferobject.html#invalidateSceneGraph
    """
    #  void QQuickFramebufferObject::invalidateSceneGraph()
    self.uglySide.call(
        'ritual_ZN23QQuickFramebufferObject20invalidateSceneGraphEv',
    )
