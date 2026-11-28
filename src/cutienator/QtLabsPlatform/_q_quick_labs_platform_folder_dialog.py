"""
QQuickLabsPlatformFolderDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfolderdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformFolderDialog to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickLabsPlatformDialog
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


class QQuickLabsPlatformFolderDialog(QQuickLabsPlatformDialog):
  """
  The cute side of Qt's QQuickLabsPlatformFolderDialog: a plain Python object
  standing in front of one C++ QQuickLabsPlatformFolderDialog.

  It is built on the cute 'QQuickLabsPlatformDialog', as Qt's
  QQuickLabsPlatformFolderDialog is built on Qt's QQuickLabsPlatformDialog,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformFolderDialog that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject',
  'qmlExtendedNamespace', 'folder', 'currentFolder', 'setCurrentFolder',
  'options', 'acceptLabel', 'rejectLabel', 'folderChanged',
  'currentFolderChanged', 'optionsChanged', 'acceptLabelChanged',
  'rejectLabelChanged', 'useNativeDialog', 'onCreate', 'onShow', 'accept'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformFolderDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformFolderDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformFolderDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  11 of the 31 functions Qt declares: 8 leans on
  'QQuickLabsPlatformFolderDialog; 2 not a gap; 1 leans on 'vtable for
  QQuickLabsPlatformFolderDialog', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformFolderDialog is created at the first use, not
    by 'QQuickLabsPlatformFolderDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformFolderDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformFolderDialog.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformFolderDialog that has no cute
    function yet, '__init__', 'resetAcceptLabel', 'resetOptions',
    'resetRejectLabel', 'setAcceptLabel', 'setFolder', 'setOptions',
    'setRejectLabel', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformFolderDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformFolderDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformFolderDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformFolderDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformFolderDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def folder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFolderDialog::folder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#folder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFolderDialog::folder() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog6folderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def currentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformFolderDialog::currentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#currentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformFolderDialog::currentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog13currentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def options(self) -> QFileDialogOptions.FileDialogOptions:
    """
    Calls Qt's 'QFileDialogOptions::FileDialogOptions
    QQuickLabsPlatformFolderDialog::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#options

    Returns
    -------

    QFileDialogOptions.FileDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFileDialogOptions::FileDialogOptions
    #      QQuickLabsPlatformFolderDialog::options() const
    return QFileDialogOptions.FileDialogOptions(self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog7optionsEv',
    ))

  def acceptLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFolderDialog::acceptLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#acceptLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFolderDialog::acceptLabel() const
    return self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog11acceptLabelEv',
    )

  def rejectLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFolderDialog::rejectLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#rejectLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFolderDialog::rejectLabel() const
    return self.uglySide.call(
        'ritual_ZNK30QQuickLabsPlatformFolderDialog11rejectLabelEv',
    )

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformFolderDialog::useNativeDialog()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html
    """
    #  bool QQuickLabsPlatformFolderDialog::useNativeDialog() const
    ritual = 'ritual_ZNK30QQuickLabsPlatformFolderDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickLabsPlatformFolderDialog15useNativeDialogE'
          'v')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setCurrentFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::setCurrentFolder(const
    QUrl &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickLabsPlatformFolderDialog::setCurrentFolder(const QUrl
    #      &folder)
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog16setCurrentFolderERK4QUr'
        'l',
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
    Qt's
    'QQuickLabsPlatformFolderDialog::QQuickLabsPlatformFolderDialog(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformFolderDialog', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformFolderDialog::QQuickLabsPlatformFolderDialog(QOb"
        "ject *parent)': leans on 'vtable for "
        "QQuickLabsPlatformFolderDialog', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def folderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::folderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#folderChanged
    """
    #  void QQuickLabsPlatformFolderDialog::folderChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog13folderChangedEv',
    )

  def currentFolderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::currentFolderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html
    """
    #  void QQuickLabsPlatformFolderDialog::currentFolderChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog20currentFolderChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#optionsChanged
    """
    #  void QQuickLabsPlatformFolderDialog::optionsChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog14optionsChangedEv',
    )

  def acceptLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::acceptLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html
    """
    #  void QQuickLabsPlatformFolderDialog::acceptLabelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog18acceptLabelChangedEv',
    )

  def rejectLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::rejectLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html
    """
    #  void QQuickLabsPlatformFolderDialog::rejectLabelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog18rejectLabelChangedEv',
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFolderDialog::onCreate(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFolderDialog::onCreate(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN30QQuickLabsPlatformFolderDialog8onCreateEP21QPlatformDia'
        'logHelper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFolderDialog::onShow(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFolderDialog::onShow(QPlatformDialogHelper
    #      *dialog)
    ritual = (
        'ritual_ZN30QQuickLabsPlatformFolderDialog6onShowEP21QPlatformDialo'
        'gHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickLabsPlatformFolderDialog6onShowEP21QPlatfor'
          'mDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFolderDialog::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfolderdialog.html#accept
    """
    #  void QQuickLabsPlatformFolderDialog::accept()
    self.uglySide.call('ritual_ZN30QQuickLabsPlatformFolderDialog6acceptEv')

  @staticmethod
  def resetAcceptLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::resetAcceptLabel()': leans on
    'QQuickLabsPlatformFolderDialog::acceptLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.resetAcceptLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFolderDialog::resetAcceptLabel()': leans on "
        "'QQuickLabsPlatformFolderDialog::acceptLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def resetOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::resetOptions()': leans on
    'QQuickLabsPlatformFolderDialog::optionsChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.resetOptions' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFolderDialog::resetOptions()': "
        "leans on 'QQuickLabsPlatformFolderDialog::optionsChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def resetRejectLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::resetRejectLabel()': leans on
    'QQuickLabsPlatformFolderDialog::rejectLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.resetRejectLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFolderDialog::resetRejectLabel()': leans on "
        "'QQuickLabsPlatformFolderDialog::rejectLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setAcceptLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::setAcceptLabel(const QString
    &label)': leans on
    'QQuickLabsPlatformFolderDialog::acceptLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.setAcceptLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFolderDialog::setAcceptLabel(const QString "
        "&label)': leans on "
        "'QQuickLabsPlatformFolderDialog::acceptLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setFolder(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::setFolder(const QUrl
    &folder)': leans on 'QQuickLabsPlatformFolderDialog::folderChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.setFolder' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFolderDialog::setFolder(const "
        "QUrl &folder)': leans on "
        "'QQuickLabsPlatformFolderDialog::folderChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformFolderDialog::setOptions(QFileDialogOptions::
    FileDialogOptions options)': leans on
    'QQuickLabsPlatformFolderDialog::optionsChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.setOptions' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformFolderDialog::setOptions(QFileDialogOptions::File"
        "DialogOptions options)': leans on "
        "'QQuickLabsPlatformFolderDialog::optionsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setRejectLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFolderDialog::setRejectLabel(const QString
    &label)': leans on
    'QQuickLabsPlatformFolderDialog::rejectLabelChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFolderDialog.setRejectLabel' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFolderDialog::setRejectLabel(const QString "
        "&label)': leans on "
        "'QQuickLabsPlatformFolderDialog::rejectLabelChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
