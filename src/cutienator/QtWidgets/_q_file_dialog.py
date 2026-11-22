"""
QFileDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QDir, QObject
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractProxyModel, QByteArray, QEvent, QMetaObject
  from ..QtCore import QUrl
  from ..QtGui import QAbstractFileIconProvider
  from . import QAbstractItemDelegate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileIconProvider = WAIT['QAbstractFileIconProvider']
  QAbstractItemDelegate = WAIT['QAbstractItemDelegate']
  QAbstractProxyModel = WAIT['QAbstractProxyModel']
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileDialog(QDialog):
  """
  The cute side of Qt's QFileDialog: a plain Python object standing in front
  of one C++ QFileDialog.

  It is built on the cute 'QDialog', as Qt's QFileDialog is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileDialog that has a ritual and that Python can
  call so far, 44 names in all: 'metaObject', 'tr', 'setDirectory',
  'directory', 'setDirectoryUrl', 'directoryUrl', 'selectFile', 'selectUrl',
  'setNameFilter', 'selectNameFilter', 'selectedMimeTypeFilter',
  'selectedNameFilter', 'selectMimeTypeFilter', 'filter', 'setFilter',
  'setViewMode', 'viewMode', 'setFileMode', 'fileMode', 'setAcceptMode',
  'acceptMode', 'saveState', 'restoreState', 'setDefaultSuffix',
  'defaultSuffix', 'setItemDelegate', 'itemDelegate', 'setIconProvider',
  'iconProvider', 'setLabelText', 'labelText', 'setProxyModel', 'proxyModel',
  'setOption', 'testOption', 'setOptions', 'options', 'open', 'setVisible',
  'getExistingDirectory', 'saveFileContent', 'done', 'accept', 'changeEvent'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileDialog::~QFileDialog()': the destructor: Python never removes
    a C++ QFileDialog.
  - Qt's 'QString QFileDialog::getOpenFileName(QWidget *parent, const QString
    &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, Options options)': names 'QString', which has no cute
    class yet.
  - Qt's 'QString QFileDialog::getSaveFileName(QWidget *parent, const QString
    &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, Options options)': names 'QString', which has no cute
    class yet.

  What has no ritual
  ------------------

  36 of the 86 functions Qt declares: 20 takes or gives a type that cannot be
  passed yet; 9 a signal; 3 private; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QFileDialog is created at the first use, not by
    'QFileDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDialog.
  - Qt tells when it has removed the C++ QFileDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QFileDialog, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AcceptMode(CuteNum):
    """
    The enum 'QFileDialog::AcceptMode' of Qt, with the 2 names Qt gives in
    it.
    """

    AcceptOpen = Kee[int](0)
    AcceptSave = Kee[int](1)

  class DialogLabel(CuteNum):
    """
    The enum 'QFileDialog::DialogLabel' of Qt, with the 5 names Qt gives in
    it.
    """

    LookIn = Kee[int](0)
    FileName = Kee[int](1)
    FileType = Kee[int](2)
    Accept = Kee[int](3)
    Reject = Kee[int](4)

  class FileMode(CuteNum):
    """
    The enum 'QFileDialog::FileMode' of Qt, with the 4 names Qt gives in it.
    """

    AnyFile = Kee[int](0)
    ExistingFile = Kee[int](1)
    Directory = Kee[int](2)
    ExistingFiles = Kee[int](3)

  class Option(CuteFlags):
    """
    The flags enum 'QFileDialog::Option' of Qt, with the 7 names Qt gives in
    it. Qt names the type of its combinations 'QFileDialog::Options'.
    """

    ShowDirsOnly = 0x1
    DontResolveSymlinks = 0x2
    DontConfirmOverwrite = 0x4
    DontUseNativeDialog = 0x8
    ReadOnly = 0x10
    HideNameFilterDetails = 0x20
    DontUseCustomDirectoryIcons = 0x40

  Options = Option

  class ViewMode(CuteNum):
    """
    The enum 'QFileDialog::ViewMode' of Qt, with the 2 names Qt gives in it.
    """

    Detail = Kee[int](0)
    List = Kee[int](1)

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
    Calls Qt's 'QString QFileDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#tr

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
    #  QString QFileDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QFileDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, Options)
  @overload(NoneType, str, str, Options)
  def getExistingDirectory(
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      options: Options = Options.ShowDirsOnly,
  ) -> str:
    """
    Calls Qt's 'QString QFileDialog::getExistingDirectory(QWidget *parent,
    const QString &caption, const QString &dir, Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialog.html#getExistingDirectory

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    options : Options
      Passed on as its number. May be left out, as in Qt: it is then
      Options.ShowDirsOnly.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialog::getExistingDirectory(QWidget *parent, const
    #      QString &caption, const QString &dir, Options options)
    return Rituals.call(
        'ritual_ZN11QFileDialog20getExistingDirectoryEP7QWidgetRK7QStringS4'
        '_6QFlagsINS_6OptionEE',
        CuteMixin._addressOf(parent), caption, dir, options.value,
    )

  @staticmethod
  @overload(QByteArray, str)
  @overload(QByteArray, str, QWidget)
  @overload(QByteArray, str, NoneType)
  def saveFileContent(
      fileContent: QByteArray,
      fileNameHint: str,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QFileDialog::saveFileContent(const QByteArray
    &fileContent, const QString &fileNameHint, QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#saveFileContent

    Parameters
    ----------

    fileContent : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileNameHint : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QFileDialog::saveFileContent(const QByteArray &fileContent, const
    #      QString &fileNameHint, QWidget *parent)
    Rituals.call(
        'ritual_ZN11QFileDialog15saveFileContentERK10QByteArrayRK7QStringP7'
        'QWidget',
        CuteMixin._valueOf(fileContent), fileNameHint,
        CuteMixin._addressOf(parent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileDialog'

  #  A C++ QFileDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def directory(self) -> QDir:
    """
    Calls Qt's 'QDir QFileDialog::directory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#directory

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QFileDialog::directory() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog9directoryEv')
    return QDir._cuteOwning(address)

  def directoryUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QFileDialog::directoryUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#directoryUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QFileDialog::directoryUrl() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog12directoryUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedMimeTypeFilter(self) -> str:
    """
    Calls Qt's 'QString QFileDialog::selectedMimeTypeFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialog.html#selectedMimeTypeFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialog::selectedMimeTypeFilter() const
    return self.uglySide.call(
        'ritual_ZNK11QFileDialog22selectedMimeTypeFilterEv',
    )

  def selectedNameFilter(self) -> str:
    """
    Calls Qt's 'QString QFileDialog::selectedNameFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialog.html#selectedNameFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialog::selectedNameFilter() const
    return self.uglySide.call(
        'ritual_ZNK11QFileDialog18selectedNameFilterEv',
    )

  def filter(self) -> QDir.Filters:
    """
    Calls Qt's 'QDir::Filters QFileDialog::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#filter

    Returns
    -------

    QDir.Filters
      The value standing for the combination Qt gave back.
    """
    #  QDir::Filters QFileDialog::filter() const
    return QDir.Filters(self.uglySide.call(
        'ritual_ZNK11QFileDialog6filterEv',
    ))

  def viewMode(self) -> ViewMode:
    """
    Calls Qt's 'ViewMode QFileDialog::viewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#viewMode

    Returns
    -------

    ViewMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewMode(number)' gives.
    """
    #  ViewMode QFileDialog::viewMode() const
    return QFileDialog.ViewMode(self.uglySide.call(
        'ritual_ZNK11QFileDialog8viewModeEv',
    ))

  def fileMode(self) -> FileMode:
    """
    Calls Qt's 'FileMode QFileDialog::fileMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#fileMode

    Returns
    -------

    FileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileMode(number)' gives.
    """
    #  FileMode QFileDialog::fileMode() const
    return QFileDialog.FileMode(self.uglySide.call(
        'ritual_ZNK11QFileDialog8fileModeEv',
    ))

  def acceptMode(self) -> AcceptMode:
    """
    Calls Qt's 'AcceptMode QFileDialog::acceptMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#acceptMode

    Returns
    -------

    AcceptMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AcceptMode(number)'
      gives.
    """
    #  AcceptMode QFileDialog::acceptMode() const
    return QFileDialog.AcceptMode(self.uglySide.call(
        'ritual_ZNK11QFileDialog10acceptModeEv',
    ))

  def saveState(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFileDialog::saveState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#saveState

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFileDialog::saveState() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog9saveStateEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def defaultSuffix(self) -> str:
    """
    Calls Qt's 'QString QFileDialog::defaultSuffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#defaultSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialog::defaultSuffix() const
    return self.uglySide.call('ritual_ZNK11QFileDialog13defaultSuffixEv')

  def itemDelegate(self) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QFileDialog::itemDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#itemDelegate

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QFileDialog::itemDelegate() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog12itemDelegateEv')
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  def iconProvider(self) -> Optional[QAbstractFileIconProvider]:
    """
    Calls Qt's 'QAbstractFileIconProvider *QFileDialog::iconProvider()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#iconProvider

    Returns
    -------

    Optional[QAbstractFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileIconProvider *QFileDialog::iconProvider() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog12iconProviderEv')
    from ..QtGui import QAbstractFileIconProvider
    return QAbstractFileIconProvider._cuteAt(address)

  @overload(DialogLabel)
  def labelText(self, label: DialogLabel) -> str:
    """
    Calls Qt's 'QString QFileDialog::labelText(DialogLabel label) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#labelText

    Parameters
    ----------

    label : DialogLabel
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDialog::labelText(DialogLabel label) const
    return self.uglySide.call(
        'ritual_ZNK11QFileDialog9labelTextENS_11DialogLabelE', label.value,
    )

  def proxyModel(self) -> Optional[QAbstractProxyModel]:
    """
    Calls Qt's 'QAbstractProxyModel *QFileDialog::proxyModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#proxyModel

    Returns
    -------

    Optional[QAbstractProxyModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractProxyModel *QFileDialog::proxyModel() const
    address = self.uglySide.call('ritual_ZNK11QFileDialog10proxyModelEv')
    from ..QtCore import QAbstractProxyModel
    return QAbstractProxyModel._cuteAt(address)

  @overload(Option)
  def testOption(self, option: Option) -> bool:
    """
    Calls Qt's 'bool QFileDialog::testOption(Option option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#testOption

    Parameters
    ----------

    option : Option
      Passed on as its number.
    """
    #  bool QFileDialog::testOption(Option option) const
    return self.uglySide.call(
        'ritual_ZNK11QFileDialog10testOptionENS_6OptionE', option.value,
    )

  def options(self) -> Options:
    """
    Calls Qt's 'Options QFileDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#options

    Returns
    -------

    Options
      The value standing for the combination Qt gave back.
    """
    #  Options QFileDialog::options() const
    return QFileDialog.Options(self.uglySide.call(
        'ritual_ZNK11QFileDialog7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDirectory(self, directory: str) -> None:
    """
    Calls Qt's 'void QFileDialog::setDirectory(const QString &directory)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setDirectory

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::setDirectory(const QString &directory)
    self.uglySide.call(
        'ritual_ZN11QFileDialog12setDirectoryERK7QString', directory,
    )

  @overload(QDir)
  def setDirectory(self, directory: QDir) -> None:
    """
    Calls Qt's 'void QFileDialog::setDirectory(const QDir &directory)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setDirectory

    Parameters
    ----------

    directory : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  void QFileDialog::setDirectory(const QDir &directory)
    self.uglySide.call(
        'ritual_ZN11QFileDialog12setDirectoryERK4QDir',
        self._valueOf(directory),
    )

  @overload(QUrl)
  def setDirectoryUrl(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialog::setDirectoryUrl(const QUrl &directory)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setDirectoryUrl

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialog::setDirectoryUrl(const QUrl &directory)
    self.uglySide.call(
        'ritual_ZN11QFileDialog15setDirectoryUrlERK4QUrl',
        self._valueOf(directory),
    )

  @overload(str)
  def setNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QFileDialog::setNameFilter(const QString &filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::setNameFilter(const QString &filter)
    self.uglySide.call(
        'ritual_ZN11QFileDialog13setNameFilterERK7QString', filter,
    )

  @overload(QDir.Filters)
  def setFilter(self, filters: QDir.Filters) -> None:
    """
    Calls Qt's 'void QFileDialog::setFilter(QDir::Filters filters)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setFilter

    Parameters
    ----------

    filters : QDir.Filters
      Passed on as its number.
    """
    #  void QFileDialog::setFilter(QDir::Filters filters)
    self.uglySide.call(
        'ritual_ZN11QFileDialog9setFilterE6QFlagsIN4QDir6FilterEE',
        filters.value,
    )

  @overload(ViewMode)
  def setViewMode(self, mode: ViewMode) -> None:
    """
    Calls Qt's 'void QFileDialog::setViewMode(ViewMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setViewMode

    Parameters
    ----------

    mode : ViewMode
      Passed on as its number.
    """
    #  void QFileDialog::setViewMode(ViewMode mode)
    self.uglySide.call(
        'ritual_ZN11QFileDialog11setViewModeENS_8ViewModeE', mode.value,
    )

  @overload(FileMode)
  def setFileMode(self, mode: FileMode) -> None:
    """
    Calls Qt's 'void QFileDialog::setFileMode(FileMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setFileMode

    Parameters
    ----------

    mode : FileMode
      Passed on as its number.
    """
    #  void QFileDialog::setFileMode(FileMode mode)
    self.uglySide.call(
        'ritual_ZN11QFileDialog11setFileModeENS_8FileModeE', mode.value,
    )

  @overload(AcceptMode)
  def setAcceptMode(self, mode: AcceptMode) -> None:
    """
    Calls Qt's 'void QFileDialog::setAcceptMode(AcceptMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setAcceptMode

    Parameters
    ----------

    mode : AcceptMode
      Passed on as its number.
    """
    #  void QFileDialog::setAcceptMode(AcceptMode mode)
    self.uglySide.call(
        'ritual_ZN11QFileDialog13setAcceptModeENS_10AcceptModeE', mode.value,
    )

  @overload(str)
  def setDefaultSuffix(self, suffix: str) -> None:
    """
    Calls Qt's 'void QFileDialog::setDefaultSuffix(const QString &suffix)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setDefaultSuffix

    Parameters
    ----------

    suffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::setDefaultSuffix(const QString &suffix)
    self.uglySide.call(
        'ritual_ZN11QFileDialog16setDefaultSuffixERK7QString', suffix,
    )

  @overload(QAbstractItemDelegate)
  @overload(NoneType)
  def setItemDelegate(
      self,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QFileDialog::setItemDelegate(QAbstractItemDelegate
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setItemDelegate

    Parameters
    ----------

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialog::setItemDelegate(QAbstractItemDelegate *delegate)
    self.uglySide.call(
        'ritual_ZN11QFileDialog15setItemDelegateEP21QAbstractItemDelegate',
        self._addressOf(delegate),
    )

  @overload(QAbstractFileIconProvider)
  @overload(NoneType)
  def setIconProvider(
      self,
      provider: Optional[QAbstractFileIconProvider],
  ) -> None:
    """
    Calls Qt's 'void QFileDialog::setIconProvider(QAbstractFileIconProvider
    *provider)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setIconProvider

    Parameters
    ----------

    provider : Optional[QAbstractFileIconProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialog::setIconProvider(QAbstractFileIconProvider *provider)
    self.uglySide.call(
        'ritual_ZN11QFileDialog15setIconProviderEP25QAbstractFileIconProvid'
        'er',
        self._addressOf(provider),
    )

  @overload(DialogLabel, str)
  def setLabelText(self, label: DialogLabel, text: str) -> None:
    """
    Calls Qt's 'void QFileDialog::setLabelText(DialogLabel label, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setLabelText

    Parameters
    ----------

    label : DialogLabel
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::setLabelText(DialogLabel label, const QString &text)
    self.uglySide.call(
        'ritual_ZN11QFileDialog12setLabelTextENS_11DialogLabelERK7QString',
        label.value, text,
    )

  @overload(QAbstractProxyModel)
  @overload(NoneType)
  def setProxyModel(self, model: Optional[QAbstractProxyModel]) -> None:
    """
    Calls Qt's 'void QFileDialog::setProxyModel(QAbstractProxyModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setProxyModel

    Parameters
    ----------

    model : Optional[QAbstractProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialog::setProxyModel(QAbstractProxyModel *model)
    self.uglySide.call(
        'ritual_ZN11QFileDialog13setProxyModelEP19QAbstractProxyModel',
        self._addressOf(model),
    )

  @overload(Option)
  @overload(Option, bool)
  def setOption(self, option: Option, on: bool = True) -> None:
    """
    Calls Qt's 'void QFileDialog::setOption(Option option, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setOption

    Parameters
    ----------

    option : Option
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QFileDialog::setOption(Option option, bool on)
    self.uglySide.call(
        'ritual_ZN11QFileDialog9setOptionENS_6OptionEb', option.value, on,
    )

  @overload(Options)
  def setOptions(self, options: Options) -> None:
    """
    Calls Qt's 'void QFileDialog::setOptions(Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setOptions

    Parameters
    ----------

    options : Options
      Passed on as its number.
    """
    #  void QFileDialog::setOptions(Options options)
    self.uglySide.call(
        'ritual_ZN11QFileDialog10setOptionsE6QFlagsINS_6OptionEE',
        options.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QFileDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QFileDialog::setVisible(bool visible)
    ritual = 'ritual_ZN11QFileDialog10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFileDialog10setVisibleEb'
    self.uglySide.call(ritual, visible)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(self, parent: Optional[QWidget], f: Qt.WindowFlags) -> None:
    """
    Notes what was given, for Qt's 'QFileDialog::QFileDialog(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#QFileDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Qt.WindowFlags
      Passed on as its number.
    """
    #  QFileDialog::QFileDialog(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QFileDialog, lambda: Rituals.call(
        'ritual_ZN11QFileDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
    ))

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      directory: str = '',
      filter: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QFileDialog::QFileDialog(QWidget *parent,
    const QString &caption, const QString &directory, const QString
    &filter)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#QFileDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    directory : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QFileDialog::QFileDialog(QWidget *parent, const QString &caption,
    #      const QString &directory, const QString &filter)
    self._noteCreation(QFileDialog, lambda: Rituals.call(
        'ritual_ZN11QFileDialogC1EP7QWidgetRK7QStringS4_S4_',
        self._addressOf(parent), caption, directory, filter,
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

  @overload(str)
  def selectFile(self, filename: str) -> None:
    """
    Calls Qt's 'void QFileDialog::selectFile(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#selectFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::selectFile(const QString &filename)
    self.uglySide.call(
        'ritual_ZN11QFileDialog10selectFileERK7QString', filename,
    )

  @overload(QUrl)
  def selectUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QFileDialog::selectUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#selectUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QFileDialog::selectUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN11QFileDialog9selectUrlERK4QUrl', self._valueOf(url),
    )

  @overload(str)
  def selectNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QFileDialog::selectNameFilter(const QString &filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#selectNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::selectNameFilter(const QString &filter)
    self.uglySide.call(
        'ritual_ZN11QFileDialog16selectNameFilterERK7QString', filter,
    )

  @overload(str)
  def selectMimeTypeFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QFileDialog::selectMimeTypeFilter(const QString
    &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialog.html#selectMimeTypeFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileDialog::selectMimeTypeFilter(const QString &filter)
    self.uglySide.call(
        'ritual_ZN11QFileDialog20selectMimeTypeFilterERK7QString', filter,
    )

  @overload(QByteArray)
  def restoreState(self, state: QByteArray) -> bool:
    """
    Calls Qt's 'bool QFileDialog::restoreState(const QByteArray &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#restoreState

    Parameters
    ----------

    state : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QFileDialog::restoreState(const QByteArray &state)
    return self.uglySide.call(
        'ritual_ZN11QFileDialog12restoreStateERK10QByteArray',
        self._valueOf(state),
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QFileDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QFileDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN11QFileDialog4openEP7QObjectPKc',
        self._addressOf(receiver), self._bytesOf(member),
    )

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QFileDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QFileDialog::done(int result)
    self.uglySide.call('ritual_own_ZN11QFileDialog4doneEi', result)

  def accept(self) -> None:
    """
    Calls Qt's 'void QFileDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#accept
    """
    #  void QFileDialog::accept()
    self.uglySide.call('ritual_own_ZN11QFileDialog6acceptEv')

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QFileDialog::changeEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialog.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialog::changeEvent(QEvent *e)
    self.uglySide.call(
        'ritual_own_ZN11QFileDialog11changeEventEP6QEvent',
        self._addressOf(e),
    )
