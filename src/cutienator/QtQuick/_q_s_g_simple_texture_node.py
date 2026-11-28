"""
QSGSimpleTextureNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgsimpletexturenode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from . import QSGGeometryNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSimpleTextureNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGSimpleTextureNode: a plain Python object standing
  in front of one C++ QSGSimpleTextureNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGSimpleTextureNode is
  built on Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSimpleTextureNode that has a ritual and that
  Python can call so far, 12 names in all: 'setRect', 'rect',
  'setSourceRect', 'sourceRect', 'setTexture', 'texture', 'setFiltering',
  'filtering', 'setTextureCoordinatesTransform',
  'textureCoordinatesTransform', 'setOwnsTexture', 'ownsTexture'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSimpleTextureNode::~QSGSimpleTextureNode()': the destructor:
    Python never removes a C++ QSGSimpleTextureNode.
  - Qt's 'QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()': gives
    'QSGSimpleTextureNodePrivate', which has no cute class yet.
  - Qt's 'const QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()
    const': gives 'QSGSimpleTextureNodePrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSGSimpleTextureNode is created at the first use, not by
    'QSGSimpleTextureNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSimpleTextureNode.
  - Each name of Qt's QSGSimpleTextureNode that has no cute function yet,
    'd_func', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QSGSimpleTextureNode, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TextureCoordinatesTransformFlag(CuteFlags):
    """
    The flags enum 'QSGSimpleTextureNode::TextureCoordinatesTransformFlag' of
    Qt, with the 3 names Qt gives in it. Qt names the type of its
    combinations 'QSGSimpleTextureNode::TextureCoordinatesTransformMode'.
    """

    NoTransform = 0x0
    MirrorHorizontally = 0x1
    MirrorVertically = 0x2

  TextureCoordinatesTransformMode = TextureCoordinatesTransformFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSimpleTextureNode'

  #  A C++ QSGSimpleTextureNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSimpleTextureNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSimpleTextureNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimpletexturenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSimpleTextureNode::rect() const
    address = self._callAs(
        'QSGSimpleTextureNode', 'ritual_ZNK20QSGSimpleTextureNode4rectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSimpleTextureNode::sourceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSimpleTextureNode::sourceRect() const
    address = self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZNK20QSGSimpleTextureNode10sourceRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGSimpleTextureNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimpletexturenode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGSimpleTextureNode::texture() const
    address = self._callAs(
        'QSGSimpleTextureNode', 'ritual_ZNK20QSGSimpleTextureNode7textureEv',
    )
    return QSGTexture._cuteAt(address)

  def filtering(self) -> QSGTexture.Filtering:
    """
    Calls Qt's 'QSGTexture::Filtering QSGSimpleTextureNode::filtering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#filtering

    Returns
    -------

    QSGTexture.Filtering
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTexture.Filtering(number)' gives.
    """
    #  QSGTexture::Filtering QSGSimpleTextureNode::filtering() const
    return QSGTexture.Filtering(self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZNK20QSGSimpleTextureNode9filteringEv',
    ))

  def textureCoordinatesTransform(self) -> TextureCoordinatesTransformMode:
    """
    Calls Qt's 'TextureCoordinatesTransformMode
    QSGSimpleTextureNode::textureCoordinatesTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html

    Returns
    -------

    TextureCoordinatesTransformMode
      The value standing for the combination Qt gave back.
    """
    #  TextureCoordinatesTransformMode
    #      QSGSimpleTextureNode::textureCoordinatesTransform() const
    return QSGSimpleTextureNode.TextureCoordinatesTransformMode(self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZNK20QSGSimpleTextureNode27textureCoordinatesTransformEv',
    ))

  def ownsTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGSimpleTextureNode::ownsTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#ownsTexture
    """
    #  bool QSGSimpleTextureNode::ownsTexture() const
    return self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZNK20QSGSimpleTextureNode11ownsTextureEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSimpleTextureNode::setRect(const QRectF &rect)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QSGSimpleTextureNode::setRect(qreal x, qreal y, qreal w, qreal h)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode7setRectEdddd',
        x, y, w, h,
    )

  @overload(QRectF)
  def setSourceRect(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setSourceRect(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setSourceRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSimpleTextureNode::setSourceRect(const QRectF &r)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode13setSourceRectERK6QRectF',
        self._valueOf(r),
    )

  @overload(float, float, float, float)
  def setSourceRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setSourceRect(qreal x, qreal y,
    qreal w, qreal h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setSourceRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QSGSimpleTextureNode::setSourceRect(qreal x, qreal y, qreal w,
    #      qreal h)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode13setSourceRectEdddd',
        x, y, w, h,
    )

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSimpleTextureNode::setTexture(QSGTexture *texture)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSimpleTextureNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode12setFilteringEN10QSGTexture9Filter'
        'ingE',
        filtering.value,
    )

  @overload(TextureCoordinatesTransformMode)
  def setTextureCoordinatesTransform(
      self,
      mode: TextureCoordinatesTransformMode,
  ) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setTextureCoordinatesTransform(
    TextureCoordinatesTransformMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html

    Parameters
    ----------

    mode : TextureCoordinatesTransformMode
      Passed on as its number.
    """
    #  void QSGSimpleTextureNode::setTextureCoordinatesTransform(
    #      TextureCoordinatesTransformMode mode)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode30setTextureCoordinatesTransformE6Q'
        'FlagsINS_31TextureCoordinatesTransformFlagEE',
        mode.value,
    )

  @overload(bool)
  def setOwnsTexture(self, owns: bool) -> None:
    """
    Calls Qt's 'void QSGSimpleTextureNode::setOwnsTexture(bool owns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#setOwnsTexture

    Parameters
    ----------

    owns : bool
      Passed on as it is.
    """
    #  void QSGSimpleTextureNode::setOwnsTexture(bool owns)
    self._callAs(
        'QSGSimpleTextureNode',
        'ritual_ZN20QSGSimpleTextureNode14setOwnsTextureEb',
        owns,
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
    'QSGSimpleTextureNode::QSGSimpleTextureNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimpletexturenode.html#QSGSimpleTextureNode
    """
    #  QSGSimpleTextureNode::QSGSimpleTextureNode()
    self._noteCreation(QSGSimpleTextureNode, lambda: Rituals.call(
        'ritual_ZN20QSGSimpleTextureNodeC1Ev',
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()':
      gives 'QSGSimpleTextureNodePrivate', which has no cute class yet.
    - Qt's 'const QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()
      const': gives 'QSGSimpleTextureNodePrivate', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QSGSimpleTextureNode.d_func' has no cute function yet. Qt's "
        "'QSGSimpleTextureNodePrivate *QSGSimpleTextureNode::d_func()': "
        "gives 'QSGSimpleTextureNodePrivate', which has no cute class yet. "
        "Qt's 'const QSGSimpleTextureNodePrivate "
        "*QSGSimpleTextureNode::d_func() const': gives "
        "'QSGSimpleTextureNodePrivate', which has no cute class yet.")
