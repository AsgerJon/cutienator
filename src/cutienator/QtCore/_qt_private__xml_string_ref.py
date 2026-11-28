"""
QtPrivate::XmlStringRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtPrivate::XmlStringRef to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class XmlStringRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::XmlStringRef: a plain Python object
  standing in front of one C++ QtPrivate::XmlStringRef.

  C++ hands a QtPrivate::XmlStringRef around as a copy, so every C++
  QtPrivate::XmlStringRef behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::XmlStringRef that has a ritual and that
  Python can call so far, 15 names in all: 'clear', 'view', 'isEmpty',
  'isNull', 'toString', 'sliced', 'size', 'empty', '__eq__', '__ne__',
  '__le__', '__ge__', '__lt__', '__gt__', 'verify'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlString QtPrivate::XmlStringRef::operator QXmlString() const':
    an operator Python has no name for.
  - Qt's 'const_pointer QtPrivate::XmlStringRef::data() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_iterator QtPrivate::XmlStringRef::begin() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_iterator QtPrivate::XmlStringRef::end() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_iterator QtPrivate::XmlStringRef::cbegin() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_iterator QtPrivate::XmlStringRef::cend() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::rbegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::rend() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::crbegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::crend() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool operator==(QStringView lhs, const XmlStringRef &rhs)': takes
    in Python what 'bool operator==(const XmlStringRef &lhs, QStringView
    rhs)' takes.
  - Qt's 'bool operator!=(QStringView lhs, const XmlStringRef &rhs)': takes
    in Python what 'bool operator!=(const XmlStringRef &lhs, QStringView
    rhs)' takes.
  - Qt's 'bool operator>=(const XmlStringRef &lhs, QStringView rhs)': takes
    in Python what 'bool operator<=(QStringView lhs, const XmlStringRef
    &rhs)' takes.
  - Qt's 'bool operator>=(QStringView lhs, const XmlStringRef &rhs)': takes
    in Python what 'bool operator<=(const XmlStringRef &lhs, QStringView
    rhs)' takes.
  - Qt's 'bool operator>(const XmlStringRef &lhs, QStringView rhs)': takes in
    Python what 'bool operator<(QStringView lhs, const XmlStringRef &rhs)'
    takes.
  - Qt's 'bool operator>(QStringView lhs, const XmlStringRef &rhs)': takes in
    Python what 'bool operator<(const XmlStringRef &lhs, QStringView rhs)'
    takes.
  - Qt's 'QtPrivate::XmlStringRef::~XmlStringRef()': the destructor: Python
    removes its C++ QtPrivate::XmlStringRef by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QtPrivate::XmlStringRef is created at the first use, not by
    'QtPrivate::XmlStringRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::XmlStringRef back gives a copy the ritual
    made for Python, in a new cute QtPrivate::XmlStringRef.
  - Each name of Qt's QtPrivate::XmlStringRef that has no cute function yet,
    'begin', 'cbegin', 'cend', 'crbegin', 'crend', 'data', 'end', 'rbegin',
    'rend', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::XmlStringRef'

  #  Qt's '~QtPrivate::XmlStringRef()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::XmlStringRef behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate12XmlStringRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def view(self) -> str:
    """
    Calls Qt's 'QStringView QtPrivate::XmlStringRef::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#view

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QtPrivate::XmlStringRef::view() const
    return self.uglySide.call('ritual_ZNK9QtPrivate12XmlStringRef4viewEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::XmlStringRef::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#isEmpty
    """
    #  bool QtPrivate::XmlStringRef::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QtPrivate12XmlStringRef7isEmptyEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::XmlStringRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#isNull
    """
    #  bool QtPrivate::XmlStringRef::isNull() const
    return self.uglySide.call('ritual_ZNK9QtPrivate12XmlStringRef6isNullEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QtPrivate::XmlStringRef::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtPrivate::XmlStringRef::toString() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate12XmlStringRef8toStringEv',
    )

  @overload(int)
  def sliced(self, pos: int) -> XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos) const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate12XmlStringRef6slicedEx', pos,
    )
    return XmlStringRef._cuteOwning(address)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos,
    qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QtPrivate::XmlStringRef::sliced(qsizetype pos, qsizetype
    #      n) const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate12XmlStringRef6slicedExx', pos, n,
    )
    return XmlStringRef._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QtPrivate::XmlStringRef::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#size
    """
    #  qsizetype QtPrivate::XmlStringRef::size() const
    return self.uglySide.call('ritual_ZNK9QtPrivate12XmlStringRef4sizeEv')

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::XmlStringRef::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#empty
    """
    #  bool QtPrivate::XmlStringRef::empty() const
    return self.uglySide.call('ritual_ZNK9QtPrivate12XmlStringRef5emptyEv')

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
  def __eq__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator==(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator==

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator==(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __eq__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator==(const XmlStringRef &lhs, QStringView rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator==

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator==(const XmlStringRef &lhs, QStringView rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_12XmlStringRefE11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator!=

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator!=(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __ne__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator!=(const XmlStringRef &lhs, QStringView rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator!=

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator!=(const XmlStringRef &lhs, QStringView rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_12XmlStringRefE11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator<=(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<=

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator<=(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateleERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __le__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator<=(const XmlStringRef &lhs, QStringView rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<=

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<=(const XmlStringRef &lhs, QStringView rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateleERKNS_12XmlStringRefE11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator>=(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator>=

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator>=(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivategeERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __ge__(self, lhs: str) -> bool:
    """
    Calls Qt's 'bool operator<=(QStringView lhs, const XmlStringRef &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<=

    Parameters
    ----------

    lhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<=(QStringView lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateleE11QStringViewRKNS_12XmlStringRefE',
        lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator<(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator<(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateltERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __lt__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator<(const XmlStringRef &lhs, QStringView rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<(const XmlStringRef &lhs, QStringView rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateltERKNS_12XmlStringRefE11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: XmlStringRef) -> bool:
    """
    Calls Qt's 'bool operator>(const XmlStringRef &lhs, const XmlStringRef
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator>

    Parameters
    ----------

    rhs : XmlStringRef
      Passed on as a value: Qt reads the C++ QtPrivate::XmlStringRef, which
      stays Python's own.
    """
    #  bool operator>(const XmlStringRef &lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivategtERKNS_12XmlStringRefES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __gt__(self, lhs: str) -> bool:
    """
    Calls Qt's 'bool operator<(QStringView lhs, const XmlStringRef &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#operator<

    Parameters
    ----------

    lhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<(QStringView lhs, const XmlStringRef &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateltE11QStringViewRKNS_12XmlStringRefE',
        lhs, CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QtPrivate::XmlStringRef::XmlStringRef()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#XmlStringRef
    """
    #  QtPrivate::XmlStringRef::XmlStringRef()
    self._noteCreation(XmlStringRef, lambda: Rituals.call(
        'ritual_ZN9QtPrivate12XmlStringRefC1Ev',
    ))

  @overload(QString, int, int)
  @overload(NoneType, int, int)
  def __init__(
      self,
      string: Optional[QString],
      pos: int,
      length: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::XmlStringRef::XmlStringRef(const QString *string, qsizetype
    pos, qsizetype length)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#XmlStringRef

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  QtPrivate::XmlStringRef::XmlStringRef(const QString *string, qsizetype
    #      pos, qsizetype length)
    self._noteCreation(XmlStringRef, lambda: Rituals.call(
        'ritual_ZN9QtPrivate12XmlStringRefC1EPK7QStringxx',
        self._addressOf(string), pos, length,
    ))

  @overload(QString)
  @overload(NoneType)
  def __init__(self, string: Optional[QString]) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::XmlStringRef::XmlStringRef(const QString *string)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#XmlStringRef

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtPrivate::XmlStringRef::XmlStringRef(const QString *string)
    self._noteCreation(XmlStringRef, lambda: Rituals.call(
        'ritual_ZN9QtPrivate12XmlStringRefC1EPK7QString',
        self._addressOf(string),
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
    Calls Qt's 'void QtPrivate::XmlStringRef::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#clear
    """
    #  void QtPrivate::XmlStringRef::clear()
    self.uglySide.call('ritual_ZN9QtPrivate12XmlStringRef5clearEv')

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QtPrivate::XmlStringRef::verify(qsizetype pos, qsizetype
    n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-xmlstringref.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QtPrivate::XmlStringRef::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate12XmlStringRef6verifyExx', pos, n,
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QtPrivate::XmlStringRef::begin() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.begin' has no cute function yet. Qt's "
        "'const_iterator QtPrivate::XmlStringRef::begin() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QtPrivate::XmlStringRef::cbegin() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.cbegin' has no cute function yet. Qt's "
        "'const_iterator QtPrivate::XmlStringRef::cbegin() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QtPrivate::XmlStringRef::cend() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.cend' has no cute function yet. Qt's "
        "'const_iterator QtPrivate::XmlStringRef::cend() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::crbegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QtPrivate::XmlStringRef::crbegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::crend() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QtPrivate::XmlStringRef::crend() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'const_pointer QtPrivate::XmlStringRef::data() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.data' has no cute function yet. Qt's "
        "'const_pointer QtPrivate::XmlStringRef::data() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QtPrivate::XmlStringRef::end() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.end' has no cute function yet. Qt's "
        "'const_iterator QtPrivate::XmlStringRef::end() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::rbegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QtPrivate::XmlStringRef::rbegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QtPrivate::XmlStringRef::rend() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.XmlStringRef.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator QtPrivate::XmlStringRef::rend() const': "
        "gives a type Python has no way to take yet.")
