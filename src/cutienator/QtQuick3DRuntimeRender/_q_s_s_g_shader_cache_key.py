"""
QSSGShaderCacheKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderCacheKey to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QSSGShaderFeatures
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGShaderFeatures = WAIT['QSSGShaderFeatures']


class QSSGShaderCacheKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderCacheKey: a plain Python object standing in
  front of one C++ QSSGShaderCacheKey.

  C++ hands a QSSGShaderCacheKey around as a copy, so every C++
  QSSGShaderCacheKey behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderCacheKey that has a ritual and that Python
  can call so far, 3 names in all: 'generateHashCode', 'updateHashCode',
  '__eq__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderCacheKey &QSSGShaderCacheKey::operator=(const
    QSSGShaderCacheKey &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QSSGShaderCacheKey::~QSSGShaderCacheKey()': the destructor: Python
    removes its C++ QSSGShaderCacheKey by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderCacheKey is created at the first use, not by
    'QSSGShaderCacheKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderCacheKey back gives a copy the ritual made
    for Python, in a new cute QSSGShaderCacheKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray, QSSGShaderFeatures)
  def generateHashCode(key: QByteArray, features: QSSGShaderFeatures) -> int:
    """
    Calls Qt's 'size_t QSSGShaderCacheKey::generateHashCode(const QByteArray
    &key, QSSGShaderFeatures features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercachekey.html#generateHashCode

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    features : QSSGShaderFeatures
      Passed on as a value: Qt reads the C++ QSSGShaderFeatures, which stays
      Python's own.
    """
    #  size_t QSSGShaderCacheKey::generateHashCode(const QByteArray &key,
    #      QSSGShaderFeatures features)
    return Rituals.call(
        'ritual_ZN18QSSGShaderCacheKey16generateHashCodeERK10QByteArray18QS'
        'SGShaderFeatures',
        CuteMixin._valueOf(key), CuteMixin._valueOf(features),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderCacheKey'

  #  Qt's '~QSSGShaderCacheKey()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGShaderCacheKey behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGShaderCacheKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __eq__(self, inOther: QSSGShaderCacheKey) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCacheKey::operator==(const QSSGShaderCacheKey
    &inOther) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshadercachekey.html#operator==

    Parameters
    ----------

    inOther : QSSGShaderCacheKey
      Passed on as a value: Qt reads the C++ QSSGShaderCacheKey, which stays
      Python's own.
    """
    #  bool QSSGShaderCacheKey::operator==(const QSSGShaderCacheKey &inOther)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QSSGShaderCacheKeyeqERKS_', self._valueOf(inOther),
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
  @overload(QByteArray)
  def __init__(self, key: Optional[QByteArray] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderCacheKey::QSSGShaderCacheKey(const QByteArray &key)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercachekey.html#QSSGShaderCacheKey

    Parameters
    ----------

    key : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QSSGShaderCacheKey::QSSGShaderCacheKey(const QByteArray &key)
    if key is None:
      from ..QtCore import QByteArray
      key = QByteArray()
    self._noteCreation(QSSGShaderCacheKey, lambda: Rituals.call(
        'ritual_ZN18QSSGShaderCacheKeyC1ERK10QByteArray', self._valueOf(key),
    ))

  @overload(THIS)
  def __init__(self, other: QSSGShaderCacheKey) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderCacheKey::QSSGShaderCacheKey(const QSSGShaderCacheKey
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercachekey.html#QSSGShaderCacheKey

    Parameters
    ----------

    other : QSSGShaderCacheKey
      Passed on as a value: Qt reads the C++ QSSGShaderCacheKey, which stays
      Python's own.
    """
    #  QSSGShaderCacheKey::QSSGShaderCacheKey(const QSSGShaderCacheKey
    #      &other)
    self._noteCreation(QSSGShaderCacheKey, lambda: Rituals.call(
        'ritual_ZN18QSSGShaderCacheKeyC1ERKS_', self._valueOf(other),
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

  def updateHashCode(self) -> None:
    """
    Calls Qt's 'void QSSGShaderCacheKey::updateHashCode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercachekey.html#updateHashCode
    """
    #  void QSSGShaderCacheKey::updateHashCode()
    self.uglySide.call('ritual_ZN18QSSGShaderCacheKey14updateHashCodeEv')
