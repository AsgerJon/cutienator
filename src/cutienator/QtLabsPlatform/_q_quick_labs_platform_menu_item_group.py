"""
QQuickLabsPlatformMenuItemGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformMenuItemGroup to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickLabsPlatformMenuItem
  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickLabsPlatformMenuItem = WAIT['QQuickLabsPlatformMenuItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformMenuItemGroup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformMenuItemGroup: a plain Python
  object standing in front of one C++ QQuickLabsPlatformMenuItemGroup.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformMenuItemGroup that has a ritual
  and that Python can call so far, 16 names in all: 'metaObject',
  'isEnabled', 'isVisible', 'isExclusive', 'checkedItem', 'addItem',
  'removeItem', 'clear', 'triggered', 'hovered', 'enabledChanged',
  'visibleChanged', 'exclusiveChanged', 'checkedItemChanged', 'itemsChanged',
  'findCurrent'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformMenuItemGroup::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformMenuItemGroup::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuickLabsPlatformMenuItemGroup::~QQuickLabsPlatformMenuItemGroup()':
    the destructor: Python never removes a C++
    QQuickLabsPlatformMenuItemGroup.
  - Qt's 'qsizetype QQuickLabsPlatformMenuItemGroup::items_count(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop)': names
    'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute class
    yet.
  - Qt's 'QQuickLabsPlatformMenuItem
    *QQuickLabsPlatformMenuItemGroup::items_at(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop, qsizetype index)':
    names 'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute
    class yet.

  What has no ritual
  ------------------

  14 of the 35 functions Qt declares: 8 leans on 'QQuickLabsPlatformMenuItem;
  4 leans on 'QQuickLabsPlatformMenuItemGroup; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformMenuItemGroup is created at the first use, not
    by 'QQuickLabsPlatformMenuItemGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformMenuItemGroup.
  - Qt tells when it has removed the C++ QQuickLabsPlatformMenuItemGroup.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformMenuItemGroup that has no cute
    function yet, '__init__', 'activateItem', 'hoverItem', 'items',
    'items_append', 'items_at', 'items_clear', 'items_count',
    'setCheckedItem', 'setEnabled', 'setExclusive', 'setVisible',
    'updateCurrent', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformMenuItemGroup'

  #  A C++ QQuickLabsPlatformMenuItemGroup Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformMenuItemGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformMenuItemGroup::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenuItemGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItemGroup::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#isEnabled
    """
    #  bool QQuickLabsPlatformMenuItemGroup::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup9isEnabledEv',
    )

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItemGroup::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#isVisible
    """
    #  bool QQuickLabsPlatformMenuItemGroup::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup9isVisibleEv',
    )

  def isExclusive(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformMenuItemGroup::isExclusive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#isExclusive
    """
    #  bool QQuickLabsPlatformMenuItemGroup::isExclusive() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup11isExclusiveEv',
    )

  def checkedItem(self) -> Optional[QQuickLabsPlatformMenuItem]:
    """
    Calls Qt's 'QQuickLabsPlatformMenuItem
    *QQuickLabsPlatformMenuItemGroup::checkedItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#checkedItem

    Returns
    -------

    Optional[QQuickLabsPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenuItem
    #      *QQuickLabsPlatformMenuItemGroup::checkedItem() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup11checkedItemEv',
    )
    from . import QQuickLabsPlatformMenuItem
    return QQuickLabsPlatformMenuItem._cuteAt(address)

  def findCurrent(self) -> Optional[QQuickLabsPlatformMenuItem]:
    """
    Calls Qt's 'QQuickLabsPlatformMenuItem
    *QQuickLabsPlatformMenuItemGroup::findCurrent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#findCurrent

    Returns
    -------

    Optional[QQuickLabsPlatformMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabsPlatformMenuItem
    #      *QQuickLabsPlatformMenuItemGroup::findCurrent() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMenuItemGroup11findCurrentEv',
    )
    from . import QQuickLabsPlatformMenuItem
    return QQuickLabsPlatformMenuItem._cuteAt(address)

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
    Qt's
    'QQuickLabsPlatformMenuItemGroup::QQuickLabsPlatformMenuItemGroup(QObject
    *parent)': leans on
    'QQuickLabsPlatformMenuItemGroup::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformMenuItemGroup::QQuickLabsPlatformMenuItemGroup(Q"
        "Object *parent)': leans on "
        "'QQuickLabsPlatformMenuItemGroup::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuItemGroup::addItem(QQuickLabsPlatformMenuItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#addItem

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuItemGroup::addItem(
    #      QQuickLabsPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup7addItemEP26QQuickLabsPl'
        'atformMenuItem',
        self._addressOf(item),
    )

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuItemGroup::removeItem(QQuickLabsPlatformMenuItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#removeItem

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuItemGroup::removeItem(
    #      QQuickLabsPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup10removeItemEP26QQuickLa'
        'bsPlatformMenuItem',
        self._addressOf(item),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#clear
    """
    #  void QQuickLabsPlatformMenuItemGroup::clear()
    self.uglySide.call('ritual_ZN31QQuickLabsPlatformMenuItemGroup5clearEv')

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def triggered(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuItemGroup::triggered(QQuickLabsPlatformMenuItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#triggered

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuItemGroup::triggered(
    #      QQuickLabsPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup9triggeredEP26QQuickLabs'
        'PlatformMenuItem',
        self._addressOf(item),
    )

  @overload(QQuickLabsPlatformMenuItem)
  @overload(NoneType)
  def hovered(self, item: Optional[QQuickLabsPlatformMenuItem]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuItemGroup::hovered(QQuickLabsPlatformMenuItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#hovered

    Parameters
    ----------

    item : Optional[QQuickLabsPlatformMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuItemGroup::hovered(
    #      QQuickLabsPlatformMenuItem *item)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup7hoveredEP26QQuickLabsPl'
        'atformMenuItem',
        self._addressOf(item),
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html
    """
    #  void QQuickLabsPlatformMenuItemGroup::enabledChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup14enabledChangedEv',
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html
    """
    #  void QQuickLabsPlatformMenuItemGroup::visibleChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup14visibleChangedEv',
    )

  def exclusiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::exclusiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html
    """
    #  void QQuickLabsPlatformMenuItemGroup::exclusiveChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup16exclusiveChangedEv',
    )

  def checkedItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::checkedItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html
    """
    #  void QQuickLabsPlatformMenuItemGroup::checkedItemChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup18checkedItemChangedEv',
    )

  def itemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuItemGroup::itemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenuitemgroup.html#itemsChanged
    """
    #  void QQuickLabsPlatformMenuItemGroup::itemsChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMenuItemGroup12itemsChangedEv',
    )

  @staticmethod
  def activateItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::activateItem()': leans on
    'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.activateItem' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::activateItem()': leans on "
        "'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def hoverItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::hoverItem()': leans on
    'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.hoverItem' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenuItemGroup::hoverItem()': "
        "leans on 'QQuickLabsPlatformMenuItem::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def items(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickLabsPlatformMenuItem>
    QQuickLabsPlatformMenuItemGroup::items()': leans on
    'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.items' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuickLabsPlatformMenuItem> "
        "QQuickLabsPlatformMenuItemGroup::items()': leans on "
        "'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def items_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::items_append(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop,
    QQuickLabsPlatformMenuItem *obj)': leans on
    'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.items_append' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::items_append(QQmlListProperty<QQui"
        "ckLabsPlatformMenuItem> *prop, QQuickLabsPlatformMenuItem *obj)': "
        "leans on 'QQuickLabsPlatformMenuItem::checkedChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def items_at(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenuItem
    *QQuickLabsPlatformMenuItemGroup::items_at(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop, qsizetype index)':
    names 'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.items_at' has no cute function "
        "yet. Qt's 'QQuickLabsPlatformMenuItem "
        "*QQuickLabsPlatformMenuItemGroup::items_at(QQmlListProperty<QQuickL"
        "absPlatformMenuItem> *prop, qsizetype index)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute "
        "class yet.")

  @staticmethod
  def items_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::items_clear(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop)': leans on
    'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.items_clear' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::items_clear(QQmlListProperty<QQuic"
        "kLabsPlatformMenuItem> *prop)': leans on "
        "'QQuickLabsPlatformMenuItem::checkedChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def items_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickLabsPlatformMenuItemGroup::items_count(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *prop)': names
    'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.items_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickLabsPlatformMenuItemGroup::items_count(QQmlListProperty<QQuic"
        "kLabsPlatformMenuItem> *prop)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenuItem>', which has no cute "
        "class yet.")

  @staticmethod
  def setCheckedItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::setCheckedItem(
    QQuickLabsPlatformMenuItem *item)': leans on
    'QQuickLabsPlatformMenuItemGroup::checkedItemChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.setCheckedItem' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::setCheckedItem(QQuickLabsPlatformM"
        "enuItem *item)': leans on "
        "'QQuickLabsPlatformMenuItemGroup::checkedItemChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::setEnabled(bool enabled)':
    leans on 'QQuickLabsPlatformMenuItem::enabledChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.setEnabled' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenuItemGroup::setEnabled(bool "
        "enabled)': leans on "
        "'QQuickLabsPlatformMenuItem::enabledChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setExclusive(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::setExclusive(bool
    exclusive)': leans on
    'QQuickLabsPlatformMenuItemGroup::exclusiveChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.setExclusive' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::setExclusive(bool exclusive)': "
        "leans on 'QQuickLabsPlatformMenuItemGroup::exclusiveChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::setVisible(bool visible)':
    leans on 'QQuickLabsPlatformMenuItem::visibleChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.setVisible' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMenuItemGroup::setVisible(bool "
        "visible)': leans on "
        "'QQuickLabsPlatformMenuItem::visibleChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def updateCurrent(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuItemGroup::updateCurrent()': leans on
    'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuItemGroup.updateCurrent' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMenuItemGroup::updateCurrent()': leans on "
        "'QQuickLabsPlatformMenuItem::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
