"""
QPdfLink binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdflink.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QPointF, QRectF, QUrl
  from . import QPdfLinkPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfLinkPrivate = WAIT['QPdfLinkPrivate']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfLink(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfLink: a plain Python object standing in front of
  one C++ QPdfLink.

  C++ hands a QPdfLink around as a copy, so every C++ QPdfLink behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdfLink that has a ritual and that Python can call
  so far, 10 names in all: 'isValid', 'page', 'location', 'zoom', 'url',
  'contextBefore', 'contextAfter', 'rectangles', 'toString',
  'copyToClipboard'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfLink::~QPdfLink()': the destructor: Python removes its C++
    QPdfLink by it, and has no other use for it.
  - Qt's 'QPdfLink &QPdfLink::operator=(const QPdfLink &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QPdfLink::QPdfLink(QPdfLink &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QPdfLink &QPdfLink::operator=(QPdfLink &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QPdfLink::swap(QPdfLink &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPdfLink is created at the first use, not by 'QPdfLink(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfLink back gives a copy the ritual made for
    Python, in a new cute QPdfLink.
  - Each name of Qt's QPdfLink that has no cute function yet, 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfLink'

  #  Qt's '~QPdfLink()'. Naming it makes this a value class: Python owns
  #  every C++ QPdfLink behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QPdfLinkD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPdfLink::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#isValid
    """
    #  bool QPdfLink::isValid() const
    return self.uglySide.call('ritual_ZNK8QPdfLink7isValidEv')

  def page(self) -> int:
    """
    Calls Qt's 'int QPdfLink::page() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#page
    """
    #  int QPdfLink::page() const
    return self.uglySide.call('ritual_ZNK8QPdfLink4pageEv')

  def location(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPdfLink::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#location

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPdfLink::location() const
    address = self.uglySide.call('ritual_ZNK8QPdfLink8locationEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def zoom(self) -> float:
    """
    Calls Qt's 'qreal QPdfLink::zoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#zoom
    """
    #  qreal QPdfLink::zoom() const
    return self.uglySide.call('ritual_ZNK8QPdfLink4zoomEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPdfLink::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPdfLink::url() const
    address = self.uglySide.call('ritual_ZNK8QPdfLink3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def contextBefore(self) -> str:
    """
    Calls Qt's 'QString QPdfLink::contextBefore() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#contextBefore

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfLink::contextBefore() const
    return self.uglySide.call('ritual_ZNK8QPdfLink13contextBeforeEv')

  def contextAfter(self) -> str:
    """
    Calls Qt's 'QString QPdfLink::contextAfter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#contextAfter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfLink::contextAfter() const
    return self.uglySide.call('ritual_ZNK8QPdfLink12contextAfterEv')

  def rectangles(self) -> QList[QRectF]:
    """
    Calls Qt's 'QList<QRectF> QPdfLink::rectangles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#rectangles

    Returns
    -------

    QList[QRectF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRectF> QPdfLink::rectangles() const
    address = self.uglySide.call('ritual_ZNK8QPdfLink10rectanglesEv')
    from ..QtCore import QRectF
    return QList[QRectF]._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QPdfLink::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfLink::toString() const
    return self.uglySide.call('ritual_ZNK8QPdfLink8toStringEv')

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfLink::QPdfLink()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#QPdfLink
    """
    #  QPdfLink::QPdfLink()
    self._noteCreation(QPdfLink, lambda: Rituals.call(
        'ritual_ZN8QPdfLinkC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPdfLink) -> None:
    """
    Notes what was given, for Qt's 'QPdfLink::QPdfLink(const QPdfLink
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#QPdfLink

    Parameters
    ----------

    other : QPdfLink
      Passed on as a value: Qt reads the C++ QPdfLink, which stays Python's
      own.
    """
    #  QPdfLink::QPdfLink(const QPdfLink &other)
    self._noteCreation(QPdfLink, lambda: Rituals.call(
        'ritual_ZN8QPdfLinkC1ERKS_', self._valueOf(other),
    ))

  @overload(int, QPointF, float)
  def __init__(self, page: int, location: QPointF, zoom: float) -> None:
    """
    Notes what was given, for Qt's 'QPdfLink::QPdfLink(int page, QPointF
    location, qreal zoom)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#QPdfLink

    Parameters
    ----------

    page : int
      Passed on as it is.

    location : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    zoom : float
      Passed on as it is.
    """
    #  QPdfLink::QPdfLink(int page, QPointF location, qreal zoom)
    self._noteCreation(QPdfLink, lambda: Rituals.call(
        'ritual_ZN8QPdfLinkC1Ei7QPointFd',
        page, self._valueOf(location, 'QPointF'), zoom,
    ))

  @overload(int, QList[QRectF], str, str)
  def __init__(
      self,
      page: int,
      rects: QList[QRectF],
      contextBefore: str,
      contextAfter: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPdfLink::QPdfLink(int page,
    QList<QRectF> rects, QString contextBefore, QString contextAfter)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#QPdfLink

    Parameters
    ----------

    page : int
      Passed on as it is.

    rects : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    contextBefore : str
      Passed on as it is: a QString is made of it for the call.

    contextAfter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPdfLink::QPdfLink(int page, QList<QRectF> rects, QString
    #      contextBefore, QString contextAfter)
    self._noteCreation(QPdfLink, lambda: Rituals.call(
        'ritual_ZN8QPdfLinkC1Ei5QListI6QRectFE7QStringS3_',
        page, self._valueOf(rects), contextBefore, contextAfter,
    ))

  @overload(QPdfLinkPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QPdfLinkPrivate]) -> None:
    """
    Notes what was given, for Qt's 'QPdfLink::QPdfLink(QPdfLinkPrivate *d)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#QPdfLink

    Parameters
    ----------

    d : Optional[QPdfLinkPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfLink::QPdfLink(QPdfLinkPrivate *d)
    self._noteCreation(QPdfLink, lambda: Rituals.call(
        'ritual_ZN8QPdfLinkC1EP15QPdfLinkPrivate', self._addressOf(d),
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
    Calls Qt's 'void QPdfLink::copyToClipboard(QClipboard::Mode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflink.html#copyToClipboard

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QPdfLink::copyToClipboard(QClipboard::Mode mode) const
    self.uglySide.call(
        'ritual_ZNK8QPdfLink15copyToClipboardEN10QClipboard4ModeE',
        mode.value,
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPdfLink::swap(QPdfLink &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPdfLink.swap' has no cute function yet. Qt's 'void "
        "QPdfLink::swap(QPdfLink &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QPdfLink>': the list of QPdfLink, which 'QList[QPdfLink]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QPdfLink.
QList.createKind(
    QPdfLink, 'value',
    make='ritual_list_make_QPdfLink',
    add='ritual_list_add_QPdfLink',
    size='ritual_list_size_QPdfLink',
    at='ritual_list_at_QPdfLink',
    drop='ritual_list_drop_QPdfLink',
)
