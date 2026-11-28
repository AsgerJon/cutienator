"""
QtPrivate::QIOOperationDataStorage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qiooperation_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QtPrivate::QIOOperationDataStorage to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QIOOperationDataStorage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QIOOperationDataStorage: a plain Python
  object standing in front of one C++ QtPrivate::QIOOperationDataStorage.

  C++ hands a QtPrivate::QIOOperationDataStorage around as a copy, so every
  C++ QtPrivate::QIOOperationDataStorage behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::QIOOperationDataStorage that has a ritual
  and that Python can call so far, 5 names in all: 'isEmpty',
  'containsReadSpans', 'containsWriteSpans', 'containsByteArray',
  'getByteArray'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QSpan<const
    QSpan<std::byte>> s)': takes a type Python has no way to hand over yet.
  - Qt's
    'QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QSpan<const
    QSpan<const std::byte>> s)': takes a type Python has no way to hand over
    yet.
  - Qt's
    'QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(QByteArray
    &&a)': takes a type Python has no way to hand over yet.
  - Qt's 'ReadSpans &QtPrivate::QIOOperationDataStorage::getReadSpans()':
    gives a type Python has no way to take yet.
  - Qt's 'const ReadSpans &QtPrivate::QIOOperationDataStorage::getReadSpans()
    const': gives a type Python has no way to take yet.
  - Qt's 'WriteSpans &QtPrivate::QIOOperationDataStorage::getWriteSpans()':
    gives a type Python has no way to take yet.
  - Qt's 'const WriteSpans
    &QtPrivate::QIOOperationDataStorage::getWriteSpans() const': gives a type
    Python has no way to take yet.
  - Qt's 'QByteArray &QtPrivate::QIOOperationDataStorage::getByteArray()':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::QIOOperationDataStorage::~QIOOperationDataStorage()':
    the destructor: Python removes its C++ QtPrivate::QIOOperationDataStorage
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QtPrivate::QIOOperationDataStorage is created at the first use,
    not by 'QtPrivate::QIOOperationDataStorage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QIOOperationDataStorage back gives a copy
    the ritual made for Python, in a new cute
    QtPrivate::QIOOperationDataStorage.
  - Each name of Qt's QtPrivate::QIOOperationDataStorage that has no cute
    function yet, 'getReadSpans', 'getValue', 'getWriteSpans', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QIOOperationDataStorage'

  #  Qt's '~QtPrivate::QIOOperationDataStorage()'. Naming it makes this a
  #  value class: Python owns every C++ QtPrivate::QIOOperationDataStorage
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate23QIOOperationDataStorageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QIOOperationDataStorage::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html#isEmpty
    """
    #  bool QtPrivate::QIOOperationDataStorage::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate23QIOOperationDataStorage7isEmptyEv',
    )

  def containsReadSpans(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QIOOperationDataStorage::containsReadSpans()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html
    """
    #  bool QtPrivate::QIOOperationDataStorage::containsReadSpans() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate23QIOOperationDataStorage17containsReadSpansEv',
    )

  def containsWriteSpans(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QIOOperationDataStorage::containsWriteSpans()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html
    """
    #  bool QtPrivate::QIOOperationDataStorage::containsWriteSpans() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate23QIOOperationDataStorage18containsWriteSpansE'
        'v',
    )

  def containsByteArray(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QIOOperationDataStorage::containsByteArray()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html
    """
    #  bool QtPrivate::QIOOperationDataStorage::containsByteArray() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate23QIOOperationDataStorage17containsByteArrayEv',
    )

  def getByteArray(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray
    &QtPrivate::QIOOperationDataStorage::getByteArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QtPrivate::QIOOperationDataStorage::getByteArray()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate23QIOOperationDataStorage12getByteArrayEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html
    """
    #  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage()
    self._noteCreation(QIOOperationDataStorage, lambda: Rituals.call(
        'ritual_ZN9QtPrivate23QIOOperationDataStorageC1Ev',
    ))

  @overload(QByteArray)
  def __init__(self, a: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(const
    QByteArray &a)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qiooperationdatastorage.html

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QtPrivate::QIOOperationDataStorage::QIOOperationDataStorage(const
    #      QByteArray &a)
    self._noteCreation(QIOOperationDataStorage, lambda: Rituals.call(
        'ritual_ZN9QtPrivate23QIOOperationDataStorageC1ERK10QByteArray',
        self._valueOf(a),
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

  @staticmethod
  def getReadSpans(*__, **_) -> Never:
    """
    - Qt's 'ReadSpans &QtPrivate::QIOOperationDataStorage::getReadSpans()':
      gives a type Python has no way to take yet.
    - Qt's 'const ReadSpans
      &QtPrivate::QIOOperationDataStorage::getReadSpans() const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QIOOperationDataStorage.getReadSpans' has no cute "
        "function yet. Qt's 'ReadSpans "
        "&QtPrivate::QIOOperationDataStorage::getReadSpans()': gives a type "
        "Python has no way to take yet. Qt's 'const ReadSpans "
        "&QtPrivate::QIOOperationDataStorage::getReadSpans() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def getValue(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::QIOOperationDataStorage::getValue': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.QIOOperationDataStorage.getValue' has no cute function "
        "yet. Qt's 'QtPrivate::QIOOperationDataStorage::getValue': a "
        "template: a pattern and no single function.")

  @staticmethod
  def getWriteSpans(*__, **_) -> Never:
    """
    - Qt's 'WriteSpans &QtPrivate::QIOOperationDataStorage::getWriteSpans()':
      gives a type Python has no way to take yet.
    - Qt's 'const WriteSpans
      &QtPrivate::QIOOperationDataStorage::getWriteSpans() const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QIOOperationDataStorage.getWriteSpans' has no cute "
        "function yet. Qt's 'WriteSpans "
        "&QtPrivate::QIOOperationDataStorage::getWriteSpans()': gives a "
        "type Python has no way to take yet. Qt's 'const WriteSpans "
        "&QtPrivate::QIOOperationDataStorage::getWriteSpans() const': gives "
        "a type Python has no way to take yet.")
