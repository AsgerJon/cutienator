"""
EditableAxisLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/editableaxislabel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means EditableAxisLabel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem, QGraphicsTextItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QFocusEvent, QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EditableAxisLabel(QGraphicsTextItem):
  """
  The cute side of Qt's EditableAxisLabel: a plain Python object standing in
  front of one C++ EditableAxisLabel.

  It is built on the cute 'QGraphicsTextItem', as Qt's EditableAxisLabel is
  built on Qt's QGraphicsTextItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's EditableAxisLabel that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'focusInEvent',
  'focusOutEvent', 'sceneEvent', 'setEditable', 'reloadBeforeEditContent',
  'boundingRect', 'setInitialEditValue', 'finishEditing',
  'resetBeforeEditValue', 'isEditEndingKeyPress'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *EditableAxisLabel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int EditableAxisLabel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ EditableAxisLabel is created at the first use, not by
    'EditableAxisLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ EditableAxisLabel.
  - Qt tells when it has removed the C++ EditableAxisLabel. Every call on the
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
    Calls Qt's 'QString EditableAxisLabel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/editableaxislabel.html#tr

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
    #  QString EditableAxisLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17EditableAxisLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'EditableAxisLabel'

  #  A C++ EditableAxisLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_EditableAxisLabel'

  #  The functions Qt calls itself that EditableAxisLabel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setInitialEditValue': (
          ('_ZN17EditableAxisLabel19setInitialEditValueEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finishEditing': (
          ('_ZN17EditableAxisLabel13finishEditingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetBeforeEditValue': (
          ('_ZN17EditableAxisLabel20resetBeforeEditValueEv',
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
    Calls Qt's 'const QMetaObject *EditableAxisLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/editableaxislabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *EditableAxisLabel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17EditableAxisLabel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF EditableAxisLabel::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF EditableAxisLabel::boundingRect() const
    ritual = 'ritual_ZNK17EditableAxisLabel12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17EditableAxisLabel12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEditable(self, editable: bool) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::setEditable(bool editable)'.

    Qt's own words: https://doc.qt.io/qt-6/editableaxislabel.html#setEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void EditableAxisLabel::setEditable(bool editable)
    self.uglySide.call(
        'ritual_ZN17EditableAxisLabel11setEditableEb', editable,
    )

  def setInitialEditValue(self) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::setInitialEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#setInitialEditValue
    """
    #  void EditableAxisLabel::setInitialEditValue()
    self.uglySide.call('ritual_ZN17EditableAxisLabel19setInitialEditValueEv')

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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'EditableAxisLabel::EditableAxisLabel(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#EditableAxisLabel

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  EditableAxisLabel::EditableAxisLabel(QGraphicsItem *parent)
    self._noteCreation(EditableAxisLabel, lambda: Rituals.call(
        'ritual_ZN17EditableAxisLabelC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void EditableAxisLabel::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17EditableAxisLabel12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17EditableAxisLabel12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void EditableAxisLabel::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17EditableAxisLabel13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17EditableAxisLabel13focusOutEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def sceneEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool EditableAxisLabel::sceneEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/editableaxislabel.html#sceneEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool EditableAxisLabel::sceneEvent(QEvent *event)
    ritual = 'ritual_ZN17EditableAxisLabel10sceneEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17EditableAxisLabel10sceneEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def reloadBeforeEditContent(self) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::reloadBeforeEditContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#reloadBeforeEditContent
    """
    #  void EditableAxisLabel::reloadBeforeEditContent()
    self.uglySide.call(
        'ritual_ZN17EditableAxisLabel23reloadBeforeEditContentEv',
    )

  def finishEditing(self) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::finishEditing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#finishEditing
    """
    #  void EditableAxisLabel::finishEditing()
    self.uglySide.call('ritual_ZN17EditableAxisLabel13finishEditingEv')

  def resetBeforeEditValue(self) -> None:
    """
    Calls Qt's 'void EditableAxisLabel::resetBeforeEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#resetBeforeEditValue
    """
    #  void EditableAxisLabel::resetBeforeEditValue()
    self.uglySide.call(
        'ritual_ZN17EditableAxisLabel20resetBeforeEditValueEv',
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def isEditEndingKeyPress(self, event: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool EditableAxisLabel::isEditEndingKeyPress(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/editableaxislabel.html#isEditEndingKeyPress

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool EditableAxisLabel::isEditEndingKeyPress(QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN17EditableAxisLabel20isEditEndingKeyPressEP9QKeyEvent',
        self._addressOf(event),
    )
