"""
QQuickLabsPlatformFileDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformFileDialog to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QQuickLabsPlatformDialog
from ..QtCore import QList, QStringList
from ..QtGui import QFileDialogOptions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QPlatformDialogHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformFileDialog(QQuickLabsPlatformDialog):
  """
  The cute side of Qt's QQuickLabsPlatformFileDialog: a plain Python object
  standing in front of one C++ QQuickLabsPlatformFileDialog.

  It is built on the cute 'QQuickLabsPlatformDialog', as Qt's
  QQuickLabsPlatformFileDialog is built on Qt's QQuickLabsPlatformDialog, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformFileDialog that has a ritual and
  that Python can call so far, 34 names in all: 'metaObject',
  'qmlExtendedNamespace', 'fileMode', 'file', 'files', 'currentFile',
  'setCurrentFile', 'currentFiles', 'setCurrentFiles', 'folder', 'setFolder',
  'options', 'nameFilters', 'defaultSuffix', 'acceptLabel', 'rejectLabel',
  'fileModeChanged', 'fileChanged', 'filesChanged', 'currentFileChanged',
  'currentFilesChanged', 'folderChanged', 'optionsChanged',
  'nameFiltersChanged', 'defaultSuffixChanged', 'acceptLabelChanged',
  'rejectLabelChanged', 'useNativeDialog', 'onCreate', 'onShow', 'onHide',
  'accept', 'addDefaultSuffix', 'addDefaultSuffixes'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformFileDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformFileDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformFileDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  18 of the 55 functions Qt declares: 14 leans on
  'QQuickLabsPlatformFileDialog; 2 not a gap; 1 leans on 'vtable for
  QQuickLabsPlatformFileDialog', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on 'vtable for
  QQuickLabsPlatformFileNameFilter', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformFileDialog is created at the first use, not by
    'QQuickLabsPlatformFileDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformFileDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformFileDialog. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformFileDialog that has no cute function
    yet, '__init__', 'resetAcceptLabel', 'resetDefaultSuffix',
    'resetNameFilters', 'resetOptions', 'resetRejectLabel',
    'selectedNameFilter', 'setAcceptLabel', 'setDefaultSuffix', 'setFile',
    'setFileMode', 'setFiles', 'setNameFilters', 'setOptions',
    'setRejectLabel', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickLabsPlatformFileDialog, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FileMode(CuteNum):
    """
    The enum 'QQuickLabsPlatformFileDialog::FileMode' of Qt, with the 3 names
    Qt gives in it.
    """

    OpenFile = Kee[int](0)
    OpenFiles = Kee[int](1)
    SaveFile = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformFileDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformFileDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformFileDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformFileDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformFileDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fileMode(self) -> FileMode:
    """
    Calls Qt's 'FileMode QQuickLabsPlatformFileDialog::fileMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#fileMode

    Returns
    -------

    FileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileMode(number)' gives.
    """
    #  FileMode QQuickLabsPlatformFileDialog::fileMode() const
    return QQuickLabsPlatformFileDialog.FileMode(self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog8fileModeEv',
    ))

  def file(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFileDialog::file() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#file

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFileDialog::file() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog4fileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def files(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickLabsPlatformFileDialog::files() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#files

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickLabsPlatformFileDialog::files() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog5filesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def currentFile(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFileDialog::currentFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#currentFile

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFileDialog::currentFile() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog11currentFileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def currentFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickLabsPlatformFileDialog::currentFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#currentFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickLabsPlatformFileDialog::currentFiles() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog12currentFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def folder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFileDialog::folder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#folder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFileDialog::folder() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog6folderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def options(self) -> QFileDialogOptions.FileDialogOptions:
    """
    Calls Qt's 'QFileDialogOptions::FileDialogOptions
    QQuickLabsPlatformFileDialog::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#options

    Returns
    -------

    QFileDialogOptions.FileDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFileDialogOptions::FileDialogOptions
    #      QQuickLabsPlatformFileDialog::options() const
    return QFileDialogOptions.FileDialogOptions(self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog7optionsEv',
    ))

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickLabsPlatformFileDialog::nameFilters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickLabsPlatformFileDialog::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def defaultSuffix(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFileDialog::defaultSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#defaultSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFileDialog::defaultSuffix() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog13defaultSuffixEv',
    )

  def acceptLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFileDialog::acceptLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#acceptLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFileDialog::acceptLabel() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog11acceptLabelEv',
    )

  def rejectLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFileDialog::rejectLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#rejectLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFileDialog::rejectLabel() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog11rejectLabelEv',
    )

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformFileDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#useNativeDialog
    """
    #  bool QQuickLabsPlatformFileDialog::useNativeDialog() const
    ritual = 'ritual_ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv')
    return self.uglySide.call(ritual)

  @overload(QUrl)
  def addDefaultSuffix(self, file: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFileDialog::addDefaultSuffix(const
    QUrl &file) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#addDefaultSuffix

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFileDialog::addDefaultSuffix(const QUrl &file)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog16addDefaultSuffixERK4QUrl',
        self._valueOf(file),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QList[QUrl])
  def addDefaultSuffixes(self, files: QList[QUrl]) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl>
    QQuickLabsPlatformFileDialog::addDefaultSuffixes(const QList<QUrl>
    &files) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html

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
    #  QList<QUrl> QQuickLabsPlatformFileDialog::addDefaultSuffixes(const
    #      QList<QUrl> &files) const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFileDialog18addDefaultSuffixesERK5QL'
        'istI4QUrlE',
        self._valueOf(files),
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setCurrentFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::setCurrentFile(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#setCurrentFile

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLabsPlatformFileDialog::setCurrentFile(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog14setCurrentFileERK4QUrl',
        self._valueOf(file),
    )

  @overload(QList[QUrl])
  def setCurrentFiles(self, files: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::setCurrentFiles(const
    QList<QUrl> &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#setCurrentFiles

    Parameters
    ----------

    files : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickLabsPlatformFileDialog::setCurrentFiles(const QList<QUrl>
    #      &files)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog15setCurrentFilesERK5QListI'
        '4QUrlE',
        self._valueOf(files),
    )

  @overload(QUrl)
  def setFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::setFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#setFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLabsPlatformFileDialog::setFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog9setFolderERK4QUrl',
        self._valueOf(folder),
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
    Qt's 'QQuickLabsPlatformFileDialog::QQuickLabsPlatformFileDialog(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformFileDialog', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickLabsPlatformFileDialog::QQuickLabsPlatformFileDialog(QObject"
        " *parent)': leans on 'vtable for QQuickLabsPlatformFileDialog', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def fileModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::fileModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#fileModeChanged
    """
    #  void QQuickLabsPlatformFileDialog::fileModeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog15fileModeChangedEv',
    )

  def fileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::fileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#fileChanged
    """
    #  void QQuickLabsPlatformFileDialog::fileChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog11fileChangedEv',
    )

  def filesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::filesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#filesChanged
    """
    #  void QQuickLabsPlatformFileDialog::filesChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog12filesChangedEv',
    )

  def currentFileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::currentFileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::currentFileChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog18currentFileChangedEv',
    )

  def currentFilesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::currentFilesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::currentFilesChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog19currentFilesChangedEv',
    )

  def folderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::folderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#folderChanged
    """
    #  void QQuickLabsPlatformFileDialog::folderChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog13folderChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#optionsChanged
    """
    #  void QQuickLabsPlatformFileDialog::optionsChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog14optionsChangedEv',
    )

  def nameFiltersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::nameFiltersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::nameFiltersChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog18nameFiltersChangedEv',
    )

  def defaultSuffixChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::defaultSuffixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::defaultSuffixChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog20defaultSuffixChangedEv',
    )

  def acceptLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::acceptLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::acceptLabelChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog18acceptLabelChangedEv',
    )

  def rejectLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::rejectLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html
    """
    #  void QQuickLabsPlatformFileDialog::rejectLabelChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog18rejectLabelChangedEv',
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFileDialog::onCreate(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFileDialog::onCreate(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog8onCreateEP21QPlatformDialo'
        'gHelper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFileDialog::onShow(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFileDialog::onShow(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog6onShowEP21QPlatformDialogH'
        'elper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onHide(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFileDialog::onHide(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#onHide

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFileDialog::onHide(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFileDialog6onHideEP21QPlatformDialogH'
        'elper',
        self._addressOf(dialog),
    )

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileDialog::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfiledialog.html#accept
    """
    #  void QQuickLabsPlatformFileDialog::accept()
    self.uglySide.call('ritual_ZN28QQuickLabsPlatformFileDialog6acceptEv')

  @staticmethod
  def resetAcceptLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::resetAcceptLabel()': leans on
    'QQuickLabsPlatformFileDialog::acceptLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.resetAcceptLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::resetAcceptLabel()': leans on "
        "'QQuickLabsPlatformFileDialog::acceptLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def resetDefaultSuffix(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::resetDefaultSuffix()': leans on
    'QQuickLabsPlatformFileDialog::defaultSuffixChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.resetDefaultSuffix' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::resetDefaultSuffix()': leans on "
        "'QQuickLabsPlatformFileDialog::defaultSuffixChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def resetNameFilters(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::resetNameFilters()': leans on
    'QQuickLabsPlatformFileDialog::nameFiltersChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.resetNameFilters' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::resetNameFilters()': leans on "
        "'QQuickLabsPlatformFileDialog::nameFiltersChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def resetOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::resetOptions()': leans on
    'QQuickLabsPlatformFileDialog::optionsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.resetOptions' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileDialog::resetOptions()': "
        "leans on 'QQuickLabsPlatformFileDialog::optionsChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resetRejectLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::resetRejectLabel()': leans on
    'QQuickLabsPlatformFileDialog::rejectLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.resetRejectLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::resetRejectLabel()': leans on "
        "'QQuickLabsPlatformFileDialog::rejectLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def selectedNameFilter(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformFileNameFilter
    *QQuickLabsPlatformFileDialog::selectedNameFilter() const': leans on
    'vtable for QQuickLabsPlatformFileNameFilter', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.selectedNameFilter' has no cute "
        "function yet. Qt's 'QQuickLabsPlatformFileNameFilter "
        "*QQuickLabsPlatformFileDialog::selectedNameFilter() const': leans "
        "on 'vtable for QQuickLabsPlatformFileNameFilter', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setAcceptLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setAcceptLabel(const QString
    &label)': leans on 'QQuickLabsPlatformFileDialog::acceptLabelChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setAcceptLabel' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileDialog::setAcceptLabel(const "
        "QString &label)': leans on "
        "'QQuickLabsPlatformFileDialog::acceptLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDefaultSuffix(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setDefaultSuffix(const QString
    &suffix)': leans on
    'QQuickLabsPlatformFileDialog::defaultSuffixChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setDefaultSuffix' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::setDefaultSuffix(const QString "
        "&suffix)': leans on "
        "'QQuickLabsPlatformFileDialog::defaultSuffixChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFile(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setFile(const QUrl &file)':
    leans on 'QQuickLabsPlatformFileDialog::fileChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setFile' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformFileDialog::setFile(const QUrl "
        "&file)': leans on 'QQuickLabsPlatformFileDialog::fileChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setFileMode(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setFileMode(FileMode fileMode)':
    leans on 'QQuickLabsPlatformFileDialog::fileModeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setFileMode' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileDialog::setFileMode(FileMode "
        "fileMode)': leans on "
        "'QQuickLabsPlatformFileDialog::fileModeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFiles(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setFiles(const QList<QUrl>
    &files)': leans on 'QQuickLabsPlatformFileDialog::fileChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setFiles' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformFileDialog::setFiles(const "
        "QList<QUrl> &files)': leans on "
        "'QQuickLabsPlatformFileDialog::fileChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setNameFilters(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setNameFilters(const QStringList
    &filters)': leans on
    'QQuickLabsPlatformFileDialog::nameFiltersChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setNameFilters' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileDialog::setNameFilters(const "
        "QStringList &filters)': leans on "
        "'QQuickLabsPlatformFileDialog::nameFiltersChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setOptions(QFileDialogOptions::
    FileDialogOptions options)': leans on
    'QQuickLabsPlatformFileDialog::optionsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setOptions' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformFileDialog::setOptions(QFileDialogOptions::FileDi"
        "alogOptions options)': leans on "
        "'QQuickLabsPlatformFileDialog::optionsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setRejectLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileDialog::setRejectLabel(const QString
    &label)': leans on 'QQuickLabsPlatformFileDialog::rejectLabelChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileDialog.setRejectLabel' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileDialog::setRejectLabel(const "
        "QString &label)': leans on "
        "'QQuickLabsPlatformFileDialog::rejectLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
