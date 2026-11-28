"""
QQuickFolderDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfolderdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QFileDialogOptions
from . import QQuickAbstractDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QQuickFolderDialog(QQuickAbstractDialog):
  """
  The cute side of Qt's QQuickFolderDialog: a plain Python object standing in
  front of one C++ QQuickFolderDialog.

  It is built on the cute 'QQuickAbstractDialog', as Qt's QQuickFolderDialog
  is built on Qt's QQuickAbstractDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFolderDialog that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'currentFolder', 'setCurrentFolder',
  'selectedFolder', 'setSelectedFolder', 'options', 'setOptions',
  'resetOptions', 'acceptLabel', 'setAcceptLabel', 'resetAcceptLabel',
  'rejectLabel', 'setRejectLabel', 'resetRejectLabel',
  'currentFolderChanged', 'selectedFolderChanged', 'optionsChanged',
  'acceptLabelChanged', 'rejectLabelChanged', 'useNativeDialog', 'onCreate',
  'onShow'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFolderDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFolderDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFolderDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFolderDialog is created at the first use, not by
    'QQuickFolderDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderDialog.
  - Qt tells when it has removed the C++ QQuickFolderDialog. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickFolderDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#tr

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
    #  QString QQuickFolderDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickFolderDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickFolderDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN18QQuickFolderDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFolderDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderDialog::currentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#currentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderDialog::currentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog13currentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderDialog::selectedFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#selectedFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderDialog::selectedFolder() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog14selectedFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def options(self) -> QFileDialogOptions.FileDialogOptions:
    """
    Calls Qt's 'QFileDialogOptions::FileDialogOptions
    QQuickFolderDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#options

    Returns
    -------

    QFileDialogOptions.FileDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFileDialogOptions::FileDialogOptions QQuickFolderDialog::options()
    #      const
    return QFileDialogOptions.FileDialogOptions(self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog7optionsEv',
    ))

  def acceptLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickFolderDialog::acceptLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#acceptLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFolderDialog::acceptLabel() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog11acceptLabelEv',
    )

  def rejectLabel(self) -> str:
    """
    Calls Qt's 'QString QQuickFolderDialog::rejectLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#rejectLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFolderDialog::rejectLabel() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickFolderDialog11rejectLabelEv',
    )

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#useNativeDialog
    """
    #  bool QQuickFolderDialog::useNativeDialog() const
    ritual = 'ritual_ZNK18QQuickFolderDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickFolderDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setCurrentFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::setCurrentFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#setCurrentFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialog::setCurrentFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog16setCurrentFolderERK4QUrl',
        self._valueOf(folder),
    )

  @overload(QUrl)
  def setSelectedFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::setSelectedFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#setSelectedFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialog::setSelectedFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog17setSelectedFolderERK4QUrl',
        self._valueOf(folder),
    )

  @overload(QFileDialogOptions.FileDialogOptions)
  def setOptions(
      self,
      options: QFileDialogOptions.FileDialogOptions,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialog::setOptions(QFileDialogOptions::FileDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#setOptions

    Parameters
    ----------

    options : QFileDialogOptions.FileDialogOptions
      Passed on as its number.
    """
    #  void QQuickFolderDialog::setOptions(QFileDialogOptions::
    #      FileDialogOptions options)
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog10setOptionsE6QFlagsIN18QFileDialogOp'
        'tions16FileDialogOptionEE',
        options.value,
    )

  @overload(str)
  def setAcceptLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::setAcceptLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#setAcceptLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFolderDialog::setAcceptLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog14setAcceptLabelERK7QString', label,
    )

  @overload(str)
  def setRejectLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::setRejectLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#setRejectLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFolderDialog::setRejectLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog14setRejectLabelERK7QString', label,
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
    'QQuickFolderDialog::QQuickFolderDialog(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#QQuickFolderDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFolderDialog::QQuickFolderDialog(QObject *parent)
    self._noteCreation(QQuickFolderDialog, lambda: Rituals.call(
        'ritual_ZN18QQuickFolderDialogC1EP7QObject',
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
    Calls Qt's 'void QQuickFolderDialog::resetOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#resetOptions
    """
    #  void QQuickFolderDialog::resetOptions()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog12resetOptionsEv')

  def resetAcceptLabel(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::resetAcceptLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#resetAcceptLabel
    """
    #  void QQuickFolderDialog::resetAcceptLabel()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog16resetAcceptLabelEv')

  def resetRejectLabel(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::resetRejectLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#resetRejectLabel
    """
    #  void QQuickFolderDialog::resetRejectLabel()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog16resetRejectLabelEv')

  def currentFolderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::currentFolderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#currentFolderChanged
    """
    #  void QQuickFolderDialog::currentFolderChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog20currentFolderChangedEv',
    )

  def selectedFolderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::selectedFolderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#selectedFolderChanged
    """
    #  void QQuickFolderDialog::selectedFolderChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickFolderDialog21selectedFolderChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#optionsChanged
    """
    #  void QQuickFolderDialog::optionsChanged()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog14optionsChangedEv')

  def acceptLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::acceptLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#acceptLabelChanged
    """
    #  void QQuickFolderDialog::acceptLabelChanged()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog18acceptLabelChangedEv')

  def rejectLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::rejectLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialog.html#rejectLabelChanged
    """
    #  void QQuickFolderDialog::rejectLabelChanged()
    self.uglySide.call('ritual_ZN18QQuickFolderDialog18rejectLabelChangedEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN18QQuickFolderDialog8onCreateEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickFolderDialog8onCreateEP21QPlatformDialogHel'
          'per')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFolderDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN18QQuickFolderDialog6onShowEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickFolderDialog6onShowEP21QPlatformDialogHelpe'
          'r')
    self.uglySide.call(ritual, self._addressOf(dialog))
