"""
QQuickFlipable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickflipable_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickFlipable to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlipable(QQuickItem):
  """
  The cute side of Qt's QQuickFlipable: a plain Python object standing in
  front of one C++ QQuickFlipable.

  It is built on the cute 'QQuickItem', as Qt's QQuickFlipable is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFlipable that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'front', 'setFront',
  'back', 'setBack', 'side', 'frontChanged', 'backChanged', 'sideChanged',
  'updatePolish', 'retransformBack'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFlipable::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickFlipable::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFlipable::~QQuickFlipable()': the destructor: Python never
    removes a C++ QQuickFlipable.
  - Qt's 'QQuickFlipablePrivate *QQuickFlipable::d_func()': gives
    'QQuickFlipablePrivate', which has no cute class yet.
  - Qt's 'const QQuickFlipablePrivate *QQuickFlipable::d_func() const': gives
    'QQuickFlipablePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFlipable is created at the first use, not by
    'QQuickFlipable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlipable.
  - Qt tells when it has removed the C++ QQuickFlipable. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickFlipable, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Side(CuteNum):
    """
    The enum 'QQuickFlipable::Side' of Qt, with the 2 names Qt gives in it.
    """

    Front = Kee[int](0)
    Back = Kee[int](1)

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
    Calls Qt's 'QString QQuickFlipable::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#tr

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
    #  QString QQuickFlipable::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickFlipable2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlipable'

  #  A C++ QQuickFlipable Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFlipable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFlipable::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFlipable::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickFlipable10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def front(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickFlipable::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#front

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickFlipable::front() const
    address = self.uglySide.call('ritual_ZNK14QQuickFlipable5frontEv')
    return QQuickItem._cuteAt(address)

  def side(self) -> Side:
    """
    Calls Qt's 'Side QQuickFlipable::side() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#side

    Returns
    -------

    Side
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Side(number)' gives.
    """
    #  Side QQuickFlipable::side() const
    return QQuickFlipable.Side(self.uglySide.call(
        'ritual_ZNK14QQuickFlipable4sideEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setFront(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickFlipable::setFront(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#setFront

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlipable::setFront(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickFlipable8setFrontEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBack(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickFlipable::setBack(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#setBack

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlipable::setBack(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickFlipable7setBackEP10QQuickItem',
        self._addressOf(a0),
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
    Notes what was given, for Qt's 'QQuickFlipable::QQuickFlipable(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#QQuickFlipable

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFlipable::QQuickFlipable(QQuickItem *parent)
    self._noteCreation(QQuickFlipable, lambda: Rituals.call(
        'ritual_ZN14QQuickFlipableC1EP10QQuickItem', self._addressOf(parent),
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

  def back(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickFlipable::back()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#back

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickFlipable::back()
    address = self.uglySide.call('ritual_ZN14QQuickFlipable4backEv')
    return QQuickItem._cuteAt(address)

  def frontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlipable::frontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#frontChanged
    """
    #  void QQuickFlipable::frontChanged()
    self.uglySide.call('ritual_ZN14QQuickFlipable12frontChangedEv')

  def backChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlipable::backChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#backChanged
    """
    #  void QQuickFlipable::backChanged()
    self.uglySide.call('ritual_ZN14QQuickFlipable11backChangedEv')

  def sideChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlipable::sideChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#sideChanged
    """
    #  void QQuickFlipable::sideChanged()
    self.uglySide.call('ritual_ZN14QQuickFlipable11sideChangedEv')

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickFlipable::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflipable.html#updatePolish
    """
    #  void QQuickFlipable::updatePolish()
    ritual = 'ritual_ZN14QQuickFlipable12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickFlipable12updatePolishEv'
    self.uglySide.call(ritual)

  def retransformBack(self) -> None:
    """
    Calls Qt's 'void QQuickFlipable::retransformBack()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflipable.html#retransformBack
    """
    #  void QQuickFlipable::retransformBack()
    self.uglySide.call('ritual_ZN14QQuickFlipable15retransformBackEv')
