"""
qdesigner_internal::FormWindowBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/formwindowbase_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::FormWindowBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList
from ..QtWidgets import QWidget
from . import QDesignerFormWindowInterface, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QVariant
  from ..QtWidgets import QMenu
  from . import QDesignerDnDItemInterface, QDesignerPropertySheet
  from . import QtResourceSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDnDItemInterface = WAIT['QDesignerDnDItemInterface']
  QDesignerPropertySheet = WAIT['QDesignerPropertySheet']
  QPoint = WAIT['QPoint']
  QVariant = WAIT['QVariant']
  QtResourceSet = WAIT['QtResourceSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FormWindowBase(QDesignerFormWindowInterface):
  """
  The cute side of Qt's qdesigner_internal::FormWindowBase: a plain Python
  object standing in front of one C++ qdesigner_internal::FormWindowBase.

  It is built on the cute 'QDesignerFormWindowInterface', as Qt's
  qdesigner_internal::FormWindowBase is built on Qt's
  QDesignerFormWindowInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::FormWindowBase that has a ritual
  and that Python can call so far, 57 names in all: 'metaObject', 'tr',
  'formData', 'setFormData', 'checkContents', 'grid', 'setGrid',
  'hasFeature', 'features', 'setFeatures', 'designerGrid', 'setDesignerGrid',
  'hasFormGrid', 'setHasFormGrid', 'gridVisible', 'resourceFileSaveMode',
  'setResourceFileSaveMode', 'defaultDesignerGrid', 'setDefaultDesignerGrid',
  'initializePopupMenu', 'createExtensionTaskMenu', 'dropWidgets',
  'widgetUnderMouse', 'widgetAt', 'findContainer', 'deleteWidgetList',
  'highlightWidget', 'paste', 'createFormBuilder', 'blockSelectionChanged',
  'pixmapCache', 'iconCache', 'resourceSet', 'setResourceSet',
  'addReloadableProperty', 'removeReloadableProperty',
  'addReloadablePropertySheet', 'reloadProperties', 'emitWidgetRemoved',
  'emitObjectRemoved', 'deviceProfile', 'styleName', 'deviceProfileName',
  'setLineTerminatorMode', 'lineTerminatorMode', 'useIdBasedTranslations',
  'setUseIdBasedTranslations', 'idBasedTranslationLabel',
  'setIdBasedTranslationLabel', 'connectSlotsByName',
  'setConnectSlotsByName', 'resourceSetActivated', 'triggerDefaultAction',
  'sheetDestroyed', 'syncGridFeature', 'connectSheet', 'disconnectSheet'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::FormWindowBase::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::FormWindowBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::FormWindowBase::~FormWindowBase()': the
    destructor: Python never removes a C++
    qdesigner_internal::FormWindowBase.

  What has no ritual
  ------------------

  3 of the 63 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::FormWindowBase is created at the first use,
    not by 'qdesigner_internal::FormWindowBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::FormWindowBase.
  - Qt tells when it has removed the C++ qdesigner_internal::FormWindowBase.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::FormWindowBase that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::FormWindowBase, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class HighlightMode(CuteNum):
    """
    The enum 'qdesigner_internal::FormWindowBase::HighlightMode' of Qt, with
    the 2 names Qt gives in it.
    """

    Restore = Kee[int](0)
    Highlight = Kee[int](1)

  class LineTerminatorMode(CuteNum):
    """
    The enum 'qdesigner_internal::FormWindowBase::LineTerminatorMode' of Qt,
    with the 3 names Qt gives in it.
    """

    LFLineTerminator = Kee[int](0)
    CRLFLineTerminator = Kee[int](1)
    NativeLineTerminator = Kee[int](0)

  class PasteMode(CuteNum):
    """
    The enum 'qdesigner_internal::FormWindowBase::PasteMode' of Qt, with the
    2 names Qt gives in it.
    """

    PasteAll = Kee[int](0)
    PasteActionsOnly = Kee[int](1)

  class WidgetUnderMouseMode(CuteNum):
    """
    The enum 'qdesigner_internal::FormWindowBase::WidgetUnderMouseMode' of
    Qt, with the 2 names Qt gives in it.
    """

    FindSingleSelectionDropTarget = Kee[int](0)
    FindMultiSelectionDropTarget = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::FormWindowBase::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#tr

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
    #  QString qdesigner_internal::FormWindowBase::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultDesignerGrid() -> qdesigner_internal.Grid:
    """
    Calls Qt's 'const Grid
    &qdesigner_internal::FormWindowBase::defaultDesignerGrid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    qdesigner_internal.Grid
      A new cute qdesigner_internal::Grid around the copy Qt gave back.
      Python owns it.
    """
    #  const Grid &qdesigner_internal::FormWindowBase::defaultDesignerGrid()
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase19defaultDesignerGrid'
        'Ev',
    )
    return qdesigner_internal.Grid._cuteOwning(address)

  @staticmethod
  @overload(WAIT['qdesigner_internal.Grid'])
  def setDefaultDesignerGrid(grid: qdesigner_internal.Grid) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setDefaultDesignerGrid(const Grid
    &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    grid : qdesigner_internal.Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  void qdesigner_internal::FormWindowBase::setDefaultDesignerGrid(const
    #      Grid &grid)
    Rituals.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase22setDefaultDesignerG'
        'ridERKNS_4GridE',
        CuteMixin._valueOf(grid),
    )

  @staticmethod
  @overload(QDesignerFormWindowInterface, QObject)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormWindowInterface, QObject, bool)
  @overload(QDesignerFormWindowInterface, NoneType, bool)
  @overload(NoneType, QObject, bool)
  @overload(NoneType, NoneType, bool)
  def createExtensionTaskMenu(
      fw: Optional[QDesignerFormWindowInterface],
      o: Optional[QObject],
      trailingSeparator: bool = True,
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu
    *qdesigner_internal::FormWindowBase::createExtensionTaskMenu(
    QDesignerFormWindowInterface *fw, QObject *o, bool trailingSeparator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    trailingSeparator : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *qdesigner_internal::FormWindowBase::createExtensionTaskMenu(
    #      QDesignerFormWindowInterface *fw, QObject *o, bool
    #      trailingSeparator)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase23createExtensionTask'
        'MenuEP28QDesignerFormWindowInterfaceP7QObjectb',
        CuteMixin._addressOf(fw), CuteMixin._addressOf(o, 'QObject'),
        trailingSeparator,
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::FormWindowBase'

  #  A C++ qdesigner_internal::FormWindowBase Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_FormWindowBase'

  #  The functions Qt calls itself that qdesigner_internal::FormWindowBase is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dropWidgets': (
          'bool qdesigner_internal::FormWindowBase::dropWidgets(const '
          'QList<QDesignerDnDItemInterface *> &, QWidget *, const QPoint &)',
      ),
  }

  #  The functions Qt calls itself that qdesigner_internal::FormWindowBase is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initializePopupMenu': (
          ('_ZN18qdesigner_internal14FormWindowBase19initializePopupMenuEP7'
           'QWidget',
           ('address', 'address', 'QtWidgets:QMenu'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'widgetAt': (
          ('_ZN18qdesigner_internal14FormWindowBase8widgetAtERK6QPoint',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'findContainer': (
          ('_ZNK18qdesigner_internal14FormWindowBase13findContainerEP7QWidg'
           'etb',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('bool', 'number', ''),
           )),
      ),
      'highlightWidget': (
          ('_ZN18qdesigner_internal14FormWindowBase15highlightWidgetEP7QWid'
           'getRK6QPointNS0_13HighlightModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QPoint'),
               ('int', 'enum',
                'QtDesigner:qdesigner_internal.FormWindowBase.HighlightMode'),
           )),
      ),
      'paste': (
          ('_ZN18qdesigner_internal14FormWindowBase5pasteENS0_9PasteModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDesigner:qdesigner_internal.FormWindowBase.PasteMode'),
           )),
      ),
      'createFormBuilder': (
          ('_ZN18qdesigner_internal14FormWindowBase17createFormBuilderEv',
           ('address', 'address',
            'QtDesigner:qdesigner_internal.QEditorFormBuilder'),
           ()),
      ),
      'blockSelectionChanged': (
          ('_ZN18qdesigner_internal14FormWindowBase21blockSelectionChangedE'
           'b',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::FormWindowBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::FormWindowBase::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def checkContents(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::FormWindowBase::checkContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::FormWindowBase::checkContents() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase13checkContentsEv',
    )
    return QStringList._cuteOwning(address)

  def grid(self) -> QPoint:
    """
    Calls Qt's 'QPoint qdesigner_internal::FormWindowBase::grid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#grid

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::FormWindowBase::grid() const
    ritual = 'ritual_ZNK18qdesigner_internal14FormWindowBase4gridEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal14FormWindowBase4gridEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QDesignerFormWindowInterface.Feature)
  def hasFeature(self, f: QDesignerFormWindowInterface.Feature) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormWindowBase::hasFeature(Feature
    f) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#hasFeature

    Parameters
    ----------

    f : QDesignerFormWindowInterface.Feature
      Passed on as its number.
    """
    #  bool qdesigner_internal::FormWindowBase::hasFeature(Feature f) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14FormWindowBase10hasFeatureE6QFlags'
        'IN28QDesignerFormWindowInterface11FeatureFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14FormWindowBase10hasFeatureE6'
          'QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE')
    return self.uglySide.call(ritual, f.value)

  def features(self) -> QDesignerFormWindowInterface.Feature:
    """
    Calls Qt's 'Feature qdesigner_internal::FormWindowBase::features()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#features

    Returns
    -------

    QDesignerFormWindowInterface.Feature
      The value standing for the combination Qt gave back.
    """
    #  Feature qdesigner_internal::FormWindowBase::features() const
    ritual = 'ritual_ZNK18qdesigner_internal14FormWindowBase8featuresEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14FormWindowBase8featuresEv')
    return QDesignerFormWindowInterface.Feature(self.uglySide.call(ritual))

  def designerGrid(self) -> qdesigner_internal.Grid:
    """
    Calls Qt's 'const Grid
    &qdesigner_internal::FormWindowBase::designerGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    qdesigner_internal.Grid
      A new cute qdesigner_internal::Grid around the copy Qt gave back.
      Python owns it.
    """
    #  const Grid &qdesigner_internal::FormWindowBase::designerGrid() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase12designerGridEv',
    )
    return qdesigner_internal.Grid._cuteOwning(address)

  def hasFormGrid(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormWindowBase::hasFormGrid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#hasFormGrid
    """
    #  bool qdesigner_internal::FormWindowBase::hasFormGrid() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase11hasFormGridEv',
    )

  def gridVisible(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormWindowBase::gridVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#gridVisible
    """
    #  bool qdesigner_internal::FormWindowBase::gridVisible() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase11gridVisibleEv',
    )

  def resourceFileSaveMode(
      self,
  ) -> QDesignerFormWindowInterface.ResourceFileSaveMode:
    """
    Calls Qt's 'ResourceFileSaveMode
    qdesigner_internal::FormWindowBase::resourceFileSaveMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    QDesignerFormWindowInterface.ResourceFileSaveMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDesignerFormWindowInterface.ResourceFileSaveMode(number)' gives.
    """
    #  ResourceFileSaveMode
    #      qdesigner_internal::FormWindowBase::resourceFileSaveMode() const
    ritual = (
        'ritual_ZNK18qdesigner_internal14FormWindowBase20resourceFileSaveMo'
        'deEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14FormWindowBase20resourceFile'
          'SaveModeEv')
    return QDesignerFormWindowInterface.ResourceFileSaveMode(
        self.uglySide.call(
            'ritual_ZNK18qdesigner_internal14FormWindowBase20resourceFileSa'
            'veModeEv',
        ))

  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def findContainer(
      self,
      w: Optional[QWidget],
      excludeLayout: bool,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::FormWindowBase::findContainer(QWidget *w, bool
    excludeLayout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    excludeLayout : bool
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::FormWindowBase::findContainer(QWidget *w,
    #      bool excludeLayout) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase13findContainerEP7QW'
        'idgetb',
        self._addressOf(w), excludeLayout,
    )
    return QWidget._cuteAt(address)

  def pixmapCache(self) -> Optional[qdesigner_internal.DesignerPixmapCache]:
    """
    Calls Qt's 'DesignerPixmapCache
    *qdesigner_internal::FormWindowBase::pixmapCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#pixmapCache

    Returns
    -------

    Optional[qdesigner_internal.DesignerPixmapCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DesignerPixmapCache *qdesigner_internal::FormWindowBase::pixmapCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase11pixmapCacheEv',
    )
    return qdesigner_internal.DesignerPixmapCache._cuteAt(address)

  def iconCache(self) -> Optional[qdesigner_internal.DesignerIconCache]:
    """
    Calls Qt's 'DesignerIconCache
    *qdesigner_internal::FormWindowBase::iconCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#iconCache

    Returns
    -------

    Optional[qdesigner_internal.DesignerIconCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DesignerIconCache *qdesigner_internal::FormWindowBase::iconCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase9iconCacheEv',
    )
    return qdesigner_internal.DesignerIconCache._cuteAt(address)

  def resourceSet(self) -> Optional[QtResourceSet]:
    """
    Calls Qt's 'QtResourceSet
    *qdesigner_internal::FormWindowBase::resourceSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#resourceSet

    Returns
    -------

    Optional[QtResourceSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceSet *qdesigner_internal::FormWindowBase::resourceSet() const
    ritual = 'ritual_ZNK18qdesigner_internal14FormWindowBase11resourceSetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14FormWindowBase11resourceSetE'
          'v')
    address = self.uglySide.call(ritual)
    from . import QtResourceSet
    return QtResourceSet._cuteAt(address)

  def deviceProfile(self) -> qdesigner_internal.DeviceProfile:
    """
    Calls Qt's 'DeviceProfile
    qdesigner_internal::FormWindowBase::deviceProfile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    qdesigner_internal.DeviceProfile
      A new cute qdesigner_internal::DeviceProfile around the copy Qt gave
      back. Python owns it.
    """
    #  DeviceProfile qdesigner_internal::FormWindowBase::deviceProfile()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase13deviceProfileEv',
    )
    return qdesigner_internal.DeviceProfile._cuteOwning(address)

  def styleName(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::FormWindowBase::styleName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::FormWindowBase::styleName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase9styleNameEv',
    )

  def deviceProfileName(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::FormWindowBase::deviceProfileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::FormWindowBase::deviceProfileName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase17deviceProfileNameE'
        'v',
    )

  def lineTerminatorMode(self) -> LineTerminatorMode:
    """
    Calls Qt's 'LineTerminatorMode
    qdesigner_internal::FormWindowBase::lineTerminatorMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    LineTerminatorMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'LineTerminatorMode(number)' gives.
    """
    #  LineTerminatorMode
    #      qdesigner_internal::FormWindowBase::lineTerminatorMode() const
    return FormWindowBase.LineTerminatorMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase18lineTerminatorMode'
        'Ev',
    ))

  def useIdBasedTranslations(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::FormWindowBase::useIdBasedTranslations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html
    """
    #  bool qdesigner_internal::FormWindowBase::useIdBasedTranslations()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase22useIdBasedTranslat'
        'ionsEv',
    )

  def idBasedTranslationLabel(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::FormWindowBase::idBasedTranslationLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::FormWindowBase::idBasedTranslationLabel()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase23idBasedTranslation'
        'LabelEv',
    )

  def connectSlotsByName(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormWindowBase::connectSlotsByName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html
    """
    #  bool qdesigner_internal::FormWindowBase::connectSlotsByName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormWindowBase18connectSlotsByName'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setFormData(self, vm: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::setFormData(const
    QVariantMap &vm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#setFormData

    Parameters
    ----------

    vm : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void qdesigner_internal::FormWindowBase::setFormData(const QVariantMap
    #      &vm)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase11setFormDataERK4QMap'
        'I7QString8QVariantE',
        self._valueOf(vm),
    )

  @overload(QPoint)
  def setGrid(self, grid: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::setGrid(const QPoint
    &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#setGrid

    Parameters
    ----------

    grid : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::FormWindowBase::setGrid(const QPoint &grid)
    ritual = (
        'ritual_ZN18qdesigner_internal14FormWindowBase7setGridERK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14FormWindowBase7setGridERK6QPo'
          'int')
    self.uglySide.call(ritual, self._valueOf(grid))

  @overload(QDesignerFormWindowInterface.Feature)
  def setFeatures(self, f: QDesignerFormWindowInterface.Feature) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::setFeatures(Feature
    f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#setFeatures

    Parameters
    ----------

    f : QDesignerFormWindowInterface.Feature
      Passed on as its number.
    """
    #  void qdesigner_internal::FormWindowBase::setFeatures(Feature f)
    ritual = (
        'ritual_ZN18qdesigner_internal14FormWindowBase11setFeaturesE6QFlags'
        'IN28QDesignerFormWindowInterface11FeatureFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14FormWindowBase11setFeaturesE6'
          'QFlagsIN28QDesignerFormWindowInterface11FeatureFlagEE')
    self.uglySide.call(ritual, f.value)

  @overload(WAIT['qdesigner_internal.Grid'])
  def setDesignerGrid(self, grid: qdesigner_internal.Grid) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setDesignerGrid(const Grid &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    grid : qdesigner_internal.Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  void qdesigner_internal::FormWindowBase::setDesignerGrid(const Grid
    #      &grid)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase15setDesignerGridERKN'
        'S_4GridE',
        self._valueOf(grid),
    )

  @overload(bool)
  def setHasFormGrid(self, b: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::setHasFormGrid(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::FormWindowBase::setHasFormGrid(bool b)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase14setHasFormGridEb', b,
    )

  @overload(QDesignerFormWindowInterface.ResourceFileSaveMode)
  def setResourceFileSaveMode(
      self,
      behavior: QDesignerFormWindowInterface.ResourceFileSaveMode,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setResourceFileSaveMode(
    ResourceFileSaveMode behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    behavior : QDesignerFormWindowInterface.ResourceFileSaveMode
      Passed on as its number.
    """
    #  void qdesigner_internal::FormWindowBase::setResourceFileSaveMode(
    #      ResourceFileSaveMode behavior)
    ritual = (
        'ritual_ZN18qdesigner_internal14FormWindowBase23setResourceFileSave'
        'ModeEN28QDesignerFormWindowInterface20ResourceFileSaveModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14FormWindowBase23setResourceFi'
          'leSaveModeEN28QDesignerFormWindowInterface20ResourceFileSaveMode'
          'E')
    self.uglySide.call(ritual, behavior.value)

  @overload(QtResourceSet)
  @overload(NoneType)
  def setResourceSet(self, resourceSet: Optional[QtResourceSet]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setResourceSet(QtResourceSet
    *resourceSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    resourceSet : Optional[QtResourceSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::setResourceSet(QtResourceSet
    #      *resourceSet)
    ritual = (
        'ritual_ZN18qdesigner_internal14FormWindowBase14setResourceSetEP13Q'
        'tResourceSet')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14FormWindowBase14setResourceSe'
          'tEP13QtResourceSet')
    self.uglySide.call(ritual, self._addressOf(resourceSet))

  @overload(LineTerminatorMode)
  def setLineTerminatorMode(self, mode: LineTerminatorMode) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setLineTerminatorMode(
    LineTerminatorMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    mode : LineTerminatorMode
      Passed on as its number.
    """
    #  void qdesigner_internal::FormWindowBase::setLineTerminatorMode(
    #      LineTerminatorMode mode)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase21setLineTerminatorMo'
        'deENS0_18LineTerminatorModeE',
        mode.value,
    )

  @overload(bool)
  def setUseIdBasedTranslations(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setUseIdBasedTranslations(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void
    #      qdesigner_internal::FormWindowBase::setUseIdBasedTranslations(bool
    #      v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase25setUseIdBasedTransl'
        'ationsEb',
        v,
    )

  @overload(str)
  def setIdBasedTranslationLabel(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setIdBasedTranslationLabel(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::FormWindowBase::setIdBasedTranslationLabel(
    #      const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase26setIdBasedTranslati'
        'onLabelERK7QString',
        a0,
    )

  @overload(bool)
  def setConnectSlotsByName(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::setConnectSlotsByName(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::FormWindowBase::setConnectSlotsByName(bool v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase21setConnectSlotsByNa'
        'meEb',
        v,
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
    Qt's 'qdesigner_internal::FormWindowBase::FormWindowBase(
    QDesignerFormEditorInterface *core, QWidget *parent, Qt::WindowFlags
    flags)': the class is abstract, so C++ cannot make one, and the C++ class
    of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.FormWindowBase.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::FormWindowBase::FormWindowBase(QDesignerFormEd"
        "itorInterface *core, QWidget *parent, Qt::WindowFlags flags)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def formData(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap qdesigner_internal::FormWindowBase::formData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#formData

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap qdesigner_internal::FormWindowBase::formData()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase8formDataEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def initializePopupMenu(
      self,
      managedWidget: Optional[QWidget],
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu
    *qdesigner_internal::FormWindowBase::initializePopupMenu(QWidget
    *managedWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    managedWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *qdesigner_internal::FormWindowBase::initializePopupMenu(QWidget
    #      *managedWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal14FormWindowBase19initializePopupMenu'
        'EP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14FormWindowBase19initializePop'
          'upMenuEP7QWidget')
    address = self.uglySide.call(ritual, self._addressOf(managedWidget))
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  @overload(QList[QDesignerDnDItemInterface], QWidget, QPoint)
  @overload(QList[QDesignerDnDItemInterface], NoneType, QPoint)
  def dropWidgets(
      self,
      item_list: QList[QDesignerDnDItemInterface],
      target: Optional[QWidget],
      global_mouse_pos: QPoint,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormWindowBase::dropWidgets(const
    QList<QDesignerDnDItemInterface *> &item_list, QWidget *target, const
    QPoint &global_mouse_pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#dropWidgets

    Parameters
    ----------

    item_list : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    target : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    global_mouse_pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool qdesigner_internal::FormWindowBase::dropWidgets(const
    #      QList<QDesignerDnDItemInterface *> &item_list, QWidget *target,
    #      const QPoint &global_mouse_pos)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase11dropWidgetsERK5QLis'
        'tIP25QDesignerDnDItemInterfaceEP7QWidgetRK6QPoint',
        self._valueOf(item_list), self._addressOf(target),
        self._valueOf(global_mouse_pos),
    )

  @overload(QPoint, WidgetUnderMouseMode)
  def widgetUnderMouse(
      self,
      formPos: QPoint,
      m: WidgetUnderMouseMode,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::FormWindowBase::widgetUnderMouse(const QPoint
    &formPos, WidgetUnderMouseMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    formPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    m : WidgetUnderMouseMode
      Passed on as its number.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::FormWindowBase::widgetUnderMouse(const
    #      QPoint &formPos, WidgetUnderMouseMode m)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase16widgetUnderMouseERK'
        '6QPointNS0_20WidgetUnderMouseModeE',
        self._valueOf(formPos), m.value,
    )
    return QWidget._cuteAt(address)

  @overload(QPoint)
  def widgetAt(self, pos: QPoint) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::FormWindowBase::widgetAt(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#widgetAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::FormWindowBase::widgetAt(const QPoint
    #      &pos)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase8widgetAtERK6QPoint',
        self._valueOf(pos),
    )
    return QWidget._cuteAt(address)

  @overload(QList[QWidget])
  def deleteWidgetList(self, widget_list: QList[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::deleteWidgetList(const QWidgetList
    &widget_list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    widget_list : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::FormWindowBase::deleteWidgetList(const
    #      QWidgetList &widget_list)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase16deleteWidgetListERK'
        '5QListIP7QWidgetE',
        self._valueOf(widget_list),
    )

  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  @overload(QWidget, QPoint, HighlightMode)
  @overload(NoneType, QPoint, HighlightMode)
  def highlightWidget(
      self,
      w: Optional[QWidget],
      pos: QPoint,
      mode: HighlightMode = HighlightMode.Highlight,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::highlightWidget(QWidget *w, const
    QPoint &pos, HighlightMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    mode : HighlightMode
      Passed on as its number. May be left out, as in Qt: it is then
      HighlightMode.Highlight.
    """
    #  void qdesigner_internal::FormWindowBase::highlightWidget(QWidget *w,
    #      const QPoint &pos, HighlightMode mode)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase15highlightWidgetEP7Q'
        'WidgetRK6QPointNS0_13HighlightModeE',
        self._addressOf(w), self._valueOf(pos), mode.value,
    )

  @overload(PasteMode)
  def paste(self, pasteMode: PasteMode) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::paste(PasteMode
    pasteMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html#paste

    Parameters
    ----------

    pasteMode : PasteMode
      Passed on as its number.
    """
    #  void qdesigner_internal::FormWindowBase::paste(PasteMode pasteMode)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase5pasteENS0_9PasteMode'
        'E',
        pasteMode.value,
    )

  def createFormBuilder(
      self,
  ) -> Optional[qdesigner_internal.QEditorFormBuilder]:
    """
    Calls Qt's 'QEditorFormBuilder
    *qdesigner_internal::FormWindowBase::createFormBuilder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Returns
    -------

    Optional[qdesigner_internal.QEditorFormBuilder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEditorFormBuilder
    #      *qdesigner_internal::FormWindowBase::createFormBuilder()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase17createFormBuilderEv',
    )
    return qdesigner_internal.QEditorFormBuilder._cuteAt(address)

  @overload(bool)
  def blockSelectionChanged(self, blocked: bool) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::FormWindowBase::blockSelectionChanged(bool blocked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    blocked : bool
      Passed on as it is.
    """
    #  bool qdesigner_internal::FormWindowBase::blockSelectionChanged(bool
    #      blocked)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase21blockSelectionChang'
        'edEb',
        blocked,
    )

  @overload(QDesignerPropertySheet, int)
  @overload(NoneType, int)
  def addReloadableProperty(
      self,
      sheet: Optional[QDesignerPropertySheet],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::addReloadableProperty(
    QDesignerPropertySheet *sheet, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    sheet : Optional[QDesignerPropertySheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void qdesigner_internal::FormWindowBase::addReloadableProperty(
    #      QDesignerPropertySheet *sheet, int index)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase21addReloadableProper'
        'tyEP22QDesignerPropertySheeti',
        self._addressOf(sheet), index,
    )

  @overload(QDesignerPropertySheet, int)
  @overload(NoneType, int)
  def removeReloadableProperty(
      self,
      sheet: Optional[QDesignerPropertySheet],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::removeReloadableProperty(
    QDesignerPropertySheet *sheet, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    sheet : Optional[QDesignerPropertySheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void qdesigner_internal::FormWindowBase::removeReloadableProperty(
    #      QDesignerPropertySheet *sheet, int index)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase24removeReloadablePro'
        'pertyEP22QDesignerPropertySheeti',
        self._addressOf(sheet), index,
    )

  @overload(QDesignerPropertySheet, QObject)
  @overload(QDesignerPropertySheet, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def addReloadablePropertySheet(
      self,
      sheet: Optional[QDesignerPropertySheet],
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::addReloadablePropertySheet(
    QDesignerPropertySheet *sheet, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    sheet : Optional[QDesignerPropertySheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::addReloadablePropertySheet(
    #      QDesignerPropertySheet *sheet, QObject *object)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase26addReloadableProper'
        'tySheetEP22QDesignerPropertySheetP7QObject',
        self._addressOf(sheet), self._addressOf(object, 'QObject'),
    )

  def reloadProperties(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::reloadProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html
    """
    #  void qdesigner_internal::FormWindowBase::reloadProperties()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase16reloadPropertiesEv',
    )

  @overload(QWidget)
  @overload(NoneType)
  def emitWidgetRemoved(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::emitWidgetRemoved(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::emitWidgetRemoved(QWidget *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase17emitWidgetRemovedEP'
        '7QWidget',
        self._addressOf(w),
    )

  @overload(QObject)
  @overload(NoneType)
  def emitObjectRemoved(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::emitObjectRemoved(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::emitObjectRemoved(QObject *o)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase17emitObjectRemovedEP'
        '7QObject',
        self._addressOf(o, 'QObject'),
    )

  @overload(QtResourceSet, bool)
  @overload(NoneType, bool)
  def resourceSetActivated(
      self,
      resourceSet: Optional[QtResourceSet],
      resourceSetChanged: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::resourceSetActivated(QtResourceSet
    *resourceSet, bool resourceSetChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    resourceSet : Optional[QtResourceSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceSetChanged : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::FormWindowBase::resourceSetActivated(
    #      QtResourceSet *resourceSet, bool resourceSetChanged)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase20resourceSetActivate'
        'dEP13QtResourceSetb',
        self._addressOf(resourceSet), resourceSetChanged,
    )

  @overload(QWidget)
  @overload(NoneType)
  def triggerDefaultAction(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::triggerDefaultAction(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::triggerDefaultAction(QWidget
    #      *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase20triggerDefaultActio'
        'nEP7QWidget',
        self._addressOf(w),
    )

  @overload(QObject)
  @overload(NoneType)
  def sheetDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::sheetDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::sheetDestroyed(QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase14sheetDestroyedEP7QO'
        'bject',
        self._addressOf(object, 'QObject'),
    )

  def syncGridFeature(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::syncGridFeature()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html
    """
    #  void qdesigner_internal::FormWindowBase::syncGridFeature()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase15syncGridFeatureEv',
    )

  @overload(QDesignerPropertySheet)
  @overload(NoneType)
  def connectSheet(self, sheet: Optional[QDesignerPropertySheet]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::FormWindowBase::connectSheet(QDesignerPropertySheet
    *sheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    sheet : Optional[QDesignerPropertySheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::connectSheet(
    #      QDesignerPropertySheet *sheet)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase12connectSheetEP22QDe'
        'signerPropertySheet',
        self._addressOf(sheet),
    )

  @overload(QDesignerPropertySheet)
  @overload(NoneType)
  def disconnectSheet(self, sheet: Optional[QDesignerPropertySheet]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormWindowBase::disconnectSheet(
    QDesignerPropertySheet *sheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formwindowbase.html

    Parameters
    ----------

    sheet : Optional[QDesignerPropertySheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::FormWindowBase::disconnectSheet(
    #      QDesignerPropertySheet *sheet)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormWindowBase15disconnectSheetEP22'
        'QDesignerPropertySheet',
        self._addressOf(sheet),
    )
