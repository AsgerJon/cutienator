"""
QDesignerFormEditorInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformeditor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QIcon
  from ..QtWidgets import QWidget
  from . import QDesignerActionEditorInterface, QDesignerDialogGuiInterface
  from . import QDesignerFormWindowManagerInterface
  from . import QDesignerIntegrationInterface
  from . import QDesignerIntrospectionInterface
  from . import QDesignerMetaDataBaseInterface
  from . import QDesignerObjectInspectorInterface
  from . import QDesignerOptionsPageInterface, QDesignerPluginManager
  from . import QDesignerPromotionInterface, QDesignerPropertyEditorInterface
  from . import QDesignerSettingsInterface, QDesignerWidgetBoxInterface
  from . import QDesignerWidgetDataBaseInterface
  from . import QDesignerWidgetFactoryInterface, QExtensionManager
  from . import QtResourceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerActionEditorInterface = WAIT['QDesignerActionEditorInterface']
  QDesignerDialogGuiInterface = WAIT['QDesignerDialogGuiInterface']
  QDesignerFormWindowManagerInterface = WAIT['QDesignerFormWindowManagerInterface']
  QDesignerIntegrationInterface = WAIT['QDesignerIntegrationInterface']
  QDesignerIntrospectionInterface = WAIT['QDesignerIntrospectionInterface']
  QDesignerMetaDataBaseInterface = WAIT['QDesignerMetaDataBaseInterface']
  QDesignerObjectInspectorInterface = WAIT['QDesignerObjectInspectorInterface']
  QDesignerOptionsPageInterface = WAIT['QDesignerOptionsPageInterface']
  QDesignerPluginManager = WAIT['QDesignerPluginManager']
  QDesignerPromotionInterface = WAIT['QDesignerPromotionInterface']
  QDesignerPropertyEditorInterface = WAIT['QDesignerPropertyEditorInterface']
  QDesignerSettingsInterface = WAIT['QDesignerSettingsInterface']
  QDesignerWidgetBoxInterface = WAIT['QDesignerWidgetBoxInterface']
  QDesignerWidgetDataBaseInterface = WAIT['QDesignerWidgetDataBaseInterface']
  QDesignerWidgetFactoryInterface = WAIT['QDesignerWidgetFactoryInterface']
  QExtensionManager = WAIT['QExtensionManager']
  QWidget = WAIT['QWidget']
  QtResourceModel = WAIT['QtResourceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormEditorInterface(QObject):
  """
  The cute side of Qt's QDesignerFormEditorInterface: a plain Python object
  standing in front of one C++ QDesignerFormEditorInterface.

  It is built on the cute 'QObject', as Qt's QDesignerFormEditorInterface is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerFormEditorInterface that has a ritual and
  that Python can call so far, 41 names in all: 'metaObject', 'tr',
  'extensionManager', 'topLevel', 'widgetBox', 'propertyEditor',
  'objectInspector', 'formWindowManager', 'widgetDataBase', 'metaDataBase',
  'promotion', 'widgetFactory', 'actionEditor', 'integration',
  'pluginManager', 'introspection', 'dialogGui', 'settingsManager',
  'resourceLocation', 'resourceModel', 'optionsPages', 'setTopLevel',
  'setWidgetBox', 'setPropertyEditor', 'setObjectInspector',
  'setPluginManager', 'setActionEditor', 'setIntegration',
  'setIntrospection', 'setDialogGui', 'setSettingsManager',
  'setResourceModel', 'setOptionsPages', 'pluginInstances', 'createIcon',
  'setFormManager', 'setMetaDataBase', 'setWidgetDataBase', 'setPromotion',
  'setWidgetFactory', 'setExtensionManager'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerFormEditorInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerFormEditorInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerFormEditorInterface::~QDesignerFormEditorInterface()': the
    destructor: Python never removes a C++ QDesignerFormEditorInterface.
  - Qt's 'QtGradientManager *QDesignerFormEditorInterface::gradientManager()
    const': gives 'QtGradientManager', which has no cute class yet.
  - Qt's 'void
    QDesignerFormEditorInterface::setGradientManager(QtGradientManager
    *manager)': names 'QtGradientManager', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 49 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerFormEditorInterface is created at the first use, not by
    'QDesignerFormEditorInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormEditorInterface.
  - Qt tells when it has removed the C++ QDesignerFormEditorInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerFormEditorInterface that has no cute function
    yet, 'gradientManager', 'setGradientManager', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QDesignerFormEditorInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#tr

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
    #  QString QDesignerFormEditorInterface::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QDesignerFormEditorInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def createIcon(name: str) -> QIcon:
    """
    Calls Qt's 'QIcon QDesignerFormEditorInterface::createIcon(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#createIcon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QDesignerFormEditorInterface::createIcon(const QString &name)
    address = Rituals.call(
        'ritual_ZN28QDesignerFormEditorInterface10createIconERK7QString',
        name,
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormEditorInterface'

  #  A C++ QDesignerFormEditorInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormEditorInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerFormEditorInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerFormEditorInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def extensionManager(self) -> Optional[QExtensionManager]:
    """
    Calls Qt's 'QExtensionManager
    *QDesignerFormEditorInterface::extensionManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#extensionManager

    Returns
    -------

    Optional[QExtensionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QExtensionManager *QDesignerFormEditorInterface::extensionManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface16extensionManagerEv',
    )
    from . import QExtensionManager
    return QExtensionManager._cuteAt(address)

  def topLevel(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormEditorInterface::topLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#topLevel

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormEditorInterface::topLevel() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface8topLevelEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def widgetBox(self) -> Optional[QDesignerWidgetBoxInterface]:
    """
    Calls Qt's 'QDesignerWidgetBoxInterface
    *QDesignerFormEditorInterface::widgetBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#widgetBox

    Returns
    -------

    Optional[QDesignerWidgetBoxInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerWidgetBoxInterface *QDesignerFormEditorInterface::widgetBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface9widgetBoxEv',
    )
    from . import QDesignerWidgetBoxInterface
    return QDesignerWidgetBoxInterface._cuteAt(address)

  def propertyEditor(self) -> Optional[QDesignerPropertyEditorInterface]:
    """
    Calls Qt's 'QDesignerPropertyEditorInterface
    *QDesignerFormEditorInterface::propertyEditor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#propertyEditor

    Returns
    -------

    Optional[QDesignerPropertyEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerPropertyEditorInterface
    #      *QDesignerFormEditorInterface::propertyEditor() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface14propertyEditorEv',
    )
    from . import QDesignerPropertyEditorInterface
    return QDesignerPropertyEditorInterface._cuteAt(address)

  def objectInspector(self) -> Optional[QDesignerObjectInspectorInterface]:
    """
    Calls Qt's 'QDesignerObjectInspectorInterface
    *QDesignerFormEditorInterface::objectInspector() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#objectInspector

    Returns
    -------

    Optional[QDesignerObjectInspectorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerObjectInspectorInterface
    #      *QDesignerFormEditorInterface::objectInspector() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface15objectInspectorEv',
    )
    from . import QDesignerObjectInspectorInterface
    return QDesignerObjectInspectorInterface._cuteAt(address)

  def formWindowManager(
      self,
  ) -> Optional[QDesignerFormWindowManagerInterface]:
    """
    Calls Qt's 'QDesignerFormWindowManagerInterface
    *QDesignerFormEditorInterface::formWindowManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Returns
    -------

    Optional[QDesignerFormWindowManagerInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowManagerInterface
    #      *QDesignerFormEditorInterface::formWindowManager() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface17formWindowManagerEv',
    )
    from . import QDesignerFormWindowManagerInterface
    return QDesignerFormWindowManagerInterface._cuteAt(address)

  def widgetDataBase(self) -> Optional[QDesignerWidgetDataBaseInterface]:
    """
    Calls Qt's 'QDesignerWidgetDataBaseInterface
    *QDesignerFormEditorInterface::widgetDataBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#widgetDataBase

    Returns
    -------

    Optional[QDesignerWidgetDataBaseInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerWidgetDataBaseInterface
    #      *QDesignerFormEditorInterface::widgetDataBase() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface14widgetDataBaseEv',
    )
    from . import QDesignerWidgetDataBaseInterface
    return QDesignerWidgetDataBaseInterface._cuteAt(address)

  def metaDataBase(self) -> Optional[QDesignerMetaDataBaseInterface]:
    """
    Calls Qt's 'QDesignerMetaDataBaseInterface
    *QDesignerFormEditorInterface::metaDataBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#metaDataBase

    Returns
    -------

    Optional[QDesignerMetaDataBaseInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMetaDataBaseInterface
    #      *QDesignerFormEditorInterface::metaDataBase() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface12metaDataBaseEv',
    )
    from . import QDesignerMetaDataBaseInterface
    return QDesignerMetaDataBaseInterface._cuteAt(address)

  def promotion(self) -> Optional[QDesignerPromotionInterface]:
    """
    Calls Qt's 'QDesignerPromotionInterface
    *QDesignerFormEditorInterface::promotion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#promotion

    Returns
    -------

    Optional[QDesignerPromotionInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerPromotionInterface *QDesignerFormEditorInterface::promotion()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface9promotionEv',
    )
    from . import QDesignerPromotionInterface
    return QDesignerPromotionInterface._cuteAt(address)

  def widgetFactory(self) -> Optional[QDesignerWidgetFactoryInterface]:
    """
    Calls Qt's 'QDesignerWidgetFactoryInterface
    *QDesignerFormEditorInterface::widgetFactory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#widgetFactory

    Returns
    -------

    Optional[QDesignerWidgetFactoryInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerWidgetFactoryInterface
    #      *QDesignerFormEditorInterface::widgetFactory() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface13widgetFactoryEv',
    )
    from . import QDesignerWidgetFactoryInterface
    return QDesignerWidgetFactoryInterface._cuteAt(address)

  def actionEditor(self) -> Optional[QDesignerActionEditorInterface]:
    """
    Calls Qt's 'QDesignerActionEditorInterface
    *QDesignerFormEditorInterface::actionEditor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#actionEditor

    Returns
    -------

    Optional[QDesignerActionEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerActionEditorInterface
    #      *QDesignerFormEditorInterface::actionEditor() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface12actionEditorEv',
    )
    from . import QDesignerActionEditorInterface
    return QDesignerActionEditorInterface._cuteAt(address)

  def integration(self) -> Optional[QDesignerIntegrationInterface]:
    """
    Calls Qt's 'QDesignerIntegrationInterface
    *QDesignerFormEditorInterface::integration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#integration

    Returns
    -------

    Optional[QDesignerIntegrationInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerIntegrationInterface
    #      *QDesignerFormEditorInterface::integration() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface11integrationEv',
    )
    from . import QDesignerIntegrationInterface
    return QDesignerIntegrationInterface._cuteAt(address)

  def pluginManager(self) -> Optional[QDesignerPluginManager]:
    """
    Calls Qt's 'QDesignerPluginManager
    *QDesignerFormEditorInterface::pluginManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#pluginManager

    Returns
    -------

    Optional[QDesignerPluginManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerPluginManager *QDesignerFormEditorInterface::pluginManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface13pluginManagerEv',
    )
    from . import QDesignerPluginManager
    return QDesignerPluginManager._cuteAt(address)

  def introspection(self) -> Optional[QDesignerIntrospectionInterface]:
    """
    Calls Qt's 'QDesignerIntrospectionInterface
    *QDesignerFormEditorInterface::introspection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#introspection

    Returns
    -------

    Optional[QDesignerIntrospectionInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerIntrospectionInterface
    #      *QDesignerFormEditorInterface::introspection() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface13introspectionEv',
    )
    from . import QDesignerIntrospectionInterface
    return QDesignerIntrospectionInterface._cuteAt(address)

  def dialogGui(self) -> Optional[QDesignerDialogGuiInterface]:
    """
    Calls Qt's 'QDesignerDialogGuiInterface
    *QDesignerFormEditorInterface::dialogGui() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#dialogGui

    Returns
    -------

    Optional[QDesignerDialogGuiInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerDialogGuiInterface *QDesignerFormEditorInterface::dialogGui()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface9dialogGuiEv',
    )
    from . import QDesignerDialogGuiInterface
    return QDesignerDialogGuiInterface._cuteAt(address)

  def settingsManager(self) -> Optional[QDesignerSettingsInterface]:
    """
    Calls Qt's 'QDesignerSettingsInterface
    *QDesignerFormEditorInterface::settingsManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#settingsManager

    Returns
    -------

    Optional[QDesignerSettingsInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerSettingsInterface
    #      *QDesignerFormEditorInterface::settingsManager() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface15settingsManagerEv',
    )
    from . import QDesignerSettingsInterface
    return QDesignerSettingsInterface._cuteAt(address)

  def resourceLocation(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormEditorInterface::resourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#resourceLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormEditorInterface::resourceLocation() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface16resourceLocationEv',
    )

  def resourceModel(self) -> Optional[QtResourceModel]:
    """
    Calls Qt's 'QtResourceModel
    *QDesignerFormEditorInterface::resourceModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#resourceModel

    Returns
    -------

    Optional[QtResourceModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceModel *QDesignerFormEditorInterface::resourceModel() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface13resourceModelEv',
    )
    from . import QtResourceModel
    return QtResourceModel._cuteAt(address)

  def optionsPages(self) -> QList[QDesignerOptionsPageInterface]:
    """
    Calls Qt's 'QList<QDesignerOptionsPageInterface *>
    QDesignerFormEditorInterface::optionsPages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#optionsPages

    Returns
    -------

    QList[QDesignerOptionsPageInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDesignerOptionsPageInterface *>
    #      QDesignerFormEditorInterface::optionsPages() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface12optionsPagesEv',
    )
    from . import QDesignerOptionsPageInterface
    return QList[QDesignerOptionsPageInterface]._cuteOwning(address)

  def pluginInstances(self) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList QDesignerFormEditorInterface::pluginInstances()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#pluginInstances

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList QDesignerFormEditorInterface::pluginInstances() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormEditorInterface15pluginInstancesEv',
    )
    return QList[QObject]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setTopLevel(self, topLevel: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setTopLevel(QWidget
    *topLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setTopLevel

    Parameters
    ----------

    topLevel : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setTopLevel(QWidget *topLevel)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface11setTopLevelEP7QWidget',
        self._addressOf(topLevel),
    )

  @overload(QDesignerWidgetBoxInterface)
  @overload(NoneType)
  def setWidgetBox(
      self,
      widgetBox: Optional[QDesignerWidgetBoxInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setWidgetBox(QDesignerWidgetBoxInterface
    *widgetBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setWidgetBox

    Parameters
    ----------

    widgetBox : Optional[QDesignerWidgetBoxInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setWidgetBox(
    #      QDesignerWidgetBoxInterface *widgetBox)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface12setWidgetBoxEP27QDesigner'
        'WidgetBoxInterface',
        self._addressOf(widgetBox),
    )

  @overload(QDesignerPropertyEditorInterface)
  @overload(NoneType)
  def setPropertyEditor(
      self,
      propertyEditor: Optional[QDesignerPropertyEditorInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setPropertyEditor(
    QDesignerPropertyEditorInterface *propertyEditor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    propertyEditor : Optional[QDesignerPropertyEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setPropertyEditor(
    #      QDesignerPropertyEditorInterface *propertyEditor)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface17setPropertyEditorEP32QDes'
        'ignerPropertyEditorInterface',
        self._addressOf(propertyEditor),
    )

  @overload(QDesignerObjectInspectorInterface)
  @overload(NoneType)
  def setObjectInspector(
      self,
      objectInspector: Optional[QDesignerObjectInspectorInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setObjectInspector(
    QDesignerObjectInspectorInterface *objectInspector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    objectInspector : Optional[QDesignerObjectInspectorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setObjectInspector(
    #      QDesignerObjectInspectorInterface *objectInspector)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface18setObjectInspectorEP33QDe'
        'signerObjectInspectorInterface',
        self._addressOf(objectInspector),
    )

  @overload(QDesignerPluginManager)
  @overload(NoneType)
  def setPluginManager(
      self,
      pluginManager: Optional[QDesignerPluginManager],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setPluginManager(QDesignerPluginManager
    *pluginManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setPluginManager

    Parameters
    ----------

    pluginManager : Optional[QDesignerPluginManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setPluginManager(
    #      QDesignerPluginManager *pluginManager)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface16setPluginManagerEP22QDesi'
        'gnerPluginManager',
        self._addressOf(pluginManager),
    )

  @overload(QDesignerActionEditorInterface)
  @overload(NoneType)
  def setActionEditor(
      self,
      actionEditor: Optional[QDesignerActionEditorInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setActionEditor(
    QDesignerActionEditorInterface *actionEditor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setActionEditor

    Parameters
    ----------

    actionEditor : Optional[QDesignerActionEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setActionEditor(
    #      QDesignerActionEditorInterface *actionEditor)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface15setActionEditorEP30QDesig'
        'nerActionEditorInterface',
        self._addressOf(actionEditor),
    )

  @overload(QDesignerIntegrationInterface)
  @overload(NoneType)
  def setIntegration(
      self,
      integration: Optional[QDesignerIntegrationInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setIntegration(
    QDesignerIntegrationInterface *integration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setIntegration

    Parameters
    ----------

    integration : Optional[QDesignerIntegrationInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setIntegration(
    #      QDesignerIntegrationInterface *integration)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface14setIntegrationEP29QDesign'
        'erIntegrationInterface',
        self._addressOf(integration),
    )

  @overload(QDesignerIntrospectionInterface)
  @overload(NoneType)
  def setIntrospection(
      self,
      introspection: Optional[QDesignerIntrospectionInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setIntrospection(
    QDesignerIntrospectionInterface *introspection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setIntrospection

    Parameters
    ----------

    introspection : Optional[QDesignerIntrospectionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setIntrospection(
    #      QDesignerIntrospectionInterface *introspection)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface16setIntrospectionEP31QDesi'
        'gnerIntrospectionInterface',
        self._addressOf(introspection),
    )

  @overload(QDesignerDialogGuiInterface)
  @overload(NoneType)
  def setDialogGui(
      self,
      dialogGui: Optional[QDesignerDialogGuiInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setDialogGui(QDesignerDialogGuiInterface
    *dialogGui)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setDialogGui

    Parameters
    ----------

    dialogGui : Optional[QDesignerDialogGuiInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setDialogGui(
    #      QDesignerDialogGuiInterface *dialogGui)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface12setDialogGuiEP27QDesigner'
        'DialogGuiInterface',
        self._addressOf(dialogGui),
    )

  @overload(QDesignerSettingsInterface)
  @overload(NoneType)
  def setSettingsManager(
      self,
      settingsManager: Optional[QDesignerSettingsInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setSettingsManager(
    QDesignerSettingsInterface *settingsManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    settingsManager : Optional[QDesignerSettingsInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setSettingsManager(
    #      QDesignerSettingsInterface *settingsManager)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface18setSettingsManagerEP26QDe'
        'signerSettingsInterface',
        self._addressOf(settingsManager),
    )

  @overload(QtResourceModel)
  @overload(NoneType)
  def setResourceModel(self, model: Optional[QtResourceModel]) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setResourceModel(QtResourceModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setResourceModel

    Parameters
    ----------

    model : Optional[QtResourceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setResourceModel(QtResourceModel
    #      *model)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface16setResourceModelEP15QtRes'
        'ourceModel',
        self._addressOf(model),
    )

  @overload(QList[QDesignerOptionsPageInterface])
  def setOptionsPages(
      self,
      optionsPages: QList[QDesignerOptionsPageInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setOptionsPages(const
    QList<QDesignerOptionsPageInterface *> &optionsPages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setOptionsPages

    Parameters
    ----------

    optionsPages : QList[QDesignerOptionsPageInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerFormEditorInterface::setOptionsPages(const
    #      QList<QDesignerOptionsPageInterface *> &optionsPages)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface15setOptionsPagesERK5QListI'
        'P29QDesignerOptionsPageInterfaceE',
        self._valueOf(optionsPages),
    )

  @overload(QDesignerFormWindowManagerInterface)
  @overload(NoneType)
  def setFormManager(
      self,
      formWindowManager: Optional[QDesignerFormWindowManagerInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setFormManager(
    QDesignerFormWindowManagerInterface *formWindowManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setFormManager

    Parameters
    ----------

    formWindowManager : Optional[QDesignerFormWindowManagerInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setFormManager(
    #      QDesignerFormWindowManagerInterface *formWindowManager)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface14setFormManagerEP35QDesign'
        'erFormWindowManagerInterface',
        self._addressOf(formWindowManager),
    )

  @overload(QDesignerMetaDataBaseInterface)
  @overload(NoneType)
  def setMetaDataBase(
      self,
      metaDataBase: Optional[QDesignerMetaDataBaseInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setMetaDataBase(
    QDesignerMetaDataBaseInterface *metaDataBase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setMetaDataBase

    Parameters
    ----------

    metaDataBase : Optional[QDesignerMetaDataBaseInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setMetaDataBase(
    #      QDesignerMetaDataBaseInterface *metaDataBase)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface15setMetaDataBaseEP30QDesig'
        'nerMetaDataBaseInterface',
        self._addressOf(metaDataBase),
    )

  @overload(QDesignerWidgetDataBaseInterface)
  @overload(NoneType)
  def setWidgetDataBase(
      self,
      widgetDataBase: Optional[QDesignerWidgetDataBaseInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setWidgetDataBase(
    QDesignerWidgetDataBaseInterface *widgetDataBase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    widgetDataBase : Optional[QDesignerWidgetDataBaseInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setWidgetDataBase(
    #      QDesignerWidgetDataBaseInterface *widgetDataBase)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface17setWidgetDataBaseEP32QDes'
        'ignerWidgetDataBaseInterface',
        self._addressOf(widgetDataBase),
    )

  @overload(QDesignerPromotionInterface)
  @overload(NoneType)
  def setPromotion(
      self,
      promotion: Optional[QDesignerPromotionInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setPromotion(QDesignerPromotionInterface
    *promotion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setPromotion

    Parameters
    ----------

    promotion : Optional[QDesignerPromotionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setPromotion(
    #      QDesignerPromotionInterface *promotion)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface12setPromotionEP27QDesigner'
        'PromotionInterface',
        self._addressOf(promotion),
    )

  @overload(QDesignerWidgetFactoryInterface)
  @overload(NoneType)
  def setWidgetFactory(
      self,
      widgetFactory: Optional[QDesignerWidgetFactoryInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorInterface::setWidgetFactory(
    QDesignerWidgetFactoryInterface *widgetFactory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html#setWidgetFactory

    Parameters
    ----------

    widgetFactory : Optional[QDesignerWidgetFactoryInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setWidgetFactory(
    #      QDesignerWidgetFactoryInterface *widgetFactory)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface16setWidgetFactoryEP31QDesi'
        'gnerWidgetFactoryInterface',
        self._addressOf(widgetFactory),
    )

  @overload(QExtensionManager)
  @overload(NoneType)
  def setExtensionManager(
      self,
      extensionManager: Optional[QExtensionManager],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormEditorInterface::setExtensionManager(QExtensionManager
    *extensionManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    extensionManager : Optional[QExtensionManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorInterface::setExtensionManager(
    #      QExtensionManager *extensionManager)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormEditorInterface19setExtensionManagerEP17QE'
        'xtensionManager',
        self._addressOf(extensionManager),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerFormEditorInterface::QDesignerFormEditorInterface(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorinterface.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerFormEditorInterface::QDesignerFormEditorInterface(QObject
    #      *parent)
    self._noteCreation(QDesignerFormEditorInterface, lambda: Rituals.call(
        'ritual_ZN28QDesignerFormEditorInterfaceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @staticmethod
  def gradientManager(*__, **_) -> Never:
    """
    Qt's 'QtGradientManager *QDesignerFormEditorInterface::gradientManager()
    const': gives 'QtGradientManager', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDesignerFormEditorInterface.gradientManager' has no cute "
        "function yet. Qt's 'QtGradientManager "
        "*QDesignerFormEditorInterface::gradientManager() const': gives "
        "'QtGradientManager', which has no cute class yet.")

  @staticmethod
  def setGradientManager(*__, **_) -> Never:
    """
    Qt's 'void
    QDesignerFormEditorInterface::setGradientManager(QtGradientManager
    *manager)': names 'QtGradientManager', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDesignerFormEditorInterface.setGradientManager' has no cute "
        "function yet. Qt's 'void "
        "QDesignerFormEditorInterface::setGradientManager(QtGradientManager "
        "*manager)': names 'QtGradientManager', which has no cute class yet."
    )
