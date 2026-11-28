"""
QDesignerIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractintegration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerIntegrationInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtWidgets import QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
  from . import QDesignerResourceBrowserInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerIntegration(QDesignerIntegrationInterface):
  """
  The cute side of Qt's QDesignerIntegration: a plain Python object standing
  in front of one C++ QDesignerIntegration.

  It is built on the cute 'QDesignerIntegrationInterface', as Qt's
  QDesignerIntegration is built on Qt's QDesignerIntegrationInterface, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerIntegration that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr',
  'headerSuffix', 'setHeaderSuffix', 'isHeaderLowercase',
  'setHeaderLowercase', 'features', 'setFeatures',
  'resourceFileWatcherBehaviour', 'setResourceFileWatcherBehaviour',
  'containerWindow', 'initializePlugins', 'createResourceBrowser',
  'contextHelpId', 'updateProperty', 'resetProperty', 'addDynamicProperty',
  'removeDynamicProperty', 'updateActiveFormWindow', 'setupFormWindow',
  'updateSelection', 'updateCustomWidgetPlugins'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerIntegration::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDesignerIntegration::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerIntegration::~QDesignerIntegration()': the destructor:
    Python never removes a C++ QDesignerIntegration.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerIntegration is created at the first use, not by
    'QDesignerIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerIntegration.
  - Qt tells when it has removed the C++ QDesignerIntegration. Every call on
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
    Calls Qt's 'QString QDesignerIntegration::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerintegration.html#tr

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
    #  QString QDesignerIntegration::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QDesignerIntegration2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def initializePlugins(
      formEditor: Optional[QDesignerFormEditorInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegration::initializePlugins(QDesignerFormEditorInterface
    *formEditor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#initializePlugins

    Parameters
    ----------

    formEditor : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerIntegration::initializePlugins(
    #      QDesignerFormEditorInterface *formEditor)
    Rituals.call(
        'ritual_ZN20QDesignerIntegration17initializePluginsEP28QDesignerFor'
        'mEditorInterface',
        CuteMixin._addressOf(formEditor),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerIntegration'

  #  A C++ QDesignerIntegration Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerIntegration'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerIntegration::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerIntegration::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QDesignerIntegration10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def headerSuffix(self) -> str:
    """
    Calls Qt's 'QString QDesignerIntegration::headerSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#headerSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerIntegration::headerSuffix() const
    ritual = 'ritual_ZNK20QDesignerIntegration12headerSuffixEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerIntegration12headerSuffixEv'
    return self.uglySide.call(ritual)

  def isHeaderLowercase(self) -> bool:
    """
    Calls Qt's 'bool QDesignerIntegration::isHeaderLowercase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#isHeaderLowercase
    """
    #  bool QDesignerIntegration::isHeaderLowercase() const
    ritual = 'ritual_ZNK20QDesignerIntegration17isHeaderLowercaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerIntegration17isHeaderLowercaseEv'
    return self.uglySide.call(ritual)

  def features(self) -> QDesignerIntegrationInterface.Feature:
    """
    Calls Qt's 'Feature QDesignerIntegration::features() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerintegration.html#features

    Returns
    -------

    QDesignerIntegrationInterface.Feature
      The value standing for the combination Qt gave back.
    """
    #  Feature QDesignerIntegration::features() const
    ritual = 'ritual_ZNK20QDesignerIntegration8featuresEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerIntegration8featuresEv'
    return QDesignerIntegrationInterface.Feature(self.uglySide.call(ritual))

  def resourceFileWatcherBehaviour(
      self,
  ) -> QDesignerIntegrationInterface.ResourceFileWatcherBehaviour:
    """
    Calls Qt's 'ResourceFileWatcherBehaviour
    QDesignerIntegration::resourceFileWatcherBehaviour() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html

    Returns
    -------

    QDesignerIntegrationInterface.ResourceFileWatcherBehaviour
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDesignerIntegrationInterface.ResourceFileWatcherBehaviour(number)'
      gives.
    """
    #  ResourceFileWatcherBehaviour
    #      QDesignerIntegration::resourceFileWatcherBehaviour() const
    ritual = (
        'ritual_ZNK20QDesignerIntegration28resourceFileWatcherBehaviourEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDesignerIntegration28resourceFileWatcherBehavio'
          'urEv')
    return QDesignerIntegrationInterface.ResourceFileWatcherBehaviour(
        self.uglySide.call(
            'ritual_ZNK20QDesignerIntegration28resourceFileWatcherBehaviour'
            'Ev',
        ))

  @overload(QWidget)
  @overload(NoneType)
  def containerWindow(self, widget: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerIntegration::containerWindow(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#containerWindow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerIntegration::containerWindow(QWidget *widget) const
    ritual = 'ritual_ZNK20QDesignerIntegration15containerWindowEP7QWidget'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDesignerIntegration15containerWindowEP7QWidget')
    address = self.uglySide.call(ritual, self._addressOf(widget))
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def contextHelpId(self) -> str:
    """
    Calls Qt's 'QString QDesignerIntegration::contextHelpId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#contextHelpId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerIntegration::contextHelpId() const
    ritual = 'ritual_ZNK20QDesignerIntegration13contextHelpIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerIntegration13contextHelpIdEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHeaderSuffix(self, headerSuffix: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::setHeaderSuffix(const QString
    &headerSuffix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#setHeaderSuffix

    Parameters
    ----------

    headerSuffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegration::setHeaderSuffix(const QString
    #      &headerSuffix)
    ritual = 'ritual_ZN20QDesignerIntegration15setHeaderSuffixERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration15setHeaderSuffixERK7QString')
    self.uglySide.call(ritual, headerSuffix)

  @overload(bool)
  def setHeaderLowercase(self, headerLowerCase: bool) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::setHeaderLowercase(bool
    headerLowerCase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#setHeaderLowercase

    Parameters
    ----------

    headerLowerCase : bool
      Passed on as it is.
    """
    #  void QDesignerIntegration::setHeaderLowercase(bool headerLowerCase)
    ritual = 'ritual_ZN20QDesignerIntegration18setHeaderLowercaseEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesignerIntegration18setHeaderLowercaseEb'
    self.uglySide.call(ritual, headerLowerCase)

  @overload(QDesignerIntegrationInterface.Feature)
  def setFeatures(self, f: QDesignerIntegrationInterface.Feature) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::setFeatures(Feature f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#setFeatures

    Parameters
    ----------

    f : QDesignerIntegrationInterface.Feature
      Passed on as its number.
    """
    #  void QDesignerIntegration::setFeatures(Feature f)
    ritual = (
        'ritual_ZN20QDesignerIntegration11setFeaturesE6QFlagsIN29QDesignerI'
        'ntegrationInterface11FeatureFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration11setFeaturesE6QFlagsIN29QDes'
          'ignerIntegrationInterface11FeatureFlagEE')
    self.uglySide.call(ritual, f.value)

  @overload(QDesignerIntegrationInterface.ResourceFileWatcherBehaviour)
  def setResourceFileWatcherBehaviour(
      self,
      behaviour: QDesignerIntegrationInterface.ResourceFileWatcherBehaviour,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::setResourceFileWatcherBehaviour(
    ResourceFileWatcherBehaviour behaviour)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html

    Parameters
    ----------

    behaviour : QDesignerIntegrationInterface.ResourceFileWatcherBehaviour
      Passed on as its number.
    """
    #  void QDesignerIntegration::setResourceFileWatcherBehaviour(
    #      ResourceFileWatcherBehaviour behaviour)
    ritual = (
        'ritual_ZN20QDesignerIntegration31setResourceFileWatcherBehaviourEN'
        '29QDesignerIntegrationInterface28ResourceFileWatcherBehaviourE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration31setResourceFileWatcherBehav'
          'iourEN29QDesignerIntegrationInterface28ResourceFileWatcherBehavi'
          'ourE')
    self.uglySide.call(ritual, behaviour.value)

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
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerIntegration::QDesignerIntegration(QDesignerFormEditorInterface
    *core, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#QDesignerIntegration

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerIntegration::QDesignerIntegration(
    #      QDesignerFormEditorInterface *core, QObject *parent)
    self._noteCreation(QDesignerIntegration, lambda: Rituals.call(
        'ritual_ZN20QDesignerIntegrationC1EP28QDesignerFormEditorInterfaceP'
        '7QObject',
        self._addressOf(core), self._addressOf(parent, 'QObject'),
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
  @overload(QWidget)
  @overload(NoneType)
  def createResourceBrowser(
      self,
      parent: Optional[QWidget] = None,
  ) -> Optional[QDesignerResourceBrowserInterface]:
    """
    Calls Qt's 'QDesignerResourceBrowserInterface
    *QDesignerIntegration::createResourceBrowser(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#createResourceBrowser

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QDesignerResourceBrowserInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerResourceBrowserInterface
    #      *QDesignerIntegration::createResourceBrowser(QWidget *parent)
    ritual = (
        'ritual_ZN20QDesignerIntegration21createResourceBrowserEP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration21createResourceBrowserEP7QWi'
          'dget')
    address = self.uglySide.call(ritual, self._addressOf(parent))
    from . import QDesignerResourceBrowserInterface
    return QDesignerResourceBrowserInterface._cuteAt(address)

  @overload(str, QVariant, bool)
  def updateProperty(
      self,
      name: str,
      value: QVariant,
      enableSubPropertyHandling: bool,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::updateProperty(const QString
    &name, const QVariant &value, bool enableSubPropertyHandling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#updateProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    enableSubPropertyHandling : bool
      Passed on as it is.
    """
    #  void QDesignerIntegration::updateProperty(const QString &name, const
    #      QVariant &value, bool enableSubPropertyHandling)
    ritual = (
        'ritual_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVari'
        'antb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration14updatePropertyERK7QStringRK'
          '8QVariantb')
    self.uglySide.call(
        ritual, name, self._valueOf(value), enableSubPropertyHandling,
    )

  @overload(str, QVariant)
  def updateProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::updateProperty(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#updateProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerIntegration::updateProperty(const QString &name, const
    #      QVariant &value)
    ritual = (
        'ritual_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVari'
        'ant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration14updatePropertyERK7QStringRK'
          '8QVariant')
    self.uglySide.call(ritual, name, self._valueOf(value))

  @overload(str)
  def resetProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::resetProperty(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#resetProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegration::resetProperty(const QString &name)
    ritual = 'ritual_ZN20QDesignerIntegration13resetPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration13resetPropertyERK7QString')
    self.uglySide.call(ritual, name)

  @overload(str, QVariant)
  def addDynamicProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::addDynamicProperty(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#addDynamicProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerIntegration::addDynamicProperty(const QString &name,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN20QDesignerIntegration18addDynamicPropertyERK7QStringRK8Q'
        'Variant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration18addDynamicPropertyERK7QStri'
          'ngRK8QVariant')
    self.uglySide.call(ritual, name, self._valueOf(value))

  @overload(str)
  def removeDynamicProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::removeDynamicProperty(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#removeDynamicProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegration::removeDynamicProperty(const QString &name)
    ritual = (
        'ritual_ZN20QDesignerIntegration21removeDynamicPropertyERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration21removeDynamicPropertyERK7QS'
          'tring')
    self.uglySide.call(ritual, name)

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def updateActiveFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegration::updateActiveFormWindow(QDesignerFormWindowInterface
    *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#updateActiveFormWindow

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerIntegration::updateActiveFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    ritual = (
        'ritual_ZN20QDesignerIntegration22updateActiveFormWindowEP28QDesign'
        'erFormWindowInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration22updateActiveFormWindowEP28Q'
          'DesignerFormWindowInterface')
    self.uglySide.call(ritual, self._addressOf(formWindow))

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setupFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegration::setupFormWindow(QDesignerFormWindowInterface
    *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#setupFormWindow

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QDesignerIntegration::setupFormWindow(QDesignerFormWindowInterface
    #      *formWindow)
    ritual = (
        'ritual_ZN20QDesignerIntegration15setupFormWindowEP28QDesignerFormW'
        'indowInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration15setupFormWindowEP28QDesigne'
          'rFormWindowInterface')
    self.uglySide.call(ritual, self._addressOf(formWindow))

  def updateSelection(self) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::updateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html#updateSelection
    """
    #  void QDesignerIntegration::updateSelection()
    ritual = 'ritual_ZN20QDesignerIntegration15updateSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesignerIntegration15updateSelectionEv'
    self.uglySide.call(ritual)

  def updateCustomWidgetPlugins(self) -> None:
    """
    Calls Qt's 'void QDesignerIntegration::updateCustomWidgetPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegration.html
    """
    #  void QDesignerIntegration::updateCustomWidgetPlugins()
    ritual = 'ritual_ZN20QDesignerIntegration25updateCustomWidgetPluginsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerIntegration25updateCustomWidgetPluginsEv')
    self.uglySide.call(ritual)
