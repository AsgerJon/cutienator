"""
qdesigner_internal::WidgetFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/widgetfactory_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::WidgetFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerWidgetFactoryInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QLayout, QStyle, QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QLayout = WAIT['QLayout']
  QStyle = WAIT['QStyle']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class WidgetFactory(QDesignerWidgetFactoryInterface):
  """
  The cute side of Qt's qdesigner_internal::WidgetFactory: a plain Python
  object standing in front of one C++ qdesigner_internal::WidgetFactory.

  It is built on the cute 'QDesignerWidgetFactoryInterface', as Qt's
  qdesigner_internal::WidgetFactory is built on Qt's
  QDesignerWidgetFactoryInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::WidgetFactory that has a ritual
  and that Python can call so far, 26 names in all: 'metaObject', 'tr',
  'containerOfWidget', 'widgetOfContainer', 'createObject', 'createWidget',
  'createLayout', 'isPassiveInteractor', 'initialize', 'initializeCommon',
  'initializePreview', 'core', 'classNameOf', 'currentFormWindow',
  'createUnmanagedLayout', 'styleName', 'setStyleName', 'getStyle', 'style',
  'applyStyleTopLevel', 'applyStyleToTopLevel', 'isFormEditorObject',
  'loadPlugins', 'activeFormWindowChanged', 'formWindowAdded',
  'setFormWindowStyle'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::WidgetFactory::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::WidgetFactory::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::WidgetFactory::~WidgetFactory()': the
    destructor: Python never removes a C++ qdesigner_internal::WidgetFactory.
  - Qt's 'QWidget
    *qdesigner_internal::WidgetFactory::createCustomWidget(const QString
    &className, QWidget *parentWidget, bool *creationError) const': takes a
    number to change where it is.

  What has no ritual
  ------------------

  3 of the 34 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::WidgetFactory is created at the first use,
    not by 'qdesigner_internal::WidgetFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::WidgetFactory.
  - Qt tells when it has removed the C++ qdesigner_internal::WidgetFactory.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::WidgetFactory that has no cute
    function yet, 'createCustomWidget', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::WidgetFactory::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#tr

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
    #  QString qdesigner_internal::WidgetFactory::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def classNameOf(
      core: Optional[QDesignerFormEditorInterface],
      o: Optional[QObject],
  ) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetFactory::classNameOf(
    QDesignerFormEditorInterface *core, const QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#classNameOf

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetFactory::classNameOf(
    #      QDesignerFormEditorInterface *core, const QObject *o)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory11classNameOfEP28QDesi'
        'gnerFormEditorInterfacePK7QObject',
        CuteMixin._addressOf(core), CuteMixin._addressOf(o, 'QObject'),
    )

  @staticmethod
  @overload(QWidget, int)
  @overload(NoneType, int)
  def createUnmanagedLayout(
      parentWidget: Optional[QWidget],
      type: int,
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout
    *qdesigner_internal::WidgetFactory::createUnmanagedLayout(QWidget
    *parentWidget, int type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout
    #      *qdesigner_internal::WidgetFactory::createUnmanagedLayout(QWidget
    #      *parentWidget, int type)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory21createUnmanagedLayou'
        'tEP7QWidgeti',
        CuteMixin._addressOf(parentWidget), type,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @staticmethod
  @overload(QStyle, QWidget)
  @overload(QStyle, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def applyStyleToTopLevel(
      style: Optional[QStyle],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetFactory::applyStyleToTopLevel(QStyle *style,
    QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::applyStyleToTopLevel(QStyle
    #      *style, QWidget *widget)
    Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory20applyStyleToTopLevel'
        'EP6QStyleP7QWidget',
        CuteMixin._addressOf(style), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def isFormEditorObject(o: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::WidgetFactory::isFormEditorObject(const QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::WidgetFactory::isFormEditorObject(const
    #      QObject *o)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory18isFormEditorObjectEP'
        'K7QObject',
        CuteMixin._addressOf(o, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::WidgetFactory'

  #  A C++ qdesigner_internal::WidgetFactory Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_WidgetFactory'

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
    *qdesigner_internal::WidgetFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::WidgetFactory::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def containerOfWidget(
      self,
      widget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::WidgetFactory::containerOfWidget(QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::WidgetFactory::containerOfWidget(QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK18qdesigner_internal13WidgetFactory17containerOfWidgetEP'
        '7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13WidgetFactory17containerOfWi'
          'dgetEP7QWidget')
    address = self.uglySide.call(ritual, self._addressOf(widget))
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def widgetOfContainer(
      self,
      widget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::WidgetFactory::widgetOfContainer(QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::WidgetFactory::widgetOfContainer(QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK18qdesigner_internal13WidgetFactory17widgetOfContainerEP'
        '7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13WidgetFactory17widgetOfConta'
          'inerEP7QWidget')
    address = self.uglySide.call(ritual, self._addressOf(widget))
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str, QObject)
  @overload(str, NoneType)
  def createObject(
      self,
      className: str,
      parent: Optional[QObject],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *qdesigner_internal::WidgetFactory::createObject(const QString
    &className, QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#createObject

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *qdesigner_internal::WidgetFactory::createObject(const QString
    #      &className, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory12createObjectERK7QSt'
        'ringP7QObject',
        className, self._addressOf(parent, 'QObject'),
    )
    return QObject._cuteAt(address)

  @overload(str, QWidget)
  @overload(str, NoneType)
  def createWidget(
      self,
      className: str,
      parentWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::WidgetFactory::createWidget(const QString
    &className, QWidget *parentWidget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#createWidget

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::WidgetFactory::createWidget(const QString
    #      &className, QWidget *parentWidget) const
    ritual = (
        'ritual_ZNK18qdesigner_internal13WidgetFactory12createWidgetERK7QSt'
        'ringP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13WidgetFactory12createWidgetE'
          'RK7QStringP7QWidget')
    address = self.uglySide.call(
        ritual, className, self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget, QLayout, int)
  @overload(QWidget, NoneType, int)
  @overload(NoneType, QLayout, int)
  @overload(NoneType, NoneType, int)
  def createLayout(
      self,
      widget: Optional[QWidget],
      layout: Optional[QLayout],
      type: int,
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout
    *qdesigner_internal::WidgetFactory::createLayout(QWidget *widget, QLayout
    *layout, int type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#createLayout

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::WidgetFactory::createLayout(QWidget
    #      *widget, QLayout *layout, int type) const
    ritual = (
        'ritual_ZNK18qdesigner_internal13WidgetFactory12createLayoutEP7QWid'
        'getP7QLayouti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13WidgetFactory12createLayoutE'
          'P7QWidgetP7QLayouti')
    address = self.uglySide.call(
        ritual, self._addressOf(widget), self._addressOf(layout), type,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::WidgetFactory::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *qdesigner_internal::WidgetFactory::core() const
    ritual = 'ritual_ZNK18qdesigner_internal13WidgetFactory4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal13WidgetFactory4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def styleName(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::WidgetFactory::styleName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetFactory::styleName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory9styleNameEv',
    )

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *qdesigner_internal::WidgetFactory::style() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *qdesigner_internal::WidgetFactory::style() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory5styleEv',
    )
    from ..QtWidgets import QStyle
    return QStyle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStyleName(self, styleName: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetFactory::setStyleName(const
    QString &styleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#setStyleName

    Parameters
    ----------

    styleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::WidgetFactory::setStyleName(const QString
    #      &styleName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory12setStyleNameERK7QStr'
        'ing',
        styleName,
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setFormWindowStyle(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetFactory::setFormWindowStyle(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::setFormWindowStyle(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory18setFormWindowStyleEP'
        '28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::WidgetFactory::WidgetFactory(
    QDesignerFormEditorInterface *core, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::WidgetFactory::WidgetFactory(
    #      QDesignerFormEditorInterface *core, QObject *parent)
    self._noteCreation(WidgetFactory, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal13WidgetFactoryC1EP28QDesignerFormEdi'
        'torInterfaceP7QObject',
        self._addressOf(core), self._addressOf(parent, 'QObject'),
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

  @overload(QWidget)
  @overload(NoneType)
  def isPassiveInteractor(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::WidgetFactory::isPassiveInteractor(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::WidgetFactory::isPassiveInteractor(QWidget
    #      *widget)
    ritual = (
        'ritual_ZN18qdesigner_internal13WidgetFactory19isPassiveInteractorE'
        'P7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal13WidgetFactory19isPassiveInter'
          'actorEP7QWidget')
    return self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QObject)
  @overload(NoneType)
  def initialize(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetFactory::initialize(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#initialize

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::initialize(QObject *object)
    #      const
    ritual = (
        'ritual_ZNK18qdesigner_internal13WidgetFactory10initializeEP7QObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13WidgetFactory10initializeEP7'
          'QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

  @overload(QWidget)
  @overload(NoneType)
  def initializeCommon(self, object: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetFactory::initializeCommon(QWidget *object)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    object : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::initializeCommon(QWidget
    #      *object) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory16initializeCommonEP7'
        'QWidget',
        self._addressOf(object),
    )

  @overload(QWidget)
  @overload(NoneType)
  def initializePreview(self, object: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetFactory::initializePreview(QWidget *object)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    object : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::initializePreview(QWidget
    #      *object) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13WidgetFactory17initializePreviewEP'
        '7QWidget',
        self._addressOf(object),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def currentFormWindow(
      self,
      fw: Optional[QDesignerFormWindowInterface],
  ) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::WidgetFactory::currentFormWindow(
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::WidgetFactory::currentFormWindow(
    #      QDesignerFormWindowInterface *fw)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory17currentFormWindowEP2'
        '8QDesignerFormWindowInterface',
        self._addressOf(fw),
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  @overload(str)
  def getStyle(self, styleName: str) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *qdesigner_internal::WidgetFactory::getStyle(const
    QString &styleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#getStyle

    Parameters
    ----------

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *qdesigner_internal::WidgetFactory::getStyle(const QString
    #      &styleName)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory8getStyleERK7QString',
        styleName,
    )
    from ..QtWidgets import QStyle
    return QStyle._cuteAt(address)

  @overload(str, QWidget)
  @overload(str, NoneType)
  def applyStyleTopLevel(self, styleName: str, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetFactory::applyStyleTopLevel(const QString
    &styleName, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::applyStyleTopLevel(const
    #      QString &styleName, QWidget *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory18applyStyleTopLevelER'
        'K7QStringP7QWidget',
        styleName, self._addressOf(w),
    )

  def loadPlugins(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetFactory::loadPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html#loadPlugins
    """
    #  void qdesigner_internal::WidgetFactory::loadPlugins()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory11loadPluginsEv',
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def activeFormWindowChanged(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetFactory::activeFormWindowChanged(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::activeFormWindowChanged(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory23activeFormWindowChan'
        'gedEP28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def formWindowAdded(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetFactory::formWindowAdded(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetfactory.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::WidgetFactory::formWindowAdded(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13WidgetFactory15formWindowAddedEP28Q'
        'DesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @staticmethod
  def createCustomWidget(*__, **_) -> Never:
    """
    Qt's 'QWidget
    *qdesigner_internal::WidgetFactory::createCustomWidget(const QString
    &className, QWidget *parentWidget, bool *creationError) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.WidgetFactory.createCustomWidget' has no cute "
        "function yet. Qt's 'QWidget "
        "*qdesigner_internal::WidgetFactory::createCustomWidget(const "
        "QString &className, QWidget *parentWidget, bool *creationError) "
        "const': takes a number to change where it is.")
