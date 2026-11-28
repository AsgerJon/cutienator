"""
DomWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomWidget to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomAction, DomActionGroup, DomActionRef, DomColumn, DomItem
  from . import DomLayout, DomProperty, DomRow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomAction = WAIT['DomAction']
  DomActionGroup = WAIT['DomActionGroup']
  DomActionRef = WAIT['DomActionRef']
  DomColumn = WAIT['DomColumn']
  DomItem = WAIT['DomItem']
  DomLayout = WAIT['DomLayout']
  DomProperty = WAIT['DomProperty']
  DomRow = WAIT['DomRow']


class DomWidget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomWidget: a plain Python object standing in front of
  one C++ DomWidget.

  What exists
  -----------

  Every function of Qt's DomWidget that has a ritual and that Python can call
  so far, 36 names in all: 'hasAttributeClass', 'attributeClass',
  'setAttributeClass', 'clearAttributeClass', 'hasAttributeName',
  'attributeName', 'setAttributeName', 'clearAttributeName',
  'hasAttributeNative', 'attributeNative', 'setAttributeNative',
  'clearAttributeNative', 'elementClass', 'setElementClass',
  'elementProperty', 'setElementProperty', 'elementAttribute',
  'setElementAttribute', 'elementRow', 'setElementRow', 'elementColumn',
  'setElementColumn', 'elementItem', 'setElementItem', 'elementLayout',
  'setElementLayout', 'elementWidget', 'setElementWidget', 'elementAction',
  'setElementAction', 'elementActionGroup', 'setElementActionGroup',
  'elementAddAction', 'setElementAddAction', 'elementZOrder',
  'setElementZOrder'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomWidget::~DomWidget()': the destructor: Python never removes a
    C++ DomWidget.
  - Qt's 'void DomWidget::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomWidget::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 44 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomWidget is created at the first use, not by 'DomWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomWidget.
  - Each name of Qt's DomWidget that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeClass(self) -> bool:
    """
    Calls Qt's 'bool DomWidget::hasAttributeClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#hasAttributeClass
    """
    #  bool DomWidget::hasAttributeClass() const
    return self.uglySide.call('ritual_ZNK9DomWidget17hasAttributeClassEv')

  def attributeClass(self) -> str:
    """
    Calls Qt's 'QString DomWidget::attributeClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#attributeClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomWidget::attributeClass() const
    return self.uglySide.call('ritual_ZNK9DomWidget14attributeClassEv')

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomWidget::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#hasAttributeName
    """
    #  bool DomWidget::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK9DomWidget16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomWidget::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomWidget::attributeName() const
    return self.uglySide.call('ritual_ZNK9DomWidget13attributeNameEv')

  def hasAttributeNative(self) -> bool:
    """
    Calls Qt's 'bool DomWidget::hasAttributeNative() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#hasAttributeNative
    """
    #  bool DomWidget::hasAttributeNative() const
    return self.uglySide.call('ritual_ZNK9DomWidget18hasAttributeNativeEv')

  def attributeNative(self) -> bool:
    """
    Calls Qt's 'bool DomWidget::attributeNative() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#attributeNative
    """
    #  bool DomWidget::attributeNative() const
    return self.uglySide.call('ritual_ZNK9DomWidget15attributeNativeEv')

  def elementClass(self) -> QStringList:
    """
    Calls Qt's 'QStringList DomWidget::elementClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementClass

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList DomWidget::elementClass() const
    address = self.uglySide.call('ritual_ZNK9DomWidget12elementClassEv')
    return QStringList._cuteOwning(address)

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomWidget::elementProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomWidget::elementProperty() const
    address = self.uglySide.call('ritual_ZNK9DomWidget15elementPropertyEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementAttribute(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomWidget::elementAttribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementAttribute

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomWidget::elementAttribute() const
    address = self.uglySide.call('ritual_ZNK9DomWidget16elementAttributeEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementRow(self) -> QList[DomRow]:
    """
    Calls Qt's 'QList<DomRow *> DomWidget::elementRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementRow

    Returns
    -------

    QList[DomRow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomRow *> DomWidget::elementRow() const
    address = self.uglySide.call('ritual_ZNK9DomWidget10elementRowEv')
    from . import DomRow
    return QList[DomRow]._cuteOwning(address)

  def elementColumn(self) -> QList[DomColumn]:
    """
    Calls Qt's 'QList<DomColumn *> DomWidget::elementColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementColumn

    Returns
    -------

    QList[DomColumn]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomColumn *> DomWidget::elementColumn() const
    address = self.uglySide.call('ritual_ZNK9DomWidget13elementColumnEv')
    from . import DomColumn
    return QList[DomColumn]._cuteOwning(address)

  def elementItem(self) -> QList[DomItem]:
    """
    Calls Qt's 'QList<DomItem *> DomWidget::elementItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementItem

    Returns
    -------

    QList[DomItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomItem *> DomWidget::elementItem() const
    address = self.uglySide.call('ritual_ZNK9DomWidget11elementItemEv')
    from . import DomItem
    return QList[DomItem]._cuteOwning(address)

  def elementLayout(self) -> QList[DomLayout]:
    """
    Calls Qt's 'QList<DomLayout *> DomWidget::elementLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementLayout

    Returns
    -------

    QList[DomLayout]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomLayout *> DomWidget::elementLayout() const
    address = self.uglySide.call('ritual_ZNK9DomWidget13elementLayoutEv')
    from . import DomLayout
    return QList[DomLayout]._cuteOwning(address)

  def elementWidget(self) -> QList[DomWidget]:
    """
    Calls Qt's 'QList<DomWidget *> DomWidget::elementWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementWidget

    Returns
    -------

    QList[DomWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomWidget *> DomWidget::elementWidget() const
    address = self.uglySide.call('ritual_ZNK9DomWidget13elementWidgetEv')
    return QList[DomWidget]._cuteOwning(address)

  def elementAction(self) -> QList[DomAction]:
    """
    Calls Qt's 'QList<DomAction *> DomWidget::elementAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementAction

    Returns
    -------

    QList[DomAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomAction *> DomWidget::elementAction() const
    address = self.uglySide.call('ritual_ZNK9DomWidget13elementActionEv')
    from . import DomAction
    return QList[DomAction]._cuteOwning(address)

  def elementActionGroup(self) -> QList[DomActionGroup]:
    """
    Calls Qt's 'QList<DomActionGroup *> DomWidget::elementActionGroup()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementActionGroup

    Returns
    -------

    QList[DomActionGroup]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomActionGroup *> DomWidget::elementActionGroup() const
    address = self.uglySide.call(
        'ritual_ZNK9DomWidget18elementActionGroupEv',
    )
    from . import DomActionGroup
    return QList[DomActionGroup]._cuteOwning(address)

  def elementAddAction(self) -> QList[DomActionRef]:
    """
    Calls Qt's 'QList<DomActionRef *> DomWidget::elementAddAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementAddAction

    Returns
    -------

    QList[DomActionRef]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomActionRef *> DomWidget::elementAddAction() const
    address = self.uglySide.call('ritual_ZNK9DomWidget16elementAddActionEv')
    from . import DomActionRef
    return QList[DomActionRef]._cuteOwning(address)

  def elementZOrder(self) -> QStringList:
    """
    Calls Qt's 'QStringList DomWidget::elementZOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#elementZOrder

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList DomWidget::elementZOrder() const
    address = self.uglySide.call('ritual_ZNK9DomWidget13elementZOrderEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeClass(self, a: str) -> None:
    """
    Calls Qt's 'void DomWidget::setAttributeClass(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setAttributeClass

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomWidget::setAttributeClass(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget17setAttributeClassERK7QString', a,
    )

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomWidget::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomWidget::setAttributeName(const QString &a)
    self.uglySide.call('ritual_ZN9DomWidget16setAttributeNameERK7QString', a)

  @overload(bool)
  def setAttributeNative(self, a: bool) -> None:
    """
    Calls Qt's 'void DomWidget::setAttributeNative(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setAttributeNative

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomWidget::setAttributeNative(bool a)
    self.uglySide.call('ritual_ZN9DomWidget18setAttributeNativeEb', a)

  @overload(QStringList)
  def setElementClass(self, a: QStringList) -> None:
    """
    Calls Qt's 'void DomWidget::setElementClass(const QStringList &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementClass

    Parameters
    ----------

    a : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementClass(const QStringList &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget15setElementClassERK5QListI7QStringE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementProperty(const QList<DomProperty *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget18setElementPropertyERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementAttribute(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementAttribute(const QList<DomProperty
    *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementAttribute

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementAttribute(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget19setElementAttributeERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[DomRow])
  def setElementRow(self, a: QList[DomRow]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementRow(const QList<DomRow *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementRow

    Parameters
    ----------

    a : QList[DomRow]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementRow(const QList<DomRow *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget13setElementRowERK5QListIP6DomRowE',
        self._valueOf(a),
    )

  @overload(QList[DomColumn])
  def setElementColumn(self, a: QList[DomColumn]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementColumn(const QList<DomColumn *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementColumn

    Parameters
    ----------

    a : QList[DomColumn]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementColumn(const QList<DomColumn *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget16setElementColumnERK5QListIP9DomColumnE',
        self._valueOf(a),
    )

  @overload(QList[DomItem])
  def setElementItem(self, a: QList[DomItem]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementItem(const QList<DomItem *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementItem

    Parameters
    ----------

    a : QList[DomItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementItem(const QList<DomItem *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget14setElementItemERK5QListIP7DomItemE',
        self._valueOf(a),
    )

  @overload(QList[DomLayout])
  def setElementLayout(self, a: QList[DomLayout]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementLayout(const QList<DomLayout *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementLayout

    Parameters
    ----------

    a : QList[DomLayout]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementLayout(const QList<DomLayout *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget16setElementLayoutERK5QListIP9DomLayoutE',
        self._valueOf(a),
    )

  @overload(QList[WAIT['DomWidget']])
  def setElementWidget(self, a: QList[DomWidget]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementWidget(const QList<DomWidget *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementWidget

    Parameters
    ----------

    a : QList[DomWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementWidget(const QList<DomWidget *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget16setElementWidgetERK5QListIPS_E',
        self._valueOf(a),
    )

  @overload(QList[DomAction])
  def setElementAction(self, a: QList[DomAction]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementAction(const QList<DomAction *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementAction

    Parameters
    ----------

    a : QList[DomAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementAction(const QList<DomAction *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget16setElementActionERK5QListIP9DomActionE',
        self._valueOf(a),
    )

  @overload(QList[DomActionGroup])
  def setElementActionGroup(self, a: QList[DomActionGroup]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementActionGroup(const
    QList<DomActionGroup *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domwidget.html#setElementActionGroup

    Parameters
    ----------

    a : QList[DomActionGroup]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementActionGroup(const QList<DomActionGroup *>
    #      &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget21setElementActionGroupERK5QListIP14DomActionGr'
        'oupE',
        self._valueOf(a),
    )

  @overload(QList[DomActionRef])
  def setElementAddAction(self, a: QList[DomActionRef]) -> None:
    """
    Calls Qt's 'void DomWidget::setElementAddAction(const QList<DomActionRef
    *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementAddAction

    Parameters
    ----------

    a : QList[DomActionRef]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementAddAction(const QList<DomActionRef *> &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget19setElementAddActionERK5QListIP12DomActionRefE',
        self._valueOf(a),
    )

  @overload(QStringList)
  def setElementZOrder(self, a: QStringList) -> None:
    """
    Calls Qt's 'void DomWidget::setElementZOrder(const QStringList &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#setElementZOrder

    Parameters
    ----------

    a : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomWidget::setElementZOrder(const QStringList &a)
    self.uglySide.call(
        'ritual_ZN9DomWidget16setElementZOrderERK5QListI7QStringE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomWidget::DomWidget()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#DomWidget
    """
    #  DomWidget::DomWidget()
    self._noteCreation(DomWidget, lambda: Rituals.call(
        'ritual_ZN9DomWidgetC1Ev',
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

  def clearAttributeClass(self) -> None:
    """
    Calls Qt's 'void DomWidget::clearAttributeClass()'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#clearAttributeClass
    """
    #  void DomWidget::clearAttributeClass()
    self.uglySide.call('ritual_ZN9DomWidget19clearAttributeClassEv')

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomWidget::clearAttributeName()'.

    Qt's own words: https://doc.qt.io/qt-6/domwidget.html#clearAttributeName
    """
    #  void DomWidget::clearAttributeName()
    self.uglySide.call('ritual_ZN9DomWidget18clearAttributeNameEv')

  def clearAttributeNative(self) -> None:
    """
    Calls Qt's 'void DomWidget::clearAttributeNative()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domwidget.html#clearAttributeNative
    """
    #  void DomWidget::clearAttributeNative()
    self.uglySide.call('ritual_ZN9DomWidget20clearAttributeNativeEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomWidget::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomWidget.read' has no cute function yet. Qt's 'void "
        "DomWidget::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomWidget::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomWidget.write' has no cute function yet. Qt's 'void "
        "DomWidget::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomWidget *>': the list of DomWidget, which 'QList[DomWidget]'
#  gives. It is made here, so that there is one as soon as there can be a
#  DomWidget.
QList.createKind(
    DomWidget, 'address',
    make='ritual_list_make_DomWidget_ptr',
    add='ritual_list_add_DomWidget_ptr',
    size='ritual_list_size_DomWidget_ptr',
    at='ritual_list_at_DomWidget_ptr',
    drop='ritual_list_drop_DomWidget_ptr',
)
