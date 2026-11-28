"""
QCss::Declaration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::Declaration to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QSharedData
from . import QCss

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from . import QBrush, QColor, QIcon, QPalette
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QPalette = WAIT['QPalette']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Declaration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::Declaration: a plain Python object standing in
  front of one C++ QCss::Declaration.

  C++ hands a QCss::Declaration around as a copy, so every C++
  QCss::Declaration behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCss::Declaration that has a ritual and that Python
  can call so far, 17 names in all: 'isEmpty', 'colorValue', 'colorValues',
  'brushValue', 'brushValues', 'styleValue', 'originValue', 'repeatValue',
  'alignmentValue', 'positionValue', 'attachmentValue', 'styleFeaturesValue',
  'sizeValue', 'rectValue', 'uriValue', 'iconValue', 'borderCollapseValue'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QCss::Declaration::styleValues(BorderStyle *s) const': names
    'QCss::BorderStyle', which has no cute class yet.
  - Qt's 'bool QCss::Declaration::intValue(int *i, const char *unit) const':
    takes a number to change where it is.
  - Qt's 'bool QCss::Declaration::realValue(qreal *r, const char *unit)
    const': takes a number to change where it is.
  - Qt's 'void QCss::Declaration::borderImageValue(QString *image, int *cuts,
    TileMode *h, TileMode *v) const': takes a number to change where it is.
  - Qt's 'QList<qreal> QCss::Declaration::dashArray() const': gives a type
    Python has no way to take yet.
  - Qt's 'QCss::Declaration::~Declaration()': the destructor: Python removes
    its C++ QCss::Declaration by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::Declaration is created at the first use, not by
    'QCss::Declaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::Declaration back gives a copy the ritual made
    for Python, in a new cute QCss::Declaration.
  - Each name of Qt's QCss::Declaration that has no cute function yet,
    'borderImageValue', 'dashArray', 'intValue', 'realValue', 'styleValues',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QCss::Declaration, each a class in here as
  #  in C++.

  class DeclarationData(QSharedData):
    """
    The cute side of Qt's QCss::Declaration::DeclarationData: a plain Python
    object standing in front of one C++ QCss::Declaration::DeclarationData.

    It is built on the cute 'QSharedData', as Qt's
    QCss::Declaration::DeclarationData is built on Qt's QSharedData, and has
    everything that class has.

    C++ hands a QCss::Declaration::DeclarationData around as a copy, so every
    C++ QCss::Declaration::DeclarationData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QCss::Declaration::DeclarationData yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCss::Declaration::DeclarationData::~DeclarationData()': the
      destructor: Python removes its C++ QCss::Declaration::DeclarationData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QCss::Declaration::DeclarationData is created at the first use,
      not by 'QCss::Declaration::DeclarationData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCss::Declaration::DeclarationData back gives a
      copy the ritual made for Python, in a new cute
      QCss::Declaration::DeclarationData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCss::Declaration::DeclarationData'

    #  Qt's '~QCss::Declaration::DeclarationData()'. Naming it makes this a
    #  value class: Python owns every C++ QCss::Declaration::DeclarationData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN4QCss11Declaration15DeclarationDataD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QCss::Declaration::DeclarationData::DeclarationData()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcss-declaration-declarationdata.html
      """
      #  QCss::Declaration::DeclarationData::DeclarationData()
      self._noteCreation(Declaration.DeclarationData, lambda: Rituals.call(
          'ritual_ZN4QCss11Declaration15DeclarationDataC1Ev',
      ))

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
  __qt_class__ = 'QCss::Declaration'

  #  Qt's '~QCss::Declaration()'. Naming it makes this a value class: Python
  #  owns every C++ QCss::Declaration behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN4QCss11DeclarationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCss::Declaration::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#isEmpty
    """
    #  bool QCss::Declaration::isEmpty() const
    return self.uglySide.call('ritual_ZNK4QCss11Declaration7isEmptyEv')

  @overload()
  @overload(QPalette)
  def colorValue(self, a0: Optional[QPalette] = None) -> QColor:
    """
    Calls Qt's 'QColor QCss::Declaration::colorValue(const QPalette &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#colorValue

    Parameters
    ----------

    a0 : Optional[QPalette]
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own. May be left out, as in Qt: a new 'QPalette()' is then passed on.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCss::Declaration::colorValue(const QPalette &a0) const
    if a0 is None:
      from . import QPalette
      a0 = QPalette()
    address = self.uglySide.call(
        'ritual_ZNK4QCss11Declaration10colorValueERK8QPalette',
        self._valueOf(a0),
    )
    from . import QColor
    return QColor._cuteOwning(address)

  @overload()
  @overload(QPalette)
  def brushValue(self, a0: Optional[QPalette] = None) -> QBrush:
    """
    Calls Qt's 'QBrush QCss::Declaration::brushValue(const QPalette &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#brushValue

    Parameters
    ----------

    a0 : Optional[QPalette]
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own. May be left out, as in Qt: a new 'QPalette()' is then passed on.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QCss::Declaration::brushValue(const QPalette &a0) const
    if a0 is None:
      from . import QPalette
      a0 = QPalette()
    address = self.uglySide.call(
        'ritual_ZNK4QCss11Declaration10brushValueERK8QPalette',
        self._valueOf(a0),
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  def styleValue(self) -> QCss.BorderStyle:
    """
    Calls Qt's 'BorderStyle QCss::Declaration::styleValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#styleValue

    Returns
    -------

    QCss.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.BorderStyle(number)'
      gives.
    """
    #  BorderStyle QCss::Declaration::styleValue() const
    return QCss.BorderStyle(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration10styleValueEv',
    ))

  def originValue(self) -> QCss.Origin:
    """
    Calls Qt's 'Origin QCss::Declaration::originValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#originValue

    Returns
    -------

    QCss.Origin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.Origin(number)'
      gives.
    """
    #  Origin QCss::Declaration::originValue() const
    return QCss.Origin(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration11originValueEv',
    ))

  def repeatValue(self) -> QCss.Repeat:
    """
    Calls Qt's 'Repeat QCss::Declaration::repeatValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#repeatValue

    Returns
    -------

    QCss.Repeat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.Repeat(number)'
      gives.
    """
    #  Repeat QCss::Declaration::repeatValue() const
    return QCss.Repeat(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration11repeatValueEv',
    ))

  def alignmentValue(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QCss::Declaration::alignmentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-declaration.html#alignmentValue

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QCss::Declaration::alignmentValue() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration14alignmentValueEv',
    ))

  def positionValue(self) -> QCss.PositionMode:
    """
    Calls Qt's 'PositionMode QCss::Declaration::positionValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-declaration.html#positionValue

    Returns
    -------

    QCss.PositionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QCss.PositionMode(number)' gives.
    """
    #  PositionMode QCss::Declaration::positionValue() const
    return QCss.PositionMode(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration13positionValueEv',
    ))

  def attachmentValue(self) -> QCss.Attachment:
    """
    Calls Qt's 'Attachment QCss::Declaration::attachmentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-declaration.html#attachmentValue

    Returns
    -------

    QCss.Attachment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.Attachment(number)'
      gives.
    """
    #  Attachment QCss::Declaration::attachmentValue() const
    return QCss.Attachment(self.uglySide.call(
        'ritual_ZNK4QCss11Declaration15attachmentValueEv',
    ))

  def styleFeaturesValue(self) -> int:
    """
    Calls Qt's 'int QCss::Declaration::styleFeaturesValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-declaration.html#styleFeaturesValue
    """
    #  int QCss::Declaration::styleFeaturesValue() const
    return self.uglySide.call(
        'ritual_ZNK4QCss11Declaration18styleFeaturesValueEv',
    )

  def sizeValue(self) -> QSize:
    """
    Calls Qt's 'QSize QCss::Declaration::sizeValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#sizeValue

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCss::Declaration::sizeValue() const
    address = self.uglySide.call('ritual_ZNK4QCss11Declaration9sizeValueEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def rectValue(self) -> QRect:
    """
    Calls Qt's 'QRect QCss::Declaration::rectValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#rectValue

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCss::Declaration::rectValue() const
    address = self.uglySide.call('ritual_ZNK4QCss11Declaration9rectValueEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def uriValue(self) -> str:
    """
    Calls Qt's 'QString QCss::Declaration::uriValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#uriValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::Declaration::uriValue() const
    return self.uglySide.call('ritual_ZNK4QCss11Declaration8uriValueEv')

  def iconValue(self) -> QIcon:
    """
    Calls Qt's 'QIcon QCss::Declaration::iconValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#iconValue

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QCss::Declaration::iconValue() const
    address = self.uglySide.call('ritual_ZNK4QCss11Declaration9iconValueEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def borderCollapseValue(self) -> bool:
    """
    Calls Qt's 'bool QCss::Declaration::borderCollapseValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-declaration.html#borderCollapseValue
    """
    #  bool QCss::Declaration::borderCollapseValue() const
    return self.uglySide.call(
        'ritual_ZNK4QCss11Declaration19borderCollapseValueEv',
    )

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
    Notes what was given, for Qt's 'QCss::Declaration::Declaration()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#Declaration
    """
    #  QCss::Declaration::Declaration()
    self._noteCreation(Declaration, lambda: Rituals.call(
        'ritual_ZN4QCss11DeclarationC1Ev',
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

  @overload(QColor)
  @overload(NoneType)
  @overload(QColor, QPalette)
  @overload(NoneType, QPalette)
  def colorValues(
      self,
      c: Optional[QColor],
      a1: Optional[QPalette] = None,
  ) -> None:
    """
    Calls Qt's 'void QCss::Declaration::colorValues(QColor *c, const QPalette
    &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#colorValues

    Parameters
    ----------

    c : Optional[QColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QPalette]
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own. May be left out, as in Qt: a new 'QPalette()' is then passed on.
    """
    #  void QCss::Declaration::colorValues(QColor *c, const QPalette &a1)
    #      const
    if a1 is None:
      from . import QPalette
      a1 = QPalette()
    self.uglySide.call(
        'ritual_ZNK4QCss11Declaration11colorValuesEP6QColorRK8QPalette',
        self._addressOf(c), self._valueOf(a1),
    )

  @overload(QBrush)
  @overload(NoneType)
  @overload(QBrush, QPalette)
  @overload(NoneType, QPalette)
  def brushValues(
      self,
      c: Optional[QBrush],
      a1: Optional[QPalette] = None,
  ) -> None:
    """
    Calls Qt's 'void QCss::Declaration::brushValues(QBrush *c, const QPalette
    &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-declaration.html#brushValues

    Parameters
    ----------

    c : Optional[QBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QPalette]
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own. May be left out, as in Qt: a new 'QPalette()' is then passed on.
    """
    #  void QCss::Declaration::brushValues(QBrush *c, const QPalette &a1)
    #      const
    if a1 is None:
      from . import QPalette
      a1 = QPalette()
    self.uglySide.call(
        'ritual_ZNK4QCss11Declaration11brushValuesEP6QBrushRK8QPalette',
        self._addressOf(c), self._valueOf(a1),
    )

  @staticmethod
  def borderImageValue(*__, **_) -> Never:
    """
    Qt's 'void QCss::Declaration::borderImageValue(QString *image, int *cuts,
    TileMode *h, TileMode *v) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.Declaration.borderImageValue' has no cute function yet. Qt's "
        "'void QCss::Declaration::borderImageValue(QString *image, int "
        "*cuts, TileMode *h, TileMode *v) const': takes a number to change "
        "where it is.")

  @staticmethod
  def dashArray(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QCss::Declaration::dashArray() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCss.Declaration.dashArray' has no cute function yet. Qt's "
        "'QList<qreal> QCss::Declaration::dashArray() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def intValue(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Declaration::intValue(int *i, const char *unit) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.Declaration.intValue' has no cute function yet. Qt's 'bool "
        "QCss::Declaration::intValue(int *i, const char *unit) const': "
        "takes a number to change where it is.")

  @staticmethod
  def realValue(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Declaration::realValue(qreal *r, const char *unit)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.Declaration.realValue' has no cute function yet. Qt's 'bool "
        "QCss::Declaration::realValue(qreal *r, const char *unit) const': "
        "takes a number to change where it is.")

  @staticmethod
  def styleValues(*__, **_) -> Never:
    """
    Qt's 'void QCss::Declaration::styleValues(BorderStyle *s) const': names
    'QCss::BorderStyle', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.Declaration.styleValues' has no cute function yet. Qt's "
        "'void QCss::Declaration::styleValues(BorderStyle *s) const': names "
        "'QCss::BorderStyle', which has no cute class yet.")
