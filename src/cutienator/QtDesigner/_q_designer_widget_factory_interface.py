"""
QDesignerWidgetFactoryInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractwidgetfactory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QLayout, QWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayout = WAIT['QLayout']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerWidgetFactoryInterface(QObject):
  """
  The cute side of Qt's QDesignerWidgetFactoryInterface: a plain Python
  object standing in front of one C++ QDesignerWidgetFactoryInterface.

  It is built on the cute 'QObject', as Qt's QDesignerWidgetFactoryInterface
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerWidgetFactoryInterface that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'core', 'containerOfWidget', 'widgetOfContainer', 'createWidget',
  'createLayout', 'isPassiveInteractor', 'initialize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerWidgetFactoryInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QDesignerWidgetFactoryInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerWidgetFactoryInterface::~QDesignerWidgetFactoryInterface()':
    the destructor: Python never removes a C++
    QDesignerWidgetFactoryInterface.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerWidgetFactoryInterface is created at the first use, not
    by 'QDesignerWidgetFactoryInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerWidgetFactoryInterface.
  - Qt tells when it has removed the C++ QDesignerWidgetFactoryInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDesignerWidgetFactoryInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#tr

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
    #  QString QDesignerWidgetFactoryInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QDesignerWidgetFactoryInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerWidgetFactoryInterface'

  #  A C++ QDesignerWidgetFactoryInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerWidgetFactoryInterface'

  #  The functions Qt calls itself that QDesignerWidgetFactoryInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK31QDesignerWidgetFactoryInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'containerOfWidget': (
          ('_ZNK31QDesignerWidgetFactoryInterface17containerOfWidgetEP7QWid'
           'get',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'widgetOfContainer': (
          ('_ZNK31QDesignerWidgetFactoryInterface17widgetOfContainerEP7QWid'
           'get',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createWidget': (
          ('_ZNK31QDesignerWidgetFactoryInterface12createWidgetERK7QStringP'
           '7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createLayout': (
          ('_ZNK31QDesignerWidgetFactoryInterface12createLayoutEP7QWidgetP7'
           'QLayouti',
           ('address', 'address', 'QtWidgets:QLayout'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QLayout'),
               ('int', 'number', ''),
           )),
      ),
      'isPassiveInteractor': (
          ('_ZN31QDesignerWidgetFactoryInterface19isPassiveInteractorEP7QWi'
           'dget',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'initialize': (
          ('_ZNK31QDesignerWidgetFactoryInterface10initializeEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDesignerWidgetFactoryInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerWidgetFactoryInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerWidgetFactoryInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerWidgetFactoryInterface::core()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def containerOfWidget(self, w: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QDesignerWidgetFactoryInterface::containerOfWidget(QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerWidgetFactoryInterface::containerOfWidget(QWidget
    #      *w) const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface17containerOfWidgetEP7Q'
        'Widget',
        self._addressOf(w),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def widgetOfContainer(self, w: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QDesignerWidgetFactoryInterface::widgetOfContainer(QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerWidgetFactoryInterface::widgetOfContainer(QWidget
    #      *w) const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface17widgetOfContainerEP7Q'
        'Widget',
        self._addressOf(w),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def createWidget(
      self,
      name: str,
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerWidgetFactoryInterface::createWidget(const
    QString &name, QWidget *parentWidget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#createWidget

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerWidgetFactoryInterface::createWidget(const QString
    #      &name, QWidget *parentWidget) const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface12createWidgetERK7QStri'
        'ngP7QWidget',
        name, self._addressOf(parentWidget),
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
    *QDesignerWidgetFactoryInterface::createLayout(QWidget *widget, QLayout
    *layout, int type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#createLayout

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
    #  QLayout *QDesignerWidgetFactoryInterface::createLayout(QWidget
    #      *widget, QLayout *layout, int type) const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface12createLayoutEP7QWidge'
        'tP7QLayouti',
        self._addressOf(widget), self._addressOf(layout), type,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerWidgetFactoryInterface::QDesignerWidgetFactoryInterface(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerWidgetFactoryInterface::QDesignerWidgetFactoryInterface(
    #      QObject *parent)
    self._noteCreation(QDesignerWidgetFactoryInterface, lambda: Rituals.call(
        'ritual_ZN31QDesignerWidgetFactoryInterfaceC1EP7QObject',
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

  @overload(QWidget)
  @overload(NoneType)
  def isPassiveInteractor(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool
    QDesignerWidgetFactoryInterface::isPassiveInteractor(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerWidgetFactoryInterface::isPassiveInteractor(QWidget
    #      *widget)
    return self.uglySide.call(
        'ritual_ZN31QDesignerWidgetFactoryInterface19isPassiveInteractorEP7'
        'QWidget',
        self._addressOf(widget),
    )

  @overload(QObject)
  @overload(NoneType)
  def initialize(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDesignerWidgetFactoryInterface::initialize(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetfactoryinterface.html#initialize

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerWidgetFactoryInterface::initialize(QObject *object)
    #      const
    self.uglySide.call(
        'ritual_ZNK31QDesignerWidgetFactoryInterface10initializeEP7QObject',
        self._addressOf(object, 'QObject'),
    )
