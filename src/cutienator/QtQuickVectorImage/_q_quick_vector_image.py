"""
QQuickVectorImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVectorImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickVectorImageAnimations, QQuickVectorImagePrivate
  from ..QtCore import QMetaObject, QUrl
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickVectorImage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickVectorImage: a plain Python object standing in
  front of one C++ QQuickVectorImage.

  What exists
  -----------

  Every function of Qt's QQuickVectorImage that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'fillMode', 'setFillMode', 'preferredRendererType',
  'setPreferredRendererType', 'asynchronousShapes', 'setAsynchronousShapes',
  'asynchronous', 'setAsynchronous', 'retainWhileLoading',
  'setRetainWhileLoading', 'status', 'animations', 'assumeTrustedSource',
  'setAssumeTrustedSource', 'componentComplete', 'generatedItem',
  'sourceChanged', 'fillModeChanged', 'preferredRendererTypeChanged',
  'asynchronousShapesChanged', 'assumeTrustedSourceChanged',
  'asynchronousChanged', 'statusChanged', 'retainWhileLoadingChanged',
  'generatedItemChanged', 'd_func', 'updateRootItemScale',
  'updateAnimationProperties', 'updateItem'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickVectorImage::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickVectorImage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickVectorImage::~QQuickVectorImage()': the destructor: Python
    never removes a C++ QQuickVectorImage.
  - Qt's 'const QQuickVectorImagePrivate *QQuickVectorImage::d_func() const':
    takes in Python what 'QQuickVectorImagePrivate
    *QQuickVectorImage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickVectorImage is created at the first use, not by
    'QQuickVectorImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickVectorImage.
  - Qt tells when it has removed the C++ QQuickVectorImage. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickVectorImage, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FillMode(CuteNum):
    """
    The enum 'QQuickVectorImage::FillMode' of Qt, with the 4 names Qt gives
    in it.
    """

    NoResize = Kee[int](0)
    PreserveAspectFit = Kee[int](1)
    PreserveAspectCrop = Kee[int](2)
    Stretch = Kee[int](3)

  class RendererType(CuteNum):
    """
    The enum 'QQuickVectorImage::RendererType' of Qt, with the 2 names Qt
    gives in it.
    """

    GeometryRenderer = Kee[int](0)
    CurveRenderer = Kee[int](1)

  class Status(CuteNum, scoped=True):
    """
    The enum 'QQuickVectorImage::Status' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuickVectorImage::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#tr

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
    #  QString QQuickVectorImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickVectorImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVectorImage'

  #  A C++ QQuickVectorImage Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickVectorImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickVectorImage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickVectorImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickVectorImage::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickVectorImage::source() const
    address = self.uglySide.call('ritual_ZNK17QQuickVectorImage6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def fillMode(self) -> FillMode:
    """
    Calls Qt's 'FillMode QQuickVectorImage::fillMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#fillMode

    Returns
    -------

    FillMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FillMode(number)' gives.
    """
    #  FillMode QQuickVectorImage::fillMode() const
    return QQuickVectorImage.FillMode(self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage8fillModeEv',
    ))

  def preferredRendererType(self) -> RendererType:
    """
    Calls Qt's 'RendererType QQuickVectorImage::preferredRendererType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#preferredRendererType

    Returns
    -------

    RendererType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RendererType(number)'
      gives.
    """
    #  RendererType QQuickVectorImage::preferredRendererType() const
    return QQuickVectorImage.RendererType(self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage21preferredRendererTypeEv',
    ))

  def asynchronousShapes(self) -> bool:
    """
    Calls Qt's 'bool QQuickVectorImage::asynchronousShapes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#asynchronousShapes
    """
    #  bool QQuickVectorImage::asynchronousShapes() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage18asynchronousShapesEv',
    )

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuickVectorImage::asynchronous() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#asynchronous
    """
    #  bool QQuickVectorImage::asynchronous() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage12asynchronousEv',
    )

  def retainWhileLoading(self) -> bool:
    """
    Calls Qt's 'bool QQuickVectorImage::retainWhileLoading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#retainWhileLoading
    """
    #  bool QQuickVectorImage::retainWhileLoading() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage18retainWhileLoadingEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickVectorImage::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickVectorImage::status() const
    return QQuickVectorImage.Status(self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage6statusEv',
    ))

  def assumeTrustedSource(self) -> bool:
    """
    Calls Qt's 'bool QQuickVectorImage::assumeTrustedSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#assumeTrustedSource
    """
    #  bool QQuickVectorImage::assumeTrustedSource() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage19assumeTrustedSourceEv',
    )

  def generatedItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickVectorImage::generatedItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#generatedItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickVectorImage::generatedItem() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickVectorImage13generatedItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickVectorImage::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(FillMode)
  def setFillMode(self, newFillMode: FillMode) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setFillMode(FillMode newFillMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#setFillMode

    Parameters
    ----------

    newFillMode : FillMode
      Passed on as its number.
    """
    #  void QQuickVectorImage::setFillMode(FillMode newFillMode)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage11setFillModeENS_8FillModeE',
        newFillMode.value,
    )

  @overload(RendererType)
  def setPreferredRendererType(
      self,
      newPreferredRendererType: RendererType,
  ) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setPreferredRendererType(RendererType
    newPreferredRendererType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#setPreferredRendererType

    Parameters
    ----------

    newPreferredRendererType : RendererType
      Passed on as its number.
    """
    #  void QQuickVectorImage::setPreferredRendererType(RendererType
    #      newPreferredRendererType)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage24setPreferredRendererTypeENS_12Render'
        'erTypeE',
        newPreferredRendererType.value,
    )

  @overload(bool)
  def setAsynchronousShapes(self, asynchronous: bool) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setAsynchronousShapes(bool
    asynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#setAsynchronousShapes

    Parameters
    ----------

    asynchronous : bool
      Passed on as it is.
    """
    #  void QQuickVectorImage::setAsynchronousShapes(bool asynchronous)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage21setAsynchronousShapesEb',
        asynchronous,
    )

  @overload(bool)
  def setAsynchronous(self, asynchronous: bool) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setAsynchronous(bool asynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#setAsynchronous

    Parameters
    ----------

    asynchronous : bool
      Passed on as it is.
    """
    #  void QQuickVectorImage::setAsynchronous(bool asynchronous)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage15setAsynchronousEb', asynchronous,
    )

  @overload(bool)
  def setRetainWhileLoading(self, retainWhileLoading: bool) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setRetainWhileLoading(bool
    retainWhileLoading)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#setRetainWhileLoading

    Parameters
    ----------

    retainWhileLoading : bool
      Passed on as it is.
    """
    #  void QQuickVectorImage::setRetainWhileLoading(bool retainWhileLoading)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage21setRetainWhileLoadingEb',
        retainWhileLoading,
    )

  @overload(bool)
  def setAssumeTrustedSource(self, assumeTrustedSource: bool) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::setAssumeTrustedSource(bool
    assumeTrustedSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#setAssumeTrustedSource

    Parameters
    ----------

    assumeTrustedSource : bool
      Passed on as it is.
    """
    #  void QQuickVectorImage::setAssumeTrustedSource(bool
    #      assumeTrustedSource)
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage22setAssumeTrustedSourceEb',
        assumeTrustedSource,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickVectorImage::QQuickVectorImage(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#QQuickVectorImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickVectorImage::QQuickVectorImage(QQuickItem *parent)
    self._noteCreation(QQuickVectorImage, lambda: Rituals.call(
        'ritual_ZN17QQuickVectorImageC1EP10QQuickItem',
        self._addressOf(parent),
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

  def animations(self) -> Optional[QQuickVectorImageAnimations]:
    """
    Calls Qt's 'QQuickVectorImageAnimations
    *QQuickVectorImage::animations()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#animations

    Returns
    -------

    Optional[QQuickVectorImageAnimations]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickVectorImageAnimations *QQuickVectorImage::animations()
    address = self.uglySide.call(
        'ritual_ZN17QQuickVectorImage10animationsEv',
    )
    from . import QQuickVectorImageAnimations
    return QQuickVectorImageAnimations._cuteAt(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#componentComplete
    """
    #  void QQuickVectorImage::componentComplete()
    ritual = 'ritual_ZN17QQuickVectorImage17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickVectorImage17componentCompleteEv'
    self.uglySide.call(ritual)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#sourceChanged
    """
    #  void QQuickVectorImage::sourceChanged()
    self.uglySide.call('ritual_ZN17QQuickVectorImage13sourceChangedEv')

  def fillModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::fillModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#fillModeChanged
    """
    #  void QQuickVectorImage::fillModeChanged()
    self.uglySide.call('ritual_ZN17QQuickVectorImage15fillModeChangedEv')

  def preferredRendererTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::preferredRendererTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html
    """
    #  void QQuickVectorImage::preferredRendererTypeChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage28preferredRendererTypeChangedEv',
    )

  def asynchronousShapesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::asynchronousShapesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#asynchronousShapesChanged
    """
    #  void QQuickVectorImage::asynchronousShapesChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage25asynchronousShapesChangedEv',
    )

  def assumeTrustedSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::assumeTrustedSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#assumeTrustedSourceChanged
    """
    #  void QQuickVectorImage::assumeTrustedSourceChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage26assumeTrustedSourceChangedEv',
    )

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#asynchronousChanged
    """
    #  void QQuickVectorImage::asynchronousChanged()
    self.uglySide.call('ritual_ZN17QQuickVectorImage19asynchronousChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#statusChanged
    """
    #  void QQuickVectorImage::statusChanged()
    self.uglySide.call('ritual_ZN17QQuickVectorImage13statusChangedEv')

  def retainWhileLoadingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::retainWhileLoadingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#retainWhileLoadingChanged
    """
    #  void QQuickVectorImage::retainWhileLoadingChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage25retainWhileLoadingChangedEv',
    )

  def generatedItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::generatedItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#generatedItemChanged
    """
    #  void QQuickVectorImage::generatedItemChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage20generatedItemChangedEv',
    )

  def d_func(self) -> Optional[QQuickVectorImagePrivate]:
    """
    Calls Qt's 'QQuickVectorImagePrivate *QQuickVectorImage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#d_func

    Returns
    -------

    Optional[QQuickVectorImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickVectorImagePrivate *QQuickVectorImage::d_func()
    address = self.uglySide.call('ritual_ZN17QQuickVectorImage6d_funcEv')
    from . import QQuickVectorImagePrivate
    return QQuickVectorImagePrivate._cuteAt(address)

  def updateRootItemScale(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::updateRootItemScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#updateRootItemScale
    """
    #  void QQuickVectorImage::updateRootItemScale()
    self.uglySide.call('ritual_ZN17QQuickVectorImage19updateRootItemScaleEv')

  def updateAnimationProperties(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::updateAnimationProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimage.html#updateAnimationProperties
    """
    #  void QQuickVectorImage::updateAnimationProperties()
    self.uglySide.call(
        'ritual_ZN17QQuickVectorImage25updateAnimationPropertiesEv',
    )

  def updateItem(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImage::updateItem()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvectorimage.html#updateItem
    """
    #  void QQuickVectorImage::updateItem()
    self.uglySide.call('ritual_ZN17QQuickVectorImage10updateItemEv')
