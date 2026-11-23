"""
QAccessible binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible_base.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAccessibleEvent, QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleEvent = WAIT['QAccessibleEvent']
  QAccessibleInterface = WAIT['QAccessibleInterface']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessible(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessible: a plain Python object standing in front
  of one C++ QAccessible.

  C++ hands a QAccessible around as a copy, so every C++ QAccessible behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAccessible that has a ritual and that Python can
  call so far, 12 names in all: 'installActivationObserver',
  'removeActivationObserver', 'queryAccessibleInterface', 'uniqueId',
  'accessibleInterface', 'registerAccessibleInterface',
  'deleteAccessibleInterface', 'updateAccessibility', 'isActive',
  'setActive', 'setRootObject', 'cleanup'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessible::~QAccessible()': the destructor: Python removes its
    C++ QAccessible by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QAccessible is created at the first use, not by
    'QAccessible(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAccessible back gives a copy the ritual made for
    Python, in a new cute QAccessible.
  """

  #  The enums Qt writes inside QAccessible, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AnnouncementPoliteness(CuteNum, scoped=True):
    """
    The enum 'QAccessible::AnnouncementPoliteness' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Polite = Kee[int](0)
    Assertive = Kee[int](1)

  class Attribute(CuteNum, scoped=True):
    """
    The enum 'QAccessible::Attribute' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Custom = Kee[int](0)
    Level = Kee[int](1)
    Locale = Kee[int](2)
    Orientation = Kee[int](3)

  class Event(CuteNum):
    """
    The enum 'QAccessible::Event' of Qt, with the 73 names Qt gives in it.
    """

    SoundPlayed = Kee[int](1)
    Alert = Kee[int](2)
    ForegroundChanged = Kee[int](3)
    MenuStart = Kee[int](4)
    MenuEnd = Kee[int](5)
    PopupMenuStart = Kee[int](6)
    PopupMenuEnd = Kee[int](7)
    ContextHelpStart = Kee[int](12)
    ContextHelpEnd = Kee[int](13)
    DragDropStart = Kee[int](14)
    DragDropEnd = Kee[int](15)
    DialogStart = Kee[int](16)
    DialogEnd = Kee[int](17)
    ScrollingStart = Kee[int](18)
    ScrollingEnd = Kee[int](19)
    ScrollingPositionChanged = Kee[int](20)
    MenuCommand = Kee[int](24)
    ActionChanged = Kee[int](257)
    ActiveDescendantChanged = Kee[int](258)
    AttributeChanged = Kee[int](259)
    DocumentContentChanged = Kee[int](260)
    DocumentLoadComplete = Kee[int](261)
    DocumentLoadStopped = Kee[int](262)
    DocumentReload = Kee[int](263)
    HyperlinkEndIndexChanged = Kee[int](264)
    HyperlinkNumberOfAnchorsChanged = Kee[int](265)
    HyperlinkSelectedLinkChanged = Kee[int](266)
    HypertextLinkActivated = Kee[int](267)
    HypertextLinkSelected = Kee[int](268)
    HyperlinkStartIndexChanged = Kee[int](269)
    HypertextChanged = Kee[int](270)
    HypertextNLinksChanged = Kee[int](271)
    ObjectAttributeChanged = Kee[int](272)
    PageChanged = Kee[int](273)
    SectionChanged = Kee[int](274)
    TableCaptionChanged = Kee[int](275)
    TableColumnDescriptionChanged = Kee[int](276)
    TableColumnHeaderChanged = Kee[int](277)
    TableModelChanged = Kee[int](278)
    TableRowDescriptionChanged = Kee[int](279)
    TableRowHeaderChanged = Kee[int](280)
    TableSummaryChanged = Kee[int](281)
    TextAttributeChanged = Kee[int](282)
    TextCaretMoved = Kee[int](283)
    TextColumnChanged = Kee[int](285)
    TextInserted = Kee[int](286)
    TextRemoved = Kee[int](287)
    TextUpdated = Kee[int](288)
    TextSelectionChanged = Kee[int](289)
    VisibleDataChanged = Kee[int](290)
    ObjectCreated = Kee[int](32768)
    ObjectDestroyed = Kee[int](32769)
    ObjectShow = Kee[int](32770)
    ObjectHide = Kee[int](32771)
    ObjectReorder = Kee[int](32772)
    Focus = Kee[int](32773)
    Selection = Kee[int](32774)
    SelectionAdd = Kee[int](32775)
    SelectionRemove = Kee[int](32776)
    SelectionWithin = Kee[int](32777)
    StateChanged = Kee[int](32778)
    LocationChanged = Kee[int](32779)
    NameChanged = Kee[int](32780)
    DescriptionChanged = Kee[int](32781)
    ValueChanged = Kee[int](32782)
    ParentChanged = Kee[int](32783)
    HelpChanged = Kee[int](32928)
    DefaultActionChanged = Kee[int](32944)
    AcceleratorChanged = Kee[int](32960)
    Announcement = Kee[int](32976)
    IdentifierChanged = Kee[int](32992)
    RoleChanged = Kee[int](32993)
    InvalidEvent = Kee[int](32961)

  class InterfaceType(CuteNum):
    """
    The enum 'QAccessible::InterfaceType' of Qt, with the 11 names Qt gives
    in it.
    """

    TextInterface = Kee[int](0)
    EditableTextInterface = Kee[int](1)
    ValueInterface = Kee[int](2)
    ActionInterface = Kee[int](3)
    ImageInterface = Kee[int](4)
    TableInterface = Kee[int](5)
    TableCellInterface = Kee[int](6)
    HyperlinkInterface = Kee[int](7)
    SelectionInterface = Kee[int](8)
    AttributesInterface = Kee[int](9)
    ViewportInterface = Kee[int](10)

  class RelationFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QAccessible::RelationFlag' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QAccessible::Relation'.
    """

    Label = 0x1
    Labelled = 0x2
    Controller = 0x4
    Controlled = 0x8
    DescriptionFor = 0x10
    Described = 0x20
    FlowsFrom = 0x40
    FlowsTo = 0x80
    AllRelations = 0xffffffff

  Relation = RelationFlag

  class Role(CuteNum):
    """
    The enum 'QAccessible::Role' of Qt, with the 79 names Qt gives in it.
    """

    NoRole = Kee[int](0)
    TitleBar = Kee[int](1)
    MenuBar = Kee[int](2)
    ScrollBar = Kee[int](3)
    Grip = Kee[int](4)
    Sound = Kee[int](5)
    Cursor = Kee[int](6)
    Caret = Kee[int](7)
    AlertMessage = Kee[int](8)
    Window = Kee[int](9)
    Client = Kee[int](10)
    PopupMenu = Kee[int](11)
    MenuItem = Kee[int](12)
    ToolTip = Kee[int](13)
    Application = Kee[int](14)
    Document = Kee[int](15)
    Pane = Kee[int](16)
    Chart = Kee[int](17)
    Dialog = Kee[int](18)
    Border = Kee[int](19)
    Grouping = Kee[int](20)
    Separator = Kee[int](21)
    ToolBar = Kee[int](22)
    StatusBar = Kee[int](23)
    Table = Kee[int](24)
    ColumnHeader = Kee[int](25)
    RowHeader = Kee[int](26)
    Column = Kee[int](27)
    Row = Kee[int](28)
    Cell = Kee[int](29)
    Link = Kee[int](30)
    HelpBalloon = Kee[int](31)
    Assistant = Kee[int](32)
    List = Kee[int](33)
    ListItem = Kee[int](34)
    Tree = Kee[int](35)
    TreeItem = Kee[int](36)
    PageTab = Kee[int](37)
    PropertyPage = Kee[int](38)
    Indicator = Kee[int](39)
    Graphic = Kee[int](40)
    StaticText = Kee[int](41)
    EditableText = Kee[int](42)
    Button = Kee[int](43)
    PushButton = Kee[int](43)
    CheckBox = Kee[int](44)
    RadioButton = Kee[int](45)
    ComboBox = Kee[int](46)
    ProgressBar = Kee[int](48)
    Dial = Kee[int](49)
    HotkeyField = Kee[int](50)
    Slider = Kee[int](51)
    SpinBox = Kee[int](52)
    Canvas = Kee[int](53)
    Animation = Kee[int](54)
    Equation = Kee[int](55)
    ButtonDropDown = Kee[int](56)
    ButtonMenu = Kee[int](57)
    ButtonDropGrid = Kee[int](58)
    Whitespace = Kee[int](59)
    PageTabList = Kee[int](60)
    Clock = Kee[int](61)
    Splitter = Kee[int](62)
    LayeredPane = Kee[int](128)
    Terminal = Kee[int](129)
    Desktop = Kee[int](130)
    Paragraph = Kee[int](131)
    WebDocument = Kee[int](132)
    Section = Kee[int](133)
    Notification = Kee[int](134)
    Switch = Kee[int](135)
    ColorChooser = Kee[int](1028)
    Footer = Kee[int](1038)
    Form = Kee[int](1040)
    Heading = Kee[int](1044)
    Note = Kee[int](1051)
    ComplementaryContent = Kee[int](1068)
    BlockQuote = Kee[int](1073)
    UserRole = Kee[int](65535)

  class Text(CuteNum):
    """
    The enum 'QAccessible::Text' of Qt, with the 8 names Qt gives in it.
    """

    Name = Kee[int](0)
    Description = Kee[int](1)
    Value = Kee[int](2)
    Help = Kee[int](3)
    Accelerator = Kee[int](4)
    DebugDescription = Kee[int](5)
    Identifier = Kee[int](6)
    UserText = Kee[int](65535)

  class TextBoundaryType(CuteNum):
    """
    The enum 'QAccessible::TextBoundaryType' of Qt, with the 6 names Qt gives
    in it.
    """

    CharBoundary = Kee[int](0)
    WordBoundary = Kee[int](1)
    SentenceBoundary = Kee[int](2)
    ParagraphBoundary = Kee[int](3)
    LineBoundary = Kee[int](4)
    NoBoundary = Kee[int](5)

  #  The classes Qt writes inside QAccessible, each a class in here as in
  #  C++.

  class ActivationObserver(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAccessible::ActivationObserver: a plain Python
    object standing in front of one C++ QAccessible::ActivationObserver.

    What exists
    -----------

    Every function of Qt's QAccessible::ActivationObserver that has a ritual
    and that Python can call so far, 1 name in all:
    'accessibilityActiveChanged'. None can be made from Python: one comes out
    of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAccessible::ActivationObserver::~ActivationObserver()': the
      destructor: Python never removes a C++ QAccessible::ActivationObserver.

    What to expect
    --------------

    - The C++ QAccessible::ActivationObserver is created at the first use,
      not by 'QAccessible::ActivationObserver(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QAccessible::ActivationObserver.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAccessible::ActivationObserver'

    #  A C++ QAccessible::ActivationObserver Python makes is of a C++ class
    #  of ours, in which Python can take functions over. This ritual hands
    #  one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QAccessible_ActivationObserver'

    #  The functions Qt calls itself that QAccessible::ActivationObserver is
    #  the first to declare. A class of a program built on it can write one
    #  anew, and Qt then calls that. For each name: the key C++ knows the
    #  function by, what it gives, and what it takes.
    __virtual_functions__ = {
        'accessibilityActiveChanged': (
            ('_ZN11QAccessible18ActivationObserver26accessibilityActiveChan'
             'gedEb',
             ('nothing', 'nothing', ''),
             (
                 ('bool', 'number', ''),
             )),
        ),
    }

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(bool)
    def accessibilityActiveChanged(self, active: bool) -> None:
      """
      Calls Qt's 'void
      QAccessible::ActivationObserver::accessibilityActiveChanged(bool
      active)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qaccessible-activationobserver.html

      Parameters
      ----------

      active : bool
        Passed on as it is.
      """
      #  void
      #      QAccessible::ActivationObserver::accessibilityActiveChanged(bool
      #      active)
      self.uglySide.call(
          'ritual_ZN11QAccessible18ActivationObserver26accessibilityActiveC'
          'hangedEb',
          active,
      )

  class State(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAccessible::State: a plain Python object standing
    in front of one C++ QAccessible::State.

    C++ hands a QAccessible::State around as a copy, so every C++
    QAccessible::State behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QAccessible::State that has a ritual and that
    Python can call so far, 1 name in all: '__eq__'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAccessible::State::~State()': the destructor: Python removes its
      C++ QAccessible::State by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QAccessible::State is created at the first use, not by
      'QAccessible::State(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAccessible::State back gives a copy the ritual
      made for Python, in a new cute QAccessible::State.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAccessible::State'

    #  Qt's '~QAccessible::State()'. Naming it makes this a value class:
    #  Python owns every C++ QAccessible::State behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QAccessible5StateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, second: QAccessible.State) -> bool:
      """
      Calls Qt's 'bool operator==(const QAccessible::State &first, const
      QAccessible::State &second)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qaccessible-state.html#operator==

      Parameters
      ----------

      second : QAccessible.State
        Passed on as a value: Qt reads the C++ QAccessible::State, which
        stays Python's own.
      """
      #  bool operator==(const QAccessible::State &first, const
      #      QAccessible::State &second)
      return Rituals.call(
          'ritual_ZeqRKN11QAccessible5StateES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(second),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QAccessible::State::State()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qaccessible-state.html#State
      """
      #  QAccessible::State::State()
      self._noteCreation(QAccessible.State, lambda: Rituals.call(
          'ritual_ZN11QAccessible5StateC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ActivationObserver)
  @overload(NoneType)
  def installActivationObserver(a0: Optional[ActivationObserver]) -> None:
    """
    Calls Qt's 'void
    QAccessible::installActivationObserver(ActivationObserver *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#installActivationObserver

    Parameters
    ----------

    a0 : Optional[ActivationObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessible::installActivationObserver(ActivationObserver *a0)
    Rituals.call(
        'ritual_ZN11QAccessible25installActivationObserverEPNS_18Activation'
        'ObserverE',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(ActivationObserver)
  @overload(NoneType)
  def removeActivationObserver(a0: Optional[ActivationObserver]) -> None:
    """
    Calls Qt's 'void QAccessible::removeActivationObserver(ActivationObserver
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#removeActivationObserver

    Parameters
    ----------

    a0 : Optional[ActivationObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessible::removeActivationObserver(ActivationObserver *a0)
    Rituals.call(
        'ritual_ZN11QAccessible24removeActivationObserverEPNS_18ActivationO'
        'bserverE',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def queryAccessibleInterface(
      a0: Optional[QObject],
  ) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessible::queryAccessibleInterface(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#queryAccessibleInterface

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessible::queryAccessibleInterface(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN11QAccessible24queryAccessibleInterfaceEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @staticmethod
  @overload(QAccessibleInterface)
  @overload(NoneType)
  def uniqueId(iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'Id QAccessible::uniqueId(QAccessibleInterface *iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#uniqueId

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Id QAccessible::uniqueId(QAccessibleInterface *iface)
    return Rituals.call(
        'ritual_ZN11QAccessible8uniqueIdEP20QAccessibleInterface',
        CuteMixin._addressOf(iface),
    )

  @staticmethod
  @overload(int)
  def accessibleInterface(uniqueId: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessible::accessibleInterface(Id
    uniqueId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#accessibleInterface

    Parameters
    ----------

    uniqueId : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessible::accessibleInterface(Id uniqueId)
    address = Rituals.call(
        'ritual_ZN11QAccessible19accessibleInterfaceEj', uniqueId,
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @staticmethod
  @overload(QAccessibleInterface)
  @overload(NoneType)
  def registerAccessibleInterface(
      iface: Optional[QAccessibleInterface],
  ) -> int:
    """
    Calls Qt's 'Id
    QAccessible::registerAccessibleInterface(QAccessibleInterface *iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#registerAccessibleInterface

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Id QAccessible::registerAccessibleInterface(QAccessibleInterface
    #      *iface)
    return Rituals.call(
        'ritual_ZN11QAccessible27registerAccessibleInterfaceEP20QAccessible'
        'Interface',
        CuteMixin._addressOf(iface),
    )

  @staticmethod
  @overload(int)
  def deleteAccessibleInterface(uniqueId: int) -> None:
    """
    Calls Qt's 'void QAccessible::deleteAccessibleInterface(Id uniqueId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#deleteAccessibleInterface

    Parameters
    ----------

    uniqueId : int
      Passed on as it is.
    """
    #  void QAccessible::deleteAccessibleInterface(Id uniqueId)
    Rituals.call(
        'ritual_ZN11QAccessible25deleteAccessibleInterfaceEj', uniqueId,
    )

  @staticmethod
  @overload(QAccessibleEvent)
  @overload(NoneType)
  def updateAccessibility(event: Optional[QAccessibleEvent]) -> None:
    """
    Calls Qt's 'void QAccessible::updateAccessibility(QAccessibleEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessible.html#updateAccessibility

    Parameters
    ----------

    event : Optional[QAccessibleEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessible::updateAccessibility(QAccessibleEvent *event)
    Rituals.call(
        'ritual_ZN11QAccessible19updateAccessibilityEP16QAccessibleEvent',
        CuteMixin._addressOf(event),
    )

  @staticmethod
  def isActive() -> bool:
    """
    Calls Qt's 'bool QAccessible::isActive()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#isActive
    """
    #  bool QAccessible::isActive()
    return Rituals.call('ritual_ZN11QAccessible8isActiveEv')

  @staticmethod
  @overload(bool)
  def setActive(active: bool) -> None:
    """
    Calls Qt's 'void QAccessible::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QAccessible::setActive(bool active)
    Rituals.call('ritual_ZN11QAccessible9setActiveEb', active)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def setRootObject(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAccessible::setRootObject(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#setRootObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessible::setRootObject(QObject *object)
    Rituals.call(
        'ritual_ZN11QAccessible13setRootObjectEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QAccessible::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#cleanup
    """
    #  void QAccessible::cleanup()
    Rituals.call('ritual_ZN11QAccessible7cleanupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessible'

  #  Qt's '~QAccessible()'. Naming it makes this a value class: Python owns
  #  every C++ QAccessible behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QAccessibleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QAccessible::QAccessible()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaccessible.html#QAccessible
    """
    #  QAccessible::QAccessible()
    self._noteCreation(QAccessible, lambda: Rituals.call(
        'ritual_ZN11QAccessibleC1Ev',
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
