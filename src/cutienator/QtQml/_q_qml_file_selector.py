"""
QQmlFileSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlfileselector.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileSelector, QMetaObject
  from . import QQmlEngine, QQmlFileSelectorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileSelector = WAIT['QFileSelector']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlFileSelector(QObject):
  """
  The cute side of Qt's QQmlFileSelector: a plain Python object standing in
  front of one C++ QQmlFileSelector.

  It is built on the cute 'QObject', as Qt's QQmlFileSelector is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlFileSelector that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func', 'selector',
  'setSelector', 'setExtraSelectors', 'get'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlFileSelector::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlFileSelector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlFileSelectorPrivate *QQmlFileSelector::d_func() const':
    takes in Python what 'QQmlFileSelectorPrivate
    *QQmlFileSelector::d_func()' takes.
  - Qt's 'QQmlFileSelector::~QQmlFileSelector()': the destructor: Python
    never removes a C++ QQmlFileSelector.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlFileSelector is created at the first use, not by
    'QQmlFileSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlFileSelector.
  - Qt tells when it has removed the C++ QQmlFileSelector. Every call on the
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
    Calls Qt's 'QString QQmlFileSelector::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#tr

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
    #  QString QQmlFileSelector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlFileSelector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQmlEngine)
  @overload(NoneType)
  def get(a0: Optional[QQmlEngine]) -> Optional[QQmlFileSelector]:
    """
    Calls Qt's 'QQmlFileSelector *QQmlFileSelector::get(QQmlEngine *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#get

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlFileSelector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFileSelector *QQmlFileSelector::get(QQmlEngine *a0)
    address = Rituals.call(
        'ritual_ZN16QQmlFileSelector3getEP10QQmlEngine',
        CuteMixin._addressOf(a0),
    )
    return QQmlFileSelector._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlFileSelector'

  #  A C++ QQmlFileSelector Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlFileSelector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlFileSelector::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlFileSelector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlFileSelector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selector(self) -> Optional[QFileSelector]:
    """
    Calls Qt's 'QFileSelector *QQmlFileSelector::selector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#selector

    Returns
    -------

    Optional[QFileSelector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSelector *QQmlFileSelector::selector() const
    address = self.uglySide.call('ritual_ZNK16QQmlFileSelector8selectorEv')
    from ..QtCore import QFileSelector
    return QFileSelector._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileSelector)
  @overload(NoneType)
  def setSelector(self, selector: Optional[QFileSelector]) -> None:
    """
    Calls Qt's 'void QQmlFileSelector::setSelector(QFileSelector *selector)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#setSelector

    Parameters
    ----------

    selector : Optional[QFileSelector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlFileSelector::setSelector(QFileSelector *selector)
    self.uglySide.call(
        'ritual_ZN16QQmlFileSelector11setSelectorEP13QFileSelector',
        self._addressOf(selector),
    )

  @overload(QStringList)
  def setExtraSelectors(self, strings: QStringList) -> None:
    """
    Calls Qt's 'void QQmlFileSelector::setExtraSelectors(const QStringList
    &strings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselector.html#setExtraSelectors

    Parameters
    ----------

    strings : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlFileSelector::setExtraSelectors(const QStringList &strings)
    self.uglySide.call(
        'ritual_ZN16QQmlFileSelector17setExtraSelectorsERK5QListI7QStringE',
        self._valueOf(strings),
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

  @overload(QQmlEngine)
  @overload(NoneType)
  @overload(QQmlEngine, QObject)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlFileSelector::QQmlFileSelector(QQmlEngine *engine, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlfileselector.html#QQmlFileSelector

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlFileSelector::QQmlFileSelector(QQmlEngine *engine, QObject
    #      *parent)
    self._noteCreation(QQmlFileSelector, lambda: Rituals.call(
        'ritual_ZN16QQmlFileSelectorC1EP10QQmlEngineP7QObject',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QQmlFileSelectorPrivate]:
    """
    Calls Qt's 'QQmlFileSelectorPrivate *QQmlFileSelector::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlfileselector.html#d_func

    Returns
    -------

    Optional[QQmlFileSelectorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlFileSelectorPrivate *QQmlFileSelector::d_func()
    address = self.uglySide.call('ritual_ZN16QQmlFileSelector6d_funcEv')
    from . import QQmlFileSelectorPrivate
    return QQmlFileSelectorPrivate._cuteAt(address)
