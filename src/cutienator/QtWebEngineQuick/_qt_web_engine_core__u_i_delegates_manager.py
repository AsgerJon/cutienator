"""
QtWebEngineCore::UIDelegatesManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/ui_delegates_manager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWebEngineCore::UIDelegatesManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QPoint
  from . import QQuickWebEngineAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QQuickWebEngineAction = WAIT['QQuickWebEngineAction']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UIDelegatesManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtWebEngineCore::UIDelegatesManager: a plain Python
  object standing in front of one C++ QtWebEngineCore::UIDelegatesManager.

  What exists
  -----------

  Every function of Qt's QtWebEngineCore::UIDelegatesManager that has a
  ritual and that Python can call so far, 4 names in all: 'tr',
  'addMenuItem', 'addMenu', 'showMenu'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWebEngineCore::UIDelegatesManager::~UIDelegatesManager()': the
    destructor: Python never removes a C++
    QtWebEngineCore::UIDelegatesManager.

  What has no ritual
  ------------------

  17 of the 22 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 6 the
  compiler refuses its ritual as it would be written here; 2 cannot be called
  and cannot be called through the meta-object and cannot be copied; 2
  forbidden.

  What to expect
  --------------

  - The C++ QtWebEngineCore::UIDelegatesManager is created at the first use,
    not by 'QtWebEngineCore::UIDelegatesManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWebEngineCore::UIDelegatesManager.
  - Each name of Qt's QtWebEngineCore::UIDelegatesManager that has no cute
    function yet, '__init__', 'addMenuSeparator', 'createTouchHandle',
    'creationContextForComponent', 'ensureComponentLoaded',
    'hideAutofillPopup', 'hideTouchSelectionMenu', 'showAutofillPopup',
    'showColorDialog', 'showDialog', 'showDirectoryPicker', 'showFilePicker',
    'showToolTip', 'showTouchSelectionMenu', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QtWebEngineCore::UIDelegatesManager, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ComponentType(CuteNum):
    """
    The enum 'QtWebEngineCore::UIDelegatesManager::ComponentType' of Qt, with
    the 16 names Qt gives in it.
    """

    Invalid = Kee[int](-1)
    Menu = Kee[int](0)
    MenuItem = Kee[int](1)
    MenuSeparator = Kee[int](2)
    AlertDialog = Kee[int](3)
    ColorDialog = Kee[int](4)
    ConfirmDialog = Kee[int](5)
    PromptDialog = Kee[int](6)
    FilePicker = Kee[int](7)
    DirectoryPicker = Kee[int](8)
    AuthenticationDialog = Kee[int](9)
    ToolTip = Kee[int](10)
    TouchHandle = Kee[int](11)
    TouchSelectionMenu = Kee[int](12)
    AutofillPopup = Kee[int](13)
    ComponentTypeCount = Kee[int](14)

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QtWebEngineCore::UIDelegatesManager::tr(const char
    *sourceText, const char *disambiguation, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-uidelegatesmanager.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtWebEngineCore::UIDelegatesManager::tr(const char
    #      *sourceText, const char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN15QtWebEngineCore18UIDelegatesManager2trEPKcS2_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWebEngineCore::UIDelegatesManager'

  #  A C++ QtWebEngineCore::UIDelegatesManager Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWebEngineCore_UIDelegatesManager'

  #  The functions Qt calls itself that QtWebEngineCore::UIDelegatesManager
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'addMenuItem': (
          ('_ZN15QtWebEngineCore18UIDelegatesManager11addMenuItemEP21QQuick'
           'WebEngineActionP7QObjectbb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWebEngineQuick:QQuickWebEngineAction'),
               ('address', 'address', 'QtCore:QObject'),
               ('bool', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'addMenu': (
          ('_ZN15QtWebEngineCore18UIDelegatesManager7addMenuEP7QObjectRK7QS'
           'tringRK6QPoint',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'showMenu': (
          ('_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject',
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
    Qt's 'QtWebEngineCore::UIDelegatesManager::UIDelegatesManager(
    QQuickWebEngineView *a0)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.__init__' has no cute function "
        "yet. Qt's "
        "'QtWebEngineCore::UIDelegatesManager::UIDelegatesManager(QQuickWebE"
        "ngineView *a0)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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

  @overload(QQuickWebEngineAction, QObject)
  @overload(QQuickWebEngineAction, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QQuickWebEngineAction, QObject, bool)
  @overload(QQuickWebEngineAction, NoneType, bool)
  @overload(NoneType, QObject, bool)
  @overload(NoneType, NoneType, bool)
  @overload(QQuickWebEngineAction, QObject, bool, bool)
  @overload(QQuickWebEngineAction, NoneType, bool, bool)
  @overload(NoneType, QObject, bool, bool)
  @overload(NoneType, NoneType, bool, bool)
  def addMenuItem(
      self,
      action: Optional[QQuickWebEngineAction],
      menu: Optional[QObject],
      checkable: bool = False,
      checked: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QtWebEngineCore::UIDelegatesManager::addMenuItem(QQuickWebEngineAction
    *action, QObject *menu, bool checkable, bool checked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-uidelegatesmanager.html

    Parameters
    ----------

    action : Optional[QQuickWebEngineAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    menu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    checkable : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    checked : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QtWebEngineCore::UIDelegatesManager::addMenuItem(
    #      QQuickWebEngineAction *action, QObject *menu, bool checkable, bool
    #      checked)
    self.uglySide.call(
        'ritual_ZN15QtWebEngineCore18UIDelegatesManager11addMenuItemEP21QQu'
        'ickWebEngineActionP7QObjectbb',
        self._addressOf(action), self._addressOf(menu, 'QObject'), checkable,
        checked,
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  @overload(QObject, str, QPoint)
  @overload(NoneType, str, QPoint)
  def addMenu(
      self,
      parentMenu: Optional[QObject],
      title: str,
      pos: Optional[QPoint] = None,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtWebEngineCore::UIDelegatesManager::addMenu(QObject
    *parentMenu, const QString &title, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-uidelegatesmanager.html#addMenu

    Parameters
    ----------

    parentMenu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    pos : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint()' is then passed on.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtWebEngineCore::UIDelegatesManager::addMenu(QObject
    #      *parentMenu, const QString &title, const QPoint &pos)
    if pos is None:
      from ..QtCore import QPoint
      pos = QPoint()
    address = self.uglySide.call(
        'ritual_ZN15QtWebEngineCore18UIDelegatesManager7addMenuEP7QObjectRK'
        '7QStringRK6QPoint',
        self._addressOf(parentMenu, 'QObject'), title, self._valueOf(pos),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def showMenu(self, menu: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QtWebEngineCore::UIDelegatesManager::showMenu(QObject
    *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwebenginecore-uidelegatesmanager.html#showMenu

    Parameters
    ----------

    menu : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtWebEngineCore::UIDelegatesManager::showMenu(QObject *menu)
    ritual = (
        'ritual_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QtWebEngineCore18UIDelegatesManager8showMenuEP7QO'
          'bject')
    self.uglySide.call(ritual, self._addressOf(menu, 'QObject'))

  @staticmethod
  def addMenuSeparator(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::addMenuSeparator(QObject
    *menu)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: no matching function for call to
    'qmlContext'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.addMenuSeparator' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::addMenuSeparator(QObject "
        "*menu)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'qmlContext'.")

  @staticmethod
  def createTouchHandle(*__, **_) -> Never:
    """
    Qt's 'QQuickItem
    *QtWebEngineCore::UIDelegatesManager::createTouchHandle()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: no matching function for call to 'qmlContext'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.createTouchHandle' has no cute "
        "function yet. Qt's 'QQuickItem "
        "*QtWebEngineCore::UIDelegatesManager::createTouchHandle()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching function for call to "
        "'qmlContext'.")

  @staticmethod
  def creationContextForComponent(*__, **_) -> Never:
    """
    Qt's 'QQmlContext
    *QtWebEngineCore::UIDelegatesManager::creationContextForComponent(
    QQmlComponent *a0)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.creationContextForComponent' "
        "has no cute function yet. Qt's 'QQmlContext "
        "*QtWebEngineCore::UIDelegatesManager::creationContextForComponent(Q"
        "QmlComponent *a0)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def ensureComponentLoaded(*__, **_) -> Never:
    """
    Qt's 'bool
    QtWebEngineCore::UIDelegatesManager::ensureComponentLoaded(ComponentType
    a0)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: no matching function for call to
    'qmlEngine'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.ensureComponentLoaded' has no "
        "cute function yet. Qt's 'bool "
        "QtWebEngineCore::UIDelegatesManager::ensureComponentLoaded(Componen"
        "tType a0)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'qmlEngine'.")

  @staticmethod
  def hideAutofillPopup(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::hideAutofillPopup()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: no matching function for call to
    'singleShot'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.hideAutofillPopup' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::hideAutofillPopup()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching function for call to "
        "'singleShot'.")

  @staticmethod
  def hideTouchSelectionMenu(*__, **_) -> Never:
    """
    Qt's 'void
    QtWebEngineCore::UIDelegatesManager::hideTouchSelectionMenu()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching function for call to 'singleShot'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.hideTouchSelectionMenu' has no "
        "cute function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::hideTouchSelectionMenu()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no matching function for call to "
        "'singleShot'.")

  @staticmethod
  def showAutofillPopup(*__, **_) -> Never:
    """
    Qt's 'void
    QtWebEngineCore::UIDelegatesManager::showAutofillPopup(QtWebEngineCore::
    AutofillPopupController *controller, QPointF pos, int width, bool
    autoselectFirstSuggestion)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QtWebEngineCore::AutofillPopupController'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showAutofillPopup' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showAutofillPopup(QtWebEngineC"
        "ore::AutofillPopupController *controller, QPointF pos, int width, "
        "bool autoselectFirstSuggestion)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type "
        "'QtWebEngineCore::AutofillPopupController'.")

  @staticmethod
  def showColorDialog(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::showColorDialog(
    QSharedPointer<ColorChooserController> a0)': the compiler refuses its
    ritual as it would be written here: unknown type name
    'ColorChooserController'; did you mean
    'QtWebEngineCore::ColorChooserController'?.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showColorDialog' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showColorDialog(QSharedPointer"
        "<ColorChooserController> a0)': the compiler refuses its ritual as "
        "it would be written here: unknown type name "
        "'ColorChooserController'; did you mean "
        "'QtWebEngineCore::ColorChooserController'?.")

  @staticmethod
  def showDialog(*__, **_) -> Never:
    """
    - Qt's 'void QtWebEngineCore::UIDelegatesManager::showDialog(
      QSharedPointer<JavaScriptDialogController> a0)': the compiler refuses
      its ritual as it would be written here: unknown type name
      'JavaScriptDialogController'; did you mean
      'QtWebEngineCore::JavaScriptDialogController'?.
    - Qt's 'void QtWebEngineCore::UIDelegatesManager::showDialog(
      QSharedPointer<AuthenticationDialogController> a0)': the compiler
      refuses its ritual as it would be written here: unknown type name
      'AuthenticationDialogController'; did you mean
      'QtWebEngineCore::AuthenticationDialogController'?.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showDialog' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showDialog(QSharedPointer<Java"
        "ScriptDialogController> a0)': the compiler refuses its ritual as "
        "it would be written here: unknown type name "
        "'JavaScriptDialogController'; did you mean "
        "'QtWebEngineCore::JavaScriptDialogController'?. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showDialog(QSharedPointer<Auth"
        "enticationDialogController> a0)': the compiler refuses its ritual "
        "as it would be written here: unknown type name "
        "'AuthenticationDialogController'; did you mean "
        "'QtWebEngineCore::AuthenticationDialogController'?.")

  @staticmethod
  def showDirectoryPicker(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::showDirectoryPicker(
    QSharedPointer<FilePickerController> a0)': the compiler refuses its
    ritual as it would be written here: unknown type name
    'FilePickerController'; did you mean
    'QtWebEngineCore::FilePickerController'?.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showDirectoryPicker' has no "
        "cute function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showDirectoryPicker(QSharedPoi"
        "nter<FilePickerController> a0)': the compiler refuses its ritual "
        "as it would be written here: unknown type name "
        "'FilePickerController'; did you mean "
        "'QtWebEngineCore::FilePickerController'?.")

  @staticmethod
  def showFilePicker(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::showFilePicker(
    QSharedPointer<FilePickerController> a0)': the compiler refuses its
    ritual as it would be written here: unknown type name
    'FilePickerController'; did you mean
    'QtWebEngineCore::FilePickerController'?.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showFilePicker' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showFilePicker(QSharedPointer<"
        "FilePickerController> a0)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'FilePickerController'; "
        "did you mean 'QtWebEngineCore::FilePickerController'?.")

  @staticmethod
  def showToolTip(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::showToolTip(const QString
    &text)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: no matching function for call to
    'qmlContext'.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showToolTip' has no cute "
        "function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showToolTip(const QString "
        "&text)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no matching function "
        "for call to 'qmlContext'.")

  @staticmethod
  def showTouchSelectionMenu(*__, **_) -> Never:
    """
    Qt's 'void QtWebEngineCore::UIDelegatesManager::showTouchSelectionMenu(
    TouchSelectionMenuController *a0, const QRect &a1, const int spacing)':
    the compiler refuses its ritual as it would be written here: unknown type
    name 'TouchSelectionMenuController'; did you mean
    'QtWebEngineCore::TouchSelectionMenuController'?.
    """
    raise NotImplementedError(
        "'QtWebEngineCore.UIDelegatesManager.showTouchSelectionMenu' has no "
        "cute function yet. Qt's 'void "
        "QtWebEngineCore::UIDelegatesManager::showTouchSelectionMenu(TouchSe"
        "lectionMenuController *a0, const QRect &a1, const int spacing)': "
        "the compiler refuses its ritual as it would be written here: "
        "unknown type name 'TouchSelectionMenuController'; did you mean "
        "'QtWebEngineCore::TouchSelectionMenuController'?.")
