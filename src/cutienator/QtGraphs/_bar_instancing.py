"""
BarInstancing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/barinstancing_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means BarInstancing to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import BarItemHolder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BarItemHolder = WAIT['BarItemHolder']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BarInstancing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's BarInstancing: a plain Python object standing in
  front of one C++ BarInstancing.

  What exists
  -----------

  Every function of Qt's BarInstancing that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'dataArray',
  'setDataArray', 'markDataDirty', 'transparency', 'setTransparency',
  'clearDataArray'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BarInstancing::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int BarInstancing::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'BarInstancing::~BarInstancing()': the destructor: Python never
    removes a C++ BarInstancing.
  - Qt's 'QByteArray BarInstancing::getInstanceBuffer(int *instanceCount)':
    takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ BarInstancing is created at the first use, not by
    'BarInstancing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BarInstancing.
  - Qt tells when it has removed the C++ BarInstancing. Every call on the
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
    Calls Qt's 'QString BarInstancing::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#tr

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
    #  QString BarInstancing::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13BarInstancing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BarInstancing'

  #  A C++ BarInstancing Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BarInstancing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BarInstancing::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BarInstancing::metaObject() const
    address = self.uglySide.call('ritual_ZNK13BarInstancing10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataArray(self) -> QList[BarItemHolder]:
    """
    Calls Qt's 'QList<BarItemHolder *> BarInstancing::dataArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#dataArray

    Returns
    -------

    QList[BarItemHolder]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<BarItemHolder *> BarInstancing::dataArray() const
    address = self.uglySide.call('ritual_ZNK13BarInstancing9dataArrayEv')
    from . import BarItemHolder
    return QList[BarItemHolder]._cuteOwning(address)

  def transparency(self) -> bool:
    """
    Calls Qt's 'bool BarInstancing::transparency() const'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#transparency
    """
    #  bool BarInstancing::transparency() const
    return self.uglySide.call('ritual_ZNK13BarInstancing12transparencyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[BarItemHolder])
  def setDataArray(self, newDataArray: QList[BarItemHolder]) -> None:
    """
    Calls Qt's 'void BarInstancing::setDataArray(const QList<BarItemHolder *>
    &newDataArray)'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#setDataArray

    Parameters
    ----------

    newDataArray : QList[BarItemHolder]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void BarInstancing::setDataArray(const QList<BarItemHolder *>
    #      &newDataArray)
    self.uglySide.call(
        'ritual_ZN13BarInstancing12setDataArrayERK5QListIP13BarItemHolderE',
        self._valueOf(newDataArray),
    )

  @overload(bool)
  def setTransparency(self, newTransparencyValue: bool) -> None:
    """
    Calls Qt's 'void BarInstancing::setTransparency(bool
    newTransparencyValue)'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#setTransparency

    Parameters
    ----------

    newTransparencyValue : bool
      Passed on as it is.
    """
    #  void BarInstancing::setTransparency(bool newTransparencyValue)
    self.uglySide.call(
        'ritual_ZN13BarInstancing15setTransparencyEb', newTransparencyValue,
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
    Notes what was given, for Qt's 'BarInstancing::BarInstancing()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#BarInstancing
    """
    #  BarInstancing::BarInstancing()
    self._noteCreation(BarInstancing, lambda: Rituals.call(
        'ritual_ZN13BarInstancingC1Ev',
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

  def markDataDirty(self) -> None:
    """
    Calls Qt's 'void BarInstancing::markDataDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#markDataDirty
    """
    #  void BarInstancing::markDataDirty()
    self.uglySide.call('ritual_ZN13BarInstancing13markDataDirtyEv')

  def clearDataArray(self) -> None:
    """
    Calls Qt's 'void BarInstancing::clearDataArray()'.

    Qt's own words: https://doc.qt.io/qt-6/barinstancing.html#clearDataArray
    """
    #  void BarInstancing::clearDataArray()
    self.uglySide.call('ritual_ZN13BarInstancing14clearDataArrayEv')
