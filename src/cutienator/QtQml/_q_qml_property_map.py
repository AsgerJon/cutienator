"""
QQmlPropertyMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlpropertymap.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyMap(QObject):
  """
  The cute side of Qt's QQmlPropertyMap: a plain Python object standing in
  front of one C++ QQmlPropertyMap.

  It is built on the cute 'QObject', as Qt's QQmlPropertyMap is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyMap that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'create', 'value',
  'insert', 'clear', 'freeze', 'keys', 'count', 'size', 'isEmpty',
  'contains', '__getitem__', 'valueChanged', 'updateValue'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlPropertyMap::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlPropertyMap::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlPropertyMap::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQmlPropertyMap::~QQmlPropertyMap()': the destructor: Python never
    removes a C++ QQmlPropertyMap.
  - Qt's 'QVariant &QQmlPropertyMap::operator[](const QString &key)': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlPropertyMapPrivate *QQmlPropertyMap::d_func()': gives
    'QQmlPropertyMapPrivate', which has no cute class yet.
  - Qt's 'const QQmlPropertyMapPrivate *QQmlPropertyMap::d_func() const':
    gives 'QQmlPropertyMapPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 30 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QQmlPropertyMap is created at the first use, not by
    'QQmlPropertyMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyMap.
  - Qt tells when it has removed the C++ QQmlPropertyMap. Every call on the
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
    Calls Qt's 'QString QQmlPropertyMap::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#tr

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
    #  QString QQmlPropertyMap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlPropertyMap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  @overload(QObject)
  @overload(NoneType)
  def create(parent: Optional[QObject] = None) -> Optional[QQmlPropertyMap]:
    """
    Calls Qt's 'QQmlPropertyMap *QQmlPropertyMap::create(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#create

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQmlPropertyMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyMap *QQmlPropertyMap::create(QObject *parent)
    address = Rituals.call(
        'ritual_ZN15QQmlPropertyMap6createEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QQmlPropertyMap._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyMap'

  #  A C++ QQmlPropertyMap Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlPropertyMap'

  #  The functions Qt calls itself that QQmlPropertyMap is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateValue': (
          ('_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPropertyMap::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPropertyMap::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlPropertyMap10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def value(self, key: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPropertyMap::value(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPropertyMap::value(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlPropertyMap5valueERK7QString', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlPropertyMap::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlPropertyMap::keys() const
    address = self.uglySide.call('ritual_ZNK15QQmlPropertyMap4keysEv')
    return QStringList._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyMap::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#count
    """
    #  int QQmlPropertyMap::count() const
    return self.uglySide.call('ritual_ZNK15QQmlPropertyMap5countEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyMap::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#size
    """
    #  int QQmlPropertyMap::size() const
    return self.uglySide.call('ritual_ZNK15QQmlPropertyMap4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyMap::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#isEmpty
    """
    #  bool QQmlPropertyMap::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QQmlPropertyMap7isEmptyEv')

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyMap::contains(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlPropertyMap::contains(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK15QQmlPropertyMap8containsERK7QString', key,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __getitem__(self, key: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPropertyMap::operator[](const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPropertyMap::operator[](const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlPropertyMapixERK7QString', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyMap::QQmlPropertyMap(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertymap.html#QQmlPropertyMap

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlPropertyMap::QQmlPropertyMap(QObject *parent)
    self._noteCreation(QQmlPropertyMap, lambda: Rituals.call(
        'ritual_ZN15QQmlPropertyMapC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QMetaObject, QObject)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      staticMetaObject: Optional[QMetaObject],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyMap::QQmlPropertyMap(const
    QMetaObject *staticMetaObject, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertymap.html#QQmlPropertyMap

    Parameters
    ----------

    staticMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlPropertyMap::QQmlPropertyMap(const QMetaObject *staticMetaObject,
    #      QObject *parent)
    self._noteCreation(QQmlPropertyMap, lambda: Rituals.call(
        'ritual_ZN15QQmlPropertyMapC1EPK11QMetaObjectP7QObject',
        self._addressOf(staticMetaObject, 'QMetaObject'),
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

  @overload(str, QVariant)
  def insert(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlPropertyMap::insert(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#insert

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlPropertyMap::insert(const QString &key, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QQmlPropertyMap6insertERK7QStringRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(QHash[str, QVariant])
  def insert(self, values: QHash[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQmlPropertyMap::insert(const QVariantHash &values)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#insert

    Parameters
    ----------

    values : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlPropertyMap::insert(const QVariantHash &values)
    self.uglySide.call(
        'ritual_ZN15QQmlPropertyMap6insertERK5QHashI7QString8QVariantE',
        self._valueOf(values),
    )

  @overload(str)
  def clear(self, key: str) -> None:
    """
    Calls Qt's 'void QQmlPropertyMap::clear(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#clear

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlPropertyMap::clear(const QString &key)
    self.uglySide.call('ritual_ZN15QQmlPropertyMap5clearERK7QString', key)

  def freeze(self) -> None:
    """
    Calls Qt's 'void QQmlPropertyMap::freeze()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#freeze
    """
    #  void QQmlPropertyMap::freeze()
    self.uglySide.call('ritual_ZN15QQmlPropertyMap6freezeEv')

  @overload(str, QVariant)
  def valueChanged(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlPropertyMap::valueChanged(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#valueChanged

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlPropertyMap::valueChanged(const QString &key, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QQmlPropertyMap12valueChangedERK7QStringRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(str, QVariant)
  def updateValue(self, key: str, input: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPropertyMap::updateValue(const QString &key,
    const QVariant &input)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertymap.html#updateValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    input : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPropertyMap::updateValue(const QString &key, const
    #      QVariant &input)
    ritual = 'ritual_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVarian'
          't')
    address = self.uglySide.call(ritual, key, self._valueOf(input))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
