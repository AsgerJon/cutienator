"""
QQuickIconLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIconLabelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSizeF
  from ..QtQuick import QQuickItem
  from . import QQuickIconLabel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickIconLabelPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickIconLabelPrivate: a plain Python object
  standing in front of one C++ QQuickIconLabelPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickIconLabelPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has. Qt's
  QQuickIconLabelPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickIconLabelPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickIconLabelPrivate that has a ritual and that
  Python can call so far, 24 names in all: 'q_func', 'hasIcon', 'hasText',
  'createImage', 'destroyImage', 'updateImage', 'syncImage',
  'updateOrSyncImage', 'createLabel', 'destroyLabel', 'updateLabel',
  'syncLabel', 'updateOrSyncLabel', 'updateImplicitSize', 'layout',
  'watchChanges', 'itemImplicitWidthChanged', 'itemImplicitHeightChanged',
  'itemDestroyed', 'textChange', 'displayChange', 'beginClass',
  'completeComponent', 'alignedRect'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickIconLabel *QQuickIconLabelPrivate::q_func() const':
    takes in Python what 'QQuickIconLabel *QQuickIconLabelPrivate::q_func()'
    takes.
  - Qt's 'QQuickIconLabelPrivate::~QQuickIconLabelPrivate()': the destructor:
    Python never removes a C++ QQuickIconLabelPrivate.

  What has no ritual
  ------------------

  3 of the 29 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickIconLabelPrivate is created at the first use, not by
    'QQuickIconLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIconLabelPrivate.
  - Each name of Qt's QQuickIconLabelPrivate that has no cute function yet,
    'isLeftToRight', 'setPositioningDirty', 'unwatchChanges', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def beginClass(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::beginClass(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#beginClass

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::beginClass(QQuickItem *item)
    Rituals.call(
        'ritual_ZN22QQuickIconLabelPrivate10beginClassEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def completeComponent(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::completeComponent(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#completeComponent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::completeComponent(QQuickItem *item)
    Rituals.call(
        'ritual_ZN22QQuickIconLabelPrivate17completeComponentEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(bool, Qt.Alignment, QSizeF, QRectF)
  def alignedRect(
      mirrored: bool,
      alignment: Qt.Alignment,
      size: QSizeF,
      rectangle: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickIconLabelPrivate::alignedRect(bool mirrored,
    Qt::Alignment alignment, const QSizeF &size, const QRectF &rectangle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#alignedRect

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickIconLabelPrivate::alignedRect(bool mirrored,
    #      Qt::Alignment alignment, const QSizeF &size, const QRectF
    #      &rectangle)
    address = Rituals.call(
        'ritual_ZN22QQuickIconLabelPrivate11alignedRectEb6QFlagsIN2Qt13Alig'
        'nmentFlagEERK6QSizeFRK6QRectF',
        mirrored, alignment.value, CuteMixin._valueOf(size),
        CuteMixin._valueOf(rectangle),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIconLabelPrivate'

  #  A C++ QQuickIconLabelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickIconLabelPrivate'

  #  The functions Qt calls itself that QQuickIconLabelPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateImplicitSize': (
          ('_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'layout': (
          ('_ZN22QQuickIconLabelPrivate6layoutEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQuick'
           'Item',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQuic'
           'kItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'textChange': (
          ('_ZN22QQuickIconLabelPrivate10textChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'displayChange': (
          ('_ZN22QQuickIconLabelPrivate13displayChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasIcon(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::hasIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#hasIcon
    """
    #  bool QQuickIconLabelPrivate::hasIcon() const
    return self.uglySide.call('ritual_ZNK22QQuickIconLabelPrivate7hasIconEv')

  def hasText(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::hasText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#hasText
    """
    #  bool QQuickIconLabelPrivate::hasText() const
    return self.uglySide.call('ritual_ZNK22QQuickIconLabelPrivate7hasTextEv')

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

  def q_func(self) -> Optional[QQuickIconLabel]:
    """
    Calls Qt's 'QQuickIconLabel *QQuickIconLabelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabelprivate.html#q_func

    Returns
    -------

    Optional[QQuickIconLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIconLabel *QQuickIconLabelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate6q_funcEv',
    )
    from . import QQuickIconLabel
    return QQuickIconLabel._cuteAt(address)

  def createImage(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::createImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#createImage
    """
    #  bool QQuickIconLabelPrivate::createImage()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate11createImageEv',
    )

  def destroyImage(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::destroyImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#destroyImage
    """
    #  bool QQuickIconLabelPrivate::destroyImage()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate12destroyImageEv',
    )

  def updateImage(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::updateImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#updateImage
    """
    #  bool QQuickIconLabelPrivate::updateImage()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate11updateImageEv',
    )

  def syncImage(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::syncImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#syncImage
    """
    #  void QQuickIconLabelPrivate::syncImage()
    self.uglySide.call('ritual_ZN22QQuickIconLabelPrivate9syncImageEv')

  def updateOrSyncImage(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::updateOrSyncImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#updateOrSyncImage
    """
    #  void QQuickIconLabelPrivate::updateOrSyncImage()
    self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate17updateOrSyncImageEv',
    )

  def createLabel(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::createLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#createLabel
    """
    #  bool QQuickIconLabelPrivate::createLabel()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate11createLabelEv',
    )

  def destroyLabel(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::destroyLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#destroyLabel
    """
    #  bool QQuickIconLabelPrivate::destroyLabel()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate12destroyLabelEv',
    )

  def updateLabel(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabelPrivate::updateLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#updateLabel
    """
    #  bool QQuickIconLabelPrivate::updateLabel()
    return self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate11updateLabelEv',
    )

  def syncLabel(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::syncLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#syncLabel
    """
    #  void QQuickIconLabelPrivate::syncLabel()
    self.uglySide.call('ritual_ZN22QQuickIconLabelPrivate9syncLabelEv')

  def updateOrSyncLabel(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::updateOrSyncLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#updateOrSyncLabel
    """
    #  void QQuickIconLabelPrivate::updateOrSyncLabel()
    self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate17updateOrSyncLabelEv',
    )

  def updateImplicitSize(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::updateImplicitSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#updateImplicitSize
    """
    #  void QQuickIconLabelPrivate::updateImplicitSize()
    ritual = 'ritual_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickIconLabelPrivate18updateImplicitSizeEv'
    self.uglySide.call(ritual)

  def layout(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::layout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabelprivate.html#layout
    """
    #  void QQuickIconLabelPrivate::layout()
    ritual = 'ritual_ZN22QQuickIconLabelPrivate6layoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickIconLabelPrivate6layoutEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def watchChanges(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::watchChanges(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#watchChanges

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::watchChanges(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickIconLabelPrivate12watchChangesEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::itemImplicitWidthChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedEP10QQu'
        'ickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickIconLabelPrivate24itemImplicitWidthChangedE'
          'P10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::itemImplicitHeightChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN22QQuickIconLabelPrivate25itemImplicitHeightChangedEP10QQ'
        'uickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickIconLabelPrivate25itemImplicitHeightChanged'
          'EP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIconLabelPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickIconLabelPrivate13itemDestroyedEP10QQuickIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))

  def textChange(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::textChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#textChange
    """
    #  void QQuickIconLabelPrivate::textChange()
    ritual = 'ritual_ZN22QQuickIconLabelPrivate10textChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickIconLabelPrivate10textChangeEv'
    self.uglySide.call(ritual)

  def displayChange(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabelPrivate::displayChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabelprivate.html#displayChange
    """
    #  void QQuickIconLabelPrivate::displayChange()
    ritual = 'ritual_ZN22QQuickIconLabelPrivate13displayChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickIconLabelPrivate13displayChangeEv'
    self.uglySide.call(ritual)

  @staticmethod
  def isLeftToRight(*__, **_) -> Never:
    """
    Qt's 'bool QQuickIconLabelPrivate::isLeftToRight() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickIconLabelPrivate.isLeftToRight' has no cute function yet. "
        "Qt's 'bool QQuickIconLabelPrivate::isLeftToRight() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setPositioningDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuickIconLabelPrivate::setPositioningDirty()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickIconLabelPrivate.setPositioningDirty' has no cute function "
        "yet. Qt's 'void QQuickIconLabelPrivate::setPositioningDirty()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def unwatchChanges(*__, **_) -> Never:
    """
    Qt's 'void QQuickIconLabelPrivate::unwatchChanges(QQuickItem *item)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'itemChangeTypes'; did you mean 'itemChange'?.
    """
    raise NotImplementedError(
        "'QQuickIconLabelPrivate.unwatchChanges' has no cute function yet. "
        "Qt's 'void QQuickIconLabelPrivate::unwatchChanges(QQuickItem "
        "*item)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'itemChangeTypes'; did you mean 'itemChange'?.")
