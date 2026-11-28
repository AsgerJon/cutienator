"""
QWebEngineContextMenuRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginecontextmenurequest.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QtWebEngineCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QUrl
  from . import QWebEngineContextMenuRequestPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineContextMenuRequestPrivate = WAIT['QWebEngineContextMenuRequestPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineContextMenuRequest(QObject):
  """
  The cute side of Qt's QWebEngineContextMenuRequest: a plain Python object
  standing in front of one C++ QWebEngineContextMenuRequest.

  It is built on the cute 'QObject', as Qt's QWebEngineContextMenuRequest is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineContextMenuRequest that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'tr',
  'position', 'selectedText', 'linkText', 'linkUrl', 'mediaUrl', 'mediaType',
  'isContentEditable', 'misspelledWord', 'spellCheckerSuggestions',
  'isAccepted', 'setAccepted', 'mediaFlags', 'editFlags', 'filteredLinkUrl',
  'altText', 'titleText', 'referrerUrl', 'referrerPolicy', 'hasImageContent',
  'suggestedFileName'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineContextMenuRequest::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWebEngineContextMenuRequest::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineContextMenuRequest::~QWebEngineContextMenuRequest()': the
    destructor: Python never removes a C++ QWebEngineContextMenuRequest.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineContextMenuRequest is created at the first use, not by
    'QWebEngineContextMenuRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineContextMenuRequest.
  - Qt tells when it has removed the C++ QWebEngineContextMenuRequest. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWebEngineContextMenuRequest, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class EditFlag(CuteFlags):
    """
    The flags enum 'QWebEngineContextMenuRequest::EditFlag' of Qt, with the 9
    names Qt gives in it. Qt names the type of its combinations
    'QWebEngineContextMenuRequest::EditFlags'.
    """

    CanUndo = 0x1
    CanRedo = 0x2
    CanCut = 0x4
    CanCopy = 0x8
    CanPaste = 0x10
    CanDelete = 0x20
    CanSelectAll = 0x40
    CanTranslate = 0x80
    CanEditRichly = 0x100

  EditFlags = EditFlag

  class MediaFlag(CuteFlags):
    """
    The flags enum 'QWebEngineContextMenuRequest::MediaFlag' of Qt, with the
    10 names Qt gives in it. Qt names the type of its combinations
    'QWebEngineContextMenuRequest::MediaFlags'.
    """

    MediaInError = 0x1
    MediaPaused = 0x2
    MediaMuted = 0x4
    MediaLoop = 0x8
    MediaCanSave = 0x10
    MediaHasAudio = 0x20
    MediaCanToggleControls = 0x40
    MediaControls = 0x80
    MediaCanPrint = 0x100
    MediaCanRotate = 0x200

  MediaFlags = MediaFlag

  class MediaType(CuteNum):
    """
    The enum 'QWebEngineContextMenuRequest::MediaType' of Qt, with the 7
    names Qt gives in it.
    """

    MediaTypeNone = Kee[int](0)
    MediaTypeImage = Kee[int](1)
    MediaTypeVideo = Kee[int](2)
    MediaTypeAudio = Kee[int](3)
    MediaTypeCanvas = Kee[int](4)
    MediaTypeFile = Kee[int](5)
    MediaTypePlugin = Kee[int](6)

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
    Calls Qt's 'QString QWebEngineContextMenuRequest::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#tr

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
    #  QString QWebEngineContextMenuRequest::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QWebEngineContextMenuRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineContextMenuRequest'

  #  A C++ QWebEngineContextMenuRequest Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineContextMenuRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineContextMenuRequest::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineContextMenuRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWebEngineContextMenuRequest::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWebEngineContextMenuRequest::position() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest8positionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::selectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::selectedText() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest12selectedTextEv',
    )

  def linkText(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::linkText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#linkText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::linkText() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest8linkTextEv',
    )

  def linkUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineContextMenuRequest::linkUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#linkUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineContextMenuRequest::linkUrl() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest7linkUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def mediaUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineContextMenuRequest::mediaUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#mediaUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineContextMenuRequest::mediaUrl() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest8mediaUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def mediaType(self) -> MediaType:
    """
    Calls Qt's 'MediaType QWebEngineContextMenuRequest::mediaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#mediaType

    Returns
    -------

    MediaType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MediaType(number)' gives.
    """
    #  MediaType QWebEngineContextMenuRequest::mediaType() const
    return QWebEngineContextMenuRequest.MediaType(self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest9mediaTypeEv',
    ))

  def isContentEditable(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineContextMenuRequest::isContentEditable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html
    """
    #  bool QWebEngineContextMenuRequest::isContentEditable() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest17isContentEditableEv',
    )

  def misspelledWord(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::misspelledWord()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#misspelledWord

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::misspelledWord() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest14misspelledWordEv',
    )

  def spellCheckerSuggestions(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QWebEngineContextMenuRequest::spellCheckerSuggestions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebEngineContextMenuRequest::spellCheckerSuggestions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest23spellCheckerSuggestionsE'
        'v',
    )
    return QStringList._cuteOwning(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineContextMenuRequest::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#isAccepted
    """
    #  bool QWebEngineContextMenuRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest10isAcceptedEv',
    )

  def mediaFlags(self) -> MediaFlags:
    """
    Calls Qt's 'MediaFlags QWebEngineContextMenuRequest::mediaFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#mediaFlags

    Returns
    -------

    MediaFlags
      The value standing for the combination Qt gave back.
    """
    #  MediaFlags QWebEngineContextMenuRequest::mediaFlags() const
    return QWebEngineContextMenuRequest.MediaFlags(self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest10mediaFlagsEv',
    ))

  def editFlags(self) -> EditFlags:
    """
    Calls Qt's 'EditFlags QWebEngineContextMenuRequest::editFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#editFlags

    Returns
    -------

    EditFlags
      The value standing for the combination Qt gave back.
    """
    #  EditFlags QWebEngineContextMenuRequest::editFlags() const
    return QWebEngineContextMenuRequest.EditFlags(self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest9editFlagsEv',
    ))

  def filteredLinkUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineContextMenuRequest::filteredLinkUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#filteredLinkUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineContextMenuRequest::filteredLinkUrl() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest15filteredLinkUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def altText(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::altText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#altText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::altText() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest7altTextEv',
    )

  def titleText(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::titleText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#titleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::titleText() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest9titleTextEv',
    )

  def referrerUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineContextMenuRequest::referrerUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#referrerUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineContextMenuRequest::referrerUrl() const
    address = self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest11referrerUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def referrerPolicy(self) -> QtWebEngineCore.ReferrerPolicy:
    """
    Calls Qt's 'QtWebEngineCore::ReferrerPolicy
    QWebEngineContextMenuRequest::referrerPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#referrerPolicy

    Returns
    -------

    QtWebEngineCore.ReferrerPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtWebEngineCore.ReferrerPolicy(number)' gives.
    """
    #  QtWebEngineCore::ReferrerPolicy
    #      QWebEngineContextMenuRequest::referrerPolicy() const
    return QtWebEngineCore.ReferrerPolicy(self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest14referrerPolicyEv',
    ))

  def hasImageContent(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineContextMenuRequest::hasImageContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#hasImageContent
    """
    #  bool QWebEngineContextMenuRequest::hasImageContent() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest15hasImageContentEv',
    )

  def suggestedFileName(self) -> str:
    """
    Calls Qt's 'QString QWebEngineContextMenuRequest::suggestedFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineContextMenuRequest::suggestedFileName() const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineContextMenuRequest17suggestedFileNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QWebEngineContextMenuRequest::setAccepted(bool
    accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QWebEngineContextMenuRequest::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN28QWebEngineContextMenuRequest11setAcceptedEb', accepted,
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

  @overload(QWebEngineContextMenuRequestPrivate)
  @overload(NoneType)
  def __init__(
      self,
      d: Optional[QWebEngineContextMenuRequestPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineContextMenuRequest::QWebEngineContextMenuRequest(
    QWebEngineContextMenuRequestPrivate *d)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecontextmenurequest.html

    Parameters
    ----------

    d : Optional[QWebEngineContextMenuRequestPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineContextMenuRequest::QWebEngineContextMenuRequest(
    #      QWebEngineContextMenuRequestPrivate *d)
    self._noteCreation(QWebEngineContextMenuRequest, lambda: Rituals.call(
        'ritual_ZN28QWebEngineContextMenuRequestC1EP35QWebEngineContextMenu'
        'RequestPrivate',
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
