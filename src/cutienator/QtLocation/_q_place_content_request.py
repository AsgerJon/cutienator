"""
QPlaceContentRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacecontentrequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPlaceContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QPlaceContentRequestPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QPlaceContentRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceContentRequest: a plain Python object standing
  in front of one C++ QPlaceContentRequest.

  C++ hands a QPlaceContentRequest around as a copy, so every C++
  QPlaceContentRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceContentRequest that has a ritual and that
  Python can call so far, 13 names in all: '__eq__', '__ne__', 'contentType',
  'setContentType', 'placeId', 'setPlaceId', 'contentContext',
  'setContentContext', 'limit', 'setLimit', 'clear', 'isEqual', 'd_func'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceContentRequest::QPlaceContentRequest(QPlaceContentRequest
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QPlaceContentRequest::~QPlaceContentRequest()': the destructor:
    Python removes its C++ QPlaceContentRequest by it, and has no other use
    for it.
  - Qt's 'QPlaceContentRequest &QPlaceContentRequest::operator=(const
    QPlaceContentRequest &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QPlaceContentRequest
    &QPlaceContentRequest::operator=(QPlaceContentRequest &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceContentRequest::swap(QPlaceContentRequest &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QPlaceContentRequestPrivate *QPlaceContentRequest::d_func()
    const': takes in Python what 'QPlaceContentRequestPrivate
    *QPlaceContentRequest::d_func()' takes.

  What to expect
  --------------

  - The C++ QPlaceContentRequest is created at the first use, not by
    'QPlaceContentRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceContentRequest back gives a copy the ritual
    made for Python, in a new cute QPlaceContentRequest.
  - Each name of Qt's QPlaceContentRequest that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QPlaceContentRequest'

  #  Qt's '~QPlaceContentRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceContentRequest behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPlaceContentRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentType(self) -> QPlaceContent.Type:
    """
    Calls Qt's 'QPlaceContent::Type QPlaceContentRequest::contentType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#contentType

    Returns
    -------

    QPlaceContent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlaceContent.Type(number)' gives.
    """
    #  QPlaceContent::Type QPlaceContentRequest::contentType() const
    return QPlaceContent.Type(self.uglySide.call(
        'ritual_ZNK20QPlaceContentRequest11contentTypeEv',
    ))

  def placeId(self) -> str:
    """
    Calls Qt's 'QString QPlaceContentRequest::placeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#placeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceContentRequest::placeId() const
    return self.uglySide.call('ritual_ZNK20QPlaceContentRequest7placeIdEv')

  def contentContext(self) -> QVariant:
    """
    Calls Qt's 'QVariant QPlaceContentRequest::contentContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#contentContext

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlaceContentRequest::contentContext() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlaceContentRequest14contentContextEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def limit(self) -> int:
    """
    Calls Qt's 'int QPlaceContentRequest::limit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#limit
    """
    #  int QPlaceContentRequest::limit() const
    return self.uglySide.call('ritual_ZNK20QPlaceContentRequest5limitEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceContentRequest) -> bool:
    """
    Calls Qt's 'bool QPlaceContentRequest::isEqual(const QPlaceContentRequest
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#isEqual

    Parameters
    ----------

    other : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  bool QPlaceContentRequest::isEqual(const QPlaceContentRequest &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QPlaceContentRequest7isEqualERKS_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlaceContent.Type)
  def setContentType(self, type: QPlaceContent.Type) -> None:
    """
    Calls Qt's 'void QPlaceContentRequest::setContentType(QPlaceContent::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#setContentType

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.
    """
    #  void QPlaceContentRequest::setContentType(QPlaceContent::Type type)
    self.uglySide.call(
        'ritual_ZN20QPlaceContentRequest14setContentTypeEN13QPlaceContent4T'
        'ypeE',
        type.value,
    )

  @overload(str)
  def setPlaceId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlaceContentRequest::setPlaceId(const QString
    &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#setPlaceId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceContentRequest::setPlaceId(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN20QPlaceContentRequest10setPlaceIdERK7QString', identifier,
    )

  @overload(QVariant)
  def setContentContext(self, context: QVariant) -> None:
    """
    Calls Qt's 'void QPlaceContentRequest::setContentContext(const QVariant
    &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#setContentContext

    Parameters
    ----------

    context : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPlaceContentRequest::setContentContext(const QVariant &context)
    self.uglySide.call(
        'ritual_ZN20QPlaceContentRequest17setContentContextERK8QVariant',
        self._valueOf(context),
    )

  @overload(int)
  def setLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QPlaceContentRequest::setLimit(int limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#setLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QPlaceContentRequest::setLimit(int limit)
    self.uglySide.call('ritual_ZN20QPlaceContentRequest8setLimitEi', limit)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceContentRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceContentRequest &lhs, const
    QPlaceContentRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#operator==

    Parameters
    ----------

    rhs : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  bool operator==(const QPlaceContentRequest &lhs, const
    #      QPlaceContentRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QPlaceContentRequestS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QPlaceContentRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceContentRequest &lhs, const
    QPlaceContentRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#operator!=

    Parameters
    ----------

    rhs : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  bool operator!=(const QPlaceContentRequest &lhs, const
    #      QPlaceContentRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK20QPlaceContentRequestS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'QPlaceContentRequest::QPlaceContentRequest()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#QPlaceContentRequest
    """
    #  QPlaceContentRequest::QPlaceContentRequest()
    self._noteCreation(QPlaceContentRequest, lambda: Rituals.call(
        'ritual_ZN20QPlaceContentRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceContentRequest) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceContentRequest::QPlaceContentRequest(const QPlaceContentRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentrequest.html#QPlaceContentRequest

    Parameters
    ----------

    other : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.
    """
    #  QPlaceContentRequest::QPlaceContentRequest(const QPlaceContentRequest
    #      &other)
    self._noteCreation(QPlaceContentRequest, lambda: Rituals.call(
        'ritual_ZN20QPlaceContentRequestC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QPlaceContentRequest::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#clear
    """
    #  void QPlaceContentRequest::clear()
    self.uglySide.call('ritual_ZN20QPlaceContentRequest5clearEv')

  def d_func(self) -> Optional[QPlaceContentRequestPrivate]:
    """
    Calls Qt's 'QPlaceContentRequestPrivate *QPlaceContentRequest::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentrequest.html#d_func

    Returns
    -------

    Optional[QPlaceContentRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceContentRequestPrivate *QPlaceContentRequest::d_func()
    address = self.uglySide.call('ritual_ZN20QPlaceContentRequest6d_funcEv')
    from . import QPlaceContentRequestPrivate
    return QPlaceContentRequestPrivate._cuteAt(address)

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceContentRequest::swap(QPlaceContentRequest &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceContentRequest.swap' has no cute function yet. Qt's 'void "
        "QPlaceContentRequest::swap(QPlaceContentRequest &other)': takes a "
        "type Python has no way to hand over yet.")
