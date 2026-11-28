"""
QGeoTileFetcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotilefetcher_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTileFetcher to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QTimerEvent
  from . import QGeoMappingManagerEngine, QGeoTileFetcherPrivate
  from . import QGeoTileSpec, QGeoTiledMapReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QGeoMappingManagerEngine = WAIT['QGeoMappingManagerEngine']
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QGeoTiledMapReply = WAIT['QGeoTiledMapReply']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTileFetcher(QObject):
  """
  The cute side of Qt's QGeoTileFetcher: a plain Python object standing in
  front of one C++ QGeoTileFetcher.

  It is built on the cute 'QObject', as Qt's QGeoTileFetcher is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTileFetcher that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'd_func',
  'requestNextTile', 'finished', 'tileFinished', 'tileError', 'timerEvent',
  'initialized', 'fetchingEnabled', 'getTileImage', 'handleReply'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoTileFetcher::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGeoTileFetcher::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QGeoTileFetcherPrivate *QGeoTileFetcher::d_func() const':
    takes in Python what 'QGeoTileFetcherPrivate *QGeoTileFetcher::d_func()'
    takes.
  - Qt's 'QGeoTileFetcher::~QGeoTileFetcher()': the destructor: Python never
    removes a C++ QGeoTileFetcher.
  - Qt's 'void QGeoTileFetcher::updateTileRequests(const QSet<QGeoTileSpec>
    &tilesAdded, const QSet<QGeoTileSpec> &tilesRemoved)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QGeoTileFetcher::cancelTileRequests(const QSet<QGeoTileSpec>
    &tiles)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoTileFetcher::QGeoTileFetcher(QGeoTileFetcherPrivate &dd,
    QGeoMappingManagerEngine *parent)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  5 of the 25 functions Qt declares: 2 not a gap; 2 forbidden; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGeoTileFetcher is created at the first use, not by
    'QGeoTileFetcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTileFetcher.
  - Qt tells when it has removed the C++ QGeoTileFetcher. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGeoTileFetcher that has no cute function yet,
    'cacheHint', 'cancelTileRequests', 'updateTileRequests', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QGeoTileFetcher::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#tr

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
    #  QString QGeoTileFetcher::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGeoTileFetcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTileFetcher'

  #  A C++ QGeoTileFetcher Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTileFetcher'

  #  The functions Qt calls itself that QGeoTileFetcher is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialized': (
          ('_ZNK15QGeoTileFetcher11initializedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fetchingEnabled': (
          ('_ZNK15QGeoTileFetcher15fetchingEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'getTileImage': (
          ('_ZN15QGeoTileFetcher12getTileImageERK12QGeoTileSpec',
           ('address', 'address', 'QtLocation:QGeoTiledMapReply'),
           (
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
           )),
      ),
      'handleReply': (
          ('_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReplyRK12QGeoT'
           'ileSpec',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtLocation:QGeoTiledMapReply'),
               ('address', 'value', 'QtLocation:QGeoTileSpec'),
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
    Calls Qt's 'const QMetaObject *QGeoTileFetcher::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoTileFetcher::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGeoTileFetcher10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QGeoTileFetcher::initialized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#initialized
    """
    #  bool QGeoTileFetcher::initialized() const
    ritual = 'ritual_ZNK15QGeoTileFetcher11initializedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGeoTileFetcher11initializedEv'
    return self.uglySide.call(ritual)

  def fetchingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGeoTileFetcher::fetchingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilefetcher.html#fetchingEnabled
    """
    #  bool QGeoTileFetcher::fetchingEnabled() const
    ritual = 'ritual_ZNK15QGeoTileFetcher15fetchingEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGeoTileFetcher15fetchingEnabledEv'
    return self.uglySide.call(ritual)

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

  @overload(QGeoMappingManagerEngine)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGeoMappingManagerEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QGeoTileFetcher::QGeoTileFetcher(QGeoMappingManagerEngine *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilefetcher.html#QGeoTileFetcher

    Parameters
    ----------

    parent : Optional[QGeoMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoTileFetcher::QGeoTileFetcher(QGeoMappingManagerEngine *parent)
    self._noteCreation(QGeoTileFetcher, lambda: Rituals.call(
        'ritual_ZN15QGeoTileFetcherC1EP24QGeoMappingManagerEngine',
        self._addressOf(parent),
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

  def d_func(self) -> Optional[QGeoTileFetcherPrivate]:
    """
    Calls Qt's 'QGeoTileFetcherPrivate *QGeoTileFetcher::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#d_func

    Returns
    -------

    Optional[QGeoTileFetcherPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTileFetcherPrivate *QGeoTileFetcher::d_func()
    address = self.uglySide.call('ritual_ZN15QGeoTileFetcher6d_funcEv')
    from . import QGeoTileFetcherPrivate
    return QGeoTileFetcherPrivate._cuteAt(address)

  def requestNextTile(self) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::requestNextTile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotilefetcher.html#requestNextTile
    """
    #  void QGeoTileFetcher::requestNextTile()
    self.uglySide.call('ritual_ZN15QGeoTileFetcher15requestNextTileEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#finished
    """
    #  void QGeoTileFetcher::finished()
    self.uglySide.call('ritual_ZN15QGeoTileFetcher8finishedEv')

  @overload(QGeoTileSpec, QByteArray, str)
  def tileFinished(
      self,
      spec: QGeoTileSpec,
      bytes: QByteArray,
      format: str,
  ) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::tileFinished(const QGeoTileSpec &spec,
    const QByteArray &bytes, const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#tileFinished

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTileFetcher::tileFinished(const QGeoTileSpec &spec, const
    #      QByteArray &bytes, const QString &format)
    self.uglySide.call(
        'ritual_ZN15QGeoTileFetcher12tileFinishedERK12QGeoTileSpecRK10QByte'
        'ArrayRK7QString',
        self._valueOf(spec), self._valueOf(bytes), format,
    )

  @overload(QGeoTileSpec, str)
  def tileError(self, spec: QGeoTileSpec, errorString: str) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::tileError(const QGeoTileSpec &spec,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#tileError

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoTileFetcher::tileError(const QGeoTileSpec &spec, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN15QGeoTileFetcher9tileErrorERK12QGeoTileSpecRK7QString',
        self._valueOf(spec), errorString,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTileFetcher::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QGeoTileFetcher10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QGeoTileFetcher10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGeoTileSpec)
  def getTileImage(self, spec: QGeoTileSpec) -> Optional[QGeoTiledMapReply]:
    """
    Calls Qt's 'QGeoTiledMapReply *QGeoTileFetcher::getTileImage(const
    QGeoTileSpec &spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#getTileImage

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    Returns
    -------

    Optional[QGeoTiledMapReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoTiledMapReply *QGeoTileFetcher::getTileImage(const QGeoTileSpec
    #      &spec)
    address = self.uglySide.call(
        'ritual_ZN15QGeoTileFetcher12getTileImageERK12QGeoTileSpec',
        self._valueOf(spec),
    )
    from . import QGeoTiledMapReply
    return QGeoTiledMapReply._cuteAt(address)

  @overload(QGeoTiledMapReply, QGeoTileSpec)
  @overload(NoneType, QGeoTileSpec)
  def handleReply(
      self,
      reply: Optional[QGeoTiledMapReply],
      spec: QGeoTileSpec,
  ) -> None:
    """
    Calls Qt's 'void QGeoTileFetcher::handleReply(QGeoTiledMapReply *reply,
    const QGeoTileSpec &spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeotilefetcher.html#handleReply

    Parameters
    ----------

    reply : Optional[QGeoTiledMapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.
    """
    #  void QGeoTileFetcher::handleReply(QGeoTiledMapReply *reply, const
    #      QGeoTileSpec &spec)
    ritual = (
        'ritual_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReplyRK12QG'
        'eoTileSpec')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGeoTileFetcher11handleReplyEP17QGeoTiledMapReply'
          'RK12QGeoTileSpec')
    self.uglySide.call(ritual, self._addressOf(reply), self._valueOf(spec))

  @staticmethod
  def cacheHint(*__, **_) -> Never:
    """
    Qt's 'QAbstractGeoTileCache::CacheAreas QGeoTileFetcher::cacheHint()
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QGeoTileFetcher.cacheHint' has no cute function yet. Qt's "
        "'QAbstractGeoTileCache::CacheAreas QGeoTileFetcher::cacheHint() "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def cancelTileRequests(*__, **_) -> Never:
    """
    Qt's 'void QGeoTileFetcher::cancelTileRequests(const QSet<QGeoTileSpec>
    &tiles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTileFetcher.cancelTileRequests' has no cute function yet. "
        "Qt's 'void QGeoTileFetcher::cancelTileRequests(const "
        "QSet<QGeoTileSpec> &tiles)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateTileRequests(*__, **_) -> Never:
    """
    Qt's 'void QGeoTileFetcher::updateTileRequests(const QSet<QGeoTileSpec>
    &tilesAdded, const QSet<QGeoTileSpec> &tilesRemoved)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoTileFetcher.updateTileRequests' has no cute function yet. "
        "Qt's 'void QGeoTileFetcher::updateTileRequests(const "
        "QSet<QGeoTileSpec> &tilesAdded, const QSet<QGeoTileSpec> "
        "&tilesRemoved)': takes a type Python has no way to hand over yet.")
