"""
QQuickFileDialogImplAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogImplAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickListView
  from . import QQuickFileDialogImplAttachedPrivate
  from . import QQuickFolderBreadcrumbBar, QQuickSideBar
  from ..QtQuickTemplates2 import QQuickComboBox, QQuickDialog
  from ..QtQuickTemplates2 import QQuickDialogButtonBox, QQuickLabel
  from ..QtQuickTemplates2 import QQuickTextField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickComboBox = WAIT['QQuickComboBox']
  QQuickDialog = WAIT['QQuickDialog']
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']
  QQuickFolderBreadcrumbBar = WAIT['QQuickFolderBreadcrumbBar']
  QQuickLabel = WAIT['QQuickLabel']
  QQuickListView = WAIT['QQuickListView']
  QQuickSideBar = WAIT['QQuickSideBar']
  QQuickTextField = WAIT['QQuickTextField']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogImplAttached(QObject):
  """
  The cute side of Qt's QQuickFileDialogImplAttached: a plain Python object
  standing in front of one C++ QQuickFileDialogImplAttached.

  It is built on the cute 'QObject', as Qt's QQuickFileDialogImplAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogImplAttached that has a ritual and
  that Python can call so far, 32 names in all: 'metaObject', 'tr',
  'buttonBox', 'setButtonBox', 'nameFiltersComboBox',
  'setNameFiltersComboBox', 'filterLabel', 'setFilterLabel',
  'selectedNameFilter', 'selectNameFilter', 'fileDialogListView',
  'setFileDialogListView', 'breadcrumbBar', 'setBreadcrumbBar',
  'fileNameLabel', 'setFileNameLabel', 'fileNameTextField',
  'setFileNameTextField', 'overwriteConfirmationDialog',
  'setOverwriteConfirmationDialog', 'sideBar', 'setSideBar',
  'buttonBoxChanged', 'nameFiltersComboBoxChanged', 'filterLabelChanged',
  'fileDialogListViewChanged', 'breadcrumbBarChanged',
  'fileNameLabelChanged', 'fileNameTextFieldChanged',
  'overwriteConfirmationDialogChanged', 'sideBarChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileDialogImplAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFileDialogImplAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickFileDialogImplAttachedPrivate
    *QQuickFileDialogImplAttached::d_func() const': takes in Python what
    'QQuickFileDialogImplAttachedPrivate
    *QQuickFileDialogImplAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFileDialogImplAttached is created at the first use, not by
    'QQuickFileDialogImplAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogImplAttached.
  - Qt tells when it has removed the C++ QQuickFileDialogImplAttached. Every
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
    Calls Qt's 'QString QQuickFileDialogImplAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#tr

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
    #  QString QQuickFileDialogImplAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuickFileDialogImplAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogImplAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialogImplAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialogImplAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonBox(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickFileDialogImplAttached::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#buttonBox

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickFileDialogImplAttached::buttonBox() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached9buttonBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  def nameFiltersComboBox(self) -> Optional[QQuickComboBox]:
    """
    Calls Qt's 'QQuickComboBox
    *QQuickFileDialogImplAttached::nameFiltersComboBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Returns
    -------

    Optional[QQuickComboBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickComboBox *QQuickFileDialogImplAttached::nameFiltersComboBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached19nameFiltersComboBoxEv',
    )
    from ..QtQuickTemplates2 import QQuickComboBox
    return QQuickComboBox._cuteAt(address)

  def filterLabel(self) -> Optional[QQuickLabel]:
    """
    Calls Qt's 'QQuickLabel *QQuickFileDialogImplAttached::filterLabel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#filterLabel

    Returns
    -------

    Optional[QQuickLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabel *QQuickFileDialogImplAttached::filterLabel() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached11filterLabelEv',
    )
    from ..QtQuickTemplates2 import QQuickLabel
    return QQuickLabel._cuteAt(address)

  def selectedNameFilter(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialogImplAttached::selectedNameFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialogImplAttached::selectedNameFilter() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached18selectedNameFilterEv',
    )

  def fileDialogListView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView
    *QQuickFileDialogImplAttached::fileDialogListView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QQuickFileDialogImplAttached::fileDialogListView()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached18fileDialogListViewEv',
    )
    from ..QtQuick import QQuickListView
    return QQuickListView._cuteAt(address)

  def breadcrumbBar(self) -> Optional[QQuickFolderBreadcrumbBar]:
    """
    Calls Qt's 'QQuickFolderBreadcrumbBar
    *QQuickFileDialogImplAttached::breadcrumbBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#breadcrumbBar

    Returns
    -------

    Optional[QQuickFolderBreadcrumbBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderBreadcrumbBar
    #      *QQuickFileDialogImplAttached::breadcrumbBar() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached13breadcrumbBarEv',
    )
    from . import QQuickFolderBreadcrumbBar
    return QQuickFolderBreadcrumbBar._cuteAt(address)

  def fileNameLabel(self) -> Optional[QQuickLabel]:
    """
    Calls Qt's 'QQuickLabel *QQuickFileDialogImplAttached::fileNameLabel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#fileNameLabel

    Returns
    -------

    Optional[QQuickLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabel *QQuickFileDialogImplAttached::fileNameLabel() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached13fileNameLabelEv',
    )
    from ..QtQuickTemplates2 import QQuickLabel
    return QQuickLabel._cuteAt(address)

  def fileNameTextField(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField
    *QQuickFileDialogImplAttached::fileNameTextField() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickFileDialogImplAttached::fileNameTextField()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached17fileNameTextFieldEv',
    )
    from ..QtQuickTemplates2 import QQuickTextField
    return QQuickTextField._cuteAt(address)

  def overwriteConfirmationDialog(self) -> Optional[QQuickDialog]:
    """
    Calls Qt's 'QQuickDialog
    *QQuickFileDialogImplAttached::overwriteConfirmationDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Returns
    -------

    Optional[QQuickDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialog
    #      *QQuickFileDialogImplAttached::overwriteConfirmationDialog() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached27overwriteConfirmationDia'
        'logEv',
    )
    from ..QtQuickTemplates2 import QQuickDialog
    return QQuickDialog._cuteAt(address)

  def sideBar(self) -> Optional[QQuickSideBar]:
    """
    Calls Qt's 'QQuickSideBar *QQuickFileDialogImplAttached::sideBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#sideBar

    Returns
    -------

    Optional[QQuickSideBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSideBar *QQuickFileDialogImplAttached::sideBar() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFileDialogImplAttached7sideBarEv',
    )
    from . import QQuickSideBar
    return QQuickSideBar._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def setButtonBox(self, buttonBox: Optional[QQuickDialogButtonBox]) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    *buttonBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#setButtonBox

    Parameters
    ----------

    buttonBox : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setButtonBox(QQuickDialogButtonBox
    #      *buttonBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached12setButtonBoxEP21QQuickDia'
        'logButtonBox',
        self._addressOf(buttonBox),
    )

  @overload(QQuickComboBox)
  @overload(NoneType)
  def setNameFiltersComboBox(
      self,
      nameFiltersComboBox: Optional[QQuickComboBox],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setNameFiltersComboBox(QQuickComboBox
    *nameFiltersComboBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Parameters
    ----------

    nameFiltersComboBox : Optional[QQuickComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setNameFiltersComboBox(
    #      QQuickComboBox *nameFiltersComboBox)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached22setNameFiltersComboBoxEP1'
        '4QQuickComboBox',
        self._addressOf(nameFiltersComboBox),
    )

  @overload(QQuickLabel)
  @overload(NoneType)
  def setFilterLabel(self, label: Optional[QQuickLabel]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::setFilterLabel(QQuickLabel
    *label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#setFilterLabel

    Parameters
    ----------

    label : Optional[QQuickLabel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setFilterLabel(QQuickLabel *label)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached14setFilterLabelEP11QQuickL'
        'abel',
        self._addressOf(label),
    )

  @overload(QQuickListView)
  @overload(NoneType)
  def setFileDialogListView(
      self,
      fileDialogListView: Optional[QQuickListView],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setFileDialogListView(QQuickListView
    *fileDialogListView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Parameters
    ----------

    fileDialogListView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickFileDialogImplAttached::setFileDialogListView(QQuickListView
    #      *fileDialogListView)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached21setFileDialogListViewEP14'
        'QQuickListView',
        self._addressOf(fileDialogListView),
    )

  @overload(QQuickFolderBreadcrumbBar)
  @overload(NoneType)
  def setBreadcrumbBar(
      self,
      breadcrumbBar: Optional[QQuickFolderBreadcrumbBar],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setBreadcrumbBar(QQuickFolderBreadcrumbBar
    *breadcrumbBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#setBreadcrumbBar

    Parameters
    ----------

    breadcrumbBar : Optional[QQuickFolderBreadcrumbBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setBreadcrumbBar(
    #      QQuickFolderBreadcrumbBar *breadcrumbBar)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached16setBreadcrumbBarEP25QQuic'
        'kFolderBreadcrumbBar',
        self._addressOf(breadcrumbBar),
    )

  @overload(QQuickLabel)
  @overload(NoneType)
  def setFileNameLabel(self, fileNameLabel: Optional[QQuickLabel]) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setFileNameLabel(QQuickLabel
    *fileNameLabel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#setFileNameLabel

    Parameters
    ----------

    fileNameLabel : Optional[QQuickLabel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setFileNameLabel(QQuickLabel
    #      *fileNameLabel)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached16setFileNameLabelEP11QQuic'
        'kLabel',
        self._addressOf(fileNameLabel),
    )

  @overload(QQuickTextField)
  @overload(NoneType)
  def setFileNameTextField(
      self,
      fileNameTextField: Optional[QQuickTextField],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setFileNameTextField(QQuickTextField
    *fileNameTextField)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Parameters
    ----------

    fileNameTextField : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickFileDialogImplAttached::setFileNameTextField(QQuickTextField
    #      *fileNameTextField)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached20setFileNameTextFieldEP15Q'
        'QuickTextField',
        self._addressOf(fileNameTextField),
    )

  @overload(QQuickDialog)
  @overload(NoneType)
  def setOverwriteConfirmationDialog(
      self,
      dialog: Optional[QQuickDialog],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::setOverwriteConfirmationDialog(QQuickDialog
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Parameters
    ----------

    dialog : Optional[QQuickDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setOverwriteConfirmationDialog(
    #      QQuickDialog *dialog)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached30setOverwriteConfirmationD'
        'ialogEP12QQuickDialog',
        self._addressOf(dialog),
    )

  @overload(QQuickSideBar)
  @overload(NoneType)
  def setSideBar(self, sideBar: Optional[QQuickSideBar]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::setSideBar(QQuickSideBar
    *sideBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#setSideBar

    Parameters
    ----------

    sideBar : Optional[QQuickSideBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogImplAttached::setSideBar(QQuickSideBar *sideBar)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached10setSideBarEP13QQuickSideB'
        'ar',
        self._addressOf(sideBar),
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
    'QQuickFileDialogImplAttached::QQuickFileDialogImplAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFileDialogImplAttached::QQuickFileDialogImplAttached(QObject
    #      *parent)
    self._noteCreation(QQuickFileDialogImplAttached, lambda: Rituals.call(
        'ritual_ZN28QQuickFileDialogImplAttachedC1EP7QObject',
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

  @overload(str)
  def selectNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::selectNameFilter(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#selectNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImplAttached::selectNameFilter(const QString
    #      &filter)
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached16selectNameFilterERK7QStri'
        'ng',
        filter,
    )

  def buttonBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::buttonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#buttonBoxChanged
    """
    #  void QQuickFileDialogImplAttached::buttonBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached16buttonBoxChangedEv',
    )

  def nameFiltersComboBoxChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::nameFiltersComboBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::nameFiltersComboBoxChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached26nameFiltersComboBoxChange'
        'dEv',
    )

  def filterLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::filterLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::filterLabelChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached18filterLabelChangedEv',
    )

  def fileDialogListViewChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::fileDialogListViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::fileDialogListViewChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached25fileDialogListViewChanged'
        'Ev',
    )

  def breadcrumbBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::breadcrumbBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::breadcrumbBarChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached20breadcrumbBarChangedEv',
    )

  def fileNameLabelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::fileNameLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::fileNameLabelChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached20fileNameLabelChangedEv',
    )

  def fileNameTextFieldChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::fileNameTextFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void QQuickFileDialogImplAttached::fileNameTextFieldChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached24fileNameTextFieldChangedE'
        'v',
    )

  def overwriteConfirmationDialogChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttached::overwriteConfirmationDialogChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html
    """
    #  void
    #      QQuickFileDialogImplAttached::overwriteConfirmationDialogChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached34overwriteConfirmationDial'
        'ogChangedEv',
    )

  def sideBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImplAttached::sideBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#sideBarChanged
    """
    #  void QQuickFileDialogImplAttached::sideBarChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached14sideBarChangedEv',
    )

  def d_func(self) -> Optional[QQuickFileDialogImplAttachedPrivate]:
    """
    Calls Qt's 'QQuickFileDialogImplAttachedPrivate
    *QQuickFileDialogImplAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattached.html#d_func

    Returns
    -------

    Optional[QQuickFileDialogImplAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplAttachedPrivate
    #      *QQuickFileDialogImplAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickFileDialogImplAttached6d_funcEv',
    )
    from . import QQuickFileDialogImplAttachedPrivate
    return QQuickFileDialogImplAttachedPrivate._cuteAt(address)
