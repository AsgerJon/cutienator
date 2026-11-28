"""
QQuickPlatformFolderDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfolderdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPlatformFolderDialog to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QPlatformFileDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QWindow
  from . import QQuickFolderDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPlatformFolderDialog(QPlatformFileDialogHelper):
  """
  The cute side of Qt's QQuickPlatformFolderDialog: a plain Python object
  standing in front of one C++ QQuickPlatformFolderDialog.

  It is built on the cute 'QPlatformFileDialogHelper', as Qt's
  QQuickPlatformFolderDialog is built on Qt's QPlatformFileDialogHelper, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPlatformFolderDialog that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'isValid', 'defaultNameFilterDisables', 'setDirectory', 'directory',
  'selectFile', 'selectedFiles', 'setFilter', 'selectNameFilter',
  'selectedNameFilter', 'exec', 'show', 'hide', 'dialog'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPlatformFolderDialog::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickPlatformFolderDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPlatformFolderDialog::~QQuickPlatformFolderDialog()': the
    destructor: Python never removes a C++ QQuickPlatformFolderDialog.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPlatformFolderDialog is created at the first use, not by
    'QQuickPlatformFolderDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPlatformFolderDialog.
  - Qt tells when it has removed the C++ QQuickPlatformFolderDialog. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickPlatformFolderDialog::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#tr

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
    #  QString QQuickPlatformFolderDialog::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickPlatformFolderDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPlatformFolderDialog'

  #  A C++ QQuickPlatformFolderDialog Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPlatformFolderDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPlatformFolderDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPlatformFolderDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPlatformFolderDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformFolderDialog::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#isValid
    """
    #  bool QQuickPlatformFolderDialog::isValid() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickPlatformFolderDialog7isValidEv',
    )

  def defaultNameFilterDisables(self) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformFolderDialog::defaultNameFilterDisables()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html
    """
    #  bool QQuickPlatformFolderDialog::defaultNameFilterDisables() const
    ritual = (
        'ritual_ZNK26QQuickPlatformFolderDialog25defaultNameFilterDisablesE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QQuickPlatformFolderDialog25defaultNameFilterDis'
          'ablesEv')
    return self.uglySide.call(ritual)

  def directory(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickPlatformFolderDialog::directory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#directory

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickPlatformFolderDialog::directory() const
    ritual = 'ritual_ZNK26QQuickPlatformFolderDialog9directoryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QQuickPlatformFolderDialog9directoryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFiles(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickPlatformFolderDialog::selectedFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#selectedFiles

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickPlatformFolderDialog::selectedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPlatformFolderDialog13selectedFilesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def selectedNameFilter(self) -> str:
    """
    Calls Qt's 'QString QQuickPlatformFolderDialog::selectedNameFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#selectedNameFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPlatformFolderDialog::selectedNameFilter() const
    ritual = 'ritual_ZNK26QQuickPlatformFolderDialog18selectedNameFilterEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QQuickPlatformFolderDialog18selectedNameFilterEv')
    return self.uglySide.call(ritual)

  def dialog(self) -> Optional[QQuickFolderDialogImpl]:
    """
    Calls Qt's 'QQuickFolderDialogImpl *QQuickPlatformFolderDialog::dialog()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#dialog

    Returns
    -------

    Optional[QQuickFolderDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImpl *QQuickPlatformFolderDialog::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPlatformFolderDialog6dialogEv',
    )
    from . import QQuickFolderDialogImpl
    return QQuickFolderDialogImpl._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setDirectory(self, directory: QUrl) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::setDirectory(const QUrl
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#setDirectory

    Parameters
    ----------

    directory : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickPlatformFolderDialog::setDirectory(const QUrl &directory)
    ritual = 'ritual_ZN26QQuickPlatformFolderDialog12setDirectoryERK4QUrl'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickPlatformFolderDialog12setDirectoryERK4QUrl')
    self.uglySide.call(ritual, self._valueOf(directory))

  def setFilter(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::setFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#setFilter
    """
    #  void QQuickPlatformFolderDialog::setFilter()
    ritual = 'ritual_ZN26QQuickPlatformFolderDialog9setFilterEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickPlatformFolderDialog9setFilterEv'
    self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPlatformFolderDialog::QQuickPlatformFolderDialog(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPlatformFolderDialog::QQuickPlatformFolderDialog(QObject
    #      *parent)
    self._noteCreation(QQuickPlatformFolderDialog, lambda: Rituals.call(
        'ritual_ZN26QQuickPlatformFolderDialogC1EP7QObject',
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

  @overload(QUrl)
  def selectFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::selectFile(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#selectFile

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickPlatformFolderDialog::selectFile(const QUrl &file)
    ritual = 'ritual_ZN26QQuickPlatformFolderDialog10selectFileERK4QUrl'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickPlatformFolderDialog10selectFileERK4QUrl')
    self.uglySide.call(ritual, self._valueOf(file))

  @overload(str)
  def selectNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::selectNameFilter(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#selectNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPlatformFolderDialog::selectNameFilter(const QString
    #      &filter)
    ritual = (
        'ritual_ZN26QQuickPlatformFolderDialog16selectNameFilterERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickPlatformFolderDialog16selectNameFilterERK7Q'
          'String')
    self.uglySide.call(ritual, filter)

  def exec(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::exec()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#exec
    """
    #  void QQuickPlatformFolderDialog::exec()
    ritual = 'ritual_ZN26QQuickPlatformFolderDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickPlatformFolderDialog4execEv'
    self.uglySide.call(ritual)

  @overload(Qt.WindowFlags, Qt.WindowModality, QWindow)
  @overload(Qt.WindowFlags, Qt.WindowModality, NoneType)
  def show(
      self,
      flags: Qt.WindowFlags,
      modality: Qt.WindowModality,
      parent: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformFolderDialog::show(Qt::WindowFlags flags,
    Qt::WindowModality modality, QWindow *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#show

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.

    modality : Qt.WindowModality
      Passed on as its number.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPlatformFolderDialog::show(Qt::WindowFlags flags,
    #      Qt::WindowModality modality, QWindow *parent)
    ritual = (
        'ritual_ZN26QQuickPlatformFolderDialog4showE6QFlagsIN2Qt10WindowTyp'
        'eEENS1_14WindowModalityEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickPlatformFolderDialog4showE6QFlagsIN2Qt10Win'
          'dowTypeEENS1_14WindowModalityEP7QWindow')
    return self.uglySide.call(
        ritual, flags.value, modality.value, self._addressOf(parent),
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformFolderDialog::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfolderdialog.html#hide
    """
    #  void QQuickPlatformFolderDialog::hide()
    ritual = 'ritual_ZN26QQuickPlatformFolderDialog4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickPlatformFolderDialog4hideEv'
    self.uglySide.call(ritual)
