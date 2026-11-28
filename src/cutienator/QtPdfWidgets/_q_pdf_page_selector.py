"""
QPdfPageSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdfWidgets/qpdfpageselector.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtPdf import QPdfDocument
  from . import QPdfPageSelectorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfDocument = WAIT['QPdfDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfPageSelector(QWidget):
  """
  The cute side of Qt's QPdfPageSelector: a plain Python object standing in
  front of one C++ QPdfPageSelector.

  It is built on the cute 'QWidget', as Qt's QPdfPageSelector is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfPageSelector that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'setDocument',
  'document', 'currentPage', 'currentPageLabel', 'setCurrentPage',
  'documentChanged', 'currentPageChanged', 'currentPageLabelChanged',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfPageSelector::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPdfPageSelector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfPageSelector::~QPdfPageSelector()': the destructor: Python
    never removes a C++ QPdfPageSelector.
  - Qt's 'const QPdfPageSelectorPrivate *QPdfPageSelector::d_func() const':
    takes in Python what 'QPdfPageSelectorPrivate
    *QPdfPageSelector::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfPageSelector is created at the first use, not by
    'QPdfPageSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfPageSelector.
  - Qt tells when it has removed the C++ QPdfPageSelector. Every call on the
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
    Calls Qt's 'QString QPdfPageSelector::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#tr

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
    #  QString QPdfPageSelector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPdfPageSelector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfPageSelector'

  #  A C++ QPdfPageSelector Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfPageSelector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfPageSelector::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfPageSelector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPdfPageSelector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfPageSelector::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfPageSelector::document() const
    address = self.uglySide.call('ritual_ZNK16QPdfPageSelector8documentEv')
    from ..QtPdf import QPdfDocument
    return QPdfDocument._cuteAt(address)

  def currentPage(self) -> int:
    """
    Calls Qt's 'int QPdfPageSelector::currentPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#currentPage
    """
    #  int QPdfPageSelector::currentPage() const
    return self.uglySide.call('ritual_ZNK16QPdfPageSelector11currentPageEv')

  def currentPageLabel(self) -> str:
    """
    Calls Qt's 'QString QPdfPageSelector::currentPageLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#currentPageLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfPageSelector::currentPageLabel() const
    return self.uglySide.call(
        'ritual_ZNK16QPdfPageSelector16currentPageLabelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPdfDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfPageSelector::setDocument(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#setDocument

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfPageSelector::setDocument(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN16QPdfPageSelector11setDocumentEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(int)
  def setCurrentPage(self, index: int) -> None:
    """
    Calls Qt's 'void QPdfPageSelector::setCurrentPage(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#setCurrentPage

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QPdfPageSelector::setCurrentPage(int index)
    self.uglySide.call(
        'ritual_ZN16QPdfPageSelector14setCurrentPageEi', index,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfPageSelector::QPdfPageSelector()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#QPdfPageSelector
    """
    #  QPdfPageSelector::QPdfPageSelector()
    self._noteCreation(QPdfPageSelector, lambda: Rituals.call(
        'ritual_ZN16QPdfPageSelectorC1Ev',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QPdfPageSelector::QPdfPageSelector(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#QPdfPageSelector

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfPageSelector::QPdfPageSelector(QWidget *parent)
    self._noteCreation(QPdfPageSelector, lambda: Rituals.call(
        'ritual_ZN16QPdfPageSelectorC1EP7QWidget', self._addressOf(parent),
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

  @overload(QPdfDocument)
  @overload(NoneType)
  def documentChanged(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfPageSelector::documentChanged(QPdfDocument
    *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#documentChanged

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfPageSelector::documentChanged(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN16QPdfPageSelector15documentChangedEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(int)
  def currentPageChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QPdfPageSelector::currentPageChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#currentPageChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QPdfPageSelector::currentPageChanged(int index)
    self.uglySide.call(
        'ritual_ZN16QPdfPageSelector18currentPageChangedEi', index,
    )

  @overload(str)
  def currentPageLabelChanged(self, label: str) -> None:
    """
    Calls Qt's 'void QPdfPageSelector::currentPageLabelChanged(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpageselector.html#currentPageLabelChanged

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfPageSelector::currentPageLabelChanged(const QString &label)
    self.uglySide.call(
        'ritual_ZN16QPdfPageSelector23currentPageLabelChangedERK7QString',
        label,
    )

  def d_func(self) -> Optional[QPdfPageSelectorPrivate]:
    """
    Calls Qt's 'QPdfPageSelectorPrivate *QPdfPageSelector::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpageselector.html#d_func

    Returns
    -------

    Optional[QPdfPageSelectorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfPageSelectorPrivate *QPdfPageSelector::d_func()
    address = self.uglySide.call('ritual_ZN16QPdfPageSelector6d_funcEv')
    from . import QPdfPageSelectorPrivate
    return QPdfPageSelectorPrivate._cuteAt(address)
