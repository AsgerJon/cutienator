"""
DeclarativeCategoryRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeCategoryRange to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeCategoryRange(QObject):
  """
  The cute side of Qt's DeclarativeCategoryRange: a plain Python object
  standing in front of one C++ DeclarativeCategoryRange.

  It is built on the cute 'QObject', as Qt's DeclarativeCategoryRange is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeCategoryRange that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'endValue',
  'setEndValue', 'label', 'setLabel'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeCategoryRange::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int DeclarativeCategoryRange::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeCategoryRange is created at the first use, not by
    'DeclarativeCategoryRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeCategoryRange.
  - Qt tells when it has removed the C++ DeclarativeCategoryRange. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString DeclarativeCategoryRange::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativecategoryrange.html#tr

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
    #  QString DeclarativeCategoryRange::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24DeclarativeCategoryRange2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeCategoryRange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeCategoryRange::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeCategoryRange::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24DeclarativeCategoryRange10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setEndValue(self, endValue: float) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryRange::setEndValue(qreal endValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html#setEndValue

    Parameters
    ----------

    endValue : float
      Passed on as it is.
    """
    #  void DeclarativeCategoryRange::setEndValue(qreal endValue)
    self.uglySide.call(
        'ritual_ZN24DeclarativeCategoryRange11setEndValueEd', endValue,
    )

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void DeclarativeCategoryRange::setLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCategoryRange::setLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN24DeclarativeCategoryRange8setLabelERK7QString', label,
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
    'DeclarativeCategoryRange::DeclarativeCategoryRange(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeCategoryRange::DeclarativeCategoryRange(QObject *parent)
    self._noteCreation(DeclarativeCategoryRange, lambda: Rituals.call(
        'ritual_ZN24DeclarativeCategoryRangeC1EP7QObject',
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

  def endValue(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeCategoryRange::endValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html#endValue
    """
    #  qreal DeclarativeCategoryRange::endValue()
    return self.uglySide.call(
        'ritual_ZN24DeclarativeCategoryRange8endValueEv',
    )

  def label(self) -> str:
    """
    Calls Qt's 'QString DeclarativeCategoryRange::label()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecategoryrange.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeCategoryRange::label()
    return self.uglySide.call('ritual_ZN24DeclarativeCategoryRange5labelEv')
