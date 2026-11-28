"""
QtVirtualKeyboard::ShadowInputContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shadowinputcontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::ShadowInputContext to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QVariant
  from . import QVirtualKeyboardInputContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ShadowInputContext(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::ShadowInputContext: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::ShadowInputContext.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::ShadowInputContext is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::ShadowInputContext that has a
  ritual and that Python can call so far, 20 names in all: 'metaObject',
  'tr', 'setInputContext', 'inputItem', 'setInputItem', 'anchorRectangle',
  'cursorRectangle', 'anchorRectIntersectsClipRect',
  'cursorRectIntersectsClipRect', 'selectionControlVisible',
  'setSelectionOnFocusObject', 'updateSelectionProperties',
  'inputItemChanged', 'anchorRectangleChanged', 'cursorRectangleChanged',
  'anchorRectIntersectsClipRectChanged',
  'cursorRectIntersectsClipRectChanged', 'selectionControlVisibleChanged',
  'update', 'queryFocusObject'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::ShadowInputContext::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::ShadowInputContext::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 30 functions Qt declares: 2 not a gap; 2 forbidden; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::ShadowInputContext is created at the first
    use, not by 'QtVirtualKeyboard::ShadowInputContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::ShadowInputContext.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::ShadowInputContext. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::ShadowInputContext::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html#tr

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
    #  QString QtVirtualKeyboard::ShadowInputContext::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::ShadowInputContext'

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
    *QtVirtualKeyboard::ShadowInputContext::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::ShadowInputContext::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputItem(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtVirtualKeyboard::ShadowInputContext::inputItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtVirtualKeyboard::ShadowInputContext::inputItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext9inputItemEv',
    )
    return QObject._cuteAt(address)

  def anchorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QtVirtualKeyboard::ShadowInputContext::anchorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QtVirtualKeyboard::ShadowInputContext::anchorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext15anchorRectangle'
        'Ev',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QtVirtualKeyboard::ShadowInputContext::cursorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QtVirtualKeyboard::ShadowInputContext::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext15cursorRectangle'
        'Ev',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def anchorRectIntersectsClipRect(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::ShadowInputContext::anchorRectIntersectsClipRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  bool QtVirtualKeyboard::ShadowInputContext::
    #      anchorRectIntersectsClipRect() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext28anchorRectInter'
        'sectsClipRectEv',
    )

  def cursorRectIntersectsClipRect(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::ShadowInputContext::cursorRectIntersectsClipRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  bool QtVirtualKeyboard::ShadowInputContext::
    #      cursorRectIntersectsClipRect() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext28cursorRectInter'
        'sectsClipRectEv',
    )

  def selectionControlVisible(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::ShadowInputContext::selectionControlVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  bool QtVirtualKeyboard::ShadowInputContext::selectionControlVisible()
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard18ShadowInputContext23selectionContro'
        'lVisibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVirtualKeyboardInputContext)
  @overload(NoneType)
  def setInputContext(
      self,
      inputContext: Optional[QVirtualKeyboardInputContext],
  ) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShadowInputContext::setInputContext(
    QVirtualKeyboardInputContext *inputContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Parameters
    ----------

    inputContext : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::ShadowInputContext::setInputContext(
    #      QVirtualKeyboardInputContext *inputContext)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext15setInputContextE'
        'P28QVirtualKeyboardInputContext',
        self._addressOf(inputContext),
    )

  @overload(QObject)
  @overload(NoneType)
  def setInputItem(self, inputItem: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::setInputItem(QObject *inputItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Parameters
    ----------

    inputItem : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::ShadowInputContext::setInputItem(QObject
    #      *inputItem)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext12setInputItemEP7Q'
        'Object',
        self._addressOf(inputItem, 'QObject'),
    )

  @overload(QPointF, QPointF)
  def setSelectionOnFocusObject(
      self,
      anchorPos: QPointF,
      cursorPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::setSelectionOnFocusObject(const
    QPointF &anchorPos, const QPointF &cursorPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Parameters
    ----------

    anchorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cursorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QtVirtualKeyboard::ShadowInputContext::setSelectionOnFocusObject(
    #      const QPointF &anchorPos, const QPointF &cursorPos)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext25setSelectionOnFo'
        'cusObjectERK7QPointFS3_',
        self._valueOf(anchorPos, 'QPointF'), self._valueOf(cursorPos,
        'QPointF'),
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
    'QtVirtualKeyboard::ShadowInputContext::ShadowInputContext(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::ShadowInputContext::ShadowInputContext(QObject
    #      *parent)
    self._noteCreation(ShadowInputContext, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContextC1EP7QObject',
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

  def updateSelectionProperties(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::updateSelectionProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void
    #      QtVirtualKeyboard::ShadowInputContext::updateSelectionProperties()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext25updateSelectionP'
        'ropertiesEv',
    )

  def inputItemChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::inputItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::inputItemChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext16inputItemChanged'
        'Ev',
    )

  def anchorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::anchorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::anchorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext22anchorRectangleC'
        'hangedEv',
    )

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::cursorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext22cursorRectangleC'
        'hangedEv',
    )

  def anchorRectIntersectsClipRectChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShadowInputContext::
    anchorRectIntersectsClipRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::
    #      anchorRectIntersectsClipRectChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext35anchorRectInters'
        'ectsClipRectChangedEv',
    )

  def cursorRectIntersectsClipRectChanged(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::ShadowInputContext::
    cursorRectIntersectsClipRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::
    #      cursorRectIntersectsClipRectChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext35cursorRectInters'
        'ectsClipRectChangedEv',
    )

  def selectionControlVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::selectionControlVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html
    """
    #  void QtVirtualKeyboard::ShadowInputContext::
    #      selectionControlVisibleChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext30selectionControl'
        'VisibleChangedEv',
    )

  @overload(Qt.InputMethodQueries)
  def update(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::ShadowInputContext::update(Qt::InputMethodQueries
    queries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html#update

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QtVirtualKeyboard::ShadowInputContext::update(Qt::
    #      InputMethodQueries queries)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext6updateE6QFlagsIN2'
        'Qt16InputMethodQueryEE',
        queries.value,
    )

  @overload(Qt.InputMethodQuery, QVariant)
  def queryFocusObject(
      self,
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QtVirtualKeyboard::ShadowInputContext::queryFocusObject(Qt::
    InputMethodQuery query, QVariant argument)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-shadowinputcontext.html

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtVirtualKeyboard::ShadowInputContext::queryFocusObject(Qt::
    #      InputMethodQuery query, QVariant argument)
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard18ShadowInputContext16queryFocusObject'
        'EN2Qt16InputMethodQueryE8QVariant',
        query.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
