"""
QInputControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinputcontrol_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QInputControl to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData, QVariant
  from . import QInputMethodEvent, QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMimeData = WAIT['QMimeData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputControl(QObject):
  """
  The cute side of Qt's QInputControl: a plain Python object standing in
  front of one C++ QInputControl.

  It is built on the cute 'QObject', as Qt's QInputControl is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputControl that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'isAcceptableInput',
  'isCommonTextEditShortcut', 'selectionWrapper', 'mimeDataForInputEvent'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QInputControl::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QInputControl::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QInputControl::QInputControl(Type type, QObjectPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QInputControl is created at the first use, not by
    'QInputControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputControl.
  - Qt tells when it has removed the C++ QInputControl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QInputControl, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QInputControl::Type' of Qt, with the 2 names Qt gives in it.
    """

    LineEdit = Kee[int](0)
    TextEdit = Kee[int](1)

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
    Calls Qt's 'QString QInputControl::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputcontrol.html#tr

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
    #  QString QInputControl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QInputControl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QKeyEvent)
  @overload(NoneType)
  def isCommonTextEditShortcut(ke: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QInputControl::isCommonTextEditShortcut(const QKeyEvent
    *ke)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputcontrol.html#isCommonTextEditShortcut

    Parameters
    ----------

    ke : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QInputControl::isCommonTextEditShortcut(const QKeyEvent *ke)
    return Rituals.call(
        'ritual_ZN13QInputControl24isCommonTextEditShortcutEPK9QKeyEvent',
        CuteMixin._addressOf(ke),
    )

  @staticmethod
  @overload(QMimeData)
  @overload(NoneType)
  def selectionWrapper(mimeData: Optional[QMimeData]) -> QVariant:
    """
    Calls Qt's 'QVariant QInputControl::selectionWrapper(QMimeData
    *mimeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputcontrol.html#selectionWrapper

    Parameters
    ----------

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QInputControl::selectionWrapper(QMimeData *mimeData)
    address = Rituals.call(
        'ritual_ZN13QInputControl16selectionWrapperEP9QMimeData',
        CuteMixin._addressOf(mimeData),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QInputMethodEvent)
  @overload(NoneType)
  def mimeDataForInputEvent(
      event: Optional[QInputMethodEvent],
  ) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData
    *QInputControl::mimeDataForInputEvent(QInputMethodEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputcontrol.html#mimeDataForInputEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QInputControl::mimeDataForInputEvent(QInputMethodEvent
    #      *event)
    address = Rituals.call(
        'ritual_ZN13QInputControl21mimeDataForInputEventEP17QInputMethodEve'
        'nt',
        CuteMixin._addressOf(event),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QInputControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInputControl::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QInputControl10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QKeyEvent)
  @overload(NoneType)
  def isAcceptableInput(self, event: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QInputControl::isAcceptableInput(const QKeyEvent *event)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputcontrol.html#isAcceptableInput

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QInputControl::isAcceptableInput(const QKeyEvent *event) const
    return self.uglySide.call(
        'ritual_ZNK13QInputControl17isAcceptableInputEPK9QKeyEvent',
        self._addressOf(event),
    )

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

  @overload(Type)
  @overload(Type, QObject)
  @overload(Type, NoneType)
  def __init__(self, type: Type, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QInputControl::QInputControl(Type type,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputcontrol.html#QInputControl

    Parameters
    ----------

    type : Type
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QInputControl::QInputControl(Type type, QObject *parent)
    self._noteCreation(QInputControl, lambda: Rituals.call(
        'ritual_ZN13QInputControlC1ENS_4TypeEP7QObject',
        type.value, self._addressOf(parent, 'QObject'),
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
