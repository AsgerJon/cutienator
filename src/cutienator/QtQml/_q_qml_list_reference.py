"""
QQmlListReference binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmllist.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject, QVariant
  from . import QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlListReference(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlListReference: a plain Python object standing in
  front of one C++ QQmlListReference.

  C++ hands a QQmlListReference around as a copy, so every C++
  QQmlListReference behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlListReference that has a ritual and that Python
  can call so far, 19 names in all: 'isValid', 'object', 'listElementType',
  'canAppend', 'canAt', 'canClear', 'canCount', 'canReplace',
  'canRemoveLast', 'isManipulable', 'isReadable', 'append', 'at', 'clear',
  'count', 'size', 'replace', 'removeLast', '__eq__'. It can be made from
  Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlListReference &QQmlListReference::operator=(const
    QQmlListReference &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQmlListReference::~QQmlListReference()': the destructor: Python
    removes its C++ QQmlListReference by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlListReference is created at the first use, not by
    'QQmlListReference(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlListReference back gives a copy the ritual made
    for Python, in a new cute QQmlListReference.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListReference'

  #  Qt's '~QQmlListReference()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlListReference behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQmlListReferenceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#isValid
    """
    #  bool QQmlListReference::isValid() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference7isValidEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlListReference::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlListReference::object() const
    address = self.uglySide.call('ritual_ZNK17QQmlListReference6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def listElementType(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlListReference::listElementType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#listElementType

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlListReference::listElementType() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlListReference15listElementTypeEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def canAppend(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canAppend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#canAppend
    """
    #  bool QQmlListReference::canAppend() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference9canAppendEv')

  def canAt(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canAt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#canAt
    """
    #  bool QQmlListReference::canAt() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference5canAtEv')

  def canClear(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canClear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#canClear
    """
    #  bool QQmlListReference::canClear() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference8canClearEv')

  def canCount(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#canCount
    """
    #  bool QQmlListReference::canCount() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference8canCountEv')

  def canReplace(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canReplace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#canReplace
    """
    #  bool QQmlListReference::canReplace() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference10canReplaceEv')

  def canRemoveLast(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::canRemoveLast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#canRemoveLast
    """
    #  bool QQmlListReference::canRemoveLast() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlListReference13canRemoveLastEv',
    )

  def isManipulable(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::isManipulable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#isManipulable
    """
    #  bool QQmlListReference::isManipulable() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlListReference13isManipulableEv',
    )

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#isReadable
    """
    #  bool QQmlListReference::isReadable() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference10isReadableEv')

  @overload(QObject)
  @overload(NoneType)
  def append(self, a0: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::append(QObject *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#append

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlListReference::append(QObject *a0) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlListReference6appendEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(int)
  def at(self, a0: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlListReference::at(qsizetype a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#at

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlListReference::at(qsizetype a0) const
    address = self.uglySide.call('ritual_ZNK17QQmlListReference2atEx', a0)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def clear(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::clear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#clear
    """
    #  bool QQmlListReference::clear() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference5clearEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlListReference::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#count
    """
    #  qsizetype QQmlListReference::count() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference5countEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlListReference::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#size
    """
    #  qsizetype QQmlListReference::size() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference4sizeEv')

  @overload(int, QObject)
  @overload(int, NoneType)
  def replace(self, a0: int, a1: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::replace(qsizetype a0, QObject *a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#replace

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlListReference::replace(qsizetype a0, QObject *a1) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlListReference7replaceExP7QObject',
        a0, self._addressOf(a1, 'QObject'),
    )

  def removeLast(self) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::removeLast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#removeLast
    """
    #  bool QQmlListReference::removeLast() const
    return self.uglySide.call('ritual_ZNK17QQmlListReference10removeLastEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQmlListReference) -> bool:
    """
    Calls Qt's 'bool QQmlListReference::operator==(const QQmlListReference
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistreference.html#operator==

    Parameters
    ----------

    other : QQmlListReference
      Passed on as a value: Qt reads the C++ QQmlListReference, which stays
      Python's own.
    """
    #  bool QQmlListReference::operator==(const QQmlListReference &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QQmlListReferenceeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlListReference::QQmlListReference()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference
    """
    #  QQmlListReference::QQmlListReference()
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1Ev',
    ))

  @overload(QVariant, QQmlEngine)
  @overload(QVariant, NoneType)
  def __init__(
      self,
      variant: QVariant,
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListReference::QQmlListReference(const QVariant &variant, QQmlEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlListReference::QQmlListReference(const QVariant &variant,
    #      QQmlEngine *engine)
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1ERK8QVariantP10QQmlEngine',
        self._valueOf(variant), self._addressOf(engine),
    ))

  @overload(QObject, str, QQmlEngine)
  @overload(QObject, str, NoneType)
  @overload(QObject, NoneType, QQmlEngine)
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, str, QQmlEngine)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, QQmlEngine)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      o: Optional[QObject],
      property: Optional[str],
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListReference::QQmlListReference(QObject *o, const char *property,
    QQmlEngine *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlListReference::QQmlListReference(QObject *o, const char *property,
    #      QQmlEngine *engine)
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1EP7QObjectPKcP10QQmlEngine',
        self._addressOf(o, 'QObject'), self._bytesOf(property),
        self._addressOf(engine),
    ))

  @overload(QVariant)
  def __init__(self, variant: QVariant) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListReference::QQmlListReference(const QVariant &variant)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QQmlListReference::QQmlListReference(const QVariant &variant)
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1ERK8QVariant', self._valueOf(variant),
    ))

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def __init__(self, o: Optional[QObject], property: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListReference::QQmlListReference(QObject *o, const char *property)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QQmlListReference::QQmlListReference(QObject *o, const char *property)
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1EP7QObjectPKc',
        self._addressOf(o, 'QObject'), self._bytesOf(property),
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlListReference) -> None:
    """
    Notes what was given, for Qt's
    'QQmlListReference::QQmlListReference(const QQmlListReference &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistreference.html#QQmlListReference

    Parameters
    ----------

    a0 : QQmlListReference
      Passed on as a value: Qt reads the C++ QQmlListReference, which stays
      Python's own.
    """
    #  QQmlListReference::QQmlListReference(const QQmlListReference &a0)
    self._noteCreation(QQmlListReference, lambda: Rituals.call(
        'ritual_ZN17QQmlListReferenceC1ERKS_', self._valueOf(a0),
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
