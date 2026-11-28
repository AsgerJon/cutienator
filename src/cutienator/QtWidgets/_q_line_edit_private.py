"""
QLineEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLineEditPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QAction, QIcon
  from . import QLineEdit, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLineEdit = WAIT['QLineEdit']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineEditPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QLineEditPrivate: a plain Python object standing in
  front of one C++ QLineEditPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QLineEditPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLineEditPrivate that has a ritual and that Python
  can call so far, 24 names in all: 'q_func', 'initMouseYThreshold',
  'setText', 'textBeforeCursor', 'textAfterCursor',
  'updatePasswordEchoEditing', 'resetInputMethod', 'shouldEnableInputMethod',
  'shouldShowPlaceholderText', 'get', 'handleWindowActivate', 'textEdited',
  'cursorPositionChanged', 'connectCompleter', 'disconnectCompleter',
  'completionHighlighted', 'drag', 'clearButtonClicked',
  'controlEditingFinished', 'sideWidgetParameters', 'clearButtonIcon',
  'setClearButtonEnabled', 'positionSideWidgets', 'hasSideWidgets'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLineEdit *QLineEditPrivate::q_func() const': takes in Python
    what 'QLineEdit *QLineEditPrivate::q_func()' takes.
  - Qt's 'QLineEditPrivate::~QLineEditPrivate()': the destructor: Python
    never removes a C++ QLineEditPrivate.
  - Qt's 'const SideWidgetEntryList &QLineEditPrivate::leftSideWidgetList()
    const': gives a type Python has no way to take yet.
  - Qt's 'const SideWidgetEntryList &QLineEditPrivate::rightSideWidgetList()
    const': gives a type Python has no way to take yet.
  - Qt's 'SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction
    *a) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  14 of the 44 functions Qt declares: 9 leans on 'QLineEditPrivate; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 leans on 'QLineEditIconButton; 1 leans on 'vtable
  for QLineEditIconButton', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QLineEditPrivate is created at the first use, not by
    'QLineEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLineEditPrivate.
  - Each name of Qt's QLineEditPrivate that has no cute function yet,
    'addAction', 'adjustedContentsRect', 'adjustedControlRect', 'cursorRect',
    'effectiveTextMargins', 'findSideWidget', 'inSelection',
    'leftSideWidgetList', 'removeAction', 'rightSideWidgetList',
    'selectionChanged', 'sendMouseEventToInputContext', 'setCursorVisible',
    'textChanged', 'updateNeeded', 'xToPos', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLineEditPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SideWidgetFlag(CuteNum):
    """
    The enum 'QLineEditPrivate::SideWidgetFlag' of Qt, with the 3 names Qt
    gives in it.
    """

    SideWidgetFadeInWithText = Kee[int](1)
    SideWidgetCreatedByWidgetAction = Kee[int](2)
    SideWidgetClearButton = Kee[int](4)

  #  The classes Qt writes inside QLineEditPrivate, each a class in here as
  #  in C++.

  class SideWidgetEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLineEditPrivate::SideWidgetEntry: a plain Python
    object standing in front of one C++ QLineEditPrivate::SideWidgetEntry.

    C++ hands a QLineEditPrivate::SideWidgetEntry around as a copy, so every
    C++ QLineEditPrivate::SideWidgetEntry behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QLineEditPrivate::SideWidgetEntry yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLineEditPrivate::SideWidgetEntry::~SideWidgetEntry()': the
      destructor: Python removes its C++ QLineEditPrivate::SideWidgetEntry by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QLineEditPrivate::SideWidgetEntry is created at the first use,
      not by 'QLineEditPrivate::SideWidgetEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLineEditPrivate::SideWidgetEntry back gives a copy
      the ritual made for Python, in a new cute
      QLineEditPrivate::SideWidgetEntry.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QAction = WAIT['QAction']
      QWidget = WAIT['QWidget']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLineEditPrivate::SideWidgetEntry'

    #  Qt's '~QLineEditPrivate::SideWidgetEntry()'. Naming it makes this a
    #  value class: Python owns every C++ QLineEditPrivate::SideWidgetEntry
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QLineEditPrivate15SideWidgetEntryD1Ev'

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

    @overload()
    @overload(QWidget)
    @overload(NoneType)
    @overload(QWidget, QAction)
    @overload(QWidget, NoneType)
    @overload(NoneType, QAction)
    @overload(NoneType, NoneType)
    @overload(QWidget, QAction, int)
    @overload(QWidget, NoneType, int)
    @overload(NoneType, QAction, int)
    @overload(NoneType, NoneType, int)
    def __init__(
        self,
        w: Optional[QWidget] = None,
        a: Optional[QAction] = None,
        _flags: int = 0,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QLineEditPrivate::SideWidgetEntry::SideWidgetEntry(QWidget *w, QAction
      *a, int _flags)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qlineeditprivate-sidewidgetentry.html

      Parameters
      ----------

      w : Optional[QWidget]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      a : Optional[QAction]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      _flags : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QLineEditPrivate::SideWidgetEntry::SideWidgetEntry(QWidget *w,
      #      QAction *a, int _flags)
      self._noteCreation(
          QLineEditPrivate.SideWidgetEntry, lambda: Rituals.call(
              'ritual_ZN16QLineEditPrivate15SideWidgetEntryC1EP7QWidgetP7QA'
              'ctioni',
              self._addressOf(w), self._addressOf(a), _flags,
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

  class SideWidgetParameters(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLineEditPrivate::SideWidgetParameters: a plain
    Python object standing in front of one C++
    QLineEditPrivate::SideWidgetParameters.

    C++ hands a QLineEditPrivate::SideWidgetParameters around as a copy, so
    every C++ QLineEditPrivate::SideWidgetParameters behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QLineEditPrivate::SideWidgetParameters yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLineEditPrivate::SideWidgetParameters::~SideWidgetParameters()':
      the destructor: Python removes its C++
      QLineEditPrivate::SideWidgetParameters by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QLineEditPrivate::SideWidgetParameters is created at the first
      use, not by 'QLineEditPrivate::SideWidgetParameters(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLineEditPrivate::SideWidgetParameters back gives a
      copy the ritual made for Python, in a new cute
      QLineEditPrivate::SideWidgetParameters.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLineEditPrivate::SideWidgetParameters'

    #  Qt's '~QLineEditPrivate::SideWidgetParameters()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QLineEditPrivate::SideWidgetParameters behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN16QLineEditPrivate20SideWidgetParametersD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QLineEdit)
  @overload(NoneType)
  def get(lineEdit: Optional[QLineEdit]) -> Optional[QLineEditPrivate]:
    """
    Calls Qt's 'QLineEditPrivate *QLineEditPrivate::get(QLineEdit
    *lineEdit)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineeditprivate.html#get

    Parameters
    ----------

    lineEdit : Optional[QLineEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLineEditPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineEditPrivate *QLineEditPrivate::get(QLineEdit *lineEdit)
    address = Rituals.call(
        'ritual_ZN16QLineEditPrivate3getEP9QLineEdit',
        CuteMixin._addressOf(lineEdit),
    )
    return QLineEditPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLineEditPrivate'

  #  A C++ QLineEditPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLineEditPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def textBeforeCursor(self, curPos: int) -> str:
    """
    Calls Qt's 'QString QLineEditPrivate::textBeforeCursor(int curPos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#textBeforeCursor

    Parameters
    ----------

    curPos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEditPrivate::textBeforeCursor(int curPos) const
    return self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate16textBeforeCursorEi', curPos,
    )

  @overload(int)
  def textAfterCursor(self, curPos: int) -> str:
    """
    Calls Qt's 'QString QLineEditPrivate::textAfterCursor(int curPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#textAfterCursor

    Parameters
    ----------

    curPos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEditPrivate::textAfterCursor(int curPos) const
    return self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate15textAfterCursorEi', curPos,
    )

  def shouldEnableInputMethod(self) -> bool:
    """
    Calls Qt's 'bool QLineEditPrivate::shouldEnableInputMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#shouldEnableInputMethod
    """
    #  bool QLineEditPrivate::shouldEnableInputMethod() const
    return self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate23shouldEnableInputMethodEv',
    )

  def shouldShowPlaceholderText(self) -> bool:
    """
    Calls Qt's 'bool QLineEditPrivate::shouldShowPlaceholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#shouldShowPlaceholderText
    """
    #  bool QLineEditPrivate::shouldShowPlaceholderText() const
    return self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate25shouldShowPlaceholderTextEv',
    )

  def sideWidgetParameters(self) -> SideWidgetParameters:
    """
    Calls Qt's 'SideWidgetParameters QLineEditPrivate::sideWidgetParameters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#sideWidgetParameters

    Returns
    -------

    SideWidgetParameters
      A new cute QLineEditPrivate::SideWidgetParameters around the copy Qt
      gave back. Python owns it.
    """
    #  SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
    address = self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate20sideWidgetParametersEv',
    )
    return QLineEditPrivate.SideWidgetParameters._cuteOwning(address)

  def clearButtonIcon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QLineEditPrivate::clearButtonIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#clearButtonIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QLineEditPrivate::clearButtonIcon() const
    address = self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate15clearButtonIconEv',
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def hasSideWidgets(self) -> bool:
    """
    Calls Qt's 'bool QLineEditPrivate::hasSideWidgets() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#hasSideWidgets
    """
    #  bool QLineEditPrivate::hasSideWidgets() const
    return self.uglySide.call(
        'ritual_ZNK16QLineEditPrivate14hasSideWidgetsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineeditprivate.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEditPrivate::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate7setTextERK7QString', text,
    )

  @overload(bool)
  def setClearButtonEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::setClearButtonEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#setClearButtonEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QLineEditPrivate::setClearButtonEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate21setClearButtonEnabledEb', enabled,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLineEditPrivate::QLineEditPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#QLineEditPrivate
    """
    #  QLineEditPrivate::QLineEditPrivate()
    self._noteCreation(QLineEditPrivate, lambda: Rituals.call(
        'ritual_ZN16QLineEditPrivateC1Ev',
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

  def q_func(self) -> Optional[QLineEdit]:
    """
    Calls Qt's 'QLineEdit *QLineEditPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineeditprivate.html#q_func

    Returns
    -------

    Optional[QLineEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLineEdit *QLineEditPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QLineEditPrivate6q_funcEv')
    from . import QLineEdit
    return QLineEdit._cuteAt(address)

  def initMouseYThreshold(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::initMouseYThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#initMouseYThreshold
    """
    #  void QLineEditPrivate::initMouseYThreshold()
    self.uglySide.call('ritual_ZN16QLineEditPrivate19initMouseYThresholdEv')

  @overload(bool)
  def updatePasswordEchoEditing(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::updatePasswordEchoEditing(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#updatePasswordEchoEditing

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLineEditPrivate::updatePasswordEchoEditing(bool a0)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate25updatePasswordEchoEditingEb', a0,
    )

  def resetInputMethod(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::resetInputMethod()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#resetInputMethod
    """
    #  void QLineEditPrivate::resetInputMethod()
    self.uglySide.call('ritual_ZN16QLineEditPrivate16resetInputMethodEv')

  def handleWindowActivate(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::handleWindowActivate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#handleWindowActivate
    """
    #  void QLineEditPrivate::handleWindowActivate()
    self.uglySide.call('ritual_ZN16QLineEditPrivate20handleWindowActivateEv')

  @overload(str)
  def textEdited(self, a0: str) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::textEdited(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineeditprivate.html#textEdited

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEditPrivate::textEdited(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate10textEditedERK7QString', a0,
    )

  @overload(int, int)
  def cursorPositionChanged(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::cursorPositionChanged(int a0, int
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#cursorPositionChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QLineEditPrivate::cursorPositionChanged(int a0, int a1)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate21cursorPositionChangedEii', a0, a1,
    )

  def connectCompleter(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::connectCompleter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#connectCompleter
    """
    #  void QLineEditPrivate::connectCompleter()
    self.uglySide.call('ritual_ZN16QLineEditPrivate16connectCompleterEv')

  def disconnectCompleter(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::disconnectCompleter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#disconnectCompleter
    """
    #  void QLineEditPrivate::disconnectCompleter()
    self.uglySide.call('ritual_ZN16QLineEditPrivate19disconnectCompleterEv')

  @overload(str)
  def completionHighlighted(self, a0: str) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::completionHighlighted(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#completionHighlighted

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEditPrivate::completionHighlighted(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate21completionHighlightedERK7QString', a0,
    )

  def drag(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::drag()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineeditprivate.html#drag
    """
    #  void QLineEditPrivate::drag()
    self.uglySide.call('ritual_ZN16QLineEditPrivate4dragEv')

  def clearButtonClicked(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::clearButtonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#clearButtonClicked
    """
    #  void QLineEditPrivate::clearButtonClicked()
    self.uglySide.call('ritual_ZN16QLineEditPrivate18clearButtonClickedEv')

  def controlEditingFinished(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::controlEditingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#controlEditingFinished
    """
    #  void QLineEditPrivate::controlEditingFinished()
    self.uglySide.call(
        'ritual_ZN16QLineEditPrivate22controlEditingFinishedEv',
    )

  def positionSideWidgets(self) -> None:
    """
    Calls Qt's 'void QLineEditPrivate::positionSideWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineeditprivate.html#positionSideWidgets
    """
    #  void QLineEditPrivate::positionSideWidgets()
    self.uglySide.call('ritual_ZN16QLineEditPrivate19positionSideWidgetsEv')

  @staticmethod
  def addAction(*__, **_) -> Never:
    """
    Qt's 'QWidget *QLineEditPrivate::addAction(QAction *newAction, QAction
    *before, QLineEdit::ActionPosition a2, int flags)': leans on 'vtable for
    QLineEditIconButton', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.addAction' has no cute function yet. Qt's "
        "'QWidget *QLineEditPrivate::addAction(QAction *newAction, QAction "
        "*before, QLineEdit::ActionPosition a2, int flags)': leans on "
        "'vtable for QLineEditIconButton', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def adjustedContentsRect(*__, **_) -> Never:
    """
    Qt's 'QRect QLineEditPrivate::adjustedContentsRect() const': leans on
    'QLineEditIconButton::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.adjustedContentsRect' has no cute function yet. "
        "Qt's 'QRect QLineEditPrivate::adjustedContentsRect() const': leans "
        "on 'QLineEditIconButton::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def adjustedControlRect(*__, **_) -> Never:
    """
    Qt's 'QRect QLineEditPrivate::adjustedControlRect(const QRect &a0)
    const': leans on 'QLineEditPrivate::horizontalMargin', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.adjustedControlRect' has no cute function yet. "
        "Qt's 'QRect QLineEditPrivate::adjustedControlRect(const QRect &a0) "
        "const': leans on 'QLineEditPrivate::horizontalMargin', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def cursorRect(*__, **_) -> Never:
    """
    Qt's 'QRect QLineEditPrivate::cursorRect() const': leans on
    'QLineEditPrivate::horizontalMargin', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.cursorRect' has no cute function yet. Qt's "
        "'QRect QLineEditPrivate::cursorRect() const': leans on "
        "'QLineEditPrivate::horizontalMargin', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def effectiveTextMargins(*__, **_) -> Never:
    """
    Qt's 'QMargins QLineEditPrivate::effectiveTextMargins() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'effectiveTextMargin'.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.effectiveTextMargins' has no cute function yet. "
        "Qt's 'QMargins QLineEditPrivate::effectiveTextMargins() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'effectiveTextMargin'.")

  @staticmethod
  def findSideWidget(*__, **_) -> Never:
    """
    Qt's 'SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction
    *a) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.findSideWidget' has no cute function yet. Qt's "
        "'SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction "
        "*a) const': gives a type Python has no way to take yet.")

  @staticmethod
  def inSelection(*__, **_) -> Never:
    """
    Qt's 'bool QLineEditPrivate::inSelection(int x) const': leans on
    'QLineEditPrivate::horizontalMargin', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.inSelection' has no cute function yet. Qt's "
        "'bool QLineEditPrivate::inSelection(int x) const': leans on "
        "'QLineEditPrivate::horizontalMargin', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def leftSideWidgetList(*__, **_) -> Never:
    """
    Qt's 'const SideWidgetEntryList &QLineEditPrivate::leftSideWidgetList()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.leftSideWidgetList' has no cute function yet. "
        "Qt's 'const SideWidgetEntryList "
        "&QLineEditPrivate::leftSideWidgetList() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def removeAction(*__, **_) -> Never:
    """
    Qt's 'void QLineEditPrivate::removeAction(QAction *action)': leans on
    'QLineEditIconButton::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.removeAction' has no cute function yet. Qt's "
        "'void QLineEditPrivate::removeAction(QAction *action)': leans on "
        "'QLineEditIconButton::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def rightSideWidgetList(*__, **_) -> Never:
    """
    Qt's 'const SideWidgetEntryList &QLineEditPrivate::rightSideWidgetList()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.rightSideWidgetList' has no cute function yet. "
        "Qt's 'const SideWidgetEntryList "
        "&QLineEditPrivate::rightSideWidgetList() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def selectionChanged(*__, **_) -> Never:
    """
    Qt's 'void QLineEditPrivate::selectionChanged()': leans on
    'QLineEditPrivate::horizontalMargin', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.selectionChanged' has no cute function yet. Qt's "
        "'void QLineEditPrivate::selectionChanged()': leans on "
        "'QLineEditPrivate::horizontalMargin', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sendMouseEventToInputContext(*__, **_) -> Never:
    """
    Qt's 'bool QLineEditPrivate::sendMouseEventToInputContext(QMouseEvent
    *e)': leans on 'QLineEditPrivate::horizontalMargin', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.sendMouseEventToInputContext' has no cute "
        "function yet. Qt's 'bool "
        "QLineEditPrivate::sendMouseEventToInputContext(QMouseEvent *e)': "
        "leans on 'QLineEditPrivate::horizontalMargin', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setCursorVisible(*__, **_) -> Never:
    """
    Qt's 'void QLineEditPrivate::setCursorVisible(bool visible)': leans on
    'QLineEditPrivate::horizontalMargin', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.setCursorVisible' has no cute function yet. Qt's "
        "'void QLineEditPrivate::setCursorVisible(bool visible)': leans on "
        "'QLineEditPrivate::horizontalMargin', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textChanged(*__, **_) -> Never:
    """
    Qt's 'void QLineEditPrivate::textChanged(const QString &a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'displayWidgets'.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.textChanged' has no cute function yet. Qt's "
        "'void QLineEditPrivate::textChanged(const QString &a0)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'displayWidgets'.")

  @staticmethod
  def updateNeeded(*__, **_) -> Never:
    """
    Qt's 'void QLineEditPrivate::updateNeeded(const QRect &a0)': leans on
    'QLineEditPrivate::horizontalMargin', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.updateNeeded' has no cute function yet. Qt's "
        "'void QLineEditPrivate::updateNeeded(const QRect &a0)': leans on "
        "'QLineEditPrivate::horizontalMargin', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def xToPos(*__, **_) -> Never:
    """
    Qt's 'int QLineEditPrivate::xToPos(int x, QTextLine::CursorPosition a1)
    const': leans on 'QLineEditPrivate::horizontalMargin', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLineEditPrivate.xToPos' has no cute function yet. Qt's 'int "
        "QLineEditPrivate::xToPos(int x, QTextLine::CursorPosition a1) "
        "const': leans on 'QLineEditPrivate::horizontalMargin', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
