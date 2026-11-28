"""
QWaylandClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandclient.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandCompositor

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandClient(QObject):
  """
  The cute side of Qt's QWaylandClient: a plain Python object standing in
  front of one C++ QWaylandClient.

  It is built on the cute 'QObject', as Qt's QWaylandClient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandClient that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'textInputProtocols',
  'setTextInputProtocols', 'compositor', 'userId', 'groupId', 'processId',
  'kill', 'close'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandClient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandClientPrivate *QWaylandClient::d_func()': gives
    'QWaylandClientPrivate', which has no cute class yet.
  - Qt's 'const QWaylandClientPrivate *QWaylandClient::d_func() const': gives
    'QWaylandClientPrivate', which has no cute class yet.
  - Qt's 'void QWaylandClient::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QWaylandClient::~QWaylandClient()': the destructor: Python never
    removes a C++ QWaylandClient.
  - Qt's 'QWaylandClient *QWaylandClient::fromWlClient(QWaylandCompositor
    *compositor, wl_client *wlClient)': names 'wl_client', which has no cute
    class yet.
  - Qt's 'wl_client *QWaylandClient::client() const': gives 'wl_client',
    which has no cute class yet.
  - Qt's 'QWaylandClient::QWaylandClient(QWaylandCompositor *compositor,
    wl_client *client)': names 'wl_client', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandClient is created at the first use, not by
    'QWaylandClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandClient.
  - Qt tells when it has removed the C++ QWaylandClient. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandClient that has no cute function yet,
    '__init__', 'client', 'fromWlClient', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandClient, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TextInputProtocol(CuteFlags):
    """
    The flags enum 'QWaylandClient::TextInputProtocol' of Qt, with the 7
    names Qt gives in it. Qt names the type of its combinations
    'QWaylandClient::TextInputProtocols'.
    """

    NoProtocol = 0x0
    QtTextInputMethodV1 = 0x1
    TextInputV2 = 0x2
    TextInputV3 = 0x4
    TextInputV4 = 0x4
    QtTextInputMethod = 0x1
    TextInput = 0x2

  TextInputProtocols = TextInputProtocol

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
    Calls Qt's 'QString QWaylandClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#tr

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
    #  QString QWaylandClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWaylandClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandClient'

  #  A C++ QWaylandClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWaylandClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textInputProtocols(self) -> TextInputProtocols:
    """
    Calls Qt's 'TextInputProtocols QWaylandClient::textInputProtocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandclient.html#textInputProtocols

    Returns
    -------

    TextInputProtocols
      The value standing for the combination Qt gave back.
    """
    #  TextInputProtocols QWaylandClient::textInputProtocols() const
    return QWaylandClient.TextInputProtocols(self.uglySide.call(
        'ritual_ZNK14QWaylandClient18textInputProtocolsEv',
    ))

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandClient::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandClient::compositor() const
    address = self.uglySide.call('ritual_ZNK14QWaylandClient10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def userId(self) -> int:
    """
    Calls Qt's 'qint64 QWaylandClient::userId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#userId
    """
    #  qint64 QWaylandClient::userId() const
    return self.uglySide.call('ritual_ZNK14QWaylandClient6userIdEv')

  def groupId(self) -> int:
    """
    Calls Qt's 'qint64 QWaylandClient::groupId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#groupId
    """
    #  qint64 QWaylandClient::groupId() const
    return self.uglySide.call('ritual_ZNK14QWaylandClient7groupIdEv')

  def processId(self) -> int:
    """
    Calls Qt's 'qint64 QWaylandClient::processId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#processId
    """
    #  qint64 QWaylandClient::processId() const
    return self.uglySide.call('ritual_ZNK14QWaylandClient9processIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TextInputProtocols)
  def setTextInputProtocols(self, p: TextInputProtocols) -> None:
    """
    Calls Qt's 'void QWaylandClient::setTextInputProtocols(TextInputProtocols
    p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandclient.html#setTextInputProtocols

    Parameters
    ----------

    p : TextInputProtocols
      Passed on as its number.
    """
    #  void QWaylandClient::setTextInputProtocols(TextInputProtocols p)
    self.uglySide.call(
        'ritual_ZN14QWaylandClient21setTextInputProtocolsE6QFlagsINS_17Text'
        'InputProtocolEE',
        p.value,
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
    Qt's 'QWaylandClient::QWaylandClient(QWaylandCompositor *compositor,
    wl_client *client)': names 'wl_client', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandClient.__init__' has no cute function yet. Qt's "
        "'QWaylandClient::QWaylandClient(QWaylandCompositor *compositor, "
        "wl_client *client)': names 'wl_client', which has no cute class "
        "yet.")

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

  @overload()
  @overload(int)
  def kill(self, signal: int = 15) -> None:
    """
    Calls Qt's 'void QWaylandClient::kill(int signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#kill

    Parameters
    ----------

    signal : int
      Passed on as it is. May be left out, as in Qt: it is then 15.
    """
    #  void QWaylandClient::kill(int signal)
    self.uglySide.call('ritual_ZN14QWaylandClient4killEi', signal)

  def close(self) -> None:
    """
    Calls Qt's 'void QWaylandClient::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandclient.html#close
    """
    #  void QWaylandClient::close()
    self.uglySide.call('ritual_ZN14QWaylandClient5closeEv')

  @staticmethod
  def client(*__, **_) -> Never:
    """
    Qt's 'wl_client *QWaylandClient::client() const': gives 'wl_client',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandClient.client' has no cute function yet. Qt's 'wl_client "
        "*QWaylandClient::client() const': gives 'wl_client', which has no "
        "cute class yet.")

  @staticmethod
  def fromWlClient(*__, **_) -> Never:
    """
    Qt's 'QWaylandClient *QWaylandClient::fromWlClient(QWaylandCompositor
    *compositor, wl_client *wlClient)': names 'wl_client', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWaylandClient.fromWlClient' has no cute function yet. Qt's "
        "'QWaylandClient *QWaylandClient::fromWlClient(QWaylandCompositor "
        "*compositor, wl_client *wlClient)': names 'wl_client', which has "
        "no cute class yet.")


#  Qt's 'QList<QWaylandClient *>': the list of QWaylandClient, which
#  'QList[QWaylandClient]' gives. It is made here, so that there is one as
#  soon as there can be a QWaylandClient.
QList.createKind(
    QWaylandClient, 'address',
    make='ritual_list_make_QWaylandClient_ptr',
    add='ritual_list_add_QWaylandClient_ptr',
    size='ritual_list_size_QWaylandClient_ptr',
    at='ritual_list_at_QWaylandClient_ptr',
    drop='ritual_list_drop_QWaylandClient_ptr',
)
