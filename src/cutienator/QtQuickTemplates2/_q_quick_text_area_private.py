"""
QQuickTextAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTextAreaPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickTextEditPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QRectF
  from ..QtGui import QFont, QPalette
  from ..QtQuick import QQuickFlickable, QQuickGeometryChange, QQuickItem
  from . import QQuickTextArea
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuickFlickable = WAIT['QQuickFlickable']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickTextArea = WAIT['QQuickTextArea']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextAreaPrivate(QQuickTextEditPrivate):
  """
  The cute side of Qt's QQuickTextAreaPrivate: a plain Python object standing
  in front of one C++ QQuickTextAreaPrivate.

  It is built on the cute 'QQuickTextEditPrivate', as Qt's
  QQuickTextAreaPrivate is built on Qt's QQuickTextEditPrivate, and has
  everything that class has. Qt's QQuickTextAreaPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickTextAreaPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickTextAreaPrivate that has a ritual and that
  Python can call so far, 35 names in all: 'q_func', 'get', 'getInset',
  'getTopInset', 'getLeftInset', 'getRightInset', 'getBottomInset',
  'setTopInset', 'setLeftInset', 'setRightInset', 'setBottomInset',
  'resizeBackground', 'resolveFont', 'inheritFont', 'updateFont',
  'setFont_helper', 'updateHoverEnabled', 'attachFlickable',
  'detachFlickable', 'ensureCursorVisible', 'resizeFlickableControl',
  'resizeFlickableContent', 'itemGeometryChanged', 'getImplicitWidth',
  'getImplicitHeight', 'implicitWidthChanged', 'implicitHeightChanged',
  'accessibilityActiveChanged', 'cancelBackground', 'executeBackground',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged', 'itemDestroyed',
  'defaultPalette', 'setLastFocusChangeReason'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextArea *QQuickTextAreaPrivate::q_func() const': takes
    in Python what 'QQuickTextArea *QQuickTextAreaPrivate::q_func()' takes.
  - Qt's 'QQuickTextAreaPrivate::~QQuickTextAreaPrivate()': the destructor:
    Python never removes a C++ QQuickTextAreaPrivate.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on 'non-virtual thunk
  to QQuickTextAreaPrivate.

  What to expect
  --------------

  - The C++ QQuickTextAreaPrivate is created at the first use, not by
    'QQuickTextAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextAreaPrivate.
  - Each name of Qt's QQuickTextAreaPrivate that has no cute function yet,
    '__init__', 'readOnlyChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickTextAreaPrivate, each a class in here
  #  as in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextAreaPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickTextAreaPrivate::ExtraData.

    C++ hands a QQuickTextAreaPrivate::ExtraData around as a copy, so every
    C++ QQuickTextAreaPrivate::ExtraData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickTextAreaPrivate::ExtraData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextAreaPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickTextAreaPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextAreaPrivate::ExtraData is created at the first use,
      not by 'QQuickTextAreaPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextAreaPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuickTextAreaPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextAreaPrivate::ExtraData'

    #  Qt's '~QQuickTextAreaPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTextAreaPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuickTextAreaPrivate9ExtraDataD1Ev'

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

  @staticmethod
  @overload(QQuickTextArea)
  @overload(NoneType)
  def get(item: Optional[QQuickTextArea]) -> Optional[QQuickTextAreaPrivate]:
    """
    Calls Qt's 'QQuickTextAreaPrivate
    *QQuickTextAreaPrivate::get(QQuickTextArea *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextareaprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickTextArea]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextAreaPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextAreaPrivate *QQuickTextAreaPrivate::get(QQuickTextArea
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickTextAreaPrivate3getEP14QQuickTextArea',
        CuteMixin._addressOf(item),
    )
    return QQuickTextAreaPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextAreaPrivate'

  #  A C++ QQuickTextAreaPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextAreaPrivate'

  #  The functions Qt calls itself that QQuickTextAreaPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickItem20'
           'QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQuickI'
           'tem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQuick'
           'Item',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'defaultPalette': (
          ('_ZNK21QQuickTextAreaPrivate14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
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

  def getInset(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickTextAreaPrivate::getInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getInset

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickTextAreaPrivate::getInset() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickTextAreaPrivate8getInsetEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def getTopInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getTopInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getTopInset
    """
    #  qreal QQuickTextAreaPrivate::getTopInset() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTextAreaPrivate11getTopInsetEv',
    )

  def getLeftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getLeftInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getLeftInset
    """
    #  qreal QQuickTextAreaPrivate::getLeftInset() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTextAreaPrivate12getLeftInsetEv',
    )

  def getRightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getRightInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getRightInset
    """
    #  qreal QQuickTextAreaPrivate::getRightInset() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTextAreaPrivate13getRightInsetEv',
    )

  def getBottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getBottomInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getBottomInset
    """
    #  qreal QQuickTextAreaPrivate::getBottomInset() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTextAreaPrivate14getBottomInsetEv',
    )

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getImplicitWidth
    """
    #  qreal QQuickTextAreaPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK21QQuickTextAreaPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTextAreaPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextAreaPrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#getImplicitHeight
    """
    #  qreal QQuickTextAreaPrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK21QQuickTextAreaPrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTextAreaPrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickTextAreaPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickTextAreaPrivate::defaultPalette() const
    ritual = 'ritual_ZNK21QQuickTextAreaPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTextAreaPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, bool)
  def setTopInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::setTopInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#setTopInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextAreaPrivate::setTopInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate11setTopInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::setLeftInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#setLeftInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextAreaPrivate::setLeftInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate12setLeftInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::setRightInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#setRightInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextAreaPrivate::setRightInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate13setRightInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::setBottomInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#setBottomInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextAreaPrivate::setBottomInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate14setBottomInsetEdb', value, reset,
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::setFont_helper(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextAreaPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(Qt.FocusReason)
  def setLastFocusChangeReason(self, reason: Qt.FocusReason) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  bool QQuickTextAreaPrivate::setLastFocusChangeReason(Qt::FocusReason
    #      reason)
    ritual = (
        'ritual_ZN21QQuickTextAreaPrivate24setLastFocusChangeReasonEN2Qt11F'
        'ocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate24setLastFocusChangeReasonEN'
          '2Qt11FocusReasonE')
    return self.uglySide.call(ritual, reason.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickTextAreaPrivate::QQuickTextAreaPrivate()': leans on
    'non-virtual thunk to QQuickTextAreaPrivate::defaultPalette() const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextAreaPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickTextAreaPrivate::QQuickTextAreaPrivate()': leans on "
        "'non-virtual thunk to QQuickTextAreaPrivate::defaultPalette() "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickTextArea]:
    """
    Calls Qt's 'QQuickTextArea *QQuickTextAreaPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextareaprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextArea *QQuickTextAreaPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickTextAreaPrivate6q_funcEv')
    from . import QQuickTextArea
    return QQuickTextArea._cuteAt(address)

  def resizeBackground(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::resizeBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#resizeBackground
    """
    #  void QQuickTextAreaPrivate::resizeBackground()
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate16resizeBackgroundEv',
    )

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#resolveFont
    """
    #  void QQuickTextAreaPrivate::resolveFont()
    self.uglySide.call('ritual_ZN21QQuickTextAreaPrivate11resolveFontEv')

  @overload(QFont)
  def inheritFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::inheritFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#inheritFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextAreaPrivate::inheritFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate11inheritFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::updateFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextAreaPrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  @overload(bool, bool)
  def updateHoverEnabled(self, h: bool, e: bool) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::updateHoverEnabled(bool h, bool
    e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#updateHoverEnabled

    Parameters
    ----------

    h : bool
      Passed on as it is.

    e : bool
      Passed on as it is.
    """
    #  void QQuickTextAreaPrivate::updateHoverEnabled(bool h, bool e)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate18updateHoverEnabledEbb', h, e,
    )

  @overload(QQuickFlickable)
  @overload(NoneType)
  def attachFlickable(self, flickable: Optional[QQuickFlickable]) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::attachFlickable(QQuickFlickable
    *flickable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#attachFlickable

    Parameters
    ----------

    flickable : Optional[QQuickFlickable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextAreaPrivate::attachFlickable(QQuickFlickable
    #      *flickable)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate15attachFlickableEP15QQuickFlickab'
        'le',
        self._addressOf(flickable),
    )

  def detachFlickable(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::detachFlickable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#detachFlickable
    """
    #  void QQuickTextAreaPrivate::detachFlickable()
    self.uglySide.call('ritual_ZN21QQuickTextAreaPrivate15detachFlickableEv')

  def ensureCursorVisible(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::ensureCursorVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#ensureCursorVisible
    """
    #  void QQuickTextAreaPrivate::ensureCursorVisible()
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate19ensureCursorVisibleEv',
    )

  def resizeFlickableControl(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::resizeFlickableControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#resizeFlickableControl
    """
    #  void QQuickTextAreaPrivate::resizeFlickableControl()
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate22resizeFlickableControlEv',
    )

  def resizeFlickableContent(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::resizeFlickableContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#resizeFlickableContent
    """
    #  void QQuickTextAreaPrivate::resizeFlickableContent()
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate22resizeFlickableContentEv',
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTextAreaPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQuickIte'
        'm20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate19itemGeometryChangedEP10QQu'
          'ickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#implicitWidthChanged
    """
    #  void QQuickTextAreaPrivate::implicitWidthChanged()
    ritual = 'ritual_ZN21QQuickTextAreaPrivate20implicitWidthChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickTextAreaPrivate20implicitWidthChangedEv'
    self.uglySide.call(ritual)

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#implicitHeightChanged
    """
    #  void QQuickTextAreaPrivate::implicitHeightChanged()
    ritual = 'ritual_ZN21QQuickTextAreaPrivate21implicitHeightChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate21implicitHeightChangedEv')
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickTextAreaPrivate::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN21QQuickTextAreaPrivate26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate26accessibilityActiveChanged'
          'Eb')
    self.uglySide.call(ritual, active)

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#cancelBackground
    """
    #  void QQuickTextAreaPrivate::cancelBackground()
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate16cancelBackgroundEv',
    )

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::executeBackground(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#executeBackground

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextAreaPrivate::executeBackground(bool complete)
    self.uglySide.call(
        'ritual_ZN21QQuickTextAreaPrivate17executeBackgroundEb', complete,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextAreaPrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate24itemImplicitWidthChangedEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextAreaPrivate::itemImplicitHeightChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedEP10QQu'
        'ickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate25itemImplicitHeightChangedE'
          'P10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextAreaPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTextAreaPrivate13itemDestroyedEP10QQuickIte'
          'm')
    self.uglySide.call(ritual, self._addressOf(item))

  @staticmethod
  def readOnlyChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextAreaPrivate::readOnlyChanged(bool isReadOnly)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTextAreaPrivate.readOnlyChanged' has no cute function yet. "
        "Qt's 'void QQuickTextAreaPrivate::readOnlyChanged(bool "
        "isReadOnly)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
