"""
QFileDialogOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QDir, QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QFileDialogOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFileDialogOptions: a plain Python object standing in
  front of one C++ QFileDialogOptions.

  What exists
  -----------

  Every function of Qt's QFileDialogOptions that has a ritual and that Python
  can call so far, 40 names in all: 'windowTitle', 'setWindowTitle',
  'setOption', 'testOption', 'setOptions', 'options', 'filter', 'setFilter',
  'setViewMode', 'viewMode', 'setFileMode', 'fileMode', 'setAcceptMode',
  'acceptMode', 'setSidebarUrls', 'sidebarUrls', 'useDefaultNameFilters',
  'setUseDefaultNameFilters', 'setNameFilters', 'nameFilters',
  'setMimeTypeFilters', 'mimeTypeFilters', 'setDefaultSuffix',
  'defaultSuffix', 'setHistory', 'history', 'setLabelText', 'labelText',
  'isLabelExplicitlySet', 'initialDirectory', 'setInitialDirectory',
  'initiallySelectedMimeTypeFilter', 'setInitiallySelectedMimeTypeFilter',
  'initiallySelectedNameFilter', 'setInitiallySelectedNameFilter',
  'initiallySelectedFiles', 'setInitiallySelectedFiles',
  'setSupportedSchemes', 'supportedSchemes', 'defaultNameFilterString'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileDialogOptions::QFileDialogOptions(QFileDialogOptionsPrivate
    *dd)': names 'QFileDialogOptionsPrivate', which has no cute class yet.
  - Qt's 'QFileDialogOptions::~QFileDialogOptions()': the destructor: Python
    never removes a C++ QFileDialogOptions.
  - Qt's 'QSharedPointer<QFileDialogOptions> QFileDialogOptions::create()':
    gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QFileDialogOptions> QFileDialogOptions::clone()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 49 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QFileDialogOptions is created at the first use, not by
    'QFileDialogOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDialogOptions.
  - Each name of Qt's QFileDialogOptions that has no cute function yet,
    '__init__', 'clone', 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFileDialogOptions, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AcceptMode(CuteNum):
    """
    The enum 'QFileDialogOptions::AcceptMode' of Qt, with the 2 names Qt
    gives in it.
    """

    AcceptOpen = Kee[int](0)
    AcceptSave = Kee[int](1)

  class DialogLabel(CuteNum):
    """
    The enum 'QFileDialogOptions::DialogLabel' of Qt, with the 6 names Qt
    gives in it.
    """

    LookIn = Kee[int](0)
    FileName = Kee[int](1)
    FileType = Kee[int](2)
    Accept = Kee[int](3)
    Reject = Kee[int](4)
    DialogLabelCount = Kee[int](5)

  class FileDialogOption(CuteFlags):
    """
    The flags enum 'QFileDialogOptions::FileDialogOption' of Qt, with the 7
    names Qt gives in it. Qt names the type of its combinations
    'QFileDialogOptions::FileDialogOptions'.
    """

    ShowDirsOnly = 0x1
    DontResolveSymlinks = 0x2
    DontConfirmOverwrite = 0x4
    DontUseNativeDialog = 0x8
    ReadOnly = 0x10
    HideNameFilterDetails = 0x20
    DontUseCustomDirectoryIcons = 0x40

  FileDialogOptions = FileDialogOption

  class FileMode(CuteNum):
    """
    The enum 'QFileDialogOptions::FileMode' of Qt, with the 5 names Qt gives
    in it.
    """

    AnyFile = Kee[int](0)
    ExistingFile = Kee[int](1)
    Directory = Kee[int](2)
    ExistingFiles = Kee[int](3)
    DirectoryOnly = Kee[int](4)

  class ViewMode(CuteNum):
    """
    The enum 'QFileDialogOptions::ViewMode' of Qt, with the 2 names Qt gives
    in it.
    """

    Detail = Kee[int](0)
    List = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultNameFilterString() -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::defaultNameFilterString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#defaultNameFilterString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::defaultNameFilterString()
    return Rituals.call(
        'ritual_ZN18QFileDialogOptions23defaultNameFilterStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileDialogOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::windowTitle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::windowTitle() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions11windowTitleEv',
    )

  @overload(FileDialogOption)
  def testOption(self, option: FileDialogOption) -> bool:
    """
    Calls Qt's 'bool QFileDialogOptions::testOption(FileDialogOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#testOption

    Parameters
    ----------

    option : FileDialogOption
      Passed on as its number.
    """
    #  bool QFileDialogOptions::testOption(FileDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions10testOptionENS_16FileDialogOptionE',
        option.value,
    )

  def options(self) -> FileDialogOptions:
    """
    Calls Qt's 'FileDialogOptions QFileDialogOptions::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#options

    Returns
    -------

    FileDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  FileDialogOptions QFileDialogOptions::options() const
    return QFileDialogOptions.FileDialogOptions(self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions7optionsEv',
    ))

  def filter(self) -> QDir.Filters:
    """
    Calls Qt's 'QDir::Filters QFileDialogOptions::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#filter

    Returns
    -------

    QDir.Filters
      The value standing for the combination Qt gave back.
    """
    #  QDir::Filters QFileDialogOptions::filter() const
    return QDir.Filters(self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions6filterEv',
    ))

  def viewMode(self) -> ViewMode:
    """
    Calls Qt's 'ViewMode QFileDialogOptions::viewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#viewMode

    Returns
    -------

    ViewMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewMode(number)' gives.
    """
    #  ViewMode QFileDialogOptions::viewMode() const
    return QFileDialogOptions.ViewMode(self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions8viewModeEv',
    ))

  def fileMode(self) -> FileMode:
    """
    Calls Qt's 'FileMode QFileDialogOptions::fileMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#fileMode

    Returns
    -------

    FileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileMode(number)' gives.
    """
    #  FileMode QFileDialogOptions::fileMode() const
    return QFileDialogOptions.FileMode(self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions8fileModeEv',
    ))

  def acceptMode(self) -> AcceptMode:
    """
    Calls Qt's 'AcceptMode QFileDialogOptions::acceptMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#acceptMode

    Returns
    -------

    AcceptMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AcceptMode(number)'
      gives.
    """
    #  AcceptMode QFileDialogOptions::acceptMode() const
    return QFileDialogOptions.AcceptMode(self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions10acceptModeEv',
    ))

  def sidebarUrls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QFileDialogOptions::sidebarUrls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#sidebarUrls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QFileDialogOptions::sidebarUrls() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions11sidebarUrlsEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def useDefaultNameFilters(self) -> bool:
    """
    Calls Qt's 'bool QFileDialogOptions::useDefaultNameFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#useDefaultNameFilters
    """
    #  bool QFileDialogOptions::useDefaultNameFilters() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions21useDefaultNameFiltersEv',
    )

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogOptions::nameFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogOptions::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def mimeTypeFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogOptions::mimeTypeFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#mimeTypeFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogOptions::mimeTypeFilters() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions15mimeTypeFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def defaultSuffix(self) -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::defaultSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#defaultSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::defaultSuffix() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions13defaultSuffixEv',
    )

  def history(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogOptions::history() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#history

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogOptions::history() const
    address = self.uglySide.call('ritual_ZNK18QFileDialogOptions7historyEv')
    return QStringList._cuteOwning(address)

  @overload(DialogLabel)
  def labelText(self, label: DialogLabel) -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::labelText(DialogLabel label)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#labelText

    Parameters
    ----------

    label : DialogLabel
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::labelText(DialogLabel label) const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions9labelTextENS_11DialogLabelE',
        label.value,
    )

  def initialDirectory(self) -> QUrl:
    """
    Calls Qt's 'QUrl QFileDialogOptions::initialDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#initialDirectory

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QFileDialogOptions::initialDirectory() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions16initialDirectoryEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def initiallySelectedMimeTypeFilter(self) -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::initiallySelectedMimeTypeFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::initiallySelectedMimeTypeFilter() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions31initiallySelectedMimeTypeFilterEv',
    )

  def initiallySelectedNameFilter(self) -> str:
    """
    Calls Qt's 'QString QFileDialogOptions::initiallySelectedNameFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialogOptions::initiallySelectedNameFilter() const
    return self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions27initiallySelectedNameFilterEv',
    )

  def initiallySelectedFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QFileDialogOptions::initiallySelectedFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#initiallySelectedFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QFileDialogOptions::initiallySelectedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions22initiallySelectedFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def supportedSchemes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileDialogOptions::supportedSchemes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#supportedSchemes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileDialogOptions::supportedSchemes() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileDialogOptions16supportedSchemesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setWindowTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setWindowTitle(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setWindowTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogOptions::setWindowTitle(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions14setWindowTitleERK7QString', a0,
    )

  @overload(FileDialogOption)
  @overload(FileDialogOption, bool)
  def setOption(self, option: FileDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setOption(FileDialogOption option,
    bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#setOption

    Parameters
    ----------

    option : FileDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QFileDialogOptions::setOption(FileDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions9setOptionENS_16FileDialogOptionEb',
        option.value, on,
    )

  @overload(FileDialogOptions)
  def setOptions(self, options: FileDialogOptions) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setOptions(FileDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#setOptions

    Parameters
    ----------

    options : FileDialogOptions
      Passed on as its number.
    """
    #  void QFileDialogOptions::setOptions(FileDialogOptions options)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions10setOptionsE6QFlagsINS_16FileDialogO'
        'ptionEE',
        options.value,
    )

  @overload(QDir.Filters)
  def setFilter(self, filters: QDir.Filters) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setFilter(QDir::Filters filters)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#setFilter

    Parameters
    ----------

    filters : QDir.Filters
      Passed on as its number.
    """
    #  void QFileDialogOptions::setFilter(QDir::Filters filters)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions9setFilterE6QFlagsIN4QDir6FilterEE',
        filters.value,
    )

  @overload(ViewMode)
  def setViewMode(self, mode: ViewMode) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setViewMode(ViewMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setViewMode

    Parameters
    ----------

    mode : ViewMode
      Passed on as its number.
    """
    #  void QFileDialogOptions::setViewMode(ViewMode mode)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions11setViewModeENS_8ViewModeE',
        mode.value,
    )

  @overload(FileMode)
  def setFileMode(self, mode: FileMode) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setFileMode(FileMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setFileMode

    Parameters
    ----------

    mode : FileMode
      Passed on as its number.
    """
    #  void QFileDialogOptions::setFileMode(FileMode mode)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions11setFileModeENS_8FileModeE',
        mode.value,
    )

  @overload(AcceptMode)
  def setAcceptMode(self, mode: AcceptMode) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setAcceptMode(AcceptMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setAcceptMode

    Parameters
    ----------

    mode : AcceptMode
      Passed on as its number.
    """
    #  void QFileDialogOptions::setAcceptMode(AcceptMode mode)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions13setAcceptModeENS_10AcceptModeE',
        mode.value,
    )

  @overload(QList[QUrl])
  def setSidebarUrls(self, urls: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setSidebarUrls(const QList<QUrl>
    &urls)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setSidebarUrls

    Parameters
    ----------

    urls : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setSidebarUrls(const QList<QUrl> &urls)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions14setSidebarUrlsERK5QListI4QUrlE',
        self._valueOf(urls),
    )

  @overload(bool)
  def setUseDefaultNameFilters(self, d: bool) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setUseDefaultNameFilters(bool d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setUseDefaultNameFilters

    Parameters
    ----------

    d : bool
      Passed on as it is.
    """
    #  void QFileDialogOptions::setUseDefaultNameFilters(bool d)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions24setUseDefaultNameFiltersEb', d,
    )

  @overload(QStringList)
  def setNameFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setNameFilters(const QStringList
    &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setNameFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setNameFilters(const QStringList &filters)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions14setNameFiltersERK5QListI7QStringE',
        self._valueOf(filters),
    )

  @overload(QStringList)
  def setMimeTypeFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setMimeTypeFilters(const QStringList
    &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setMimeTypeFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setMimeTypeFilters(const QStringList
    #      &filters)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions18setMimeTypeFiltersERK5QListI7QStrin'
        'gE',
        self._valueOf(filters),
    )

  @overload(str)
  def setDefaultSuffix(self, suffix: str) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setDefaultSuffix(const QString
    &suffix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setDefaultSuffix

    Parameters
    ----------

    suffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogOptions::setDefaultSuffix(const QString &suffix)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions16setDefaultSuffixERK7QString', suffix,
    )

  @overload(QStringList)
  def setHistory(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setHistory(const QStringList
    &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialogoptions.html#setHistory

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setHistory(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions10setHistoryERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(DialogLabel, str)
  def setLabelText(self, label: DialogLabel, text: str) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setLabelText(DialogLabel label,
    const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setLabelText

    Parameters
    ----------

    label : DialogLabel
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogOptions::setLabelText(DialogLabel label, const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions12setLabelTextENS_11DialogLabelERK7QS'
        'tring',
        label.value, text,
    )

  @overload(QUrl)
  def setInitialDirectory(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setInitialDirectory(const QUrl
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setInitialDirectory

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialogOptions::setInitialDirectory(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions19setInitialDirectoryERK4QUrl',
        self._valueOf(a0),
    )

  @overload(str)
  def setInitiallySelectedMimeTypeFilter(self, a0: str) -> None:
    """
    Calls Qt's 'void
    QFileDialogOptions::setInitiallySelectedMimeTypeFilter(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogOptions::setInitiallySelectedMimeTypeFilter(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions34setInitiallySelectedMimeTypeFilterE'
        'RK7QString',
        a0,
    )

  @overload(str)
  def setInitiallySelectedNameFilter(self, a0: str) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setInitiallySelectedNameFilter(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialogOptions::setInitiallySelectedNameFilter(const QString
    #      &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions30setInitiallySelectedNameFilterERK7Q'
        'String',
        a0,
    )

  @overload(QList[QUrl])
  def setInitiallySelectedFiles(self, a0: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setInitiallySelectedFiles(const
    QList<QUrl> &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setInitiallySelectedFiles

    Parameters
    ----------

    a0 : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setInitiallySelectedFiles(const QList<QUrl>
    #      &a0)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions25setInitiallySelectedFilesERK5QListI'
        '4QUrlE',
        self._valueOf(a0),
    )

  @overload(QStringList)
  def setSupportedSchemes(self, schemes: QStringList) -> None:
    """
    Calls Qt's 'void QFileDialogOptions::setSupportedSchemes(const
    QStringList &schemes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#setSupportedSchemes

    Parameters
    ----------

    schemes : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileDialogOptions::setSupportedSchemes(const QStringList
    #      &schemes)
    self.uglySide.call(
        'ritual_ZN18QFileDialogOptions19setSupportedSchemesERK5QListI7QStri'
        'ngE',
        self._valueOf(schemes),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QFileDialogOptions::QFileDialogOptions(QFileDialogOptionsPrivate
    *dd)': names 'QFileDialogOptionsPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFileDialogOptions.__init__' has no cute function yet. Qt's "
        "'QFileDialogOptions::QFileDialogOptions(QFileDialogOptionsPrivate "
        "*dd)': names 'QFileDialogOptionsPrivate', which has no cute class "
        "yet.")

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

  @overload(DialogLabel)
  def isLabelExplicitlySet(self, label: DialogLabel) -> bool:
    """
    Calls Qt's 'bool QFileDialogOptions::isLabelExplicitlySet(DialogLabel
    label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialogoptions.html#isLabelExplicitlySet

    Parameters
    ----------

    label : DialogLabel
      Passed on as its number.
    """
    #  bool QFileDialogOptions::isLabelExplicitlySet(DialogLabel label)
    return self.uglySide.call(
        'ritual_ZN18QFileDialogOptions20isLabelExplicitlySetENS_11DialogLab'
        'elE',
        label.value,
    )

  @staticmethod
  def clone(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions> QFileDialogOptions::clone()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFileDialogOptions.clone' has no cute function yet. Qt's "
        "'QSharedPointer<QFileDialogOptions> QFileDialogOptions::clone() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions> QFileDialogOptions::create()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFileDialogOptions.create' has no cute function yet. Qt's "
        "'QSharedPointer<QFileDialogOptions> QFileDialogOptions::create()': "
        "gives a type Python has no way to take yet.")
