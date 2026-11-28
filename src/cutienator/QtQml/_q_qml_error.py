"""
QQmlError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlerror.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlError: a plain Python object standing in front of
  one C++ QQmlError.

  C++ hands a QQmlError around as a copy, so every C++ QQmlError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlError that has a ritual and that Python can call
  so far, 13 names in all: 'isValid', 'url', 'setUrl', 'description',
  'setDescription', 'line', 'setLine', 'column', 'setColumn', 'object',
  'setObject', 'toString', '__eq__'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlError::QQmlError(QQmlError &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QQmlError &QQmlError::operator=(const QQmlError &a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlError &QQmlError::operator=(QQmlError &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlError::~QQmlError()': the destructor: Python removes its C++
    QQmlError by it, and has no other use for it.
  - Qt's 'void QQmlError::swap(QQmlError &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QtMsgType QQmlError::messageType() const': gives the enum
    'QtMsgType', whose class cannot be named here.
  - Qt's 'void QQmlError::setMessageType(QtMsgType messageType)': names the
    enum 'QtMsgType', whose class cannot be named here.

  What to expect
  --------------

  - The C++ QQmlError is created at the first use, not by 'QQmlError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlError back gives a copy the ritual made for
    Python, in a new cute QQmlError.
  - Each name of Qt's QQmlError that has no cute function yet, 'messageType',
    'setMessageType', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlError'

  #  Qt's '~QQmlError()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QQmlErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlError::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#isValid
    """
    #  bool QQmlError::isValid() const
    return self.uglySide.call('ritual_ZNK9QQmlError7isValidEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlError::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlError::url() const
    address = self.uglySide.call('ritual_ZNK9QQmlError3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def description(self) -> str:
    """
    Calls Qt's 'QString QQmlError::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlError::description() const
    return self.uglySide.call('ritual_ZNK9QQmlError11descriptionEv')

  def line(self) -> int:
    """
    Calls Qt's 'int QQmlError::line() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#line
    """
    #  int QQmlError::line() const
    return self.uglySide.call('ritual_ZNK9QQmlError4lineEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlError::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#column
    """
    #  int QQmlError::column() const
    return self.uglySide.call('ritual_ZNK9QQmlError6columnEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlError::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlError::object() const
    address = self.uglySide.call('ritual_ZNK9QQmlError6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlError::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlError::toString() const
    return self.uglySide.call('ritual_ZNK9QQmlError8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQmlError::setUrl(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#setUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlError::setUrl(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN9QQmlError6setUrlERK4QUrl', self._valueOf(a0),
    )

  @overload(str)
  def setDescription(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlError::setDescription(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#setDescription

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlError::setDescription(const QString &a0)
    self.uglySide.call('ritual_ZN9QQmlError14setDescriptionERK7QString', a0)

  @overload(int)
  def setLine(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlError::setLine(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#setLine

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlError::setLine(int a0)
    self.uglySide.call('ritual_ZN9QQmlError7setLineEi', a0)

  @overload(int)
  def setColumn(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlError::setColumn(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#setColumn

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlError::setColumn(int a0)
    self.uglySide.call('ritual_ZN9QQmlError9setColumnEi', a0)

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlError::setObject(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#setObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlError::setObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN9QQmlError9setObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlError) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlError &a, const QQmlError &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#operator==

    Parameters
    ----------

    b : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  bool operator==(const QQmlError &a, const QQmlError &b)
    return Rituals.call(
        'ritual_ZeqRK9QQmlErrorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    Notes what was given, for Qt's 'QQmlError::QQmlError()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#QQmlError
    """
    #  QQmlError::QQmlError()
    self._noteCreation(QQmlError, lambda: Rituals.call(
        'ritual_ZN9QQmlErrorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlError) -> None:
    """
    Notes what was given, for Qt's 'QQmlError::QQmlError(const QQmlError
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlerror.html#QQmlError

    Parameters
    ----------

    a0 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  QQmlError::QQmlError(const QQmlError &a0)
    self._noteCreation(QQmlError, lambda: Rituals.call(
        'ritual_ZN9QQmlErrorC1ERKS_', self._valueOf(a0),
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
  def messageType(*__, **_) -> Never:
    """
    Qt's 'QtMsgType QQmlError::messageType() const': gives the enum
    'QtMsgType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlError.messageType' has no cute function yet. Qt's 'QtMsgType "
        "QQmlError::messageType() const': gives the enum 'QtMsgType', whose "
        "class cannot be named here.")

  @staticmethod
  def setMessageType(*__, **_) -> Never:
    """
    Qt's 'void QQmlError::setMessageType(QtMsgType messageType)': names the
    enum 'QtMsgType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlError.setMessageType' has no cute function yet. Qt's 'void "
        "QQmlError::setMessageType(QtMsgType messageType)': names the enum "
        "'QtMsgType', whose class cannot be named here.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QQmlError::swap(QQmlError &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlError.swap' has no cute function yet. Qt's 'void "
        "QQmlError::swap(QQmlError &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QQmlError>': the list of QQmlError, which 'QList[QQmlError]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QQmlError.
QList.createKind(
    QQmlError, 'value',
    make='ritual_list_make_QQmlError',
    add='ritual_list_add_QQmlError',
    size='ritual_list_size_QQmlError',
    at='ritual_list_at_QQmlError',
    drop='ritual_list_drop_QQmlError',
)
