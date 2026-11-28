"""
QOpenGLTextureBlitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengltextureblitter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect, QRectF
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']


class QOpenGLTextureBlitter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLTextureBlitter: a plain Python object standing
  in front of one C++ QOpenGLTextureBlitter.

  What exists
  -----------

  Every function of Qt's QOpenGLTextureBlitter that has a ritual and that
  Python can call so far, 11 names in all: 'create', 'isCreated', 'destroy',
  'supportsExternalOESTarget', 'supportsRectangleTarget', 'bind', 'release',
  'setRedBlueSwizzle', 'setOpacity', 'blit', 'targetTransform'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLTextureBlitter::~QOpenGLTextureBlitter()': the destructor:
    Python never removes a C++ QOpenGLTextureBlitter.
  - Qt's 'void QOpenGLTextureBlitter::blit(GLuint texture, const QMatrix4x4
    &targetTransform, const QMatrix3x3 &sourceTransform)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMatrix3x3 QOpenGLTextureBlitter::sourceTransform(const QRectF
    &subTexture, const QSize &textureSize, Origin origin)': gives a type
    Python has no way to take yet.
  - Qt's 'QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func()':
    gives 'QOpenGLTextureBlitterPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func()
    const': gives 'QOpenGLTextureBlitterPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLTextureBlitter is created at the first use, not by
    'QOpenGLTextureBlitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTextureBlitter.
  - Each name of Qt's QOpenGLTextureBlitter that has no cute function yet,
    'd_func', 'sourceTransform', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpenGLTextureBlitter, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Origin(CuteNum):
    """
    The enum 'QOpenGLTextureBlitter::Origin' of Qt, with the 2 names Qt gives
    in it.
    """

    OriginBottomLeft = Kee[int](0)
    OriginTopLeft = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRectF, QRect)
  def targetTransform(target: QRectF, viewport: QRect) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QOpenGLTextureBlitter::targetTransform(const
    QRectF &target, const QRect &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#targetTransform

    Parameters
    ----------

    target : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QOpenGLTextureBlitter::targetTransform(const QRectF
    #      &target, const QRect &viewport)
    address = Rituals.call(
        'ritual_ZN21QOpenGLTextureBlitter15targetTransformERK6QRectFRK5QRec'
        't',
        CuteMixin._valueOf(target), CuteMixin._valueOf(viewport),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTextureBlitter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTextureBlitter::isCreated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#isCreated
    """
    #  bool QOpenGLTextureBlitter::isCreated() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTextureBlitter9isCreatedEv',
    )

  def supportsExternalOESTarget(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTextureBlitter::supportsExternalOESTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html
    """
    #  bool QOpenGLTextureBlitter::supportsExternalOESTarget() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTextureBlitter25supportsExternalOESTargetEv',
    )

  def supportsRectangleTarget(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTextureBlitter::supportsRectangleTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#supportsRectangleTarget
    """
    #  bool QOpenGLTextureBlitter::supportsRectangleTarget() const
    return self.uglySide.call(
        'ritual_ZNK21QOpenGLTextureBlitter23supportsRectangleTargetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRedBlueSwizzle(self, swizzle: bool) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::setRedBlueSwizzle(bool swizzle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#setRedBlueSwizzle

    Parameters
    ----------

    swizzle : bool
      Passed on as it is.
    """
    #  void QOpenGLTextureBlitter::setRedBlueSwizzle(bool swizzle)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTextureBlitter17setRedBlueSwizzleEb', swizzle,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::setOpacity(float opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QOpenGLTextureBlitter::setOpacity(float opacity)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTextureBlitter10setOpacityEf', opacity,
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
    'QOpenGLTextureBlitter::QOpenGLTextureBlitter()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltextureblitter.html#QOpenGLTextureBlitter
    """
    #  QOpenGLTextureBlitter::QOpenGLTextureBlitter()
    self._noteCreation(QOpenGLTextureBlitter, lambda: Rituals.call(
        'ritual_ZN21QOpenGLTextureBlitterC1Ev',
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTextureBlitter::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureblitter.html#create
    """
    #  bool QOpenGLTextureBlitter::create()
    return self.uglySide.call('ritual_ZN21QOpenGLTextureBlitter6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureblitter.html#destroy
    """
    #  void QOpenGLTextureBlitter::destroy()
    self.uglySide.call('ritual_ZN21QOpenGLTextureBlitter7destroyEv')

  @overload()
  @overload(int)
  def bind(self, target: int = 3553) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::bind(GLenum target)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureblitter.html#bind

    Parameters
    ----------

    target : int
      Passed on as it is. May be left out, as in Qt: it is then 3553.
    """
    #  void QOpenGLTextureBlitter::bind(GLenum target)
    self.uglySide.call('ritual_ZN21QOpenGLTextureBlitter4bindEj', target)

  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureblitter.html#release
    """
    #  void QOpenGLTextureBlitter::release()
    self.uglySide.call('ritual_ZN21QOpenGLTextureBlitter7releaseEv')

  @overload(int, QMatrix4x4, Origin)
  def blit(
      self,
      texture: int,
      targetTransform: QMatrix4x4,
      sourceOrigin: Origin,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureBlitter::blit(GLuint texture, const
    QMatrix4x4 &targetTransform, Origin sourceOrigin)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltextureblitter.html#blit

    Parameters
    ----------

    texture : int
      Passed on as it is.

    targetTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    sourceOrigin : Origin
      Passed on as its number.
    """
    #  void QOpenGLTextureBlitter::blit(GLuint texture, const QMatrix4x4
    #      &targetTransform, Origin sourceOrigin)
    self.uglySide.call(
        'ritual_ZN21QOpenGLTextureBlitter4blitEjRK10QMatrix4x4NS_6OriginE',
        texture, self._valueOf(targetTransform), sourceOrigin.value,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func()':
      gives 'QOpenGLTextureBlitterPrivate', which has no cute class yet.
    - Qt's 'const QOpenGLTextureBlitterPrivate
      *QOpenGLTextureBlitter::d_func() const': gives
      'QOpenGLTextureBlitterPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureBlitter.d_func' has no cute function yet. Qt's "
        "'QOpenGLTextureBlitterPrivate *QOpenGLTextureBlitter::d_func()': "
        "gives 'QOpenGLTextureBlitterPrivate', which has no cute class yet. "
        "Qt's 'const QOpenGLTextureBlitterPrivate "
        "*QOpenGLTextureBlitter::d_func() const': gives "
        "'QOpenGLTextureBlitterPrivate', which has no cute class yet.")

  @staticmethod
  def sourceTransform(*__, **_) -> Never:
    """
    Qt's 'QMatrix3x3 QOpenGLTextureBlitter::sourceTransform(const QRectF
    &subTexture, const QSize &textureSize, Origin origin)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureBlitter.sourceTransform' has no cute function yet. "
        "Qt's 'QMatrix3x3 QOpenGLTextureBlitter::sourceTransform(const "
        "QRectF &subTexture, const QSize &textureSize, Origin origin)': "
        "gives a type Python has no way to take yet.")
