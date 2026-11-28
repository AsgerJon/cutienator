"""
QPlatformInputContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatforminputcontext.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QInputMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QPointF, QRectF
  from ..QtCore import QVariant
  from . import QPlatformInputContextPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformInputContext(QObject):
  """
  The cute side of Qt's QPlatformInputContext: a plain Python object standing
  in front of one C++ QPlatformInputContext.

  It is built on the cute 'QObject', as Qt's QPlatformInputContext is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformInputContext that has a ritual and that
  Python can call so far, 31 names in all: 'metaObject', 'tr', 'd_func',
  'isValid', 'hasCapability', 'reset', 'commit', 'update', 'invokeAction',
  'filterEvent', 'keyboardRect', 'emitKeyboardRectChanged', 'isAnimating',
  'emitAnimatingChanged', 'showInputPanel', 'hideInputPanel',
  'isInputPanelVisible', 'emitInputPanelVisibleChanged', 'locale',
  'emitLocaleChanged', 'inputDirection', 'emitInputDirectionChanged',
  'setFocusObject', 'inputMethodAccepted', 'setSelectionOnFocusObject',
  'queryFocusObject', 'inputItemRectangle', 'inputItemClipRectangle',
  'cursorRectangle', 'anchorRectangle', 'keyboardRectangle'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformInputContext::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformInputContext::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QPlatformInputContextPrivate *QPlatformInputContext::d_func()
    const': takes in Python what 'QPlatformInputContextPrivate
    *QPlatformInputContext::d_func()' takes.
  - Qt's 'QPlatformInputContext::~QPlatformInputContext()': the destructor:
    Python never removes a C++ QPlatformInputContext.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformInputContext is created at the first use, not by
    'QPlatformInputContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformInputContext.
  - Qt tells when it has removed the C++ QPlatformInputContext. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPlatformInputContext, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteNum):
    """
    The enum 'QPlatformInputContext::Capability' of Qt, with the 1 names Qt
    gives in it.
    """

    HiddenTextCapability = Kee[int](1)

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
    Calls Qt's 'QString QPlatformInputContext::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#tr

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
    #  QString QPlatformInputContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPlatformInputContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPointF, QPointF)
  def setSelectionOnFocusObject(
      anchorPos: QPointF,
      cursorPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::setSelectionOnFocusObject(const
    QPointF &anchorPos, const QPointF &cursorPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html

    Parameters
    ----------

    anchorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cursorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPlatformInputContext::setSelectionOnFocusObject(const QPointF
    #      &anchorPos, const QPointF &cursorPos)
    Rituals.call(
        'ritual_ZN21QPlatformInputContext25setSelectionOnFocusObjectERK7QPo'
        'intFS2_',
        CuteMixin._valueOf(anchorPos, 'QPointF'),
        CuteMixin._valueOf(cursorPos, 'QPointF'),
    )

  @staticmethod
  @overload(Qt.InputMethodQuery, QPointF)
  def queryFocusObject(
      query: Qt.InputMethodQuery,
      position: QPointF,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlatformInputContext::queryFocusObject(Qt::InputMethodQuery query,
    QPointF position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#queryFocusObject

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformInputContext::queryFocusObject(Qt::InputMethodQuery
    #      query, QPointF position)
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext16queryFocusObjectEN2Qt16InputMeth'
        'odQueryE7QPointF',
        query.value, CuteMixin._valueOf(position, 'QPointF'),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  def inputItemRectangle() -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::inputItemRectangle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#inputItemRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::inputItemRectangle()
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext18inputItemRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def inputItemClipRectangle() -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::inputItemClipRectangle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#inputItemClipRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::inputItemClipRectangle()
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext22inputItemClipRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def cursorRectangle() -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::cursorRectangle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::cursorRectangle()
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def anchorRectangle() -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::anchorRectangle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#anchorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::anchorRectangle()
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext15anchorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @staticmethod
  def keyboardRectangle() -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::keyboardRectangle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#keyboardRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::keyboardRectangle()
    address = Rituals.call(
        'ritual_ZN21QPlatformInputContext17keyboardRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformInputContext'

  #  A C++ QPlatformInputContext Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformInputContext'

  #  The functions Qt calls itself that QPlatformInputContext is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK21QPlatformInputContext7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasCapability': (
          ('_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformInputContext.Capability'),
           )),
      ),
      'reset': (
          ('_ZN21QPlatformInputContext5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'commit': (
          ('_ZN21QPlatformInputContext6commitEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'update': (
          ('_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQuer'
           'yEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.InputMethodQuery'),
           )),
      ),
      'invokeAction': (
          ('_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6Action'
           'Ei',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QInputMethod.Action'),
               ('int', 'number', ''),
           )),
      ),
      'filterEvent': (
          ('_ZN21QPlatformInputContext11filterEventEPK6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'keyboardRect': (
          ('_ZNK21QPlatformInputContext12keyboardRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'isAnimating': (
          ('_ZNK21QPlatformInputContext11isAnimatingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'showInputPanel': (
          ('_ZN21QPlatformInputContext14showInputPanelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hideInputPanel': (
          ('_ZN21QPlatformInputContext14hideInputPanelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isInputPanelVisible': (
          ('_ZNK21QPlatformInputContext19isInputPanelVisibleEv',
           ('bool', 'number', ''),
           ()),
      ),
      'locale': (
          ('_ZNK21QPlatformInputContext6localeEv',
           ('address', 'value', 'QtCore:QLocale'),
           ()),
      ),
      'inputDirection': (
          ('_ZNK21QPlatformInputContext14inputDirectionEv',
           ('int', 'enum', 'QtCore:Qt.LayoutDirection'),
           ()),
      ),
      'setFocusObject': (
          ('_ZN21QPlatformInputContext14setFocusObjectEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
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
    Calls Qt's 'const QMetaObject *QPlatformInputContext::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformInputContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformInputContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#isValid
    """
    #  bool QPlatformInputContext::isValid() const
    ritual = 'ritual_ZNK21QPlatformInputContext7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext7isValidEv'
    return self.uglySide.call(ritual)

  @overload(Capability)
  def hasCapability(self, capability: Capability) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::hasCapability(Capability
    capability) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#hasCapability

    Parameters
    ----------

    capability : Capability
      Passed on as its number.
    """
    #  bool QPlatformInputContext::hasCapability(Capability capability) const
    ritual = (
        'ritual_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlatformInputContext13hasCapabilityENS_10Capabi'
          'lityE')
    return self.uglySide.call(ritual, capability.value)

  def keyboardRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPlatformInputContext::keyboardRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#keyboardRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPlatformInputContext::keyboardRect() const
    ritual = 'ritual_ZNK21QPlatformInputContext12keyboardRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext12keyboardRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::isAnimating() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#isAnimating
    """
    #  bool QPlatformInputContext::isAnimating() const
    ritual = 'ritual_ZNK21QPlatformInputContext11isAnimatingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext11isAnimatingEv'
    return self.uglySide.call(ritual)

  def isInputPanelVisible(self) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::isInputPanelVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#isInputPanelVisible
    """
    #  bool QPlatformInputContext::isInputPanelVisible() const
    ritual = 'ritual_ZNK21QPlatformInputContext19isInputPanelVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext19isInputPanelVisibleEv'
    return self.uglySide.call(ritual)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QPlatformInputContext::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QPlatformInputContext::locale() const
    ritual = 'ritual_ZNK21QPlatformInputContext6localeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext6localeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def inputDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QPlatformInputContext::inputDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#inputDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QPlatformInputContext::inputDirection() const
    ritual = 'ritual_ZNK21QPlatformInputContext14inputDirectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformInputContext14inputDirectionEv'
    return Qt.LayoutDirection(self.uglySide.call(ritual))

  def inputMethodAccepted(self) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::inputMethodAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#inputMethodAccepted
    """
    #  bool QPlatformInputContext::inputMethodAccepted() const
    return self.uglySide.call(
        'ritual_ZNK21QPlatformInputContext19inputMethodAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setFocusObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::setFocusObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#setFocusObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformInputContext::setFocusObject(QObject *object)
    ritual = 'ritual_ZN21QPlatformInputContext14setFocusObjectEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformInputContext14setFocusObjectEP7QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

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
    Notes what was given, for Qt's
    'QPlatformInputContext::QPlatformInputContext()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#QPlatformInputContext
    """
    #  QPlatformInputContext::QPlatformInputContext()
    self._noteCreation(QPlatformInputContext, lambda: Rituals.call(
        'ritual_ZN21QPlatformInputContextC1Ev',
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

  def d_func(self) -> Optional[QPlatformInputContextPrivate]:
    """
    Calls Qt's 'QPlatformInputContextPrivate
    *QPlatformInputContext::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#d_func

    Returns
    -------

    Optional[QPlatformInputContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContextPrivate *QPlatformInputContext::d_func()
    address = self.uglySide.call('ritual_ZN21QPlatformInputContext6d_funcEv')
    from . import QPlatformInputContextPrivate
    return QPlatformInputContextPrivate._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#reset
    """
    #  void QPlatformInputContext::reset()
    ritual = 'ritual_ZN21QPlatformInputContext5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformInputContext5resetEv'
    self.uglySide.call(ritual)

  def commit(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#commit
    """
    #  void QPlatformInputContext::commit()
    ritual = 'ritual_ZN21QPlatformInputContext6commitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformInputContext6commitEv'
    self.uglySide.call(ritual)

  @overload(Qt.InputMethodQueries)
  def update(self, a0: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::update(Qt::InputMethodQueries
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatforminputcontext.html#update

    Parameters
    ----------

    a0 : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QPlatformInputContext::update(Qt::InputMethodQueries a0)
    ritual = (
        'ritual_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQ'
        'ueryEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputM'
          'ethodQueryEE')
    self.uglySide.call(ritual, a0.value)

  @overload(QInputMethod.Action, int)
  def invokeAction(
      self,
      a0: QInputMethod.Action,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::invokeAction(QInputMethod::Action
    a0, int cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#invokeAction

    Parameters
    ----------

    a0 : QInputMethod.Action
      Passed on as its number.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QPlatformInputContext::invokeAction(QInputMethod::Action a0, int
    #      cursorPosition)
    ritual = (
        'ritual_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6Act'
        'ionEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformInputContext12invokeActionEN12QInputMeth'
          'od6ActionEi')
    self.uglySide.call(ritual, a0.value, cursorPosition)

  @overload(QEvent)
  @overload(NoneType)
  def filterEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPlatformInputContext::filterEvent(const QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#filterEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformInputContext::filterEvent(const QEvent *event)
    ritual = 'ritual_ZN21QPlatformInputContext11filterEventEPK6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformInputContext11filterEventEPK6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def emitKeyboardRectChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::emitKeyboardRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#emitKeyboardRectChanged
    """
    #  void QPlatformInputContext::emitKeyboardRectChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformInputContext23emitKeyboardRectChangedEv',
    )

  def emitAnimatingChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::emitAnimatingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#emitAnimatingChanged
    """
    #  void QPlatformInputContext::emitAnimatingChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformInputContext20emitAnimatingChangedEv',
    )

  def showInputPanel(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::showInputPanel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#showInputPanel
    """
    #  void QPlatformInputContext::showInputPanel()
    ritual = 'ritual_ZN21QPlatformInputContext14showInputPanelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformInputContext14showInputPanelEv'
    self.uglySide.call(ritual)

  def hideInputPanel(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::hideInputPanel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#hideInputPanel
    """
    #  void QPlatformInputContext::hideInputPanel()
    ritual = 'ritual_ZN21QPlatformInputContext14hideInputPanelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QPlatformInputContext14hideInputPanelEv'
    self.uglySide.call(ritual)

  def emitInputPanelVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::emitInputPanelVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html
    """
    #  void QPlatformInputContext::emitInputPanelVisibleChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformInputContext28emitInputPanelVisibleChangedEv',
    )

  def emitLocaleChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformInputContext::emitLocaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html#emitLocaleChanged
    """
    #  void QPlatformInputContext::emitLocaleChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformInputContext17emitLocaleChangedEv',
    )

  @overload(Qt.LayoutDirection)
  def emitInputDirectionChanged(
      self,
      newDirection: Qt.LayoutDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformInputContext::emitInputDirectionChanged(Qt::LayoutDirection
    newDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontext.html

    Parameters
    ----------

    newDirection : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QPlatformInputContext::emitInputDirectionChanged(Qt::
    #      LayoutDirection newDirection)
    self.uglySide.call(
        'ritual_ZN21QPlatformInputContext25emitInputDirectionChangedEN2Qt15'
        'LayoutDirectionE',
        newDirection.value,
    )
