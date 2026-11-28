"""
QQStyleKitReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitreader_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitReader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQSK, QQStyleKitControlProperties

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QFont, QPalette
  from . import QQStyleKitStyle
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickPalette, QQuickStateGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQStyleKitStyle = WAIT['QQStyleKitStyle']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickPalette = WAIT['QQuickPalette']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitReader(QQStyleKitControlProperties):
  """
  The cute side of Qt's QQStyleKitReader: a plain Python object standing in
  front of one C++ QQStyleKitReader.

  It is built on the cute 'QQStyleKitControlProperties', as Qt's
  QQStyleKitReader is built on Qt's QQStyleKitControlProperties, and has
  everything that class has. Qt's QQStyleKitReader is built on Qt's
  QQmlParserStatus as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQStyleKitReader that has a ritual and that Python
  can call so far, 62 names in all: 'metaObject', 'tr', 'controlType',
  'setControlType', 'typeAsControlType', 'hovered', 'setHovered', 'enabled',
  'setEnabled', 'focused', 'setFocused', 'checked', 'setChecked', 'pressed',
  'setPressed', 'palette', 'setPalette', 'effectivePalette', 'vertical',
  'setVertical', 'highlighted', 'setHighlighted', 'explicitStyle',
  'setExplicitStyle', 'font', 'global_', 'readStyleProperty',
  'writeStyleProperty', 'clearLocalStorage', 'controlState',
  'setControlTypeAndState', 'target', 'setTarget', 'setCompleted',
  'transitionsEnabled', 'setTransitionsEnabled', 'resetReadersForStyle',
  'controlTypeChanged', 'customTypeChanged', 'propertiesChanged',
  'enabledChanged', 'focusedChanged', 'checkedChanged', 'hoveredChanged',
  'pressedChanged', 'paletteChanged', 'verticalChanged',
  'highlightedChanged', 'fontChanged', 'onPaletteChanged', 'classBegin',
  'componentComplete', 'updateControl', 'populateLocalStorage',
  'dontEmitChangedSignals', 'stateGroup', 'createControlChangesComponent',
  'createDelegateChangesComponent', 'instantiatePropertyChanges',
  'maybeTrackDelegates', 'rebuildEffectivePalette', 'rebuildEffectiveFont'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitReader::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitReader::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQStyleKitReader::~QQStyleKitReader()': the destructor: Python
    never removes a C++ QQStyleKitReader.

  What has no ritual
  ------------------

  4 of the 70 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQStyleKitReader is created at the first use, not by
    'QQStyleKitReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitReader.
  - Qt tells when it has removed the C++ QQStyleKitReader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQStyleKitReader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AlternateState(CuteNum, scoped=True):
    """
    The enum 'QQStyleKitReader::AlternateState' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Alternate1 = Kee[int](0)
    Alternate2 = Kee[int](1)

  class ControlType(CuteNum):
    """
    The enum 'QQStyleKitReader::ControlType' of Qt, with the 48 names Qt
    gives in it.
    """

    Unspecified = Kee[int](100000)
    Control = Kee[int](100001)
    AbstractButton = Kee[int](100002)
    ApplicationWindow = Kee[int](100003)
    BusyIndicator = Kee[int](100004)
    Button = Kee[int](100005)
    CheckBox = Kee[int](100006)
    CheckDelegate = Kee[int](100007)
    ComboBox = Kee[int](100008)
    DelayButton = Kee[int](100009)
    Dial = Kee[int](100010)
    Dialog = Kee[int](100011)
    DialogButtonBox = Kee[int](100012)
    FlatButton = Kee[int](100013)
    ProgressBar = Kee[int](100014)
    ScrollBar = Kee[int](100015)
    ScrollIndicator = Kee[int](100016)
    ScrollView = Kee[int](100017)
    Slider = Kee[int](100018)
    SpinBox = Kee[int](100019)
    SwipeDelegate = Kee[int](100020)
    SwitchControl = Kee[int](100021)
    SwitchDelegate = Kee[int](100022)
    SearchField = Kee[int](100023)
    TabBar = Kee[int](100024)
    TabButton = Kee[int](100025)
    TextArea = Kee[int](100026)
    TextField = Kee[int](100027)
    TextInput = Kee[int](100028)
    ToolBar = Kee[int](100029)
    ToolButton = Kee[int](100030)
    ToolSeparator = Kee[int](100031)
    RadioButton = Kee[int](100032)
    RadioDelegate = Kee[int](100033)
    RoundButton = Kee[int](100034)
    ItemDelegate = Kee[int](100035)
    Popup = Kee[int](100036)
    Menu = Kee[int](100037)
    MenuBar = Kee[int](100038)
    MenuBarItem = Kee[int](100039)
    MenuItem = Kee[int](100040)
    MenuSeparator = Kee[int](100041)
    Pane = Kee[int](100042)
    Page = Kee[int](100043)
    PageIndicator = Kee[int](100044)
    Frame = Kee[int](100045)
    Label = Kee[int](100046)
    GroupBox = Kee[int](100047)

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
    Calls Qt's 'QString QQStyleKitReader::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#tr

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
    #  QString QQStyleKitReader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQStyleKitReader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQStyleKitStyle)
  @overload(NoneType)
  def resetReadersForStyle(style: Optional[QQStyleKitStyle]) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::resetReadersForStyle(const
    QQStyleKitStyle *style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#resetReadersForStyle

    Parameters
    ----------

    style : Optional[QQStyleKitStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitReader::resetReadersForStyle(const QQStyleKitStyle
    #      *style)
    Rituals.call(
        'ritual_ZN16QQStyleKitReader20resetReadersForStyleEPK15QQStyleKitSt'
        'yle',
        CuteMixin._addressOf(style),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitReader'

  #  A C++ QQStyleKitReader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitReader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitReader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def controlType(self) -> int:
    """
    Calls Qt's 'QQStyleKitExtendableControlType
    QQStyleKitReader::controlType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#controlType
    """
    #  QQStyleKitExtendableControlType QQStyleKitReader::controlType() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader11controlTypeEv')

  def typeAsControlType(self) -> ControlType:
    """
    Calls Qt's 'ControlType QQStyleKitReader::typeAsControlType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#typeAsControlType

    Returns
    -------

    ControlType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ControlType(number)'
      gives.
    """
    #  ControlType QQStyleKitReader::typeAsControlType() const
    return QQStyleKitReader.ControlType(self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader17typeAsControlTypeEv',
    ))

  def hovered(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::hovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#hovered
    """
    #  bool QQStyleKitReader::hovered() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader7hoveredEv')

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#enabled
    """
    #  bool QQStyleKitReader::enabled() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader7enabledEv')

  def focused(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::focused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#focused
    """
    #  bool QQStyleKitReader::focused() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader7focusedEv')

  def checked(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::checked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#checked
    """
    #  bool QQStyleKitReader::checked() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader7checkedEv')

  def pressed(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::pressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#pressed
    """
    #  bool QQStyleKitReader::pressed() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader7pressedEv')

  def palette(self) -> Optional[QQuickPalette]:
    """
    Calls Qt's 'QQuickPalette *QQStyleKitReader::palette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#palette

    Returns
    -------

    Optional[QQuickPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPalette *QQStyleKitReader::palette() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitReader7paletteEv')
    from ..QtQuick import QQuickPalette
    return QQuickPalette._cuteAt(address)

  def effectivePalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQStyleKitReader::effectivePalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#effectivePalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQStyleKitReader::effectivePalette() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader16effectivePaletteEv',
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def vertical(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::vertical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#vertical
    """
    #  bool QQStyleKitReader::vertical() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader8verticalEv')

  def highlighted(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::highlighted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#highlighted
    """
    #  bool QQStyleKitReader::highlighted() const
    return self.uglySide.call('ritual_ZNK16QQStyleKitReader11highlightedEv')

  def explicitStyle(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitReader::explicitStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#explicitStyle

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitReader::explicitStyle() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader13explicitStyleEv',
    )
    from . import QQStyleKitStyle
    return QQStyleKitStyle._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQStyleKitReader::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQStyleKitReader::font() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitReader4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def global_(self) -> Optional[QQStyleKitControlProperties]:
    """
    Calls Qt's 'QQStyleKitControlProperties *QQStyleKitReader::global()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#global

    Returns
    -------

    Optional[QQStyleKitControlProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitControlProperties *QQStyleKitReader::global() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitReader6globalEv')
    return QQStyleKitControlProperties._cuteAt(address)

  @overload(int)
  def readStyleProperty(self, key: int) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQStyleKitReader::readStyleProperty(PropertyStorageId key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#readStyleProperty

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQStyleKitReader::readStyleProperty(PropertyStorageId key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader17readStylePropertyEj', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def controlState(self) -> QQSK.State:
    """
    Calls Qt's 'QQSK::State QQStyleKitReader::controlState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#controlState

    Returns
    -------

    QQSK.State
      The value standing for the combination Qt gave back.
    """
    #  QQSK::State QQStyleKitReader::controlState() const
    return QQSK.State(self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader12controlStateEv',
    ))

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQStyleKitReader::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQStyleKitReader::target() const
    address = self.uglySide.call('ritual_ZNK16QQStyleKitReader6targetEv')
    return QObject._cuteAt(address)

  def transitionsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::transitionsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#transitionsEnabled
    """
    #  bool QQStyleKitReader::transitionsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader18transitionsEnabledEv',
    )

  def dontEmitChangedSignals(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::dontEmitChangedSignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#dontEmitChangedSignals
    """
    #  bool QQStyleKitReader::dontEmitChangedSignals() const
    return self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader22dontEmitChangedSignalsEv',
    )

  def createControlChangesComponent(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *QQStyleKitReader::createControlChangesComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitReader::createControlChangesComponent() const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader29createControlChangesComponentEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  @overload(str)
  def createDelegateChangesComponent(
      self,
      delegateName: str,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *QQStyleKitReader::createDelegateChangesComponent(const QString
    &delegateName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html

    Parameters
    ----------

    delegateName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitReader::createDelegateChangesComponent(const
    #      QString &delegateName) const
    address = self.uglySide.call(
        'ritual_ZNK16QQStyleKitReader30createDelegateChangesComponentERK7QS'
        'tring',
        delegateName,
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setControlType(self, type: int) -> None:
    """
    Calls Qt's 'void
    QQStyleKitReader::setControlType(QQStyleKitExtendableControlType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#setControlType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QQStyleKitReader::setControlType(QQStyleKitExtendableControlType
    #      type)
    self.uglySide.call('ritual_ZN16QQStyleKitReader14setControlTypeEj', type)

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setHovered(bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setHovered(bool hovered)
    self.uglySide.call('ritual_ZN16QQStyleKitReader10setHoveredEb', hovered)

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN16QQStyleKitReader10setEnabledEb', enabled)

  @overload(bool)
  def setFocused(self, focused: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setFocused(bool focused)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setFocused

    Parameters
    ----------

    focused : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setFocused(bool focused)
    self.uglySide.call('ritual_ZN16QQStyleKitReader10setFocusedEb', focused)

  @overload(bool)
  def setChecked(self, checked: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setChecked(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setChecked

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setChecked(bool checked)
    self.uglySide.call('ritual_ZN16QQStyleKitReader10setCheckedEb', checked)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN16QQStyleKitReader10setPressedEb', pressed)

  @overload(QQuickPalette)
  @overload(NoneType)
  def setPalette(self, palette: Optional[QQuickPalette]) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setPalette(QQuickPalette *palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setPalette

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitReader::setPalette(QQuickPalette *palette)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader10setPaletteEP13QQuickPalette',
        self._addressOf(palette),
    )

  @overload(bool)
  def setVertical(self, vertical: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setVertical(bool vertical)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setVertical

    Parameters
    ----------

    vertical : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setVertical(bool vertical)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader11setVerticalEb', vertical,
    )

  @overload(bool)
  def setHighlighted(self, highlighted: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setHighlighted(bool highlighted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#setHighlighted

    Parameters
    ----------

    highlighted : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setHighlighted(bool highlighted)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader14setHighlightedEb', highlighted,
    )

  @overload(QQStyleKitStyle)
  @overload(NoneType)
  def setExplicitStyle(self, style: Optional[QQStyleKitStyle]) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setExplicitStyle(QQStyleKitStyle
    *style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#setExplicitStyle

    Parameters
    ----------

    style : Optional[QQStyleKitStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitReader::setExplicitStyle(QQStyleKitStyle *style)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader16setExplicitStyleEP15QQStyleKitStyle',
        self._addressOf(style),
    )

  @overload(int, QQSK.State)
  @overload(int, QQSK.State, bool)
  def setControlTypeAndState(
      self,
      controlType: int,
      flags: QQSK.State,
      applyStateChange: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitReader::setControlTypeAndState(QQStyleKitExtendableControlType
    controlType, QQSK::State flags, bool applyStateChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#setControlTypeAndState

    Parameters
    ----------

    controlType : int
      Passed on as it is.

    flags : QQSK.State
      Passed on as its number.

    applyStateChange : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQStyleKitReader::setControlTypeAndState(
    #      QQStyleKitExtendableControlType controlType, QQSK::State flags,
    #      bool applyStateChange)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader22setControlTypeAndStateEj6QFlagsIN4QQS'
        'K9StateFlagEEb',
        controlType, flags.value, applyStateChange,
    )

  @overload(QObject)
  @overload(NoneType)
  def setTarget(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setTarget(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setTarget

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitReader::setTarget(QObject *target)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader9setTargetEP7QObject',
        self._addressOf(target, 'QObject'),
    )

  @overload(bool)
  def setCompleted(self, completed: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setCompleted(bool completed)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#setCompleted

    Parameters
    ----------

    completed : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setCompleted(bool completed)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader12setCompletedEb', completed,
    )

  @overload(bool)
  def setTransitionsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::setTransitionsEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#setTransitionsEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQStyleKitReader::setTransitionsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader21setTransitionsEnabledEb', enabled,
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
    'QQStyleKitReader::QQStyleKitReader(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#QQStyleKitReader

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitReader::QQStyleKitReader(QObject *parent)
    self._noteCreation(QQStyleKitReader, lambda: Rituals.call(
        'ritual_ZN16QQStyleKitReaderC1EP7QObject',
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

  @overload(int, QVariant)
  def writeStyleProperty(self, key: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::writeStyleProperty(PropertyStorageId
    key, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#writeStyleProperty

    Parameters
    ----------

    key : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQStyleKitReader::writeStyleProperty(PropertyStorageId key, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader18writeStylePropertyEjRK8QVariant',
        key, self._valueOf(value),
    )

  def clearLocalStorage(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::clearLocalStorage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#clearLocalStorage
    """
    #  void QQStyleKitReader::clearLocalStorage()
    self.uglySide.call('ritual_ZN16QQStyleKitReader17clearLocalStorageEv')

  def controlTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::controlTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#controlTypeChanged
    """
    #  void QQStyleKitReader::controlTypeChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader18controlTypeChangedEv')

  def customTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::customTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#customTypeChanged
    """
    #  void QQStyleKitReader::customTypeChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader17customTypeChangedEv')

  def propertiesChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::propertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#propertiesChanged
    """
    #  void QQStyleKitReader::propertiesChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader17propertiesChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#enabledChanged
    """
    #  void QQStyleKitReader::enabledChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14enabledChangedEv')

  def focusedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::focusedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#focusedChanged
    """
    #  void QQStyleKitReader::focusedChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14focusedChangedEv')

  def checkedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::checkedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#checkedChanged
    """
    #  void QQStyleKitReader::checkedChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14checkedChangedEv')

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#hoveredChanged
    """
    #  void QQStyleKitReader::hoveredChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14hoveredChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#pressedChanged
    """
    #  void QQStyleKitReader::pressedChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14pressedChangedEv')

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::paletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#paletteChanged
    """
    #  void QQStyleKitReader::paletteChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader14paletteChangedEv')

  def verticalChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::verticalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#verticalChanged
    """
    #  void QQStyleKitReader::verticalChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader15verticalChangedEv')

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#highlightedChanged
    """
    #  void QQStyleKitReader::highlightedChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader18highlightedChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#fontChanged
    """
    #  void QQStyleKitReader::fontChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader11fontChangedEv')

  def onPaletteChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::onPaletteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#onPaletteChanged
    """
    #  void QQStyleKitReader::onPaletteChanged()
    self.uglySide.call('ritual_ZN16QQStyleKitReader16onPaletteChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#classBegin
    """
    #  void QQStyleKitReader::classBegin()
    ritual = 'ritual_ZN16QQStyleKitReader10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQStyleKitReader10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#componentComplete
    """
    #  void QQStyleKitReader::componentComplete()
    ritual = 'ritual_ZN16QQStyleKitReader17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQStyleKitReader17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def updateControl(self, applyStateChange: bool = True) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::updateControl(bool applyStateChange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#updateControl

    Parameters
    ----------

    applyStateChange : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQStyleKitReader::updateControl(bool applyStateChange)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader13updateControlEb', applyStateChange,
    )

  def populateLocalStorage(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::populateLocalStorage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#populateLocalStorage
    """
    #  void QQStyleKitReader::populateLocalStorage()
    self.uglySide.call('ritual_ZN16QQStyleKitReader20populateLocalStorageEv')

  def stateGroup(self) -> Optional[QQuickStateGroup]:
    """
    Calls Qt's 'QQuickStateGroup *QQStyleKitReader::stateGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitreader.html#stateGroup

    Returns
    -------

    Optional[QQuickStateGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateGroup *QQStyleKitReader::stateGroup()
    address = self.uglySide.call('ritual_ZN16QQStyleKitReader10stateGroupEv')
    from ..QtQuick import QQuickStateGroup
    return QQuickStateGroup._cuteAt(address)

  @overload(QQmlComponent)
  @overload(NoneType)
  def instantiatePropertyChanges(
      self,
      comp: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitReader::instantiatePropertyChanges(QQmlComponent *comp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#instantiatePropertyChanges

    Parameters
    ----------

    comp : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitReader::instantiatePropertyChanges(QQmlComponent *comp)
    self.uglySide.call(
        'ritual_ZN16QQStyleKitReader26instantiatePropertyChangesEP13QQmlCom'
        'ponent',
        self._addressOf(comp),
    )

  def maybeTrackDelegates(self) -> None:
    """
    Calls Qt's 'void QQStyleKitReader::maybeTrackDelegates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#maybeTrackDelegates
    """
    #  void QQStyleKitReader::maybeTrackDelegates()
    self.uglySide.call('ritual_ZN16QQStyleKitReader19maybeTrackDelegatesEv')

  def rebuildEffectivePalette(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::rebuildEffectivePalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#rebuildEffectivePalette
    """
    #  bool QQStyleKitReader::rebuildEffectivePalette()
    return self.uglySide.call(
        'ritual_ZN16QQStyleKitReader23rebuildEffectivePaletteEv',
    )

  def rebuildEffectiveFont(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitReader::rebuildEffectiveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitreader.html#rebuildEffectiveFont
    """
    #  bool QQStyleKitReader::rebuildEffectiveFont()
    return self.uglySide.call(
        'ritual_ZN16QQStyleKitReader20rebuildEffectiveFontEv',
    )
