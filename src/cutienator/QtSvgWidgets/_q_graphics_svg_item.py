"""
QGraphicsSvgItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvgWidgets/qgraphicssvgitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem, QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QPainter
  from ..QtSvg import QSvgRenderer
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QSize = WAIT['QSize']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QSvgRenderer = WAIT['QSvgRenderer']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSvgItem(QGraphicsObject):
  """
  The cute side of Qt's QGraphicsSvgItem: a plain Python object standing in
  front of one C++ QGraphicsSvgItem.

  It is built on the cute 'QGraphicsObject', as Qt's QGraphicsSvgItem is
  built on Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSvgItem that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'setSharedRenderer',
  'renderer', 'setElementId', 'elementId', 'setCachingEnabled',
  'isCachingEnabled', 'setMaximumCacheSize', 'maximumCacheSize',
  'boundingRect', 'paint', 'type'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphicsSvgItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGraphicsSvgItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsSvgItem::~QGraphicsSvgItem()': the destructor: Python
    never removes a C++ QGraphicsSvgItem.
  - Qt's 'QGraphicsSvgItemPrivate *QGraphicsSvgItem::d_func()': gives
    'QGraphicsSvgItemPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsSvgItemPrivate *QGraphicsSvgItem::d_func() const':
    gives 'QGraphicsSvgItemPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSvgItem is created at the first use, not by
    'QGraphicsSvgItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSvgItem.
  - Qt tells when it has removed the C++ QGraphicsSvgItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QGraphicsSvgItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#tr

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
    #  QString QGraphicsSvgItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QGraphicsSvgItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSvgItem'

  #  A C++ QGraphicsSvgItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSvgItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsSvgItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsSvgItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QGraphicsSvgItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderer(self) -> Optional[QSvgRenderer]:
    """
    Calls Qt's 'QSvgRenderer *QGraphicsSvgItem::renderer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#renderer

    Returns
    -------

    Optional[QSvgRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgRenderer *QGraphicsSvgItem::renderer() const
    address = self.uglySide.call('ritual_ZNK16QGraphicsSvgItem8rendererEv')
    from ..QtSvg import QSvgRenderer
    return QSvgRenderer._cuteAt(address)

  def elementId(self) -> str:
    """
    Calls Qt's 'QString QGraphicsSvgItem::elementId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#elementId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsSvgItem::elementId() const
    return self.uglySide.call('ritual_ZNK16QGraphicsSvgItem9elementIdEv')

  def isCachingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsSvgItem::isCachingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#isCachingEnabled
    """
    #  bool QGraphicsSvgItem::isCachingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QGraphicsSvgItem16isCachingEnabledEv',
    )

  def maximumCacheSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGraphicsSvgItem::maximumCacheSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#maximumCacheSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGraphicsSvgItem::maximumCacheSize() const
    address = self.uglySide.call(
        'ritual_ZNK16QGraphicsSvgItem16maximumCacheSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsSvgItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsSvgItem::boundingRect() const
    ritual = 'ritual_ZNK16QGraphicsSvgItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QGraphicsSvgItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsSvgItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#type
    """
    #  int QGraphicsSvgItem::type() const
    ritual = 'ritual_ZNK16QGraphicsSvgItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QGraphicsSvgItem4typeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgRenderer)
  @overload(NoneType)
  def setSharedRenderer(self, renderer: Optional[QSvgRenderer]) -> None:
    """
    Calls Qt's 'void QGraphicsSvgItem::setSharedRenderer(QSvgRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#setSharedRenderer

    Parameters
    ----------

    renderer : Optional[QSvgRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsSvgItem::setSharedRenderer(QSvgRenderer *renderer)
    self.uglySide.call(
        'ritual_ZN16QGraphicsSvgItem17setSharedRendererEP12QSvgRenderer',
        self._addressOf(renderer),
    )

  @overload(str)
  def setElementId(self, id: str) -> None:
    """
    Calls Qt's 'void QGraphicsSvgItem::setElementId(const QString &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#setElementId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsSvgItem::setElementId(const QString &id)
    self.uglySide.call(
        'ritual_ZN16QGraphicsSvgItem12setElementIdERK7QString', id,
    )

  @overload(bool)
  def setCachingEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QGraphicsSvgItem::setCachingEnabled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#setCachingEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QGraphicsSvgItem::setCachingEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN16QGraphicsSvgItem17setCachingEnabledEb', a0,
    )

  @overload(QSize)
  def setMaximumCacheSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGraphicsSvgItem::setMaximumCacheSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#setMaximumCacheSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGraphicsSvgItem::setMaximumCacheSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN16QGraphicsSvgItem19setMaximumCacheSizeERK5QSize',
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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parentItem: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSvgItem::QGraphicsSvgItem(QGraphicsItem *parentItem)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#QGraphicsSvgItem

    Parameters
    ----------

    parentItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsSvgItem::QGraphicsSvgItem(QGraphicsItem *parentItem)
    self._noteCreation(QGraphicsSvgItem, lambda: Rituals.call(
        'ritual_ZN16QGraphicsSvgItemC1EP13QGraphicsItem',
        self._addressOf(parentItem, 'QGraphicsItem'),
    ))

  @overload(str)
  @overload(str, QGraphicsItem)
  @overload(str, NoneType)
  def __init__(
      self,
      fileName: str,
      parentItem: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGraphicsSvgItem::QGraphicsSvgItem(const
    QString &fileName, QGraphicsItem *parentItem)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssvgitem.html#QGraphicsSvgItem

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    parentItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsSvgItem::QGraphicsSvgItem(const QString &fileName,
    #      QGraphicsItem *parentItem)
    self._noteCreation(QGraphicsSvgItem, lambda: Rituals.call(
        'ritual_ZN16QGraphicsSvgItemC1ERK7QStringP13QGraphicsItem',
        fileName, self._addressOf(parentItem, 'QGraphicsItem'),
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

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsSvgItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssvgitem.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsSvgItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN16QGraphicsSvgItem5paintEP8QPainterPK24QStyleOptionGraphi'
        'csItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QGraphicsSvgItem5paintEP8QPainterPK24QStyleOption'
          'GraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
