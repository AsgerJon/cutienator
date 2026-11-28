"""
QCanvasPainterItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspainteritem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from ..QtGui import QColor
  from . import QCanvasPainterItemPrivate, QCanvasPainterItemRenderer
  from ..QtQuick import QQuickItem, QQuickRhiItemRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainterItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainterItem: a plain Python object standing in
  front of one C++ QCanvasPainterItem.

  What exists
  -----------

  Every function of Qt's QCanvasPainterItem that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'fillColor',
  'setFillColor', 'debug', 'createItemRenderer', 'createRenderer', 'event',
  'fillColorChanged', 'debugChanged', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCanvasPainterItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCanvasPainterItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCanvasPainterItem::~QCanvasPainterItem()': the destructor: Python
    never removes a C++ QCanvasPainterItem.
  - Qt's 'QCanvasPainterItem::QCanvasPainterItem(QCanvasPainterItemPrivate
    &dd, QQuickItem *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QCanvasPainterItemPrivate *QCanvasPainterItem::d_func()
    const': takes in Python what 'QCanvasPainterItemPrivate
    *QCanvasPainterItem::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCanvasPainterItem is created at the first use, not by
    'QCanvasPainterItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainterItem.
  - Qt tells when it has removed the C++ QCanvasPainterItem. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QCanvasPainterItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#tr

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
    #  QString QCanvasPainterItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QCanvasPainterItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainterItem'

  #  A C++ QCanvasPainterItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasPainterItem'

  #  The functions Qt calls itself that QCanvasPainterItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createItemRenderer': (
          ('_ZNK18QCanvasPainterItem18createItemRendererEv',
           ('address', 'address',
            'QtCanvasPainter:QCanvasPainterItemRenderer'),
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
    Calls Qt's 'const QMetaObject *QCanvasPainterItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCanvasPainterItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasPainterItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasPainterItem::fillColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasPainterItem::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasPainterItem9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def createItemRenderer(self) -> Optional[QCanvasPainterItemRenderer]:
    """
    Calls Qt's 'QCanvasPainterItemRenderer
    *QCanvasPainterItem::createItemRenderer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#createItemRenderer

    Returns
    -------

    Optional[QCanvasPainterItemRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainterItemRenderer *QCanvasPainterItem::createItemRenderer()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasPainterItem18createItemRendererEv',
    )
    from . import QCanvasPainterItemRenderer
    return QCanvasPainterItemRenderer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasPainterItem::setFillColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasPainterItem::setFillColor(QColor color)
    self.uglySide.call(
        'ritual_ZN18QCanvasPainterItem12setFillColorE6QColor',
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasPainterItem::QCanvasPainterItem(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#QCanvasPainterItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCanvasPainterItem::QCanvasPainterItem(QQuickItem *parent)
    self._noteCreation(QCanvasPainterItem, lambda: Rituals.call(
        'ritual_ZN18QCanvasPainterItemC1EP10QQuickItem',
        self._addressOf(parent),
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

  def debug(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QCanvasPainterItem::debug()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#debug

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QCanvasPainterItem::debug()
    address = self.uglySide.call('ritual_ZN18QCanvasPainterItem5debugEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def createRenderer(self) -> Optional[QQuickRhiItemRenderer]:
    """
    Calls Qt's 'QQuickRhiItemRenderer *QCanvasPainterItem::createRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#createRenderer

    Returns
    -------

    Optional[QQuickRhiItemRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRhiItemRenderer *QCanvasPainterItem::createRenderer()
    address = self.uglySide.call(
        'ritual_ZN18QCanvasPainterItem14createRendererEv',
    )
    from ..QtQuick import QQuickRhiItemRenderer
    return QQuickRhiItemRenderer._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCanvasPainterItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCanvasPainterItem::event(QEvent *event)
    ritual = 'ritual_ZN18QCanvasPainterItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QCanvasPainterItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterItem::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#fillColorChanged
    """
    #  void QCanvasPainterItem::fillColorChanged()
    self.uglySide.call('ritual_ZN18QCanvasPainterItem16fillColorChangedEv')

  def debugChanged(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterItem::debugChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritem.html#debugChanged
    """
    #  void QCanvasPainterItem::debugChanged()
    self.uglySide.call('ritual_ZN18QCanvasPainterItem12debugChangedEv')

  def d_func(self) -> Optional[QCanvasPainterItemPrivate]:
    """
    Calls Qt's 'QCanvasPainterItemPrivate *QCanvasPainterItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainteritem.html#d_func

    Returns
    -------

    Optional[QCanvasPainterItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainterItemPrivate *QCanvasPainterItem::d_func()
    address = self.uglySide.call('ritual_ZN18QCanvasPainterItem6d_funcEv')
    from . import QCanvasPainterItemPrivate
    return QCanvasPainterItemPrivate._cuteAt(address)
