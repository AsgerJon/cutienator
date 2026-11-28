"""
QQuickItemGrabResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickitemgrabresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QUrl
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemGrabResult(QObject):
  """
  The cute side of Qt's QQuickItemGrabResult: a plain Python object standing
  in front of one C++ QQuickItemGrabResult.

  It is built on the cute 'QObject', as Qt's QQuickItemGrabResult is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemGrabResult that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'image', 'url',
  'saveToFile', 'event', 'ready', 'setup', 'render'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemGrabResult::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickItemGrabResult::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickItemGrabResultPrivate *QQuickItemGrabResult::d_func()': gives
    'QQuickItemGrabResultPrivate', which has no cute class yet.
  - Qt's 'const QQuickItemGrabResultPrivate *QQuickItemGrabResult::d_func()
    const': gives 'QQuickItemGrabResultPrivate', which has no cute class yet.
  - Qt's 'void QQuickItemGrabResult::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemGrabResult is created at the first use, not by
    'QQuickItemGrabResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemGrabResult.
  - Qt tells when it has removed the C++ QQuickItemGrabResult. Every call on
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
    Calls Qt's 'QString QQuickItemGrabResult::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#tr

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
    #  QString QQuickItemGrabResult::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickItemGrabResult2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemGrabResult'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemGrabResult::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgrabresult.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemGrabResult::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickItemGrabResult10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickItemGrabResult::image() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickItemGrabResult::image() const
    address = self.uglySide.call('ritual_ZNK20QQuickItemGrabResult5imageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickItemGrabResult::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickItemGrabResult::url() const
    address = self.uglySide.call('ritual_ZNK20QQuickItemGrabResult3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(str)
  def saveToFile(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QQuickItemGrabResult::saveToFile(const QString
    &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgrabresult.html#saveToFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickItemGrabResult::saveToFile(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemGrabResult10saveToFileERK7QString', fileName,
    )

  @overload(QUrl)
  def saveToFile(self, fileName: QUrl) -> bool:
    """
    Calls Qt's 'bool QQuickItemGrabResult::saveToFile(const QUrl &fileName)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgrabresult.html#saveToFile

    Parameters
    ----------

    fileName : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQuickItemGrabResult::saveToFile(const QUrl &fileName) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemGrabResult10saveToFileERK4QUrl',
        self._valueOf(fileName),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemGrabResult::QQuickItemGrabResult(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgrabresult.html#QQuickItemGrabResult

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItemGrabResult::QQuickItemGrabResult(QObject *parent)
    self._noteCreation(QQuickItemGrabResult, lambda: Rituals.call(
        'ritual_ZN20QQuickItemGrabResultC1EP7QObject',
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickItemGrabResult::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItemGrabResult::event(QEvent *a0)
    ritual = 'ritual_ZN20QQuickItemGrabResult5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickItemGrabResult5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def ready(self) -> None:
    """
    Calls Qt's 'void QQuickItemGrabResult::ready()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#ready
    """
    #  void QQuickItemGrabResult::ready()
    self.uglySide.call('ritual_ZN20QQuickItemGrabResult5readyEv')

  def setup(self) -> None:
    """
    Calls Qt's 'void QQuickItemGrabResult::setup()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#setup
    """
    #  void QQuickItemGrabResult::setup()
    self.uglySide.call('ritual_ZN20QQuickItemGrabResult5setupEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QQuickItemGrabResult::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgrabresult.html#render
    """
    #  void QQuickItemGrabResult::render()
    self.uglySide.call('ritual_ZN20QQuickItemGrabResult6renderEv')
