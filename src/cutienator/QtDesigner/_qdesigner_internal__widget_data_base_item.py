"""
qdesigner_internal::WidgetDataBaseItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::WidgetDataBaseItem to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QDesignerWidgetDataBaseItemInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from ..QtGui import QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class WidgetDataBaseItem(QDesignerWidgetDataBaseItemInterface):
  """
  The cute side of Qt's qdesigner_internal::WidgetDataBaseItem: a plain
  Python object standing in front of one C++
  qdesigner_internal::WidgetDataBaseItem.

  It is built on the cute 'QDesignerWidgetDataBaseItemInterface', as Qt's
  qdesigner_internal::WidgetDataBaseItem is built on Qt's
  QDesignerWidgetDataBaseItemInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::WidgetDataBaseItem that has a
  ritual and that Python can call so far, 35 names in all: 'name', 'setName',
  'group', 'setGroup', 'toolTip', 'setToolTip', 'whatsThis', 'setWhatsThis',
  'includeFile', 'setIncludeFile', 'icon', 'setIcon', 'isCompat',
  'setCompat', 'isContainer', 'setContainer', 'isCustom', 'setCustom',
  'pluginPath', 'setPluginPath', 'isPromoted', 'setPromoted', 'extends',
  'setExtends', 'setDefaultPropertyValues', 'defaultPropertyValues', 'clone',
  'baseClassName', 'setBaseClassName', 'fakeSlots', 'setFakeSlots',
  'fakeSignals', 'setFakeSignals', 'addPageMethod', 'setAddPageMethod'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::WidgetDataBaseItem is created at the first
    use, not by 'qdesigner_internal::WidgetDataBaseItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::WidgetDataBaseItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerWidgetDataBaseItemInterface)
  @overload(NoneType)
  def clone(
      item: Optional[QDesignerWidgetDataBaseItemInterface],
  ) -> Optional[WidgetDataBaseItem]:
    """
    Calls Qt's 'WidgetDataBaseItem
    *qdesigner_internal::WidgetDataBaseItem::clone(const
    QDesignerWidgetDataBaseItemInterface *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#clone

    Parameters
    ----------

    item : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[WidgetDataBaseItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  WidgetDataBaseItem
    #      *qdesigner_internal::WidgetDataBaseItem::clone(const
    #      QDesignerWidgetDataBaseItemInterface *item)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem5cloneEPK36QDesig'
        'nerWidgetDataBaseItemInterface',
        CuteMixin._addressOf(item),
    )
    return WidgetDataBaseItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::WidgetDataBaseItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::name() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem4nameEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem4nameEv')
    return self.uglySide.call(ritual)

  def group(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::group()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::group() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem5groupEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem5groupEv')
    return self.uglySide.call(ritual)

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::toolTip()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::toolTip() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem7toolTipEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem7toolTipEv')
    return self.uglySide.call(ritual)

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::whatsThis()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::whatsThis() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem9whatsThisEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem9whatsThis'
          'Ev')
    return self.uglySide.call(ritual)

  def includeFile(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::includeFile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::includeFile() const
    ritual = (
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11includeFileEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem11includeF'
          'ileEv')
    return self.uglySide.call(ritual)

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon qdesigner_internal::WidgetDataBaseItem::icon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon qdesigner_internal::WidgetDataBaseItem::icon() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem4iconEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem4iconEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def isCompat(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::WidgetDataBaseItem::isCompat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html
    """
    #  bool qdesigner_internal::WidgetDataBaseItem::isCompat() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem8isCompatEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem8isCompatE'
          'v')
    return self.uglySide.call(ritual)

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::WidgetDataBaseItem::isContainer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html
    """
    #  bool qdesigner_internal::WidgetDataBaseItem::isContainer() const
    ritual = (
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11isContainerEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem11isContai'
          'nerEv')
    return self.uglySide.call(ritual)

  def isCustom(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::WidgetDataBaseItem::isCustom()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html
    """
    #  bool qdesigner_internal::WidgetDataBaseItem::isCustom() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem8isCustomEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem8isCustomE'
          'v')
    return self.uglySide.call(ritual)

  def pluginPath(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::pluginPath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::pluginPath() const
    ritual = (
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem10pluginPathEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem10pluginPa'
          'thEv')
    return self.uglySide.call(ritual)

  def isPromoted(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::WidgetDataBaseItem::isPromoted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html
    """
    #  bool qdesigner_internal::WidgetDataBaseItem::isPromoted() const
    ritual = (
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem10isPromotedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem10isPromot'
          'edEv')
    return self.uglySide.call(ritual)

  def extends(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetDataBaseItem::extends()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#extends

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::extends() const
    ritual = 'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem7extendsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18WidgetDataBaseItem7extendsEv')
    return self.uglySide.call(ritual)

  def defaultPropertyValues(self) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant>
    qdesigner_internal::WidgetDataBaseItem::defaultPropertyValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant>
    #      qdesigner_internal::WidgetDataBaseItem::defaultPropertyValues()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem21defaultPropert'
        'yValuesEv',
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def baseClassName(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::WidgetDataBaseItem::baseClassName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::baseClassName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem13baseClassNameE'
        'v',
    )

  def fakeSlots(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::WidgetDataBaseItem::fakeSlots() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::WidgetDataBaseItem::fakeSlots() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem9fakeSlotsEv',
    )
    return QStringList._cuteOwning(address)

  def fakeSignals(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::WidgetDataBaseItem::fakeSignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::WidgetDataBaseItem::fakeSignals()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem11fakeSignalsEv',
    )
    return QStringList._cuteOwning(address)

  def addPageMethod(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::WidgetDataBaseItem::addPageMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBaseItem::addPageMethod() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18WidgetDataBaseItem13addPageMethodE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setName(const QString
    #      &name)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem7setNameERK7QStri'
        'ng')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem7setNameERK'
          '7QString')
    self.uglySide.call(ritual, name)

  @overload(str)
  def setGroup(self, group: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setGroup(const
    QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setGroup(const QString
    #      &group)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem8setGroupERK7QStr'
        'ing')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem8setGroupER'
          'K7QString')
    self.uglySide.call(ritual, group)

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setToolTip(const
    QString &toolTip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setToolTip(const QString
    #      &toolTip)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem10setToolTipERK7Q'
        'String')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem10setToolTi'
          'pERK7QString')
    self.uglySide.call(ritual, toolTip)

  @overload(str)
  def setWhatsThis(self, whatsThis: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setWhatsThis(const QString
    &whatsThis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setWhatsThis(const
    #      QString &whatsThis)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setWhatsThisERK'
        '7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem12setWhatsT'
          'hisERK7QString')
    self.uglySide.call(ritual, whatsThis)

  @overload(str)
  def setIncludeFile(self, includeFile: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setIncludeFile(const QString
    &includeFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    includeFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setIncludeFile(const
    #      QString &includeFile)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem14setIncludeFileE'
        'RK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem14setInclud'
          'eFileERK7QString')
    self.uglySide.call(ritual, includeFile)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setIcon(const
    QIcon &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setIcon(const QIcon
    #      &icon)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem7setIconERK5QIcon')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem7setIconERK'
          '5QIcon')
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(bool)
  def setCompat(self, compat: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setCompat(bool
    compat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    compat : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setCompat(bool compat)
    ritual = 'ritual_ZN18qdesigner_internal18WidgetDataBaseItem9setCompatEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem9setCompatE'
          'b')
    self.uglySide.call(ritual, compat)

  @overload(bool)
  def setContainer(self, b: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setContainer(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setContainer(bool b)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setContainerEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem12setContai'
          'nerEb')
    self.uglySide.call(ritual, b)

  @overload(bool)
  def setCustom(self, b: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setCustom(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setCustom(bool b)
    ritual = 'ritual_ZN18qdesigner_internal18WidgetDataBaseItem9setCustomEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem9setCustomE'
          'b')
    self.uglySide.call(ritual, b)

  @overload(str)
  def setPluginPath(self, path: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setPluginPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setPluginPath(const
    #      QString &path)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem13setPluginPathER'
        'K7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem13setPlugin'
          'PathERK7QString')
    self.uglySide.call(ritual, path)

  @overload(bool)
  def setPromoted(self, b: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setPromoted(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setPromoted(bool b)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem11setPromotedEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem11setPromot'
          'edEb')
    self.uglySide.call(ritual, b)

  @overload(str)
  def setExtends(self, s: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBaseItem::setExtends(const
    QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setExtends(const QString
    #      &s)
    ritual = (
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem10setExtendsERK7Q'
        'String')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18WidgetDataBaseItem10setExtend'
          'sERK7QString')
    self.uglySide.call(ritual, s)

  @overload(QList[QVariant])
  def setDefaultPropertyValues(self, list: QList[QVariant]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setDefaultPropertyValues(const
    QList<QVariant> &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setDefaultPropertyValues(
    #      const QList<QVariant> &list)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem24setDefaultPrope'
        'rtyValuesERK5QListI8QVariantE',
        self._valueOf(list),
    )

  @overload(str)
  def setBaseClassName(self, b: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setBaseClassName(const QString
    &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    b : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setBaseClassName(const
    #      QString &b)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem16setBaseClassNam'
        'eERK7QString',
        b,
    )

  @overload(QStringList)
  def setFakeSlots(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setFakeSlots(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setFakeSlots(const
    #      QStringList &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem12setFakeSlotsERK'
        '5QListI7QStringE',
        self._valueOf(a0),
    )

  @overload(QStringList)
  def setFakeSignals(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setFakeSignals(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setFakeSignals(const
    #      QStringList &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem14setFakeSignalsE'
        'RK5QListI7QStringE',
        self._valueOf(a0),
    )

  @overload(str)
  def setAddPageMethod(self, m: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBaseItem::setAddPageMethod(const QString
    &m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    m : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetDataBaseItem::setAddPageMethod(const
    #      QString &m)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItem16setAddPageMetho'
        'dERK7QString',
        m,
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
  @overload(str)
  @overload(str, str)
  def __init__(self, name: str = '', group: str = '') -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::WidgetDataBaseItem::WidgetDataBaseItem(const QString
    &name, const QString &group)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabaseitem.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    group : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::WidgetDataBaseItem::WidgetDataBaseItem(const
    #      QString &name, const QString &group)
    self._noteCreation(WidgetDataBaseItem, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18WidgetDataBaseItemC1ERK7QStringS3_',
        name, group,
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
