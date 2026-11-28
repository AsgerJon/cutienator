"""
QtProtobufPrivate::QProtobufLazyMessagePointerBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobuflazymessagepointer.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QProtobufMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QProtobufMessage = WAIT['QProtobufMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufLazyMessagePointerBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtProtobufPrivate::QProtobufLazyMessagePointerBase: a
  plain Python object standing in front of one C++
  QtProtobufPrivate::QProtobufLazyMessagePointerBase.

  What exists
  -----------

  Every function of Qt's QtProtobufPrivate::QProtobufLazyMessagePointerBase
  that has a ritual and that Python can call so far, 3 names in all:
  'message', 'setMessage', '__bool__'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    QProtobufLazyMessagePointerBase(QProtobufLazyMessagePointerBase
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufLazyMessagePointerBase
    &QtProtobufPrivate::QProtobufLazyMessagePointerBase::operator=(
    QProtobufLazyMessagePointerBase &&other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    ~QProtobufLazyMessagePointerBase()': the destructor: Python never removes
    a C++ QtProtobufPrivate::QProtobufLazyMessagePointerBase.
  - Qt's 'void QtProtobufPrivate::QProtobufLazyMessagePointerBase::swap(
    QProtobufLazyMessagePointerBase &other)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QtProtobufPrivate::QProtobufLazyMessagePointerBase is created at
    the first use, not by
    'QtProtobufPrivate::QProtobufLazyMessagePointerBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtProtobufPrivate::QProtobufLazyMessagePointerBase.
  - Each name of Qt's QtProtobufPrivate::QProtobufLazyMessagePointerBase that
    has no cute function yet, 'swap', holds a function that raises
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
  __qt_class__ = 'QtProtobufPrivate::QProtobufLazyMessagePointerBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def message(self) -> Optional[QProtobufMessage]:
    """
    Calls Qt's 'QProtobufMessage
    *QtProtobufPrivate::QProtobufLazyMessagePointerBase::message() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuflazymessagepointerbase.html

    Returns
    -------

    Optional[QProtobufMessage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufMessage
    #      *QtProtobufPrivate::QProtobufLazyMessagePointerBase::message()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBase7mes'
        'sageEv',
    )
    from . import QProtobufMessage
    return QProtobufMessage._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QProtobufMessage)
  @overload(NoneType)
  def setMessage(self, msg: Optional[QProtobufMessage]) -> None:
    """
    Calls Qt's 'void
    QtProtobufPrivate::QProtobufLazyMessagePointerBase::setMessage(
    QProtobufMessage *msg) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuflazymessagepointerbase.html

    Parameters
    ----------

    msg : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtProtobufPrivate::QProtobufLazyMessagePointerBase::setMessage(
    #      QProtobufMessage *msg) const
    self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBase10se'
        'tMessageEP16QProtobufMessage',
        self._addressOf(msg),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool
    QtProtobufPrivate::QProtobufLazyMessagePointerBase::operator bool()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuflazymessagepointerbase.html
    """
    #  bool QtProtobufPrivate::QProtobufLazyMessagePointerBase::operator
    #      bool() const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBasecvbE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    QProtobufLazyMessagePointerBase()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuflazymessagepointerbase.html
    """
    #  QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    #      QProtobufLazyMessagePointerBase()
    self._noteCreation(QProtobufLazyMessagePointerBase, lambda: Rituals.call(
        'ritual_ZN17QtProtobufPrivate31QProtobufLazyMessagePointerBaseC1Ev',
    ))

  @overload(QProtobufMessage)
  @overload(NoneType)
  def __init__(self, ptr: Optional[QProtobufMessage]) -> None:
    """
    Notes what was given, for Qt's
    'QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    QProtobufLazyMessagePointerBase(QProtobufMessage *ptr)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuflazymessagepointerbase.html

    Parameters
    ----------

    ptr : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtProtobufPrivate::QProtobufLazyMessagePointerBase::
    #      QProtobufLazyMessagePointerBase(QProtobufMessage *ptr)
    self._noteCreation(QProtobufLazyMessagePointerBase, lambda: Rituals.call(
        'ritual_ZN17QtProtobufPrivate31QProtobufLazyMessagePointerBaseC1EP1'
        '6QProtobufMessage',
        self._addressOf(ptr),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtProtobufPrivate::QProtobufLazyMessagePointerBase::swap(
    QProtobufLazyMessagePointerBase &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufLazyMessagePointerBase.swap' has no "
        "cute function yet. Qt's 'void "
        "QtProtobufPrivate::QProtobufLazyMessagePointerBase::swap(QProtobufL"
        "azyMessagePointerBase &other)': takes a type Python has no way to "
        "hand over yet.")
