"""
DeclarativeBoxSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeboxplotseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeBoxSet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtCharts import QBoxSet

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


class DeclarativeBoxSet(QBoxSet):
  """
  The cute side of Qt's DeclarativeBoxSet: a plain Python object standing in
  front of one C++ DeclarativeBoxSet.

  It is built on the cute 'QBoxSet', as Qt's DeclarativeBoxSet is built on
  Qt's QBoxSet, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeBoxSet that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'values',
  'setValues', 'brushFilename', 'setBrushFilename', 'append', 'clear', 'at',
  'setValue', 'changedValues', 'changedValue', 'brushFilenameChanged',
  'handleBrushChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeBoxSet::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DeclarativeBoxSet::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeBoxSet is created at the first use, not by
    'DeclarativeBoxSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeBoxSet.
  - Qt tells when it has removed the C++ DeclarativeBoxSet. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside DeclarativeBoxSet, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ValuePositions(CuteNum):
    """
    The enum 'DeclarativeBoxSet::ValuePositions' of Qt, with the 5 names Qt
    gives in it.
    """

    LowerExtreme = Kee[int](0)
    LowerQuartile = Kee[int](1)
    Median = Kee[int](2)
    UpperQuartile = Kee[int](3)
    UpperExtreme = Kee[int](4)

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
    Calls Qt's 'QString DeclarativeBoxSet::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#tr

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
    #  QString DeclarativeBoxSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17DeclarativeBoxSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeBoxSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeBoxSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeBoxSet::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17DeclarativeBoxSet10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeBoxSet::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeBoxSet::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK17DeclarativeBoxSet13brushFilenameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVariant])
  def setValues(self, values: QList[QVariant]) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::setValues(QVariantList values)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#setValues

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativeBoxSet::setValues(QVariantList values)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBoxSet9setValuesE5QListI8QVariantE',
        self._valueOf(values),
    )

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::setBrushFilename(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBoxSet::setBrushFilename(const QString &brushFilename)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBoxSet16setBrushFilenameERK7QString',
        brushFilename,
    )

  @overload(int, float)
  def setValue(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::setValue(int index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#setValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void DeclarativeBoxSet::setValue(int index, qreal value)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBoxSet8setValueEid', index, value,
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
  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      label: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeBoxSet::DeclarativeBoxSet(const QString label, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#DeclarativeBoxSet

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeBoxSet::DeclarativeBoxSet(const QString label, QObject
    #      *parent)
    self._noteCreation(DeclarativeBoxSet, lambda: Rituals.call(
        'ritual_ZN17DeclarativeBoxSetC1E7QStringP7QObject',
        label, self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'QVariantList DeclarativeBoxSet::values()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#values

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList DeclarativeBoxSet::values()
    address = self.uglySide.call('ritual_ZN17DeclarativeBoxSet6valuesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @overload(float)
  def append(self, value: float) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::append(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void DeclarativeBoxSet::append(qreal value)
    self.uglySide.call('ritual_ZN17DeclarativeBoxSet6appendEd', value)

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#clear
    """
    #  void DeclarativeBoxSet::clear()
    self.uglySide.call('ritual_ZN17DeclarativeBoxSet5clearEv')

  @overload(int)
  def at(self, index: int) -> float:
    """
    Calls Qt's 'qreal DeclarativeBoxSet::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeboxset.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal DeclarativeBoxSet::at(int index)
    return self.uglySide.call('ritual_ZN17DeclarativeBoxSet2atEi', index)

  def changedValues(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::changedValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#changedValues
    """
    #  void DeclarativeBoxSet::changedValues()
    self.uglySide.call('ritual_ZN17DeclarativeBoxSet13changedValuesEv')

  @overload(int)
  def changedValue(self, index: int) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::changedValue(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#changedValue

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void DeclarativeBoxSet::changedValue(int index)
    self.uglySide.call('ritual_ZN17DeclarativeBoxSet12changedValueEi', index)

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::brushFilenameChanged(const QString
    &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#brushFilenameChanged

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeBoxSet::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN17DeclarativeBoxSet20brushFilenameChangedERK7QString',
        brushFilename,
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeBoxSet::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeboxset.html#handleBrushChanged
    """
    #  void DeclarativeBoxSet::handleBrushChanged()
    self.uglySide.call('ritual_ZN17DeclarativeBoxSet18handleBrushChangedEv')
