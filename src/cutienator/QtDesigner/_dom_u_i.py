"""
DomUI binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomUI to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomButtonGroups, DomConnections, DomCustomWidgets
  from . import DomDesignerData, DomIncludes, DomLayoutDefault
  from . import DomLayoutFunction, DomResources, DomSlots, DomTabStops
  from . import DomWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomButtonGroups = WAIT['DomButtonGroups']
  DomConnections = WAIT['DomConnections']
  DomCustomWidgets = WAIT['DomCustomWidgets']
  DomDesignerData = WAIT['DomDesignerData']
  DomIncludes = WAIT['DomIncludes']
  DomLayoutDefault = WAIT['DomLayoutDefault']
  DomLayoutFunction = WAIT['DomLayoutFunction']
  DomResources = WAIT['DomResources']
  DomSlots = WAIT['DomSlots']
  DomTabStops = WAIT['DomTabStops']
  DomWidget = WAIT['DomWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomUI(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomUI: a plain Python object standing in front of one
  C++ DomUI.

  What exists
  -----------

  Every function of Qt's DomUI that has a ritual and that Python can call so
  far, 107 names in all: 'hasAttributeVersion', 'attributeVersion',
  'setAttributeVersion', 'clearAttributeVersion', 'hasAttributeLanguage',
  'attributeLanguage', 'setAttributeLanguage', 'clearAttributeLanguage',
  'hasAttributeDisplayname', 'attributeDisplayname',
  'setAttributeDisplayname', 'clearAttributeDisplayname',
  'hasAttributeIdbasedtr', 'attributeIdbasedtr', 'setAttributeIdbasedtr',
  'clearAttributeIdbasedtr', 'hasAttributeLabel', 'attributeLabel',
  'setAttributeLabel', 'clearAttributeLabel',
  'hasAttributeConnectslotsbyname', 'attributeConnectslotsbyname',
  'setAttributeConnectslotsbyname', 'clearAttributeConnectslotsbyname',
  'hasAttributeStdsetdef', 'attributeStdsetdef', 'setAttributeStdsetdef',
  'clearAttributeStdsetdef', 'hasAttributeStdSetDef', 'attributeStdSetDef',
  'setAttributeStdSetDef', 'clearAttributeStdSetDef', 'elementAuthor',
  'setElementAuthor', 'hasElementAuthor', 'clearElementAuthor',
  'elementComment', 'setElementComment', 'hasElementComment',
  'clearElementComment', 'elementExportMacro', 'setElementExportMacro',
  'hasElementExportMacro', 'clearElementExportMacro', 'elementClass',
  'setElementClass', 'hasElementClass', 'clearElementClass', 'elementWidget',
  'takeElementWidget', 'setElementWidget', 'hasElementWidget',
  'clearElementWidget', 'elementLayoutDefault', 'takeElementLayoutDefault',
  'setElementLayoutDefault', 'hasElementLayoutDefault',
  'clearElementLayoutDefault', 'elementLayoutFunction',
  'takeElementLayoutFunction', 'setElementLayoutFunction',
  'hasElementLayoutFunction', 'clearElementLayoutFunction',
  'elementPixmapFunction', 'setElementPixmapFunction',
  'hasElementPixmapFunction', 'clearElementPixmapFunction',
  'elementCustomWidgets', 'takeElementCustomWidgets',
  'setElementCustomWidgets', 'hasElementCustomWidgets',
  'clearElementCustomWidgets', 'elementTabStops', 'takeElementTabStops',
  'setElementTabStops', 'hasElementTabStops', 'clearElementTabStops',
  'elementIncludes', 'takeElementIncludes', 'setElementIncludes',
  'hasElementIncludes', 'clearElementIncludes', 'elementResources',
  'takeElementResources', 'setElementResources', 'hasElementResources',
  'clearElementResources', 'elementConnections', 'takeElementConnections',
  'setElementConnections', 'hasElementConnections',
  'clearElementConnections', 'elementDesignerdata',
  'takeElementDesignerdata', 'setElementDesignerdata',
  'hasElementDesignerdata', 'clearElementDesignerdata', 'elementSlots',
  'takeElementSlots', 'setElementSlots', 'hasElementSlots',
  'clearElementSlots', 'elementButtonGroups', 'takeElementButtonGroups',
  'setElementButtonGroups', 'hasElementButtonGroups',
  'clearElementButtonGroups'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomUI::~DomUI()': the destructor: Python never removes a C++ DomUI.
  - Qt's 'void DomUI::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomUI::write(QXmlStreamWriter &writer, const QString &tagName)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 115 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomUI is created at the first use, not by 'DomUI(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomUI.
  - Each name of Qt's DomUI that has no cute function yet, 'read', 'write',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomUI'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeVersion(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeVersion
    """
    #  bool DomUI::hasAttributeVersion() const
    return self.uglySide.call('ritual_ZNK5DomUI19hasAttributeVersionEv')

  def attributeVersion(self) -> str:
    """
    Calls Qt's 'QString DomUI::attributeVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::attributeVersion() const
    return self.uglySide.call('ritual_ZNK5DomUI16attributeVersionEv')

  def hasAttributeLanguage(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeLanguage
    """
    #  bool DomUI::hasAttributeLanguage() const
    return self.uglySide.call('ritual_ZNK5DomUI20hasAttributeLanguageEv')

  def attributeLanguage(self) -> str:
    """
    Calls Qt's 'QString DomUI::attributeLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::attributeLanguage() const
    return self.uglySide.call('ritual_ZNK5DomUI17attributeLanguageEv')

  def hasAttributeDisplayname(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeDisplayname() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeDisplayname
    """
    #  bool DomUI::hasAttributeDisplayname() const
    return self.uglySide.call('ritual_ZNK5DomUI23hasAttributeDisplaynameEv')

  def attributeDisplayname(self) -> str:
    """
    Calls Qt's 'QString DomUI::attributeDisplayname() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeDisplayname

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::attributeDisplayname() const
    return self.uglySide.call('ritual_ZNK5DomUI20attributeDisplaynameEv')

  def hasAttributeIdbasedtr(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeIdbasedtr() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeIdbasedtr
    """
    #  bool DomUI::hasAttributeIdbasedtr() const
    return self.uglySide.call('ritual_ZNK5DomUI21hasAttributeIdbasedtrEv')

  def attributeIdbasedtr(self) -> bool:
    """
    Calls Qt's 'bool DomUI::attributeIdbasedtr() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeIdbasedtr
    """
    #  bool DomUI::attributeIdbasedtr() const
    return self.uglySide.call('ritual_ZNK5DomUI18attributeIdbasedtrEv')

  def hasAttributeLabel(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeLabel
    """
    #  bool DomUI::hasAttributeLabel() const
    return self.uglySide.call('ritual_ZNK5DomUI17hasAttributeLabelEv')

  def attributeLabel(self) -> str:
    """
    Calls Qt's 'QString DomUI::attributeLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::attributeLabel() const
    return self.uglySide.call('ritual_ZNK5DomUI14attributeLabelEv')

  def hasAttributeConnectslotsbyname(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeConnectslotsbyname() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#hasAttributeConnectslotsbyname
    """
    #  bool DomUI::hasAttributeConnectslotsbyname() const
    return self.uglySide.call(
        'ritual_ZNK5DomUI30hasAttributeConnectslotsbynameEv',
    )

  def attributeConnectslotsbyname(self) -> bool:
    """
    Calls Qt's 'bool DomUI::attributeConnectslotsbyname() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#attributeConnectslotsbyname
    """
    #  bool DomUI::attributeConnectslotsbyname() const
    return self.uglySide.call(
        'ritual_ZNK5DomUI27attributeConnectslotsbynameEv',
    )

  def hasAttributeStdsetdef(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeStdsetdef() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeStdsetdef
    """
    #  bool DomUI::hasAttributeStdsetdef() const
    return self.uglySide.call('ritual_ZNK5DomUI21hasAttributeStdsetdefEv')

  def attributeStdsetdef(self) -> int:
    """
    Calls Qt's 'int DomUI::attributeStdsetdef() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeStdsetdef
    """
    #  int DomUI::attributeStdsetdef() const
    return self.uglySide.call('ritual_ZNK5DomUI18attributeStdsetdefEv')

  def hasAttributeStdSetDef(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasAttributeStdSetDef() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasAttributeStdSetDef
    """
    #  bool DomUI::hasAttributeStdSetDef() const
    return self.uglySide.call('ritual_ZNK5DomUI21hasAttributeStdSetDefEv')

  def attributeStdSetDef(self) -> int:
    """
    Calls Qt's 'int DomUI::attributeStdSetDef() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#attributeStdSetDef
    """
    #  int DomUI::attributeStdSetDef() const
    return self.uglySide.call('ritual_ZNK5DomUI18attributeStdSetDefEv')

  def elementAuthor(self) -> str:
    """
    Calls Qt's 'QString DomUI::elementAuthor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementAuthor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::elementAuthor() const
    return self.uglySide.call('ritual_ZNK5DomUI13elementAuthorEv')

  def hasElementAuthor(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementAuthor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementAuthor
    """
    #  bool DomUI::hasElementAuthor() const
    return self.uglySide.call('ritual_ZNK5DomUI16hasElementAuthorEv')

  def elementComment(self) -> str:
    """
    Calls Qt's 'QString DomUI::elementComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementComment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::elementComment() const
    return self.uglySide.call('ritual_ZNK5DomUI14elementCommentEv')

  def hasElementComment(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementComment
    """
    #  bool DomUI::hasElementComment() const
    return self.uglySide.call('ritual_ZNK5DomUI17hasElementCommentEv')

  def elementExportMacro(self) -> str:
    """
    Calls Qt's 'QString DomUI::elementExportMacro() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementExportMacro

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::elementExportMacro() const
    return self.uglySide.call('ritual_ZNK5DomUI18elementExportMacroEv')

  def hasElementExportMacro(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementExportMacro() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementExportMacro
    """
    #  bool DomUI::hasElementExportMacro() const
    return self.uglySide.call('ritual_ZNK5DomUI21hasElementExportMacroEv')

  def elementClass(self) -> str:
    """
    Calls Qt's 'QString DomUI::elementClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::elementClass() const
    return self.uglySide.call('ritual_ZNK5DomUI12elementClassEv')

  def hasElementClass(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementClass
    """
    #  bool DomUI::hasElementClass() const
    return self.uglySide.call('ritual_ZNK5DomUI15hasElementClassEv')

  def elementWidget(self) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget *DomUI::elementWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementWidget

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *DomUI::elementWidget() const
    address = self.uglySide.call('ritual_ZNK5DomUI13elementWidgetEv')
    from . import DomWidget
    return DomWidget._cuteAt(address)

  def hasElementWidget(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementWidget
    """
    #  bool DomUI::hasElementWidget() const
    return self.uglySide.call('ritual_ZNK5DomUI16hasElementWidgetEv')

  def elementLayoutDefault(self) -> Optional[DomLayoutDefault]:
    """
    Calls Qt's 'DomLayoutDefault *DomUI::elementLayoutDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementLayoutDefault

    Returns
    -------

    Optional[DomLayoutDefault]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayoutDefault *DomUI::elementLayoutDefault() const
    address = self.uglySide.call('ritual_ZNK5DomUI20elementLayoutDefaultEv')
    from . import DomLayoutDefault
    return DomLayoutDefault._cuteAt(address)

  def hasElementLayoutDefault(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementLayoutDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementLayoutDefault
    """
    #  bool DomUI::hasElementLayoutDefault() const
    return self.uglySide.call('ritual_ZNK5DomUI23hasElementLayoutDefaultEv')

  def elementLayoutFunction(self) -> Optional[DomLayoutFunction]:
    """
    Calls Qt's 'DomLayoutFunction *DomUI::elementLayoutFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementLayoutFunction

    Returns
    -------

    Optional[DomLayoutFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayoutFunction *DomUI::elementLayoutFunction() const
    address = self.uglySide.call('ritual_ZNK5DomUI21elementLayoutFunctionEv')
    from . import DomLayoutFunction
    return DomLayoutFunction._cuteAt(address)

  def hasElementLayoutFunction(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementLayoutFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#hasElementLayoutFunction
    """
    #  bool DomUI::hasElementLayoutFunction() const
    return self.uglySide.call('ritual_ZNK5DomUI24hasElementLayoutFunctionEv')

  def elementPixmapFunction(self) -> str:
    """
    Calls Qt's 'QString DomUI::elementPixmapFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementPixmapFunction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomUI::elementPixmapFunction() const
    return self.uglySide.call('ritual_ZNK5DomUI21elementPixmapFunctionEv')

  def hasElementPixmapFunction(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementPixmapFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#hasElementPixmapFunction
    """
    #  bool DomUI::hasElementPixmapFunction() const
    return self.uglySide.call('ritual_ZNK5DomUI24hasElementPixmapFunctionEv')

  def elementCustomWidgets(self) -> Optional[DomCustomWidgets]:
    """
    Calls Qt's 'DomCustomWidgets *DomUI::elementCustomWidgets() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementCustomWidgets

    Returns
    -------

    Optional[DomCustomWidgets]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomCustomWidgets *DomUI::elementCustomWidgets() const
    address = self.uglySide.call('ritual_ZNK5DomUI20elementCustomWidgetsEv')
    from . import DomCustomWidgets
    return DomCustomWidgets._cuteAt(address)

  def hasElementCustomWidgets(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementCustomWidgets() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementCustomWidgets
    """
    #  bool DomUI::hasElementCustomWidgets() const
    return self.uglySide.call('ritual_ZNK5DomUI23hasElementCustomWidgetsEv')

  def elementTabStops(self) -> Optional[DomTabStops]:
    """
    Calls Qt's 'DomTabStops *DomUI::elementTabStops() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementTabStops

    Returns
    -------

    Optional[DomTabStops]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomTabStops *DomUI::elementTabStops() const
    address = self.uglySide.call('ritual_ZNK5DomUI15elementTabStopsEv')
    from . import DomTabStops
    return DomTabStops._cuteAt(address)

  def hasElementTabStops(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementTabStops() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementTabStops
    """
    #  bool DomUI::hasElementTabStops() const
    return self.uglySide.call('ritual_ZNK5DomUI18hasElementTabStopsEv')

  def elementIncludes(self) -> Optional[DomIncludes]:
    """
    Calls Qt's 'DomIncludes *DomUI::elementIncludes() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementIncludes

    Returns
    -------

    Optional[DomIncludes]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomIncludes *DomUI::elementIncludes() const
    address = self.uglySide.call('ritual_ZNK5DomUI15elementIncludesEv')
    from . import DomIncludes
    return DomIncludes._cuteAt(address)

  def hasElementIncludes(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementIncludes() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementIncludes
    """
    #  bool DomUI::hasElementIncludes() const
    return self.uglySide.call('ritual_ZNK5DomUI18hasElementIncludesEv')

  def elementResources(self) -> Optional[DomResources]:
    """
    Calls Qt's 'DomResources *DomUI::elementResources() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementResources

    Returns
    -------

    Optional[DomResources]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResources *DomUI::elementResources() const
    address = self.uglySide.call('ritual_ZNK5DomUI16elementResourcesEv')
    from . import DomResources
    return DomResources._cuteAt(address)

  def hasElementResources(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementResources() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementResources
    """
    #  bool DomUI::hasElementResources() const
    return self.uglySide.call('ritual_ZNK5DomUI19hasElementResourcesEv')

  def elementConnections(self) -> Optional[DomConnections]:
    """
    Calls Qt's 'DomConnections *DomUI::elementConnections() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementConnections

    Returns
    -------

    Optional[DomConnections]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomConnections *DomUI::elementConnections() const
    address = self.uglySide.call('ritual_ZNK5DomUI18elementConnectionsEv')
    from . import DomConnections
    return DomConnections._cuteAt(address)

  def hasElementConnections(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementConnections() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementConnections
    """
    #  bool DomUI::hasElementConnections() const
    return self.uglySide.call('ritual_ZNK5DomUI21hasElementConnectionsEv')

  def elementDesignerdata(self) -> Optional[DomDesignerData]:
    """
    Calls Qt's 'DomDesignerData *DomUI::elementDesignerdata() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementDesignerdata

    Returns
    -------

    Optional[DomDesignerData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDesignerData *DomUI::elementDesignerdata() const
    address = self.uglySide.call('ritual_ZNK5DomUI19elementDesignerdataEv')
    from . import DomDesignerData
    return DomDesignerData._cuteAt(address)

  def hasElementDesignerdata(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementDesignerdata() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementDesignerdata
    """
    #  bool DomUI::hasElementDesignerdata() const
    return self.uglySide.call('ritual_ZNK5DomUI22hasElementDesignerdataEv')

  def elementSlots(self) -> Optional[DomSlots]:
    """
    Calls Qt's 'DomSlots *DomUI::elementSlots() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementSlots

    Returns
    -------

    Optional[DomSlots]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSlots *DomUI::elementSlots() const
    address = self.uglySide.call('ritual_ZNK5DomUI12elementSlotsEv')
    from . import DomSlots
    return DomSlots._cuteAt(address)

  def hasElementSlots(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementSlots() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementSlots
    """
    #  bool DomUI::hasElementSlots() const
    return self.uglySide.call('ritual_ZNK5DomUI15hasElementSlotsEv')

  def elementButtonGroups(self) -> Optional[DomButtonGroups]:
    """
    Calls Qt's 'DomButtonGroups *DomUI::elementButtonGroups() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#elementButtonGroups

    Returns
    -------

    Optional[DomButtonGroups]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomButtonGroups *DomUI::elementButtonGroups() const
    address = self.uglySide.call('ritual_ZNK5DomUI19elementButtonGroupsEv')
    from . import DomButtonGroups
    return DomButtonGroups._cuteAt(address)

  def hasElementButtonGroups(self) -> bool:
    """
    Calls Qt's 'bool DomUI::hasElementButtonGroups() const'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#hasElementButtonGroups
    """
    #  bool DomUI::hasElementButtonGroups() const
    return self.uglySide.call('ritual_ZNK5DomUI22hasElementButtonGroupsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeVersion(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeVersion(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeVersion

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setAttributeVersion(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI19setAttributeVersionERK7QString', a)

  @overload(str)
  def setAttributeLanguage(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeLanguage(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeLanguage

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setAttributeLanguage(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI20setAttributeLanguageERK7QString', a)

  @overload(str)
  def setAttributeDisplayname(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeDisplayname(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeDisplayname

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setAttributeDisplayname(const QString &a)
    self.uglySide.call(
        'ritual_ZN5DomUI23setAttributeDisplaynameERK7QString', a,
    )

  @overload(bool)
  def setAttributeIdbasedtr(self, a: bool) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeIdbasedtr(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeIdbasedtr

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomUI::setAttributeIdbasedtr(bool a)
    self.uglySide.call('ritual_ZN5DomUI21setAttributeIdbasedtrEb', a)

  @overload(str)
  def setAttributeLabel(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeLabel(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeLabel

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setAttributeLabel(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI17setAttributeLabelERK7QString', a)

  @overload(bool)
  def setAttributeConnectslotsbyname(self, a: bool) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeConnectslotsbyname(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#setAttributeConnectslotsbyname

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomUI::setAttributeConnectslotsbyname(bool a)
    self.uglySide.call(
        'ritual_ZN5DomUI30setAttributeConnectslotsbynameEb', a,
    )

  @overload(int)
  def setAttributeStdsetdef(self, a: int) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeStdsetdef(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeStdsetdef

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomUI::setAttributeStdsetdef(int a)
    self.uglySide.call('ritual_ZN5DomUI21setAttributeStdsetdefEi', a)

  @overload(int)
  def setAttributeStdSetDef(self, a: int) -> None:
    """
    Calls Qt's 'void DomUI::setAttributeStdSetDef(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setAttributeStdSetDef

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomUI::setAttributeStdSetDef(int a)
    self.uglySide.call('ritual_ZN5DomUI21setAttributeStdSetDefEi', a)

  @overload(str)
  def setElementAuthor(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setElementAuthor(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementAuthor

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setElementAuthor(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI16setElementAuthorERK7QString', a)

  @overload(str)
  def setElementComment(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setElementComment(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementComment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setElementComment(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI17setElementCommentERK7QString', a)

  @overload(str)
  def setElementExportMacro(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setElementExportMacro(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementExportMacro

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setElementExportMacro(const QString &a)
    self.uglySide.call(
        'ritual_ZN5DomUI21setElementExportMacroERK7QString', a,
    )

  @overload(str)
  def setElementClass(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setElementClass(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementClass

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setElementClass(const QString &a)
    self.uglySide.call('ritual_ZN5DomUI15setElementClassERK7QString', a)

  @overload(DomWidget)
  @overload(NoneType)
  def setElementWidget(self, a: Optional[DomWidget]) -> None:
    """
    Calls Qt's 'void DomUI::setElementWidget(DomWidget *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementWidget

    Parameters
    ----------

    a : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementWidget(DomWidget *a)
    self.uglySide.call(
        'ritual_ZN5DomUI16setElementWidgetEP9DomWidget', self._addressOf(a),
    )

  @overload(DomLayoutDefault)
  @overload(NoneType)
  def setElementLayoutDefault(self, a: Optional[DomLayoutDefault]) -> None:
    """
    Calls Qt's 'void DomUI::setElementLayoutDefault(DomLayoutDefault *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementLayoutDefault

    Parameters
    ----------

    a : Optional[DomLayoutDefault]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementLayoutDefault(DomLayoutDefault *a)
    self.uglySide.call(
        'ritual_ZN5DomUI23setElementLayoutDefaultEP16DomLayoutDefault',
        self._addressOf(a),
    )

  @overload(DomLayoutFunction)
  @overload(NoneType)
  def setElementLayoutFunction(self, a: Optional[DomLayoutFunction]) -> None:
    """
    Calls Qt's 'void DomUI::setElementLayoutFunction(DomLayoutFunction *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#setElementLayoutFunction

    Parameters
    ----------

    a : Optional[DomLayoutFunction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementLayoutFunction(DomLayoutFunction *a)
    self.uglySide.call(
        'ritual_ZN5DomUI24setElementLayoutFunctionEP17DomLayoutFunction',
        self._addressOf(a),
    )

  @overload(str)
  def setElementPixmapFunction(self, a: str) -> None:
    """
    Calls Qt's 'void DomUI::setElementPixmapFunction(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#setElementPixmapFunction

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomUI::setElementPixmapFunction(const QString &a)
    self.uglySide.call(
        'ritual_ZN5DomUI24setElementPixmapFunctionERK7QString', a,
    )

  @overload(DomCustomWidgets)
  @overload(NoneType)
  def setElementCustomWidgets(self, a: Optional[DomCustomWidgets]) -> None:
    """
    Calls Qt's 'void DomUI::setElementCustomWidgets(DomCustomWidgets *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementCustomWidgets

    Parameters
    ----------

    a : Optional[DomCustomWidgets]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementCustomWidgets(DomCustomWidgets *a)
    self.uglySide.call(
        'ritual_ZN5DomUI23setElementCustomWidgetsEP16DomCustomWidgets',
        self._addressOf(a),
    )

  @overload(DomTabStops)
  @overload(NoneType)
  def setElementTabStops(self, a: Optional[DomTabStops]) -> None:
    """
    Calls Qt's 'void DomUI::setElementTabStops(DomTabStops *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementTabStops

    Parameters
    ----------

    a : Optional[DomTabStops]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementTabStops(DomTabStops *a)
    self.uglySide.call(
        'ritual_ZN5DomUI18setElementTabStopsEP11DomTabStops',
        self._addressOf(a),
    )

  @overload(DomIncludes)
  @overload(NoneType)
  def setElementIncludes(self, a: Optional[DomIncludes]) -> None:
    """
    Calls Qt's 'void DomUI::setElementIncludes(DomIncludes *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementIncludes

    Parameters
    ----------

    a : Optional[DomIncludes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementIncludes(DomIncludes *a)
    self.uglySide.call(
        'ritual_ZN5DomUI18setElementIncludesEP11DomIncludes',
        self._addressOf(a),
    )

  @overload(DomResources)
  @overload(NoneType)
  def setElementResources(self, a: Optional[DomResources]) -> None:
    """
    Calls Qt's 'void DomUI::setElementResources(DomResources *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementResources

    Parameters
    ----------

    a : Optional[DomResources]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementResources(DomResources *a)
    self.uglySide.call(
        'ritual_ZN5DomUI19setElementResourcesEP12DomResources',
        self._addressOf(a),
    )

  @overload(DomConnections)
  @overload(NoneType)
  def setElementConnections(self, a: Optional[DomConnections]) -> None:
    """
    Calls Qt's 'void DomUI::setElementConnections(DomConnections *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementConnections

    Parameters
    ----------

    a : Optional[DomConnections]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementConnections(DomConnections *a)
    self.uglySide.call(
        'ritual_ZN5DomUI21setElementConnectionsEP14DomConnections',
        self._addressOf(a),
    )

  @overload(DomDesignerData)
  @overload(NoneType)
  def setElementDesignerdata(self, a: Optional[DomDesignerData]) -> None:
    """
    Calls Qt's 'void DomUI::setElementDesignerdata(DomDesignerData *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementDesignerdata

    Parameters
    ----------

    a : Optional[DomDesignerData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementDesignerdata(DomDesignerData *a)
    self.uglySide.call(
        'ritual_ZN5DomUI22setElementDesignerdataEP15DomDesignerData',
        self._addressOf(a),
    )

  @overload(DomSlots)
  @overload(NoneType)
  def setElementSlots(self, a: Optional[DomSlots]) -> None:
    """
    Calls Qt's 'void DomUI::setElementSlots(DomSlots *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementSlots

    Parameters
    ----------

    a : Optional[DomSlots]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementSlots(DomSlots *a)
    self.uglySide.call(
        'ritual_ZN5DomUI15setElementSlotsEP8DomSlots', self._addressOf(a),
    )

  @overload(DomButtonGroups)
  @overload(NoneType)
  def setElementButtonGroups(self, a: Optional[DomButtonGroups]) -> None:
    """
    Calls Qt's 'void DomUI::setElementButtonGroups(DomButtonGroups *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#setElementButtonGroups

    Parameters
    ----------

    a : Optional[DomButtonGroups]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUI::setElementButtonGroups(DomButtonGroups *a)
    self.uglySide.call(
        'ritual_ZN5DomUI22setElementButtonGroupsEP15DomButtonGroups',
        self._addressOf(a),
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
    Notes what was given, for Qt's 'DomUI::DomUI()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#DomUI
    """
    #  DomUI::DomUI()
    self._noteCreation(DomUI, lambda: Rituals.call('ritual_ZN5DomUIC1Ev'))

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

  def clearAttributeVersion(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeVersion()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeVersion
    """
    #  void DomUI::clearAttributeVersion()
    self.uglySide.call('ritual_ZN5DomUI21clearAttributeVersionEv')

  def clearAttributeLanguage(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeLanguage()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeLanguage
    """
    #  void DomUI::clearAttributeLanguage()
    self.uglySide.call('ritual_ZN5DomUI22clearAttributeLanguageEv')

  def clearAttributeDisplayname(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeDisplayname()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearAttributeDisplayname
    """
    #  void DomUI::clearAttributeDisplayname()
    self.uglySide.call('ritual_ZN5DomUI25clearAttributeDisplaynameEv')

  def clearAttributeIdbasedtr(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeIdbasedtr()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeIdbasedtr
    """
    #  void DomUI::clearAttributeIdbasedtr()
    self.uglySide.call('ritual_ZN5DomUI23clearAttributeIdbasedtrEv')

  def clearAttributeLabel(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeLabel()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeLabel
    """
    #  void DomUI::clearAttributeLabel()
    self.uglySide.call('ritual_ZN5DomUI19clearAttributeLabelEv')

  def clearAttributeConnectslotsbyname(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeConnectslotsbyname()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearAttributeConnectslotsbyname
    """
    #  void DomUI::clearAttributeConnectslotsbyname()
    self.uglySide.call('ritual_ZN5DomUI32clearAttributeConnectslotsbynameEv')

  def clearAttributeStdsetdef(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeStdsetdef()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeStdsetdef
    """
    #  void DomUI::clearAttributeStdsetdef()
    self.uglySide.call('ritual_ZN5DomUI23clearAttributeStdsetdefEv')

  def clearAttributeStdSetDef(self) -> None:
    """
    Calls Qt's 'void DomUI::clearAttributeStdSetDef()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearAttributeStdSetDef
    """
    #  void DomUI::clearAttributeStdSetDef()
    self.uglySide.call('ritual_ZN5DomUI23clearAttributeStdSetDefEv')

  def clearElementAuthor(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementAuthor()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementAuthor
    """
    #  void DomUI::clearElementAuthor()
    self.uglySide.call('ritual_ZN5DomUI18clearElementAuthorEv')

  def clearElementComment(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementComment()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementComment
    """
    #  void DomUI::clearElementComment()
    self.uglySide.call('ritual_ZN5DomUI19clearElementCommentEv')

  def clearElementExportMacro(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementExportMacro()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementExportMacro
    """
    #  void DomUI::clearElementExportMacro()
    self.uglySide.call('ritual_ZN5DomUI23clearElementExportMacroEv')

  def clearElementClass(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementClass()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementClass
    """
    #  void DomUI::clearElementClass()
    self.uglySide.call('ritual_ZN5DomUI17clearElementClassEv')

  def takeElementWidget(self) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget *DomUI::takeElementWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementWidget

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *DomUI::takeElementWidget()
    address = self.uglySide.call('ritual_ZN5DomUI17takeElementWidgetEv')
    from . import DomWidget
    return DomWidget._cuteAt(address)

  def clearElementWidget(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementWidget
    """
    #  void DomUI::clearElementWidget()
    self.uglySide.call('ritual_ZN5DomUI18clearElementWidgetEv')

  def takeElementLayoutDefault(self) -> Optional[DomLayoutDefault]:
    """
    Calls Qt's 'DomLayoutDefault *DomUI::takeElementLayoutDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#takeElementLayoutDefault

    Returns
    -------

    Optional[DomLayoutDefault]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayoutDefault *DomUI::takeElementLayoutDefault()
    address = self.uglySide.call(
        'ritual_ZN5DomUI24takeElementLayoutDefaultEv',
    )
    from . import DomLayoutDefault
    return DomLayoutDefault._cuteAt(address)

  def clearElementLayoutDefault(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementLayoutDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementLayoutDefault
    """
    #  void DomUI::clearElementLayoutDefault()
    self.uglySide.call('ritual_ZN5DomUI25clearElementLayoutDefaultEv')

  def takeElementLayoutFunction(self) -> Optional[DomLayoutFunction]:
    """
    Calls Qt's 'DomLayoutFunction *DomUI::takeElementLayoutFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#takeElementLayoutFunction

    Returns
    -------

    Optional[DomLayoutFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayoutFunction *DomUI::takeElementLayoutFunction()
    address = self.uglySide.call(
        'ritual_ZN5DomUI25takeElementLayoutFunctionEv',
    )
    from . import DomLayoutFunction
    return DomLayoutFunction._cuteAt(address)

  def clearElementLayoutFunction(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementLayoutFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementLayoutFunction
    """
    #  void DomUI::clearElementLayoutFunction()
    self.uglySide.call('ritual_ZN5DomUI26clearElementLayoutFunctionEv')

  def clearElementPixmapFunction(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementPixmapFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementPixmapFunction
    """
    #  void DomUI::clearElementPixmapFunction()
    self.uglySide.call('ritual_ZN5DomUI26clearElementPixmapFunctionEv')

  def takeElementCustomWidgets(self) -> Optional[DomCustomWidgets]:
    """
    Calls Qt's 'DomCustomWidgets *DomUI::takeElementCustomWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#takeElementCustomWidgets

    Returns
    -------

    Optional[DomCustomWidgets]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomCustomWidgets *DomUI::takeElementCustomWidgets()
    address = self.uglySide.call(
        'ritual_ZN5DomUI24takeElementCustomWidgetsEv',
    )
    from . import DomCustomWidgets
    return DomCustomWidgets._cuteAt(address)

  def clearElementCustomWidgets(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementCustomWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementCustomWidgets
    """
    #  void DomUI::clearElementCustomWidgets()
    self.uglySide.call('ritual_ZN5DomUI25clearElementCustomWidgetsEv')

  def takeElementTabStops(self) -> Optional[DomTabStops]:
    """
    Calls Qt's 'DomTabStops *DomUI::takeElementTabStops()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementTabStops

    Returns
    -------

    Optional[DomTabStops]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomTabStops *DomUI::takeElementTabStops()
    address = self.uglySide.call('ritual_ZN5DomUI19takeElementTabStopsEv')
    from . import DomTabStops
    return DomTabStops._cuteAt(address)

  def clearElementTabStops(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementTabStops()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementTabStops
    """
    #  void DomUI::clearElementTabStops()
    self.uglySide.call('ritual_ZN5DomUI20clearElementTabStopsEv')

  def takeElementIncludes(self) -> Optional[DomIncludes]:
    """
    Calls Qt's 'DomIncludes *DomUI::takeElementIncludes()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementIncludes

    Returns
    -------

    Optional[DomIncludes]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomIncludes *DomUI::takeElementIncludes()
    address = self.uglySide.call('ritual_ZN5DomUI19takeElementIncludesEv')
    from . import DomIncludes
    return DomIncludes._cuteAt(address)

  def clearElementIncludes(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementIncludes()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementIncludes
    """
    #  void DomUI::clearElementIncludes()
    self.uglySide.call('ritual_ZN5DomUI20clearElementIncludesEv')

  def takeElementResources(self) -> Optional[DomResources]:
    """
    Calls Qt's 'DomResources *DomUI::takeElementResources()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementResources

    Returns
    -------

    Optional[DomResources]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResources *DomUI::takeElementResources()
    address = self.uglySide.call('ritual_ZN5DomUI20takeElementResourcesEv')
    from . import DomResources
    return DomResources._cuteAt(address)

  def clearElementResources(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementResources()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementResources
    """
    #  void DomUI::clearElementResources()
    self.uglySide.call('ritual_ZN5DomUI21clearElementResourcesEv')

  def takeElementConnections(self) -> Optional[DomConnections]:
    """
    Calls Qt's 'DomConnections *DomUI::takeElementConnections()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementConnections

    Returns
    -------

    Optional[DomConnections]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomConnections *DomUI::takeElementConnections()
    address = self.uglySide.call('ritual_ZN5DomUI22takeElementConnectionsEv')
    from . import DomConnections
    return DomConnections._cuteAt(address)

  def clearElementConnections(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementConnections()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementConnections
    """
    #  void DomUI::clearElementConnections()
    self.uglySide.call('ritual_ZN5DomUI23clearElementConnectionsEv')

  def takeElementDesignerdata(self) -> Optional[DomDesignerData]:
    """
    Calls Qt's 'DomDesignerData *DomUI::takeElementDesignerdata()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementDesignerdata

    Returns
    -------

    Optional[DomDesignerData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDesignerData *DomUI::takeElementDesignerdata()
    address = self.uglySide.call(
        'ritual_ZN5DomUI23takeElementDesignerdataEv',
    )
    from . import DomDesignerData
    return DomDesignerData._cuteAt(address)

  def clearElementDesignerdata(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementDesignerdata()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementDesignerdata
    """
    #  void DomUI::clearElementDesignerdata()
    self.uglySide.call('ritual_ZN5DomUI24clearElementDesignerdataEv')

  def takeElementSlots(self) -> Optional[DomSlots]:
    """
    Calls Qt's 'DomSlots *DomUI::takeElementSlots()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementSlots

    Returns
    -------

    Optional[DomSlots]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSlots *DomUI::takeElementSlots()
    address = self.uglySide.call('ritual_ZN5DomUI16takeElementSlotsEv')
    from . import DomSlots
    return DomSlots._cuteAt(address)

  def clearElementSlots(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementSlots()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#clearElementSlots
    """
    #  void DomUI::clearElementSlots()
    self.uglySide.call('ritual_ZN5DomUI17clearElementSlotsEv')

  def takeElementButtonGroups(self) -> Optional[DomButtonGroups]:
    """
    Calls Qt's 'DomButtonGroups *DomUI::takeElementButtonGroups()'.

    Qt's own words: https://doc.qt.io/qt-6/domui.html#takeElementButtonGroups

    Returns
    -------

    Optional[DomButtonGroups]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomButtonGroups *DomUI::takeElementButtonGroups()
    address = self.uglySide.call(
        'ritual_ZN5DomUI23takeElementButtonGroupsEv',
    )
    from . import DomButtonGroups
    return DomButtonGroups._cuteAt(address)

  def clearElementButtonGroups(self) -> None:
    """
    Calls Qt's 'void DomUI::clearElementButtonGroups()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domui.html#clearElementButtonGroups
    """
    #  void DomUI::clearElementButtonGroups()
    self.uglySide.call('ritual_ZN5DomUI24clearElementButtonGroupsEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomUI::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomUI.read' has no cute function yet. Qt's 'void "
        "DomUI::read(QXmlStreamReader &reader)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomUI::write(QXmlStreamWriter &writer, const QString &tagName)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomUI.write' has no cute function yet. Qt's 'void "
        "DomUI::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
