"""
QPdfPageRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfpagerenderer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QImage
  from . import QPdfDocument, QPdfDocumentRenderOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPdfDocument = WAIT['QPdfDocument']
  QPdfDocumentRenderOptions = WAIT['QPdfDocumentRenderOptions']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfPageRenderer(QObject):
  """
  The cute side of Qt's QPdfPageRenderer: a plain Python object standing in
  front of one C++ QPdfPageRenderer.

  It is built on the cute 'QObject', as Qt's QPdfPageRenderer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfPageRenderer that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'renderMode',
  'setRenderMode', 'document', 'setDocument', 'requestPage',
  'documentChanged', 'renderModeChanged', 'pageRendered'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfPageRenderer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPdfPageRenderer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfPageRenderer::~QPdfPageRenderer()': the destructor: Python
    never removes a C++ QPdfPageRenderer.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfPageRenderer is created at the first use, not by
    'QPdfPageRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfPageRenderer.
  - Qt tells when it has removed the C++ QPdfPageRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfPageRenderer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RenderMode(CuteNum, scoped=True):
    """
    The enum 'QPdfPageRenderer::RenderMode' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    MultiThreaded = Kee[int](0)
    SingleThreaded = Kee[int](1)

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
    Calls Qt's 'QString QPdfPageRenderer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#tr

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
    #  QString QPdfPageRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPdfPageRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfPageRenderer'

  #  A C++ QPdfPageRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfPageRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfPageRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfPageRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPdfPageRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderMode(self) -> RenderMode:
    """
    Calls Qt's 'RenderMode QPdfPageRenderer::renderMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#renderMode

    Returns
    -------

    RenderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderMode(number)'
      gives.
    """
    #  RenderMode QPdfPageRenderer::renderMode() const
    return QPdfPageRenderer.RenderMode(self.uglySide.call(
        'ritual_ZNK16QPdfPageRenderer10renderModeEv',
    ))

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfPageRenderer::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfPageRenderer::document() const
    address = self.uglySide.call('ritual_ZNK16QPdfPageRenderer8documentEv')
    from . import QPdfDocument
    return QPdfDocument._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RenderMode)
  def setRenderMode(self, mode: RenderMode) -> None:
    """
    Calls Qt's 'void QPdfPageRenderer::setRenderMode(RenderMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagerenderer.html#setRenderMode

    Parameters
    ----------

    mode : RenderMode
      Passed on as its number.
    """
    #  void QPdfPageRenderer::setRenderMode(RenderMode mode)
    self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer13setRenderModeENS_10RenderModeE',
        mode.value,
    )

  @overload(QPdfDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfPageRenderer::setDocument(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#setDocument

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfPageRenderer::setDocument(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer11setDocumentEP12QPdfDocument',
        self._addressOf(document),
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
    Notes what was given, for Qt's 'QPdfPageRenderer::QPdfPageRenderer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagerenderer.html#QPdfPageRenderer
    """
    #  QPdfPageRenderer::QPdfPageRenderer()
    self._noteCreation(QPdfPageRenderer, lambda: Rituals.call(
        'ritual_ZN16QPdfPageRendererC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QPdfPageRenderer::QPdfPageRenderer(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagerenderer.html#QPdfPageRenderer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfPageRenderer::QPdfPageRenderer(QObject *parent)
    self._noteCreation(QPdfPageRenderer, lambda: Rituals.call(
        'ritual_ZN16QPdfPageRendererC1EP7QObject',
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

  @overload(int, QSize)
  @overload(int, QSize, QPdfDocumentRenderOptions)
  def requestPage(
      self,
      pageNumber: int,
      imageSize: QSize,
      options: Optional[QPdfDocumentRenderOptions] = None,
  ) -> int:
    """
    Calls Qt's 'quint64 QPdfPageRenderer::requestPage(int pageNumber, QSize
    imageSize, QPdfDocumentRenderOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#requestPage

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : Optional[QPdfDocumentRenderOptions]
      Passed on as a value: Qt reads the C++ QPdfDocumentRenderOptions, which
      stays Python's own. May be left out, as in Qt: a new
      'QPdfDocumentRenderOptions()' is then passed on.
    """
    #  quint64 QPdfPageRenderer::requestPage(int pageNumber, QSize imageSize,
    #      QPdfDocumentRenderOptions options)
    if options is None:
      from . import QPdfDocumentRenderOptions
      options = QPdfDocumentRenderOptions()
    return self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer11requestPageEi5QSize25QPdfDocumentRend'
        'erOptions',
        pageNumber, self._valueOf(imageSize), self._valueOf(options),
    )

  @overload(QPdfDocument)
  @overload(NoneType)
  def documentChanged(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfPageRenderer::documentChanged(QPdfDocument
    *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagerenderer.html#documentChanged

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfPageRenderer::documentChanged(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer15documentChangedEP12QPdfDocument',
        self._addressOf(document),
    )

  @overload(RenderMode)
  def renderModeChanged(self, renderMode: RenderMode) -> None:
    """
    Calls Qt's 'void
    QPdfPageRenderer::renderModeChanged(QPdfPageRenderer::RenderMode
    renderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagerenderer.html#renderModeChanged

    Parameters
    ----------

    renderMode : RenderMode
      Passed on as its number.
    """
    #  void QPdfPageRenderer::renderModeChanged(QPdfPageRenderer::RenderMode
    #      renderMode)
    self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer17renderModeChangedENS_10RenderModeE',
        renderMode.value,
    )

  @overload(int, QSize, QImage, QPdfDocumentRenderOptions, int)
  def pageRendered(
      self,
      pageNumber: int,
      imageSize: QSize,
      image: QImage,
      options: QPdfDocumentRenderOptions,
      requestId: int,
  ) -> None:
    """
    Calls Qt's 'void QPdfPageRenderer::pageRendered(int pageNumber, QSize
    imageSize, const QImage &image, QPdfDocumentRenderOptions options,
    quint64 requestId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagerenderer.html#pageRendered

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    options : QPdfDocumentRenderOptions
      Passed on as a value: Qt reads the C++ QPdfDocumentRenderOptions, which
      stays Python's own.

    requestId : int
      Passed on as it is.
    """
    #  void QPdfPageRenderer::pageRendered(int pageNumber, QSize imageSize,
    #      const QImage &image, QPdfDocumentRenderOptions options, quint64
    #      requestId)
    self.uglySide.call(
        'ritual_ZN16QPdfPageRenderer12pageRenderedEi5QSizeRK6QImage25QPdfDo'
        'cumentRenderOptionsy',
        pageNumber, self._valueOf(imageSize), self._valueOf(image),
        self._valueOf(options), requestId,
    )
