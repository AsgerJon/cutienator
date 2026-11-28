"""
QWebChannelAbstractTransport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebChannel/qwebchannelabstracttransport.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebChannelAbstractTransport(QObject):
  """
  The cute side of Qt's QWebChannelAbstractTransport: a plain Python object
  standing in front of one C++ QWebChannelAbstractTransport.

  It is built on the cute 'QObject', as Qt's QWebChannelAbstractTransport is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebChannelAbstractTransport that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'sendMessage', 'messageReceived'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebChannelAbstractTransport::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWebChannelAbstractTransport::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebChannelAbstractTransport::~QWebChannelAbstractTransport()': the
    destructor: Python never removes a C++ QWebChannelAbstractTransport.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebChannelAbstractTransport is created at the first use, not by
    'QWebChannelAbstractTransport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebChannelAbstractTransport.
  - Qt tells when it has removed the C++ QWebChannelAbstractTransport. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QWebChannelAbstractTransport::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#tr

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
    #  QString QWebChannelAbstractTransport::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QWebChannelAbstractTransport2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebChannelAbstractTransport'

  #  A C++ QWebChannelAbstractTransport Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebChannelAbstractTransport'

  #  The functions Qt calls itself that QWebChannelAbstractTransport is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'sendMessage': (
          ('_ZN28QWebChannelAbstractTransport11sendMessageERK11QJsonObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QJsonObject'),
           )),
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
    Calls Qt's 'const QMetaObject *QWebChannelAbstractTransport::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebChannelAbstractTransport::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebChannelAbstractTransport10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWebChannelAbstractTransport::QWebChannelAbstractTransport(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebChannelAbstractTransport::QWebChannelAbstractTransport(QObject
    #      *parent)
    self._noteCreation(QWebChannelAbstractTransport, lambda: Rituals.call(
        'ritual_ZN28QWebChannelAbstractTransportC1EP7QObject',
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

  @overload(QJsonObject)
  def sendMessage(self, message: QJsonObject) -> None:
    """
    Calls Qt's 'void QWebChannelAbstractTransport::sendMessage(const
    QJsonObject &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#sendMessage

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void QWebChannelAbstractTransport::sendMessage(const QJsonObject
    #      &message)
    self.uglySide.call(
        'ritual_ZN28QWebChannelAbstractTransport11sendMessageERK11QJsonObje'
        'ct',
        self._valueOf(message),
    )

  @overload(QJsonObject, THIS)
  @overload(QJsonObject, NoneType)
  def messageReceived(
      self,
      message: QJsonObject,
      transport: Optional[QWebChannelAbstractTransport],
  ) -> None:
    """
    Calls Qt's 'void QWebChannelAbstractTransport::messageReceived(const
    QJsonObject &message, QWebChannelAbstractTransport *transport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebchannelabstracttransport.html#messageReceived

    Parameters
    ----------

    message : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    transport : Optional[QWebChannelAbstractTransport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebChannelAbstractTransport::messageReceived(const QJsonObject
    #      &message, QWebChannelAbstractTransport *transport)
    self.uglySide.call(
        'ritual_ZN28QWebChannelAbstractTransport15messageReceivedERK11QJson'
        'ObjectPS_',
        self._valueOf(message), self._addressOf(transport),
    )
