"""
QFileSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfileselector.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QFileSelectorPrivate, QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileSelector(QObject):
  """
  The cute side of Qt's QFileSelector: a plain Python object standing in
  front of one C++ QFileSelector.

  It is built on the cute 'QObject', as Qt's QFileSelector is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSelector that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'select',
  'extraSelectors', 'setExtraSelectors', 'allSelectors', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFileSelector::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QFileSelector::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QFileSelector::~QFileSelector()': the destructor: Python never
    removes a C++ QFileSelector.
  - Qt's 'const QFileSelectorPrivate *QFileSelector::d_func() const': takes
    in Python what 'QFileSelectorPrivate *QFileSelector::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QFileSelector is created at the first use, not by
    'QFileSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSelector.
  - Qt tells when it has removed the C++ QFileSelector. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QFileSelector::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#tr

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
    #  QString QFileSelector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QFileSelector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSelector'

  #  A C++ QFileSelector Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileSelector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileSelector::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileSelector::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QFileSelector10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def select(self, filePath: str) -> str:
    """
    Calls Qt's 'QString QFileSelector::select(const QString &filePath)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#select

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSelector::select(const QString &filePath) const
    return self.uglySide.call(
        'ritual_ZNK13QFileSelector6selectERK7QString', filePath,
    )

  @overload(QUrl)
  def select(self, filePath: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QFileSelector::select(const QUrl &filePath) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#select

    Parameters
    ----------

    filePath : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QFileSelector::select(const QUrl &filePath) const
    address = self.uglySide.call(
        'ritual_ZNK13QFileSelector6selectERK4QUrl', self._valueOf(filePath),
    )
    from . import QUrl
    return QUrl._cuteOwning(address)

  def extraSelectors(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSelector::extraSelectors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#extraSelectors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSelector::extraSelectors() const
    address = self.uglySide.call(
        'ritual_ZNK13QFileSelector14extraSelectorsEv',
    )
    return QStringList._cuteOwning(address)

  def allSelectors(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSelector::allSelectors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#allSelectors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSelector::allSelectors() const
    address = self.uglySide.call('ritual_ZNK13QFileSelector12allSelectorsEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setExtraSelectors(self, list: QStringList) -> None:
    """
    Calls Qt's 'void QFileSelector::setExtraSelectors(const QStringList
    &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselector.html#setExtraSelectors

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileSelector::setExtraSelectors(const QStringList &list)
    self.uglySide.call(
        'ritual_ZN13QFileSelector17setExtraSelectorsERK5QListI7QStringE',
        self._valueOf(list),
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
    Notes what was given, for Qt's 'QFileSelector::QFileSelector(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#QFileSelector

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileSelector::QFileSelector(QObject *parent)
    self._noteCreation(QFileSelector, lambda: Rituals.call(
        'ritual_ZN13QFileSelectorC1EP7QObject',
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

  def d_func(self) -> Optional[QFileSelectorPrivate]:
    """
    Calls Qt's 'QFileSelectorPrivate *QFileSelector::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselector.html#d_func

    Returns
    -------

    Optional[QFileSelectorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSelectorPrivate *QFileSelector::d_func()
    address = self.uglySide.call('ritual_ZN13QFileSelector6d_funcEv')
    from . import QFileSelectorPrivate
    return QFileSelectorPrivate._cuteAt(address)
