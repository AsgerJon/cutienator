"""
qdesigner_internal::NewFormWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/newformwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::NewFormWidget to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget
from . import QDesignerNewFormWidgetInterface, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize, QString
  from ..QtGui import QPixmap
  from ..QtWidgets import QTreeWidgetItem
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QSize = WAIT['QSize']
  QString = WAIT['QString']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class NewFormWidget(QDesignerNewFormWidgetInterface):
  """
  The cute side of Qt's qdesigner_internal::NewFormWidget: a plain Python
  object standing in front of one C++ qdesigner_internal::NewFormWidget.

  It is built on the cute 'QDesignerNewFormWidgetInterface', as Qt's
  qdesigner_internal::NewFormWidget is built on Qt's
  QDesignerNewFormWidgetInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::NewFormWidget that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'hasCurrentTemplate', 'currentTemplate', 'isEmbeddedGroupBoxVisible',
  'setEmbeddedGroupBoxVisible', 'treeWidgetItemActivated',
  'treeWidgetCurrentItemChanged', 'treeWidgetItemPressed',
  'slotDeviceProfileIndexChanged', 'formPreviewPixmap', 'itemToTemplate',
  'currentTemplateI', 'templateSize', 'setTemplateSize', 'profileComboIndex',
  'currentDeviceProfile', 'showCurrentItemPixmap'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::NewFormWidget::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::NewFormWidget::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::NewFormWidget::~NewFormWidget()': the
    destructor: Python never removes a C++ qdesigner_internal::NewFormWidget.
  - Qt's 'QImage
    qdesigner_internal::NewFormWidget::grabForm(QDesignerFormEditorInterface
    *core, QIODevice &file, const QString &workingDir, const
    qdesigner_internal::DeviceProfile &dp)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QPixmap
    qdesigner_internal::NewFormWidget::formPreviewPixmap(QIODevice &file,
    const QString &workingDir) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  8 of the 33 functions Qt declares: 4 forbidden; 2 not a gap; 2 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::NewFormWidget is created at the first use,
    not by 'qdesigner_internal::NewFormWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::NewFormWidget.
  - Qt tells when it has removed the C++ qdesigner_internal::NewFormWidget.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::NewFormWidget that has no cute
    function yet, 'grabForm', 'loadFrom', holds a function that raises
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
    Calls Qt's 'QString qdesigner_internal::NewFormWidget::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html#tr

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
    #  QString qdesigner_internal::NewFormWidget::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::NewFormWidget'

  #  A C++ qdesigner_internal::NewFormWidget Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_NewFormWidget'

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
    *qdesigner_internal::NewFormWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::NewFormWidget::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasCurrentTemplate(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::NewFormWidget::hasCurrentTemplate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html
    """
    #  bool qdesigner_internal::NewFormWidget::hasCurrentTemplate() const
    ritual = (
        'ritual_ZNK18qdesigner_internal13NewFormWidget18hasCurrentTemplateE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal13NewFormWidget18hasCurrentTem'
          'plateEv')
    return self.uglySide.call(ritual)

  def isEmbeddedGroupBoxVisible(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::NewFormWidget::isEmbeddedGroupBoxVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html
    """
    #  bool qdesigner_internal::NewFormWidget::isEmbeddedGroupBoxVisible()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget25isEmbeddedGroupBoxV'
        'isibleEv',
    )

  @overload(str)
  def formPreviewPixmap(self, fileName: str) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::NewFormWidget::formPreviewPixmap(const QString
    &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::NewFormWidget::formPreviewPixmap(const
    #      QString &fileName) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget17formPreviewPixmapER'
        'K7QString',
        fileName,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def formPreviewPixmap(self, item: Optional[QTreeWidgetItem]) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::NewFormWidget::formPreviewPixmap(const
    QTreeWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::NewFormWidget::formPreviewPixmap(const
    #      QTreeWidgetItem *item)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget17formPreviewPixmapEPK'
        '15QTreeWidgetItem',
        self._addressOf(item),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QTreeWidgetItem, QString)
  @overload(QTreeWidgetItem, NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def itemToTemplate(
      self,
      item: Optional[QTreeWidgetItem],
      errorMessage: Optional[QString],
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::NewFormWidget::itemToTemplate(const QTreeWidgetItem
    *item, QString *errorMessage) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::NewFormWidget::itemToTemplate(const
    #      QTreeWidgetItem *item, QString *errorMessage) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget14itemToTemplateEPK15'
        'QTreeWidgetItemP7QString',
        self._addressOf(item), self._addressOf(errorMessage),
    )

  def templateSize(self) -> QSize:
    """
    Calls Qt's 'QSize qdesigner_internal::NewFormWidget::templateSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html#templateSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize qdesigner_internal::NewFormWidget::templateSize() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget12templateSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def profileComboIndex(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::NewFormWidget::profileComboIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html
    """
    #  int qdesigner_internal::NewFormWidget::profileComboIndex() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget17profileComboIndexEv',
    )

  def currentDeviceProfile(self) -> qdesigner_internal.DeviceProfile:
    """
    Calls Qt's 'qdesigner_internal::DeviceProfile
    qdesigner_internal::NewFormWidget::currentDeviceProfile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Returns
    -------

    qdesigner_internal.DeviceProfile
      A new cute qdesigner_internal::DeviceProfile around the copy Qt gave
      back. Python owns it.
    """
    #  qdesigner_internal::DeviceProfile
    #      qdesigner_internal::NewFormWidget::currentDeviceProfile() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13NewFormWidget20currentDeviceProfil'
        'eEv',
    )
    return qdesigner_internal.DeviceProfile._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEmbeddedGroupBoxVisible(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidget::setEmbeddedGroupBoxVisible(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void
    #      qdesigner_internal::NewFormWidget::setEmbeddedGroupBoxVisible(bool
    #      v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget26setEmbeddedGroupBoxV'
        'isibleEb',
        v,
    )

  @overload(QSize)
  def setTemplateSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewFormWidget::setTemplateSize(const
    QSize &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void qdesigner_internal::NewFormWidget::setTemplateSize(const QSize
    #      &s)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget15setTemplateSizeERK5Q'
        'Size',
        self._valueOf(s),
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

  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::NewFormWidget::NewFormWidget(
    QDesignerFormEditorInterface *core, QWidget *parentWidget)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::NewFormWidget::NewFormWidget(
    #      QDesignerFormEditorInterface *core, QWidget *parentWidget)
    self._noteCreation(NewFormWidget, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal13NewFormWidgetC1EP28QDesignerFormEdi'
        'torInterfaceP7QWidget',
        self._addressOf(core), self._addressOf(parentWidget),
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

  @overload()
  @overload(QString)
  @overload(NoneType)
  def currentTemplate(self, errorMessage: Optional[QString] = None) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::NewFormWidget::currentTemplate(QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::NewFormWidget::currentTemplate(QString
    #      *errorMessage)
    ritual = (
        'ritual_ZN18qdesigner_internal13NewFormWidget15currentTemplateEP7QS'
        'tring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal13NewFormWidget15currentTemplat'
          'eEP7QString')
    return self.uglySide.call(ritual, self._addressOf(errorMessage))

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def treeWidgetItemActivated(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidget::treeWidgetItemActivated(
    QTreeWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::NewFormWidget::treeWidgetItemActivated(
    #      QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget23treeWidgetItemActiva'
        'tedEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def treeWidgetCurrentItemChanged(
      self,
      current: Optional[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidget::treeWidgetCurrentItemChanged(
    QTreeWidgetItem *current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    current : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::NewFormWidget::treeWidgetCurrentItemChanged(
    #      QTreeWidgetItem *current)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget28treeWidgetCurrentIte'
        'mChangedEP15QTreeWidgetItem',
        self._addressOf(current),
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def treeWidgetItemPressed(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidget::treeWidgetItemPressed(QTreeWidgetItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::NewFormWidget::treeWidgetItemPressed(
    #      QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget21treeWidgetItemPresse'
        'dEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def slotDeviceProfileIndexChanged(self, idx: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewFormWidget::slotDeviceProfileIndexChanged(int
    idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void qdesigner_internal::NewFormWidget::slotDeviceProfileIndexChanged(
    #      int idx)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget29slotDeviceProfileInd'
        'exChangedEi',
        idx,
    )

  @overload(QString)
  @overload(NoneType)
  def currentTemplateI(self, ptrToErrorMessage: Optional[QString]) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::NewFormWidget::currentTemplateI(QString
    *ptrToErrorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html

    Parameters
    ----------

    ptrToErrorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::NewFormWidget::currentTemplateI(QString
    #      *ptrToErrorMessage)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget16currentTemplateIEP7Q'
        'String',
        self._addressOf(ptrToErrorMessage),
    )

  def showCurrentItemPixmap(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::NewFormWidget::showCurrentItemPixmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newformwidget.html
    """
    #  bool qdesigner_internal::NewFormWidget::showCurrentItemPixmap()
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal13NewFormWidget21showCurrentItemPixma'
        'pEv',
    )

  @staticmethod
  def grabForm(*__, **_) -> Never:
    """
    Qt's 'QImage
    qdesigner_internal::NewFormWidget::grabForm(QDesignerFormEditorInterface
    *core, QIODevice &file, const QString &workingDir, const
    qdesigner_internal::DeviceProfile &dp)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewFormWidget.grabForm' has no cute function "
        "yet. Qt's 'QImage "
        "qdesigner_internal::NewFormWidget::grabForm(QDesignerFormEditorInte"
        "rface *core, QIODevice &file, const QString &workingDir, const "
        "qdesigner_internal::DeviceProfile &dp)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def loadFrom(*__, **_) -> Never:
    """
    - Qt's 'void qdesigner_internal::NewFormWidget::loadFrom(const QString
      &path, bool resourceFile, const QString &uiExtension, const QString
      &selectedItem, QTreeWidgetItem *&selectedItemFound)': takes or gives a
      type that cannot be passed yet: QTreeWidgetItem *&.
    - Qt's 'void qdesigner_internal::NewFormWidget::loadFrom(const QString
      &title, const QStringList &nameList, const QString &selectedItem,
      QTreeWidgetItem *&selectedItemFound)': takes or gives a type that
      cannot be passed yet: QTreeWidgetItem *&.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewFormWidget.loadFrom' has no cute function "
        "yet. Qt's 'void qdesigner_internal::NewFormWidget::loadFrom(const "
        "QString &path, bool resourceFile, const QString &uiExtension, "
        "const QString &selectedItem, QTreeWidgetItem "
        "*&selectedItemFound)': takes or gives a type that cannot be passed "
        "yet: QTreeWidgetItem *&. Qt's 'void "
        "qdesigner_internal::NewFormWidget::loadFrom(const QString &title, "
        "const QStringList &nameList, const QString &selectedItem, "
        "QTreeWidgetItem *&selectedItemFound)': takes or gives a type that "
        "cannot be passed yet: QTreeWidgetItem *&.")
