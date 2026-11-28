"""
DeclarativeBarSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeBarSet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtCharts import QBarSet

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeBarSet(QBarSet):
  """
  The cute side of Qt's DeclarativeBarSet: a plain Python object standing in
  front of one C++ DeclarativeBarSet.

  It is built on the cute 'QBarSet', as Qt's DeclarativeBarSet is built on
  Qt's QBarSet, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeBarSet that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'values',
  'setValues', 'borderWidth', 'setBorderWidth', 'brushFilename',
  'setBrushFilename', 'append', 'remove', 'replace', 'at', 'countChanged',
  'borderWidthChanged', 'brushFilenameChanged', 'handleCountChanged',
  'handleBrushChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeBarSet::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DeclarativeBarSet::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeBarSet is created at the first use, not by
    'DeclarativeBarSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeBarSet.
  - Qt tells when it has removed the C++ DeclarativeBarSet. Every call on the
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
    Calls Qt's 'QString DeclarativeBarSet::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#tr

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
    #  QString DeclarativeBarSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17DeclarativeBarSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeBarSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeBarSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeBarSet::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17DeclarativeBarSet10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal DeclarativeBarSet::borderWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#borderWidth
    """
    #  qreal DeclarativeBarSet::borderWidth() const
    return self.uglySide.call('ritual_ZNK17DeclarativeBarSet11borderWidthEv')

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeBarSet::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeBarSet::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK17DeclarativeBarSet13brushFilenameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def setValues(self, values: QList[QVariant]) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::setValues(QVariantList values)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#setValues

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativeBarSet::setValues(QVariantList values)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet9setValuesE5QListI8QVariantE',
        self._valueOf(values),
    )

  @overload(float)
  def setBorderWidth(self, borderWidth: float) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::setBorderWidth(qreal borderWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#setBorderWidth

    Parameters
    ----------

    borderWidth : float
      Passed on as it is.
    """
    #  void DeclarativeBarSet::setBorderWidth(qreal borderWidth)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet14setBorderWidthEd', borderWidth,
    )

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::setBrushFilename(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBarSet::setBrushFilename(const QString &brushFilename)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet16setBrushFilenameERK7QString',
        brushFilename,
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
    'DeclarativeBarSet::DeclarativeBarSet(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#DeclarativeBarSet

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeBarSet::DeclarativeBarSet(QObject *parent)
    self._noteCreation(DeclarativeBarSet, lambda: Rituals.call(
        'ritual_ZN17DeclarativeBarSetC1EP7QObject',
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

  def values(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList DeclarativeBarSet::values()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#values

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList DeclarativeBarSet::values()
    address = self.uglySide.call('ritual_ZN17DeclarativeBarSet6valuesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @overload(float)
  def append(self, value: float) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::append(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void DeclarativeBarSet::append(qreal value)
    self.uglySide.call('ritual_ZN17DeclarativeBarSet6appendEd', value)

  @overload(int)
  @overload(int, int)
  def remove(self, index: int, count: int = 1) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::remove(const int index, const int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void DeclarativeBarSet::remove(const int index, const int count)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet6removeEii', index, count,
    )

  @overload(int, float)
  def replace(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::replace(int index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void DeclarativeBarSet::replace(int index, qreal value)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet7replaceEid', index, value,
    )

  @overload(int)
  def at(self, index: int) -> float:
    """
    Calls Qt's 'qreal DeclarativeBarSet::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativebarset.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal DeclarativeBarSet::at(int index)
    return self.uglySide.call('ritual_ZN17DeclarativeBarSet2atEi', index)

  @overload(int)
  def countChanged(self, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::countChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#countChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void DeclarativeBarSet::countChanged(int count)
    self.uglySide.call('ritual_ZN17DeclarativeBarSet12countChangedEi', count)

  @overload(float)
  def borderWidthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::borderWidthChanged(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#borderWidthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void DeclarativeBarSet::borderWidthChanged(qreal width)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet18borderWidthChangedEd', width,
    )

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::brushFilenameChanged(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#brushFilenameChanged

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBarSet::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet20brushFilenameChangedERK7QString',
        brushFilename,
    )

  @overload(int, int)
  def handleCountChanged(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::handleCountChanged(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#handleCountChanged

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void DeclarativeBarSet::handleCountChanged(int index, int count)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBarSet18handleCountChangedEii', index, count,
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeBarSet::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativebarset.html#handleBrushChanged
    """
    #  void DeclarativeBarSet::handleBrushChanged()
    self.uglySide.call('ritual_ZN17DeclarativeBarSet18handleBrushChangedEv')
