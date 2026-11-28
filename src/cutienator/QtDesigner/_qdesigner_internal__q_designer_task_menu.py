"""
qdesigner_internal::QDesignerTaskMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_taskmenu_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerTaskMenu to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QDesignerTaskMenuExtension

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerTaskMenu(QObject, QDesignerTaskMenuExtension):
  """
  The cute side of Qt's qdesigner_internal::QDesignerTaskMenu: a plain Python
  object standing in front of one C++ qdesigner_internal::QDesignerTaskMenu.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::QDesignerTaskMenu is built on Qt's QObject, and has
  everything that class has. It is built on the cute
  'QDesignerTaskMenuExtension' as well, as Qt's
  qdesigner_internal::QDesignerTaskMenu is built on Qt's
  QDesignerTaskMenuExtension too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerTaskMenu that has a
  ritual and that Python can call so far, 24 names in all: 'metaObject',
  'tr', 'widget', 'taskActions', 'isSlotNavigationEnabled', 'navigateToSlot',
  'formWindow', 'changeTextProperty', 'createSeparator', 'applicableObjects',
  'applicableWidgets', 'setProperty', 'changeObjectName', 'changeToolTip',
  'changeWhatsThis', 'changeStyleSheet', 'createMenuBar', 'addToolBar',
  'createStatusBar', 'removeStatusBar', 'containerFakeMethods',
  'slotNavigateToSlot', 'applySize', 'slotLayoutAlignment'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::QDesignerTaskMenu::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerTaskMenu::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::QDesignerTaskMenu::~QDesignerTaskMenu()': the
    destructor: Python never removes a C++
    qdesigner_internal::QDesignerTaskMenu.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerTaskMenu is created at the first
    use, not by 'qdesigner_internal::QDesignerTaskMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerTaskMenu.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerTaskMenu. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::QDesignerTaskMenu, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class PropertyMode(CuteNum):
    """
    The enum 'qdesigner_internal::QDesignerTaskMenu::PropertyMode' of Qt,
    with the 2 names Qt gives in it.
    """

    CurrentWidgetMode = Kee[int](0)
    MultiSelectionMode = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::QDesignerTaskMenu::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html#tr

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
    #  QString qdesigner_internal::QDesignerTaskMenu::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def isSlotNavigationEnabled(
      core: Optional[QDesignerFormEditorInterface],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerTaskMenu::isSlotNavigationEnabled(const
    QDesignerFormEditorInterface *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerTaskMenu::isSlotNavigationEnabled(
    #      const QDesignerFormEditorInterface *core)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu23isSlotNavigation'
        'EnabledEPK28QDesignerFormEditorInterface',
        CuteMixin._addressOf(core),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QObject, str)
  @overload(QDesignerFormEditorInterface, NoneType, str)
  @overload(NoneType, QObject, str)
  @overload(NoneType, NoneType, str)
  def navigateToSlot(
      core: Optional[QDesignerFormEditorInterface],
      o: Optional[QObject],
      defaultSignal: str = '',
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerTaskMenu::navigateToSlot(
    QDesignerFormEditorInterface *core, QObject *o, const QString
    &defaultSignal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    defaultSignal : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void qdesigner_internal::QDesignerTaskMenu::navigateToSlot(
    #      QDesignerFormEditorInterface *core, QObject *o, const QString
    #      &defaultSignal)
    Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu14navigateToSlotEP'
        '28QDesignerFormEditorInterfaceP7QObjectRK7QString',
        CuteMixin._addressOf(core), CuteMixin._addressOf(o, 'QObject'),
        defaultSignal,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerTaskMenu'

  #  Qt's qdesigner_internal::QDesignerTaskMenu is built on more than one
  #  class. The part of a C++ qdesigner_internal::QDesignerTaskMenu that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDesignerTaskMenuExtension':
          'ritual_cast_qdesigner_internal_QDesignerTaskMenu_QDesignerTaskMenuExtension',
  }

  #  A C++ qdesigner_internal::QDesignerTaskMenu Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QDesignerTaskMenu'

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
    *qdesigner_internal::QDesignerTaskMenu::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::QDesignerTaskMenu::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::QDesignerTaskMenu::widget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerTaskMenu::widget() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu6widgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def taskActions(self) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *>
    qdesigner_internal::QDesignerTaskMenu::taskActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *> qdesigner_internal::QDesignerTaskMenu::taskActions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu11taskActionsEv',
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::QDesignerTaskMenu::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::QDesignerTaskMenu::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  @overload(QDesignerFormWindowInterface, PropertyMode)
  @overload(NoneType, PropertyMode)
  def applicableObjects(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      pm: PropertyMode,
  ) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList
    qdesigner_internal::QDesignerTaskMenu::applicableObjects(const
    QDesignerFormWindowInterface *fw, PropertyMode pm) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pm : PropertyMode
      Passed on as its number.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList
    #      qdesigner_internal::QDesignerTaskMenu::applicableObjects(const
    #      QDesignerFormWindowInterface *fw, PropertyMode pm) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu17applicableObjec'
        'tsEPK28QDesignerFormWindowInterfaceNS0_12PropertyModeE',
        self._addressOf(fw), pm.value,
    )
    return QList[QObject]._cuteOwning(address)

  @overload(QDesignerFormWindowInterface, PropertyMode)
  @overload(NoneType, PropertyMode)
  def applicableWidgets(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      pm: PropertyMode,
  ) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::QDesignerTaskMenu::applicableWidgets(const
    QDesignerFormWindowInterface *fw, PropertyMode pm) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pm : PropertyMode
      Passed on as its number.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList
    #      qdesigner_internal::QDesignerTaskMenu::applicableWidgets(const
    #      QDesignerFormWindowInterface *fw, PropertyMode pm) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerTaskMenu17applicableWidge'
        'tsEPK28QDesignerFormWindowInterfaceNS0_12PropertyModeE',
        self._addressOf(fw), pm.value,
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormWindowInterface, PropertyMode, str, QVariant)
  @overload(NoneType, PropertyMode, str, QVariant)
  def setProperty(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      pm: PropertyMode,
      name: str,
      newValue: QVariant,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerTaskMenu::setProperty(
    QDesignerFormWindowInterface *fw, PropertyMode pm, const QString &name,
    const QVariant &newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pm : PropertyMode
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    newValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerTaskMenu::setProperty(
    #      QDesignerFormWindowInterface *fw, PropertyMode pm, const QString
    #      &name, const QVariant &newValue)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu11setPropertyEP28Q'
        'DesignerFormWindowInterfaceNS0_12PropertyModeERK7QStringRK8QVarian'
        't',
        self._addressOf(fw), pm.value, name, self._valueOf(newValue),
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

  @overload(QWidget, QObject)
  @overload(QWidget, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      widget: Optional[QWidget],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerTaskMenu::QDesignerTaskMenu(QWidget
    *widget, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QDesignerTaskMenu::QDesignerTaskMenu(QWidget
    #      *widget, QObject *parent)
    self._noteCreation(QDesignerTaskMenu, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenuC1EP7QWidgetP7QObj'
        'ect',
        self._addressOf(widget), self._addressOf(parent, 'QObject'),
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

  @overload(str, str, PropertyMode, Qt.TextFormat)
  def changeTextProperty(
      self,
      propertyName: str,
      windowTitle: str,
      pm: PropertyMode,
      desiredFormat: Qt.TextFormat,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::changeTextProperty(const QString
    &propertyName, const QString &windowTitle, PropertyMode pm,
    Qt::TextFormat desiredFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    windowTitle : str
      Passed on as it is: a QString is made of it for the call.

    pm : PropertyMode
      Passed on as its number.

    desiredFormat : Qt.TextFormat
      Passed on as its number.
    """
    #  void qdesigner_internal::QDesignerTaskMenu::changeTextProperty(const
    #      QString &propertyName, const QString &windowTitle, PropertyMode
    #      pm, Qt::TextFormat desiredFormat)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu18changeTextProper'
        'tyERK7QStringS3_NS0_12PropertyModeEN2Qt10TextFormatE',
        propertyName, windowTitle, pm.value, desiredFormat.value,
    )

  def createSeparator(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *qdesigner_internal::QDesignerTaskMenu::createSeparator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::QDesignerTaskMenu::createSeparator()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu15createSeparatorE'
        'v',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def changeObjectName(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::changeObjectName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::changeObjectName()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu16changeObjectName'
        'Ev',
    )

  def changeToolTip(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerTaskMenu::changeToolTip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::changeToolTip()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu13changeToolTipEv',
    )

  def changeWhatsThis(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::changeWhatsThis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::changeWhatsThis()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu15changeWhatsThisE'
        'v',
    )

  def changeStyleSheet(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::changeStyleSheet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::changeStyleSheet()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu16changeStyleSheet'
        'Ev',
    )

  def createMenuBar(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerTaskMenu::createMenuBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::createMenuBar()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu13createMenuBarEv',
    )

  @overload(Qt.ToolBarArea)
  def addToolBar(self, area: Qt.ToolBarArea) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::addToolBar(Qt::ToolBarArea area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    area : Qt.ToolBarArea
      Passed on as its number.
    """
    #  void qdesigner_internal::QDesignerTaskMenu::addToolBar(Qt::ToolBarArea
    #      area)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu10addToolBarEN2Qt1'
        '1ToolBarAreaE',
        area.value,
    )

  def createStatusBar(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::createStatusBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::createStatusBar()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu15createStatusBarE'
        'v',
    )

  def removeStatusBar(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::removeStatusBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::removeStatusBar()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu15removeStatusBarE'
        'v',
    )

  def containerFakeMethods(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::containerFakeMethods()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::containerFakeMethods()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu20containerFakeMet'
        'hodsEv',
    )

  def slotNavigateToSlot(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::slotNavigateToSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::slotNavigateToSlot()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu18slotNavigateToSl'
        'otEv',
    )

  @overload(QAction)
  @overload(NoneType)
  def applySize(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerTaskMenu::applySize(QAction
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerTaskMenu::applySize(QAction *a)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu9applySizeEP7QActi'
        'on',
        self._addressOf(a),
    )

  def slotLayoutAlignment(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerTaskMenu::slotLayoutAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignertaskmenu.html
    """
    #  void qdesigner_internal::QDesignerTaskMenu::slotLayoutAlignment()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17QDesignerTaskMenu19slotLayoutAlignm'
        'entEv',
    )
