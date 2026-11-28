"""
qdesigner_internal::QSimpleResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QSimpleResource to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractFormBuilder, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtGui import QBrush
  from ..QtWidgets import QWidget
  from . import DomBrush, DomCustomWidget, DomCustomWidgets, DomWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomBrush = WAIT['DomBrush']
  DomCustomWidget = WAIT['DomCustomWidget']
  DomCustomWidgets = WAIT['DomCustomWidgets']
  DomWidget = WAIT['DomWidget']
  QBrush = WAIT['QBrush']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QObject = WAIT['QObject']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSimpleResource(QAbstractFormBuilder):
  """
  The cute side of Qt's qdesigner_internal::QSimpleResource: a plain Python
  object standing in front of one C++ qdesigner_internal::QSimpleResource.

  It is built on the cute 'QAbstractFormBuilder', as Qt's
  qdesigner_internal::QSimpleResource is built on Qt's QAbstractFormBuilder,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QSimpleResource that has a
  ritual and that Python can call so far, 9 names in all: 'setupBrush',
  'saveBrush', 'core', 'addExtensionDataToDOM', 'applyExtensionDataFromDOM',
  'customWidgetScript', 'hasCustomWidgetScript', 'handleDomCustomWidgets',
  'addFakeMethodsToWidgetDataBase'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::QSimpleResource::~QSimpleResource()': the
    destructor: Python never removes a C++
    qdesigner_internal::QSimpleResource.
  - Qt's 'bool qdesigner_internal::QSimpleResource::addFakeMethods(const
    DomSlots *domSlots, QStringList &fakeSlots, QStringList &fakeSignals)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    qdesigner_internal::QSimpleResource::addCustomWidgetsToWidgetDatabase(
    const QDesignerFormEditorInterface *core, QList<DomCustomWidget *>
    &custom_widget_list)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::QSimpleResource is created at the first use,
    not by 'qdesigner_internal::QSimpleResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QSimpleResource.
  - Each name of Qt's qdesigner_internal::QSimpleResource that has no cute
    function yet, 'addCustomWidgetsToWidgetDatabase', 'addFakeMethods', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, DomWidget, QWidget,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, DomWidget,
      NoneType,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, NoneType, QWidget,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, NoneType, NoneType,
  )
  @overload(QAbstractFormBuilder, NoneType, DomWidget, QWidget)
  @overload(QAbstractFormBuilder, NoneType, DomWidget, NoneType)
  @overload(QAbstractFormBuilder, NoneType, NoneType, QWidget)
  @overload(QAbstractFormBuilder, NoneType, NoneType, NoneType)
  @overload(NoneType, QDesignerFormEditorInterface, DomWidget, QWidget)
  @overload(NoneType, QDesignerFormEditorInterface, DomWidget, NoneType)
  @overload(NoneType, QDesignerFormEditorInterface, NoneType, QWidget)
  @overload(NoneType, QDesignerFormEditorInterface, NoneType, NoneType)
  @overload(NoneType, NoneType, DomWidget, QWidget)
  @overload(NoneType, NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def addExtensionDataToDOM(
      afb: Optional[QAbstractFormBuilder],
      core: Optional[QDesignerFormEditorInterface],
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QSimpleResource::addExtensionDataToDOM(
    QAbstractFormBuilder *afb, QDesignerFormEditorInterface *core, DomWidget
    *ui_widget, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    afb : Optional[QAbstractFormBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QSimpleResource::addExtensionDataToDOM(
    #      QAbstractFormBuilder *afb, QDesignerFormEditorInterface *core,
    #      DomWidget *ui_widget, QWidget *widget)
    Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource21addExtensionDataTo'
        'DOMEP20QAbstractFormBuilderP28QDesignerFormEditorInterfaceP9DomWid'
        'getP7QWidget',
        CuteMixin._addressOf(afb), CuteMixin._addressOf(core),
        CuteMixin._addressOf(ui_widget), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, DomWidget, QWidget,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, DomWidget,
      NoneType,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, NoneType, QWidget,
  )
  @overload(
      QAbstractFormBuilder, QDesignerFormEditorInterface, NoneType, NoneType,
  )
  @overload(QAbstractFormBuilder, NoneType, DomWidget, QWidget)
  @overload(QAbstractFormBuilder, NoneType, DomWidget, NoneType)
  @overload(QAbstractFormBuilder, NoneType, NoneType, QWidget)
  @overload(QAbstractFormBuilder, NoneType, NoneType, NoneType)
  @overload(NoneType, QDesignerFormEditorInterface, DomWidget, QWidget)
  @overload(NoneType, QDesignerFormEditorInterface, DomWidget, NoneType)
  @overload(NoneType, QDesignerFormEditorInterface, NoneType, QWidget)
  @overload(NoneType, QDesignerFormEditorInterface, NoneType, NoneType)
  @overload(NoneType, NoneType, DomWidget, QWidget)
  @overload(NoneType, NoneType, DomWidget, NoneType)
  @overload(NoneType, NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def applyExtensionDataFromDOM(
      afb: Optional[QAbstractFormBuilder],
      core: Optional[QDesignerFormEditorInterface],
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QSimpleResource::applyExtensionDataFromDOM(
    QAbstractFormBuilder *afb, QDesignerFormEditorInterface *core, DomWidget
    *ui_widget, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    afb : Optional[QAbstractFormBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QSimpleResource::applyExtensionDataFromDOM(
    #      QAbstractFormBuilder *afb, QDesignerFormEditorInterface *core,
    #      DomWidget *ui_widget, QWidget *widget)
    Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource25applyExtensionData'
        'FromDOMEP20QAbstractFormBuilderP28QDesignerFormEditorInterfaceP9Do'
        'mWidgetP7QWidget',
        CuteMixin._addressOf(afb), CuteMixin._addressOf(core),
        CuteMixin._addressOf(ui_widget), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def customWidgetScript(
      core: Optional[QDesignerFormEditorInterface],
      object: Optional[QObject],
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::QSimpleResource::customWidgetScript(
    QDesignerFormEditorInterface *core, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::QSimpleResource::customWidgetScript(
    #      QDesignerFormEditorInterface *core, QObject *object)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource18customWidgetScript'
        'EP28QDesignerFormEditorInterfaceP7QObject',
        CuteMixin._addressOf(core), CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, str)
  @overload(NoneType, str)
  def customWidgetScript(
      core: Optional[QDesignerFormEditorInterface],
      className: str,
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::QSimpleResource::customWidgetScript(
    QDesignerFormEditorInterface *core, const QString &className)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    className : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::QSimpleResource::customWidgetScript(
    #      QDesignerFormEditorInterface *core, const QString &className)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource18customWidgetScript'
        'EP28QDesignerFormEditorInterfaceRK7QString',
        CuteMixin._addressOf(core), className,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def hasCustomWidgetScript(
      core: Optional[QDesignerFormEditorInterface],
      object: Optional[QObject],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QSimpleResource::hasCustomWidgetScript(
    QDesignerFormEditorInterface *core, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QSimpleResource::hasCustomWidgetScript(
    #      QDesignerFormEditorInterface *core, QObject *object)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource21hasCustomWidgetScr'
        'iptEP28QDesignerFormEditorInterfaceP7QObject',
        CuteMixin._addressOf(core), CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, DomCustomWidgets)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, DomCustomWidgets)
  @overload(NoneType, NoneType)
  def handleDomCustomWidgets(
      core: Optional[QDesignerFormEditorInterface],
      dom_custom_widgets: Optional[DomCustomWidgets],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QSimpleResource::handleDomCustomWidgets(const
    QDesignerFormEditorInterface *core, const DomCustomWidgets
    *dom_custom_widgets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dom_custom_widgets : Optional[DomCustomWidgets]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QSimpleResource::handleDomCustomWidgets(const
    #      QDesignerFormEditorInterface *core, const DomCustomWidgets
    #      *dom_custom_widgets)
    Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource22handleDomCustomWid'
        'getsEPK28QDesignerFormEditorInterfacePK16DomCustomWidgets',
        CuteMixin._addressOf(core), CuteMixin._addressOf(dom_custom_widgets),
    )

  @staticmethod
  @overload(DomCustomWidget, WAIT['qdesigner_internal.WidgetDataBaseItem'])
  @overload(DomCustomWidget, NoneType)
  @overload(NoneType, WAIT['qdesigner_internal.WidgetDataBaseItem'])
  @overload(NoneType, NoneType)
  def addFakeMethodsToWidgetDataBase(
      domCustomWidget: Optional[DomCustomWidget],
      item: Optional[qdesigner_internal.WidgetDataBaseItem],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QSimpleResource::addFakeMethodsToWidgetDataBase(const
    DomCustomWidget *domCustomWidget, WidgetDataBaseItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    domCustomWidget : Optional[DomCustomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[qdesigner_internal.WidgetDataBaseItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QSimpleResource::
    #      addFakeMethodsToWidgetDataBase(const DomCustomWidget
    #      *domCustomWidget, WidgetDataBaseItem *item)
    Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource30addFakeMethodsToWi'
        'dgetDataBaseEPK15DomCustomWidgetPNS_18WidgetDataBaseItemE',
        CuteMixin._addressOf(domCustomWidget), CuteMixin._addressOf(item),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QSimpleResource'

  #  A C++ qdesigner_internal::QSimpleResource Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QSimpleResource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::QSimpleResource::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *qdesigner_internal::QSimpleResource::core() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15QSimpleResource4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def __init__(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QSimpleResource::QSimpleResource(
    QDesignerFormEditorInterface *core)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QSimpleResource::QSimpleResource(
    #      QDesignerFormEditorInterface *core)
    self._noteCreation(QSimpleResource, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal15QSimpleResourceC1EP28QDesignerFormE'
        'ditorInterface',
        self._addressOf(core),
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

  @overload(DomBrush)
  @overload(NoneType)
  def setupBrush(self, brush: Optional[DomBrush]) -> QBrush:
    """
    Calls Qt's 'QBrush
    qdesigner_internal::QSimpleResource::setupBrush(DomBrush *brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html#setupBrush

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
    #  QBrush qdesigner_internal::QSimpleResource::setupBrush(DomBrush
    #      *brush)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource10setupBrushEP8DomBr'
        'ush',
        self._addressOf(brush),
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(QBrush)
  def saveBrush(self, brush: QBrush) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush
    *qdesigner_internal::QSimpleResource::saveBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qsimpleresource.html#saveBrush

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
    #  DomBrush *qdesigner_internal::QSimpleResource::saveBrush(const QBrush
    #      &brush)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal15QSimpleResource9saveBrushERK6QBrush',
        self._valueOf(brush),
    )
    from . import DomBrush
    return DomBrush._cuteAt(address)

  @staticmethod
  def addCustomWidgetsToWidgetDatabase(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QSimpleResource::addCustomWidgetsToWidgetDatabase(
    const QDesignerFormEditorInterface *core, QList<DomCustomWidget *>
    &custom_widget_list)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QSimpleResource.addCustomWidgetsToWidgetDatabas"
        "e' has no cute function yet. Qt's 'void "
        "qdesigner_internal::QSimpleResource::addCustomWidgetsToWidgetDataba"
        "se(const QDesignerFormEditorInterface *core, QList<DomCustomWidget "
        "*> &custom_widget_list)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def addFakeMethods(*__, **_) -> Never:
    """
    Qt's 'bool qdesigner_internal::QSimpleResource::addFakeMethods(const
    DomSlots *domSlots, QStringList &fakeSlots, QStringList &fakeSignals)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QSimpleResource.addFakeMethods' has no cute "
        "function yet. Qt's 'bool "
        "qdesigner_internal::QSimpleResource::addFakeMethods(const DomSlots "
        "*domSlots, QStringList &fakeSlots, QStringList &fakeSignals)': "
        "takes a type Python has no way to hand over yet.")
