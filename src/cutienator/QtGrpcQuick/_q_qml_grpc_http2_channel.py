"""
QQmlGrpcHttp2Channel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpchttp2channel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlGrpcHttp2Channel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlAbstractGrpcChannel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQmlGrpcChannelOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlGrpcChannelOptions = WAIT['QQmlGrpcChannelOptions']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGrpcHttp2Channel(QQmlAbstractGrpcChannel):
  """
  The cute side of Qt's QQmlGrpcHttp2Channel: a plain Python object standing
  in front of one C++ QQmlGrpcHttp2Channel.

  It is built on the cute 'QQmlAbstractGrpcChannel', as Qt's
  QQmlGrpcHttp2Channel is built on Qt's QQmlAbstractGrpcChannel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlGrpcHttp2Channel that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'options',
  'setOptions', 'hostUri', 'setHostUri', 'optionsChanged', 'channelUpdated',
  'hostUriChanged', 'updateChannel'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlGrpcHttp2Channel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlGrpcHttp2Channel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlGrpcHttp2Channel::~QQmlGrpcHttp2Channel()': the destructor:
    Python never removes a C++ QQmlGrpcHttp2Channel.
  - Qt's 'std::shared_ptr<QAbstractGrpcChannel>
    QQmlGrpcHttp2Channel::channel() const': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlGrpcHttp2ChannelPrivate *QQmlGrpcHttp2Channel::d_func()': gives
    'QQmlGrpcHttp2ChannelPrivate', which has no cute class yet.
  - Qt's 'const QQmlGrpcHttp2ChannelPrivate *QQmlGrpcHttp2Channel::d_func()
    const': gives 'QQmlGrpcHttp2ChannelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlGrpcHttp2Channel is created at the first use, not by
    'QQmlGrpcHttp2Channel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGrpcHttp2Channel.
  - Qt tells when it has removed the C++ QQmlGrpcHttp2Channel. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlGrpcHttp2Channel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#tr

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
    #  QString QQmlGrpcHttp2Channel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlGrpcHttp2Channel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGrpcHttp2Channel'

  #  A C++ QQmlGrpcHttp2Channel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGrpcHttp2Channel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlGrpcHttp2Channel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlGrpcHttp2Channel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGrpcHttp2Channel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def options(self) -> Optional[QQmlGrpcChannelOptions]:
    """
    Calls Qt's 'QQmlGrpcChannelOptions *QQmlGrpcHttp2Channel::options()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#options

    Returns
    -------

    Optional[QQmlGrpcChannelOptions]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGrpcChannelOptions *QQmlGrpcHttp2Channel::options() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGrpcHttp2Channel7optionsEv',
    )
    from . import QQmlGrpcChannelOptions
    return QQmlGrpcChannelOptions._cuteAt(address)

  def hostUri(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlGrpcHttp2Channel::hostUri() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#hostUri

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlGrpcHttp2Channel::hostUri() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGrpcHttp2Channel7hostUriEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlGrpcChannelOptions)
  @overload(NoneType)
  def setOptions(self, options: Optional[QQmlGrpcChannelOptions]) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::setOptions(QQmlGrpcChannelOptions
    *options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#setOptions

    Parameters
    ----------

    options : Optional[QQmlGrpcChannelOptions]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlGrpcHttp2Channel::setOptions(QQmlGrpcChannelOptions *options)
    self.uglySide.call(
        'ritual_ZN20QQmlGrpcHttp2Channel10setOptionsEP22QQmlGrpcChannelOpti'
        'ons',
        self._addressOf(options),
    )

  @overload(QUrl)
  def setHostUri(self, hostUri: QUrl) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::setHostUri(const QUrl &hostUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#setHostUri

    Parameters
    ----------

    hostUri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlGrpcHttp2Channel::setHostUri(const QUrl &hostUri)
    self.uglySide.call(
        'ritual_ZN20QQmlGrpcHttp2Channel10setHostUriERK4QUrl',
        self._valueOf(hostUri),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGrpcHttp2Channel::QQmlGrpcHttp2Channel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#QQmlGrpcHttp2Channel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlGrpcHttp2Channel::QQmlGrpcHttp2Channel(QObject *parent)
    self._noteCreation(QQmlGrpcHttp2Channel, lambda: Rituals.call(
        'ritual_ZN20QQmlGrpcHttp2ChannelC1EP7QObject',
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

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#optionsChanged
    """
    #  void QQmlGrpcHttp2Channel::optionsChanged()
    self.uglySide.call('ritual_ZN20QQmlGrpcHttp2Channel14optionsChangedEv')

  def channelUpdated(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::channelUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#channelUpdated
    """
    #  void QQmlGrpcHttp2Channel::channelUpdated()
    self.uglySide.call('ritual_ZN20QQmlGrpcHttp2Channel14channelUpdatedEv')

  def hostUriChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::hostUriChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#hostUriChanged
    """
    #  void QQmlGrpcHttp2Channel::hostUriChanged()
    self.uglySide.call('ritual_ZN20QQmlGrpcHttp2Channel14hostUriChangedEv')

  def updateChannel(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcHttp2Channel::updateChannel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpchttp2channel.html#updateChannel
    """
    #  void QQmlGrpcHttp2Channel::updateChannel()
    self.uglySide.call('ritual_ZN20QQmlGrpcHttp2Channel13updateChannelEv')
