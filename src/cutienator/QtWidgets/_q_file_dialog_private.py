"""
QFileDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileDialogPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QDir, QList, QStringList
from . import QDialog, QDialogPrivate, QFileDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPoint, QUrl
  from ..QtGui import QAction, QKeyEvent, QPlatformDialogHelper
  from ..QtGui import QPlatformFileDialogHelper
  from . import QAbstractItemView, QFileDialogArgs, QLineEdit
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QFileDialogArgs = WAIT['QFileDialogArgs']
  QKeyEvent = WAIT['QKeyEvent']
  QModelIndex = WAIT['QModelIndex']
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']
  QPoint = WAIT['QPoint']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileDialogPrivate(QDialogPrivate):
  """
  The cute side of Qt's QFileDialogPrivate: a plain Python object standing in
  front of one C++ QFileDialogPrivate.

  It is built on the cute 'QDialogPrivate', as Qt's QFileDialogPrivate is
  built on Qt's QDialogPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileDialogPrivate that has a ritual and that Python
  can call so far, 79 names in all: 'q_func', 'platformFileDialogHelper',
  'createToolButtons', 'createMenuActions', 'createWidgets', 'init',
  'itemViewKeyboardEvent', 'getEnvironmentVariable', 'typedFiles',
  'userSelectedFiles', 'addDefaultSuffixToFiles', 'addDefaultSuffixToUrls',
  'removeDirectory', 'setLabelTextControl', 'updateLookInLabel',
  'updateFileNameLabel', 'updateFileTypeLabel', 'updateOkButtonText',
  'updateCancelButtonText', 'mapToSource', 'mapFromSource', 'rootPath',
  'lineEdit', 'maxNameLength', 'basename', 'filterForMode', 'currentView',
  'toInternal', 'saveSettings', 'restoreFromSettings',
  'setLastVisitedDirectory', 'retranslateWindowTitle', 'retranslateStrings',
  'emitFilesSelected', 'saveHistorySelection', 'goHome', 'pathChanged',
  'navigateBackward', 'navigateForward', 'navigateToParent',
  'createDirectory', 'showListView', 'showDetailsView', 'showContextMenu',
  'renameCurrent', 'deleteCurrent', 'showHidden', 'showHeader',
  'updateOkButton', 'currentChanged', 'enterDirectory', 'emitUrlSelected',
  'emitUrlsSelected', 'nativeCurrentChanged', 'nativeEnterDirectory',
  'goToDirectory', 'useNameFilter', 'selectionChanged', 'goToUrl',
  'autoCompleteFileName', 'rowsInserted', 'fileRenamed', 'canBeNativeDialog',
  'setVisible', 'usingWidgets', 'setDirectory_sys', 'directory_sys',
  'selectFile_sys', 'selectedFiles_sys', 'setFilter_sys',
  'selectMimeTypeFilter_sys', 'selectedMimeTypeFilter_sys',
  'selectNameFilter_sys', 'selectedNameFilter_sys', 'initHelper',
  'helperPrepareShow', 'helperDone', 'itemNotFound', 'itemAlreadyExists'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileDialog *QFileDialogPrivate::q_func() const': takes in
    Python what 'QFileDialog *QFileDialogPrivate::q_func()' takes.
  - Qt's 'bool QFileDialogPrivate::restoreWidgetState(QStringList &history,
    int splitterPosition)': takes a type Python has no way to hand over yet.
  - Qt's 'void QFileDialogPrivate::navigate(HistoryItem &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QFileDialogPrivate::~QFileDialogPrivate()': the destructor: Python
    never removes a C++ QFileDialogPrivate.

  What has no ritual
  ------------------

  7 of the 91 functions Qt declares: 4 forbidden; 3 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QFileDialogPrivate is created at the first use, not by
    'QFileDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDialogPrivate.
  - Each name of Qt's QFileDialogPrivate that has no cute function yet,
    'navigate', 'restoreWidgetState', 'rootIndex', 'select', 'setRootIndex',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QFileDialogPrivate, each a class in here as
  #  in C++.

  class HistoryItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFileDialogPrivate::HistoryItem: a plain Python
    object standing in front of one C++ QFileDialogPrivate::HistoryItem.

    C++ hands a QFileDialogPrivate::HistoryItem around as a copy, so every
    C++ QFileDialogPrivate::HistoryItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QFileDialogPrivate::HistoryItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFileDialogPrivate::HistoryItem::~HistoryItem()': the destructor:
      Python removes its C++ QFileDialogPrivate::HistoryItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QFileDialogPrivate::HistoryItem is created at the first use,
      not by 'QFileDialogPrivate::HistoryItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFileDialogPrivate::HistoryItem back gives a copy
      the ritual made for Python, in a new cute
      QFileDialogPrivate::HistoryItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFileDialogPrivate::HistoryItem'

    #  Qt's '~QFileDialogPrivate::HistoryItem()'. Naming it makes this a
    #  value class: Python owns every C++ QFileDialogPrivate::HistoryItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QFileDialogPrivate11HistoryItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def maxNameLength(path: str) -> int:
    """
    Calls Qt's 'long QFileDialogPrivate::maxNameLength(const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#maxNameLength

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  long QFileDialogPrivate::maxNameLength(const QString &path)
    return Rituals.call(
        'ritual_ZN18QFileDialogPrivate13maxNameLengthERK7QString', path,
    )

  @staticmethod
  @overload(str)
  def toInternal(path: str) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::toInternal(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#toInternal

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::toInternal(const QString &path)
    return Rituals.call(
        'ritual_ZN18QFileDialogPrivate10toInternalERK7QString', path,
    )

  @staticmethod
  @overload(QUrl)
  def setLastVisitedDirectory(dir: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::setLastVisitedDirectory(const QUrl
    &dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#setLastVisitedDirectory

    Parameters
    ----------

    dir : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::setLastVisitedDirectory(const QUrl &dir)
    Rituals.call(
        'ritual_ZN18QFileDialogPrivate23setLastVisitedDirectoryERK4QUrl',
        CuteMixin._valueOf(dir),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileDialogPrivate'

  #  A C++ QFileDialogPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileDialogPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def platformFileDialogHelper(self) -> Optional[QPlatformFileDialogHelper]:
    """
    Calls Qt's 'QPlatformFileDialogHelper
    *QFileDialogPrivate::platformFileDialogHelper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#platformFileDialogHelper

    Returns
    -------

    Optional[QPlatformFileDialogHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformFileDialogHelper
    #      *QFileDialogPrivate::platformFileDialogHelper() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate24platformFileDialogHelperEv',
    )
    from ..QtGui import QPlatformFileDialogHelper
    return QPlatformFileDialogHelper._cuteAt(address)

  def typedFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogPrivate::typedFiles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#typedFiles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogPrivate::typedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate10typedFilesEv',
    )
    return QStringList._cuteOwning(address)

  def userSelectedFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QFileDialogPrivate::userSelectedFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#userSelectedFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QFileDialogPrivate::userSelectedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate17userSelectedFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(QStringList)
  def addDefaultSuffixToFiles(self, filesToFix: QStringList) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogPrivate::addDefaultSuffixToFiles(const
    QStringList &filesToFix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#addDefaultSuffixToFiles

    Parameters
    ----------

    filesToFix : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogPrivate::addDefaultSuffixToFiles(const
    #      QStringList &filesToFix) const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate23addDefaultSuffixToFilesERK5QListI7'
        'QStringE',
        self._valueOf(filesToFix),
    )
    return QStringList._cuteOwning(address)

  @overload(QList[QUrl])
  def addDefaultSuffixToUrls(self, urlsToFix: QList[QUrl]) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QFileDialogPrivate::addDefaultSuffixToUrls(const
    QList<QUrl> &urlsToFix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#addDefaultSuffixToUrls

    Parameters
    ----------

    urlsToFix : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QFileDialogPrivate::addDefaultSuffixToUrls(const
    #      QList<QUrl> &urlsToFix) const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate22addDefaultSuffixToUrlsERK5QListI4Q'
        'UrlE',
        self._valueOf(urlsToFix),
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(QModelIndex)
  def mapToSource(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileDialogPrivate::mapToSource(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#mapToSource

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileDialogPrivate::mapToSource(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate11mapToSourceERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def mapFromSource(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileDialogPrivate::mapFromSource(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#mapFromSource

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileDialogPrivate::mapFromSource(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate13mapFromSourceERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def rootPath(self) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::rootPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#rootPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::rootPath() const
    return self.uglySide.call('ritual_ZNK18QFileDialogPrivate8rootPathEv')

  def lineEdit(self) -> Optional[QLineEdit]:
    """
    Calls Qt's 'QLineEdit *QFileDialogPrivate::lineEdit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#lineEdit

    Returns
    -------

    Optional[QLineEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineEdit *QFileDialogPrivate::lineEdit() const
    address = self.uglySide.call('ritual_ZNK18QFileDialogPrivate8lineEditEv')
    from . import QLineEdit
    return QLineEdit._cuteAt(address)

  @overload(str)
  def basename(self, path: str) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::basename(const QString &path)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#basename

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::basename(const QString &path) const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate8basenameERK7QString', path,
    )

  @overload(QDir.Filters)
  def filterForMode(self, filters: QDir.Filters) -> QDir.Filters:
    """
    Calls Qt's 'QDir::Filters QFileDialogPrivate::filterForMode(QDir::Filters
    filters) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#filterForMode

    Parameters
    ----------

    filters : QDir.Filters
      Passed on as its number.

    Returns
    -------

    QDir.Filters
      The value standing for the combination Qt gave back.
    """
    #  QDir::Filters QFileDialogPrivate::filterForMode(QDir::Filters filters)
    #      const
    return QDir.Filters(self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate13filterForModeE6QFlagsIN4QDir6Filte'
        'rEE',
        filters.value,
    ))

  def currentView(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QFileDialogPrivate::currentView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#currentView

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QFileDialogPrivate::currentView() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate11currentViewEv',
    )
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def canBeNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::canBeNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#canBeNativeDialog
    """
    #  bool QFileDialogPrivate::canBeNativeDialog() const
    ritual = 'ritual_ZNK18QFileDialogPrivate17canBeNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QFileDialogPrivate17canBeNativeDialogEv'
    return self.uglySide.call(ritual)

  def usingWidgets(self) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::usingWidgets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#usingWidgets
    """
    #  bool QFileDialogPrivate::usingWidgets() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate12usingWidgetsEv',
    )

  def directory_sys(self) -> QUrl:
    """
    Calls Qt's 'QUrl QFileDialogPrivate::directory_sys() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#directory_sys

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QFileDialogPrivate::directory_sys() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate13directory_sysEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFiles_sys(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QFileDialogPrivate::selectedFiles_sys() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectedFiles_sys

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QFileDialogPrivate::selectedFiles_sys() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate17selectedFiles_sysEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def selectedMimeTypeFilter_sys(self) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::selectedMimeTypeFilter_sys()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectedMimeTypeFilter_sys

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::selectedMimeTypeFilter_sys() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate26selectedMimeTypeFilter_sysEv',
    )

  def selectedNameFilter_sys(self) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::selectedNameFilter_sys() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectedNameFilter_sys

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::selectedNameFilter_sys() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogPrivate22selectedNameFilter_sysEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileDialog.DialogLabel, str)
  def setLabelTextControl(
      self,
      label: QFileDialog.DialogLabel,
      text: str,
  ) -> None:
    """
    Calls Qt's 'void
    QFileDialogPrivate::setLabelTextControl(QFileDialog::DialogLabel label,
    const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#setLabelTextControl

    Parameters
    ----------

    label : QFileDialog.DialogLabel
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::setLabelTextControl(QFileDialog::DialogLabel
    #      label, const QString &text)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate19setLabelTextControlEN11QFileDialog1'
        '1DialogLabelERK7QString',
        label.value, text,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QFileDialogPrivate::setVisible(bool visible)
    ritual = 'ritual_ZN18QFileDialogPrivate10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QFileDialogPrivate10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(QUrl)
  def setDirectory_sys(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::setDirectory_sys(const QUrl
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#setDirectory_sys

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::setDirectory_sys(const QUrl &directory)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate16setDirectory_sysERK4QUrl',
        self._valueOf(directory),
    )

  def setFilter_sys(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::setFilter_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#setFilter_sys
    """
    #  void QFileDialogPrivate::setFilter_sys()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate13setFilter_sysEv')

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
    'QFileDialogPrivate::QFileDialogPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#QFileDialogPrivate
    """
    #  QFileDialogPrivate::QFileDialogPrivate()
    self._noteCreation(QFileDialogPrivate, lambda: Rituals.call(
        'ritual_ZN18QFileDialogPrivateC1Ev',
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

  def q_func(self) -> Optional[QFileDialog]:
    """
    Calls Qt's 'QFileDialog *QFileDialogPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#q_func

    Returns
    -------

    Optional[QFileDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileDialog *QFileDialogPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QFileDialogPrivate6q_funcEv')
    return QFileDialog._cuteAt(address)

  def createToolButtons(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::createToolButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#createToolButtons
    """
    #  void QFileDialogPrivate::createToolButtons()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate17createToolButtonsEv')

  def createMenuActions(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::createMenuActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#createMenuActions
    """
    #  void QFileDialogPrivate::createMenuActions()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate17createMenuActionsEv')

  def createWidgets(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::createWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#createWidgets
    """
    #  void QFileDialogPrivate::createWidgets()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate13createWidgetsEv')

  @overload(QFileDialogArgs)
  def init(self, args: QFileDialogArgs) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::init(const QFileDialogArgs &args)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#init

    Parameters
    ----------

    args : QFileDialogArgs
      Passed on as a value: Qt reads the C++ QFileDialogArgs, which stays
      Python's own.
    """
    #  void QFileDialogPrivate::init(const QFileDialogArgs &args)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate4initERK15QFileDialogArgs',
        self._valueOf(args),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def itemViewKeyboardEvent(self, event: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::itemViewKeyboardEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#itemViewKeyboardEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFileDialogPrivate::itemViewKeyboardEvent(QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate21itemViewKeyboardEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(str)
  def getEnvironmentVariable(self, string: str) -> str:
    """
    Calls Qt's 'QString QFileDialogPrivate::getEnvironmentVariable(const
    QString &string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#getEnvironmentVariable

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogPrivate::getEnvironmentVariable(const QString
    #      &string)
    return self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate22getEnvironmentVariableERK7QString',
        string,
    )

  @overload(str)
  def removeDirectory(self, path: str) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::removeDirectory(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#removeDirectory

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileDialogPrivate::removeDirectory(const QString &path)
    return self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate15removeDirectoryERK7QString', path,
    )

  def updateLookInLabel(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateLookInLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateLookInLabel
    """
    #  void QFileDialogPrivate::updateLookInLabel()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate17updateLookInLabelEv')

  def updateFileNameLabel(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateFileNameLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateFileNameLabel
    """
    #  void QFileDialogPrivate::updateFileNameLabel()
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate19updateFileNameLabelEv',
    )

  def updateFileTypeLabel(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateFileTypeLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateFileTypeLabel
    """
    #  void QFileDialogPrivate::updateFileTypeLabel()
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate19updateFileTypeLabelEv',
    )

  @overload()
  @overload(bool)
  def updateOkButtonText(self, saveAsOnFolder: bool = False) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateOkButtonText(bool
    saveAsOnFolder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateOkButtonText

    Parameters
    ----------

    saveAsOnFolder : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QFileDialogPrivate::updateOkButtonText(bool saveAsOnFolder)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate18updateOkButtonTextEb',
        saveAsOnFolder,
    )

  def updateCancelButtonText(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateCancelButtonText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateCancelButtonText
    """
    #  void QFileDialogPrivate::updateCancelButtonText()
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate22updateCancelButtonTextEv',
    )

  def saveSettings(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::saveSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#saveSettings
    """
    #  void QFileDialogPrivate::saveSettings()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate12saveSettingsEv')

  def restoreFromSettings(self) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::restoreFromSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#restoreFromSettings
    """
    #  bool QFileDialogPrivate::restoreFromSettings()
    return self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate19restoreFromSettingsEv',
    )

  def retranslateWindowTitle(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::retranslateWindowTitle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#retranslateWindowTitle
    """
    #  void QFileDialogPrivate::retranslateWindowTitle()
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate22retranslateWindowTitleEv',
    )

  def retranslateStrings(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::retranslateStrings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#retranslateStrings
    """
    #  void QFileDialogPrivate::retranslateStrings()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate18retranslateStringsEv')

  @overload(QStringList)
  def emitFilesSelected(self, files: QStringList) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::emitFilesSelected(const QStringList
    &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#emitFilesSelected

    Parameters
    ----------

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogPrivate::emitFilesSelected(const QStringList &files)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate17emitFilesSelectedERK5QListI7QString'
        'E',
        self._valueOf(files),
    )

  def saveHistorySelection(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::saveHistorySelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#saveHistorySelection
    """
    #  void QFileDialogPrivate::saveHistorySelection()
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate20saveHistorySelectionEv',
    )

  def goHome(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::goHome()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#goHome
    """
    #  void QFileDialogPrivate::goHome()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate6goHomeEv')

  @overload(str)
  def pathChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::pathChanged(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#pathChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::pathChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate11pathChangedERK7QString', a0,
    )

  def navigateBackward(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::navigateBackward()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#navigateBackward
    """
    #  void QFileDialogPrivate::navigateBackward()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate16navigateBackwardEv')

  def navigateForward(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::navigateForward()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#navigateForward
    """
    #  void QFileDialogPrivate::navigateForward()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate15navigateForwardEv')

  def navigateToParent(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::navigateToParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#navigateToParent
    """
    #  void QFileDialogPrivate::navigateToParent()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate16navigateToParentEv')

  def createDirectory(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::createDirectory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#createDirectory
    """
    #  void QFileDialogPrivate::createDirectory()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate15createDirectoryEv')

  def showListView(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::showListView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#showListView
    """
    #  void QFileDialogPrivate::showListView()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate12showListViewEv')

  def showDetailsView(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::showDetailsView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#showDetailsView
    """
    #  void QFileDialogPrivate::showDetailsView()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate15showDetailsViewEv')

  @overload(QPoint)
  def showContextMenu(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::showContextMenu(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#showContextMenu

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QFileDialogPrivate::showContextMenu(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate15showContextMenuERK6QPoint',
        self._valueOf(position),
    )

  def renameCurrent(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::renameCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#renameCurrent
    """
    #  void QFileDialogPrivate::renameCurrent()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate13renameCurrentEv')

  def deleteCurrent(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::deleteCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#deleteCurrent
    """
    #  void QFileDialogPrivate::deleteCurrent()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate13deleteCurrentEv')

  def showHidden(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::showHidden()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#showHidden
    """
    #  void QFileDialogPrivate::showHidden()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate10showHiddenEv')

  @overload(QAction)
  @overload(NoneType)
  def showHeader(self, a0: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::showHeader(QAction *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#showHeader

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogPrivate::showHeader(QAction *a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate10showHeaderEP7QAction',
        self._addressOf(a0),
    )

  def updateOkButton(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::updateOkButton()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#updateOkButton
    """
    #  void QFileDialogPrivate::updateOkButton()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate14updateOkButtonEv')

  @overload(QModelIndex)
  def currentChanged(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::currentChanged(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#currentChanged

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QFileDialogPrivate::currentChanged(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate14currentChangedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def enterDirectory(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::enterDirectory(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#enterDirectory

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QFileDialogPrivate::enterDirectory(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate14enterDirectoryERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QUrl)
  def emitUrlSelected(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::emitUrlSelected(const QUrl &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#emitUrlSelected

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::emitUrlSelected(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate15emitUrlSelectedERK4QUrl',
        self._valueOf(file),
    )

  @overload(QList[QUrl])
  def emitUrlsSelected(self, files: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::emitUrlsSelected(const QList<QUrl>
    &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#emitUrlsSelected

    Parameters
    ----------

    files : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogPrivate::emitUrlsSelected(const QList<QUrl> &files)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate16emitUrlsSelectedERK5QListI4QUrlE',
        self._valueOf(files),
    )

  @overload(QUrl)
  def nativeCurrentChanged(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::nativeCurrentChanged(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#nativeCurrentChanged

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::nativeCurrentChanged(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate20nativeCurrentChangedERK4QUrl',
        self._valueOf(file),
    )

  @overload(QUrl)
  def nativeEnterDirectory(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::nativeEnterDirectory(const QUrl
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#nativeEnterDirectory

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::nativeEnterDirectory(const QUrl &directory)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate20nativeEnterDirectoryERK4QUrl',
        self._valueOf(directory),
    )

  @overload(str)
  def goToDirectory(self, a0: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::goToDirectory(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#goToDirectory

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::goToDirectory(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate13goToDirectoryERK7QString', a0,
    )

  @overload(int)
  def useNameFilter(self, index: int) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::useNameFilter(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#useNameFilter

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QFileDialogPrivate::useNameFilter(int index)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate13useNameFilterEi', index,
    )

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectionChanged
    """
    #  void QFileDialogPrivate::selectionChanged()
    self.uglySide.call('ritual_ZN18QFileDialogPrivate16selectionChangedEv')

  @overload(QUrl)
  def goToUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::goToUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#goToUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::goToUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate7goToUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str)
  def autoCompleteFileName(self, a0: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::autoCompleteFileName(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#autoCompleteFileName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::autoCompleteFileName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate20autoCompleteFileNameERK7QString', a0,
    )

  @overload(QModelIndex)
  def rowsInserted(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::rowsInserted(const QModelIndex
    &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#rowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QFileDialogPrivate::rowsInserted(const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate12rowsInsertedERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(str, str, str)
  def fileRenamed(self, path: str, oldName: str, newName: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::fileRenamed(const QString &path,
    const QString &oldName, const QString &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#fileRenamed

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    oldName : str
      Passed on as it is: a QString is made of it for the call.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::fileRenamed(const QString &path, const
    #      QString &oldName, const QString &newName)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate11fileRenamedERK7QStringS2_S2_',
        path, oldName, newName,
    )

  @overload(QUrl)
  def selectFile_sys(self, filename: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::selectFile_sys(const QUrl
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectFile_sys

    Parameters
    ----------

    filename : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogPrivate::selectFile_sys(const QUrl &filename)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate14selectFile_sysERK4QUrl',
        self._valueOf(filename),
    )

  @overload(str)
  def selectMimeTypeFilter_sys(self, filter: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::selectMimeTypeFilter_sys(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectMimeTypeFilter_sys

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::selectMimeTypeFilter_sys(const QString
    #      &filter)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate24selectMimeTypeFilter_sysERK7QString',
        filter,
    )

  @overload(str)
  def selectNameFilter_sys(self, filter: str) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::selectNameFilter_sys(const QString
    &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#selectNameFilter_sys

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogPrivate::selectNameFilter_sys(const QString &filter)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate20selectNameFilter_sysERK7QString',
        filter,
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def initHelper(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::initHelper(QPlatformDialogHelper
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#initHelper

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogPrivate::initHelper(QPlatformDialogHelper *a0)
    ritual = (
        'ritual_ZN18QFileDialogPrivate10initHelperEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFileDialogPrivate10initHelperEP21QPlatformDialog'
          'Helper')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def helperPrepareShow(self, a0: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QFileDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#helperPrepareShow

    Parameters
    ----------

    a0 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
    ritual = (
        'ritual_ZN18QFileDialogPrivate17helperPrepareShowEP21QPlatformDialo'
        'gHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFileDialogPrivate17helperPrepareShowEP21QPlatfor'
          'mDialogHelper')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDialog.DialogCode, QPlatformDialogHelper)
  @overload(QDialog.DialogCode, NoneType)
  def helperDone(
      self,
      a0: QDialog.DialogCode,
      a1: Optional[QPlatformDialogHelper],
  ) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::helperDone(QDialog::DialogCode a0,
    QPlatformDialogHelper *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogprivate.html#helperDone

    Parameters
    ----------

    a0 : QDialog.DialogCode
      Passed on as its number.

    a1 : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogPrivate::helperDone(QDialog::DialogCode a0,
    #      QPlatformDialogHelper *a1)
    ritual = (
        'ritual_ZN18QFileDialogPrivate10helperDoneEN7QDialog10DialogCodeEP2'
        '1QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFileDialogPrivate10helperDoneEN7QDialog10DialogC'
          'odeEP21QPlatformDialogHelper')
    self.uglySide.call(ritual, a0.value, self._addressOf(a1))

  @overload(str, QFileDialog.FileMode)
  def itemNotFound(self, fileName: str, mode: QFileDialog.FileMode) -> None:
    """
    Calls Qt's 'void QFileDialogPrivate::itemNotFound(const QString
    &fileName, QFileDialog::FileMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#itemNotFound

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QFileDialog.FileMode
      Passed on as its number.
    """
    #  void QFileDialogPrivate::itemNotFound(const QString &fileName,
    #      QFileDialog::FileMode mode)
    self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate12itemNotFoundERK7QStringN11QFileDial'
        'og8FileModeE',
        fileName, mode.value,
    )

  @overload(str)
  def itemAlreadyExists(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QFileDialogPrivate::itemAlreadyExists(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogprivate.html#itemAlreadyExists

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileDialogPrivate::itemAlreadyExists(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN18QFileDialogPrivate17itemAlreadyExistsERK7QString',
        fileName,
    )

  @staticmethod
  def navigate(*__, **_) -> Never:
    """
    Qt's 'void QFileDialogPrivate::navigate(HistoryItem &a0)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileDialogPrivate.navigate' has no cute function yet. Qt's 'void "
        "QFileDialogPrivate::navigate(HistoryItem &a0)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def restoreWidgetState(*__, **_) -> Never:
    """
    Qt's 'bool QFileDialogPrivate::restoreWidgetState(QStringList &history,
    int splitterPosition)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileDialogPrivate.restoreWidgetState' has no cute function yet. "
        "Qt's 'bool QFileDialogPrivate::restoreWidgetState(QStringList "
        "&history, int splitterPosition)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def rootIndex(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QFileDialogPrivate::rootIndex() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'Ui_QFileDialog'.
    """
    raise NotImplementedError(
        "'QFileDialogPrivate.rootIndex' has no cute function yet. Qt's "
        "'QModelIndex QFileDialogPrivate::rootIndex() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'Ui_QFileDialog'.")

  @staticmethod
  def select(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QFileDialogPrivate::select(const QModelIndex &index)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'Ui_QFileDialog'.
    """
    raise NotImplementedError(
        "'QFileDialogPrivate.select' has no cute function yet. Qt's "
        "'QModelIndex QFileDialogPrivate::select(const QModelIndex &index) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'Ui_QFileDialog'.")

  @staticmethod
  def setRootIndex(*__, **_) -> Never:
    """
    Qt's 'void QFileDialogPrivate::setRootIndex(const QModelIndex &index)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'Ui_QFileDialog'.
    """
    raise NotImplementedError(
        "'QFileDialogPrivate.setRootIndex' has no cute function yet. Qt's "
        "'void QFileDialogPrivate::setRootIndex(const QModelIndex &index) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'Ui_QFileDialog'.")
