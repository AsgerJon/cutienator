"""
QGrpcInterceptorChain binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcinterceptorchain.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGrpcInterceptorChainPrivate


class QGrpcInterceptorChain(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcInterceptorChain: a plain Python object standing
  in front of one C++ QGrpcInterceptorChain.

  What exists
  -----------

  Every function of Qt's QGrpcInterceptorChain that has a ritual and that
  Python can call so far, 7 names in all: 'clear', 'size', 'isEmpty',
  'empty', 'hasHandlerFor', 'warnNullInterceptor', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcInterceptorChain::~QGrpcInterceptorChain()': the destructor:
    Python never removes a C++ QGrpcInterceptorChain.
  - Qt's 'QGrpcInterceptorChain::QGrpcInterceptorChain(QGrpcInterceptorChain
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcInterceptorChain
    &QGrpcInterceptorChain::operator=(QGrpcInterceptorChain &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGrpcInterceptorChain::swap(QGrpcInterceptorChain &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QGrpcInterceptorChain::addImpl(void *interceptor, DeleterFn
    deleter, QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding>
    bindings)': names 'void', which has no cute class yet.
  - Qt's 'const QGrpcInterceptorChainPrivate *QGrpcInterceptorChain::d_func()
    const': takes in Python what 'QGrpcInterceptorChainPrivate
    *QGrpcInterceptorChain::d_func()' takes.

  What has no ritual
  ------------------

  15 of the 29 functions Qt declares: 7 forbidden; 6 a template; 2 takes or
  gives a number that is not equally wide on every system.

  What to expect
  --------------

  - The C++ QGrpcInterceptorChain is created at the first use, not by
    'QGrpcInterceptorChain(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcInterceptorChain.
  - Each name of Qt's QGrpcInterceptorChain that has no cute function yet,
    'add', 'addHelper', 'addImpl', 'capabilities', 'capabilitiesAt', 'set',
    'setHelper', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcInterceptorChain'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QGrpcInterceptorChain::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#size
    """
    #  qsizetype QGrpcInterceptorChain::size() const
    return self.uglySide.call('ritual_ZNK21QGrpcInterceptorChain4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGrpcInterceptorChain::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#isEmpty
    """
    #  bool QGrpcInterceptorChain::isEmpty() const
    return self.uglySide.call('ritual_ZNK21QGrpcInterceptorChain7isEmptyEv')

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QGrpcInterceptorChain::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#empty
    """
    #  bool QGrpcInterceptorChain::empty() const
    return self.uglySide.call('ritual_ZNK21QGrpcInterceptorChain5emptyEv')

  @overload(QtGrpc.InterceptorCapability)
  def hasHandlerFor(self, cap: QtGrpc.InterceptorCapability) -> bool:
    """
    Calls Qt's 'bool
    QGrpcInterceptorChain::hasHandlerFor(QtGrpc::InterceptorCapability cap)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#hasHandlerFor

    Parameters
    ----------

    cap : QtGrpc.InterceptorCapability
      Passed on as its number.
    """
    #  bool
    #      QGrpcInterceptorChain::hasHandlerFor(QtGrpc::InterceptorCapability
    #      cap) const
    return self.uglySide.call(
        'ritual_ZNK21QGrpcInterceptorChain13hasHandlerForEN6QtGrpc21Interce'
        'ptorCapabilityE',
        cap.value,
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
    Notes what was given, for Qt's
    'QGrpcInterceptorChain::QGrpcInterceptorChain()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#QGrpcInterceptorChain
    """
    #  QGrpcInterceptorChain::QGrpcInterceptorChain()
    self._noteCreation(QGrpcInterceptorChain, lambda: Rituals.call(
        'ritual_ZN21QGrpcInterceptorChainC1Ev',
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
    Calls Qt's 'void QGrpcInterceptorChain::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#clear
    """
    #  void QGrpcInterceptorChain::clear()
    self.uglySide.call('ritual_ZN21QGrpcInterceptorChain5clearEv')

  @overload()
  @overload(int)
  @overload(int, int)
  def warnNullInterceptor(self, index: int = -1, total: int = -1) -> None:
    """
    Calls Qt's 'void QGrpcInterceptorChain::warnNullInterceptor(qsizetype
    index, qsizetype total) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#warnNullInterceptor

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    total : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QGrpcInterceptorChain::warnNullInterceptor(qsizetype index,
    #      qsizetype total) const
    self.uglySide.call(
        'ritual_ZNK21QGrpcInterceptorChain19warnNullInterceptorExx',
        index, total,
    )

  def d_func(self) -> Optional[QGrpcInterceptorChainPrivate]:
    """
    Calls Qt's 'QGrpcInterceptorChainPrivate
    *QGrpcInterceptorChain::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcinterceptorchain.html#d_func

    Returns
    -------

    Optional[QGrpcInterceptorChainPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGrpcInterceptorChainPrivate *QGrpcInterceptorChain::d_func()
    address = self.uglySide.call('ritual_ZN21QGrpcInterceptorChain6d_funcEv')
    from . import QGrpcInterceptorChainPrivate
    return QGrpcInterceptorChainPrivate._cuteAt(address)

  @staticmethod
  def add(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorChain::add': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.add' has no cute function yet. Qt's "
        "'QGrpcInterceptorChain::add': a template: a pattern and no single "
        "function.")

  @staticmethod
  def addHelper(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorChain::addHelper': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.addHelper' has no cute function yet. Qt's "
        "'QGrpcInterceptorChain::addHelper': a template: a pattern and no "
        "single function.")

  @staticmethod
  def addImpl(*__, **_) -> Never:
    """
    Qt's 'bool QGrpcInterceptorChain::addImpl(void *interceptor, DeleterFn
    deleter, QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding>
    bindings)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.addImpl' has no cute function yet. Qt's "
        "'bool QGrpcInterceptorChain::addImpl(void *interceptor, DeleterFn "
        "deleter, QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding> "
        "bindings)': names 'void', which has no cute class yet.")

  @staticmethod
  def capabilities(*__, **_) -> Never:
    """
    Qt's 'QtGrpc::InterceptorCapabilities
    QGrpcInterceptorChain::capabilities() const': takes or gives a number
    that is not equally wide on every system:
    QtGrpc::InterceptorCapabilities.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.capabilities' has no cute function yet. "
        "Qt's 'QtGrpc::InterceptorCapabilities "
        "QGrpcInterceptorChain::capabilities() const': takes or gives a "
        "number that is not equally wide on every system: "
        "QtGrpc::InterceptorCapabilities.")

  @staticmethod
  def capabilitiesAt(*__, **_) -> Never:
    """
    Qt's 'QtGrpc::InterceptorCapabilities
    QGrpcInterceptorChain::capabilitiesAt(qsizetype index) const': takes or
    gives a number that is not equally wide on every system:
    QtGrpc::InterceptorCapabilities.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.capabilitiesAt' has no cute function yet. "
        "Qt's 'QtGrpc::InterceptorCapabilities "
        "QGrpcInterceptorChain::capabilitiesAt(qsizetype index) const': "
        "takes or gives a number that is not equally wide on every system: "
        "QtGrpc::InterceptorCapabilities.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorChain::set': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.set' has no cute function yet. Qt's "
        "'QGrpcInterceptorChain::set': a template: a pattern and no single "
        "function.")

  @staticmethod
  def setHelper(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorChain::setHelper': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.setHelper' has no cute function yet. Qt's "
        "'QGrpcInterceptorChain::setHelper': a template: a pattern and no "
        "single function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorChain::swap(QGrpcInterceptorChain &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorChain.swap' has no cute function yet. Qt's 'void "
        "QGrpcInterceptorChain::swap(QGrpcInterceptorChain &other)': takes "
        "a type Python has no way to hand over yet.")
