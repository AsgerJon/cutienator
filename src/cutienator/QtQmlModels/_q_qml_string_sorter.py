"""
QQmlStringSorter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlstringsorter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlStringSorter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQmlRoleSorter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QModelIndex, QPartialOrdering
  from . import QQmlSortFilterProxyModel, QQmlStringSorterPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QModelIndex = WAIT['QModelIndex']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlStringSorter(QQmlRoleSorter):
  """
  The cute side of Qt's QQmlStringSorter: a plain Python object standing in
  front of one C++ QQmlStringSorter.

  It is built on the cute 'QQmlRoleSorter', as Qt's QQmlStringSorter is built
  on Qt's QQmlRoleSorter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlStringSorter that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'caseSensitivity',
  'setCaseSensitivity', 'ignorePunctuation', 'setIgnorePunctuation',
  'locale', 'setLocale', 'numericMode', 'setNumericMode', 'compare',
  'caseSensitivityChanged', 'ignorePunctuationChanged', 'localeChanged',
  'numericModeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlStringSorter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlStringSorter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlStringSorter::~QQmlStringSorter()': the destructor: Python
    never removes a C++ QQmlStringSorter.
  - Qt's 'const QQmlStringSorterPrivate *QQmlStringSorter::d_func() const':
    takes in Python what 'QQmlStringSorterPrivate
    *QQmlStringSorter::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlStringSorter is created at the first use, not by
    'QQmlStringSorter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlStringSorter.
  - Qt tells when it has removed the C++ QQmlStringSorter. Every call on the
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
    Calls Qt's 'QString QQmlStringSorter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#tr

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
    #  QString QQmlStringSorter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlStringSorter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlStringSorter'

  #  A C++ QQmlStringSorter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlStringSorter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlStringSorter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlStringSorter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlStringSorter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QQmlStringSorter::caseSensitivity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QQmlStringSorter::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK16QQmlStringSorter15caseSensitivityEv',
    ))

  def ignorePunctuation(self) -> bool:
    """
    Calls Qt's 'bool QQmlStringSorter::ignorePunctuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#ignorePunctuation
    """
    #  bool QQmlStringSorter::ignorePunctuation() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlStringSorter17ignorePunctuationEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQmlStringSorter::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQmlStringSorter::locale() const
    address = self.uglySide.call('ritual_ZNK16QQmlStringSorter6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def numericMode(self) -> bool:
    """
    Calls Qt's 'bool QQmlStringSorter::numericMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#numericMode
    """
    #  bool QQmlStringSorter::numericMode() const
    return self.uglySide.call('ritual_ZNK16QQmlStringSorter11numericModeEv')

  @overload(QModelIndex, QModelIndex, QQmlSortFilterProxyModel)
  @overload(QModelIndex, QModelIndex, NoneType)
  def compare(
      self,
      sourceLeft: QModelIndex,
      sourceRight: QModelIndex,
      proxyModel: Optional[QQmlSortFilterProxyModel],
  ) -> QPartialOrdering:
    """
    Calls Qt's 'QPartialOrdering QQmlStringSorter::compare(const QModelIndex
    &sourceLeft, const QModelIndex &sourceRight, const
    QQmlSortFilterProxyModel *proxyModel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#compare

    Parameters
    ----------

    sourceLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    proxyModel : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPartialOrdering
      A new cute QPartialOrdering around the copy Qt gave back. Python owns
      it.
    """
    #  QPartialOrdering QQmlStringSorter::compare(const QModelIndex
    #      &sourceLeft, const QModelIndex &sourceRight, const
    #      QQmlSortFilterProxyModel *proxyModel) const
    ritual = (
        'ritual_ZNK16QQmlStringSorter7compareERK11QModelIndexS2_PK24QQmlSor'
        'tFilterProxyModel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QQmlStringSorter7compareERK11QModelIndexS2_PK24Q'
          'QmlSortFilterProxyModel')
    address = self.uglySide.call(
        ritual,
        self._valueOf(sourceLeft), self._valueOf(sourceRight),
        self._addressOf(proxyModel),
    )
    from ..QtCore import QPartialOrdering
    return QPartialOrdering._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, caseSensitivity: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::setCaseSensitivity(Qt::CaseSensitivity
    caseSensitivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#setCaseSensitivity

    Parameters
    ----------

    caseSensitivity : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QQmlStringSorter::setCaseSensitivity(Qt::CaseSensitivity
    #      caseSensitivity)
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter18setCaseSensitivityEN2Qt15CaseSensitiv'
        'ityE',
        caseSensitivity.value,
    )

  @overload(bool)
  def setIgnorePunctuation(self, ignorePunctation: bool) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::setIgnorePunctuation(bool
    ignorePunctation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#setIgnorePunctuation

    Parameters
    ----------

    ignorePunctation : bool
      Passed on as it is.
    """
    #  void QQmlStringSorter::setIgnorePunctuation(bool ignorePunctation)
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter20setIgnorePunctuationEb',
        ignorePunctation,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQmlStringSorter::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(bool)
  def setNumericMode(self, numericMode: bool) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::setNumericMode(bool numericMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#setNumericMode

    Parameters
    ----------

    numericMode : bool
      Passed on as it is.
    """
    #  void QQmlStringSorter::setNumericMode(bool numericMode)
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter14setNumericModeEb', numericMode,
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
    'QQmlStringSorter::QQmlStringSorter(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#QQmlStringSorter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlStringSorter::QQmlStringSorter(QObject *parent)
    self._noteCreation(QQmlStringSorter, lambda: Rituals.call(
        'ritual_ZN16QQmlStringSorterC1EP7QObject',
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

  def caseSensitivityChanged(self) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::caseSensitivityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#caseSensitivityChanged
    """
    #  void QQmlStringSorter::caseSensitivityChanged()
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter22caseSensitivityChangedEv',
    )

  def ignorePunctuationChanged(self) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::ignorePunctuationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#ignorePunctuationChanged
    """
    #  void QQmlStringSorter::ignorePunctuationChanged()
    self.uglySide.call(
        'ritual_ZN16QQmlStringSorter24ignorePunctuationChangedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#localeChanged
    """
    #  void QQmlStringSorter::localeChanged()
    self.uglySide.call('ritual_ZN16QQmlStringSorter13localeChangedEv')

  def numericModeChanged(self) -> None:
    """
    Calls Qt's 'void QQmlStringSorter::numericModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstringsorter.html#numericModeChanged
    """
    #  void QQmlStringSorter::numericModeChanged()
    self.uglySide.call('ritual_ZN16QQmlStringSorter18numericModeChangedEv')

  def d_func(self) -> Optional[QQmlStringSorterPrivate]:
    """
    Calls Qt's 'QQmlStringSorterPrivate *QQmlStringSorter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstringsorter.html#d_func

    Returns
    -------

    Optional[QQmlStringSorterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlStringSorterPrivate *QQmlStringSorter::d_func()
    address = self.uglySide.call('ritual_ZN16QQmlStringSorter6d_funcEv')
    from . import QQmlStringSorterPrivate
    return QQmlStringSorterPrivate._cuteAt(address)
