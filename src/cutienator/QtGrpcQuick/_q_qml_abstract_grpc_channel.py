"""
QQmlAbstractGrpcChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/qqmlabstractgrpcchannel.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlAbstractGrpcChannelPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAbstractGrpcChannel(QObject):
  """
  The cute side of Qt's QQmlAbstractGrpcChannel: a plain Python object
  standing in front of one C++ QQmlAbstractGrpcChannel.

  It is built on the cute 'QObject', as Qt's QQmlAbstractGrpcChannel is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlAbstractGrpcChannel that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'tr', 'd_func'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlAbstractGrpcChannel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlAbstractGrpcChannel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlAbstractGrpcChannel::~QQmlAbstractGrpcChannel()': the
    destructor: Python never removes a C++ QQmlAbstractGrpcChannel.
  - Qt's 'std::shared_ptr<QAbstractGrpcChannel>
    QQmlAbstractGrpcChannel::channel() const': gives a type Python has no way
    to take yet.
  - Qt's 'const QQmlAbstractGrpcChannelPrivate
    *QQmlAbstractGrpcChannel::d_func() const': takes in Python what
    'QQmlAbstractGrpcChannelPrivate *QQmlAbstractGrpcChannel::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQmlAbstractGrpcChannel is created at the first use, not by
    'QQmlAbstractGrpcChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractGrpcChannel.
  - Qt tells when it has removed the C++ QQmlAbstractGrpcChannel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlAbstractGrpcChannel that has no cute function yet,
    '__init__', 'channel', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQmlAbstractGrpcChannel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractgrpcchannel.html#tr

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
    #  QString QQmlAbstractGrpcChannel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQmlAbstractGrpcChannel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractGrpcChannel'

  #  A C++ QQmlAbstractGrpcChannel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractGrpcChannel'

  #  The functions Qt calls itself that QQmlAbstractGrpcChannel is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'channel': (
          'std::shared_ptr<QAbstractGrpcChannel> '
          'QQmlAbstractGrpcChannel::channel() const',
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
    Calls Qt's 'const QMetaObject *QQmlAbstractGrpcChannel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractgrpcchannel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlAbstractGrpcChannel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractGrpcChannel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQmlAbstractGrpcChannel::QQmlAbstractGrpcChannel(QObject
      *parent)': the class is abstract, so C++ cannot make one, and the C++
      class of ours does not fill in every function it leaves open.
    - Qt's 'QQmlAbstractGrpcChannel::QQmlAbstractGrpcChannel(
      QQmlAbstractGrpcChannelPrivate &dd, QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlAbstractGrpcChannel.__init__' has no cute function yet. Qt's "
        "'QQmlAbstractGrpcChannel::QQmlAbstractGrpcChannel(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open. "
        "Qt's "
        "'QQmlAbstractGrpcChannel::QQmlAbstractGrpcChannel(QQmlAbstractGrpcC"
        "hannelPrivate &dd, QObject *parent)': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  def d_func(self) -> Optional[QQmlAbstractGrpcChannelPrivate]:
    """
    Calls Qt's 'QQmlAbstractGrpcChannelPrivate
    *QQmlAbstractGrpcChannel::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractgrpcchannel.html#d_func

    Returns
    -------

    Optional[QQmlAbstractGrpcChannelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractGrpcChannelPrivate *QQmlAbstractGrpcChannel::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQmlAbstractGrpcChannel6d_funcEv',
    )
    from . import QQmlAbstractGrpcChannelPrivate
    return QQmlAbstractGrpcChannelPrivate._cuteAt(address)

  @staticmethod
  def channel(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QAbstractGrpcChannel>
    QQmlAbstractGrpcChannel::channel() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractGrpcChannel.channel' has no cute function yet. Qt's "
        "'std::shared_ptr<QAbstractGrpcChannel> "
        "QQmlAbstractGrpcChannel::channel() const': gives a type Python has "
        "no way to take yet.")
