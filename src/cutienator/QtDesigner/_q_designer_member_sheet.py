"""
QDesignerMemberSheet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_membersheet_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMemberSheet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QDesignerMemberSheetExtension

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMemberSheet(QObject, QDesignerMemberSheetExtension):
  """
  The cute side of Qt's QDesignerMemberSheet: a plain Python object standing
  in front of one C++ QDesignerMemberSheet.

  It is built on the cute 'QObject', as Qt's QDesignerMemberSheet is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QDesignerMemberSheetExtension' as well, as Qt's QDesignerMemberSheet is
  built on Qt's QDesignerMemberSheetExtension too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QDesignerMemberSheet that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'indexOf',
  'count', 'memberName', 'memberGroup', 'setMemberGroup', 'isVisible',
  'setVisible', 'isSignal', 'isSlot', 'inheritedFromWidget',
  'signalMatchesSlot', 'declaredInClass', 'signature', 'parameterTypes',
  'parameterNames'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerMemberSheet::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDesignerMemberSheet::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerMemberSheet::~QDesignerMemberSheet()': the destructor:
    Python never removes a C++ QDesignerMemberSheet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerMemberSheet is created at the first use, not by
    'QDesignerMemberSheet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMemberSheet.
  - Qt tells when it has removed the C++ QDesignerMemberSheet. Every call on
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
    Calls Qt's 'QString QDesignerMemberSheet::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermembersheet.html#tr

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
    #  QString QDesignerMemberSheet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QDesignerMemberSheet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str, str)
  def signalMatchesSlot(signal: str, slot: str) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheet::signalMatchesSlot(const QString
    &signal, const QString &slot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#signalMatchesSlot

    Parameters
    ----------

    signal : str
      Passed on as it is: a QString is made of it for the call.

    slot : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerMemberSheet::signalMatchesSlot(const QString &signal,
    #      const QString &slot)
    return Rituals.call(
        'ritual_ZN20QDesignerMemberSheet17signalMatchesSlotERK7QStringS2_',
        signal, slot,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMemberSheet'

  #  Qt's QDesignerMemberSheet is built on more than one class. The part of a
  #  C++ QDesignerMemberSheet that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDesignerMemberSheetExtension':
          'ritual_cast_QDesignerMemberSheet_QDesignerMemberSheetExtension',
  }

  #  A C++ QDesignerMemberSheet Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMemberSheet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerMemberSheet::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerMemberSheet::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QDesignerMemberSheet10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def indexOf(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerMemberSheet::indexOf(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermembersheet.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMemberSheet::indexOf(const QString &name) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet7indexOfERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet7indexOfERK7QString'
    return self.uglySide.call(ritual, name)

  def count(self) -> int:
    """
    Calls Qt's 'int QDesignerMemberSheet::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermembersheet.html#count
    """
    #  int QDesignerMemberSheet::count() const
    ritual = 'ritual_ZNK20QDesignerMemberSheet5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def memberName(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheet::memberName(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#memberName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheet::memberName(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet10memberNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet10memberNameEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def memberGroup(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheet::memberGroup(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#memberGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheet::memberGroup(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet11memberGroupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet11memberGroupEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def isVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheet::isVisible(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#isVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheet::isVisible(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet9isVisibleEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet9isVisibleEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def isSignal(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheet::isSignal(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermembersheet.html#isSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheet::isSignal(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet8isSignalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet8isSignalEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def isSlot(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheet::isSlot(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermembersheet.html#isSlot

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheet::isSlot(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet6isSlotEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet6isSlotEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def inheritedFromWidget(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheet::inheritedFromWidget(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#inheritedFromWidget

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheet::inheritedFromWidget(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet19inheritedFromWidgetEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet19inheritedFromWidgetEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def declaredInClass(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheet::declaredInClass(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#declaredInClass

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheet::declaredInClass(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet15declaredInClassEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet15declaredInClassEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def signature(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheet::signature(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#signature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheet::signature(int index) const
    ritual = 'ritual_ZNK20QDesignerMemberSheet9signatureEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDesignerMemberSheet9signatureEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def parameterTypes(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QDesignerMemberSheet::parameterTypes(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#parameterTypes

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QDesignerMemberSheet::parameterTypes(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QDesignerMemberSheet14parameterTypesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def parameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QDesignerMemberSheet::parameterNames(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#parameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QDesignerMemberSheet::parameterNames(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QDesignerMemberSheet14parameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, str)
  def setMemberGroup(self, index: int, group: str) -> None:
    """
    Calls Qt's 'void QDesignerMemberSheet::setMemberGroup(int index, const
    QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#setMemberGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerMemberSheet::setMemberGroup(int index, const QString
    #      &group)
    ritual = 'ritual_ZN20QDesignerMemberSheet14setMemberGroupEiRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDesignerMemberSheet14setMemberGroupEiRK7QString')
    self.uglySide.call(ritual, index, group)

  @overload(int, bool)
  def setVisible(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerMemberSheet::setVisible(int index, bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#setVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerMemberSheet::setVisible(int index, bool b)
    ritual = 'ritual_ZN20QDesignerMemberSheet10setVisibleEib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDesignerMemberSheet10setVisibleEib'
    self.uglySide.call(ritual, index, b)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerMemberSheet::QDesignerMemberSheet(QObject *object, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheet.html#QDesignerMemberSheet

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerMemberSheet::QDesignerMemberSheet(QObject *object, QObject
    #      *parent)
    self._noteCreation(QDesignerMemberSheet, lambda: Rituals.call(
        'ritual_ZN20QDesignerMemberSheetC1EP7QObjectS1_',
        self._addressOf(object, 'QObject'), self._addressOf(parent,
        'QObject'),
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
