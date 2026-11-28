"""
DeclarativeMargins binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativemargins_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means DeclarativeMargins to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QMargins, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeMargins(QObject, QMargins):
  """
  The cute side of Qt's DeclarativeMargins: a plain Python object standing in
  front of one C++ DeclarativeMargins.

  It is built on the cute 'QObject', as Qt's DeclarativeMargins is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QMargins' as well, as Qt's DeclarativeMargins is built on Qt's QMargins
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeMargins that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'setTop',
  'setBottom', 'setLeft', 'setRight', 'topChanged', 'bottomChanged',
  'leftChanged', 'rightChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeMargins::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DeclarativeMargins::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void DeclarativeMargins::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeMargins is created at the first use, not by
    'DeclarativeMargins(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeMargins.
  - Qt tells when it has removed the C++ DeclarativeMargins. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString DeclarativeMargins::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#tr

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
    #  QString DeclarativeMargins::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18DeclarativeMargins2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeMargins'

  #  Qt's DeclarativeMargins is built on more than one class. The part of a
  #  C++ DeclarativeMargins that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QMargins': 'ritual_cast_DeclarativeMargins_QMargins',
  }

  #  A C++ DeclarativeMargins Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeMargins'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeMargins::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeMargins::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18DeclarativeMargins10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTop(self, top: int) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::setTop(int top)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#setTop

    Parameters
    ----------

    top : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::setTop(int top)
    self.uglySide.call('ritual_ZN18DeclarativeMargins6setTopEi', top)

  @overload(int)
  def setBottom(self, bottom: int) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::setBottom(int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#setBottom

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::setBottom(int bottom)
    self.uglySide.call('ritual_ZN18DeclarativeMargins9setBottomEi', bottom)

  @overload(int)
  def setLeft(self, left: int) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::setLeft(int left)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#setLeft

    Parameters
    ----------

    left : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::setLeft(int left)
    self.uglySide.call('ritual_ZN18DeclarativeMargins7setLeftEi', left)

  @overload(int)
  def setRight(self, right: int) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::setRight(int right)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#setRight

    Parameters
    ----------

    right : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::setRight(int right)
    self.uglySide.call('ritual_ZN18DeclarativeMargins8setRightEi', right)

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
    'DeclarativeMargins::DeclarativeMargins(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativemargins.html#DeclarativeMargins

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeMargins::DeclarativeMargins(QObject *parent)
    self._noteCreation(DeclarativeMargins, lambda: Rituals.call(
        'ritual_ZN18DeclarativeMarginsC1EP7QObject',
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

  @overload(int, int, int, int)
  def topChanged(self, top: int, bottom: int, left: int, right: int) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::topChanged(int top, int bottom, int
    left, int right)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativemargins.html#topChanged

    Parameters
    ----------

    top : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    left : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::topChanged(int top, int bottom, int left, int
    #      right)
    self.uglySide.call(
        'ritual_ZN18DeclarativeMargins10topChangedEiiii',
        top, bottom, left, right,
    )

  @overload(int, int, int, int)
  def bottomChanged(
      self,
      top: int,
      bottom: int,
      left: int,
      right: int,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::bottomChanged(int top, int bottom,
    int left, int right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativemargins.html#bottomChanged

    Parameters
    ----------

    top : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    left : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::bottomChanged(int top, int bottom, int left,
    #      int right)
    self.uglySide.call(
        'ritual_ZN18DeclarativeMargins13bottomChangedEiiii',
        top, bottom, left, right,
    )

  @overload(int, int, int, int)
  def leftChanged(
      self,
      top: int,
      bottom: int,
      left: int,
      right: int,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::leftChanged(int top, int bottom, int
    left, int right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativemargins.html#leftChanged

    Parameters
    ----------

    top : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    left : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::leftChanged(int top, int bottom, int left,
    #      int right)
    self.uglySide.call(
        'ritual_ZN18DeclarativeMargins11leftChangedEiiii',
        top, bottom, left, right,
    )

  @overload(int, int, int, int)
  def rightChanged(
      self,
      top: int,
      bottom: int,
      left: int,
      right: int,
  ) -> None:
    """
    Calls Qt's 'void DeclarativeMargins::rightChanged(int top, int bottom,
    int left, int right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativemargins.html#rightChanged

    Parameters
    ----------

    top : int
      Passed on as it is.

    bottom : int
      Passed on as it is.

    left : int
      Passed on as it is.

    right : int
      Passed on as it is.
    """
    #  void DeclarativeMargins::rightChanged(int top, int bottom, int left,
    #      int right)
    self.uglySide.call(
        'ritual_ZN18DeclarativeMargins12rightChangedEiiii',
        top, bottom, left, right,
    )
