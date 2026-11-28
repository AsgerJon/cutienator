"""
QPdfSelection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfselection.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QClipboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QPolygonF
  from . import QPdfSelectionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfSelectionPrivate = WAIT['QPdfSelectionPrivate']
  QPolygonF = WAIT['QPolygonF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfSelection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfSelection: a plain Python object standing in
  front of one C++ QPdfSelection.

  C++ hands a QPdfSelection around as a copy, so every C++ QPdfSelection
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdfSelection that has a ritual and that Python can
  call so far, 7 names in all: 'isValid', 'bounds', 'text',
  'boundingRectangle', 'startIndex', 'endIndex', 'copyToClipboard'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfSelection::~QPdfSelection()': the destructor: Python removes
    its C++ QPdfSelection by it, and has no other use for it.
  - Qt's 'QPdfSelection &QPdfSelection::operator=(const QPdfSelection
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPdfSelection::QPdfSelection(QPdfSelection &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPdfSelection &QPdfSelection::operator=(QPdfSelection &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPdfSelection::swap(QPdfSelection &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPdfSelection is created at the first use, not by
    'QPdfSelection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfSelection back gives a copy the ritual made for
    Python, in a new cute QPdfSelection.
  - Each name of Qt's QPdfSelection that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfSelection'

  #  Qt's '~QPdfSelection()'. Naming it makes this a value class: Python owns
  #  every C++ QPdfSelection behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QPdfSelectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPdfSelection::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#isValid
    """
    #  bool QPdfSelection::isValid() const
    return self.uglySide.call('ritual_ZNK13QPdfSelection7isValidEv')

  def bounds(self) -> QList[QPolygonF]:
    """
    Calls Qt's 'QList<QPolygonF> QPdfSelection::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#bounds

    Returns
    -------

    QList[QPolygonF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPolygonF> QPdfSelection::bounds() const
    address = self.uglySide.call('ritual_ZNK13QPdfSelection6boundsEv')
    from ..QtGui import QPolygonF
    return QList[QPolygonF]._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QPdfSelection::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfSelection::text() const
    return self.uglySide.call('ritual_ZNK13QPdfSelection4textEv')

  def boundingRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPdfSelection::boundingRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfselection.html#boundingRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPdfSelection::boundingRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK13QPdfSelection17boundingRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def startIndex(self) -> int:
    """
    Calls Qt's 'int QPdfSelection::startIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#startIndex
    """
    #  int QPdfSelection::startIndex() const
    return self.uglySide.call('ritual_ZNK13QPdfSelection10startIndexEv')

  def endIndex(self) -> int:
    """
    Calls Qt's 'int QPdfSelection::endIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#endIndex
    """
    #  int QPdfSelection::endIndex() const
    return self.uglySide.call('ritual_ZNK13QPdfSelection8endIndexEv')

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

  @overload(THIS)
  def __init__(self, other: QPdfSelection) -> None:
    """
    Notes what was given, for Qt's 'QPdfSelection::QPdfSelection(const
    QPdfSelection &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#QPdfSelection

    Parameters
    ----------

    other : QPdfSelection
      Passed on as a value: Qt reads the C++ QPdfSelection, which stays
      Python's own.
    """
    #  QPdfSelection::QPdfSelection(const QPdfSelection &other)
    self._noteCreation(QPdfSelection, lambda: Rituals.call(
        'ritual_ZN13QPdfSelectionC1ERKS_', self._valueOf(other),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfSelection::QPdfSelection()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#QPdfSelection
    """
    #  QPdfSelection::QPdfSelection()
    self._noteCreation(QPdfSelection, lambda: Rituals.call(
        'ritual_ZN13QPdfSelectionC1Ev',
    ))

  @overload(str, QList[QPolygonF], QRectF, int, int)
  def __init__(
      self,
      text: str,
      bounds: QList[QPolygonF],
      boundingRect: QRectF,
      startIndex: int,
      endIndex: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPdfSelection::QPdfSelection(const
    QString &text, QList<QPolygonF> bounds, QRectF boundingRect, int
    startIndex, int endIndex)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#QPdfSelection

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    bounds : QList[QPolygonF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    boundingRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    startIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  QPdfSelection::QPdfSelection(const QString &text, QList<QPolygonF>
    #      bounds, QRectF boundingRect, int startIndex, int endIndex)
    self._noteCreation(QPdfSelection, lambda: Rituals.call(
        'ritual_ZN13QPdfSelectionC1ERK7QString5QListI9QPolygonFE6QRectFii',
        text, self._valueOf(bounds), self._valueOf(boundingRect), startIndex,
        endIndex,
    ))

  @overload(QPdfSelectionPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QPdfSelectionPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QPdfSelection::QPdfSelection(QPdfSelectionPrivate *d)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#QPdfSelection

    Parameters
    ----------

    d : Optional[QPdfSelectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfSelection::QPdfSelection(QPdfSelectionPrivate *d)
    self._noteCreation(QPdfSelection, lambda: Rituals.call(
        'ritual_ZN13QPdfSelectionC1EP20QPdfSelectionPrivate',
        self._addressOf(d),
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

  @overload()
  @overload(QClipboard.Mode)
  def copyToClipboard(
      self,
      mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
  ) -> None:
    """
    Calls Qt's 'void QPdfSelection::copyToClipboard(QClipboard::Mode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfselection.html#copyToClipboard

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QPdfSelection::copyToClipboard(QClipboard::Mode mode) const
    self.uglySide.call(
        'ritual_ZNK13QPdfSelection15copyToClipboardEN10QClipboard4ModeE',
        mode.value,
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPdfSelection::swap(QPdfSelection &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPdfSelection.swap' has no cute function yet. Qt's 'void "
        "QPdfSelection::swap(QPdfSelection &other)': takes a type Python "
        "has no way to hand over yet.")
