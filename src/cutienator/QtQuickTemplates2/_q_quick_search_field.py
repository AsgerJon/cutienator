"""
QQuickSearchField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksearchfield_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSearchField to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from ..QtGui import QFocusEvent, QHoverEvent, QKeyEvent
  from ..QtQml import QQmlComponent
  from ..QtQmlModels import QQmlInstanceModel
  from . import QQuickIndicatorButton, QQuickPopup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickPopup = WAIT['QQuickPopup']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSearchField(QQuickControl):
  """
  The cute side of Qt's QQuickSearchField: a plain Python object standing in
  front of one C++ QQuickSearchField.

  It is built on the cute 'QQuickControl', as Qt's QQuickSearchField is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSearchField that has a ritual and that Python
  can call so far, 68 names in all: 'metaObject', 'tr', 'suggestionModel',
  'setSuggestionModel', 'delegateModel', 'suggestionCount', 'currentIndex',
  'setCurrentIndex', 'highlightedIndex', 'text', 'setText', 'textRole',
  'setTextRole', 'isLive', 'setLive', 'searchIndicator', 'clearIndicator',
  'popup', 'setPopup', 'delegate', 'setDelegate', 'placeholderText',
  'setPlaceholderText', 'selectTextByMouse', 'setSelectTextByMouse',
  'selectedText', 'selectionStart', 'selectionEnd', 'cursorPosition',
  'setCursorPosition', 'select', 'selectWord', 'selectAll', 'deselect',
  'activated', 'highlighted', 'accepted', 'searchTriggered', 'textEdited',
  'suggestionModelChanged', 'delegateModelChanged', 'suggestionCountChanged',
  'currentIndexChanged', 'highlightedIndexChanged', 'textChanged',
  'textRoleChanged', 'liveChanged', 'popupChanged', 'delegateChanged',
  'placeholderTextChanged', 'selectTextByMouseChanged',
  'selectedTextChanged', 'selectionStartChanged', 'selectionEndChanged',
  'cursorPositionChanged', 'searchButtonPressed', 'clearButtonPressed',
  'eventFilter', 'focusInEvent', 'focusOutEvent', 'hoverEnterEvent',
  'hoverMoveEvent', 'hoverLeaveEvent', 'keyPressEvent', 'classBegin',
  'componentComplete', 'contentItemChange', 'itemChange'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSearchField::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickSearchField::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSearchField::~QQuickSearchField()': the destructor: Python
    never removes a C++ QQuickSearchField.
  - Qt's 'QQuickSearchFieldPrivate *QQuickSearchField::d_func()': gives
    'QQuickSearchFieldPrivate', which has no cute class yet.
  - Qt's 'const QQuickSearchFieldPrivate *QQuickSearchField::d_func() const':
    gives 'QQuickSearchFieldPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 78 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSearchField is created at the first use, not by
    'QQuickSearchField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSearchField.
  - Qt tells when it has removed the C++ QQuickSearchField. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickSearchField::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#tr

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
    #  QString QQuickSearchField::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickSearchField2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSearchField'

  #  A C++ QQuickSearchField Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSearchField'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSearchField::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSearchField::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickSearchField10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def suggestionModel(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickSearchField::suggestionModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#suggestionModel

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickSearchField::suggestionModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickSearchField15suggestionModelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegateModel(self) -> Optional[QQmlInstanceModel]:
    """
    Calls Qt's 'QQmlInstanceModel *QQuickSearchField::delegateModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#delegateModel

    Returns
    -------

    Optional[QQmlInstanceModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstanceModel *QQuickSearchField::delegateModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickSearchField13delegateModelEv',
    )
    from ..QtQmlModels import QQmlInstanceModel
    return QQmlInstanceModel._cuteAt(address)

  def suggestionCount(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::suggestionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#suggestionCount
    """
    #  int QQuickSearchField::suggestionCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField15suggestionCountEv',
    )

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#currentIndex
    """
    #  int QQuickSearchField::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField12currentIndexEv',
    )

  def highlightedIndex(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::highlightedIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#highlightedIndex
    """
    #  int QQuickSearchField::highlightedIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField16highlightedIndexEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickSearchField::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSearchField::text() const
    return self.uglySide.call('ritual_ZNK17QQuickSearchField4textEv')

  def textRole(self) -> str:
    """
    Calls Qt's 'QString QQuickSearchField::textRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#textRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSearchField::textRole() const
    return self.uglySide.call('ritual_ZNK17QQuickSearchField8textRoleEv')

  def isLive(self) -> bool:
    """
    Calls Qt's 'bool QQuickSearchField::isLive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#isLive
    """
    #  bool QQuickSearchField::isLive() const
    return self.uglySide.call('ritual_ZNK17QQuickSearchField6isLiveEv')

  def searchIndicator(self) -> Optional[QQuickIndicatorButton]:
    """
    Calls Qt's 'QQuickIndicatorButton *QQuickSearchField::searchIndicator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#searchIndicator

    Returns
    -------

    Optional[QQuickIndicatorButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIndicatorButton *QQuickSearchField::searchIndicator() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickSearchField15searchIndicatorEv',
    )
    from . import QQuickIndicatorButton
    return QQuickIndicatorButton._cuteAt(address)

  def clearIndicator(self) -> Optional[QQuickIndicatorButton]:
    """
    Calls Qt's 'QQuickIndicatorButton *QQuickSearchField::clearIndicator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#clearIndicator

    Returns
    -------

    Optional[QQuickIndicatorButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIndicatorButton *QQuickSearchField::clearIndicator() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickSearchField14clearIndicatorEv',
    )
    from . import QQuickIndicatorButton
    return QQuickIndicatorButton._cuteAt(address)

  def popup(self) -> Optional[QQuickPopup]:
    """
    Calls Qt's 'QQuickPopup *QQuickSearchField::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#popup

    Returns
    -------

    Optional[QQuickPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopup *QQuickSearchField::popup() const
    address = self.uglySide.call('ritual_ZNK17QQuickSearchField5popupEv')
    from . import QQuickPopup
    return QQuickPopup._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSearchField::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSearchField::delegate() const
    address = self.uglySide.call('ritual_ZNK17QQuickSearchField8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QQuickSearchField::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSearchField::placeholderText() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField15placeholderTextEv',
    )

  def selectTextByMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickSearchField::selectTextByMouse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectTextByMouse
    """
    #  bool QQuickSearchField::selectTextByMouse() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField17selectTextByMouseEv',
    )

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QQuickSearchField::selectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickSearchField::selectedText() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField12selectedTextEv',
    )

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectionStart
    """
    #  int QQuickSearchField::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::selectionEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectionEnd
    """
    #  int QQuickSearchField::selectionEnd() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField12selectionEndEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QQuickSearchField::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#cursorPosition
    """
    #  int QQuickSearchField::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickSearchField14cursorPositionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setSuggestionModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setSuggestionModel(const QVariant
    &model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#setSuggestionModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickSearchField::setSuggestionModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField18setSuggestionModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickSearchField::setCurrentIndex(int index)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField15setCurrentIndexEi', index,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSearchField::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField7setTextERK7QString', text,
    )

  @overload(str)
  def setTextRole(self, textRole: str) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setTextRole(const QString
    &textRole)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#setTextRole

    Parameters
    ----------

    textRole : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSearchField::setTextRole(const QString &textRole)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField11setTextRoleERK7QString', textRole,
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setLive(const bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickSearchField::setLive(const bool live)
    self.uglySide.call('ritual_ZN17QQuickSearchField7setLiveEb', live)

  @overload(QQuickPopup)
  @overload(NoneType)
  def setPopup(self, popup: Optional[QQuickPopup]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setPopup(QQuickPopup *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#setPopup

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::setPopup(QQuickPopup *popup)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField8setPopupEP11QQuickPopup',
        self._addressOf(popup),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(str)
  def setPlaceholderText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setPlaceholderText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#setPlaceholderText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickSearchField::setPlaceholderText(const QString &text)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField18setPlaceholderTextERK7QString', text,
    )

  @overload(bool)
  def setSelectTextByMouse(self, selectable: bool) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setSelectTextByMouse(const bool
    selectable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#setSelectTextByMouse

    Parameters
    ----------

    selectable : bool
      Passed on as it is.
    """
    #  void QQuickSearchField::setSelectTextByMouse(const bool selectable)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField20setSelectTextByMouseEb', selectable,
    )

  @overload(int)
  def setCursorPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QQuickSearchField::setCursorPosition(int position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#setCursorPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QQuickSearchField::setCursorPosition(int position)
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField17setCursorPositionEi', position,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSearchField::QQuickSearchField(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#QQuickSearchField

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSearchField::QQuickSearchField(QQuickItem *parent)
    self._noteCreation(QQuickSearchField, lambda: Rituals.call(
        'ritual_ZN17QQuickSearchFieldC1EP10QQuickItem',
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

  @overload(int, int)
  def select(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QQuickSearchField::select(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#select

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickSearchField::select(int start, int end)
    self.uglySide.call('ritual_ZN17QQuickSearchField6selectEii', start, end)

  def selectWord(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectWord()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#selectWord
    """
    #  void QQuickSearchField::selectWord()
    self.uglySide.call('ritual_ZN17QQuickSearchField10selectWordEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#selectAll
    """
    #  void QQuickSearchField::selectAll()
    self.uglySide.call('ritual_ZN17QQuickSearchField9selectAllEv')

  def deselect(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::deselect()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#deselect
    """
    #  void QQuickSearchField::deselect()
    self.uglySide.call('ritual_ZN17QQuickSearchField8deselectEv')

  @overload(int)
  def activated(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickSearchField::activated(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#activated

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickSearchField::activated(int index)
    self.uglySide.call('ritual_ZN17QQuickSearchField9activatedEi', index)

  @overload(int)
  def highlighted(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickSearchField::highlighted(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#highlighted

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickSearchField::highlighted(int index)
    self.uglySide.call('ritual_ZN17QQuickSearchField11highlightedEi', index)

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#accepted
    """
    #  void QQuickSearchField::accepted()
    self.uglySide.call('ritual_ZN17QQuickSearchField8acceptedEv')

  def searchTriggered(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::searchTriggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#searchTriggered
    """
    #  void QQuickSearchField::searchTriggered()
    self.uglySide.call('ritual_ZN17QQuickSearchField15searchTriggeredEv')

  def textEdited(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::textEdited()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#textEdited
    """
    #  void QQuickSearchField::textEdited()
    self.uglySide.call('ritual_ZN17QQuickSearchField10textEditedEv')

  def suggestionModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::suggestionModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#suggestionModelChanged
    """
    #  void QQuickSearchField::suggestionModelChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField22suggestionModelChangedEv',
    )

  def delegateModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::delegateModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#delegateModelChanged
    """
    #  void QQuickSearchField::delegateModelChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField20delegateModelChangedEv',
    )

  def suggestionCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::suggestionCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#suggestionCountChanged
    """
    #  void QQuickSearchField::suggestionCountChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField22suggestionCountChangedEv',
    )

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#currentIndexChanged
    """
    #  void QQuickSearchField::currentIndexChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField19currentIndexChangedEv')

  def highlightedIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::highlightedIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#highlightedIndexChanged
    """
    #  void QQuickSearchField::highlightedIndexChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField23highlightedIndexChangedEv',
    )

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#textChanged
    """
    #  void QQuickSearchField::textChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField11textChangedEv')

  def textRoleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::textRoleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#textRoleChanged
    """
    #  void QQuickSearchField::textRoleChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField15textRoleChangedEv')

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::liveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#liveChanged
    """
    #  void QQuickSearchField::liveChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField11liveChangedEv')

  def popupChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::popupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#popupChanged
    """
    #  void QQuickSearchField::popupChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField12popupChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#delegateChanged
    """
    #  void QQuickSearchField::delegateChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField15delegateChangedEv')

  def placeholderTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::placeholderTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#placeholderTextChanged
    """
    #  void QQuickSearchField::placeholderTextChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField22placeholderTextChangedEv',
    )

  def selectTextByMouseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectTextByMouseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectTextByMouseChanged
    """
    #  void QQuickSearchField::selectTextByMouseChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField24selectTextByMouseChangedEv',
    )

  def selectedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectedTextChanged
    """
    #  void QQuickSearchField::selectedTextChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField19selectedTextChangedEv')

  def selectionStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectionStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectionStartChanged
    """
    #  void QQuickSearchField::selectionStartChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField21selectionStartChangedEv',
    )

  def selectionEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::selectionEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#selectionEndChanged
    """
    #  void QQuickSearchField::selectionEndChanged()
    self.uglySide.call('ritual_ZN17QQuickSearchField19selectionEndChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#cursorPositionChanged
    """
    #  void QQuickSearchField::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickSearchField21cursorPositionChangedEv',
    )

  def searchButtonPressed(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::searchButtonPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#searchButtonPressed
    """
    #  void QQuickSearchField::searchButtonPressed()
    self.uglySide.call('ritual_ZN17QQuickSearchField19searchButtonPressedEv')

  def clearButtonPressed(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::clearButtonPressed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#clearButtonPressed
    """
    #  void QQuickSearchField::clearButtonPressed()
    self.uglySide.call('ritual_ZN17QQuickSearchField18clearButtonPressedEv')

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickSearchField::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSearchField::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField13focusOutEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickSearchField::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QQuickSearchField13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickSearchField13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#classBegin
    """
    #  void QQuickSearchField::classBegin()
    ritual = 'ritual_ZN17QQuickSearchField10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickSearchField10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSearchField::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#componentComplete
    """
    #  void QQuickSearchField::componentComplete()
    ritual = 'ritual_ZN17QQuickSearchField17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickSearchField17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickSearchField::contentItemChange(QQuickItem
    *newItem, QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksearchfield.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSearchField::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = (
        'ritual_ZN17QQuickSearchField17contentItemChangeEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField17contentItemChangeEP10QQuickIte'
          'mS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickSearchField::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksearchfield.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickSearchField::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN17QQuickSearchField10itemChangeEN10QQuickItem10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickSearchField10itemChangeEN10QQuickItem10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))
