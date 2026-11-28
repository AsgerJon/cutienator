"""
ScatterInstancing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/scatterinstancing_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ScatterInstancing to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import DataItemHolder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DataItemHolder = WAIT['DataItemHolder']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScatterInstancing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ScatterInstancing: a plain Python object standing in
  front of one C++ ScatterInstancing.

  What exists
  -----------

  Every function of Qt's ScatterInstancing that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'dataArray',
  'setDataArray', 'hideDataItem', 'unhidePreviousDataItem', 'resetVisibilty',
  'markDataDirty', 'rangeGradient', 'setRangeGradient', 'setTransparency',
  'isDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ScatterInstancing::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ScatterInstancing::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QList<float> &ScatterInstancing::customData() const': gives a
    type Python has no way to take yet.
  - Qt's 'void ScatterInstancing::setCustomData(const QList<float>
    &newCustomData)': takes a type Python has no way to hand over yet.
  - Qt's 'QByteArray ScatterInstancing::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ScatterInstancing is created at the first use, not by
    'ScatterInstancing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ScatterInstancing.
  - Qt tells when it has removed the C++ ScatterInstancing. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ScatterInstancing that has no cute function yet,
    'customData', 'setCustomData', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString ScatterInstancing::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterinstancing.html#tr

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
    #  QString ScatterInstancing::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17ScatterInstancing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterInstancing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ScatterInstancing::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterinstancing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ScatterInstancing::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17ScatterInstancing10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataArray(self) -> QList[DataItemHolder]:
    """
    Calls Qt's 'const QList<DataItemHolder> &ScatterInstancing::dataArray()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterinstancing.html#dataArray

    Returns
    -------

    QList[DataItemHolder]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<DataItemHolder> &ScatterInstancing::dataArray() const
    address = self.uglySide.call('ritual_ZNK17ScatterInstancing9dataArrayEv')
    from . import DataItemHolder
    return QList[DataItemHolder]._cuteOwning(address)

  def rangeGradient(self) -> bool:
    """
    Calls Qt's 'bool ScatterInstancing::rangeGradient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#rangeGradient
    """
    #  bool ScatterInstancing::rangeGradient() const
    return self.uglySide.call(
        'ritual_ZNK17ScatterInstancing13rangeGradientEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool ScatterInstancing::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterinstancing.html#isDirty
    """
    #  bool ScatterInstancing::isDirty() const
    return self.uglySide.call('ritual_ZNK17ScatterInstancing7isDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[DataItemHolder])
  def setDataArray(self, newDataArray: QList[DataItemHolder]) -> None:
    """
    Calls Qt's 'void ScatterInstancing::setDataArray(const
    QList<DataItemHolder> &newDataArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#setDataArray

    Parameters
    ----------

    newDataArray : QList[DataItemHolder]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ScatterInstancing::setDataArray(const QList<DataItemHolder>
    #      &newDataArray)
    self.uglySide.call(
        'ritual_ZN17ScatterInstancing12setDataArrayERK5QListI14DataItemHold'
        'erE',
        self._valueOf(newDataArray),
    )

  @overload(bool)
  def setRangeGradient(self, newRangeGradient: bool) -> None:
    """
    Calls Qt's 'void ScatterInstancing::setRangeGradient(bool
    newRangeGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#setRangeGradient

    Parameters
    ----------

    newRangeGradient : bool
      Passed on as it is.
    """
    #  void ScatterInstancing::setRangeGradient(bool newRangeGradient)
    self.uglySide.call(
        'ritual_ZN17ScatterInstancing16setRangeGradientEb', newRangeGradient,
    )

  @overload(bool)
  def setTransparency(self, transparency: bool) -> None:
    """
    Calls Qt's 'void ScatterInstancing::setTransparency(bool transparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#setTransparency

    Parameters
    ----------

    transparency : bool
      Passed on as it is.
    """
    #  void ScatterInstancing::setTransparency(bool transparency)
    self.uglySide.call(
        'ritual_ZN17ScatterInstancing15setTransparencyEb', transparency,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'ScatterInstancing::ScatterInstancing()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#ScatterInstancing
    """
    #  ScatterInstancing::ScatterInstancing()
    self._noteCreation(ScatterInstancing, lambda: Rituals.call(
        'ritual_ZN17ScatterInstancingC1Ev',
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

  @overload(int)
  def hideDataItem(self, index: int) -> None:
    """
    Calls Qt's 'void ScatterInstancing::hideDataItem(qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#hideDataItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void ScatterInstancing::hideDataItem(qsizetype index)
    self.uglySide.call('ritual_ZN17ScatterInstancing12hideDataItemEx', index)

  def unhidePreviousDataItem(self) -> None:
    """
    Calls Qt's 'void ScatterInstancing::unhidePreviousDataItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#unhidePreviousDataItem
    """
    #  void ScatterInstancing::unhidePreviousDataItem()
    self.uglySide.call(
        'ritual_ZN17ScatterInstancing22unhidePreviousDataItemEv',
    )

  def resetVisibilty(self) -> None:
    """
    Calls Qt's 'void ScatterInstancing::resetVisibilty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#resetVisibilty
    """
    #  void ScatterInstancing::resetVisibilty()
    self.uglySide.call('ritual_ZN17ScatterInstancing14resetVisibiltyEv')

  def markDataDirty(self) -> None:
    """
    Calls Qt's 'void ScatterInstancing::markDataDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterinstancing.html#markDataDirty
    """
    #  void ScatterInstancing::markDataDirty()
    self.uglySide.call('ritual_ZN17ScatterInstancing13markDataDirtyEv')

  @staticmethod
  def customData(*__, **_) -> Never:
    """
    Qt's 'const QList<float> &ScatterInstancing::customData() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ScatterInstancing.customData' has no cute function yet. Qt's "
        "'const QList<float> &ScatterInstancing::customData() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setCustomData(*__, **_) -> Never:
    """
    Qt's 'void ScatterInstancing::setCustomData(const QList<float>
    &newCustomData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ScatterInstancing.setCustomData' has no cute function yet. Qt's "
        "'void ScatterInstancing::setCustomData(const QList<float> "
        "&newCustomData)': takes a type Python has no way to hand over yet.")
