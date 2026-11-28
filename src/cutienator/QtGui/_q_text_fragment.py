"""
QTextFragment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGlyphRun, QTextCharFormat, QTextDocumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocumentPrivate = WAIT['QTextDocumentPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextFragment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextFragment: a plain Python object standing in
  front of one C++ QTextFragment.

  C++ hands a QTextFragment around as a copy, so every C++ QTextFragment
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextFragment that has a ritual and that Python can
  call so far, 11 names in all: 'isValid', '__eq__', '__ne__', '__lt__',
  'position', 'length', 'contains', 'charFormat', 'charFormatIndex', 'text',
  'glyphRuns'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFragment &QTextFragment::operator=(const QTextFragment &o)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QTextFragment::~QTextFragment()': the destructor: Python removes
    its C++ QTextFragment by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextFragment is created at the first use, not by
    'QTextFragment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextFragment back gives a copy the ritual made for
    Python, in a new cute QTextFragment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFragment'

  #  Qt's '~QTextFragment()'. Naming it makes this a value class: Python owns
  #  every C++ QTextFragment behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QTextFragmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextFragment::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#isValid
    """
    #  bool QTextFragment::isValid() const
    return self.uglySide.call('ritual_ZNK13QTextFragment7isValidEv')

  def position(self) -> int:
    """
    Calls Qt's 'int QTextFragment::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#position
    """
    #  int QTextFragment::position() const
    return self.uglySide.call('ritual_ZNK13QTextFragment8positionEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QTextFragment::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#length
    """
    #  int QTextFragment::length() const
    return self.uglySide.call('ritual_ZNK13QTextFragment6lengthEv')

  @overload(int)
  def contains(self, position: int) -> bool:
    """
    Calls Qt's 'bool QTextFragment::contains(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#contains

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  bool QTextFragment::contains(int position) const
    return self.uglySide.call(
        'ritual_ZNK13QTextFragment8containsEi', position,
    )

  def charFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFragment::charFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#charFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFragment::charFormat() const
    address = self.uglySide.call('ritual_ZNK13QTextFragment10charFormatEv')
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def charFormatIndex(self) -> int:
    """
    Calls Qt's 'int QTextFragment::charFormatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#charFormatIndex
    """
    #  int QTextFragment::charFormatIndex() const
    return self.uglySide.call('ritual_ZNK13QTextFragment15charFormatIndexEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QTextFragment::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextFragment::text() const
    return self.uglySide.call('ritual_ZNK13QTextFragment4textEv')

  @overload()
  @overload(int)
  @overload(int, int)
  def glyphRuns(self, from_: int = -1, length: int = -1) -> QList[QGlyphRun]:
    """
    Calls Qt's 'QList<QGlyphRun> QTextFragment::glyphRuns(int from, int
    length) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#glyphRuns

    Parameters
    ----------

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QList[QGlyphRun]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGlyphRun> QTextFragment::glyphRuns(int from, int length) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextFragment9glyphRunsEii', from_, length,
    )
    from . import QGlyphRun
    return QList[QGlyphRun]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, o: QTextFragment) -> bool:
    """
    Calls Qt's 'bool QTextFragment::operator==(const QTextFragment &o)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#operator==

    Parameters
    ----------

    o : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  bool QTextFragment::operator==(const QTextFragment &o) const
    return self.uglySide.call(
        'ritual_ZNK13QTextFragmenteqERKS_', self._valueOf(o),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, o: QTextFragment) -> bool:
    """
    Calls Qt's 'bool QTextFragment::operator!=(const QTextFragment &o)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#operator!=

    Parameters
    ----------

    o : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  bool QTextFragment::operator!=(const QTextFragment &o) const
    return self.uglySide.call(
        'ritual_ZNK13QTextFragmentneERKS_', self._valueOf(o),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, o: QTextFragment) -> bool:
    """
    Calls Qt's 'bool QTextFragment::operator<(const QTextFragment &o) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#operator<

    Parameters
    ----------

    o : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  bool QTextFragment::operator<(const QTextFragment &o) const
    return self.uglySide.call(
        'ritual_ZNK13QTextFragmentltERKS_', self._valueOf(o),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocumentPrivate, int, int)
  @overload(NoneType, int, int)
  def __init__(
      self,
      priv: Optional[QTextDocumentPrivate],
      f: int,
      fe: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextFragment::QTextFragment(const
    QTextDocumentPrivate *priv, int f, int fe)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#QTextFragment

    Parameters
    ----------

    priv : Optional[QTextDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : int
      Passed on as it is.

    fe : int
      Passed on as it is.
    """
    #  QTextFragment::QTextFragment(const QTextDocumentPrivate *priv, int f,
    #      int fe)
    self._noteCreation(QTextFragment, lambda: Rituals.call(
        'ritual_ZN13QTextFragmentC1EPK20QTextDocumentPrivateii',
        self._addressOf(priv), f, fe,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextFragment::QTextFragment()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#QTextFragment
    """
    #  QTextFragment::QTextFragment()
    self._noteCreation(QTextFragment, lambda: Rituals.call(
        'ritual_ZN13QTextFragmentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QTextFragment) -> None:
    """
    Notes what was given, for Qt's 'QTextFragment::QTextFragment(const
    QTextFragment &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#QTextFragment

    Parameters
    ----------

    o : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  QTextFragment::QTextFragment(const QTextFragment &o)
    self._noteCreation(QTextFragment, lambda: Rituals.call(
        'ritual_ZN13QTextFragmentC1ERKS_', self._valueOf(o),
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
