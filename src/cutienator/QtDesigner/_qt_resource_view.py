"""
QtResourceView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qtresourceview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtResourceView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QDesignerFormEditorInterface, QtResourceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QEvent = WAIT['QEvent']
  QtResourceModel = WAIT['QtResourceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtResourceView(QWidget):
  """
  The cute side of Qt's QtResourceView: a plain Python object standing in
  front of one C++ QtResourceView.

  It is built on the cute 'QWidget', as Qt's QtResourceView is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtResourceView that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'setDragEnabled',
  'dragEnabled', 'model', 'setResourceModel', 'selectedResource',
  'selectResource', 'settingsKey', 'setSettingsKey',
  'isResourceEditingEnabled', 'setResourceEditingEnabled', 'encodeMimeData',
  'resourceSelected', 'resourceActivated', 'event'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtResourceView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QtResourceView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QtResourceView::~QtResourceView()': the destructor: Python never
    removes a C++ QtResourceView.
  - Qt's 'bool QtResourceView::decodeMimeData(const QMimeData *md,
    ResourceType *t, QString *file)': names 'QtResourceView::ResourceType',
    which has no cute class yet.
  - Qt's 'bool QtResourceView::decodeMimeData(const QString &text,
    ResourceType *t, QString *file)': names 'QtResourceView::ResourceType',
    which has no cute class yet.
  - Qt's 'QtResourceViewPrivate *QtResourceView::d_func()': gives
    'QtResourceViewPrivate', which has no cute class yet.
  - Qt's 'const QtResourceViewPrivate *QtResourceView::d_func() const': gives
    'QtResourceViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 30 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QtResourceView is created at the first use, not by
    'QtResourceView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtResourceView.
  - Qt tells when it has removed the C++ QtResourceView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtResourceView that has no cute function yet,
    'decodeMimeData', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QtResourceView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ResourceType(CuteNum):
    """
    The enum 'QtResourceView::ResourceType' of Qt, with the 3 names Qt gives
    in it.
    """

    ResourceImage = Kee[int](0)
    ResourceStyleSheet = Kee[int](1)
    ResourceOther = Kee[int](2)

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
    Calls Qt's 'QString QtResourceView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#tr

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
    #  QString QtResourceView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QtResourceView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(ResourceType, str)
  def encodeMimeData(resourceType: ResourceType, path: str) -> str:
    """
    Calls Qt's 'QString QtResourceView::encodeMimeData(ResourceType
    resourceType, const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#encodeMimeData

    Parameters
    ----------

    resourceType : ResourceType
      Passed on as its number.

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtResourceView::encodeMimeData(ResourceType resourceType,
    #      const QString &path)
    return Rituals.call(
        'ritual_ZN14QtResourceView14encodeMimeDataENS_12ResourceTypeERK7QSt'
        'ring',
        resourceType.value, path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtResourceView'

  #  A C++ QtResourceView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtResourceView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtResourceView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtResourceView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QtResourceView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dragEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtResourceView::dragEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#dragEnabled
    """
    #  bool QtResourceView::dragEnabled() const
    return self.uglySide.call('ritual_ZNK14QtResourceView11dragEnabledEv')

  def model(self) -> Optional[QtResourceModel]:
    """
    Calls Qt's 'QtResourceModel *QtResourceView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#model

    Returns
    -------

    Optional[QtResourceModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceModel *QtResourceView::model() const
    address = self.uglySide.call('ritual_ZNK14QtResourceView5modelEv')
    from . import QtResourceModel
    return QtResourceModel._cuteAt(address)

  def selectedResource(self) -> str:
    """
    Calls Qt's 'QString QtResourceView::selectedResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#selectedResource

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtResourceView::selectedResource() const
    return self.uglySide.call(
        'ritual_ZNK14QtResourceView16selectedResourceEv',
    )

  def settingsKey(self) -> str:
    """
    Calls Qt's 'QString QtResourceView::settingsKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#settingsKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtResourceView::settingsKey() const
    return self.uglySide.call('ritual_ZNK14QtResourceView11settingsKeyEv')

  def isResourceEditingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtResourceView::isResourceEditingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#isResourceEditingEnabled
    """
    #  bool QtResourceView::isResourceEditingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK14QtResourceView24isResourceEditingEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDragEnabled(self, dragEnabled: bool) -> None:
    """
    Calls Qt's 'void QtResourceView::setDragEnabled(bool dragEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#setDragEnabled

    Parameters
    ----------

    dragEnabled : bool
      Passed on as it is.
    """
    #  void QtResourceView::setDragEnabled(bool dragEnabled)
    self.uglySide.call(
        'ritual_ZN14QtResourceView14setDragEnabledEb', dragEnabled,
    )

  @overload(QtResourceModel)
  @overload(NoneType)
  def setResourceModel(self, model: Optional[QtResourceModel]) -> None:
    """
    Calls Qt's 'void QtResourceView::setResourceModel(QtResourceModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#setResourceModel

    Parameters
    ----------

    model : Optional[QtResourceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtResourceView::setResourceModel(QtResourceModel *model)
    self.uglySide.call(
        'ritual_ZN14QtResourceView16setResourceModelEP15QtResourceModel',
        self._addressOf(model),
    )

  @overload(str)
  def setSettingsKey(self, key: str) -> None:
    """
    Calls Qt's 'void QtResourceView::setSettingsKey(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#setSettingsKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceView::setSettingsKey(const QString &key)
    self.uglySide.call(
        'ritual_ZN14QtResourceView14setSettingsKeyERK7QString', key,
    )

  @overload(bool)
  def setResourceEditingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QtResourceView::setResourceEditingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#setResourceEditingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtResourceView::setResourceEditingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN14QtResourceView25setResourceEditingEnabledEb', enable,
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtResourceView::QtResourceView(QDesignerFormEditorInterface *core,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#QtResourceView

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtResourceView::QtResourceView(QDesignerFormEditorInterface *core,
    #      QWidget *parent)
    self._noteCreation(QtResourceView, lambda: Rituals.call(
        'ritual_ZN14QtResourceViewC1EP28QDesignerFormEditorInterfaceP7QWidg'
        'et',
        self._addressOf(core), self._addressOf(parent),
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
  def selectResource(self, resource: str) -> None:
    """
    Calls Qt's 'void QtResourceView::selectResource(const QString
    &resource)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#selectResource

    Parameters
    ----------

    resource : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceView::selectResource(const QString &resource)
    self.uglySide.call(
        'ritual_ZN14QtResourceView14selectResourceERK7QString', resource,
    )

  @overload(str)
  def resourceSelected(self, resource: str) -> None:
    """
    Calls Qt's 'void QtResourceView::resourceSelected(const QString
    &resource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#resourceSelected

    Parameters
    ----------

    resource : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceView::resourceSelected(const QString &resource)
    self.uglySide.call(
        'ritual_ZN14QtResourceView16resourceSelectedERK7QString', resource,
    )

  @overload(str)
  def resourceActivated(self, resource: str) -> None:
    """
    Calls Qt's 'void QtResourceView::resourceActivated(const QString
    &resource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceview.html#resourceActivated

    Parameters
    ----------

    resource : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceView::resourceActivated(const QString &resource)
    self.uglySide.call(
        'ritual_ZN14QtResourceView17resourceActivatedERK7QString', resource,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtResourceView::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceview.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtResourceView::event(QEvent *event)
    ritual = 'ritual_ZN14QtResourceView5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QtResourceView5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def decodeMimeData(*__, **_) -> Never:
    """
    - Qt's 'bool QtResourceView::decodeMimeData(const QMimeData *md,
      ResourceType *t, QString *file)': names 'QtResourceView::ResourceType',
      which has no cute class yet.
    - Qt's 'bool QtResourceView::decodeMimeData(const QString &text,
      ResourceType *t, QString *file)': names 'QtResourceView::ResourceType',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtResourceView.decodeMimeData' has no cute function yet. Qt's "
        "'bool QtResourceView::decodeMimeData(const QMimeData *md, "
        "ResourceType *t, QString *file)': names "
        "'QtResourceView::ResourceType', which has no cute class yet. Qt's "
        "'bool QtResourceView::decodeMimeData(const QString &text, "
        "ResourceType *t, QString *file)': names "
        "'QtResourceView::ResourceType', which has no cute class yet.")
