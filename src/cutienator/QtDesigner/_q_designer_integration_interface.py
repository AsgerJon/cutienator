"""
QDesignerIntegrationInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractintegration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant, QVersionNumber
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
  QVersionNumber = WAIT['QVersionNumber']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerIntegrationInterface(QObject):
  """
  The cute side of Qt's QDesignerIntegrationInterface: a plain Python object
  standing in front of one C++ QDesignerIntegrationInterface.

  It is built on the cute 'QObject', as Qt's QDesignerIntegrationInterface is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerIntegrationInterface that has a ritual and
  that Python can call so far, 32 names in all: 'metaObject', 'tr', 'core',
  'containerWindow', 'createResourceBrowser', 'headerSuffix',
  'setHeaderSuffix', 'isHeaderLowercase', 'setHeaderLowercase', 'qtVersion',
  'setQtVersion', 'features', 'hasFeature', 'resourceFileWatcherBehaviour',
  'setResourceFileWatcherBehaviour', 'contextHelpId',
  'emitObjectNameChanged', 'emitNavigateToSlot', 'emitHelpRequested',
  'propertyChanged', 'objectNameChanged', 'helpRequested', 'navigateToSlot',
  'setFeatures', 'updateProperty', 'resetProperty', 'addDynamicProperty',
  'removeDynamicProperty', 'updateActiveFormWindow', 'setupFormWindow',
  'updateSelection', 'updateCustomWidgetPlugins'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerIntegrationInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerIntegrationInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerIntegrationInterface::~QDesignerIntegrationInterface()':
    the destructor: Python never removes a C++ QDesignerIntegrationInterface.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerIntegrationInterface is created at the first use, not by
    'QDesignerIntegrationInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerIntegrationInterface.
  - Qt tells when it has removed the C++ QDesignerIntegrationInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDesignerIntegrationInterface, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class FeatureFlag(CuteFlags):
    """
    The flags enum 'QDesignerIntegrationInterface::FeatureFlag' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QDesignerIntegrationInterface::Feature'.
    """

    ResourceEditorFeature = 0x1
    SlotNavigationFeature = 0x2
    DefaultWidgetActionFeature = 0x4
    DefaultFeature = 0x5

  Feature = FeatureFlag

  class ResourceFileWatcherBehaviour(CuteNum):
    """
    The enum 'QDesignerIntegrationInterface::ResourceFileWatcherBehaviour' of
    Qt, with the 3 names Qt gives in it.
    """

    NoResourceFileWatcher = Kee[int](0)
    ReloadResourceFileSilently = Kee[int](1)
    PromptToReloadResourceFile = Kee[int](2)

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
    Calls Qt's 'QString QDesignerIntegrationInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#tr

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
    #  QString QDesignerIntegrationInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QDesignerIntegrationInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerIntegrationInterface'

  #  A C++ QDesignerIntegrationInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerIntegrationInterface'

  #  The functions Qt calls itself that QDesignerIntegrationInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'containerWindow': (
          ('_ZNK29QDesignerIntegrationInterface15containerWindowEP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createResourceBrowser': (
          ('_ZN29QDesignerIntegrationInterface21createResourceBrowserEP7QWi'
           'dget',
           ('address', 'address',
            'QtDesigner:QDesignerResourceBrowserInterface'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'headerSuffix': (
          ('_ZNK29QDesignerIntegrationInterface12headerSuffixEv',
           ('address', 'text', ''),
           ()),
      ),
      'setHeaderSuffix': (
          ('_ZN29QDesignerIntegrationInterface15setHeaderSuffixERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'isHeaderLowercase': (
          ('_ZNK29QDesignerIntegrationInterface17isHeaderLowercaseEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setHeaderLowercase': (
          ('_ZN29QDesignerIntegrationInterface18setHeaderLowercaseEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'features': (
          ('_ZNK29QDesignerIntegrationInterface8featuresEv',
           ('int', 'flags',
            'QtDesigner:QDesignerIntegrationInterface.FeatureFlag'),
           ()),
      ),
      'resourceFileWatcherBehaviour': (
          ('_ZNK29QDesignerIntegrationInterface28resourceFileWatcherBehavio'
           'urEv',
           ('int', 'enum',
            'QtDesigner:QDesignerIntegrationInterface.ResourceFileWatcherBehaviour'),
           ()),
      ),
      'setResourceFileWatcherBehaviour': (
          ('_ZN29QDesignerIntegrationInterface31setResourceFileWatcherBehav'
           'iourENS_28ResourceFileWatcherBehaviourE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDesigner:QDesignerIntegrationInterface.ResourceFileWatcherBehaviour'),
           )),
      ),
      'contextHelpId': (
          ('_ZNK29QDesignerIntegrationInterface13contextHelpIdEv',
           ('address', 'text', ''),
           ()),
      ),
      'setFeatures': (
          ('_ZN29QDesignerIntegrationInterface11setFeaturesE6QFlagsINS_11Fe'
           'atureFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtDesigner:QDesignerIntegrationInterface.FeatureFlag'),
           )),
      ),
      'updateProperty': (
          ('_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK'
           '8QVariantb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('bool', 'number', ''),
           )),
          ('_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK'
           '8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'resetProperty': (
          ('_ZN29QDesignerIntegrationInterface13resetPropertyERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'addDynamicProperty': (
          ('_ZN29QDesignerIntegrationInterface18addDynamicPropertyERK7QStri'
           'ngRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'removeDynamicProperty': (
          ('_ZN29QDesignerIntegrationInterface21removeDynamicPropertyERK7QS'
           'tring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'updateActiveFormWindow': (
          ('_ZN29QDesignerIntegrationInterface22updateActiveFormWindowEP28Q'
           'DesignerFormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
           )),
      ),
      'setupFormWindow': (
          ('_ZN29QDesignerIntegrationInterface15setupFormWindowEP28QDesigne'
           'rFormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
           )),
      ),
      'updateSelection': (
          ('_ZN29QDesignerIntegrationInterface15updateSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateCustomWidgetPlugins': (
          ('_ZN29QDesignerIntegrationInterface25updateCustomWidgetPluginsEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject
    *QDesignerIntegrationInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerIntegrationInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerIntegrationInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerIntegrationInterface::core()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def containerWindow(self, widget: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QDesignerIntegrationInterface::containerWindow(QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#containerWindow

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
    #  QWidget *QDesignerIntegrationInterface::containerWindow(QWidget
    #      *widget) const
    address = self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface15containerWindowEP7QWidg'
        'et',
        self._addressOf(widget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def headerSuffix(self) -> str:
    """
    Calls Qt's 'QString QDesignerIntegrationInterface::headerSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#headerSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerIntegrationInterface::headerSuffix() const
    return self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface12headerSuffixEv',
    )

  def isHeaderLowercase(self) -> bool:
    """
    Calls Qt's 'bool QDesignerIntegrationInterface::isHeaderLowercase()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html
    """
    #  bool QDesignerIntegrationInterface::isHeaderLowercase() const
    return self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface17isHeaderLowercaseEv',
    )

  def qtVersion(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QDesignerIntegrationInterface::qtVersion()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#qtVersion

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QDesignerIntegrationInterface::qtVersion() const
    address = self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface9qtVersionEv',
    )
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def features(self) -> Feature:
    """
    Calls Qt's 'Feature QDesignerIntegrationInterface::features() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#features

    Returns
    -------

    Feature
      The value standing for the combination Qt gave back.
    """
    #  Feature QDesignerIntegrationInterface::features() const
    return QDesignerIntegrationInterface.Feature(self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface8featuresEv',
    ))

  @overload(Feature)
  def hasFeature(self, f: Feature) -> bool:
    """
    Calls Qt's 'bool QDesignerIntegrationInterface::hasFeature(Feature f)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#hasFeature

    Parameters
    ----------

    f : Feature
      Passed on as its number.
    """
    #  bool QDesignerIntegrationInterface::hasFeature(Feature f) const
    return self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface10hasFeatureE6QFlagsINS_1'
        '1FeatureFlagEE',
        f.value,
    )

  def resourceFileWatcherBehaviour(self) -> ResourceFileWatcherBehaviour:
    """
    Calls Qt's 'ResourceFileWatcherBehaviour
    QDesignerIntegrationInterface::resourceFileWatcherBehaviour() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Returns
    -------

    ResourceFileWatcherBehaviour
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ResourceFileWatcherBehaviour(number)' gives.
    """
    #  ResourceFileWatcherBehaviour
    #      QDesignerIntegrationInterface::resourceFileWatcherBehaviour()
    #      const
    return QDesignerIntegrationInterface.ResourceFileWatcherBehaviour(
        self.uglySide.call(
            'ritual_ZNK29QDesignerIntegrationInterface28resourceFileWatcher'
            'BehaviourEv',
        ))

  def contextHelpId(self) -> str:
    """
    Calls Qt's 'QString QDesignerIntegrationInterface::contextHelpId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#contextHelpId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerIntegrationInterface::contextHelpId() const
    return self.uglySide.call(
        'ritual_ZNK29QDesignerIntegrationInterface13contextHelpIdEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHeaderSuffix(self, headerSuffix: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::setHeaderSuffix(const
    QString &headerSuffix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#setHeaderSuffix

    Parameters
    ----------

    headerSuffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::setHeaderSuffix(const QString
    #      &headerSuffix)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface15setHeaderSuffixERK7QStri'
        'ng',
        headerSuffix,
    )

  @overload(bool)
  def setHeaderLowercase(self, headerLowerCase: bool) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::setHeaderLowercase(bool
    headerLowerCase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    headerLowerCase : bool
      Passed on as it is.
    """
    #  void QDesignerIntegrationInterface::setHeaderLowercase(bool
    #      headerLowerCase)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface18setHeaderLowercaseEb',
        headerLowerCase,
    )

  @overload(QVersionNumber)
  def setQtVersion(self, qtVersion: QVersionNumber) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::setQtVersion(const
    QVersionNumber &qtVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#setQtVersion

    Parameters
    ----------

    qtVersion : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  void QDesignerIntegrationInterface::setQtVersion(const QVersionNumber
    #      &qtVersion)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface12setQtVersionERK14QVersio'
        'nNumber',
        self._valueOf(qtVersion),
    )

  @overload(ResourceFileWatcherBehaviour)
  def setResourceFileWatcherBehaviour(
      self,
      behaviour: ResourceFileWatcherBehaviour,
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegrationInterface::setResourceFileWatcherBehaviour(
    ResourceFileWatcherBehaviour behaviour)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    behaviour : ResourceFileWatcherBehaviour
      Passed on as its number.
    """
    #  void QDesignerIntegrationInterface::setResourceFileWatcherBehaviour(
    #      ResourceFileWatcherBehaviour behaviour)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface31setResourceFileWatcherBe'
        'haviourENS_28ResourceFileWatcherBehaviourE',
        behaviour.value,
    )

  @overload(Feature)
  def setFeatures(self, f: Feature) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::setFeatures(Feature f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#setFeatures

    Parameters
    ----------

    f : Feature
      Passed on as its number.
    """
    #  void QDesignerIntegrationInterface::setFeatures(Feature f)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface11setFeaturesE6QFlagsINS_1'
        '1FeatureFlagEE',
        f.value,
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
    'QDesignerIntegrationInterface::QDesignerIntegrationInterface(
    QDesignerFormEditorInterface *core, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerIntegrationInterface::QDesignerIntegrationInterface(
    #      QDesignerFormEditorInterface *core, QObject *parent)
    self._noteCreation(QDesignerIntegrationInterface, lambda: Rituals.call(
        'ritual_ZN29QDesignerIntegrationInterfaceC1EP28QDesignerFormEditorI'
        'nterfaceP7QObject',
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
    *QDesignerIntegrationInterface::createResourceBrowser(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

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
    #      *QDesignerIntegrationInterface::createResourceBrowser(QWidget
    #      *parent)
    address = self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface21createResourceBrowserEP7'
        'QWidget',
        self._addressOf(parent),
    )
    from . import QDesignerResourceBrowserInterface
    return QDesignerResourceBrowserInterface._cuteAt(address)

  @overload(QDesignerFormWindowInterface, QObject, str, str)
  @overload(QDesignerFormWindowInterface, NoneType, str, str)
  @overload(NoneType, QObject, str, str)
  @overload(NoneType, NoneType, str, str)
  def emitObjectNameChanged(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      object: Optional[QObject],
      newName: str,
      oldName: str,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::emitObjectNameChanged(
    QDesignerFormWindowInterface *formWindow, QObject *object, const QString
    &newName, const QString &oldName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newName : str
      Passed on as it is: a QString is made of it for the call.

    oldName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::emitObjectNameChanged(
    #      QDesignerFormWindowInterface *formWindow, QObject *object, const
    #      QString &newName, const QString &oldName)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface21emitObjectNameChangedEP2'
        '8QDesignerFormWindowInterfaceP7QObjectRK7QStringS6_',
        self._addressOf(formWindow), self._addressOf(object, 'QObject'),
        newName, oldName,
    )

  @overload(str, str, QStringList)
  def emitNavigateToSlot(
      self,
      objectName: str,
      signalSignature: str,
      parameterNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::emitNavigateToSlot(const
    QString &objectName, const QString &signalSignature, const QStringList
    &parameterNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    objectName : str
      Passed on as it is: a QString is made of it for the call.

    signalSignature : str
      Passed on as it is: a QString is made of it for the call.

    parameterNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerIntegrationInterface::emitNavigateToSlot(const QString
    #      &objectName, const QString &signalSignature, const QStringList
    #      &parameterNames)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface18emitNavigateToSlotERK7QS'
        'tringS2_RK5QListIS0_E',
        objectName, signalSignature, self._valueOf(parameterNames),
    )

  @overload(str)
  def emitNavigateToSlot(self, slotSignature: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::emitNavigateToSlot(const
    QString &slotSignature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    slotSignature : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::emitNavigateToSlot(const QString
    #      &slotSignature)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface18emitNavigateToSlotERK7QS'
        'tring',
        slotSignature,
    )

  @overload(str, str)
  def emitHelpRequested(self, manual: str, document: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::emitHelpRequested(const
    QString &manual, const QString &document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    manual : str
      Passed on as it is: a QString is made of it for the call.

    document : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::emitHelpRequested(const QString
    #      &manual, const QString &document)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface17emitHelpRequestedERK7QSt'
        'ringS2_',
        manual, document,
    )

  @overload(QDesignerFormWindowInterface, str, QVariant)
  @overload(NoneType, str, QVariant)
  def propertyChanged(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      name: str,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::propertyChanged(
    QDesignerFormWindowInterface *formWindow, const QString &name, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#propertyChanged

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerIntegrationInterface::propertyChanged(
    #      QDesignerFormWindowInterface *formWindow, const QString &name,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface15propertyChangedEP28QDesi'
        'gnerFormWindowInterfaceRK7QStringRK8QVariant',
        self._addressOf(formWindow), name, self._valueOf(value),
    )

  @overload(QDesignerFormWindowInterface, QObject, str, str)
  @overload(QDesignerFormWindowInterface, NoneType, str, str)
  @overload(NoneType, QObject, str, str)
  @overload(NoneType, NoneType, str, str)
  def objectNameChanged(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      object: Optional[QObject],
      newName: str,
      oldName: str,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::objectNameChanged(
    QDesignerFormWindowInterface *formWindow, QObject *object, const QString
    &newName, const QString &oldName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newName : str
      Passed on as it is: a QString is made of it for the call.

    oldName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::objectNameChanged(
    #      QDesignerFormWindowInterface *formWindow, QObject *object, const
    #      QString &newName, const QString &oldName)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface17objectNameChangedEP28QDe'
        'signerFormWindowInterfaceP7QObjectRK7QStringS6_',
        self._addressOf(formWindow), self._addressOf(object, 'QObject'),
        newName, oldName,
    )

  @overload(str, str)
  def helpRequested(self, manual: str, document: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::helpRequested(const
    QString &manual, const QString &document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#helpRequested

    Parameters
    ----------

    manual : str
      Passed on as it is: a QString is made of it for the call.

    document : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::helpRequested(const QString
    #      &manual, const QString &document)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface13helpRequestedERK7QString'
        'S2_',
        manual, document,
    )

  @overload(str, str, QStringList)
  def navigateToSlot(
      self,
      objectName: str,
      signalSignature: str,
      parameterNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::navigateToSlot(const
    QString &objectName, const QString &signalSignature, const QStringList
    &parameterNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#navigateToSlot

    Parameters
    ----------

    objectName : str
      Passed on as it is: a QString is made of it for the call.

    signalSignature : str
      Passed on as it is: a QString is made of it for the call.

    parameterNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerIntegrationInterface::navigateToSlot(const QString
    #      &objectName, const QString &signalSignature, const QStringList
    #      &parameterNames)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface14navigateToSlotERK7QStrin'
        'gS2_RK5QListIS0_E',
        objectName, signalSignature, self._valueOf(parameterNames),
    )

  @overload(str)
  def navigateToSlot(self, slotSignature: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::navigateToSlot(const
    QString &slotSignature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#navigateToSlot

    Parameters
    ----------

    slotSignature : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::navigateToSlot(const QString
    #      &slotSignature)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface14navigateToSlotERK7QStrin'
        'g',
        slotSignature,
    )

  @overload(str, QVariant, bool)
  def updateProperty(
      self,
      name: str,
      value: QVariant,
      enableSubPropertyHandling: bool,
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::updateProperty(const
    QString &name, const QVariant &value, bool enableSubPropertyHandling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#updateProperty

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
    #  void QDesignerIntegrationInterface::updateProperty(const QString
    #      &name, const QVariant &value, bool enableSubPropertyHandling)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStrin'
        'gRK8QVariantb',
        name, self._valueOf(value), enableSubPropertyHandling,
    )

  @overload(str, QVariant)
  def updateProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::updateProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#updateProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerIntegrationInterface::updateProperty(const QString
    #      &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStrin'
        'gRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(str)
  def resetProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::resetProperty(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#resetProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::resetProperty(const QString &name)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface13resetPropertyERK7QString',
        name,
    )

  @overload(str, QVariant)
  def addDynamicProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::addDynamicProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerIntegrationInterface::addDynamicProperty(const QString
    #      &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface18addDynamicPropertyERK7QS'
        'tringRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(str)
  def removeDynamicProperty(self, name: str) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegrationInterface::removeDynamicProperty(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerIntegrationInterface::removeDynamicProperty(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface21removeDynamicPropertyERK'
        '7QString',
        name,
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def updateActiveFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::updateActiveFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerIntegrationInterface::updateActiveFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface22updateActiveFormWindowEP'
        '28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setupFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::setupFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#setupFormWindow

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerIntegrationInterface::setupFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface15setupFormWindowEP28QDesi'
        'gnerFormWindowInterface',
        self._addressOf(formWindow),
    )

  def updateSelection(self) -> None:
    """
    Calls Qt's 'void QDesignerIntegrationInterface::updateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html#updateSelection
    """
    #  void QDesignerIntegrationInterface::updateSelection()
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface15updateSelectionEv',
    )

  def updateCustomWidgetPlugins(self) -> None:
    """
    Calls Qt's 'void
    QDesignerIntegrationInterface::updateCustomWidgetPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerintegrationinterface.html
    """
    #  void QDesignerIntegrationInterface::updateCustomWidgetPlugins()
    self.uglySide.call(
        'ritual_ZN29QDesignerIntegrationInterface25updateCustomWidgetPlugin'
        'sEv',
    )
