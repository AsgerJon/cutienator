"""
QSGAbstractRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGAbstractRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QRectF, QSize
  from ..QtGui import QColor, QMatrix4x4
  from . import QSGAbstractRendererPrivate, QSGRootNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSGRootNode = WAIT['QSGRootNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGAbstractRenderer(QObject):
  """
  The cute side of Qt's QSGAbstractRenderer: a plain Python object standing
  in front of one C++ QSGAbstractRenderer.

  It is built on the cute 'QObject', as Qt's QSGAbstractRenderer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGAbstractRenderer that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'setRootNode',
  'rootNode', 'setDeviceRect', 'deviceRect', 'setViewportRect',
  'viewportRect', 'setProjectionMatrixToRect', 'setProjectionMatrix',
  'setProjectionMatrixWithNativeNDC', 'projectionMatrix',
  'projectionMatrixWithNativeNDC', 'projectionMatrixCount',
  'projectionMatrixWithNativeNDCCount', 'setInvertFrontFace',
  'invertFrontFace', 'setClearColor', 'clearColor', 'renderScene',
  'prepareSceneInline', 'renderSceneInline', 'sceneGraphChanged',
  'nodeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGAbstractRenderer::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGAbstractRenderer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGAbstractRenderer::~QSGAbstractRenderer()': the destructor:
    Python never removes a C++ QSGAbstractRenderer.
  - Qt's 'const QSGAbstractRendererPrivate *QSGAbstractRenderer::d_func()
    const': takes in Python what 'QSGAbstractRendererPrivate
    *QSGAbstractRenderer::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGAbstractRenderer is created at the first use, not by
    'QSGAbstractRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGAbstractRenderer.
  - Qt tells when it has removed the C++ QSGAbstractRenderer. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSGAbstractRenderer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MatrixTransformFlag(CuteFlags):
    """
    The flags enum 'QSGAbstractRenderer::MatrixTransformFlag' of Qt, with the
    1 names Qt gives in it. Qt names the type of its combinations
    'QSGAbstractRenderer::MatrixTransformFlags'.
    """

    MatrixTransformFlipY = 0x1

  MatrixTransformFlags = MatrixTransformFlag

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
    Calls Qt's 'QString QSGAbstractRenderer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgabstractrenderer.html#tr

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
    #  QString QSGAbstractRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QSGAbstractRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGAbstractRenderer'

  #  A C++ QSGAbstractRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGAbstractRenderer'

  #  The functions Qt calls itself that QSGAbstractRenderer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'renderScene': (
          ('_ZN19QSGAbstractRenderer11renderSceneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'prepareSceneInline': (
          ('_ZN19QSGAbstractRenderer18prepareSceneInlineEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'renderSceneInline': (
          ('_ZN19QSGAbstractRenderer17renderSceneInlineEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'nodeChanged': (
          ('_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13Di'
           'rtyStateBitEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('int', 'flags', 'QtQuick:QSGNode.DirtyStateBit'),
           )),
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
    Calls Qt's 'const QMetaObject *QSGAbstractRenderer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGAbstractRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rootNode(self) -> Optional[QSGRootNode]:
    """
    Calls Qt's 'QSGRootNode *QSGAbstractRenderer::rootNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgabstractrenderer.html#rootNode

    Returns
    -------

    Optional[QSGRootNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRootNode *QSGAbstractRenderer::rootNode() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer8rootNodeEv',
    )
    from . import QSGRootNode
    return QSGRootNode._cuteAt(address)

  def deviceRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSGAbstractRenderer::deviceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#deviceRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGAbstractRenderer::deviceRect() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer10deviceRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewportRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSGAbstractRenderer::viewportRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#viewportRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGAbstractRenderer::viewportRect() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer12viewportRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def projectionMatrix(self, index: int) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSGAbstractRenderer::projectionMatrix(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#projectionMatrix

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGAbstractRenderer::projectionMatrix(int index) const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer16projectionMatrixEi', index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(int)
  def projectionMatrixWithNativeNDC(self, index: int) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    QSGAbstractRenderer::projectionMatrixWithNativeNDC(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGAbstractRenderer::projectionMatrixWithNativeNDC(int
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer29projectionMatrixWithNativeNDCEi',
        index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def projectionMatrixCount(self) -> int:
    """
    Calls Qt's 'int QSGAbstractRenderer::projectionMatrixCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#projectionMatrixCount
    """
    #  int QSGAbstractRenderer::projectionMatrixCount() const
    return self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer21projectionMatrixCountEv',
    )

  def projectionMatrixWithNativeNDCCount(self) -> int:
    """
    Calls Qt's 'int QSGAbstractRenderer::projectionMatrixWithNativeNDCCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html
    """
    #  int QSGAbstractRenderer::projectionMatrixWithNativeNDCCount() const
    return self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer34projectionMatrixWithNativeNDCCoun'
        'tEv',
    )

  def invertFrontFace(self) -> bool:
    """
    Calls Qt's 'bool QSGAbstractRenderer::invertFrontFace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#invertFrontFace
    """
    #  bool QSGAbstractRenderer::invertFrontFace() const
    return self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer15invertFrontFaceEv',
    )

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGAbstractRenderer::clearColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGAbstractRenderer::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGAbstractRenderer10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGRootNode)
  @overload(NoneType)
  def setRootNode(self, node: Optional[QSGRootNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setRootNode(QSGRootNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setRootNode

    Parameters
    ----------

    node : Optional[QSGRootNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractRenderer::setRootNode(QSGRootNode *node)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer11setRootNodeEP11QSGRootNode',
        self._addressOf(node, 'QSGRootNode'),
    )

  @overload(QRect)
  def setDeviceRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setDeviceRect(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setDeviceRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSGAbstractRenderer::setDeviceRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer13setDeviceRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(QSize)
  def setDeviceRect(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setDeviceRect(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setDeviceRect

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGAbstractRenderer::setDeviceRect(const QSize &size)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer13setDeviceRectERK5QSize',
        self._valueOf(size),
    )

  @overload(QRect)
  def setViewportRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setViewportRect(const QRect
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setViewportRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSGAbstractRenderer::setViewportRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer15setViewportRectERK5QRect',
        self._valueOf(rect),
    )

  @overload(QSize)
  def setViewportRect(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setViewportRect(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setViewportRect

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGAbstractRenderer::setViewportRect(const QSize &size)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer15setViewportRectERK5QSize',
        self._valueOf(size),
    )

  @overload(QRectF)
  def setProjectionMatrixToRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setProjectionMatrixToRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setProjectionMatrixToRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF
    #      &rect)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRect'
        'F',
        self._valueOf(rect),
    )

  @overload(QRectF, MatrixTransformFlags)
  def setProjectionMatrixToRect(
      self,
      rect: QRectF,
      flags: MatrixTransformFlags,
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setProjectionMatrixToRect(const
    QRectF &rect, MatrixTransformFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setProjectionMatrixToRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : MatrixTransformFlags
      Passed on as its number.
    """
    #  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF
    #      &rect, MatrixTransformFlags flags)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRect'
        'F6QFlagsINS_19MatrixTransformFlagEE',
        self._valueOf(rect), flags.value,
    )

  @overload(QRectF, MatrixTransformFlags, bool)
  def setProjectionMatrixToRect(
      self,
      rect: QRectF,
      flags: MatrixTransformFlags,
      nativeNDCFlipY: bool,
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setProjectionMatrixToRect(const
    QRectF &rect, MatrixTransformFlags flags, bool nativeNDCFlipY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setProjectionMatrixToRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : MatrixTransformFlags
      Passed on as its number.

    nativeNDCFlipY : bool
      Passed on as it is.
    """
    #  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF
    #      &rect, MatrixTransformFlags flags, bool nativeNDCFlipY)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRect'
        'F6QFlagsINS_19MatrixTransformFlagEEb',
        self._valueOf(rect), flags.value, nativeNDCFlipY,
    )

  @overload(QMatrix4x4)
  @overload(QMatrix4x4, int)
  def setProjectionMatrix(self, matrix: QMatrix4x4, index: int = 0) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setProjectionMatrix(const
    QMatrix4x4 &matrix, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setProjectionMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QSGAbstractRenderer::setProjectionMatrix(const QMatrix4x4
    #      &matrix, int index)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer19setProjectionMatrixERK10QMatrix4x4'
        'i',
        self._valueOf(matrix), index,
    )

  @overload(QMatrix4x4)
  @overload(QMatrix4x4, int)
  def setProjectionMatrixWithNativeNDC(
      self,
      matrix: QMatrix4x4,
      index: int = 0,
  ) -> None:
    """
    Calls Qt's 'void
    QSGAbstractRenderer::setProjectionMatrixWithNativeNDC(const QMatrix4x4
    &matrix, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QSGAbstractRenderer::setProjectionMatrixWithNativeNDC(const
    #      QMatrix4x4 &matrix, int index)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer32setProjectionMatrixWithNativeNDCER'
        'K10QMatrix4x4i',
        self._valueOf(matrix), index,
    )

  @overload(bool)
  def setInvertFrontFace(self, invert: bool) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setInvertFrontFace(bool invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setInvertFrontFace

    Parameters
    ----------

    invert : bool
      Passed on as it is.
    """
    #  void QSGAbstractRenderer::setInvertFrontFace(bool invert)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer18setInvertFrontFaceEb', invert,
    )

  @overload(QColor)
  def setClearColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::setClearColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#setClearColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGAbstractRenderer::setClearColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer13setClearColorERK6QColor',
        self._valueOf(color),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSGAbstractRenderer::QSGAbstractRenderer(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#QSGAbstractRenderer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSGAbstractRenderer::QSGAbstractRenderer(QObject *parent)
    self._noteCreation(QSGAbstractRenderer, lambda: Rituals.call(
        'ritual_ZN19QSGAbstractRendererC1EP7QObject',
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

  def renderScene(self) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::renderScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#renderScene
    """
    #  void QSGAbstractRenderer::renderScene()
    self.uglySide.call('ritual_ZN19QSGAbstractRenderer11renderSceneEv')

  def prepareSceneInline(self) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::prepareSceneInline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#prepareSceneInline
    """
    #  void QSGAbstractRenderer::prepareSceneInline()
    ritual = 'ritual_ZN19QSGAbstractRenderer18prepareSceneInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGAbstractRenderer18prepareSceneInlineEv'
    self.uglySide.call(ritual)

  def renderSceneInline(self) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::renderSceneInline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#renderSceneInline
    """
    #  void QSGAbstractRenderer::renderSceneInline()
    ritual = 'ritual_ZN19QSGAbstractRenderer17renderSceneInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGAbstractRenderer17renderSceneInlineEv'
    self.uglySide.call(ritual)

  def sceneGraphChanged(self) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::sceneGraphChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#sceneGraphChanged
    """
    #  void QSGAbstractRenderer::sceneGraphChanged()
    self.uglySide.call('ritual_ZN19QSGAbstractRenderer17sceneGraphChangedEv')

  @overload(QSGNode, QSGNode.DirtyState)
  @overload(NoneType, QSGNode.DirtyState)
  def nodeChanged(
      self,
      node: Optional[QSGNode],
      state: QSGNode.DirtyState,
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractRenderer::nodeChanged(QSGNode *node,
    QSGNode::DirtyState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractrenderer.html#nodeChanged

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QSGNode.DirtyState
      Passed on as its number.
    """
    #  void QSGAbstractRenderer::nodeChanged(QSGNode *node,
    #      QSGNode::DirtyState state)
    self.uglySide.call(
        'ritual_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_1'
        '3DirtyStateBitEE',
        self._addressOf(node, 'QSGNode'), state.value,
    )

  def d_func(self) -> Optional[QSGAbstractRendererPrivate]:
    """
    Calls Qt's 'QSGAbstractRendererPrivate *QSGAbstractRenderer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgabstractrenderer.html#d_func

    Returns
    -------

    Optional[QSGAbstractRendererPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGAbstractRendererPrivate *QSGAbstractRenderer::d_func()
    address = self.uglySide.call('ritual_ZN19QSGAbstractRenderer6d_funcEv')
    from . import QSGAbstractRendererPrivate
    return QSGAbstractRendererPrivate._cuteAt(address)
