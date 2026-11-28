"""
QAbstractFormBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformbuilder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QHash, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDir, QIODevice, QMetaEnum, QMetaObject, QObject
  from ..QtCore import QVariant
  from ..QtGui import QAction, QActionGroup, QBrush, QPalette
  from ..QtWidgets import QAbstractButton, QAbstractItemView, QButtonGroup
  from ..QtWidgets import QComboBox, QLayout, QLayoutItem, QListWidget
  from ..QtWidgets import QSpacerItem, QTableWidget, QTreeWidget, QWidget
  from . import DomAction, DomActionGroup, DomActionRef, DomBrush
  from . import DomButtonGroup, DomButtonGroups, DomColorGroup
  from . import DomConnections, DomCustomWidgets, DomLayout, DomLayoutItem
  from . import DomProperty, DomResourcePixmap, DomResources, DomSpacer
  from . import DomString, DomTabStops, DomUI, DomWidget, QResourceBuilder
  from . import QTextBuilder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomAction = WAIT['DomAction']
  DomActionGroup = WAIT['DomActionGroup']
  DomBrush = WAIT['DomBrush']
  DomConnections = WAIT['DomConnections']
  DomCustomWidgets = WAIT['DomCustomWidgets']
  DomLayout = WAIT['DomLayout']
  DomLayoutItem = WAIT['DomLayoutItem']
  DomProperty = WAIT['DomProperty']
  DomResources = WAIT['DomResources']
  DomString = WAIT['DomString']
  DomTabStops = WAIT['DomTabStops']
  DomUI = WAIT['DomUI']
  DomWidget = WAIT['DomWidget']
  QAbstractButton = WAIT['QAbstractButton']
  QAbstractItemView = WAIT['QAbstractItemView']
  QAction = WAIT['QAction']
  QActionGroup = WAIT['QActionGroup']
  QBrush = WAIT['QBrush']
  QButtonGroup = WAIT['QButtonGroup']
  QComboBox = WAIT['QComboBox']
  QDir = WAIT['QDir']
  QIODevice = WAIT['QIODevice']
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QListWidget = WAIT['QListWidget']
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']
  QPalette = WAIT['QPalette']
  QResourceBuilder = WAIT['QResourceBuilder']
  QSpacerItem = WAIT['QSpacerItem']
  QTableWidget = WAIT['QTableWidget']
  QTextBuilder = WAIT['QTextBuilder']
  QTreeWidget = WAIT['QTreeWidget']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractFormBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFormBuilder: a plain Python object standing
  in front of one C++ QAbstractFormBuilder.

  What exists
  -----------

  Every function of Qt's QAbstractFormBuilder that has a ritual and that
  Python can call so far, 60 names in all: 'workingDirectory',
  'setWorkingDirectory', 'load', 'save', 'errorString', 'loadExtraInfo',
  'create', 'addMenuAction', 'applyProperties', 'applyPropertyInternally',
  'applyTabStops', 'createWidget', 'createLayout', 'createAction',
  'createActionGroup', 'createCustomWidgets', 'createConnections',
  'createResources', 'addItem', 'saveExtraInfo', 'saveDom',
  'createActionRefDom', 'createDom', 'saveConnections', 'saveCustomWidgets',
  'saveTabStops', 'saveResources', 'saveButtonGroups', 'computeProperties',
  'checkProperty', 'createProperty', 'loadListWidgetExtraInfo',
  'loadTreeWidgetExtraInfo', 'loadTableWidgetExtraInfo',
  'loadComboBoxExtraInfo', 'loadButtonExtraInfo', 'loadItemViewExtraInfo',
  'saveListWidgetExtraInfo', 'saveTreeWidgetExtraInfo',
  'saveTableWidgetExtraInfo', 'saveComboBoxExtraInfo', 'saveButtonExtraInfo',
  'saveItemViewExtraInfo', 'setResourceBuilder', 'resourceBuilder',
  'saveResource', 'setTextBuilder', 'textBuilder', 'saveText', 'toVariant',
  'toString', 'propertyMap', 'saveColorGroup', 'setupBrush', 'saveBrush',
  'reset', 'initialize', 'toolBarAreaMetaEnum', 'domPixmap',
  'toolbarAreaFromDOMAttributes'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractFormBuilder::~QAbstractFormBuilder()': the destructor:
    Python never removes a C++ QAbstractFormBuilder.
  - Qt's 'void QAbstractFormBuilder::layoutInfo(DomLayout *layout, QObject
    *parent, int *margin, int *spacing)': takes a number to change where it
    is.
  - Qt's 'void QAbstractFormBuilder::setupColorGroup(QPalette &palette,
    QPalette::ColorGroup colorGroup, DomColorGroup *group)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QAbstractFormBuilder::setIconProperty(DomProperty &a0, const
    IconPaths &a1) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QAbstractFormBuilder::setPixmapProperty(DomProperty &a0, const
    IconPaths &a1) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 82 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QAbstractFormBuilder is created at the first use, not by
    'QAbstractFormBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFormBuilder.
  - Each name of Qt's QAbstractFormBuilder that has no cute function yet,
    'layoutInfo', 'setIconProperty', 'setPixmapProperty', 'setupColorGroup',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(DomString)
  @overload(NoneType)
  def toString(str: Optional[DomString]) -> str:
    """
    Calls Qt's 'QString QAbstractFormBuilder::toString(const DomString
    *str)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#toString

    Parameters
    ----------

    str : Optional[DomString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFormBuilder::toString(const DomString *str)
    return Rituals.call(
        'ritual_ZN20QAbstractFormBuilder8toStringEPK9DomString',
        CuteMixin._addressOf(str),
    )

  @staticmethod
  @overload(QList[DomProperty])
  def propertyMap(properties: QList[DomProperty]) -> QHash[str, DomProperty]:
    """
    Calls Qt's 'DomPropertyHash QAbstractFormBuilder::propertyMap(const
    QList<DomProperty *> &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#propertyMap

    Parameters
    ----------

    properties : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QHash[str, DomProperty]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  DomPropertyHash QAbstractFormBuilder::propertyMap(const
    #      QList<DomProperty *> &properties)
    address = Rituals.call(
        'ritual_ZN20QAbstractFormBuilder11propertyMapERK5QListIP11DomProper'
        'tyE',
        CuteMixin._valueOf(properties),
    )
    from . import DomProperty
    return QHash[str, DomProperty]._cuteOwning(address)

  @staticmethod
  def toolBarAreaMetaEnum() -> QMetaEnum:
    """
    Calls Qt's 'QMetaEnum QAbstractFormBuilder::toolBarAreaMetaEnum()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#toolBarAreaMetaEnum

    Returns
    -------

    QMetaEnum
      A new cute QMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QMetaEnum QAbstractFormBuilder::toolBarAreaMetaEnum()
    address = Rituals.call(
        'ritual_ZN20QAbstractFormBuilder19toolBarAreaMetaEnumEv',
    )
    from ..QtCore import QMetaEnum
    return QMetaEnum._cuteOwning(address)

  @staticmethod
  @overload(DomProperty)
  @overload(NoneType)
  def domPixmap(p: Optional[DomProperty]) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'const DomResourcePixmap
    *QAbstractFormBuilder::domPixmap(const DomProperty *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#domPixmap

    Parameters
    ----------

    p : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const DomResourcePixmap *QAbstractFormBuilder::domPixmap(const
    #      DomProperty *p)
    address = Rituals.call(
        'ritual_ZN20QAbstractFormBuilder9domPixmapEPK11DomProperty',
        CuteMixin._addressOf(p),
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  @staticmethod
  @overload(QHash[str, DomProperty])
  def toolbarAreaFromDOMAttributes(
      attributeMap: QHash[str, DomProperty],
  ) -> Qt.ToolBarArea:
    """
    Calls Qt's 'Qt::ToolBarArea
    QAbstractFormBuilder::toolbarAreaFromDOMAttributes(const DomPropertyHash
    &attributeMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html

    Parameters
    ----------

    attributeMap : QHash[str, DomProperty]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Qt.ToolBarArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ToolBarArea(number)'
      gives.
    """
    #  Qt::ToolBarArea
    #      QAbstractFormBuilder::toolbarAreaFromDOMAttributes(const
    #      DomPropertyHash &attributeMap)
    return Qt.ToolBarArea(Rituals.call(
        'ritual_ZN20QAbstractFormBuilder28toolbarAreaFromDOMAttributesERK5Q'
        'HashI7QStringP11DomPropertyE',
        CuteMixin._valueOf(attributeMap),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFormBuilder'

  #  A C++ QAbstractFormBuilder Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractFormBuilder'

  #  The functions Qt calls itself that QAbstractFormBuilder is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'applyProperties': (
          'void QAbstractFormBuilder::applyProperties(QObject *, const '
          'QList<DomProperty *> &)',
      ),
      'computeProperties': (
          'QList<DomProperty *> '
          'QAbstractFormBuilder::computeProperties(QObject *)',
      ),
      'layoutInfo': (
          'void QAbstractFormBuilder::layoutInfo(DomLayout *, QObject *, '
          'int *, int *)',
      ),
  }

  #  The functions Qt calls itself that QAbstractFormBuilder is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'load': (
          ('_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'save': (
          ('_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'loadExtraInfo': (
          ('_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidgetS3'
           '_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'create': (
          ('_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidget',
           ('address', 'address', 'QtWidgets:QLayout'),
           (
               ('address', 'address', 'QtDesigner:DomLayout'),
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7QWi'
           'dget',
           ('address', 'address', 'QtWidgets:QLayoutItem'),
           (
               ('address', 'address', 'QtDesigner:DomLayoutItem'),
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject',
           ('address', 'address', 'QtGui:QAction'),
           (
               ('address', 'address', 'QtDesigner:DomAction'),
               ('address', 'address', 'QtCore:QObject'),
           )),
          ('_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject',
           ('address', 'address', 'QtGui:QActionGroup'),
           (
               ('address', 'address', 'QtDesigner:DomActionGroup'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'addMenuAction': (
          ('_ZN20QAbstractFormBuilder13addMenuActionEP7QAction',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
      ),
      'applyTabStops': (
          ('_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabStop'
           's',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtDesigner:DomTabStops'),
           )),
      ),
      'createWidget': (
          ('_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS2_',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
           )),
      ),
      'createLayout': (
          ('_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS2_',
           ('address', 'address', 'QtWidgets:QLayout'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createAction': (
          ('_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString',
           ('address', 'address', 'QtGui:QAction'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createActionGroup': (
          ('_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QStrin'
           'g',
           ('address', 'address', 'QtGui:QActionGroup'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createCustomWidgets': (
          ('_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomWidg'
           'ets',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomCustomWidgets'),
           )),
      ),
      'createConnections': (
          ('_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectionsP'
           '7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomConnections'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createResources': (
          ('_ZN20QAbstractFormBuilder15createResourcesEP12DomResources',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomResources'),
           )),
      ),
      'addItem': (
          ('_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayoutIte'
           'mP7QLayout',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomLayoutItem'),
               ('address', 'address', 'QtWidgets:QLayoutItem'),
               ('address', 'address', 'QtWidgets:QLayout'),
           )),
          ('_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'saveExtraInfo': (
          ('_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidgetS3'
           '_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('address', 'address', 'QtDesigner:DomWidget'),
           )),
      ),
      'saveDom': (
          ('_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createActionRefDom': (
          ('_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction',
           ('address', 'address', 'QtDesigner:DomActionRef'),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
      ),
      'createDom': (
          ('_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb',
           ('address', 'address', 'QtDesigner:DomWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('bool', 'number', ''),
           )),
          ('_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9DomWi'
           'dget',
           ('address', 'address', 'QtDesigner:DomLayout'),
           (
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'address', 'QtDesigner:DomLayout'),
               ('address', 'address', 'QtDesigner:DomWidget'),
           )),
          ('_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayoutP9'
           'DomWidget',
           ('address', 'address', 'QtDesigner:DomLayoutItem'),
           (
               ('address', 'address', 'QtWidgets:QLayoutItem'),
               ('address', 'address', 'QtDesigner:DomLayout'),
               ('address', 'address', 'QtDesigner:DomWidget'),
           )),
          ('_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayoutP9'
           'DomWidget',
           ('address', 'address', 'QtDesigner:DomSpacer'),
           (
               ('address', 'address', 'QtWidgets:QSpacerItem'),
               ('address', 'address', 'QtDesigner:DomLayout'),
               ('address', 'address', 'QtDesigner:DomWidget'),
           )),
          ('_ZN20QAbstractFormBuilder9createDomEP7QAction',
           ('address', 'address', 'QtDesigner:DomAction'),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
          ('_ZN20QAbstractFormBuilder9createDomEP12QActionGroup',
           ('address', 'address', 'QtDesigner:DomActionGroup'),
           (
               ('address', 'address', 'QtGui:QActionGroup'),
           )),
      ),
      'saveConnections': (
          ('_ZN20QAbstractFormBuilder15saveConnectionsEv',
           ('address', 'address', 'QtDesigner:DomConnections'),
           ()),
      ),
      'saveCustomWidgets': (
          ('_ZN20QAbstractFormBuilder17saveCustomWidgetsEv',
           ('address', 'address', 'QtDesigner:DomCustomWidgets'),
           ()),
      ),
      'saveTabStops': (
          ('_ZN20QAbstractFormBuilder12saveTabStopsEv',
           ('address', 'address', 'QtDesigner:DomTabStops'),
           ()),
      ),
      'saveResources': (
          ('_ZN20QAbstractFormBuilder13saveResourcesEv',
           ('address', 'address', 'QtDesigner:DomResources'),
           ()),
      ),
      'checkProperty': (
          ('_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
           )),
      ),
      'createProperty': (
          ('_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStringRK'
           '8QVariant',
           ('address', 'address', 'QtDesigner:DomProperty'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def workingDirectory(self) -> QDir:
    """
    Calls Qt's 'QDir QAbstractFormBuilder::workingDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#workingDirectory

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QAbstractFormBuilder::workingDirectory() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder16workingDirectoryEv',
    )
    from ..QtCore import QDir
    return QDir._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QAbstractFormBuilder::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFormBuilder::errorString() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder11errorStringEv',
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def checkProperty(self, obj: Optional[QObject], prop: str) -> bool:
    """
    Calls Qt's 'bool QAbstractFormBuilder::checkProperty(QObject *obj, const
    QString &prop) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#checkProperty

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prop : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAbstractFormBuilder::checkProperty(QObject *obj, const QString
    #      &prop) const
    ritual = (
        'ritual_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7QStrin'
        'g')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QAbstractFormBuilder13checkPropertyEP7QObjectRK7'
          'QString')
    return self.uglySide.call(ritual, self._addressOf(obj, 'QObject'), prop)

  def resourceBuilder(self) -> Optional[QResourceBuilder]:
    """
    Calls Qt's 'QResourceBuilder *QAbstractFormBuilder::resourceBuilder()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#resourceBuilder

    Returns
    -------

    Optional[QResourceBuilder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QResourceBuilder *QAbstractFormBuilder::resourceBuilder() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder15resourceBuilderEv',
    )
    from . import QResourceBuilder
    return QResourceBuilder._cuteAt(address)

  @overload(QVariant)
  def saveResource(self, v: QVariant) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QAbstractFormBuilder::saveResource(const
    QVariant &v) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveResource

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QAbstractFormBuilder::saveResource(const QVariant &v)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder12saveResourceERK8QVariant',
        self._valueOf(v),
    )
    from . import DomProperty
    return DomProperty._cuteAt(address)

  def textBuilder(self) -> Optional[QTextBuilder]:
    """
    Calls Qt's 'QTextBuilder *QAbstractFormBuilder::textBuilder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#textBuilder

    Returns
    -------

    Optional[QTextBuilder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextBuilder *QAbstractFormBuilder::textBuilder() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder11textBuilderEv',
    )
    from . import QTextBuilder
    return QTextBuilder._cuteAt(address)

  @overload(str, QVariant)
  def saveText(
      self,
      attributeName: str,
      v: QVariant,
  ) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QAbstractFormBuilder::saveText(const QString
    &attributeName, const QVariant &v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#saveText

    Parameters
    ----------

    attributeName : str
      Passed on as it is: a QString is made of it for the call.

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QAbstractFormBuilder::saveText(const QString
    #      &attributeName, const QVariant &v) const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractFormBuilder8saveTextERK7QStringRK8QVariant',
        attributeName, self._valueOf(v),
    )
    from . import DomProperty
    return DomProperty._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDir)
  def setWorkingDirectory(self, directory: QDir) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::setWorkingDirectory(const QDir
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#setWorkingDirectory

    Parameters
    ----------

    directory : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  void QAbstractFormBuilder::setWorkingDirectory(const QDir &directory)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder19setWorkingDirectoryERK4QDir',
        self._valueOf(directory),
    )

  @overload(QResourceBuilder)
  @overload(NoneType)
  def setResourceBuilder(self, builder: Optional[QResourceBuilder]) -> None:
    """
    Calls Qt's 'void
    QAbstractFormBuilder::setResourceBuilder(QResourceBuilder *builder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#setResourceBuilder

    Parameters
    ----------

    builder : Optional[QResourceBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::setResourceBuilder(QResourceBuilder
    #      *builder)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder18setResourceBuilderEP16QResourceBu'
        'ilder',
        self._addressOf(builder),
    )

  @overload(QTextBuilder)
  @overload(NoneType)
  def setTextBuilder(self, builder: Optional[QTextBuilder]) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::setTextBuilder(QTextBuilder
    *builder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#setTextBuilder

    Parameters
    ----------

    builder : Optional[QTextBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::setTextBuilder(QTextBuilder *builder)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder14setTextBuilderEP12QTextBuilder',
        self._addressOf(builder),
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
    'QAbstractFormBuilder::QAbstractFormBuilder()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#QAbstractFormBuilder
    """
    #  QAbstractFormBuilder::QAbstractFormBuilder()
    self._noteCreation(QAbstractFormBuilder, lambda: Rituals.call(
        'ritual_ZN20QAbstractFormBuilderC1Ev',
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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QWidget)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def load(
      self,
      dev: Optional[QIODevice],
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
    *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#load

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractFormBuilder::load(QIODevice *dev, QWidget
    #      *parentWidget)
    ritual = 'ritual_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder4loadEP9QIODeviceP7QWidget')
    address = self.uglySide.call(
        ritual, self._addressOf(dev), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QIODevice, QWidget)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def save(
      self,
      dev: Optional[QIODevice],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::save(QIODevice *dev, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#save

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::save(QIODevice *dev, QWidget *widget)
    ritual = 'ritual_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder4saveEP9QIODeviceP7QWidget')
    self.uglySide.call(ritual, self._addressOf(dev), self._addressOf(widget))

  @overload(DomWidget, QWidget, QWidget)
  @overload(DomWidget, QWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QWidget, QWidget)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadExtraInfo(DomWidget
    *ui_widget, QWidget *widget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadExtraInfo

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
    #  void QAbstractFormBuilder::loadExtraInfo(DomWidget *ui_widget, QWidget
    #      *widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7QWidge'
        'tS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder13loadExtraInfoEP9DomWidgetP7'
          'QWidgetS3_')
    self.uglySide.call(
        ritual,
        self._addressOf(ui_widget), self._addressOf(widget),
        self._addressOf(parentWidget),
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
    Calls Qt's 'QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget
    *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QWidget *QAbstractFormBuilder::create(DomUI *ui, QWidget
    #      *parentWidget)
    ritual = 'ritual_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder6createEP5DomUIP7QWidget'
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
    Calls Qt's 'QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget,
    QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QWidget *QAbstractFormBuilder::create(DomWidget *ui_widget, QWidget
    #      *parentWidget)
    ritual = 'ritual_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder6createEP9DomWidgetP7QWidget')
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
    Calls Qt's 'QLayout *QAbstractFormBuilder::create(DomLayout *ui_layout,
    QLayout *layout, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QLayout *QAbstractFormBuilder::create(DomLayout *ui_layout, QLayout
    #      *layout, QWidget *parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP7QWidg'
        'et')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder6createEP9DomLayoutP7QLayoutP'
          '7QWidget')
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
    Calls Qt's 'QLayoutItem *QAbstractFormBuilder::create(DomLayoutItem
    *ui_layoutItem, QLayout *layout, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QLayoutItem *QAbstractFormBuilder::create(DomLayoutItem
    #      *ui_layoutItem, QLayout *layout, QWidget *parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLayoutP7'
        'QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder6createEP13DomLayoutItemP7QLa'
          'youtP7QWidget')
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
    Calls Qt's 'QAction *QAbstractFormBuilder::create(DomAction *ui_action,
    QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QAction *QAbstractFormBuilder::create(DomAction *ui_action, QObject
    #      *parent)
    ritual = 'ritual_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder6createEP9DomActionP7QObject')
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
    Calls Qt's 'QActionGroup *QAbstractFormBuilder::create(DomActionGroup
    *ui_action_group, QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#create

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
    #  QActionGroup *QAbstractFormBuilder::create(DomActionGroup
    #      *ui_action_group, QObject *parent)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder6createEP14DomActionGroupP7QO'
          'bject')
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_action_group), self._addressOf(parent, 'QObject'),
    )
    from ..QtGui import QActionGroup
    return QActionGroup._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def addMenuAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::addMenuAction(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#addMenuAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::addMenuAction(QAction *action)
    ritual = 'ritual_ZN20QAbstractFormBuilder13addMenuActionEP7QAction'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder13addMenuActionEP7QAction'
    self.uglySide.call(ritual, self._addressOf(action))

  @overload(QObject, QList[DomProperty])
  @overload(NoneType, QList[DomProperty])
  def applyProperties(
      self,
      o: Optional[QObject],
      properties: QList[DomProperty],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::applyProperties(QObject *o, const
    QList<DomProperty *> &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#applyProperties

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
    #  void QAbstractFormBuilder::applyProperties(QObject *o, const
    #      QList<DomProperty *> &properties)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder15applyPropertiesEP7QObjectRK5QList'
        'IP11DomPropertyE',
        self._addressOf(o, 'QObject'), self._valueOf(properties),
    )

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def applyPropertyInternally(
      self,
      o: Optional[QObject],
      propertyName: str,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractFormBuilder::applyPropertyInternally(QObject
    *o, const QString &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#applyPropertyInternally

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QAbstractFormBuilder::applyPropertyInternally(QObject *o, const
    #      QString &propertyName, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder23applyPropertyInternallyEP7QObject'
        'RK7QStringRK8QVariant',
        self._addressOf(o, 'QObject'), propertyName, self._valueOf(value),
    )

  @overload(QWidget, DomTabStops)
  @overload(QWidget, NoneType)
  @overload(NoneType, DomTabStops)
  @overload(NoneType, NoneType)
  def applyTabStops(
      self,
      widget: Optional[QWidget],
      tabStops: Optional[DomTabStops],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::applyTabStops(QWidget *widget,
    DomTabStops *tabStops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#applyTabStops

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tabStops : Optional[DomTabStops]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::applyTabStops(QWidget *widget, DomTabStops
    #      *tabStops)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11DomTabS'
        'tops')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder13applyTabStopsEP7QWidgetP11D'
          'omTabStops')
    self.uglySide.call(
        ritual, self._addressOf(widget), self._addressOf(tabStops),
    )

  @overload(str, QWidget, str)
  @overload(str, NoneType, str)
  def createWidget(
      self,
      widgetName: str,
      parentWidget: Optional[QWidget],
      name: str,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractFormBuilder::createWidget(const QString
    &widgetName, QWidget *parentWidget, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createWidget

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
    #  QWidget *QAbstractFormBuilder::createWidget(const QString &widgetName,
    #      QWidget *parentWidget, const QString &name)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QWidgetS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder12createWidgetERK7QStringP7QW'
          'idgetS2_')
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
    Calls Qt's 'QLayout *QAbstractFormBuilder::createLayout(const QString
    &layoutName, QObject *parent, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createLayout

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
    #  QLayout *QAbstractFormBuilder::createLayout(const QString &layoutName,
    #      QObject *parent, const QString &name)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QObjectS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder12createLayoutERK7QStringP7QO'
          'bjectS2_')
    address = self.uglySide.call(
        ritual, layoutName, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def createAction(
      self,
      parent: Optional[QObject],
      name: str,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QAbstractFormBuilder::createAction(QObject *parent,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QAbstractFormBuilder::createAction(QObject *parent, const
    #      QString &name)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder12createActionEP7QObjectRK7QS'
          'tring')
    address = self.uglySide.call(
        ritual, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def createActionGroup(
      self,
      parent: Optional[QObject],
      name: str,
  ) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup *QAbstractFormBuilder::createActionGroup(QObject
    *parent, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createActionGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup *QAbstractFormBuilder::createActionGroup(QObject *parent,
    #      const QString &name)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder17createActionGroupEP7QObjectRK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder17createActionGroupEP7QObject'
          'RK7QString')
    address = self.uglySide.call(
        ritual, self._addressOf(parent, 'QObject'), name,
    )
    from ..QtGui import QActionGroup
    return QActionGroup._cuteAt(address)

  @overload(DomCustomWidgets)
  @overload(NoneType)
  def createCustomWidgets(self, a0: Optional[DomCustomWidgets]) -> None:
    """
    Calls Qt's 'void
    QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createCustomWidgets

    Parameters
    ----------

    a0 : Optional[DomCustomWidgets]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::createCustomWidgets(DomCustomWidgets *a0)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomCustomW'
        'idgets')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder19createCustomWidgetsEP16DomC'
          'ustomWidgets')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(DomConnections, QWidget)
  @overload(DomConnections, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createConnections(
      self,
      a0: Optional[DomConnections],
      a1: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::createConnections(DomConnections
    *a0, QWidget *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createConnections

    Parameters
    ----------

    a0 : Optional[DomConnections]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::createConnections(DomConnections *a0,
    #      QWidget *a1)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder17createConnectionsEP14DomConnectio'
        'nsP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder17createConnectionsEP14DomCon'
          'nectionsP7QWidget')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(DomResources)
  @overload(NoneType)
  def createResources(self, a0: Optional[DomResources]) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::createResources(DomResources
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createResources

    Parameters
    ----------

    a0 : Optional[DomResources]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::createResources(DomResources *a0)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder15createResourcesEP12DomResources')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder15createResourcesEP12DomResou'
          'rces')
    self.uglySide.call(ritual, self._addressOf(a0))

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
    Calls Qt's 'bool QAbstractFormBuilder::addItem(DomLayoutItem *ui_item,
    QLayoutItem *item, QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#addItem

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
    #  bool QAbstractFormBuilder::addItem(DomLayoutItem *ui_item, QLayoutItem
    #      *item, QLayout *layout)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11QLayout'
        'ItemP7QLayout')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder7addItemEP13DomLayoutItemP11Q'
          'LayoutItemP7QLayout')
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
    Calls Qt's 'bool QAbstractFormBuilder::addItem(DomWidget *ui_widget,
    QWidget *widget, QWidget *parentWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#addItem

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
    #  bool QAbstractFormBuilder::addItem(DomWidget *ui_widget, QWidget
    #      *widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidgetS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder7addItemEP9DomWidgetP7QWidget'
          'S3_')
    return self.uglySide.call(
        ritual,
        self._addressOf(ui_widget), self._addressOf(widget),
        self._addressOf(parentWidget),
    )

  @overload(QWidget, DomWidget, DomWidget)
  @overload(QWidget, DomWidget, NoneType)
  @overload(QWidget, NoneType, DomWidget)
  @overload(QWidget, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveExtraInfo(
      self,
      widget: Optional[QWidget],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::saveExtraInfo(QWidget *widget,
    DomWidget *ui_widget, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveExtraInfo

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveExtraInfo(QWidget *widget, DomWidget
    #      *ui_widget, DomWidget *ui_parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9DomWidge'
        'tS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder13saveExtraInfoEP7QWidgetP9Do'
          'mWidgetS3_')
    self.uglySide.call(
        ritual,
        self._addressOf(widget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def saveDom(self, ui: Optional[DomUI], widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#saveDom

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveDom(DomUI *ui, QWidget *widget)
    ritual = 'ritual_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder7saveDomEP5DomUIP7QWidget'
    self.uglySide.call(ritual, self._addressOf(ui), self._addressOf(widget))

  @overload(QAction)
  @overload(NoneType)
  def createActionRefDom(
      self,
      action: Optional[QAction],
  ) -> Optional[DomActionRef]:
    """
    Calls Qt's 'DomActionRef
    *QAbstractFormBuilder::createActionRefDom(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createActionRefDom

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomActionRef]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomActionRef *QAbstractFormBuilder::createActionRefDom(QAction
    #      *action)
    ritual = 'ritual_ZN20QAbstractFormBuilder18createActionRefDomEP7QAction'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder18createActionRefDomEP7QActio'
          'n')
    address = self.uglySide.call(ritual, self._addressOf(action))
    from . import DomActionRef
    return DomActionRef._cuteAt(address)

  @overload(QWidget, DomWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, DomWidget)
  @overload(NoneType, NoneType)
  @overload(QWidget, DomWidget, bool)
  @overload(QWidget, NoneType, bool)
  @overload(NoneType, DomWidget, bool)
  @overload(NoneType, NoneType, bool)
  def createDom(
      self,
      widget: Optional[QWidget],
      ui_parentWidget: Optional[DomWidget],
      recursive: bool = True,
  ) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget *QAbstractFormBuilder::createDom(QWidget *widget,
    DomWidget *ui_parentWidget, bool recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recursive : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *QAbstractFormBuilder::createDom(QWidget *widget, DomWidget
    #      *ui_parentWidget, bool recursive)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidgetb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder9createDomEP7QWidgetP9DomWidg'
          'etb')
    address = self.uglySide.call(
        ritual,
        self._addressOf(widget), self._addressOf(ui_parentWidget), recursive,
    )
    from . import DomWidget
    return DomWidget._cuteAt(address)

  @overload(QLayout, DomLayout, DomWidget)
  @overload(QLayout, DomLayout, NoneType)
  @overload(QLayout, NoneType, DomWidget)
  @overload(QLayout, NoneType, NoneType)
  @overload(NoneType, DomLayout, DomWidget)
  @overload(NoneType, DomLayout, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def createDom(
      self,
      layout: Optional[QLayout],
      ui_layout: Optional[DomLayout],
      ui_parentWidget: Optional[DomWidget],
  ) -> Optional[DomLayout]:
    """
    Calls Qt's 'DomLayout *QAbstractFormBuilder::createDom(QLayout *layout,
    DomLayout *ui_layout, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_layout : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayout *QAbstractFormBuilder::createDom(QLayout *layout, DomLayout
    #      *ui_layout, DomWidget *ui_parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayoutP9Do'
        'mWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder9createDomEP7QLayoutP9DomLayo'
          'utP9DomWidget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(layout), self._addressOf(ui_layout),
        self._addressOf(ui_parentWidget),
    )
    from . import DomLayout
    return DomLayout._cuteAt(address)

  @overload(QSpacerItem, DomLayout, DomWidget)
  @overload(QSpacerItem, DomLayout, NoneType)
  @overload(QSpacerItem, NoneType, DomWidget)
  @overload(QSpacerItem, NoneType, NoneType)
  def createDom(
      self,
      spacer: Optional[QSpacerItem],
      ui_parentLayout: Optional[DomLayout],
      ui_parentWidget: Optional[DomWidget],
  ) -> Optional[DomSpacer]:
    """
    Calls Qt's 'DomSpacer *QAbstractFormBuilder::createDom(QSpacerItem
    *spacer, DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    spacer : Optional[QSpacerItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentLayout : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomSpacer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSpacer *QAbstractFormBuilder::createDom(QSpacerItem *spacer,
    #      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9DomLayou'
        'tP9DomWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder9createDomEP11QSpacerItemP9Do'
          'mLayoutP9DomWidget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(spacer), self._addressOf(ui_parentLayout),
        self._addressOf(ui_parentWidget),
    )
    from . import DomSpacer
    return DomSpacer._cuteAt(address)

  @overload(QLayoutItem, DomLayout, DomWidget)
  @overload(QLayoutItem, DomLayout, NoneType)
  @overload(QLayoutItem, NoneType, DomWidget)
  @overload(QLayoutItem, NoneType, NoneType)
  def createDom(
      self,
      item: Optional[QLayoutItem],
      ui_parentLayout: Optional[DomLayout],
      ui_parentWidget: Optional[DomWidget],
  ) -> Optional[DomLayoutItem]:
    """
    Calls Qt's 'DomLayoutItem *QAbstractFormBuilder::createDom(QLayoutItem
    *item, DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentLayout : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayoutItem *QAbstractFormBuilder::createDom(QLayoutItem *item,
    #      DomLayout *ui_parentLayout, DomWidget *ui_parentWidget)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9DomLayou'
        'tP9DomWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder9createDomEP11QLayoutItemP9Do'
          'mLayoutP9DomWidget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(item, 'QLayoutItem'),
        self._addressOf(ui_parentLayout), self._addressOf(ui_parentWidget),
    )
    from . import DomLayoutItem
    return DomLayoutItem._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def createDom(self, action: Optional[QAction]) -> Optional[DomAction]:
    """
    Calls Qt's 'DomAction *QAbstractFormBuilder::createDom(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomAction *QAbstractFormBuilder::createDom(QAction *action)
    ritual = 'ritual_ZN20QAbstractFormBuilder9createDomEP7QAction'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder9createDomEP7QAction'
    address = self.uglySide.call(ritual, self._addressOf(action))
    from . import DomAction
    return DomAction._cuteAt(address)

  @overload(QActionGroup)
  def createDom(
      self,
      actionGroup: Optional[QActionGroup],
  ) -> Optional[DomActionGroup]:
    """
    Calls Qt's 'DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
    *actionGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    actionGroup : Optional[QActionGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomActionGroup *QAbstractFormBuilder::createDom(QActionGroup
    #      *actionGroup)
    ritual = 'ritual_ZN20QAbstractFormBuilder9createDomEP12QActionGroup'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder9createDomEP12QActionGroup')
    address = self.uglySide.call(ritual, self._addressOf(actionGroup))
    from . import DomActionGroup
    return DomActionGroup._cuteAt(address)

  @overload(QButtonGroup)
  def createDom(
      self,
      buttonGroup: Optional[QButtonGroup],
  ) -> Optional[DomButtonGroup]:
    """
    Calls Qt's 'DomButtonGroup *QAbstractFormBuilder::createDom(QButtonGroup
    *buttonGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createDom

    Parameters
    ----------

    buttonGroup : Optional[QButtonGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomButtonGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomButtonGroup *QAbstractFormBuilder::createDom(QButtonGroup
    #      *buttonGroup)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder9createDomEP12QButtonGroup',
        self._addressOf(buttonGroup),
    )
    from . import DomButtonGroup
    return DomButtonGroup._cuteAt(address)

  def saveConnections(self) -> Optional[DomConnections]:
    """
    Calls Qt's 'DomConnections *QAbstractFormBuilder::saveConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveConnections

    Returns
    -------

    Optional[DomConnections]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomConnections *QAbstractFormBuilder::saveConnections()
    ritual = 'ritual_ZN20QAbstractFormBuilder15saveConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder15saveConnectionsEv'
    address = self.uglySide.call(ritual)
    from . import DomConnections
    return DomConnections._cuteAt(address)

  def saveCustomWidgets(self) -> Optional[DomCustomWidgets]:
    """
    Calls Qt's 'DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveCustomWidgets

    Returns
    -------

    Optional[DomCustomWidgets]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomCustomWidgets *QAbstractFormBuilder::saveCustomWidgets()
    ritual = 'ritual_ZN20QAbstractFormBuilder17saveCustomWidgetsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder17saveCustomWidgetsEv'
    address = self.uglySide.call(ritual)
    from . import DomCustomWidgets
    return DomCustomWidgets._cuteAt(address)

  def saveTabStops(self) -> Optional[DomTabStops]:
    """
    Calls Qt's 'DomTabStops *QAbstractFormBuilder::saveTabStops()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveTabStops

    Returns
    -------

    Optional[DomTabStops]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomTabStops *QAbstractFormBuilder::saveTabStops()
    ritual = 'ritual_ZN20QAbstractFormBuilder12saveTabStopsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder12saveTabStopsEv'
    address = self.uglySide.call(ritual)
    from . import DomTabStops
    return DomTabStops._cuteAt(address)

  def saveResources(self) -> Optional[DomResources]:
    """
    Calls Qt's 'DomResources *QAbstractFormBuilder::saveResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveResources

    Returns
    -------

    Optional[DomResources]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResources *QAbstractFormBuilder::saveResources()
    ritual = 'ritual_ZN20QAbstractFormBuilder13saveResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAbstractFormBuilder13saveResourcesEv'
    address = self.uglySide.call(ritual)
    from . import DomResources
    return DomResources._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def saveButtonGroups(
      self,
      mainContainer: Optional[QWidget],
  ) -> Optional[DomButtonGroups]:
    """
    Calls Qt's 'DomButtonGroups *QAbstractFormBuilder::saveButtonGroups(const
    QWidget *mainContainer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveButtonGroups

    Parameters
    ----------

    mainContainer : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomButtonGroups]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomButtonGroups *QAbstractFormBuilder::saveButtonGroups(const QWidget
    #      *mainContainer)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder16saveButtonGroupsEPK7QWidget',
        self._addressOf(mainContainer),
    )
    from . import DomButtonGroups
    return DomButtonGroups._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def computeProperties(self, obj: Optional[QObject]) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *>
    QAbstractFormBuilder::computeProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#computeProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> QAbstractFormBuilder::computeProperties(QObject
    #      *obj)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder17computePropertiesEP7QObject',
        self._addressOf(obj, 'QObject'),
    )
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def createProperty(
      self,
      object: Optional[QObject],
      propertyName: str,
      value: QVariant,
  ) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QAbstractFormBuilder::createProperty(QObject
    *object, const QString &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#createProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QAbstractFormBuilder::createProperty(QObject *object,
    #      const QString &propertyName, const QVariant &value)
    ritual = (
        'ritual_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7QStrin'
        'gRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAbstractFormBuilder14createPropertyEP7QObjectRK7'
          'QStringRK8QVariant')
    address = self.uglySide.call(
        ritual,
        self._addressOf(object, 'QObject'), propertyName,
        self._valueOf(value),
    )
    from . import DomProperty
    return DomProperty._cuteAt(address)

  @overload(DomWidget, QListWidget, QWidget)
  @overload(DomWidget, QListWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QListWidget, QWidget)
  @overload(NoneType, QListWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadListWidgetExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      listWidget: Optional[QListWidget],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadListWidgetExtraInfo(DomWidget
    *ui_widget, QListWidget *listWidget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadListWidgetExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    listWidget : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadListWidgetExtraInfo(DomWidget
    #      *ui_widget, QListWidget *listWidget, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder23loadListWidgetExtraInfoEP9DomWidg'
        'etP11QListWidgetP7QWidget',
        self._addressOf(ui_widget), self._addressOf(listWidget),
        self._addressOf(parentWidget),
    )

  @overload(DomWidget, QTreeWidget, QWidget)
  @overload(DomWidget, QTreeWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QTreeWidget, QWidget)
  @overload(NoneType, QTreeWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadTreeWidgetExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      treeWidget: Optional[QTreeWidget],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadTreeWidgetExtraInfo(DomWidget
    *ui_widget, QTreeWidget *treeWidget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadTreeWidgetExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    treeWidget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadTreeWidgetExtraInfo(DomWidget
    #      *ui_widget, QTreeWidget *treeWidget, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder23loadTreeWidgetExtraInfoEP9DomWidg'
        'etP11QTreeWidgetP7QWidget',
        self._addressOf(ui_widget), self._addressOf(treeWidget),
        self._addressOf(parentWidget),
    )

  @overload(DomWidget, QTableWidget, QWidget)
  @overload(DomWidget, QTableWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QTableWidget, QWidget)
  @overload(NoneType, QTableWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadTableWidgetExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      tableWidget: Optional[QTableWidget],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadTableWidgetExtraInfo(DomWidget
    *ui_widget, QTableWidget *tableWidget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadTableWidgetExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tableWidget : Optional[QTableWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadTableWidgetExtraInfo(DomWidget
    #      *ui_widget, QTableWidget *tableWidget, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder24loadTableWidgetExtraInfoEP9DomWid'
        'getP12QTableWidgetP7QWidget',
        self._addressOf(ui_widget), self._addressOf(tableWidget),
        self._addressOf(parentWidget),
    )

  @overload(DomWidget, QComboBox, QWidget)
  @overload(DomWidget, QComboBox, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QComboBox, QWidget)
  @overload(NoneType, QComboBox, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadComboBoxExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      comboBox: Optional[QComboBox],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadComboBoxExtraInfo(DomWidget
    *ui_widget, QComboBox *comboBox, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadComboBoxExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    comboBox : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadComboBoxExtraInfo(DomWidget *ui_widget,
    #      QComboBox *comboBox, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder21loadComboBoxExtraInfoEP9DomWidget'
        'P9QComboBoxP7QWidget',
        self._addressOf(ui_widget), self._addressOf(comboBox),
        self._addressOf(parentWidget),
    )

  @overload(DomWidget, QAbstractButton, QWidget)
  @overload(DomWidget, QAbstractButton, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QAbstractButton, QWidget)
  @overload(NoneType, QAbstractButton, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadButtonExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      button: Optional[QAbstractButton],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadButtonExtraInfo(const
    DomWidget *ui_widget, QAbstractButton *button, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadButtonExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadButtonExtraInfo(const DomWidget
    #      *ui_widget, QAbstractButton *button, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder19loadButtonExtraInfoEPK9DomWidgetP'
        '15QAbstractButtonP7QWidget',
        self._addressOf(ui_widget), self._addressOf(button),
        self._addressOf(parentWidget),
    )

  @overload(DomWidget, QAbstractItemView, QWidget)
  @overload(DomWidget, QAbstractItemView, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QAbstractItemView, QWidget)
  @overload(NoneType, QAbstractItemView, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadItemViewExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      itemView: Optional[QAbstractItemView],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::loadItemViewExtraInfo(DomWidget
    *ui_widget, QAbstractItemView *itemView, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#loadItemViewExtraInfo

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    itemView : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::loadItemViewExtraInfo(DomWidget *ui_widget,
    #      QAbstractItemView *itemView, QWidget *parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder21loadItemViewExtraInfoEP9DomWidget'
        'P17QAbstractItemViewP7QWidget',
        self._addressOf(ui_widget), self._addressOf(itemView),
        self._addressOf(parentWidget),
    )

  @overload(QListWidget, DomWidget, DomWidget)
  @overload(QListWidget, DomWidget, NoneType)
  @overload(QListWidget, NoneType, DomWidget)
  @overload(QListWidget, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveListWidgetExtraInfo(
      self,
      widget: Optional[QListWidget],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractFormBuilder::saveListWidgetExtraInfo(QListWidget *widget,
    DomWidget *ui_widget, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveListWidgetExtraInfo

    Parameters
    ----------

    widget : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveListWidgetExtraInfo(QListWidget
    #      *widget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder23saveListWidgetExtraInfoEP11QListW'
        'idgetP9DomWidgetS3_',
        self._addressOf(widget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QTreeWidget, DomWidget, DomWidget)
  @overload(QTreeWidget, DomWidget, NoneType)
  @overload(QTreeWidget, NoneType, DomWidget)
  @overload(QTreeWidget, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveTreeWidgetExtraInfo(
      self,
      treeWidget: Optional[QTreeWidget],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractFormBuilder::saveTreeWidgetExtraInfo(QTreeWidget *treeWidget,
    DomWidget *ui_widget, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveTreeWidgetExtraInfo

    Parameters
    ----------

    treeWidget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveTreeWidgetExtraInfo(QTreeWidget
    #      *treeWidget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder23saveTreeWidgetExtraInfoEP11QTreeW'
        'idgetP9DomWidgetS3_',
        self._addressOf(treeWidget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QTableWidget, DomWidget, DomWidget)
  @overload(QTableWidget, DomWidget, NoneType)
  @overload(QTableWidget, NoneType, DomWidget)
  @overload(QTableWidget, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveTableWidgetExtraInfo(
      self,
      tablWidget: Optional[QTableWidget],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractFormBuilder::saveTableWidgetExtraInfo(QTableWidget *tablWidget,
    DomWidget *ui_widget, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveTableWidgetExtraInfo

    Parameters
    ----------

    tablWidget : Optional[QTableWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveTableWidgetExtraInfo(QTableWidget
    #      *tablWidget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder24saveTableWidgetExtraInfoEP12QTabl'
        'eWidgetP9DomWidgetS3_',
        self._addressOf(tablWidget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QComboBox, DomWidget, DomWidget)
  @overload(QComboBox, DomWidget, NoneType)
  @overload(QComboBox, NoneType, DomWidget)
  @overload(QComboBox, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveComboBoxExtraInfo(
      self,
      widget: Optional[QComboBox],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::saveComboBoxExtraInfo(QComboBox
    *widget, DomWidget *ui_widget, DomWidget *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveComboBoxExtraInfo

    Parameters
    ----------

    widget : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveComboBoxExtraInfo(QComboBox *widget,
    #      DomWidget *ui_widget, DomWidget *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder21saveComboBoxExtraInfoEP9QComboBox'
        'P9DomWidgetS3_',
        self._addressOf(widget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QAbstractButton, DomWidget, DomWidget)
  @overload(QAbstractButton, DomWidget, NoneType)
  @overload(QAbstractButton, NoneType, DomWidget)
  @overload(QAbstractButton, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveButtonExtraInfo(
      self,
      widget: Optional[QAbstractButton],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::saveButtonExtraInfo(const
    QAbstractButton *widget, DomWidget *ui_widget, DomWidget
    *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveButtonExtraInfo

    Parameters
    ----------

    widget : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveButtonExtraInfo(const QAbstractButton
    #      *widget, DomWidget *ui_widget, DomWidget *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder19saveButtonExtraInfoEPK15QAbstract'
        'ButtonP9DomWidgetS4_',
        self._addressOf(widget), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QAbstractItemView, DomWidget, DomWidget)
  @overload(QAbstractItemView, DomWidget, NoneType)
  @overload(QAbstractItemView, NoneType, DomWidget)
  @overload(QAbstractItemView, NoneType, NoneType)
  @overload(NoneType, DomWidget, DomWidget)
  @overload(NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, DomWidget)
  @overload(NoneType, NoneType, NoneType)
  def saveItemViewExtraInfo(
      self,
      itemView: Optional[QAbstractItemView],
      ui_widget: Optional[DomWidget],
      ui_parentWidget: Optional[DomWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::saveItemViewExtraInfo(const
    QAbstractItemView *itemView, DomWidget *ui_widget, DomWidget
    *ui_parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveItemViewExtraInfo

    Parameters
    ----------

    itemView : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::saveItemViewExtraInfo(const
    #      QAbstractItemView *itemView, DomWidget *ui_widget, DomWidget
    #      *ui_parentWidget)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder21saveItemViewExtraInfoEPK17QAbstra'
        'ctItemViewP9DomWidgetS4_',
        self._addressOf(itemView), self._addressOf(ui_widget),
        self._addressOf(ui_parentWidget),
    )

  @overload(QMetaObject, DomProperty)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, DomProperty)
  @overload(NoneType, NoneType)
  def toVariant(
      self,
      meta: Optional[QMetaObject],
      property: Optional[DomProperty],
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractFormBuilder::toVariant(const QMetaObject
    *meta, DomProperty *property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#toVariant

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractFormBuilder::toVariant(const QMetaObject *meta,
    #      DomProperty *property)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder9toVariantEPK11QMetaObjectP11DomPro'
        'perty',
        self._addressOf(meta, 'QMetaObject'), self._addressOf(property),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPalette)
  def saveColorGroup(self, palette: QPalette) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *QAbstractFormBuilder::saveColorGroup(const
    QPalette &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveColorGroup

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *QAbstractFormBuilder::saveColorGroup(const QPalette
    #      &palette)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder14saveColorGroupERK8QPalette',
        self._valueOf(palette),
    )
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  @overload(DomBrush)
  @overload(NoneType)
  def setupBrush(self, brush: Optional[DomBrush]) -> QBrush:
    """
    Calls Qt's 'QBrush QAbstractFormBuilder::setupBrush(DomBrush *brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#setupBrush

    Parameters
    ----------

    brush : Optional[DomBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAbstractFormBuilder::setupBrush(DomBrush *brush)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder10setupBrushEP8DomBrush',
        self._addressOf(brush),
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(QBrush)
  def saveBrush(self, brush: QBrush) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *QAbstractFormBuilder::saveBrush(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#saveBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *QAbstractFormBuilder::saveBrush(const QBrush &brush)
    address = self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder9saveBrushERK6QBrush',
        self._valueOf(brush),
    )
    from . import DomBrush
    return DomBrush._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractformbuilder.html#reset
    """
    #  void QAbstractFormBuilder::reset()
    self.uglySide.call('ritual_ZN20QAbstractFormBuilder5resetEv')

  @overload(DomUI)
  @overload(NoneType)
  def initialize(self, ui: Optional[DomUI]) -> None:
    """
    Calls Qt's 'void QAbstractFormBuilder::initialize(const DomUI *ui)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuilder.html#initialize

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractFormBuilder::initialize(const DomUI *ui)
    self.uglySide.call(
        'ritual_ZN20QAbstractFormBuilder10initializeEPK5DomUI',
        self._addressOf(ui),
    )

  @staticmethod
  def layoutInfo(*__, **_) -> Never:
    """
    Qt's 'void QAbstractFormBuilder::layoutInfo(DomLayout *layout, QObject
    *parent, int *margin, int *spacing)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QAbstractFormBuilder.layoutInfo' has no cute function yet. Qt's "
        "'void QAbstractFormBuilder::layoutInfo(DomLayout *layout, QObject "
        "*parent, int *margin, int *spacing)': takes a number to change "
        "where it is.")

  @staticmethod
  def setIconProperty(*__, **_) -> Never:
    """
    Qt's 'void QAbstractFormBuilder::setIconProperty(DomProperty &a0, const
    IconPaths &a1) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFormBuilder.setIconProperty' has no cute function yet. "
        "Qt's 'void QAbstractFormBuilder::setIconProperty(DomProperty &a0, "
        "const IconPaths &a1) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setPixmapProperty(*__, **_) -> Never:
    """
    Qt's 'void QAbstractFormBuilder::setPixmapProperty(DomProperty &a0, const
    IconPaths &a1) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFormBuilder.setPixmapProperty' has no cute function yet. "
        "Qt's 'void QAbstractFormBuilder::setPixmapProperty(DomProperty "
        "&a0, const IconPaths &a1) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setupColorGroup(*__, **_) -> Never:
    """
    Qt's 'void QAbstractFormBuilder::setupColorGroup(QPalette &palette,
    QPalette::ColorGroup colorGroup, DomColorGroup *group)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFormBuilder.setupColorGroup' has no cute function yet. "
        "Qt's 'void QAbstractFormBuilder::setupColorGroup(QPalette "
        "&palette, QPalette::ColorGroup colorGroup, DomColorGroup *group)': "
        "takes a type Python has no way to hand over yet.")
