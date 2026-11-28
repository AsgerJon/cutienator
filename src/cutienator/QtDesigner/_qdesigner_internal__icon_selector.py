"""
qdesigner_internal::IconSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/iconselector_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::IconSelector to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QString
  from . import QDesignerDialogGuiInterface, QDesignerFormEditorInterface
  from . import QtResourceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDialogGuiInterface = WAIT['QDesignerDialogGuiInterface']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QString = WAIT['QString']
  QtResourceModel = WAIT['QtResourceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IconSelector(QWidget):
  """
  The cute side of Qt's qdesigner_internal::IconSelector: a plain Python
  object standing in front of one C++ qdesigner_internal::IconSelector.

  It is built on the cute 'QWidget', as Qt's qdesigner_internal::IconSelector
  is built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::IconSelector that has a ritual
  and that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'setFormEditor', 'setIconCache', 'setIcon', 'icon', 'checkPixmap',
  'choosePixmapFile', 'choosePixmapResource', 'iconChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::IconSelector::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::IconSelector::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::IconSelector::~IconSelector()': the destructor:
    Python never removes a C++ qdesigner_internal::IconSelector.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 4 forbidden; 2 not a gap; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ qdesigner_internal::IconSelector is created at the first use, not
    by 'qdesigner_internal::IconSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::IconSelector.
  - Qt tells when it has removed the C++ qdesigner_internal::IconSelector.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::IconSelector, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class CheckMode(CuteNum):
    """
    The enum 'qdesigner_internal::IconSelector::CheckMode' of Qt, with the 2
    names Qt gives in it.
    """

    CheckFast = Kee[int](0)
    CheckFully = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::IconSelector::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#tr

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
    #  QString qdesigner_internal::IconSelector::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12IconSelector2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  @overload(str, CheckMode)
  @overload(str, CheckMode, QString)
  @overload(str, CheckMode, NoneType)
  def checkPixmap(
      fileName: str,
      cm: CheckMode = CheckMode.CheckFully,
      errorMessage: Optional[QString] = None,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::IconSelector::checkPixmap(const
    QString &fileName, CheckMode cm, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#checkPixmap

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    cm : CheckMode
      Passed on as its number. May be left out, as in Qt: it is then
      CheckMode.CheckFully.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool qdesigner_internal::IconSelector::checkPixmap(const QString
    #      &fileName, CheckMode cm, QString *errorMessage)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12IconSelector11checkPixmapERK7QStrin'
        'gNS0_9CheckModeEPS1_',
        fileName, cm.value, CuteMixin._addressOf(errorMessage),
    )

  @staticmethod
  @overload(str, QDesignerDialogGuiInterface, QWidget)
  @overload(str, QDesignerDialogGuiInterface, NoneType)
  @overload(str, NoneType, QWidget)
  @overload(str, NoneType, NoneType)
  def choosePixmapFile(
      directory: str,
      dlgGui: Optional[QDesignerDialogGuiInterface],
      parent: Optional[QWidget],
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::IconSelector::choosePixmapFile(const QString
    &directory, QDesignerDialogGuiInterface *dlgGui, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.

    dlgGui : Optional[QDesignerDialogGuiInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::IconSelector::choosePixmapFile(const
    #      QString &directory, QDesignerDialogGuiInterface *dlgGui, QWidget
    #      *parent)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12IconSelector16choosePixmapFileERK7Q'
        'StringP27QDesignerDialogGuiInterfaceP7QWidget',
        directory, CuteMixin._addressOf(dlgGui),
        CuteMixin._addressOf(parent),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QtResourceModel, str, QWidget)
  @overload(QDesignerFormEditorInterface, QtResourceModel, str, NoneType)
  @overload(QDesignerFormEditorInterface, NoneType, str, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType, str, NoneType)
  @overload(NoneType, QtResourceModel, str, QWidget)
  @overload(NoneType, QtResourceModel, str, NoneType)
  @overload(NoneType, NoneType, str, QWidget)
  @overload(NoneType, NoneType, str, NoneType)
  def choosePixmapResource(
      core: Optional[QDesignerFormEditorInterface],
      resourceModel: Optional[QtResourceModel],
      oldPath: str,
      parent: Optional[QWidget],
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::IconSelector::choosePixmapResource(
    QDesignerFormEditorInterface *core, QtResourceModel *resourceModel, const
    QString &oldPath, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceModel : Optional[QtResourceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldPath : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::IconSelector::choosePixmapResource(
    #      QDesignerFormEditorInterface *core, QtResourceModel
    #      *resourceModel, const QString &oldPath, QWidget *parent)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12IconSelector20choosePixmapResourceE'
        'P28QDesignerFormEditorInterfaceP15QtResourceModelRK7QStringP7QWidg'
        'et',
        CuteMixin._addressOf(core), CuteMixin._addressOf(resourceModel),
        oldPath, CuteMixin._addressOf(parent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::IconSelector'

  #  A C++ qdesigner_internal::IconSelector Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_IconSelector'

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
    *qdesigner_internal::IconSelector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::IconSelector::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12IconSelector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def icon(self) -> qdesigner_internal.PropertySheetIconValue:
    """
    Calls Qt's 'PropertySheetIconValue
    qdesigner_internal::IconSelector::icon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#icon

    Returns
    -------

    qdesigner_internal.PropertySheetIconValue
      A new cute qdesigner_internal::PropertySheetIconValue around the copy
      Qt gave back. Python owns it.
    """
    #  PropertySheetIconValue qdesigner_internal::IconSelector::icon() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12IconSelector4iconEv',
    )
    return qdesigner_internal.PropertySheetIconValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def setFormEditor(
      self,
      core: Optional[QDesignerFormEditorInterface],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::IconSelector::setFormEditor(
    QDesignerFormEditorInterface *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#setFormEditor

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::IconSelector::setFormEditor(
    #      QDesignerFormEditorInterface *core)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12IconSelector13setFormEditorEP28QDes'
        'ignerFormEditorInterface',
        self._addressOf(core),
    )

  @overload(WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(NoneType)
  def setIconCache(
      self,
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::IconSelector::setIconCache(DesignerIconCache
    *iconCache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#setIconCache

    Parameters
    ----------

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::IconSelector::setIconCache(DesignerIconCache
    #      *iconCache)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12IconSelector12setIconCacheEPNS_17De'
        'signerIconCacheE',
        self._addressOf(iconCache),
    )

  @overload(WAIT['qdesigner_internal.PropertySheetIconValue'])
  def setIcon(self, icon: qdesigner_internal.PropertySheetIconValue) -> None:
    """
    Calls Qt's 'void qdesigner_internal::IconSelector::setIcon(const
    PropertySheetIconValue &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#setIcon

    Parameters
    ----------

    icon : qdesigner_internal.PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  void qdesigner_internal::IconSelector::setIcon(const
    #      PropertySheetIconValue &icon)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12IconSelector7setIconERKNS_22Propert'
        'ySheetIconValueE',
        self._valueOf(icon),
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::IconSelector::IconSelector(QWidget *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#IconSelector

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::IconSelector::IconSelector(QWidget *parent)
    self._noteCreation(IconSelector, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12IconSelectorC1EP7QWidget',
        self._addressOf(parent),
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

  @overload(WAIT['qdesigner_internal.PropertySheetIconValue'])
  def iconChanged(
      self,
      icon: qdesigner_internal.PropertySheetIconValue,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::IconSelector::iconChanged(const
    PropertySheetIconValue &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconselector.html#iconChanged

    Parameters
    ----------

    icon : qdesigner_internal.PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  void qdesigner_internal::IconSelector::iconChanged(const
    #      PropertySheetIconValue &icon)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12IconSelector11iconChangedERKNS_22Pr'
        'opertySheetIconValueE',
        self._valueOf(icon),
    )
