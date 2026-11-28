"""
QQuickFileDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfiledialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialog to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from ..QtGui import QFileDialogOptions
from . import QQuickAbstractDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QPlatformDialogHelper
  from ..QtQuickDialogs2Utils import QQuickFileNameFilter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialog(QQuickAbstractDialog):
  """
  The cute side of Qt's QQuickFileDialog: a plain Python object standing in
  front of one C++ QQuickFileDialog.

  It is built on the cute 'QQuickAbstractDialog', as Qt's QQuickFileDialog is
  built on Qt's QQuickAbstractDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFileDialog that has a ritual and that Python
  can call so far, 49 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'fileMode', 'setFileMode', 'selectedFile',
  'setSelectedFile', 'selectedFiles', 'currentFile', 'setCurrentFile',
  'currentFiles', 'setCurrentFiles', 'currentFolder', 'setCurrentFolder',
  'options', 'setOptions', 'resetOptions', 'nameFilters', 'setNameFilters',
  'resetNameFilters', 'selectedNameFilter', 'defaultSuffix',
  'setDefaultSuffix', 'resetDefaultSuffix', 'acceptLabel', 'setAcceptLabel',
  'resetAcceptLabel', 'rejectLabel', 'setRejectLabel', 'resetRejectLabel',
  'fileModeChanged', 'selectedFileChanged', 'selectedFilesChanged',
  'currentFileChanged', 'currentFilesChanged', 'currentFolderChanged',
  'optionsChanged', 'nameFiltersChanged', 'defaultSuffixChanged',
  'acceptLabelChanged', 'rejectLabelChanged', 'useNativeDialog', 'onCreate',
  'onShow', 'onHide', 'accept', 'addDefaultSuffix', 'addDefaultSuffixes',
  'setSelectedFiles'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFileDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFileDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFileDialog is created at the first use, not by
    'QQuickFileDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialog.
  - Qt tells when it has removed the C++ QQuickFileDialog. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickFileDialog, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FileMode(CuteNum):
    """
    The enum 'QQuickFileDialog::FileMode' of Qt, with the 3 names Qt gives in
    it.
    """

    OpenFile = Kee[int](0)
    OpenFiles = Kee[int](1)
    SaveFile = Kee[int](2)

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
    Calls Qt's 'QString QQuickFileDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#tr

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
    #  QString QQuickFileDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickFileDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN16QQuickFileDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fileMode(self) -> FileMode:
    """
    Calls Qt's 'FileMode QQuickFileDialog::fileMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#fileMode

    Returns
    -------

    FileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileMode(number)' gives.
    """
    #  FileMode QQuickFileDialog::fileMode() const
    return QQuickFileDialog.FileMode(self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog8fileModeEv',
    ))

  def selectedFile(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialog::selectedFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#selectedFile

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialog::selectedFile() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog12selectedFileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickFileDialog::selectedFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#selectedFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickFileDialog::selectedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog13selectedFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def currentFile(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialog::currentFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#currentFile

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialog::currentFile() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog11currentFileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def currentFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickFileDialog::currentFiles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#currentFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickFileDialog::currentFiles() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog12currentFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def currentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialog::currentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#currentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialog::currentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog13currentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def options(self) -> QFileDialogOptions.FileDialogOptions:
    """
    Calls Qt's 'QFileDialogOptions::FileDialogOptions
    QQuickFileDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#options

    Returns
    -------

    QFileDialogOptions.FileDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFileDialogOptions::FileDialogOptions QQuickFileDialog::options()
    #      const
    return QFileDialogOptions.FileDialogOptions(self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog7optionsEv',
    ))

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFileDialog::nameFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFileDialog::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def selectedNameFilter(self) -> Optional[QQuickFileNameFilter]:
    """
    Calls Qt's 'QQuickFileNameFilter *QQuickFileDialog::selectedNameFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#selectedNameFilter

    Returns
    -------

    Optional[QQuickFileNameFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileNameFilter *QQuickFileDialog::selectedNameFilter() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog18selectedNameFilterEv',
    )
    from ..QtQuickDialogs2Utils import QQuickFileNameFilter
    return QQuickFileNameFilter._cuteAt(address)

  def defaultSuffix(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialog::defaultSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#defaultSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialog::defaultSuffix() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog13defaultSuffixEv',
    )

  def acceptLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialog::acceptLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#acceptLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialog::acceptLabel() const
    return self.uglySide.call('ritual_ZNK16QQuickFileDialog11acceptLabelEv')

  def rejectLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialog::rejectLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#rejectLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialog::rejectLabel() const
    return self.uglySide.call('ritual_ZNK16QQuickFileDialog11rejectLabelEv')

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickFileDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#useNativeDialog
    """
    #  bool QQuickFileDialog::useNativeDialog() const
    ritual = 'ritual_ZNK16QQuickFileDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickFileDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  @overload(QUrl)
  def addDefaultSuffix(self, file: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialog::addDefaultSuffix(const QUrl &file)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#addDefaultSuffix

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialog::addDefaultSuffix(const QUrl &file) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog16addDefaultSuffixERK4QUrl',
        self._valueOf(file),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QList[QUrl])
  def addDefaultSuffixes(self, files: QList[QUrl]) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickFileDialog::addDefaultSuffixes(const
    QList<QUrl> &files) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#addDefaultSuffixes

    Parameters
    ----------

    files : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickFileDialog::addDefaultSuffixes(const QList<QUrl>
    #      &files) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFileDialog18addDefaultSuffixesERK5QListI4QUrlE',
        self._valueOf(files),
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FileMode)
  def setFileMode(self, fileMode: FileMode) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setFileMode(FileMode fileMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#setFileMode

    Parameters
    ----------

    fileMode : FileMode
      Passed on as its number.
    """
    #  void QQuickFileDialog::setFileMode(FileMode fileMode)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog11setFileModeENS_8FileModeE',
        fileMode.value,
    )

  @overload(QUrl)
  def setSelectedFile(self, selectedFile: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setSelectedFile(const QUrl
    &selectedFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setSelectedFile

    Parameters
    ----------

    selectedFile : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialog::setSelectedFile(const QUrl &selectedFile)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog15setSelectedFileERK4QUrl',
        self._valueOf(selectedFile),
    )

  @overload(QUrl)
  def setCurrentFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setCurrentFile(const QUrl &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setCurrentFile

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialog::setCurrentFile(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog14setCurrentFileERK4QUrl',
        self._valueOf(file),
    )

  @overload(QList[QUrl])
  def setCurrentFiles(self, currentFiles: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setCurrentFiles(const QList<QUrl>
    &currentFiles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setCurrentFiles

    Parameters
    ----------

    currentFiles : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileDialog::setCurrentFiles(const QList<QUrl>
    #      &currentFiles)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog15setCurrentFilesERK5QListI4QUrlE',
        self._valueOf(currentFiles),
    )

  @overload(QUrl)
  def setCurrentFolder(self, currentFolder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setCurrentFolder(const QUrl
    &currentFolder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setCurrentFolder

    Parameters
    ----------

    currentFolder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialog::setCurrentFolder(const QUrl &currentFolder)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog16setCurrentFolderERK4QUrl',
        self._valueOf(currentFolder),
    )

  @overload(QFileDialogOptions.FileDialogOptions)
  def setOptions(
      self,
      options: QFileDialogOptions.FileDialogOptions,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialog::setOptions(QFileDialogOptions::FileDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#setOptions

    Parameters
    ----------

    options : QFileDialogOptions.FileDialogOptions
      Passed on as its number.
    """
    #  void
    #      QQuickFileDialog::setOptions(QFileDialogOptions::FileDialogOptions
    #      options)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog10setOptionsE6QFlagsIN18QFileDialogOpti'
        'ons16FileDialogOptionEE',
        options.value,
    )

  @overload(QStringList)
  def setNameFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setNameFilters(const QStringList
    &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setNameFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileDialog::setNameFilters(const QStringList &filters)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog14setNameFiltersERK5QListI7QStringE',
        self._valueOf(filters),
    )

  @overload(str)
  def setDefaultSuffix(self, suffix: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setDefaultSuffix(const QString
    &suffix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setDefaultSuffix

    Parameters
    ----------

    suffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialog::setDefaultSuffix(const QString &suffix)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog16setDefaultSuffixERK7QString', suffix,
    )

  @overload(str)
  def setAcceptLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setAcceptLabel(const QString &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setAcceptLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialog::setAcceptLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog14setAcceptLabelERK7QString', label,
    )

  @overload(str)
  def setRejectLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setRejectLabel(const QString &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setRejectLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialog::setRejectLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog14setRejectLabelERK7QString', label,
    )

  @overload(QList[QUrl])
  def setSelectedFiles(self, selectedFiles: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::setSelectedFiles(const QList<QUrl>
    &selectedFiles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#setSelectedFiles

    Parameters
    ----------

    selectedFiles : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileDialog::setSelectedFiles(const QList<QUrl>
    #      &selectedFiles)
    self.uglySide.call(
        'ritual_ZN16QQuickFileDialog16setSelectedFilesERK5QListI4QUrlE',
        self._valueOf(selectedFiles),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFileDialog::QQuickFileDialog(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#QQuickFileDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFileDialog::QQuickFileDialog(QObject *parent)
    self._noteCreation(QQuickFileDialog, lambda: Rituals.call(
        'ritual_ZN16QQuickFileDialogC1EP7QObject',
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

  def resetOptions(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::resetOptions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#resetOptions
    """
    #  void QQuickFileDialog::resetOptions()
    self.uglySide.call('ritual_ZN16QQuickFileDialog12resetOptionsEv')

  def resetNameFilters(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::resetNameFilters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#resetNameFilters
    """
    #  void QQuickFileDialog::resetNameFilters()
    self.uglySide.call('ritual_ZN16QQuickFileDialog16resetNameFiltersEv')

  def resetDefaultSuffix(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::resetDefaultSuffix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#resetDefaultSuffix
    """
    #  void QQuickFileDialog::resetDefaultSuffix()
    self.uglySide.call('ritual_ZN16QQuickFileDialog18resetDefaultSuffixEv')

  def resetAcceptLabel(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::resetAcceptLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#resetAcceptLabel
    """
    #  void QQuickFileDialog::resetAcceptLabel()
    self.uglySide.call('ritual_ZN16QQuickFileDialog16resetAcceptLabelEv')

  def resetRejectLabel(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::resetRejectLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#resetRejectLabel
    """
    #  void QQuickFileDialog::resetRejectLabel()
    self.uglySide.call('ritual_ZN16QQuickFileDialog16resetRejectLabelEv')

  def fileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::fileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#fileModeChanged
    """
    #  void QQuickFileDialog::fileModeChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog15fileModeChangedEv')

  def selectedFileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::selectedFileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#selectedFileChanged
    """
    #  void QQuickFileDialog::selectedFileChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog19selectedFileChangedEv')

  def selectedFilesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::selectedFilesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#selectedFilesChanged
    """
    #  void QQuickFileDialog::selectedFilesChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog20selectedFilesChangedEv')

  def currentFileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::currentFileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#currentFileChanged
    """
    #  void QQuickFileDialog::currentFileChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog18currentFileChangedEv')

  def currentFilesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::currentFilesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#currentFilesChanged
    """
    #  void QQuickFileDialog::currentFilesChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog19currentFilesChangedEv')

  def currentFolderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::currentFolderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#currentFolderChanged
    """
    #  void QQuickFileDialog::currentFolderChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog20currentFolderChangedEv')

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#optionsChanged
    """
    #  void QQuickFileDialog::optionsChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog14optionsChangedEv')

  def nameFiltersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::nameFiltersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#nameFiltersChanged
    """
    #  void QQuickFileDialog::nameFiltersChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog18nameFiltersChangedEv')

  def defaultSuffixChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::defaultSuffixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#defaultSuffixChanged
    """
    #  void QQuickFileDialog::defaultSuffixChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog20defaultSuffixChangedEv')

  def acceptLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::acceptLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#acceptLabelChanged
    """
    #  void QQuickFileDialog::acceptLabelChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog18acceptLabelChangedEv')

  def rejectLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::rejectLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialog.html#rejectLabelChanged
    """
    #  void QQuickFileDialog::rejectLabelChanged()
    self.uglySide.call('ritual_ZN16QQuickFileDialog18rejectLabelChangedEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN16QQuickFileDialog8onCreateEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickFileDialog8onCreateEP21QPlatformDialogHelpe'
          'r')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN16QQuickFileDialog6onShowEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickFileDialog6onShowEP21QPlatformDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onHide(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::onHide(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#onHide

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialog::onHide(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN16QQuickFileDialog6onHideEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickFileDialog6onHideEP21QPlatformDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialog.html#accept
    """
    #  void QQuickFileDialog::accept()
    ritual = 'ritual_ZN16QQuickFileDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickFileDialog6acceptEv'
    self.uglySide.call(ritual)
