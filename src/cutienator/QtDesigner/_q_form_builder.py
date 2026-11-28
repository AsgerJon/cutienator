"""
QFormBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/formbuilder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QAbstractFormBuilder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtGui import QAction, QActionGroup
  from ..QtWidgets import QLayout, QLayoutItem, QWidget
  from ..QtUiPlugin import QDesignerCustomWidgetInterface
  from . import DomAction, DomActionGroup, DomConnections, DomLayout
  from . import DomLayoutItem, DomProperty, DomUI, DomWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomAction = WAIT['DomAction']
  DomActionGroup = WAIT['DomActionGroup']
  DomConnections = WAIT['DomConnections']
  DomLayout = WAIT['DomLayout']
  DomLayoutItem = WAIT['DomLayoutItem']
  DomProperty = WAIT['DomProperty']
  DomUI = WAIT['DomUI']
  DomWidget = WAIT['DomWidget']
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QObject = WAIT['QObject']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFormBuilder(QAbstractFormBuilder):
  """
  The cute side of Qt's QFormBuilder: a plain Python object standing in front
  of one C++ QFormBuilder.

  It is built on the cute 'QAbstractFormBuilder', as Qt's QFormBuilder is
  built on Qt's QAbstractFormBuilder, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFormBuilder that has a ritual and that Python can
  call so far, 13 names in all: 'pluginPaths', 'clearPluginPaths',
  'addPluginPath', 'setPluginPath', 'customWidgets', 'create',
  'createWidget', 'createLayout', 'createConnections', 'addItem',
  'updateCustomWidgets', 'applyProperties', 'widgetByName'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFormBuilder::~QFormBuilder()': the destructor: Python never
    removes a C++ QFormBuilder.

  What to expect
  --------------

  - The C++ QFormBuilder is created at the first use, not by
    'QFormBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFormBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWidget, str)
  @overload(NoneType, str)
  def widgetByName(
      topLevel: Optional[QWidget],
      name: str,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormBuilder::widgetByName(QWidget *topLevel, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#widgetByName

    Parameters
    ----------

    topLevel : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormBuilder::widgetByName(QWidget *topLevel, const QString
    #      &name)
    address = Rituals.call(
        'ritual_ZN12QFormBuilder12widgetByNameEP7QWidgetRK7QString',
        CuteMixin._addressOf(topLevel), name,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFormBuilder'

  #  A C++ QFormBuilder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFormBuilder'

  #  The functions Qt calls itself that QFormBuilder is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'updateCustomWidgets': (
          ('_ZN12QFormBuilder19updateCustomWidgetsEv',
           ('nothing', 'nothing', ''),
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

  def pluginPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFormBuilder::pluginPaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#pluginPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFormBuilder::pluginPaths() const
    address = self.uglySide.call('ritual_ZNK12QFormBuilder11pluginPathsEv')
    return QStringList._cuteOwning(address)

  def customWidgets(self) -> QList[QDesignerCustomWidgetInterface]:
    """
    Calls Qt's 'QList<QDesignerCustomWidgetInterface *>
    QFormBuilder::customWidgets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#customWidgets

    Returns
    -------

    QList[QDesignerCustomWidgetInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDesignerCustomWidgetInterface *> QFormBuilder::customWidgets()
    #      const
    address = self.uglySide.call('ritual_ZNK12QFormBuilder13customWidgetsEv')
    from ..QtUiPlugin import QDesignerCustomWidgetInterface
    return QList[QDesignerCustomWidgetInterface]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setPluginPath(self, pluginPaths: QStringList) -> None:
    """
    Calls Qt's 'void QFormBuilder::setPluginPath(const QStringList
    &pluginPaths)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#setPluginPath

    Parameters
    ----------

    pluginPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFormBuilder::setPluginPath(const QStringList &pluginPaths)
    self.uglySide.call(
        'ritual_ZN12QFormBuilder13setPluginPathERK5QListI7QStringE',
        self._valueOf(pluginPaths),
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
    Notes what was given, for Qt's 'QFormBuilder::QFormBuilder()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#QFormBuilder
    """
    #  QFormBuilder::QFormBuilder()
    self._noteCreation(QFormBuilder, lambda: Rituals.call(
        'ritual_ZN12QFormBuilderC1Ev',
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

  def clearPluginPaths(self) -> None:
    """
    Calls Qt's 'void QFormBuilder::clearPluginPaths()'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#clearPluginPaths
    """
    #  void QFormBuilder::clearPluginPaths()
    self.uglySide.call('ritual_ZN12QFormBuilder16clearPluginPathsEv')

  @overload(str)
  def addPluginPath(self, pluginPath: str) -> None:
    """
    Calls Qt's 'void QFormBuilder::addPluginPath(const QString &pluginPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#addPluginPath

    Parameters
    ----------

    pluginPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFormBuilder::addPluginPath(const QString &pluginPath)
    self.uglySide.call(
        'ritual_ZN12QFormBuilder13addPluginPathERK7QString', pluginPath,
    )

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def create(
      self,
      ui: Optional[DomUI],
      parentWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormBuilder::create(DomUI *ui, QWidget
    *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormBuilder::create(DomUI *ui, QWidget *parentWidget)
    ritual = 'ritual_ZN12QFormBuilder6createEP5DomUIP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFormBuilder6createEP5DomUIP7QWidget'
    address = self.uglySide.call(
        ritual, self._addressOf(ui), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(DomWidget, QWidget)
  @overload(DomWidget, NoneType)
  def create(
      self,
      ui_widget: Optional[DomWidget],
      parentWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormBuilder::create(DomWidget *ui_widget, QWidget
    *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormBuilder::create(DomWidget *ui_widget, QWidget
    #      *parentWidget)
    ritual = 'ritual_ZN12QFormBuilder6createEP9DomWidgetP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFormBuilder6createEP9DomWidgetP7QWidget'
    address = self.uglySide.call(
        ritual, self._addressOf(ui_widget), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(DomLayout, QLayout, QWidget)
  @overload(DomLayout, QLayout, NoneType)
  @overload(DomLayout, NoneType, QWidget)
  @overload(DomLayout, NoneType, NoneType)
  @overload(NoneType, QLayout, QWidget)
  @overload(NoneType, QLayout, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def create(
      self,
      ui_layout: Optional[DomLayout],
      layout: Optional[QLayout],
      parentWidget: Optional[QWidget],
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QFormBuilder::create(DomLayout *ui_layout, QLayout
    *layout, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui_layout : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QFormBuilder::create(DomLayout *ui_layout, QLayout *layout,
    #      QWidget *parentWidget)
    ritual = 'ritual_ZN12QFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_layout), self._addressOf(layout),
        self._addressOf(parentWidget),
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @overload(DomLayoutItem, QLayout, QWidget)
  @overload(DomLayoutItem, QLayout, NoneType)
  @overload(DomLayoutItem, NoneType, QWidget)
  @overload(DomLayoutItem, NoneType, NoneType)
  def create(
      self,
      ui_layoutItem: Optional[DomLayoutItem],
      layout: Optional[QLayout],
      parentWidget: Optional[QWidget],
  ) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QFormBuilder::create(DomLayoutItem
    *ui_layoutItem, QLayout *layout, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui_layoutItem : Optional[DomLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QFormBuilder::create(DomLayoutItem *ui_layoutItem,
    #      QLayout *layout, QWidget *parentWidget)
    ritual = (
        'ritual_ZN12QFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder6createEP13DomLayoutItemP7QLayoutP7QW'
          'idget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_layoutItem), self._addressOf(layout),
        self._addressOf(parentWidget),
    )
    from ..QtWidgets import QLayoutItem
    return QLayoutItem._cuteAt(address)

  @overload(DomAction, QObject)
  @overload(DomAction, NoneType)
  @overload(NoneType, QObject)
  def create(
      self,
      ui_action: Optional[DomAction],
      parent: Optional[QObject],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QFormBuilder::create(DomAction *ui_action, QObject
    *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui_action : Optional[DomAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QFormBuilder::create(DomAction *ui_action, QObject *parent)
    ritual = 'ritual_ZN12QFormBuilder6createEP9DomActionP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFormBuilder6createEP9DomActionP7QObject'
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_action), self._addressOf(parent, 'QObject'),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(DomActionGroup, QObject)
  @overload(DomActionGroup, NoneType)
  def create(
      self,
      ui_action_group: Optional[DomActionGroup],
      parent: Optional[QObject],
  ) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup *QFormBuilder::create(DomActionGroup
    *ui_action_group, QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#create

    Parameters
    ----------

    ui_action_group : Optional[DomActionGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup *QFormBuilder::create(DomActionGroup *ui_action_group,
    #      QObject *parent)
    ritual = 'ritual_ZN12QFormBuilder6createEP14DomActionGroupP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder6createEP14DomActionGroupP7QObject')
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_action_group), self._addressOf(parent, 'QObject'),
    )
    from ..QtGui import QActionGroup
    return QActionGroup._cuteAt(address)

  @overload(str, QWidget, str)
  @overload(str, NoneType, str)
  def createWidget(
      self,
      widgetName: str,
      parentWidget: Optional[QWidget],
      name: str,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormBuilder::createWidget(const QString
    &widgetName, QWidget *parentWidget, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#createWidget

    Parameters
    ----------

    widgetName : str
      Passed on as it is: a QString is made of it for the call.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormBuilder::createWidget(const QString &widgetName, QWidget
    #      *parentWidget, const QString &name)
    ritual = 'ritual_ZN12QFormBuilder12createWidgetERK7QStringP7QWidgetS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder12createWidgetERK7QStringP7QWidgetS2_')
    address = self.uglySide.call(
        ritual, widgetName, self._addressOf(parentWidget), name,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str, QObject, str)
  @overload(str, NoneType, str)
  def createLayout(
      self,
      layoutName: str,
      parent: Optional[QObject],
      name: str,
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QFormBuilder::createLayout(const QString
    &layoutName, QObject *parent, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#createLayout

    Parameters
    ----------

    layoutName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QFormBuilder::createLayout(const QString &layoutName, QObject
    #      *parent, const QString &name)
    ritual = 'ritual_ZN12QFormBuilder12createLayoutERK7QStringP7QObjectS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder12createLayoutERK7QStringP7QObjectS2_')
    address = self.uglySide.call(
        ritual, layoutName, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @overload(DomConnections, QWidget)
  @overload(DomConnections, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createConnections(
      self,
      connections: Optional[DomConnections],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormBuilder::createConnections(DomConnections
    *connections, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilder.html#createConnections

    Parameters
    ----------

    connections : Optional[DomConnections]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilder::createConnections(DomConnections *connections,
    #      QWidget *widget)
    ritual = (
        'ritual_ZN12QFormBuilder17createConnectionsEP14DomConnectionsP7QWid'
        'get')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder17createConnectionsEP14DomConnections'
          'P7QWidget')
    self.uglySide.call(
        ritual, self._addressOf(connections), self._addressOf(widget),
    )

  @overload(DomLayoutItem, QLayoutItem, QLayout)
  @overload(DomLayoutItem, QLayoutItem, NoneType)
  @overload(DomLayoutItem, NoneType, QLayout)
  @overload(DomLayoutItem, NoneType, NoneType)
  @overload(NoneType, QLayoutItem, QLayout)
  @overload(NoneType, QLayoutItem, NoneType)
  @overload(NoneType, NoneType, QLayout)
  @overload(NoneType, NoneType, NoneType)
  def addItem(
      self,
      ui_item: Optional[DomLayoutItem],
      item: Optional[QLayoutItem],
      layout: Optional[QLayout],
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilder::addItem(DomLayoutItem *ui_item,
    QLayoutItem *item, QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#addItem

    Parameters
    ----------

    ui_item : Optional[DomLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem *item,
    #      QLayout *layout)
    ritual = (
        'ritual_ZN12QFormBuilder7addItemEP13DomLayoutItemP11QLayoutItemP7QL'
        'ayout')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QFormBuilder7addItemEP13DomLayoutItemP11QLayoutIt'
          'emP7QLayout')
    return self.uglySide.call(
        ritual,
        self._addressOf(ui_item), self._addressOf(item, 'QLayoutItem'),
        self._addressOf(layout),
    )

  @overload(DomWidget, QWidget, QWidget)
  @overload(DomWidget, QWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QWidget, QWidget)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  def addItem(
      self,
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
      parentWidget: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilder::addItem(DomWidget *ui_widget, QWidget
    *widget, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#addItem

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilder::addItem(DomWidget *ui_widget, QWidget *widget,
    #      QWidget *parentWidget)
    ritual = 'ritual_ZN12QFormBuilder7addItemEP9DomWidgetP7QWidgetS3_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFormBuilder7addItemEP9DomWidgetP7QWidgetS3_'
    return self.uglySide.call(
        ritual,
        self._addressOf(ui_widget), self._addressOf(widget),
        self._addressOf(parentWidget),
    )

  def updateCustomWidgets(self) -> None:
    """
    Calls Qt's 'void QFormBuilder::updateCustomWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilder.html#updateCustomWidgets
    """
    #  void QFormBuilder::updateCustomWidgets()
    ritual = 'ritual_ZN12QFormBuilder19updateCustomWidgetsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFormBuilder19updateCustomWidgetsEv'
    self.uglySide.call(ritual)

  @overload(QObject, QList[DomProperty])
  @overload(NoneType, QList[DomProperty])
  def applyProperties(
      self,
      o: Optional[QObject],
      properties: QList[DomProperty],
  ) -> None:
    """
    Calls Qt's 'void QFormBuilder::applyProperties(QObject *o, const
    QList<DomProperty *> &properties)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilder.html#applyProperties

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFormBuilder::applyProperties(QObject *o, const QList<DomProperty
    #      *> &properties)
    self.uglySide.call(
        'ritual_ZN12QFormBuilder15applyPropertiesEP7QObjectRK5QListIP11DomP'
        'ropertyE',
        self._addressOf(o, 'QObject'), self._valueOf(properties),
    )
