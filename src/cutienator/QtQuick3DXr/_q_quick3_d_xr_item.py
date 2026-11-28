"""
QQuick3DXrItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxritem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DXrItem(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DXrItem: a plain Python object standing in
  front of one C++ QQuick3DXrItem.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DXrItem is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrItem that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'componentComplete',
  'contentItemChanged', 'pixelsPerUnitChanged', 'flagsChanged',
  'manualPixelsPerUnitChanged', 'widthChanged', 'heightChanged',
  'colorChanged', 'automaticHeightChanged', 'automaticWidthChanged'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DXrItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrItemPrivate *QQuick3DXrItem::d_func()': gives
    'QQuick3DXrItemPrivate', which has no cute class yet.
  - Qt's 'const QQuick3DXrItemPrivate *QQuick3DXrItem::d_func() const': gives
    'QQuick3DXrItemPrivate', which has no cute class yet.
  - Qt's 'QQuick3DXrItem::~QQuick3DXrItem()': the destructor: Python never
    removes a C++ QQuick3DXrItem.

  What has no ritual
  ------------------

  20 of the 36 functions Qt declares: 16 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QQuick3DXrItem.

  What to expect
  --------------

  - The C++ QQuick3DXrItem is created at the first use, not by
    'QQuick3DXrItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrItem.
  - Qt tells when it has removed the C++ QQuick3DXrItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrItem that has no cute function yet,
    '__init__', 'automaticHeight', 'automaticWidth', 'color', 'contentItem',
    'height', 'manualPixelsPerUnit', 'pixelsPerUnit', 'setAutomaticHeight',
    'setAutomaticWidth', 'setColor', 'setContentItem', 'setHeight',
    'setManualPixelsPerUnit', 'setPixelsPerUnit', 'setWidth', 'width', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrItem'

  #  A C++ QQuick3DXrItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxritem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DXrItem10metaObjectEv')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrItem::QQuick3DXrItem(QQuick3DNode *parent)': leans on
    'QQuick3DXrItem::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrItem::QQuick3DXrItem(QQuick3DNode *parent)': leans on "
        "'QQuick3DXrItem::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#componentComplete
    """
    #  void QQuick3DXrItem::componentComplete()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem17componentCompleteEv')

  def contentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::contentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#contentItemChanged
    """
    #  void QQuick3DXrItem::contentItemChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem18contentItemChangedEv')

  def pixelsPerUnitChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::pixelsPerUnitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#pixelsPerUnitChanged
    """
    #  void QQuick3DXrItem::pixelsPerUnitChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem20pixelsPerUnitChangedEv')

  def flagsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::flagsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxritem.html#flagsChanged
    """
    #  void QQuick3DXrItem::flagsChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem12flagsChangedEv')

  def manualPixelsPerUnitChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::manualPixelsPerUnitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#manualPixelsPerUnitChanged
    """
    #  void QQuick3DXrItem::manualPixelsPerUnitChanged()
    self.uglySide.call(
        'ritual_ZN14QQuick3DXrItem26manualPixelsPerUnitChangedEv',
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxritem.html#widthChanged
    """
    #  void QQuick3DXrItem::widthChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::heightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxritem.html#heightChanged
    """
    #  void QQuick3DXrItem::heightChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem13heightChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxritem.html#colorChanged
    """
    #  void QQuick3DXrItem::colorChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem12colorChangedEv')

  def automaticHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::automaticHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#automaticHeightChanged
    """
    #  void QQuick3DXrItem::automaticHeightChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem22automaticHeightChangedEv')

  def automaticWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrItem::automaticWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxritem.html#automaticWidthChanged
    """
    #  void QQuick3DXrItem::automaticWidthChanged()
    self.uglySide.call('ritual_ZN14QQuick3DXrItem21automaticWidthChangedEv')

  @staticmethod
  def automaticHeight(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrItem::automaticHeight() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.automaticHeight' has no cute function yet. Qt's "
        "'bool QQuick3DXrItem::automaticHeight() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrItemPrivate'.")

  @staticmethod
  def automaticWidth(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrItem::automaticWidth() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.automaticWidth' has no cute function yet. Qt's "
        "'bool QQuick3DXrItem::automaticWidth() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrItemPrivate'.")

  @staticmethod
  def color(*__, **_) -> Never:
    """
    Qt's 'QColor QQuick3DXrItem::color() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.color' has no cute function yet. Qt's 'QColor "
        "QQuick3DXrItem::color() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuick3DXrItemPrivate'.")

  @staticmethod
  def contentItem(*__, **_) -> Never:
    """
    Qt's 'QQuickItem *QQuick3DXrItem::contentItem() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.contentItem' has no cute function yet. Qt's "
        "'QQuickItem *QQuick3DXrItem::contentItem() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuick3DXrItemPrivate'.")

  @staticmethod
  def height(*__, **_) -> Never:
    """
    Qt's 'qreal QQuick3DXrItem::height() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.height' has no cute function yet. Qt's 'qreal "
        "QQuick3DXrItem::height() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuick3DXrItemPrivate'.")

  @staticmethod
  def manualPixelsPerUnit(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrItem::manualPixelsPerUnit() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.manualPixelsPerUnit' has no cute function yet. "
        "Qt's 'bool QQuick3DXrItem::manualPixelsPerUnit() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuick3DXrItemPrivate'.")

  @staticmethod
  def pixelsPerUnit(*__, **_) -> Never:
    """
    Qt's 'qreal QQuick3DXrItem::pixelsPerUnit() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.pixelsPerUnit' has no cute function yet. Qt's "
        "'qreal QQuick3DXrItem::pixelsPerUnit() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrItemPrivate'.")

  @staticmethod
  def setAutomaticHeight(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setAutomaticHeight(bool newAutomaticHeight)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setAutomaticHeight' has no cute function yet. Qt's "
        "'void QQuick3DXrItem::setAutomaticHeight(bool "
        "newAutomaticHeight)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setAutomaticWidth(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setAutomaticWidth(bool newAutomaticHeight)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setAutomaticWidth' has no cute function yet. Qt's "
        "'void QQuick3DXrItem::setAutomaticWidth(bool newAutomaticHeight)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setColor(const QColor &newColor)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setColor' has no cute function yet. Qt's 'void "
        "QQuick3DXrItem::setColor(const QColor &newColor)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setContentItem(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setContentItem(QQuickItem *newContentItem)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setContentItem' has no cute function yet. Qt's "
        "'void QQuick3DXrItem::setContentItem(QQuickItem *newContentItem)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setHeight(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setHeight(qreal newHeight)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setHeight' has no cute function yet. Qt's 'void "
        "QQuick3DXrItem::setHeight(qreal newHeight)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setManualPixelsPerUnit(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setManualPixelsPerUnit(bool
    newManualPixelsPerUnit)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: member access into
    incomplete type 'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setManualPixelsPerUnit' has no cute function yet. "
        "Qt's 'void QQuick3DXrItem::setManualPixelsPerUnit(bool "
        "newManualPixelsPerUnit)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setPixelsPerUnit(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setPixelsPerUnit(qreal newPixelsPerUnit)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setPixelsPerUnit' has no cute function yet. Qt's "
        "'void QQuick3DXrItem::setPixelsPerUnit(qreal newPixelsPerUnit)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuick3DXrItemPrivate'.")

  @staticmethod
  def setWidth(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrItem::setWidth(qreal newWidth)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.setWidth' has no cute function yet. Qt's 'void "
        "QQuick3DXrItem::setWidth(qreal newWidth)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuick3DXrItemPrivate'.")

  @staticmethod
  def width(*__, **_) -> Never:
    """
    Qt's 'qreal QQuick3DXrItem::width() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuick3DXrItemPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrItem.width' has no cute function yet. Qt's 'qreal "
        "QQuick3DXrItem::width() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuick3DXrItemPrivate'.")
