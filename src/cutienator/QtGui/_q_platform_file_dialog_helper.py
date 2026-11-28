"""
QPlatformFileDialogHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformFileDialogHelper(QPlatformDialogHelper):
  """
  The cute side of Qt's QPlatformFileDialogHelper: a plain Python object
  standing in front of one C++ QPlatformFileDialogHelper.

  It is built on the cute 'QPlatformDialogHelper', as Qt's
  QPlatformFileDialogHelper is built on Qt's QPlatformDialogHelper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformFileDialogHelper that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'defaultNameFilterDisables', 'setDirectory', 'directory', 'selectFile',
  'selectedFiles', 'setFilter', 'selectMimeTypeFilter', 'selectNameFilter',
  'selectedMimeTypeFilter', 'selectedNameFilter', 'isSupportedUrl',
  'cleanFilterList', 'fileSelected', 'filesSelected', 'currentChanged',
  'directoryEntered', 'filterSelected'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformFileDialogHelper::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformFileDialogHelper::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSharedPointer<QFileDialogOptions>
    &QPlatformFileDialogHelper::options() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QPlatformFileDialogHelper::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformFileDialogHelper is created at the first use, not by
    'QPlatformFileDialogHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformFileDialogHelper.
  - Qt tells when it has removed the C++ QPlatformFileDialogHelper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformFileDialogHelper that has no cute function
    yet, 'options', 'setOptions', holds a function that raises
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
    Calls Qt's 'QString QPlatformFileDialogHelper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#tr

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
    #  QString QPlatformFileDialogHelper::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QPlatformFileDialogHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def cleanFilterList(filter: str) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformFileDialogHelper::cleanFilterList(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#cleanFilterList

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformFileDialogHelper::cleanFilterList(const QString
    #      &filter)
    address = Rituals.call(
        'ritual_ZN25QPlatformFileDialogHelper15cleanFilterListERK7QString',
        filter,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformFileDialogHelper'

  #  The functions Qt calls itself that QPlatformFileDialogHelper is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'selectedFiles': (
          'QList<QUrl> QPlatformFileDialogHelper::selectedFiles() const',
      ),
  }

  #  The functions Qt calls itself that QPlatformFileDialogHelper is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'defaultNameFilterDisables': (
          ('_ZNK25QPlatformFileDialogHelper25defaultNameFilterDisablesEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setDirectory': (
          ('_ZN25QPlatformFileDialogHelper12setDirectoryERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'directory': (
          ('_ZNK25QPlatformFileDialogHelper9directoryEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'selectFile': (
          ('_ZN25QPlatformFileDialogHelper10selectFileERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'setFilter': (
          ('_ZN25QPlatformFileDialogHelper9setFilterEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'selectMimeTypeFilter': (
          ('_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'selectNameFilter': (
          ('_ZN25QPlatformFileDialogHelper16selectNameFilterERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'selectedMimeTypeFilter': (
          ('_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilterEv',
           ('address', 'text', ''),
           ()),
      ),
      'selectedNameFilter': (
          ('_ZNK25QPlatformFileDialogHelper18selectedNameFilterEv',
           ('address', 'text', ''),
           ()),
      ),
      'isSupportedUrl': (
          ('_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
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
    Calls Qt's 'const QMetaObject *QPlatformFileDialogHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformFileDialogHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformFileDialogHelper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultNameFilterDisables(self) -> bool:
    """
    Calls Qt's 'bool QPlatformFileDialogHelper::defaultNameFilterDisables()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html
    """
    #  bool QPlatformFileDialogHelper::defaultNameFilterDisables() const
    return self.uglySide.call(
        'ritual_ZNK25QPlatformFileDialogHelper25defaultNameFilterDisablesEv',
    )

  def directory(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlatformFileDialogHelper::directory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#directory

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlatformFileDialogHelper::directory() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformFileDialogHelper9directoryEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QPlatformFileDialogHelper::selectedFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#selectedFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QPlatformFileDialogHelper::selectedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformFileDialogHelper13selectedFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def selectedMimeTypeFilter(self) -> str:
    """
    Calls Qt's 'QString QPlatformFileDialogHelper::selectedMimeTypeFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformFileDialogHelper::selectedMimeTypeFilter() const
    ritual = (
        'ritual_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilterEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilte'
          'rEv')
    return self.uglySide.call(ritual)

  def selectedNameFilter(self) -> str:
    """
    Calls Qt's 'QString QPlatformFileDialogHelper::selectedNameFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#selectedNameFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformFileDialogHelper::selectedNameFilter() const
    return self.uglySide.call(
        'ritual_ZNK25QPlatformFileDialogHelper18selectedNameFilterEv',
    )

  @overload(QUrl)
  def isSupportedUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QPlatformFileDialogHelper::isSupportedUrl(const QUrl
    &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#isSupportedUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QPlatformFileDialogHelper::isSupportedUrl(const QUrl &url) const
    ritual = 'ritual_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUr'
          'l')
    return self.uglySide.call(ritual, self._valueOf(url))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setDirectory(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::setDirectory(const QUrl
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#setDirectory

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformFileDialogHelper::setDirectory(const QUrl &directory)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper12setDirectoryERK4QUrl',
        self._valueOf(directory),
    )

  def setFilter(self) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::setFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#setFilter
    """
    #  void QPlatformFileDialogHelper::setFilter()
    self.uglySide.call('ritual_ZN25QPlatformFileDialogHelper9setFilterEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QUrl)
  def selectFile(self, filename: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::selectFile(const QUrl
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#selectFile

    Parameters
    ----------

    filename : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformFileDialogHelper::selectFile(const QUrl &filename)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper10selectFileERK4QUrl',
        self._valueOf(filename),
    )

  @overload(str)
  def selectMimeTypeFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::selectMimeTypeFilter(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFileDialogHelper::selectMimeTypeFilter(const QString
    #      &filter)
    ritual = (
        'ritual_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterERK7QStr'
        'ing')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterER'
          'K7QString')
    self.uglySide.call(ritual, filter)

  @overload(str)
  def selectNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::selectNameFilter(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#selectNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFileDialogHelper::selectNameFilter(const QString
    #      &filter)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper16selectNameFilterERK7QString',
        filter,
    )

  @overload(QUrl)
  def fileSelected(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::fileSelected(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#fileSelected

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformFileDialogHelper::fileSelected(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper12fileSelectedERK4QUrl',
        self._valueOf(file),
    )

  @overload(QList[QUrl])
  def filesSelected(self, files: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::filesSelected(const
    QList<QUrl> &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#filesSelected

    Parameters
    ----------

    files : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlatformFileDialogHelper::filesSelected(const QList<QUrl>
    #      &files)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper13filesSelectedERK5QListI4QUrl'
        'E',
        self._valueOf(files),
    )

  @overload(QUrl)
  def currentChanged(self, path: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::currentChanged(const QUrl
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#currentChanged

    Parameters
    ----------

    path : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformFileDialogHelper::currentChanged(const QUrl &path)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper14currentChangedERK4QUrl',
        self._valueOf(path),
    )

  @overload(QUrl)
  def directoryEntered(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::directoryEntered(const QUrl
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#directoryEntered

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformFileDialogHelper::directoryEntered(const QUrl
    #      &directory)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper16directoryEnteredERK4QUrl',
        self._valueOf(directory),
    )

  @overload(str)
  def filterSelected(self, filter: str) -> None:
    """
    Calls Qt's 'void QPlatformFileDialogHelper::filterSelected(const QString
    &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfiledialoghelper.html#filterSelected

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformFileDialogHelper::filterSelected(const QString &filter)
    self.uglySide.call(
        'ritual_ZN25QPlatformFileDialogHelper14filterSelectedERK7QString',
        filter,
    )

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'const QSharedPointer<QFileDialogOptions>
    &QPlatformFileDialogHelper::options() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformFileDialogHelper.options' has no cute function yet. Qt's "
        "'const QSharedPointer<QFileDialogOptions> "
        "&QPlatformFileDialogHelper::options() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QPlatformFileDialogHelper::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformFileDialogHelper.setOptions' has no cute function yet. "
        "Qt's 'void QPlatformFileDialogHelper::setOptions(const "
        "QSharedPointer<QFileDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")
