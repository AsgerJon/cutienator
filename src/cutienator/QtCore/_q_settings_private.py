"""
QSettingsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSettingsPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QList, QObjectPrivate, QSettings, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSettingsGroup, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSettingsGroup = WAIT['QSettingsGroup']
  QVariant = WAIT['QVariant']


class QSettingsPrivate(QObjectPrivate):
  """
  The cute side of Qt's QSettingsPrivate: a plain Python object standing in
  front of one C++ QSettingsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QSettingsPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSettingsPrivate that has a ritual and that Python
  can call so far, 18 names in all: 'q_func', 'remove', 'set', 'children',
  'clear', 'sync', 'flush', 'isWritable', 'fileName', 'beginGroupOrArray',
  'setStatus', 'requestUpdate', 'update', 'variantListToStringList',
  'stringListToVariantList', 'variantToString', 'stringToVariant',
  'splitArgs'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSettings *QSettingsPrivate::q_func() const': takes in Python
    what 'QSettings *QSettingsPrivate::q_func()' takes.
  - Qt's 'QSettingsPrivate::~QSettingsPrivate()': the destructor: Python
    never removes a C++ QSettingsPrivate.
  - Qt's 'std::optional<QVariant> QSettingsPrivate::get(const QString &key)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QSettingsPrivate::processChild(QStringView key, ChildSpec
    spec, QStringList &result)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString
    &result)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  11 of the 34 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QSettingsPrivate; 2 the class is abstract, so C++ cannot make one, and the
  C++ class of ours does not fill in every function it leaves open; 2 cannot
  be called and cannot be called through the meta-object and cannot be
  copied.

  What to expect
  --------------

  - The C++ QSettingsPrivate is created at the first use, not by
    'QSettingsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSettingsPrivate.
  - Each name of Qt's QSettingsPrivate that has no cute function yet,
    '__init__', 'actualKey', 'create', 'iniEscapedKey', 'iniEscapedString',
    'iniEscapedStringList', 'iniUnescapedKey', 'iniUnescapedStringList',
    'normalizedKey', 'processChild', 'value', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSettingsPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ChildSpec(CuteNum):
    """
    The enum 'QSettingsPrivate::ChildSpec' of Qt, with the 3 names Qt gives
    in it.
    """

    AllKeys = Kee[int](0)
    ChildKeys = Kee[int](1)
    ChildGroups = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QList[QVariant])
  def variantListToStringList(l: QList[QVariant]) -> QStringList:
    """
    Calls Qt's 'QStringList QSettingsPrivate::variantListToStringList(const
    QVariantList &l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#variantListToStringList

    Parameters
    ----------

    l : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettingsPrivate::variantListToStringList(const
    #      QVariantList &l)
    address = Rituals.call(
        'ritual_ZN16QSettingsPrivate23variantListToStringListERK5QListI8QVa'
        'riantE',
        CuteMixin._valueOf(l),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def stringListToVariantList(l: QStringList) -> QVariant:
    """
    Calls Qt's 'QVariant QSettingsPrivate::stringListToVariantList(const
    QStringList &l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#stringListToVariantList

    Parameters
    ----------

    l : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSettingsPrivate::stringListToVariantList(const QStringList
    #      &l)
    address = Rituals.call(
        'ritual_ZN16QSettingsPrivate23stringListToVariantListERK5QListI7QSt'
        'ringE',
        CuteMixin._valueOf(l),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QVariant)
  def variantToString(v: QVariant) -> str:
    """
    Calls Qt's 'QString QSettingsPrivate::variantToString(const QVariant
    &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#variantToString

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettingsPrivate::variantToString(const QVariant &v)
    return Rituals.call(
        'ritual_ZN16QSettingsPrivate15variantToStringERK8QVariant',
        CuteMixin._valueOf(v),
    )

  @staticmethod
  @overload(str)
  def stringToVariant(s: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSettingsPrivate::stringToVariant(const QString
    &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#stringToVariant

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSettingsPrivate::stringToVariant(const QString &s)
    address = Rituals.call(
        'ritual_ZN16QSettingsPrivate15stringToVariantERK7QString', s,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(str, int)
  def splitArgs(s: str, idx: int) -> QStringList:
    """
    Calls Qt's 'QStringList QSettingsPrivate::splitArgs(const QString &s,
    qsizetype idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#splitArgs

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    idx : int
      Passed on as it is.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettingsPrivate::splitArgs(const QString &s, qsizetype
    #      idx)
    address = Rituals.call(
        'ritual_ZN16QSettingsPrivate9splitArgsERK7QStringx', s, idx,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSettingsPrivate'

  #  A C++ QSettingsPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSettingsPrivate'

  #  The functions Qt calls itself that QSettingsPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'get': (
          'std::optional<QVariant> QSettingsPrivate::get(const QString &) '
          'const',
      ),
      'children': (
          'QStringList QSettingsPrivate::children(const QString &, '
          'ChildSpec) const',
      ),
  }

  #  The functions Qt calls itself that QSettingsPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'remove': (
          ('_ZN16QSettingsPrivate6removeERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'set': (
          ('_ZN16QSettingsPrivate3setERK7QStringRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'clear': (
          ('_ZN16QSettingsPrivate5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'sync': (
          ('_ZN16QSettingsPrivate4syncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'flush': (
          ('_ZN16QSettingsPrivate5flushEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isWritable': (
          ('_ZNK16QSettingsPrivate10isWritableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fileName': (
          ('_ZNK16QSettingsPrivate8fileNameEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, ChildSpec)
  def children(self, prefix: str, spec: ChildSpec) -> QStringList:
    """
    Calls Qt's 'QStringList QSettingsPrivate::children(const QString &prefix,
    ChildSpec spec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#children

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    spec : ChildSpec
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSettingsPrivate::children(const QString &prefix,
    #      ChildSpec spec) const
    address = self.uglySide.call(
        'ritual_ZNK16QSettingsPrivate8childrenERK7QStringNS_9ChildSpecE',
        prefix, spec.value,
    )
    return QStringList._cuteOwning(address)

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QSettingsPrivate::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#isWritable
    """
    #  bool QSettingsPrivate::isWritable() const
    return self.uglySide.call('ritual_ZNK16QSettingsPrivate10isWritableEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QSettingsPrivate::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettingsPrivate::fileName() const
    return self.uglySide.call('ritual_ZNK16QSettingsPrivate8fileNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSettings.Status)
  def setStatus(self, status: QSettings.Status) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::setStatus(QSettings::Status status)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#setStatus

    Parameters
    ----------

    status : QSettings.Status
      Passed on as its number.
    """
    #  void QSettingsPrivate::setStatus(QSettings::Status status) const
    self.uglySide.call(
        'ritual_ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE',
        status.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QSettingsPrivate::QSettingsPrivate(QSettings::Format format)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    - Qt's 'QSettingsPrivate::QSettingsPrivate(QSettings::Format format,
      QSettings::Scope scope, const QString &organization, const QString
      &application)': the class is abstract, so C++ cannot make one, and the
      C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.__init__' has no cute function yet. Qt's "
        "'QSettingsPrivate::QSettingsPrivate(QSettings::Format format)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open. Qt's "
        "'QSettingsPrivate::QSettingsPrivate(QSettings::Format format, "
        "QSettings::Scope scope, const QString &organization, const QString "
        "&application)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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

  def q_func(self) -> Optional[QSettings]:
    """
    Calls Qt's 'QSettings *QSettingsPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#q_func

    Returns
    -------

    Optional[QSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSettings *QSettingsPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QSettingsPrivate6q_funcEv')
    return QSettings._cuteAt(address)

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSettingsPrivate::remove(const QString &key)
    self.uglySide.call('ritual_ZN16QSettingsPrivate6removeERK7QString', key)

  @overload(str, QVariant)
  def set(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::set(const QString &key, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#set

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSettingsPrivate::set(const QString &key, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN16QSettingsPrivate3setERK7QStringRK8QVariant',
        key, self._valueOf(value),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#clear
    """
    #  void QSettingsPrivate::clear()
    self.uglySide.call('ritual_ZN16QSettingsPrivate5clearEv')

  def sync(self) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#sync
    """
    #  void QSettingsPrivate::sync()
    self.uglySide.call('ritual_ZN16QSettingsPrivate4syncEv')

  def flush(self) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#flush
    """
    #  void QSettingsPrivate::flush()
    self.uglySide.call('ritual_ZN16QSettingsPrivate5flushEv')

  @overload(QSettingsGroup)
  def beginGroupOrArray(self, group: QSettingsGroup) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup
    &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#beginGroupOrArray

    Parameters
    ----------

    group : QSettingsGroup
      Passed on as a value: Qt reads the C++ QSettingsGroup, which stays
      Python's own.
    """
    #  void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup &group)
    self.uglySide.call(
        'ritual_ZN16QSettingsPrivate17beginGroupOrArrayERK14QSettingsGroup',
        self._valueOf(group),
    )

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsettingsprivate.html#requestUpdate
    """
    #  void QSettingsPrivate::requestUpdate()
    self.uglySide.call('ritual_ZN16QSettingsPrivate13requestUpdateEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QSettingsPrivate::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsprivate.html#update
    """
    #  void QSettingsPrivate::update()
    self.uglySide.call('ritual_ZN16QSettingsPrivate6updateEv')

  @staticmethod
  def actualKey(*__, **_) -> Never:
    """
    Qt's 'QString QSettingsPrivate::actualKey(QAnyStringView key) const':
    leans on 'QSettingsPrivate::normalizedKey(QAnyStringView)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.actualKey' has no cute function yet. Qt's "
        "'QString QSettingsPrivate::actualKey(QAnyStringView key) const': "
        "leans on 'QSettingsPrivate::normalizedKey(QAnyStringView)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'QSettingsPrivate *QSettingsPrivate::create(QSettings::Format
      format, QSettings::Scope scope, const QString &organization, const
      QString &application)': cannot be called and cannot be called through
      the meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    - Qt's 'QSettingsPrivate *QSettingsPrivate::create(const QString
      &fileName, QSettings::Format format)': cannot be called and cannot be
      called through the meta-object and cannot be copied: no header file has
      its code, Qt's source does not mark it or its class for use from
      outside Qt or writes it 'inline' or nowhere, and it is no signal, slot
      or invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.create' has no cute function yet. Qt's "
        "'QSettingsPrivate *QSettingsPrivate::create(QSettings::Format "
        "format, QSettings::Scope scope, const QString &organization, const "
        "QString &application)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's 'QSettingsPrivate "
        "*QSettingsPrivate::create(const QString &fileName, "
        "QSettings::Format format)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def iniEscapedKey(*__, **_) -> Never:
    """
    Qt's 'void QSettingsPrivate::iniEscapedKey(const QString &key, QByteArray
    &result)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isAsciiLetterOrNumber'; did you mean
    'QtMiscUtils::isAsciiLetterOrNumber'?.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.iniEscapedKey' has no cute function yet. Qt's "
        "'void QSettingsPrivate::iniEscapedKey(const QString &key, "
        "QByteArray &result)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isAsciiLetterOrNumber'; did you mean "
        "'QtMiscUtils::isAsciiLetterOrNumber'?.")

  @staticmethod
  def iniEscapedString(*__, **_) -> Never:
    """
    Qt's 'void QSettingsPrivate::iniEscapedString(const QString &str,
    QByteArray &result)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'isHexDigit'; did you mean 'QtMiscUtils::isHexDigit'?.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.iniEscapedString' has no cute function yet. Qt's "
        "'void QSettingsPrivate::iniEscapedString(const QString &str, "
        "QByteArray &result)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isHexDigit'; did you mean "
        "'QtMiscUtils::isHexDigit'?.")

  @staticmethod
  def iniEscapedStringList(*__, **_) -> Never:
    """
    Qt's 'void QSettingsPrivate::iniEscapedStringList(const QStringList
    &strs, QByteArray &result)': leans on
    'QSettingsPrivate::iniEscapedString(QString const&, QByteArray&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.iniEscapedStringList' has no cute function yet. "
        "Qt's 'void QSettingsPrivate::iniEscapedStringList(const "
        "QStringList &strs, QByteArray &result)': leans on "
        "'QSettingsPrivate::iniEscapedString(QString const&, QByteArray&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def iniUnescapedKey(*__, **_) -> Never:
    """
    Qt's 'bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString
    &result)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.iniUnescapedKey' has no cute function yet. Qt's "
        "'bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, "
        "QString &result)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def iniUnescapedStringList(*__, **_) -> Never:
    """
    Qt's 'bool QSettingsPrivate::iniUnescapedStringList(QByteArrayView str,
    QString &stringResult, QStringList &stringListResult)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'isHexDigit'; did you mean
    'QtMiscUtils::isHexDigit'?.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.iniUnescapedStringList' has no cute function "
        "yet. Qt's 'bool "
        "QSettingsPrivate::iniUnescapedStringList(QByteArrayView str, "
        "QString &stringResult, QStringList &stringListResult)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isHexDigit'; did you mean 'QtMiscUtils::isHexDigit'?.")

  @staticmethod
  def normalizedKey(*__, **_) -> Never:
    """
    Qt's 'QString QSettingsPrivate::normalizedKey(QAnyStringView key)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching function for call to 'write'.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.normalizedKey' has no cute function yet. Qt's "
        "'QString QSettingsPrivate::normalizedKey(QAnyStringView key)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: no matching function for call to "
        "'write'.")

  @staticmethod
  def processChild(*__, **_) -> Never:
    """
    Qt's 'void QSettingsPrivate::processChild(QStringView key, ChildSpec
    spec, QStringList &result)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.processChild' has no cute function yet. Qt's "
        "'void QSettingsPrivate::processChild(QStringView key, ChildSpec "
        "spec, QStringList &result)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QVariant QSettingsPrivate::value(QAnyStringView key, const QVariant
    *defaultValue) const': leans on
    'QSettingsPrivate::normalizedKey(QAnyStringView)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSettingsPrivate.value' has no cute function yet. Qt's 'QVariant "
        "QSettingsPrivate::value(QAnyStringView key, const QVariant "
        "*defaultValue) const': leans on "
        "'QSettingsPrivate::normalizedKey(QAnyStringView)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
