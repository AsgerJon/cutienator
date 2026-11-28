"""
QQuickSideBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSideBar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem
  from . import QQuickSideBarPrivate
  from ..QtQuickTemplates2 import QQuickDialog
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickDialog = WAIT['QQuickDialog']
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSideBar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickSideBar: a plain Python object standing in
  front of one C++ QQuickSideBar.

  What exists
  -----------

  Every function of Qt's QQuickSideBar that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'dialog', 'setDialog',
  'favoritePaths', 'buttonDelegate', 'setButtonDelegate',
  'separatorDelegate', 'setSeparatorDelegate', 'addFavoriteDelegate',
  'setAddFavoriteDelegate', 'dialogChanged', 'folderPathsChanged',
  'effectiveFolderPathsChanged', 'favoritePathsChanged',
  'buttonDelegateChanged', 'separatorDelegateChanged',
  'addFavoriteDelegateChanged', 'componentComplete', 'setFavoritePaths',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSideBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSideBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSideBar::~QQuickSideBar()': the destructor: Python never
    removes a C++ QQuickSideBar.
  - Qt's 'QList<QStandardPaths::StandardLocation>
    QQuickSideBar::folderPaths() const': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuickSideBar::setFolderPaths(const
    QList<QStandardPaths::StandardLocation> &folderPaths)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<QStandardPaths::StandardLocation>
    QQuickSideBar::effectiveFolderPaths() const': gives a type Python has no
    way to take yet.
  - Qt's 'const QQuickSideBarPrivate *QQuickSideBar::d_func() const': takes
    in Python what 'QQuickSideBarPrivate *QQuickSideBar::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSideBar is created at the first use, not by
    'QQuickSideBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSideBar.
  - Qt tells when it has removed the C++ QQuickSideBar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickSideBar that has no cute function yet,
    'effectiveFolderPaths', 'folderPaths', 'setFolderPaths', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickSideBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#tr

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
    #  QString QQuickSideBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickSideBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSideBar'

  #  A C++ QQuickSideBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSideBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSideBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSideBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickSideBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dialog(self) -> Optional[QQuickDialog]:
    """
    Calls Qt's 'QQuickDialog *QQuickSideBar::dialog() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#dialog

    Returns
    -------

    Optional[QQuickDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialog *QQuickSideBar::dialog() const
    address = self.uglySide.call('ritual_ZNK13QQuickSideBar6dialogEv')
    from ..QtQuickTemplates2 import QQuickDialog
    return QQuickDialog._cuteAt(address)

  def favoritePaths(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickSideBar::favoritePaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#favoritePaths

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickSideBar::favoritePaths() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSideBar13favoritePathsEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def buttonDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSideBar::buttonDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#buttonDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSideBar::buttonDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSideBar14buttonDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def separatorDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSideBar::separatorDelegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#separatorDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSideBar::separatorDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSideBar17separatorDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def addFavoriteDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSideBar::addFavoriteDelegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#addFavoriteDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSideBar::addFavoriteDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSideBar19addFavoriteDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialog)
  @overload(NoneType)
  def setDialog(self, dialog: Optional[QQuickDialog]) -> None:
    """
    Calls Qt's 'void QQuickSideBar::setDialog(QQuickDialog *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#setDialog

    Parameters
    ----------

    dialog : Optional[QQuickDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBar::setDialog(QQuickDialog *dialog)
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar9setDialogEP12QQuickDialog',
        self._addressOf(dialog),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setButtonDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSideBar::setButtonDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#setButtonDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBar::setButtonDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar17setButtonDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setSeparatorDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSideBar::setSeparatorDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#setSeparatorDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBar::setSeparatorDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar20setSeparatorDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setAddFavoriteDelegate(
      self,
      delegate: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void QQuickSideBar::setAddFavoriteDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#setAddFavoriteDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSideBar::setAddFavoriteDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar22setAddFavoriteDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QList[QUrl])
  def setFavoritePaths(self, favoritePaths: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QQuickSideBar::setFavoritePaths(const QList<QUrl>
    &favoritePaths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#setFavoritePaths

    Parameters
    ----------

    favoritePaths : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickSideBar::setFavoritePaths(const QList<QUrl> &favoritePaths)
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar16setFavoritePathsERK5QListI4QUrlE',
        self._valueOf(favoritePaths),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickSideBar::QQuickSideBar(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#QQuickSideBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSideBar::QQuickSideBar(QQuickItem *parent)
    self._noteCreation(QQuickSideBar, lambda: Rituals.call(
        'ritual_ZN13QQuickSideBarC1EP10QQuickItem', self._addressOf(parent),
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

  def dialogChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::dialogChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#dialogChanged
    """
    #  void QQuickSideBar::dialogChanged()
    self.uglySide.call('ritual_ZN13QQuickSideBar13dialogChangedEv')

  def folderPathsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::folderPathsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#folderPathsChanged
    """
    #  void QQuickSideBar::folderPathsChanged()
    self.uglySide.call('ritual_ZN13QQuickSideBar18folderPathsChangedEv')

  def effectiveFolderPathsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::effectiveFolderPathsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#effectiveFolderPathsChanged
    """
    #  void QQuickSideBar::effectiveFolderPathsChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar27effectiveFolderPathsChangedEv',
    )

  def favoritePathsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::favoritePathsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#favoritePathsChanged
    """
    #  void QQuickSideBar::favoritePathsChanged()
    self.uglySide.call('ritual_ZN13QQuickSideBar20favoritePathsChangedEv')

  def buttonDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::buttonDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#buttonDelegateChanged
    """
    #  void QQuickSideBar::buttonDelegateChanged()
    self.uglySide.call('ritual_ZN13QQuickSideBar21buttonDelegateChangedEv')

  def separatorDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::separatorDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#separatorDelegateChanged
    """
    #  void QQuickSideBar::separatorDelegateChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar24separatorDelegateChangedEv',
    )

  def addFavoriteDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::addFavoriteDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#addFavoriteDelegateChanged
    """
    #  void QQuickSideBar::addFavoriteDelegateChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickSideBar26addFavoriteDelegateChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSideBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksidebar.html#componentComplete
    """
    #  void QQuickSideBar::componentComplete()
    ritual = 'ritual_ZN13QQuickSideBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSideBar17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickSideBarPrivate]:
    """
    Calls Qt's 'QQuickSideBarPrivate *QQuickSideBar::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksidebar.html#d_func

    Returns
    -------

    Optional[QQuickSideBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSideBarPrivate *QQuickSideBar::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickSideBar6d_funcEv')
    from . import QQuickSideBarPrivate
    return QQuickSideBarPrivate._cuteAt(address)

  @staticmethod
  def effectiveFolderPaths(*__, **_) -> Never:
    """
    Qt's 'QList<QStandardPaths::StandardLocation>
    QQuickSideBar::effectiveFolderPaths() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuickSideBar.effectiveFolderPaths' has no cute function yet. "
        "Qt's 'QList<QStandardPaths::StandardLocation> "
        "QQuickSideBar::effectiveFolderPaths() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def folderPaths(*__, **_) -> Never:
    """
    Qt's 'QList<QStandardPaths::StandardLocation>
    QQuickSideBar::folderPaths() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuickSideBar.folderPaths' has no cute function yet. Qt's "
        "'QList<QStandardPaths::StandardLocation> "
        "QQuickSideBar::folderPaths() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setFolderPaths(*__, **_) -> Never:
    """
    Qt's 'void QQuickSideBar::setFolderPaths(const
    QList<QStandardPaths::StandardLocation> &folderPaths)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickSideBar.setFolderPaths' has no cute function yet. Qt's "
        "'void QQuickSideBar::setFolderPaths(const "
        "QList<QStandardPaths::StandardLocation> &folderPaths)': takes a "
        "type Python has no way to hand over yet.")
