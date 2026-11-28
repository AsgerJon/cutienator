"""
QtGrpcQuickPrivate::QQmlGrpcCallOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/qqmlgrpccalloptions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlGrpcMetadata
  from ..QtGrpc import QGrpcCallOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlGrpcMetadata = WAIT['QQmlGrpcMetadata']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGrpcCallOptions(QObject):
  """
  The cute side of Qt's QtGrpcQuickPrivate::QQmlGrpcCallOptions: a plain
  Python object standing in front of one C++
  QtGrpcQuickPrivate::QQmlGrpcCallOptions.

  It is built on the cute 'QObject', as Qt's
  QtGrpcQuickPrivate::QQmlGrpcCallOptions is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtGrpcQuickPrivate::QQmlGrpcCallOptions that has a
  ritual and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'options', 'deadlineTimeout', 'setDeadlineTimeout', 'metadata',
  'setMetadata', 'deadlineTimeoutChanged', 'metadataChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtGrpcQuickPrivate::QQmlGrpcCallOptions::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtGrpcQuickPrivate::QQmlGrpcCallOptions::~QQmlGrpcCallOptions()':
    the destructor: Python never removes a C++
    QtGrpcQuickPrivate::QQmlGrpcCallOptions.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here; 1 forbidden.

  What to expect
  --------------

  - The C++ QtGrpcQuickPrivate::QQmlGrpcCallOptions is created at the first
    use, not by 'QtGrpcQuickPrivate::QQmlGrpcCallOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtGrpcQuickPrivate::QQmlGrpcCallOptions.
  - Qt tells when it has removed the C++
    QtGrpcQuickPrivate::QQmlGrpcCallOptions. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString QtGrpcQuickPrivate::QQmlGrpcCallOptions::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html#tr

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
    #  QString QtGrpcQuickPrivate::QQmlGrpcCallOptions::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGrpcQuickPrivate::QQmlGrpcCallOptions'

  #  A C++ QtGrpcQuickPrivate::QQmlGrpcCallOptions Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtGrpcQuickPrivate_QQmlGrpcCallOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtGrpcQuickPrivate::QQmlGrpcCallOptions::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtGrpcQuickPrivate::QQmlGrpcCallOptions::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtGrpcQuickPrivate19QQmlGrpcCallOptions10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def options(self) -> QGrpcCallOptions:
    """
    Calls Qt's 'const QGrpcCallOptions
    &QtGrpcQuickPrivate::QQmlGrpcCallOptions::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Returns
    -------

    QGrpcCallOptions
      A new cute QGrpcCallOptions around the copy Qt gave back. Python owns
      it.
    """
    #  const QGrpcCallOptions
    #      &QtGrpcQuickPrivate::QQmlGrpcCallOptions::options() const
    address = self.uglySide.call(
        'ritual_ZNKR18QtGrpcQuickPrivate19QQmlGrpcCallOptions7optionsEv',
    )
    from ..QtGrpc import QGrpcCallOptions
    return QGrpcCallOptions._cuteOwning(address)

  def deadlineTimeout(self) -> int:
    """
    Calls Qt's 'qint64
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::deadlineTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html
    """
    #  qint64 QtGrpcQuickPrivate::QQmlGrpcCallOptions::deadlineTimeout()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtGrpcQuickPrivate19QQmlGrpcCallOptions15deadlineTimeo'
        'utEv',
    )

  def metadata(self) -> Optional[QQmlGrpcMetadata]:
    """
    Calls Qt's 'QQmlGrpcMetadata
    *QtGrpcQuickPrivate::QQmlGrpcCallOptions::metadata() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Returns
    -------

    Optional[QQmlGrpcMetadata]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGrpcMetadata *QtGrpcQuickPrivate::QQmlGrpcCallOptions::metadata()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtGrpcQuickPrivate19QQmlGrpcCallOptions8metadataEv',
    )
    from . import QQmlGrpcMetadata
    return QQmlGrpcMetadata._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDeadlineTimeout(self, value: int) -> None:
    """
    Calls Qt's 'void
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::setDeadlineTimeout(qint64
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void
    #      QtGrpcQuickPrivate::QQmlGrpcCallOptions::setDeadlineTimeout(qint64
    #      value)
    self.uglySide.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions18setDeadlineTim'
        'eoutEx',
        value,
    )

  @overload(QQmlGrpcMetadata)
  @overload(NoneType)
  def setMetadata(self, value: Optional[QQmlGrpcMetadata]) -> None:
    """
    Calls Qt's 'void
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::setMetadata(QQmlGrpcMetadata
    *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Parameters
    ----------

    value : Optional[QQmlGrpcMetadata]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtGrpcQuickPrivate::QQmlGrpcCallOptions::setMetadata(
    #      QQmlGrpcMetadata *value)
    self.uglySide.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions11setMetadataEP1'
        '6QQmlGrpcMetadata',
        self._addressOf(value),
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
    'QtGrpcQuickPrivate::QQmlGrpcCallOptions::QQmlGrpcCallOptions(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtGrpcQuickPrivate::QQmlGrpcCallOptions::QQmlGrpcCallOptions(QObject
    #      *parent)
    self._noteCreation(QQmlGrpcCallOptions, lambda: Rituals.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptionsC1EP7QObject',
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

  def deadlineTimeoutChanged(self) -> None:
    """
    Calls Qt's 'void
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::deadlineTimeoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html
    """
    #  void QtGrpcQuickPrivate::QQmlGrpcCallOptions::deadlineTimeoutChanged()
    self.uglySide.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions22deadlineTimeou'
        'tChangedEv',
    )

  def metadataChanged(self) -> None:
    """
    Calls Qt's 'void
    QtGrpcQuickPrivate::QQmlGrpcCallOptions::metadataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpcquickprivate-qqmlgrpccalloptions.html
    """
    #  void QtGrpcQuickPrivate::QQmlGrpcCallOptions::metadataChanged()
    self.uglySide.call(
        'ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions15metadataChange'
        'dEv',
    )
