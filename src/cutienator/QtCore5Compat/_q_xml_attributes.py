"""
QXmlAttributes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class QXmlAttributes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlAttributes: a plain Python object standing in
  front of one C++ QXmlAttributes.

  C++ hands a QXmlAttributes around as a copy, so every C++ QXmlAttributes
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlAttributes that has a ritual and that Python can
  call so far, 10 names in all: 'index', 'length', 'count', 'localName',
  'qName', 'uri', 'type', 'value', 'clear', 'append'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlAttributes::QXmlAttributes(QXmlAttributes &&a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QXmlAttributes &QXmlAttributes::operator=(const QXmlAttributes
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QXmlAttributes &QXmlAttributes::operator=(QXmlAttributes &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QXmlAttributes::~QXmlAttributes()': the destructor: Python removes
    its C++ QXmlAttributes by it, and has no other use for it.
  - Qt's 'void QXmlAttributes::swap(QXmlAttributes &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QXmlAttributes is created at the first use, not by
    'QXmlAttributes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlAttributes back gives a copy the ritual made for
    Python, in a new cute QXmlAttributes.
  - Each name of Qt's QXmlAttributes that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlAttributes'

  #  Qt's '~QXmlAttributes()'. Naming it makes this a value class: Python
  #  owns every C++ QXmlAttributes behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QXmlAttributesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def index(self, qName: str) -> int:
    """
    Calls Qt's 'int QXmlAttributes::index(const QString &qName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#index

    Parameters
    ----------

    qName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QXmlAttributes::index(const QString &qName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5indexERK7QString', qName,
    )

  @overload(QLatin1String)
  def index(self, qName: QLatin1String) -> int:
    """
    Calls Qt's 'int QXmlAttributes::index(QLatin1String qName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#index

    Parameters
    ----------

    qName : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  int QXmlAttributes::index(QLatin1String qName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5indexE13QLatin1String',
        self._valueOf(qName),
    )

  @overload(str, str)
  def index(self, uri: str, localPart: str) -> int:
    """
    Calls Qt's 'int QXmlAttributes::index(const QString &uri, const QString
    &localPart) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#index

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    localPart : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QXmlAttributes::index(const QString &uri, const QString
    #      &localPart) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5indexERK7QStringS2_', uri, localPart,
    )

  def length(self) -> int:
    """
    Calls Qt's 'int QXmlAttributes::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#length
    """
    #  int QXmlAttributes::length() const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes6lengthEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QXmlAttributes::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#count
    """
    #  int QXmlAttributes::count() const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes5countEv')

  @overload(int)
  def localName(self, index: int) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::localName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#localName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::localName(int index) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes9localNameEi', index,
    )

  @overload(int)
  def qName(self, index: int) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::qName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#qName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::qName(int index) const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes5qNameEi', index)

  @overload(int)
  def uri(self, index: int) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::uri(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#uri

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::uri(int index) const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes3uriEi', index)

  @overload(int)
  def type(self, index: int) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::type(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#type

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::type(int index) const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes4typeEi', index)

  @overload(str)
  def type(self, qName: str) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::type(const QString &qName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#type

    Parameters
    ----------

    qName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::type(const QString &qName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes4typeERK7QString', qName,
    )

  @overload(str, str)
  def type(self, uri: str, localName: str) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::type(const QString &uri, const
    QString &localName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#type

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::type(const QString &uri, const QString
    #      &localName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes4typeERK7QStringS2_', uri, localName,
    )

  @overload(int)
  def value(self, index: int) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::value(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::value(int index) const
    return self.uglySide.call('ritual_ZNK14QXmlAttributes5valueEi', index)

  @overload(str)
  def value(self, qName: str) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::value(const QString &qName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#value

    Parameters
    ----------

    qName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::value(const QString &qName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5valueERK7QString', qName,
    )

  @overload(QLatin1String)
  def value(self, qName: QLatin1String) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::value(QLatin1String qName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#value

    Parameters
    ----------

    qName : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::value(QLatin1String qName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5valueE13QLatin1String',
        self._valueOf(qName),
    )

  @overload(str, str)
  def value(self, uri: str, localName: str) -> str:
    """
    Calls Qt's 'QString QXmlAttributes::value(const QString &uri, const
    QString &localName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#value

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlAttributes::value(const QString &uri, const QString
    #      &localName) const
    return self.uglySide.call(
        'ritual_ZNK14QXmlAttributes5valueERK7QStringS2_', uri, localName,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QXmlAttributes::QXmlAttributes()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#QXmlAttributes
    """
    #  QXmlAttributes::QXmlAttributes()
    self._noteCreation(QXmlAttributes, lambda: Rituals.call(
        'ritual_ZN14QXmlAttributesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QXmlAttributes) -> None:
    """
    Notes what was given, for Qt's 'QXmlAttributes::QXmlAttributes(const
    QXmlAttributes &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#QXmlAttributes

    Parameters
    ----------

    a0 : QXmlAttributes
      Passed on as a value: Qt reads the C++ QXmlAttributes, which stays
      Python's own.
    """
    #  QXmlAttributes::QXmlAttributes(const QXmlAttributes &a0)
    self._noteCreation(QXmlAttributes, lambda: Rituals.call(
        'ritual_ZN14QXmlAttributesC1ERKS_', self._valueOf(a0),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QXmlAttributes::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#clear
    """
    #  void QXmlAttributes::clear()
    self.uglySide.call('ritual_ZN14QXmlAttributes5clearEv')

  @overload(str, str, str, str)
  def append(self, qName: str, uri: str, localPart: str, value: str) -> None:
    """
    Calls Qt's 'void QXmlAttributes::append(const QString &qName, const
    QString &uri, const QString &localPart, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlattributes.html#append

    Parameters
    ----------

    qName : str
      Passed on as it is: a QString is made of it for the call.

    uri : str
      Passed on as it is: a QString is made of it for the call.

    localPart : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlAttributes::append(const QString &qName, const QString &uri,
    #      const QString &localPart, const QString &value)
    self.uglySide.call(
        'ritual_ZN14QXmlAttributes6appendERK7QStringS2_S2_S2_',
        qName, uri, localPart, value,
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QXmlAttributes::swap(QXmlAttributes &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXmlAttributes.swap' has no cute function yet. Qt's 'void "
        "QXmlAttributes::swap(QXmlAttributes &other)': takes a type Python "
        "has no way to hand over yet.")
