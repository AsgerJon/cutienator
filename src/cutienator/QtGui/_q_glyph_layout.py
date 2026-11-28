"""
QGlyphLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QGlyphLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFixed

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGlyphLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGlyphLayout: a plain Python object standing in front
  of one C++ QGlyphLayout.

  C++ hands a QGlyphLayout around as a copy, so every C++ QGlyphLayout behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGlyphLayout that has a ritual and that Python can
  call so far, 4 names in all: 'mid', 'effectiveAdvance', 'clear', 'copy'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGlyphLayout::QGlyphLayout(char *address, int totalGlyphs)': names
    'char', which has no cute class yet.
  - Qt's 'char *QGlyphLayout::data()': gives 'char', which has no cute class
    yet.
  - Qt's 'void QGlyphLayout::grow(char *address, int totalGlyphs)': names
    'char', which has no cute class yet.
  - Qt's 'QGlyphLayout::~QGlyphLayout()': the destructor: Python removes its
    C++ QGlyphLayout by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGlyphLayout is created at the first use, not by
    'QGlyphLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGlyphLayout back gives a copy the ritual made for
    Python, in a new cute QGlyphLayout.
  - Each name of Qt's QGlyphLayout that has no cute function yet, 'data',
    'grow', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGlyphLayout'

  #  Qt's '~QGlyphLayout()'. Naming it makes this a value class: Python owns
  #  every C++ QGlyphLayout behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QGlyphLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, int)
  def mid(self, position: int, n: int = -1) -> QGlyphLayout:
    """
    Calls Qt's 'QGlyphLayout QGlyphLayout::mid(int position, int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphlayout.html#mid

    Parameters
    ----------

    position : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QGlyphLayout
      A new cute QGlyphLayout around the copy Qt gave back. Python owns it.
    """
    #  QGlyphLayout QGlyphLayout::mid(int position, int n) const
    address = self._callAs(
        'QGlyphLayout', 'ritual_ZNK12QGlyphLayout3midEii', position, n,
    )
    return QGlyphLayout._cuteOwning(address)

  @overload(int)
  def effectiveAdvance(self, item: int) -> QFixed:
    """
    Calls Qt's 'QFixed QGlyphLayout::effectiveAdvance(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphlayout.html#effectiveAdvance

    Parameters
    ----------

    item : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QGlyphLayout::effectiveAdvance(int item) const
    address = self._callAs(
        'QGlyphLayout', 'ritual_ZNK12QGlyphLayout16effectiveAdvanceEi', item,
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

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
    Notes what was given, for Qt's 'QGlyphLayout::QGlyphLayout()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qglyphlayout.html#QGlyphLayout
    """
    #  QGlyphLayout::QGlyphLayout()
    self._noteCreation(QGlyphLayout, lambda: Rituals.call(
        'ritual_ZN12QGlyphLayoutC1Ev',
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

  @overload()
  @overload(int)
  @overload(int, int)
  def clear(self, first: int = 0, last: int = -1) -> None:
    """
    Calls Qt's 'void QGlyphLayout::clear(int first, int last)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphlayout.html#clear

    Parameters
    ----------

    first : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    last : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QGlyphLayout::clear(int first, int last)
    self._callAs(
        'QGlyphLayout', 'ritual_ZN12QGlyphLayout5clearEii', first, last,
    )

  @overload(THIS)
  @overload(NoneType)
  def copy(self, other: Optional[QGlyphLayout]) -> None:
    """
    Calls Qt's 'void QGlyphLayout::copy(QGlyphLayout *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphlayout.html#copy

    Parameters
    ----------

    other : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGlyphLayout::copy(QGlyphLayout *other)
    self._callAs(
        'QGlyphLayout', 'ritual_ZN12QGlyphLayout4copyEPS_',
        self._addressOf(other, 'QGlyphLayout'),
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'char *QGlyphLayout::data()': gives 'char', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QGlyphLayout.data' has no cute function yet. Qt's 'char "
        "*QGlyphLayout::data()': gives 'char', which has no cute class yet.")

  @staticmethod
  def grow(*__, **_) -> Never:
    """
    Qt's 'void QGlyphLayout::grow(char *address, int totalGlyphs)': names
    'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGlyphLayout.grow' has no cute function yet. Qt's 'void "
        "QGlyphLayout::grow(char *address, int totalGlyphs)': names 'char', "
        "which has no cute class yet.")
