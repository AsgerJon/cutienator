"""
QDesignerComponents binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/qdesigner_components.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDesignerComponents(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerComponents: a plain Python object standing
  in front of one C++ QDesignerComponents.

  C++ hands a QDesignerComponents around as a copy, so every C++
  QDesignerComponents behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QDesignerComponents yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerComponents::~QDesignerComponents()': the destructor:
    Python removes its C++ QDesignerComponents by it, and has no other use
    for it.

  What has no ritual
  ------------------

  12 of the 13 functions Qt declares: 12 cannot be called and cannot be
  called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QDesignerComponents is created at the first use, not by
    'QDesignerComponents(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDesignerComponents back gives a copy the ritual made
    for Python, in a new cute QDesignerComponents.
  - Each name of Qt's QDesignerComponents that has no cute function yet,
    'createActionEditor', 'createFormEditor',
    'createFormEditorWithPluginPaths', 'createObjectInspector',
    'createPropertyEditor', 'createResourceEditor', 'createSignalSlotEditor',
    'createTaskMenu', 'createWidgetBox', 'defaultPluginPaths',
    'initializePlugins', 'initializeResources', holds a function that raises
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
  __qt_class__ = 'QDesignerComponents'

  #  Qt's '~QDesignerComponents()'. Naming it makes this a value class:
  #  Python owns every C++ QDesignerComponents behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDesignerComponentsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def createActionEditor(*__, **_) -> Never:
    """
    Qt's 'QDesignerActionEditorInterface
    *QDesignerComponents::createActionEditor(QDesignerFormEditorInterface
    *core, QWidget *parent)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createActionEditor' has no cute function yet. "
        "Qt's 'QDesignerActionEditorInterface "
        "*QDesignerComponents::createActionEditor(QDesignerFormEditorInterfa"
        "ce *core, QWidget *parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def createFormEditor(*__, **_) -> Never:
    """
    Qt's 'QDesignerFormEditorInterface
    *QDesignerComponents::createFormEditor(QObject *parent)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createFormEditor' has no cute function yet. "
        "Qt's 'QDesignerFormEditorInterface "
        "*QDesignerComponents::createFormEditor(QObject *parent)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def createFormEditorWithPluginPaths(*__, **_) -> Never:
    """
    Qt's 'QDesignerFormEditorInterface
    *QDesignerComponents::createFormEditorWithPluginPaths(const QStringList
    &pluginPaths, QObject *parent)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createFormEditorWithPluginPaths' has no cute "
        "function yet. Qt's 'QDesignerFormEditorInterface "
        "*QDesignerComponents::createFormEditorWithPluginPaths(const "
        "QStringList &pluginPaths, QObject *parent)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def createObjectInspector(*__, **_) -> Never:
    """
    Qt's 'QDesignerObjectInspectorInterface
    *QDesignerComponents::createObjectInspector(QDesignerFormEditorInterface
    *core, QWidget *parent)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createObjectInspector' has no cute function "
        "yet. Qt's 'QDesignerObjectInspectorInterface "
        "*QDesignerComponents::createObjectInspector(QDesignerFormEditorInte"
        "rface *core, QWidget *parent)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def createPropertyEditor(*__, **_) -> Never:
    """
    Qt's 'QDesignerPropertyEditorInterface
    *QDesignerComponents::createPropertyEditor(QDesignerFormEditorInterface
    *core, QWidget *parent)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createPropertyEditor' has no cute function "
        "yet. Qt's 'QDesignerPropertyEditorInterface "
        "*QDesignerComponents::createPropertyEditor(QDesignerFormEditorInter"
        "face *core, QWidget *parent)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def createResourceEditor(*__, **_) -> Never:
    """
    Qt's 'QWidget
    *QDesignerComponents::createResourceEditor(QDesignerFormEditorInterface
    *core, QWidget *parent)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createResourceEditor' has no cute function "
        "yet. Qt's 'QWidget "
        "*QDesignerComponents::createResourceEditor(QDesignerFormEditorInter"
        "face *core, QWidget *parent)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def createSignalSlotEditor(*__, **_) -> Never:
    """
    Qt's 'QWidget
    *QDesignerComponents::createSignalSlotEditor(QDesignerFormEditorInterface
    *core, QWidget *parent)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createSignalSlotEditor' has no cute function "
        "yet. Qt's 'QWidget "
        "*QDesignerComponents::createSignalSlotEditor(QDesignerFormEditorInt"
        "erface *core, QWidget *parent)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def createTaskMenu(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QDesignerComponents::createTaskMenu(QDesignerFormEditorInterface *core,
    QObject *parent)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createTaskMenu' has no cute function yet. "
        "Qt's 'QObject "
        "*QDesignerComponents::createTaskMenu(QDesignerFormEditorInterface "
        "*core, QObject *parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def createWidgetBox(*__, **_) -> Never:
    """
    Qt's 'QDesignerWidgetBoxInterface
    *QDesignerComponents::createWidgetBox(QDesignerFormEditorInterface *core,
    QWidget *parent)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.createWidgetBox' has no cute function yet. "
        "Qt's 'QDesignerWidgetBoxInterface "
        "*QDesignerComponents::createWidgetBox(QDesignerFormEditorInterface "
        "*core, QWidget *parent)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def defaultPluginPaths(*__, **_) -> Never:
    """
    Qt's 'QStringList QDesignerComponents::defaultPluginPaths()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.defaultPluginPaths' has no cute function yet. "
        "Qt's 'QStringList QDesignerComponents::defaultPluginPaths()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def initializePlugins(*__, **_) -> Never:
    """
    Qt's 'void
    QDesignerComponents::initializePlugins(QDesignerFormEditorInterface
    *core)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.initializePlugins' has no cute function yet. "
        "Qt's 'void "
        "QDesignerComponents::initializePlugins(QDesignerFormEditorInterface"
        " *core)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def initializeResources(*__, **_) -> Never:
    """
    Qt's 'void QDesignerComponents::initializeResources()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QDesignerComponents.initializeResources' has no cute function "
        "yet. Qt's 'void QDesignerComponents::initializeResources()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
