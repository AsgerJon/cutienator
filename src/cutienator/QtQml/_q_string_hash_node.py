"""
QStringHashNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStringHashNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QHashedCStringRef, QHashedString, QHashedStringRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedCStringRef = WAIT['QHashedCStringRef']
  QHashedString = WAIT['QHashedString']
  QHashedStringRef = WAIT['QHashedStringRef']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringHashNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringHashNode: a plain Python object standing in
  front of one C++ QStringHashNode.

  C++ hands a QStringHashNode around as a copy, so every C++ QStringHashNode
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringHashNode that has a ritual and that Python
  can call so far, 6 names in all: 'key', 'isQString', 'setQString', 'size',
  'cStrData', 'equals'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStringHashNode::~QStringHashNode()': the destructor: Python
    removes its C++ QStringHashNode by it, and has no other use for it.
  - Qt's 'const char16_t *QStringHashNode::utf16Data() const': gives
    'unsigned short', which has no cute class yet.

  What to expect
  --------------

  - The C++ QStringHashNode is created at the first use, not by
    'QStringHashNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringHashNode back gives a copy the ritual made for
    Python, in a new cute QStringHashNode.
  - Each name of Qt's QStringHashNode that has no cute function yet,
    'utf16Data', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QStringHashNode, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Tag(CuteNum):
    """
    The enum 'QStringHashNode::Tag' of Qt, with the 2 names Qt gives in it.
    """

    NodeIsCString = Kee[int](0)
    NodeIsQString = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringHashNode'

  #  Qt's '~QStringHashNode()'. Naming it makes this a value class: Python
  #  owns every C++ QStringHashNode behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStringHashNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> QHashedString:
    """
    Calls Qt's 'QHashedString QStringHashNode::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#key

    Returns
    -------

    QHashedString
      A new cute QHashedString around the copy Qt gave back. Python owns it.
    """
    #  QHashedString QStringHashNode::key() const
    address = self.uglySide.call('ritual_ZNK15QStringHashNode3keyEv')
    from . import QHashedString
    return QHashedString._cuteOwning(address)

  def isQString(self) -> bool:
    """
    Calls Qt's 'bool QStringHashNode::isQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#isQString
    """
    #  bool QStringHashNode::isQString() const
    return self.uglySide.call('ritual_ZNK15QStringHashNode9isQStringEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QStringHashNode::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#size
    """
    #  qsizetype QStringHashNode::size() const
    return self.uglySide.call('ritual_ZNK15QStringHashNode4sizeEv')

  def cStrData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QStringHashNode::cStrData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#cStrData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QStringHashNode::cStrData() const
    chars = self.uglySide.call('ritual_ZNK15QStringHashNode8cStrDataEv')
    return None if chars is None else chars.decode()

  @overload(WAIT['QV4.Value'])
  def equals(self, string: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QStringHashNode::equals(const QV4::Value &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#equals

    Parameters
    ----------

    string : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QStringHashNode::equals(const QV4::Value &string) const
    return self.uglySide.call(
        'ritual_ZNK15QStringHashNode6equalsERKN3QV45ValueE',
        self._valueOf(string),
    )

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def equals(self, string: Optional[QV4.String]) -> bool:
    """
    Calls Qt's 'bool QStringHashNode::equals(const QV4::String *string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#equals

    Parameters
    ----------

    string : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStringHashNode::equals(const QV4::String *string) const
    return self.uglySide.call(
        'ritual_ZNK15QStringHashNode6equalsEPKN3QV46StringE',
        self._addressOf(string),
    )

  @overload(QHashedStringRef)
  def equals(self, string: QHashedStringRef) -> bool:
    """
    Calls Qt's 'bool QStringHashNode::equals(const QHashedStringRef &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#equals

    Parameters
    ----------

    string : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.
    """
    #  bool QStringHashNode::equals(const QHashedStringRef &string) const
    return self.uglySide.call(
        'ritual_ZNK15QStringHashNode6equalsERK16QHashedStringRef',
        self._valueOf(string),
    )

  @overload(QHashedCStringRef)
  def equals(self, string: QHashedCStringRef) -> bool:
    """
    Calls Qt's 'bool QStringHashNode::equals(const QHashedCStringRef &string)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#equals

    Parameters
    ----------

    string : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.
    """
    #  bool QStringHashNode::equals(const QHashedCStringRef &string) const
    return self.uglySide.call(
        'ritual_ZNK15QStringHashNode6equalsERK17QHashedCStringRef',
        self._valueOf(string),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setQString(self, v: bool) -> None:
    """
    Calls Qt's 'void QStringHashNode::setQString(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashnode.html#setQString

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QStringHashNode::setQString(bool v)
    self.uglySide.call('ritual_ZN15QStringHashNode10setQStringEb', v)

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
    Notes what was given, for Qt's 'QStringHashNode::QStringHashNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringhashnode.html#QStringHashNode
    """
    #  QStringHashNode::QStringHashNode()
    self._noteCreation(QStringHashNode, lambda: Rituals.call(
        'ritual_ZN15QStringHashNodeC1Ev',
    ))

  @overload(QHashedString)
  def __init__(self, key: QHashedString) -> None:
    """
    Notes what was given, for Qt's 'QStringHashNode::QStringHashNode(const
    QHashedString &key)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringhashnode.html#QStringHashNode

    Parameters
    ----------

    key : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.
    """
    #  QStringHashNode::QStringHashNode(const QHashedString &key)
    self._noteCreation(QStringHashNode, lambda: Rituals.call(
        'ritual_ZN15QStringHashNodeC1ERK13QHashedString', self._valueOf(key),
    ))

  @overload(QHashedCStringRef)
  def __init__(self, key: QHashedCStringRef) -> None:
    """
    Notes what was given, for Qt's 'QStringHashNode::QStringHashNode(const
    QHashedCStringRef &key)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringhashnode.html#QStringHashNode

    Parameters
    ----------

    key : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.
    """
    #  QStringHashNode::QStringHashNode(const QHashedCStringRef &key)
    self._noteCreation(QStringHashNode, lambda: Rituals.call(
        'ritual_ZN15QStringHashNodeC1ERK17QHashedCStringRef',
        self._valueOf(key),
    ))

  @overload(THIS)
  def __init__(self, o: QStringHashNode) -> None:
    """
    Notes what was given, for Qt's 'QStringHashNode::QStringHashNode(const
    QStringHashNode &o)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringhashnode.html#QStringHashNode

    Parameters
    ----------

    o : QStringHashNode
      Passed on as a value: Qt reads the C++ QStringHashNode, which stays
      Python's own.
    """
    #  QStringHashNode::QStringHashNode(const QStringHashNode &o)
    self._noteCreation(QStringHashNode, lambda: Rituals.call(
        'ritual_ZN15QStringHashNodeC1ERKS_', self._valueOf(o),
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
  def utf16Data(*__, **_) -> Never:
    """
    Qt's 'const char16_t *QStringHashNode::utf16Data() const': gives
    'unsigned short', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringHashNode.utf16Data' has no cute function yet. Qt's 'const "
        "char16_t *QStringHashNode::utf16Data() const': gives 'unsigned "
        "short', which has no cute class yet.")
