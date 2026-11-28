"""
Abstract3DController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/abstract3dcontroller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Abstract3DController to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Q3DTheme, QAbstract3DAxis, QAbstract3DGraph
from . import QAbstract3DInputHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMetaObject, QPoint, QRect
  from ..QtGui import QColor, QLinearGradient, QMouseEvent, QTouchEvent
  from ..QtGui import QVector3D, QWheelEvent
  from ..QtOpenGL import QOpenGLFramebufferObject
  from . import Abstract3DRenderer, Q3DScene, QAbstract3DSeries
  from . import QCategory3DAxis, QCustom3DItem, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DRenderer = WAIT['Abstract3DRenderer']
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QColor = WAIT['QColor']
  QCustom3DItem = WAIT['QtDataVisualization:QCustom3DItem']
  QLinearGradient = WAIT['QLinearGradient']
  QLocale = WAIT['QLocale']
  QMouseEvent = WAIT['QMouseEvent']
  QOpenGLFramebufferObject = WAIT['QOpenGLFramebufferObject']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QTouchEvent = WAIT['QTouchEvent']
  QVector3D = WAIT['QVector3D']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Abstract3DController(QObject):
  """
  The cute side of Qt's Abstract3DController: a plain Python object standing
  in front of one C++ Abstract3DController.

  It is built on the cute 'QObject', as Qt's Abstract3DController is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Abstract3DController that has a ritual and that
  Python can call so far, 155 names in all: 'metaObject', 'tr',
  'isInitialized', 'synchDataToRenderer', 'render', 'initializeOpenGL',
  'setRenderer', 'addSeries', 'insertSeries', 'removeSeries', 'hasSeries',
  'seriesList', 'setAxisX', 'axisX', 'setAxisY', 'axisY', 'setAxisZ',
  'axisZ', 'addAxis', 'releaseAxis', 'axes', 'addInputHandler',
  'releaseInputHandler', 'setActiveInputHandler', 'activeInputHandler',
  'inputHandlers', 'addTheme', 'releaseTheme', 'setActiveTheme',
  'activeTheme', 'themes', 'setSelectionMode', 'selectionMode',
  'setShadowQuality', 'doSetShadowQuality', 'shadowQuality',
  'shadowsSupported', 'setOptimizationHints', 'optimizationHints',
  'isSlicingActive', 'setSlicingActive', 'scene', 'markDataDirty',
  'markSeriesVisualsDirty', 'requestRender', 'addCustomItem',
  'deleteCustomItems', 'deleteCustomItem', 'releaseCustomItem',
  'customItems', 'selectedLabelIndex', 'selectedAxis',
  'selectedCustomItemIndex', 'selectedCustomItem', 'setOrthoProjection',
  'isOrthoProjection', 'setMeasureFps', 'measureFps', 'currentFps',
  'selectedElement', 'setAspectRatio', 'aspectRatio',
  'setHorizontalAspectRatio', 'horizontalAspectRatio', 'setReflection',
  'reflection', 'setReflectivity', 'reflectivity', 'setPolar', 'isPolar',
  'setRadialLabelOffset', 'radialLabelOffset', 'setLocale', 'locale',
  'queriedGraphPosition', 'setMargin', 'margin', 'emitNeedRender',
  'clearSelection', 'mouseDoubleClickEvent', 'touchEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseMoveEvent', 'wheelEvent',
  'handleAxisTitleChangedBySender', 'handleAxisLabelsChangedBySender',
  'handleAxisRangeChangedBySender', 'handleAxisSegmentCountChangedBySender',
  'handleAxisSubSegmentCountChangedBySender',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisLabelFormatChangedBySender',
  'handleAxisReversedChangedBySender', 'handleAxisFormatterDirtyBySender',
  'handleAxisLabelAutoRotationChangedBySender',
  'handleAxisTitleVisibilityChangedBySender',
  'handleAxisTitleFixedChangedBySender',
  'handleSeriesVisibilityChangedBySender', 'handlePendingClick',
  'handlePendingGraphPositionQuery', 'adjustAxisRanges',
  'markSeriesItemLabelsDirty', 'isOpenGLES', 'destroyRenderer',
  'handleAxisTitleChanged', 'handleAxisLabelsChanged',
  'handleAxisRangeChanged', 'handleAxisSegmentCountChanged',
  'handleAxisSubSegmentCountChanged', 'handleAxisAutoAdjustRangeChanged',
  'handleAxisLabelFormatChanged', 'handleAxisReversedChanged',
  'handleAxisFormatterDirty', 'handleAxisLabelAutoRotationChanged',
  'handleAxisTitleVisibilityChanged', 'handleAxisTitleFixedChanged',
  'handleInputViewChanged', 'handleInputPositionChanged',
  'handleSeriesVisibilityChanged', 'handleThemeColorStyleChanged',
  'handleThemeBaseColorsChanged', 'handleThemeBaseGradientsChanged',
  'handleThemeSingleHighlightColorChanged',
  'handleThemeSingleHighlightGradientChanged',
  'handleThemeMultiHighlightColorChanged',
  'handleThemeMultiHighlightGradientChanged', 'handleThemeTypeChanged',
  'handleRequestShadowQuality', 'updateCustomItem', 'shadowQualityChanged',
  'activeInputHandlerChanged', 'activeThemeChanged', 'selectionModeChanged',
  'needRender', 'axisXChanged', 'axisYChanged', 'axisZChanged',
  'elementSelected', 'measureFpsChanged', 'currentFpsChanged',
  'orthoProjectionChanged', 'aspectRatioChanged',
  'horizontalAspectRatioChanged', 'optimizationHintsChanged', 'polarChanged',
  'radialLabelOffsetChanged', 'reflectionChanged', 'reflectivityChanged',
  'localeChanged', 'queriedGraphPositionChanged', 'marginChanged',
  'createDefaultAxis', 'createDefaultValueAxis', 'createDefaultCategoryAxis',
  'startRecordingRemovesAndInserts'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Abstract3DController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Abstract3DController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Abstract3DController::~Abstract3DController()': the destructor:
    Python never removes a C++ Abstract3DController.
  - Qt's 'void
    Abstract3DController::setAxisHelper(QAbstract3DAxis::AxisOrientation
    orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 163 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Abstract3DController is created at the first use, not by
    'Abstract3DController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Abstract3DController.
  - Qt tells when it has removed the C++ Abstract3DController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Abstract3DController that has no cute function yet,
    'setAxisHelper', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside Abstract3DController, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SelectionType(CuteNum):
    """
    The enum 'Abstract3DController::SelectionType' of Qt, with the 4 names Qt
    gives in it.
    """

    SelectionNone = Kee[int](0)
    SelectionItem = Kee[int](1)
    SelectionRow = Kee[int](2)
    SelectionColumn = Kee[int](3)

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
    Calls Qt's 'QString Abstract3DController::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#tr

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
    #  QString Abstract3DController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20Abstract3DController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Abstract3DController'

  #  A C++ Abstract3DController Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Abstract3DController'

  #  The functions Qt calls itself that Abstract3DController is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'axes': (
          'QList<QAbstract3DAxis *> Abstract3DController::axes() const',
      ),
      'inputHandlers': (
          'QList<QAbstract3DInputHandler *> '
          'Abstract3DController::inputHandlers() const',
      ),
      'themes': (
          'QList<Q3DTheme *> Abstract3DController::themes() const',
      ),
  }

  #  The functions Qt calls itself that Abstract3DController is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'synchDataToRenderer': (
          ('_ZN20Abstract3DController19synchDataToRendererEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'render': (
          ('_ZN20Abstract3DController6renderEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'initializeOpenGL': (
          ('_ZN20Abstract3DController16initializeOpenGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addSeries': (
          ('_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DSeries'),
           )),
      ),
      'insertSeries': (
          ('_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address',
                'QtDataVisualization:QAbstract3DSeries'),
           )),
      ),
      'removeSeries': (
          ('_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DSeries'),
           )),
      ),
      'hasSeries': (
          ('_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DSeries'),
           )),
      ),
      'setAxisX': (
          ('_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'axisX': (
          ('_ZNK20Abstract3DController5axisXEv',
           ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           ()),
      ),
      'setAxisY': (
          ('_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'axisY': (
          ('_ZNK20Abstract3DController5axisYEv',
           ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           ()),
      ),
      'setAxisZ': (
          ('_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'axisZ': (
          ('_ZNK20Abstract3DController5axisZEv',
           ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           ()),
      ),
      'addAxis': (
          ('_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'releaseAxis': (
          ('_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'addInputHandler': (
          ('_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInputH'
           'andler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DInputHandler'),
           )),
      ),
      'releaseInputHandler': (
          ('_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3DIn'
           'putHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DInputHandler'),
           )),
      ),
      'setActiveInputHandler': (
          ('_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstract3D'
           'InputHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDataVisualization:QAbstract3DInputHandler'),
           )),
      ),
      'activeInputHandler': (
          ('_ZN20Abstract3DController18activeInputHandlerEv',
           ('address', 'address',
            'QtDataVisualization:QAbstract3DInputHandler'),
           ()),
      ),
      'addTheme': (
          ('_ZN20Abstract3DController8addThemeEP8Q3DTheme',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:Q3DTheme'),
           )),
      ),
      'releaseTheme': (
          ('_ZN20Abstract3DController12releaseThemeEP8Q3DTheme',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:Q3DTheme'),
           )),
      ),
      'setActiveTheme': (
          ('_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:Q3DTheme'),
               ('bool', 'number', ''),
           )),
      ),
      'activeTheme': (
          ('_ZNK20Abstract3DController11activeThemeEv',
           ('address', 'address', 'QtDataVisualization:Q3DTheme'),
           ()),
      ),
      'setSelectionMode': (
          ('_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbstrac'
           't3DGraph13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtDataVisualization:QAbstract3DGraph.SelectionFlag'),
           )),
      ),
      'selectionMode': (
          ('_ZNK20Abstract3DController13selectionModeEv',
           ('int', 'flags',
            'QtDataVisualization:QAbstract3DGraph.SelectionFlag'),
           ()),
      ),
      'setShadowQuality': (
          ('_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGraph'
           '13ShadowQualityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DGraph.ShadowQuality'),
           )),
      ),
      'doSetShadowQuality': (
          ('_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3DGra'
           'ph13ShadowQualityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DGraph.ShadowQuality'),
           )),
      ),
      'shadowQuality': (
          ('_ZNK20Abstract3DController13shadowQualityEv',
           ('int', 'enum',
            'QtDataVisualization:QAbstract3DGraph.ShadowQuality'),
           ()),
      ),
      'shadowsSupported': (
          ('_ZNK20Abstract3DController16shadowsSupportedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'clearSelection': (
          ('_ZN20Abstract3DController14clearSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'touchEvent': (
          ('_ZN20Abstract3DController10touchEventEP11QTouchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6QPo'
           'int',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventRK6Q'
           'Point',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6QPoi'
           'nt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'wheelEvent': (
          ('_ZN20Abstract3DController10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
           )),
      ),
      'handleAxisTitleChangedBySender': (
          ('_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7QOb'
           'ject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelsChangedBySender': (
          ('_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP7QO'
           'bject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisRangeChangedBySender': (
          ('_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7QOb'
           'ject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisSegmentCountChangedBySender': (
          ('_ZN20Abstract3DController37handleAxisSegmentCountChangedBySende'
           'rEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisSubSegmentCountChangedBySender': (
          ('_ZN20Abstract3DController40handleAxisSubSegmentCountChangedBySe'
           'nderEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisAutoAdjustRangeChangedInOrientation': (
          ('_ZN20Abstract3DController45handleAxisAutoAdjustRangeChangedInOr'
           'ientationEN15QAbstract3DAxis15AxisOrientationEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
               ('bool', 'number', ''),
           )),
      ),
      'handleAxisLabelFormatChangedBySender': (
          ('_ZN20Abstract3DController36handleAxisLabelFormatChangedBySender'
           'EP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisReversedChangedBySender': (
          ('_ZN20Abstract3DController33handleAxisReversedChangedBySenderEP7'
           'QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisFormatterDirtyBySender': (
          ('_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderEP7Q'
           'Object',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisLabelAutoRotationChangedBySender': (
          ('_ZN20Abstract3DController42handleAxisLabelAutoRotationChangedBy'
           'SenderEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisTitleVisibilityChangedBySender': (
          ('_ZN20Abstract3DController40handleAxisTitleVisibilityChangedBySe'
           'nderEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleAxisTitleFixedChangedBySender': (
          ('_ZN20Abstract3DController35handleAxisTitleFixedChangedBySenderE'
           'P7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleSeriesVisibilityChangedBySender': (
          ('_ZN20Abstract3DController37handleSeriesVisibilityChangedBySende'
           'rEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handlePendingClick': (
          ('_ZN20Abstract3DController18handlePendingClickEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handlePendingGraphPositionQuery': (
          ('_ZN20Abstract3DController31handlePendingGraphPositionQueryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'adjustAxisRanges': (
          ('_ZN20Abstract3DController16adjustAxisRangesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createDefaultAxis': (
          ('_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DAxis'
           '15AxisOrientationE',
           ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           (
               ('int', 'enum',
                'QtDataVisualization:QAbstract3DAxis.AxisOrientation'),
           )),
      ),
      'startRecordingRemovesAndInserts': (
          ('_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Abstract3DController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Abstract3DController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisX(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *Abstract3DController::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#axisX

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Abstract3DController::axisX() const
    ritual = 'ritual_ZNK20Abstract3DController5axisXEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController5axisXEv'
    address = self.uglySide.call(ritual)
    return QAbstract3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *Abstract3DController::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#axisY

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Abstract3DController::axisY() const
    ritual = 'ritual_ZNK20Abstract3DController5axisYEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController5axisYEv'
    address = self.uglySide.call(ritual)
    return QAbstract3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *Abstract3DController::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#axisZ

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Abstract3DController::axisZ() const
    ritual = 'ritual_ZNK20Abstract3DController5axisZEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController5axisZEv'
    address = self.uglySide.call(ritual)
    return QAbstract3DAxis._cuteAt(address)

  def axes(self) -> QList[QAbstract3DAxis]:
    """
    Calls Qt's 'QList<QAbstract3DAxis *> Abstract3DController::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#axes

    Returns
    -------

    QList[QAbstract3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DAxis *> Abstract3DController::axes() const
    address = self.uglySide.call('ritual_ZNK20Abstract3DController4axesEv')
    return QList[QAbstract3DAxis]._cuteOwning(address)

  def inputHandlers(self) -> QList[QAbstract3DInputHandler]:
    """
    Calls Qt's 'QList<QAbstract3DInputHandler *>
    Abstract3DController::inputHandlers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#inputHandlers

    Returns
    -------

    QList[QAbstract3DInputHandler]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DInputHandler *> Abstract3DController::inputHandlers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController13inputHandlersEv',
    )
    return QList[QAbstract3DInputHandler]._cuteOwning(address)

  def activeTheme(self) -> Optional[Q3DTheme]:
    """
    Calls Qt's 'Q3DTheme *Abstract3DController::activeTheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#activeTheme

    Returns
    -------

    Optional[Q3DTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DTheme *Abstract3DController::activeTheme() const
    ritual = 'ritual_ZNK20Abstract3DController11activeThemeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController11activeThemeEv'
    address = self.uglySide.call(ritual)
    return Q3DTheme._cuteAt(address)

  def themes(self) -> QList[Q3DTheme]:
    """
    Calls Qt's 'QList<Q3DTheme *> Abstract3DController::themes() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#themes

    Returns
    -------

    QList[Q3DTheme]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<Q3DTheme *> Abstract3DController::themes() const
    address = self.uglySide.call('ritual_ZNK20Abstract3DController6themesEv')
    return QList[Q3DTheme]._cuteOwning(address)

  def selectionMode(self) -> QAbstract3DGraph.SelectionFlags:
    """
    Calls Qt's 'QAbstract3DGraph::SelectionFlags
    Abstract3DController::selectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectionMode

    Returns
    -------

    QAbstract3DGraph.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QAbstract3DGraph::SelectionFlags Abstract3DController::selectionMode()
    #      const
    ritual = 'ritual_ZNK20Abstract3DController13selectionModeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController13selectionModeEv'
    return QAbstract3DGraph.SelectionFlags(self.uglySide.call(ritual))

  def shadowQuality(self) -> QAbstract3DGraph.ShadowQuality:
    """
    Calls Qt's 'QAbstract3DGraph::ShadowQuality
    Abstract3DController::shadowQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#shadowQuality

    Returns
    -------

    QAbstract3DGraph.ShadowQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstract3DGraph.ShadowQuality(number)' gives.
    """
    #  QAbstract3DGraph::ShadowQuality Abstract3DController::shadowQuality()
    #      const
    ritual = 'ritual_ZNK20Abstract3DController13shadowQualityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController13shadowQualityEv'
    return QAbstract3DGraph.ShadowQuality(self.uglySide.call(ritual))

  def shadowsSupported(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::shadowsSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#shadowsSupported
    """
    #  bool Abstract3DController::shadowsSupported() const
    ritual = 'ritual_ZNK20Abstract3DController16shadowsSupportedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20Abstract3DController16shadowsSupportedEv'
    return self.uglySide.call(ritual)

  def optimizationHints(self) -> QAbstract3DGraph.OptimizationHints:
    """
    Calls Qt's 'QAbstract3DGraph::OptimizationHints
    Abstract3DController::optimizationHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#optimizationHints

    Returns
    -------

    QAbstract3DGraph.OptimizationHints
      The value standing for the combination Qt gave back.
    """
    #  QAbstract3DGraph::OptimizationHints
    #      Abstract3DController::optimizationHints() const
    return QAbstract3DGraph.OptimizationHints(self.uglySide.call(
        'ritual_ZNK20Abstract3DController17optimizationHintsEv',
    ))

  def isSlicingActive(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::isSlicingActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#isSlicingActive
    """
    #  bool Abstract3DController::isSlicingActive() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController15isSlicingActiveEv',
    )

  def customItems(self) -> QList[QCustom3DItem]:
    """
    Calls Qt's 'QList<QCustom3DItem *> Abstract3DController::customItems()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#customItems

    Returns
    -------

    QList[QCustom3DItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCustom3DItem *> Abstract3DController::customItems() const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController11customItemsEv',
    )
    from . import QCustom3DItem
    return QList[QCustom3DItem]._cuteOwning(address)

  def selectedLabelIndex(self) -> int:
    """
    Calls Qt's 'int Abstract3DController::selectedLabelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectedLabelIndex
    """
    #  int Abstract3DController::selectedLabelIndex() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController18selectedLabelIndexEv',
    )

  def selectedAxis(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *Abstract3DController::selectedAxis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectedAxis

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *Abstract3DController::selectedAxis() const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController12selectedAxisEv',
    )
    return QAbstract3DAxis._cuteAt(address)

  def selectedCustomItemIndex(self) -> int:
    """
    Calls Qt's 'int Abstract3DController::selectedCustomItemIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectedCustomItemIndex
    """
    #  int Abstract3DController::selectedCustomItemIndex() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController23selectedCustomItemIndexEv',
    )

  def selectedCustomItem(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *Abstract3DController::selectedCustomItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectedCustomItem

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *Abstract3DController::selectedCustomItem() const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController18selectedCustomItemEv',
    )
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def isOrthoProjection(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::isOrthoProjection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#isOrthoProjection
    """
    #  bool Abstract3DController::isOrthoProjection() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController17isOrthoProjectionEv',
    )

  def measureFps(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::measureFps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#measureFps
    """
    #  bool Abstract3DController::measureFps() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController10measureFpsEv',
    )

  def currentFps(self) -> float:
    """
    Calls Qt's 'qreal Abstract3DController::currentFps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#currentFps
    """
    #  qreal Abstract3DController::currentFps() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController10currentFpsEv',
    )

  def selectedElement(self) -> QAbstract3DGraph.ElementType:
    """
    Calls Qt's 'QAbstract3DGraph::ElementType
    Abstract3DController::selectedElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectedElement

    Returns
    -------

    QAbstract3DGraph.ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstract3DGraph.ElementType(number)' gives.
    """
    #  QAbstract3DGraph::ElementType Abstract3DController::selectedElement()
    #      const
    return QAbstract3DGraph.ElementType(self.uglySide.call(
        'ritual_ZNK20Abstract3DController15selectedElementEv',
    ))

  def horizontalAspectRatio(self) -> float:
    """
    Calls Qt's 'qreal Abstract3DController::horizontalAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#horizontalAspectRatio
    """
    #  qreal Abstract3DController::horizontalAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController21horizontalAspectRatioEv',
    )

  def reflection(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::reflection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#reflection
    """
    #  bool Abstract3DController::reflection() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController10reflectionEv',
    )

  def reflectivity(self) -> float:
    """
    Calls Qt's 'qreal Abstract3DController::reflectivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#reflectivity
    """
    #  qreal Abstract3DController::reflectivity() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController12reflectivityEv',
    )

  def isPolar(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::isPolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#isPolar
    """
    #  bool Abstract3DController::isPolar() const
    return self.uglySide.call('ritual_ZNK20Abstract3DController7isPolarEv')

  def radialLabelOffset(self) -> float:
    """
    Calls Qt's 'float Abstract3DController::radialLabelOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#radialLabelOffset
    """
    #  float Abstract3DController::radialLabelOffset() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController17radialLabelOffsetEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale Abstract3DController::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale Abstract3DController::locale() const
    address = self.uglySide.call('ritual_ZNK20Abstract3DController6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Abstract3DController::queriedGraphPosition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Abstract3DController::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK20Abstract3DController20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def margin(self) -> float:
    """
    Calls Qt's 'qreal Abstract3DController::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#margin
    """
    #  qreal Abstract3DController::margin() const
    return self.uglySide.call('ritual_ZNK20Abstract3DController6marginEv')

  def isOpenGLES(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::isOpenGLES() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#isOpenGLES
    """
    #  bool Abstract3DController::isOpenGLES() const
    return self.uglySide.call(
        'ritual_ZNK20Abstract3DController10isOpenGLESEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Abstract3DRenderer)
  @overload(NoneType)
  def setRenderer(self, renderer: Optional[Abstract3DRenderer]) -> None:
    """
    Calls Qt's 'void Abstract3DController::setRenderer(Abstract3DRenderer
    *renderer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setRenderer

    Parameters
    ----------

    renderer : Optional[Abstract3DRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::setRenderer(Abstract3DRenderer *renderer)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController11setRendererEP18Abstract3DRenderer',
        self._addressOf(renderer),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::setAxisX(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::setAxisX(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::setAxisY(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::setAxisY(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::setAxisZ(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::setAxisZ(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def setActiveInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::setActiveInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setActiveInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::setActiveInputHandler(
    #      QAbstract3DInputHandler *inputHandler)
    ritual = (
        'ritual_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstrac'
        't3DInputHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController21setActiveInputHandlerEP23QA'
          'bstract3DInputHandler')
    self.uglySide.call(ritual, self._addressOf(inputHandler))

  @overload(Q3DTheme)
  @overload(NoneType)
  @overload(Q3DTheme, bool)
  @overload(NoneType, bool)
  def setActiveTheme(
      self,
      theme: Optional[Q3DTheme],
      force: bool = True,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DController::setActiveTheme(Q3DTheme *theme,
    bool force)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setActiveTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Abstract3DController::setActiveTheme(Q3DTheme *theme, bool force)
    ritual = 'ritual_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb')
    self.uglySide.call(ritual, self._addressOf(theme), force)

  @overload(QAbstract3DGraph.SelectionFlags)
  def setSelectionMode(self, mode: QAbstract3DGraph.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setSelectionMode

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Abstract3DController::setSelectionMode(QAbstract3DGraph::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbst'
        'ract3DGraph13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController16setSelectionModeE6QFlagsIN1'
          '6QAbstract3DGraph13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QAbstract3DGraph.ShadowQuality)
  def setShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::setShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DController::setShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGr'
        'aph13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController16setShadowQualityEN16QAbstra'
          'ct3DGraph13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  @overload(QAbstract3DGraph.OptimizationHints)
  def setOptimizationHints(
      self,
      hints: QAbstract3DGraph.OptimizationHints,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::setOptimizationHints(QAbstract3DGraph::
    OptimizationHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setOptimizationHints

    Parameters
    ----------

    hints : QAbstract3DGraph.OptimizationHints
      Passed on as its number.
    """
    #  void Abstract3DController::setOptimizationHints(QAbstract3DGraph::
    #      OptimizationHints hints)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController20setOptimizationHintsE6QFlagsIN16Q'
        'Abstract3DGraph16OptimizationHintEE',
        hints.value,
    )

  @overload(bool)
  def setSlicingActive(self, isSlicing: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::setSlicingActive(bool isSlicing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setSlicingActive

    Parameters
    ----------

    isSlicing : bool
      Passed on as it is.
    """
    #  void Abstract3DController::setSlicingActive(bool isSlicing)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController16setSlicingActiveEb', isSlicing,
    )

  @overload(bool)
  def setOrthoProjection(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::setOrthoProjection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setOrthoProjection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DController::setOrthoProjection(bool enable)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController18setOrthoProjectionEb', enable,
    )

  @overload(bool)
  def setMeasureFps(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::setMeasureFps(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setMeasureFps

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DController::setMeasureFps(bool enable)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController13setMeasureFpsEb', enable,
    )

  @overload(float)
  def setAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::setAspectRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DController::setAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController14setAspectRatioEd', ratio,
    )

  @overload(float)
  def setHorizontalAspectRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::setHorizontalAspectRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setHorizontalAspectRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DController::setHorizontalAspectRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController24setHorizontalAspectRatioEd', ratio,
    )

  @overload(bool)
  def setReflection(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::setReflection(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setReflection

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DController::setReflection(bool enable)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController13setReflectionEb', enable,
    )

  @overload(float)
  def setReflectivity(self, reflectivity: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::setReflectivity(qreal
    reflectivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setReflectivity

    Parameters
    ----------

    reflectivity : float
      Passed on as it is.
    """
    #  void Abstract3DController::setReflectivity(qreal reflectivity)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController15setReflectivityEd', reflectivity,
    )

  @overload(bool)
  def setPolar(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::setPolar(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#setPolar

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DController::setPolar(bool enable)
    self.uglySide.call('ritual_ZN20Abstract3DController8setPolarEb', enable)

  @overload(float)
  def setRadialLabelOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::setRadialLabelOffset(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setRadialLabelOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Abstract3DController::setRadialLabelOffset(float offset)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController20setRadialLabelOffsetEf', offset,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void Abstract3DController::setLocale(const QLocale &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void Abstract3DController::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::setMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Abstract3DController::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN20Abstract3DController9setMarginEd', margin)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect, Q3DScene)
  @overload(QRect, NoneType)
  @overload(QRect, Q3DScene, QObject)
  @overload(QRect, Q3DScene, NoneType)
  @overload(QRect, NoneType, QObject)
  @overload(QRect, NoneType, NoneType)
  def __init__(
      self,
      initialViewport: QRect,
      scene: Optional[Q3DScene],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Abstract3DController::Abstract3DController(QRect initialViewport,
    Q3DScene *scene, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#Abstract3DController

    Parameters
    ----------

    initialViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Abstract3DController::Abstract3DController(QRect initialViewport,
    #      Q3DScene *scene, QObject *parent)
    self._noteCreation(Abstract3DController, lambda: Rituals.call(
        'ritual_ZN20Abstract3DControllerC1E5QRectP8Q3DSceneP7QObject',
        self._valueOf(initialViewport), self._addressOf(scene),
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

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::isInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#isInitialized
    """
    #  bool Abstract3DController::isInitialized()
    return self.uglySide.call(
        'ritual_ZN20Abstract3DController13isInitializedEv',
    )

  def synchDataToRenderer(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::synchDataToRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#synchDataToRenderer
    """
    #  void Abstract3DController::synchDataToRenderer()
    ritual = 'ritual_ZN20Abstract3DController19synchDataToRendererEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController19synchDataToRendererEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def render(self, defaultFboHandle: int = 0) -> None:
    """
    Calls Qt's 'void Abstract3DController::render(const GLuint
    defaultFboHandle)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#render

    Parameters
    ----------

    defaultFboHandle : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void Abstract3DController::render(const GLuint defaultFboHandle)
    ritual = 'ritual_ZN20Abstract3DController6renderEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController6renderEj'
    self.uglySide.call(ritual, defaultFboHandle)

  def initializeOpenGL(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::initializeOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#initializeOpenGL
    """
    #  void Abstract3DController::initializeOpenGL()
    self.uglySide.call('ritual_ZN20Abstract3DController16initializeOpenGLEv')

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Abstract3DController::addSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::addSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeri'
          'es')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(int, QAbstract3DSeries)
  @overload(int, NoneType)
  def insertSeries(
      self,
      index: int,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Abstract3DController::insertSeries(int index,
    QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::insertSeries(int index, QAbstract3DSeries
    #      *series)
    ritual = (
        'ritual_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSerie'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController12insertSeriesEiP17QAbstract3'
          'DSeries')
    self.uglySide.call(ritual, index, self._addressOf(series))

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void Abstract3DController::removeSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::removeSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController12removeSeriesEP17QAbstract3D'
          'Series')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QAbstract3DSeries]) -> bool:
    """
    Calls Qt's 'bool Abstract3DController::hasSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#hasSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Abstract3DController::hasSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeri'
          'es')
    return self.uglySide.call(ritual, self._addressOf(series))

  def seriesList(self) -> QList[QAbstract3DSeries]:
    """
    Calls Qt's 'QList<QAbstract3DSeries *>
    Abstract3DController::seriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#seriesList

    Returns
    -------

    QList[QAbstract3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DSeries *> Abstract3DController::seriesList()
    address = self.uglySide.call(
        'ritual_ZN20Abstract3DController10seriesListEv',
    )
    from . import QAbstract3DSeries
    return QList[QAbstract3DSeries]._cuteOwning(address)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::addAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::addAxis(QAbstract3DAxis *axis)
    ritual = 'ritual_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::releaseAxis(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::releaseAxis(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController11releaseAxisEP15QAbstract3DA'
          'xis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def addInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::addInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#addInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::addInputHandler(QAbstract3DInputHandler
    #      *inputHandler)
    ritual = (
        'ritual_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInp'
        'utHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController15addInputHandlerEP23QAbstrac'
          't3DInputHandler')
    self.uglySide.call(ritual, self._addressOf(inputHandler))

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def releaseInputHandler(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#releaseInputHandler

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
    #      *inputHandler)
    ritual = (
        'ritual_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3'
        'DInputHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController19releaseInputHandlerEP23QAbs'
          'tract3DInputHandler')
    self.uglySide.call(ritual, self._addressOf(inputHandler))

  def activeInputHandler(self) -> Optional[QAbstract3DInputHandler]:
    """
    Calls Qt's 'QAbstract3DInputHandler
    *Abstract3DController::activeInputHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#activeInputHandler

    Returns
    -------

    Optional[QAbstract3DInputHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DInputHandler *Abstract3DController::activeInputHandler()
    ritual = 'ritual_ZN20Abstract3DController18activeInputHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController18activeInputHandlerEv'
    address = self.uglySide.call(ritual)
    return QAbstract3DInputHandler._cuteAt(address)

  @overload(Q3DTheme)
  @overload(NoneType)
  def addTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void Abstract3DController::addTheme(Q3DTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#addTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::addTheme(Q3DTheme *theme)
    ritual = 'ritual_ZN20Abstract3DController8addThemeEP8Q3DTheme'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController8addThemeEP8Q3DTheme'
    self.uglySide.call(ritual, self._addressOf(theme))

  @overload(Q3DTheme)
  @overload(NoneType)
  def releaseTheme(self, theme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void Abstract3DController::releaseTheme(Q3DTheme *theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#releaseTheme

    Parameters
    ----------

    theme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::releaseTheme(Q3DTheme *theme)
    ritual = 'ritual_ZN20Abstract3DController12releaseThemeEP8Q3DTheme'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController12releaseThemeEP8Q3DTheme'
    self.uglySide.call(ritual, self._addressOf(theme))

  @overload(QAbstract3DGraph.ShadowQuality)
  def doSetShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::doSetShadowQuality(QAbstract3DGraph::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#doSetShadowQuality

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DController::doSetShadowQuality(QAbstract3DGraph::
    #      ShadowQuality quality)
    ritual = (
        'ritual_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3D'
        'Graph13ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController18doSetShadowQualityEN16QAbst'
          'ract3DGraph13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  def scene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *Abstract3DController::scene()'.

    Qt's own words: https://doc.qt.io/qt-6/abstract3dcontroller.html#scene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *Abstract3DController::scene()
    address = self.uglySide.call('ritual_ZN20Abstract3DController5sceneEv')
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  def markDataDirty(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::markDataDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#markDataDirty
    """
    #  void Abstract3DController::markDataDirty()
    self.uglySide.call('ritual_ZN20Abstract3DController13markDataDirtyEv')

  def markSeriesVisualsDirty(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::markSeriesVisualsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#markSeriesVisualsDirty
    """
    #  void Abstract3DController::markSeriesVisualsDirty()
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22markSeriesVisualsDirtyEv',
    )

  @overload(QOpenGLFramebufferObject)
  @overload(NoneType)
  def requestRender(self, fbo: Optional[QOpenGLFramebufferObject]) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::requestRender(QOpenGLFramebufferObject *fbo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#requestRender

    Parameters
    ----------

    fbo : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::requestRender(QOpenGLFramebufferObject
    #      *fbo)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController13requestRenderEP24QOpenGLFramebuff'
        'erObject',
        self._addressOf(fbo),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(self, item: Optional[QCustom3DItem]) -> int:
    """
    Calls Qt's 'int Abstract3DController::addCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int Abstract3DController::addCustomItem(QCustom3DItem *item)
    return self.uglySide.call(
        'ritual_ZN20Abstract3DController13addCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  def deleteCustomItems(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::deleteCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#deleteCustomItems
    """
    #  void Abstract3DController::deleteCustomItems()
    self.uglySide.call(
        'ritual_ZN20Abstract3DController17deleteCustomItemsEv',
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def deleteCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void Abstract3DController::deleteCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#deleteCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::deleteCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController16deleteCustomItemEP13QCustom3DItem',
        self._addressOf(item),
    )

  @overload(QVector3D)
  def deleteCustomItem(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Abstract3DController::deleteCustomItem(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#deleteCustomItem

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Abstract3DController::deleteCustomItem(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController16deleteCustomItemERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QCustom3DItem)
  @overload(NoneType)
  def releaseCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void Abstract3DController::releaseCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#releaseCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::releaseCustomItem(QCustom3DItem *item)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController17releaseCustomItemEP13QCustom3DIte'
        'm',
        self._addressOf(item),
    )

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'qreal Abstract3DController::aspectRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#aspectRatio
    """
    #  qreal Abstract3DController::aspectRatio()
    return self.uglySide.call(
        'ritual_ZN20Abstract3DController11aspectRatioEv',
    )

  def emitNeedRender(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::emitNeedRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#emitNeedRender
    """
    #  void Abstract3DController::emitNeedRender()
    self.uglySide.call('ritual_ZN20Abstract3DController14emitNeedRenderEv')

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#clearSelection
    """
    #  void Abstract3DController::clearSelection()
    self.uglySide.call('ritual_ZN20Abstract3DController14clearSelectionEv')

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void Abstract3DController::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController21mouseDoubleClickEventEP11QM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void Abstract3DController::touchEvent(QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN20Abstract3DController10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController10touchEventEP11QTouchEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mousePressEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DController::mousePressEvent(QMouseEvent
    *event, const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Abstract3DController::mousePressEvent(QMouseEvent *event, const
    #      QPoint &mousePos)
    ritual = (
        'ritual_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6'
        'QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController15mousePressEventEP11QMouseEv'
          'entRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseReleaseEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DController::mouseReleaseEvent(QMouseEvent
    *event, const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Abstract3DController::mouseReleaseEvent(QMouseEvent *event, const
    #      QPoint &mousePos)
    ritual = (
        'ritual_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventR'
        'K6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController17mouseReleaseEventEP11QMouse'
          'EventRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseMoveEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Abstract3DController::mouseMoveEvent(QMouseEvent *event,
    const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Abstract3DController::mouseMoveEvent(QMouseEvent *event, const
    #      QPoint &mousePos)
    ritual = (
        'ritual_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6Q'
        'Point')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController14mouseMoveEventEP11QMouseEve'
          'ntRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void Abstract3DController::wheelEvent(QWheelEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN20Abstract3DController10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController10wheelEventEP11QWheelEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisTitleChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisTitleChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7'
        'QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController30handleAxisTitleChangedBySen'
          'derEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelsChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisLabelsChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisLabelsChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP'
        '7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController31handleAxisLabelsChangedBySe'
          'nderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisRangeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisRangeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7'
        'QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController30handleAxisRangeChangedBySen'
          'derEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisSegmentCountChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisSegmentCountChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisSegmentCountChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN20Abstract3DController37handleAxisSegmentCountChangedBySe'
        'nderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController37handleAxisSegmentCountChang'
          'edBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisSubSegmentCountChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisSubSegmentCountChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisSubSegmentCountChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN20Abstract3DController40handleAxisSubSegmentCountChangedB'
        'ySenderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController40handleAxisSubSegmentCountCh'
          'angedBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void Abstract3DController::
    #      handleAxisAutoAdjustRangeChangedInOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation, bool autoAdjust)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController45handleAxisAutoAdjustRangeChangedI'
        'nOrientationEN15QAbstract3DAxis15AxisOrientationEb',
        orientation.value, autoAdjust,
    )

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelFormatChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisLabelFormatChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Abstract3DController::handleAxisLabelFormatChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController36handleAxisLabelFormatChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController36handleAxisLabelFormatChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisReversedChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisReversedChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisReversedChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController33handleAxisReversedChangedBySender'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController33handleAxisReversedChangedBy'
          'SenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisFormatterDirtyBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisFormatterDirtyBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisFormatterDirtyBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderE'
        'P7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController32handleAxisFormatterDirtyByS'
          'enderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisLabelAutoRotationChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisLabelAutoRotationChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisLabelAutoRotationChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN20Abstract3DController42handleAxisLabelAutoRotationChange'
        'dBySenderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController42handleAxisLabelAutoRotation'
          'ChangedBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisTitleVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisTitleVisibilityChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN20Abstract3DController40handleAxisTitleVisibilityChangedB'
        'ySenderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController40handleAxisTitleVisibilityCh'
          'angedBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisTitleFixedChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN20Abstract3DController35handleAxisTitleFixedChangedBySend'
        'erEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController35handleAxisTitleFixedChanged'
          'BySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::handleSeriesVisibilityChangedBySender(
    #      QObject *sender)
    ritual = (
        'ritual_ZN20Abstract3DController37handleSeriesVisibilityChangedBySe'
        'nderEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController37handleSeriesVisibilityChang'
          'edBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def handlePendingClick(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::handlePendingClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handlePendingClick
    """
    #  void Abstract3DController::handlePendingClick()
    ritual = 'ritual_ZN20Abstract3DController18handlePendingClickEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Abstract3DController18handlePendingClickEv'
    self.uglySide.call(ritual)

  def handlePendingGraphPositionQuery(self) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handlePendingGraphPositionQuery()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html
    """
    #  void Abstract3DController::handlePendingGraphPositionQuery()
    ritual = (
        'ritual_ZN20Abstract3DController31handlePendingGraphPositionQueryEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController31handlePendingGraphPositionQ'
          'ueryEv')
    self.uglySide.call(ritual)

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#adjustAxisRanges
    """
    #  void Abstract3DController::adjustAxisRanges()
    self.uglySide.call('ritual_ZN20Abstract3DController16adjustAxisRangesEv')

  def markSeriesItemLabelsDirty(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::markSeriesItemLabelsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html
    """
    #  void Abstract3DController::markSeriesItemLabelsDirty()
    self.uglySide.call(
        'ritual_ZN20Abstract3DController25markSeriesItemLabelsDirtyEv',
    )

  def destroyRenderer(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::destroyRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#destroyRenderer
    """
    #  void Abstract3DController::destroyRenderer()
    self.uglySide.call('ritual_ZN20Abstract3DController15destroyRendererEv')

  @overload(str)
  def handleAxisTitleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisTitleChanged(const
    QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleAxisTitleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DController::handleAxisTitleChanged(const QString
    #      &title)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22handleAxisTitleChangedERK7QString',
        title,
    )

  def handleAxisLabelsChanged(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleAxisLabelsChanged
    """
    #  void Abstract3DController::handleAxisLabelsChanged()
    self.uglySide.call(
        'ritual_ZN20Abstract3DController23handleAxisLabelsChangedEv',
    )

  @overload(float, float)
  def handleAxisRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisRangeChanged(float min,
    float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleAxisRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisRangeChanged(float min, float
    #      max)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22handleAxisRangeChangedEff',
        min, max,
    )

  @overload(int)
  def handleAxisSegmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisSegmentCountChanged(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisSegmentCountChanged(int count)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController29handleAxisSegmentCountChangedEi',
        count,
    )

  @overload(int)
  def handleAxisSubSegmentCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisSubSegmentCountChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisSubSegmentCountChanged(int count)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController32handleAxisSubSegmentCountChangedE'
        'i',
        count,
    )

  @overload(bool)
  def handleAxisAutoAdjustRangeChanged(self, autoAdjust: bool) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisAutoAdjustRangeChanged(bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    autoAdjust : bool
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisAutoAdjustRangeChanged(bool
    #      autoAdjust)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController32handleAxisAutoAdjustRangeChangedE'
        'b',
        autoAdjust,
    )

  @overload(str)
  def handleAxisLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisLabelFormatChanged(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Abstract3DController::handleAxisLabelFormatChanged(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController28handleAxisLabelFormatChangedERK7Q'
        'String',
        format,
    )

  @overload(bool)
  def handleAxisReversedChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisReversedChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisReversedChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController25handleAxisReversedChangedEb',
        enable,
    )

  def handleAxisFormatterDirty(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisFormatterDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleAxisFormatterDirty
    """
    #  void Abstract3DController::handleAxisFormatterDirty()
    self.uglySide.call(
        'ritual_ZN20Abstract3DController24handleAxisFormatterDirtyEv',
    )

  @overload(float)
  def handleAxisLabelAutoRotationChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisLabelAutoRotationChanged(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisLabelAutoRotationChanged(float
    #      angle)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController34handleAxisLabelAutoRotationChange'
        'dEf',
        angle,
    )

  @overload(bool)
  def handleAxisTitleVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleAxisTitleVisibilityChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisTitleVisibilityChanged(bool
    #      visible)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController32handleAxisTitleVisibilityChangedE'
        'b',
        visible,
    )

  @overload(bool)
  def handleAxisTitleFixedChanged(self, fixed: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleAxisTitleFixedChanged(bool
    fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    fixed : bool
      Passed on as it is.
    """
    #  void Abstract3DController::handleAxisTitleFixedChanged(bool fixed)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController27handleAxisTitleFixedChangedEb',
        fixed,
    )

  @overload(QAbstract3DInputHandler.InputView)
  def handleInputViewChanged(
      self,
      view: QAbstract3DInputHandler.InputView,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleInputViewChanged(QAbstract3DInputHandler::
    InputView view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleInputViewChanged

    Parameters
    ----------

    view : QAbstract3DInputHandler.InputView
      Passed on as its number.
    """
    #  void Abstract3DController::handleInputViewChanged(
    #      QAbstract3DInputHandler::InputView view)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22handleInputViewChangedEN23QAbstra'
        'ct3DInputHandler9InputViewE',
        view.value,
    )

  @overload(QPoint)
  def handleInputPositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleInputPositionChanged(const
    QPoint &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Abstract3DController::handleInputPositionChanged(const QPoint
    #      &position)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController26handleInputPositionChangedERK6QPo'
        'int',
        self._valueOf(position),
    )

  @overload(bool)
  def handleSeriesVisibilityChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleSeriesVisibilityChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void Abstract3DController::handleSeriesVisibilityChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController29handleSeriesVisibilityChangedEb',
        visible,
    )

  @overload(Q3DTheme.ColorStyle)
  def handleThemeColorStyleChanged(self, style: Q3DTheme.ColorStyle) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeColorStyleChanged(Q3DTheme::ColorStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    style : Q3DTheme.ColorStyle
      Passed on as its number.
    """
    #  void Abstract3DController::handleThemeColorStyleChanged(Q3DTheme::
    #      ColorStyle style)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController28handleThemeColorStyleChangedEN8Q3'
        'DTheme10ColorStyleE',
        style.value,
    )

  @overload(QList[QColor])
  def handleThemeBaseColorsChanged(self, color: QList[QColor]) -> None:
    """
    Calls Qt's 'void Abstract3DController::handleThemeBaseColorsChanged(const
    QList<QColor> &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    color : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DController::handleThemeBaseColorsChanged(const
    #      QList<QColor> &color)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController28handleThemeBaseColorsChangedERK5Q'
        'ListI6QColorE',
        self._valueOf(color),
    )

  @overload(QList[QLinearGradient])
  def handleThemeBaseGradientsChanged(
      self,
      gradient: QList[QLinearGradient],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeBaseGradientsChanged(const
    QList<QLinearGradient> &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    gradient : QList[QLinearGradient]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Abstract3DController::handleThemeBaseGradientsChanged(const
    #      QList<QLinearGradient> &gradient)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController31handleThemeBaseGradientsChangedER'
        'K5QListI15QLinearGradientE',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def handleThemeSingleHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeSingleHighlightColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void
    #      Abstract3DController::handleThemeSingleHighlightColorChanged(const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController38handleThemeSingleHighlightColorCh'
        'angedERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def handleThemeSingleHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeSingleHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Abstract3DController::handleThemeSingleHighlightGradientChanged(
    #      const QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController41handleThemeSingleHighlightGradien'
        'tChangedERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(QColor)
  def handleThemeMultiHighlightColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeMultiHighlightColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Abstract3DController::handleThemeMultiHighlightColorChanged(const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController37handleThemeMultiHighlightColorCha'
        'ngedERK6QColor',
        self._valueOf(color),
    )

  @overload(QLinearGradient)
  def handleThemeMultiHighlightGradientChanged(
      self,
      gradient: QLinearGradient,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeMultiHighlightGradientChanged(const
    QLinearGradient &gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void Abstract3DController::handleThemeMultiHighlightGradientChanged(
    #      const QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController40handleThemeMultiHighlightGradient'
        'ChangedERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(Q3DTheme.Theme)
  def handleThemeTypeChanged(self, theme: Q3DTheme.Theme) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleThemeTypeChanged(Q3DTheme::Theme theme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#handleThemeTypeChanged

    Parameters
    ----------

    theme : Q3DTheme.Theme
      Passed on as its number.
    """
    #  void Abstract3DController::handleThemeTypeChanged(Q3DTheme::Theme
    #      theme)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22handleThemeTypeChangedEN8Q3DTheme'
        '5ThemeE',
        theme.value,
    )

  @overload(QAbstract3DGraph.ShadowQuality)
  def handleRequestShadowQuality(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::handleRequestShadowQuality(QAbstract3DGraph::
    ShadowQuality quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DController::handleRequestShadowQuality(
    #      QAbstract3DGraph::ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController26handleRequestShadowQualityEN16QAb'
        'stract3DGraph13ShadowQualityE',
        quality.value,
    )

  def updateCustomItem(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::updateCustomItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#updateCustomItem
    """
    #  void Abstract3DController::updateCustomItem()
    self.uglySide.call('ritual_ZN20Abstract3DController16updateCustomItemEv')

  @overload(QAbstract3DGraph.ShadowQuality)
  def shadowQualityChanged(
      self,
      quality: QAbstract3DGraph.ShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::shadowQualityChanged(QAbstract3DGraph::
    ShadowQuality quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#shadowQualityChanged

    Parameters
    ----------

    quality : QAbstract3DGraph.ShadowQuality
      Passed on as its number.
    """
    #  void Abstract3DController::shadowQualityChanged(QAbstract3DGraph::
    #      ShadowQuality quality)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController20shadowQualityChangedEN16QAbstract'
        '3DGraph13ShadowQualityE',
        quality.value,
    )

  @overload(QAbstract3DInputHandler)
  @overload(NoneType)
  def activeInputHandlerChanged(
      self,
      inputHandler: Optional[QAbstract3DInputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::activeInputHandlerChanged(QAbstract3DInputHandler
    *inputHandler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    inputHandler : Optional[QAbstract3DInputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::activeInputHandlerChanged(
    #      QAbstract3DInputHandler *inputHandler)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController25activeInputHandlerChangedEP23QAbs'
        'tract3DInputHandler',
        self._addressOf(inputHandler),
    )

  @overload(Q3DTheme)
  @overload(NoneType)
  def activeThemeChanged(self, activeTheme: Optional[Q3DTheme]) -> None:
    """
    Calls Qt's 'void Abstract3DController::activeThemeChanged(Q3DTheme
    *activeTheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#activeThemeChanged

    Parameters
    ----------

    activeTheme : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::activeThemeChanged(Q3DTheme *activeTheme)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController18activeThemeChangedEP8Q3DTheme',
        self._addressOf(activeTheme),
    )

  @overload(QAbstract3DGraph.SelectionFlags)
  def selectionModeChanged(
      self,
      mode: QAbstract3DGraph.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::selectionModeChanged(QAbstract3DGraph::
    SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#selectionModeChanged

    Parameters
    ----------

    mode : QAbstract3DGraph.SelectionFlags
      Passed on as its number.
    """
    #  void Abstract3DController::selectionModeChanged(QAbstract3DGraph::
    #      SelectionFlags mode)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController20selectionModeChangedE6QFlagsIN16Q'
        'Abstract3DGraph13SelectionFlagEE',
        mode.value,
    )

  def needRender(self) -> None:
    """
    Calls Qt's 'void Abstract3DController::needRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#needRender
    """
    #  void Abstract3DController::needRender()
    self.uglySide.call('ritual_ZN20Abstract3DController10needRenderEv')

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::axisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::axisXChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController12axisXChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::axisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::axisYChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController12axisYChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Abstract3DController::axisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Abstract3DController::axisZChanged(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController12axisZChangedEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DGraph.ElementType)
  def elementSelected(self, type: QAbstract3DGraph.ElementType) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::elementSelected(QAbstract3DGraph::ElementType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#elementSelected

    Parameters
    ----------

    type : QAbstract3DGraph.ElementType
      Passed on as its number.
    """
    #  void Abstract3DController::elementSelected(QAbstract3DGraph::
    #      ElementType type)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController15elementSelectedEN16QAbstract3DGra'
        'ph11ElementTypeE',
        type.value,
    )

  @overload(bool)
  def measureFpsChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::measureFpsChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#measureFpsChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Abstract3DController::measureFpsChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController17measureFpsChangedEb', enabled,
    )

  @overload(float)
  def currentFpsChanged(self, fps: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::currentFpsChanged(qreal fps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#currentFpsChanged

    Parameters
    ----------

    fps : float
      Passed on as it is.
    """
    #  void Abstract3DController::currentFpsChanged(qreal fps)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController17currentFpsChangedEd', fps,
    )

  @overload(bool)
  def orthoProjectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::orthoProjectionChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#orthoProjectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Abstract3DController::orthoProjectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController22orthoProjectionChangedEb', enabled,
    )

  @overload(float)
  def aspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::aspectRatioChanged(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#aspectRatioChanged

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DController::aspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController18aspectRatioChangedEd', ratio,
    )

  @overload(float)
  def horizontalAspectRatioChanged(self, ratio: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::horizontalAspectRatioChanged(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void Abstract3DController::horizontalAspectRatioChanged(qreal ratio)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController28horizontalAspectRatioChangedEd',
        ratio,
    )

  @overload(QAbstract3DGraph.OptimizationHints)
  def optimizationHintsChanged(
      self,
      hints: QAbstract3DGraph.OptimizationHints,
  ) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::optimizationHintsChanged(QAbstract3DGraph::
    OptimizationHints hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#optimizationHintsChanged

    Parameters
    ----------

    hints : QAbstract3DGraph.OptimizationHints
      Passed on as its number.
    """
    #  void Abstract3DController::optimizationHintsChanged(QAbstract3DGraph::
    #      OptimizationHints hints)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController24optimizationHintsChangedE6QFlagsI'
        'N16QAbstract3DGraph16OptimizationHintEE',
        hints.value,
    )

  @overload(bool)
  def polarChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::polarChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#polarChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Abstract3DController::polarChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController12polarChangedEb', enabled,
    )

  @overload(float)
  def radialLabelOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::radialLabelOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#radialLabelOffsetChanged

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Abstract3DController::radialLabelOffsetChanged(float offset)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController24radialLabelOffsetChangedEf',
        offset,
    )

  @overload(bool)
  def reflectionChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Abstract3DController::reflectionChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#reflectionChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Abstract3DController::reflectionChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController17reflectionChangedEb', enabled,
    )

  @overload(float)
  def reflectivityChanged(self, reflectivity: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::reflectivityChanged(qreal
    reflectivity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#reflectivityChanged

    Parameters
    ----------

    reflectivity : float
      Passed on as it is.
    """
    #  void Abstract3DController::reflectivityChanged(qreal reflectivity)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController19reflectivityChangedEd',
        reflectivity,
    )

  @overload(QLocale)
  def localeChanged(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void Abstract3DController::localeChanged(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#localeChanged

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void Abstract3DController::localeChanged(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController13localeChangedERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QVector3D)
  def queriedGraphPositionChanged(self, data: QVector3D) -> None:
    """
    Calls Qt's 'void Abstract3DController::queriedGraphPositionChanged(const
    QVector3D &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Parameters
    ----------

    data : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Abstract3DController::queriedGraphPositionChanged(const QVector3D
    #      &data)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController27queriedGraphPositionChangedERK9QV'
        'ector3D',
        self._valueOf(data),
    )

  @overload(float)
  def marginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void Abstract3DController::marginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#marginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void Abstract3DController::marginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN20Abstract3DController13marginChangedEd', margin,
    )

  @overload(QAbstract3DAxis.AxisOrientation)
  def createDefaultAxis(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *Abstract3DController::createDefaultAxis(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#createDefaultAxis

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis
    #      *Abstract3DController::createDefaultAxis(QAbstract3DAxis::
    #      AxisOrientation orientation)
    ritual = (
        'ritual_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DA'
        'xis15AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController17createDefaultAxisEN15QAbstr'
          'act3DAxis15AxisOrientationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstract3DAxis._cuteAt(address)

  def createDefaultValueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis
    *Abstract3DController::createDefaultValueAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html#createDefaultValueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Abstract3DController::createDefaultValueAxis()
    address = self.uglySide.call(
        'ritual_ZN20Abstract3DController22createDefaultValueAxisEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def createDefaultCategoryAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis
    *Abstract3DController::createDefaultCategoryAxis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *Abstract3DController::createDefaultCategoryAxis()
    address = self.uglySide.call(
        'ritual_ZN20Abstract3DController25createDefaultCategoryAxisEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def startRecordingRemovesAndInserts(self) -> None:
    """
    Calls Qt's 'void
    Abstract3DController::startRecordingRemovesAndInserts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstract3dcontroller.html
    """
    #  void Abstract3DController::startRecordingRemovesAndInserts()
    ritual = (
        'ritual_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20Abstract3DController31startRecordingRemovesAndIns'
          'ertsEv')
    self.uglySide.call(ritual)

  @staticmethod
  def setAxisHelper(*__, **_) -> Never:
    """
    Qt's 'void
    Abstract3DController::setAxisHelper(QAbstract3DAxis::AxisOrientation
    orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Abstract3DController.setAxisHelper' has no cute function yet. "
        "Qt's 'void "
        "Abstract3DController::setAxisHelper(QAbstract3DAxis::AxisOrientatio"
        "n orientation, QAbstract3DAxis *axis, QAbstract3DAxis **axisPtr)': "
        "takes a type Python has no way to hand over yet.")
