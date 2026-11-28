"""
QQStyleKitLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitLayout to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QMetaObject
  from ..QtQuick import QQuickItem


class QQStyleKitLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQStyleKitLayout: a plain Python object standing in
  front of one C++ QQStyleKitLayout.

  What exists
  -----------

  Every function of Qt's QQStyleKitLayout that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'container', 'padding',
  'contentMargins', 'spacing', 'isMirrored', 'implicitWidth',
  'implicitHeight', 'isEnabled', 'containerChanged', 'layoutItemsChanged',
  'layoutChanged', 'paddingChanged', 'contentMarginsChanged',
  'spacingChanged', 'mirroredChanged', 'implicitWidthChanged',
  'implicitHeightChanged', 'enabledChanged', 'updatePolish'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitLayout::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  16 of the 38 functions Qt declares: 13 leans on 'QQStyleKitLayout; 2 not a
  gap; 1 leans on 'vtable for QQStyleKitLayout', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitLayout is created at the first use, not by
    'QQStyleKitLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitLayout.
  - Qt tells when it has removed the C++ QQStyleKitLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitLayout that has no cute function yet,
    '__init__', 'layoutItem_append', 'layoutItem_at', 'layoutItem_clear',
    'layoutItem_count', 'layoutItems', 'setContainer', 'setContentMargins',
    'setMirrored', 'setSpacing', holds a function that raises
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
  __qt_class__ = 'QQStyleKitLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def container(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQStyleKitLayout::container() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#container

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQStyleKitLayout::container() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitLayout9containerEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def padding(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQStyleKitLayout::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#padding

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQStyleKitLayout::padding() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitLayout7paddingEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def contentMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQStyleKitLayout::contentMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#contentMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQStyleKitLayout::contentMargins() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitLayout14contentMarginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#spacing
    """
    #  qreal QQStyleKitLayout::spacing() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitLayout7spacingEv')

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitLayout::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#isMirrored
    """
    #  bool QQStyleKitLayout::isMirrored() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitLayout10isMirroredEv')

  def implicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayout::implicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#implicitWidth
    """
    #  qreal QQStyleKitLayout::implicitWidth() const
    return self.uglySide.call(
        'ritual_ZNK16QQStyleKitLayout13implicitWidthEv',
    )

  def implicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitLayout::implicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#implicitHeight
    """
    #  qreal QQStyleKitLayout::implicitHeight() const
    return self.uglySide.call(
        'ritual_ZNK16QQStyleKitLayout14implicitHeightEv',
    )

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitLayout::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#isEnabled
    """
    #  bool QQStyleKitLayout::isEnabled() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitLayout9isEnabledEv')

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
    Qt's 'QQStyleKitLayout::QQStyleKitLayout(QQuickItem *parent)': leans on
    'vtable for QQStyleKitLayout', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.__init__' has no cute function yet. Qt's "
        "'QQStyleKitLayout::QQStyleKitLayout(QQuickItem *parent)': leans on "
        "'vtable for QQStyleKitLayout', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def containerChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::containerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#containerChanged
    """
    #  void QQStyleKitLayout::containerChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout16containerChangedEv')

  def layoutItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::layoutItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#layoutItemsChanged
    """
    #  void QQStyleKitLayout::layoutItemsChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout18layoutItemsChangedEv')

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::layoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#layoutChanged
    """
    #  void QQStyleKitLayout::layoutChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout13layoutChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#paddingChanged
    """
    #  void QQStyleKitLayout::paddingChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout14paddingChangedEv')

  def contentMarginsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::contentMarginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#contentMarginsChanged
    """
    #  void QQStyleKitLayout::contentMarginsChanged()
    self.uglySide.call(
        'ritual_ZN16QQStyleKitLayout21contentMarginsChangedEv',
    )

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::spacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#spacingChanged
    """
    #  void QQStyleKitLayout::spacingChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout14spacingChangedEv')

  def mirroredChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::mirroredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#mirroredChanged
    """
    #  void QQStyleKitLayout::mirroredChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout15mirroredChangedEv')

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#implicitWidthChanged
    """
    #  void QQStyleKitLayout::implicitWidthChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout20implicitWidthChangedEv')

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#implicitHeightChanged
    """
    #  void QQStyleKitLayout::implicitHeightChanged()
    self.uglySide.call(
        'ritual_ZN16QQStyleKitLayout21implicitHeightChangedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitlayout.html#enabledChanged
    """
    #  void QQStyleKitLayout::enabledChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout14enabledChangedEv')

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQStyleKitLayout::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitlayout.html#updatePolish
    """
    #  void QQStyleKitLayout::updatePolish()
    self.uglySide.call('ritual_ZN16QQStyleKitLayout12updatePolishEv')

  @staticmethod
  def layoutItem_append(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayout::layoutItem_append(
    QQmlListProperty<QQStyleKitLayoutItem> *list, QQStyleKitLayoutItem
    *item)': leans on 'QQStyleKitLayout::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.layoutItem_append' has no cute function yet. "
        "Qt's 'void "
        "QQStyleKitLayout::layoutItem_append(QQmlListProperty<QQStyleKitLayo"
        "utItem> *list, QQStyleKitLayoutItem *item)': leans on "
        "'QQStyleKitLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def layoutItem_at(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitLayoutItem
    *QQStyleKitLayout::layoutItem_at(QQmlListProperty<QQStyleKitLayoutItem>
    *list, qsizetype index)': leans on 'QQStyleKitLayout::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.layoutItem_at' has no cute function yet. Qt's "
        "'QQStyleKitLayoutItem "
        "*QQStyleKitLayout::layoutItem_at(QQmlListProperty<QQStyleKitLayoutI"
        "tem> *list, qsizetype index)': leans on "
        "'QQStyleKitLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def layoutItem_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitLayout::layoutItem_clear(QQmlListProperty<QQStyleKitLayoutItem>
    *list)': leans on 'QQStyleKitLayout::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.layoutItem_clear' has no cute function yet. Qt's "
        "'void "
        "QQStyleKitLayout::layoutItem_clear(QQmlListProperty<QQStyleKitLayou"
        "tItem> *list)': leans on 'QQStyleKitLayout::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def layoutItem_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQStyleKitLayout::layoutItem_count(QQmlListProperty<QQStyleKitLayoutItem>
    *list)': leans on 'QQStyleKitLayout::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.layoutItem_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQStyleKitLayout::layoutItem_count(QQmlListProperty<QQStyleKitLayou"
        "tItem> *list)': leans on 'QQStyleKitLayout::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def layoutItems(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQStyleKitLayoutItem>
    QQStyleKitLayout::layoutItems()': leans on
    'QQStyleKitLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.layoutItems' has no cute function yet. Qt's "
        "'QQmlListProperty<QQStyleKitLayoutItem> "
        "QQStyleKitLayout::layoutItems()': leans on "
        "'QQStyleKitLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setContainer(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayout::setContainer(QQuickItem *item)': leans on
    'QQStyleKitLayout::containerChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.setContainer' has no cute function yet. Qt's "
        "'void QQStyleKitLayout::setContainer(QQuickItem *item)': leans on "
        "'QQStyleKitLayout::containerChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setContentMargins(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayout::setContentMargins(const QMarginsF
    &margins)': leans on 'QQStyleKitLayout::contentMarginsChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.setContentMargins' has no cute function yet. "
        "Qt's 'void QQStyleKitLayout::setContentMargins(const QMarginsF "
        "&margins)': leans on 'QQStyleKitLayout::contentMarginsChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setMirrored(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayout::setMirrored(bool mirrored)': leans on
    'QQStyleKitLayout::mirroredChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.setMirrored' has no cute function yet. Qt's "
        "'void QQStyleKitLayout::setMirrored(bool mirrored)': leans on "
        "'QQStyleKitLayout::mirroredChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSpacing(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitLayout::setSpacing(qreal spacing)': leans on
    'QQStyleKitLayout::spacingChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitLayout.setSpacing' has no cute function yet. Qt's 'void "
        "QQStyleKitLayout::setSpacing(qreal spacing)': leans on "
        "'QQStyleKitLayout::spacingChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
