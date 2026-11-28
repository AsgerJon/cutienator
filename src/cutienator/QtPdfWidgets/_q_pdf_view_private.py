"""
QPdfViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPdfViewPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtPdf import QPdfDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRect, QSize
  from ..QtGui import QImage, QTransform
  from ..QtPdf import QPdfLink
  from . import QPdfView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPdfView = WAIT['QPdfView']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfViewPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfViewPrivate: a plain Python object standing in
  front of one C++ QPdfViewPrivate.

  What exists
  -----------

  Every function of Qt's QPdfViewPrivate that has a ritual and that Python
  can call so far, 16 names in all: 'q_func', 'init',
  'documentStatusChanged', 'currentPageChanged', 'currentZoomChanged',
  'calculateViewport', 'setViewport', 'updateScrollBars', 'pageRendered',
  'invalidateDocumentLayout', 'invalidatePageCache', 'yPositionForPage',
  'pagePosition', 'screenScaleTransform', 'calculateDocumentLayout',
  'updateDocumentLayout'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPdfView *QPdfViewPrivate::q_func() const': takes in Python
    what 'QPdfView *QPdfViewPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPdfViewPrivate is created at the first use, not by
    'QPdfViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfViewPrivate.
  - Each name of Qt's QPdfViewPrivate that has no cute function yet,
    'scrollTo', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QPdfViewPrivate, each a class in here as in
  #  C++.

  class DocumentLayout(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPdfViewPrivate::DocumentLayout: a plain Python
    object standing in front of one C++ QPdfViewPrivate::DocumentLayout.

    C++ hands a QPdfViewPrivate::DocumentLayout around as a copy, so every
    C++ QPdfViewPrivate::DocumentLayout behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QPdfViewPrivate::DocumentLayout yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPdfViewPrivate::DocumentLayout::~DocumentLayout()': the
      destructor: Python removes its C++ QPdfViewPrivate::DocumentLayout by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QPdfViewPrivate::DocumentLayout is created at the first use,
      not by 'QPdfViewPrivate::DocumentLayout(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPdfViewPrivate::DocumentLayout back gives a copy
      the ritual made for Python, in a new cute
      QPdfViewPrivate::DocumentLayout.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPdfViewPrivate::DocumentLayout'

    #  Qt's '~QPdfViewPrivate::DocumentLayout()'. Naming it makes this a
    #  value class: Python owns every C++ QPdfViewPrivate::DocumentLayout
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QPdfViewPrivate14DocumentLayoutD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def yPositionForPage(self, page: int) -> float:
    """
    Calls Qt's 'qreal QPdfViewPrivate::yPositionForPage(int page) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#yPositionForPage

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  qreal QPdfViewPrivate::yPositionForPage(int page) const
    return self.uglySide.call(
        'ritual_ZNK15QPdfViewPrivate16yPositionForPageEi', page,
    )

  @overload(int)
  def screenScaleTransform(self, page: int) -> QTransform:
    """
    Calls Qt's 'QTransform QPdfViewPrivate::screenScaleTransform(int page)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#screenScaleTransform

    Parameters
    ----------

    page : int
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPdfViewPrivate::screenScaleTransform(int page) const
    address = self.uglySide.call(
        'ritual_ZNK15QPdfViewPrivate20screenScaleTransformEi', page,
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def calculateDocumentLayout(self) -> DocumentLayout:
    """
    Calls Qt's 'DocumentLayout QPdfViewPrivate::calculateDocumentLayout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#calculateDocumentLayout

    Returns
    -------

    DocumentLayout
      A new cute QPdfViewPrivate::DocumentLayout around the copy Qt gave
      back. Python owns it.
    """
    #  DocumentLayout QPdfViewPrivate::calculateDocumentLayout() const
    address = self.uglySide.call(
        'ritual_ZNK15QPdfViewPrivate23calculateDocumentLayoutEv',
    )
    return QPdfViewPrivate.DocumentLayout._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setViewport(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::setViewport(QRect viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfviewprivate.html#setViewport

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPdfViewPrivate::setViewport(QRect viewport)
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate11setViewportE5QRect',
        self._valueOf(viewport),
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

  @overload(QPdfView)
  @overload(NoneType)
  def __init__(self, q: Optional[QPdfView]) -> None:
    """
    Notes what was given, for Qt's 'QPdfViewPrivate::QPdfViewPrivate(QPdfView
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#QPdfViewPrivate

    Parameters
    ----------

    q : Optional[QPdfView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfViewPrivate::QPdfViewPrivate(QPdfView *q)
    self._noteCreation(QPdfViewPrivate, lambda: Rituals.call(
        'ritual_ZN15QPdfViewPrivateC1EP8QPdfView', self._addressOf(q),
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

  def q_func(self) -> Optional[QPdfView]:
    """
    Calls Qt's 'QPdfView *QPdfViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfviewprivate.html#q_func

    Returns
    -------

    Optional[QPdfView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfView *QPdfViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QPdfViewPrivate6q_funcEv')
    from . import QPdfView
    return QPdfView._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfviewprivate.html#init
    """
    #  void QPdfViewPrivate::init()
    self.uglySide.call('ritual_ZN15QPdfViewPrivate4initEv')

  @overload(QPdfDocument.Status)
  def documentStatusChanged(self, status: QPdfDocument.Status) -> None:
    """
    Calls Qt's 'void
    QPdfViewPrivate::documentStatusChanged(QPdfDocument::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#documentStatusChanged

    Parameters
    ----------

    status : QPdfDocument.Status
      Passed on as its number.
    """
    #  void QPdfViewPrivate::documentStatusChanged(QPdfDocument::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate21documentStatusChangedEN12QPdfDocument6'
        'StatusE',
        status.value,
    )

  @overload(int)
  def currentPageChanged(self, currentPage: int) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::currentPageChanged(int currentPage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#currentPageChanged

    Parameters
    ----------

    currentPage : int
      Passed on as it is.
    """
    #  void QPdfViewPrivate::currentPageChanged(int currentPage)
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate18currentPageChangedEi', currentPage,
    )

  @overload(float)
  def currentZoomChanged(self, currentZoom: float) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::currentZoomChanged(qreal currentZoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#currentZoomChanged

    Parameters
    ----------

    currentZoom : float
      Passed on as it is.
    """
    #  void QPdfViewPrivate::currentZoomChanged(qreal currentZoom)
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate18currentZoomChangedEd', currentZoom,
    )

  def calculateViewport(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::calculateViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#calculateViewport
    """
    #  void QPdfViewPrivate::calculateViewport()
    self.uglySide.call('ritual_ZN15QPdfViewPrivate17calculateViewportEv')

  def updateScrollBars(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::updateScrollBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#updateScrollBars
    """
    #  void QPdfViewPrivate::updateScrollBars()
    self.uglySide.call('ritual_ZN15QPdfViewPrivate16updateScrollBarsEv')

  @overload(int, QSize, QImage, int)
  def pageRendered(
      self,
      pageNumber: int,
      imageSize: QSize,
      image: QImage,
      requestId: int,
  ) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::pageRendered(int pageNumber, QSize
    imageSize, const QImage &image, quint64 requestId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfviewprivate.html#pageRendered

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    requestId : int
      Passed on as it is.
    """
    #  void QPdfViewPrivate::pageRendered(int pageNumber, QSize imageSize,
    #      const QImage &image, quint64 requestId)
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate12pageRenderedEi5QSizeRK6QImagey',
        pageNumber, self._valueOf(imageSize), self._valueOf(image),
        requestId,
    )

  def invalidateDocumentLayout(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::invalidateDocumentLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#invalidateDocumentLayout
    """
    #  void QPdfViewPrivate::invalidateDocumentLayout()
    self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate24invalidateDocumentLayoutEv',
    )

  def invalidatePageCache(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::invalidatePageCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#invalidatePageCache
    """
    #  void QPdfViewPrivate::invalidatePageCache()
    self.uglySide.call('ritual_ZN15QPdfViewPrivate19invalidatePageCacheEv')

  @overload(QPointF)
  def pagePosition(self, viewPosition: QPointF) -> QPdfLink:
    """
    Calls Qt's 'QPdfLink QPdfViewPrivate::pagePosition(const QPointF
    &viewPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfviewprivate.html#pagePosition

    Parameters
    ----------

    viewPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPdfLink
      A new cute QPdfLink around the copy Qt gave back. Python owns it.
    """
    #  QPdfLink QPdfViewPrivate::pagePosition(const QPointF &viewPosition)
    address = self.uglySide.call(
        'ritual_ZN15QPdfViewPrivate12pagePositionERK7QPointF',
        self._valueOf(viewPosition, 'QPointF'),
    )
    from ..QtPdf import QPdfLink
    return QPdfLink._cuteOwning(address)

  def updateDocumentLayout(self) -> None:
    """
    Calls Qt's 'void QPdfViewPrivate::updateDocumentLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfviewprivate.html#updateDocumentLayout
    """
    #  void QPdfViewPrivate::updateDocumentLayout()
    self.uglySide.call('ritual_ZN15QPdfViewPrivate20updateDocumentLayoutEv')

  @staticmethod
  def scrollTo(*__, **_) -> Never:
    """
    Qt's 'void QPdfViewPrivate::scrollTo(const QPdfLink &link)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'qLcWLink'.
    """
    raise NotImplementedError(
        "'QPdfViewPrivate.scrollTo' has no cute function yet. Qt's 'void "
        "QPdfViewPrivate::scrollTo(const QPdfLink &link)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qLcWLink'.")
