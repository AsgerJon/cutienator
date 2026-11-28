"""
QQuickLabsPlatformMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenubar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformMenuBar to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickLabsPlatformMenu
  from ..QtCore import QMetaObject
  from ..QtGui import QPlatformMenuBar, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickLabsPlatformMenu = WAIT['QQuickLabsPlatformMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformMenuBar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformMenuBar: a plain Python object
  standing in front of one C++ QQuickLabsPlatformMenuBar.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformMenuBar that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'handle', 'window',
  'addMenu', 'removeMenu', 'clear', 'menusChanged', 'windowChanged',
  'classBegin', 'componentComplete', 'findWindow'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformMenuBar::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformMenuBar::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickLabsPlatformMenuBar::~QQuickLabsPlatformMenuBar()': the
    destructor: Python never removes a C++ QQuickLabsPlatformMenuBar.
  - Qt's 'qsizetype
    QQuickLabsPlatformMenuBar::data_count(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'QObject
    *QQuickLabsPlatformMenuBar::data_at(QQmlListProperty<QObject> *property,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QQuickLabsPlatformMenuBar::data_clear(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'qsizetype QQuickLabsPlatformMenuBar::menus_count(
    QQmlListProperty<QQuickLabsPlatformMenu> *property)': names
    'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute class yet.
  - Qt's 'QQuickLabsPlatformMenu *QQuickLabsPlatformMenuBar::menus_at(
    QQmlListProperty<QQuickLabsPlatformMenu> *property, qsizetype index)':
    names 'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute class
    yet.

  What has no ritual
  ------------------

  11 of the 30 functions Qt declares: 5 leans on 'QQuickLabsPlatformMenu; 3
  leans on 'QQuickLabsPlatformMenuBar; 2 not a gap; 1 the compiler refuses
  its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformMenuBar is created at the first use, not by
    'QQuickLabsPlatformMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformMenuBar.
  - Qt tells when it has removed the C++ QQuickLabsPlatformMenuBar. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformMenuBar that has no cute function
    yet, '__init__', 'data', 'data_append', 'data_at', 'data_clear',
    'data_count', 'insertMenu', 'menus', 'menus_append', 'menus_at',
    'menus_clear', 'menus_count', 'setWindow', holds a function that raises
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
  __qt_class__ = 'QQuickLabsPlatformMenuBar'

  #  A C++ QQuickLabsPlatformMenuBar Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabsPlatformMenuBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformMenuBar::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMenuBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickLabsPlatformMenuBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handle(self) -> Optional[QPlatformMenuBar]:
    """
    Calls Qt's 'QPlatformMenuBar *QQuickLabsPlatformMenuBar::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#handle

    Returns
    -------

    Optional[QPlatformMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenuBar *QQuickLabsPlatformMenuBar::handle() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickLabsPlatformMenuBar6handleEv',
    )
    from ..QtGui import QPlatformMenuBar
    return QPlatformMenuBar._cuteAt(address)

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickLabsPlatformMenuBar::window() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickLabsPlatformMenuBar::window() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickLabsPlatformMenuBar6windowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def findWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickLabsPlatformMenuBar::findWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#findWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickLabsPlatformMenuBar::findWindow() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickLabsPlatformMenuBar10findWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenuBar::QQuickLabsPlatformMenuBar(QObject
    *parent)': leans on
    'QQuickLabsPlatformMenuBar::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.__init__' has no cute function yet. "
        "Qt's 'QQuickLabsPlatformMenuBar::QQuickLabsPlatformMenuBar(QObject "
        "*parent)': leans on "
        "'QQuickLabsPlatformMenuBar::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QQuickLabsPlatformMenu)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QQuickLabsPlatformMenu]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuBar::addMenu(QQuickLabsPlatformMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#addMenu

    Parameters
    ----------

    menu : Optional[QQuickLabsPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuBar::addMenu(QQuickLabsPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN25QQuickLabsPlatformMenuBar7addMenuEP22QQuickLabsPlatform'
        'Menu',
        self._addressOf(menu),
    )

  @overload(QQuickLabsPlatformMenu)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QQuickLabsPlatformMenu]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMenuBar::removeMenu(QQuickLabsPlatformMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#removeMenu

    Parameters
    ----------

    menu : Optional[QQuickLabsPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMenuBar::removeMenu(QQuickLabsPlatformMenu
    #      *menu)
    self.uglySide.call(
        'ritual_ZN25QQuickLabsPlatformMenuBar10removeMenuEP22QQuickLabsPlat'
        'formMenu',
        self._addressOf(menu),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuBar::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#clear
    """
    #  void QQuickLabsPlatformMenuBar::clear()
    self.uglySide.call('ritual_ZN25QQuickLabsPlatformMenuBar5clearEv')

  def menusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuBar::menusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#menusChanged
    """
    #  void QQuickLabsPlatformMenuBar::menusChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickLabsPlatformMenuBar12menusChangedEv',
    )

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuBar::windowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#windowChanged
    """
    #  void QQuickLabsPlatformMenuBar::windowChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickLabsPlatformMenuBar13windowChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuBar::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#classBegin
    """
    #  void QQuickLabsPlatformMenuBar::classBegin()
    ritual = 'ritual_ZN25QQuickLabsPlatformMenuBar10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickLabsPlatformMenuBar10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMenuBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmenubar.html#componentComplete
    """
    #  void QQuickLabsPlatformMenuBar::componentComplete()
    self.uglySide.call(
        'ritual_ZN25QQuickLabsPlatformMenuBar17componentCompleteEv',
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickLabsPlatformMenuBar::data()': leans
    on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickLabsPlatformMenuBar::data()': "
        "leans on 'QQuickLabsPlatformMenu::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def data_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformMenuBar::data_append(QQmlListProperty<QObject>
    *property, QObject *object)': leans on
    'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.data_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuBar::data_append(QQmlListProperty<QObject> "
        "*property, QObject *object)': leans on "
        "'QQuickLabsPlatformMenu::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def data_at(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQuickLabsPlatformMenuBar::data_at(QQmlListProperty<QObject> *property,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.data_at' has no cute function yet. Qt's "
        "'QObject "
        "*QQuickLabsPlatformMenuBar::data_at(QQmlListProperty<QObject> "
        "*property, qsizetype index)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")

  @staticmethod
  def data_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformMenuBar::data_clear(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.data_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuBar::data_clear(QQmlListProperty<QObject> "
        "*property)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickLabsPlatformMenuBar::data_count(QQmlListProperty<QObject>
    *property)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.data_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickLabsPlatformMenuBar::data_count(QQmlListProperty<QObject> "
        "*property)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def insertMenu(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuBar::insertMenu(int index,
    QQuickLabsPlatformMenu *menu)': the compiler refuses its ritual as it
    would be written here: redefinition of 'index' with a different type:
    'const int' vs 'int'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.insertMenu' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuBar::insertMenu(int index, "
        "QQuickLabsPlatformMenu *menu)': the compiler refuses its ritual as "
        "it would be written here: redefinition of 'index' with a different "
        "type: 'const int' vs 'int'.")

  @staticmethod
  def menus(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickLabsPlatformMenu>
    QQuickLabsPlatformMenuBar::menus()': leans on
    'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.menus' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickLabsPlatformMenu> "
        "QQuickLabsPlatformMenuBar::menus()': leans on "
        "'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menus_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuBar::menus_append(
    QQmlListProperty<QQuickLabsPlatformMenu> *property,
    QQuickLabsPlatformMenu *menu)': leans on
    'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.menus_append' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuBar::menus_append(QQmlListProperty<QQuickLabs"
        "PlatformMenu> *property, QQuickLabsPlatformMenu *menu)': leans on "
        "'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menus_at(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformMenu *QQuickLabsPlatformMenuBar::menus_at(
    QQmlListProperty<QQuickLabsPlatformMenu> *property, qsizetype index)':
    names 'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.menus_at' has no cute function yet. "
        "Qt's 'QQuickLabsPlatformMenu "
        "*QQuickLabsPlatformMenuBar::menus_at(QQmlListProperty<QQuickLabsPla"
        "tformMenu> *property, qsizetype index)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute "
        "class yet.")

  @staticmethod
  def menus_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuBar::menus_clear(
    QQmlListProperty<QQuickLabsPlatformMenu> *property)': leans on
    'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.menus_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuickLabsPlatformMenuBar::menus_clear(QQmlListProperty<QQuickLabsP"
        "latformMenu> *property)': leans on "
        "'QQuickLabsPlatformMenu::menuBarChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menus_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickLabsPlatformMenuBar::menus_count(
    QQmlListProperty<QQuickLabsPlatformMenu> *property)': names
    'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.menus_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickLabsPlatformMenuBar::menus_count(QQmlListProperty<QQuickLabsP"
        "latformMenu> *property)': names "
        "'QQmlListProperty<QQuickLabsPlatformMenu>', which has no cute "
        "class yet.")

  @staticmethod
  def setWindow(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMenuBar::setWindow(QWindow *window)': leans
    on 'QQuickLabsPlatformMenuBar::windowChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMenuBar.setWindow' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformMenuBar::setWindow(QWindow *window)': "
        "leans on 'QQuickLabsPlatformMenuBar::windowChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
