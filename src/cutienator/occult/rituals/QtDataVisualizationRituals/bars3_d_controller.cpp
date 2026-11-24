//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/bars3dcontroller_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/bars3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtDataVisualization/qbar3dseries.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on Bars3DController may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnBars3DController : Bars3DController {
  using Bars3DController::createDefaultAxis;
};

//  A Bars3DController that Python can take functions over in. Every Bars3DController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteBars3DControllerCall0)(const void *, int *);
typedef void (*CuteBars3DControllerCall1)(const void *, int *);
typedef void (*CuteBars3DControllerCall2)(const void *, int, int *);
typedef void (*CuteBars3DControllerCall3)(const void *, int *);
typedef void (*CuteBars3DControllerCall4)(const void *, int, bool, int *);
typedef void (*CuteBars3DControllerCall5)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall6)(const void *, int *);
typedef void (*CuteBars3DControllerCall7)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteBars3DControllerCall8)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteBars3DControllerCall9)(const void *, QBar3DSeries *, int *);
typedef void * (*CuteBars3DControllerCall10)(const void *, int *);
typedef void (*CuteBars3DControllerCall11)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteBars3DControllerCall12)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteBars3DControllerCall13)(const void *, int, QAbstract3DSeries *, int *);
typedef void (*CuteBars3DControllerCall14)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall15)(const void *, int *);
typedef void * (*CuteBars3DControllerCall16)(const void *, int, int *);
typedef void (*CuteBars3DControllerCall17)(const void *, GLuint, int *);
typedef bool (*CuteBars3DControllerCall18)(const void *, QAbstract3DSeries *, int *);
typedef void * (*CuteBars3DControllerCall19)(const void *, int *);
typedef void (*CuteBars3DControllerCall20)(const void *, QAbstract3DAxis *, int *);
typedef void * (*CuteBars3DControllerCall21)(const void *, int *);
typedef void * (*CuteBars3DControllerCall22)(const void *, int *);
typedef void (*CuteBars3DControllerCall23)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteBars3DControllerCall24)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteBars3DControllerCall25)(const void *, QAbstract3DInputHandler *, int *);
typedef void (*CuteBars3DControllerCall26)(const void *, QAbstract3DInputHandler *, int *);
typedef void (*CuteBars3DControllerCall27)(const void *, QAbstract3DInputHandler *, int *);
typedef void * (*CuteBars3DControllerCall28)(const void *, int *);
typedef void (*CuteBars3DControllerCall29)(const void *, Q3DTheme *, int *);
typedef void (*CuteBars3DControllerCall30)(const void *, Q3DTheme *, int *);
typedef void (*CuteBars3DControllerCall31)(const void *, Q3DTheme *, bool, int *);
typedef void * (*CuteBars3DControllerCall32)(const void *, int *);
typedef int (*CuteBars3DControllerCall33)(const void *, int *);
typedef void (*CuteBars3DControllerCall34)(const void *, int, int *);
typedef void (*CuteBars3DControllerCall35)(const void *, int, int *);
typedef int (*CuteBars3DControllerCall36)(const void *, int *);
typedef bool (*CuteBars3DControllerCall37)(const void *, int *);
typedef void (*CuteBars3DControllerCall38)(const void *, QMouseEvent *, int *);
typedef void (*CuteBars3DControllerCall39)(const void *, QTouchEvent *, int *);
typedef void (*CuteBars3DControllerCall40)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteBars3DControllerCall41)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteBars3DControllerCall42)(const void *, QMouseEvent *, const QPoint *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteBars3DControllerCall43)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteBars3DControllerCall44)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall45)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall46)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall47)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall48)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall49)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall50)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall51)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall52)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall53)(const void *, QObject *, int *);
typedef void (*CuteBars3DControllerCall54)(const void *, int *);
typedef void (*CuteBars3DControllerCall55)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBars3DControllerCall56)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBars3DControllerCall57)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DControllerCall58)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DControllerCall59)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DControllerCall60)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DControllerCall61)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DControllerCall62)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBars3DController : public Bars3DController {
public:
  using Bars3DController::Bars3DController;
  void *taken[63] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20Abstract3DController16initializeOpenGLEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController19synchDataToRendererEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14clearSelectionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18handlePendingClickEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSeries")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16Bars3DController13primarySeriesEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSeries")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7QObject")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16adjustAxisRangesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController6renderEj")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisXEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisYEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisZEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInputHandler")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3DInputHandler")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstract3DInputHandler")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18activeInputHandlerEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8addThemeEP8Q3DTheme")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12releaseThemeEP8Q3DTheme")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController11activeThemeEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController13selectionModeEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController13shadowQualityEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController16shadowsSupportedEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController10touchEventEP11QTouchEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6QPoint")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventRK6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6QPoint")) {
      taken[42] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN20Abstract3DController10wheelEventEP11QWheelEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31handlePendingGraphPositionQueryEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv")) {
      taken[55] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[60] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[61] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[62] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Bars3DController::initializeOpenGL()
  void initializeOpenGL() override {
    if (taken[0]) {
      int handled = 0;
      CuteBars3DControllerCall0 call = reinterpret_cast<CuteBars3DControllerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DController::initializeOpenGL();
  }

  //  void Bars3DController::synchDataToRenderer()
  void synchDataToRenderer() override {
    if (taken[1]) {
      int handled = 0;
      CuteBars3DControllerCall1 call = reinterpret_cast<CuteBars3DControllerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DController::synchDataToRenderer();
  }

  //  void
  //      Bars3DController::setSelectionMode(QAbstract3DGraph::SelectionFla
  //      gs mode)
  void setSelectionMode(QAbstract3DGraph::SelectionFlags mode) override {
    if (taken[2]) {
      int handled = 0;
      CuteBars3DControllerCall2 call = reinterpret_cast<CuteBars3DControllerCall2>(taken[2]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    Bars3DController::setSelectionMode(mode);
  }

  //  void Bars3DController::clearSelection()
  void clearSelection() override {
    if (taken[3]) {
      int handled = 0;
      CuteBars3DControllerCall3 call = reinterpret_cast<CuteBars3DControllerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DController::clearSelection();
  }

  //  void Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(
  //      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[4]) {
      int handled = 0;
      CuteBars3DControllerCall4 call = reinterpret_cast<CuteBars3DControllerCall4>(taken[4]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
    Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(orientation, autoAdjust);
  }

  //  void Bars3DController::handleSeriesVisibilityChangedBySender(QObject
  //      *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[5]) {
      int handled = 0;
      CuteBars3DControllerCall5 call = reinterpret_cast<CuteBars3DControllerCall5>(taken[5]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Bars3DController::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void Bars3DController::handlePendingClick()
  void handlePendingClick() override {
    if (taken[6]) {
      int handled = 0;
      CuteBars3DControllerCall6 call = reinterpret_cast<CuteBars3DControllerCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DController::handlePendingClick();
  }

  //  void Bars3DController::setAxisX(QAbstract3DAxis *axis)
  void setAxisX(QAbstract3DAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteBars3DControllerCall7 call = reinterpret_cast<CuteBars3DControllerCall7>(taken[7]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Bars3DController::setAxisX(axis);
  }

  //  void Bars3DController::setAxisZ(QAbstract3DAxis *axis)
  void setAxisZ(QAbstract3DAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteBars3DControllerCall8 call = reinterpret_cast<CuteBars3DControllerCall8>(taken[8]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Bars3DController::setAxisZ(axis);
  }

  //  void Bars3DController::setPrimarySeries(QBar3DSeries *series)
  void setPrimarySeries(QBar3DSeries *series) override {
    if (taken[9]) {
      int handled = 0;
      CuteBars3DControllerCall9 call = reinterpret_cast<CuteBars3DControllerCall9>(taken[9]);
      call(this, series, &handled);
      if (handled) return;
    }
    Bars3DController::setPrimarySeries(series);
  }

  //  QBar3DSeries *Bars3DController::primarySeries() const
  QBar3DSeries *primarySeries() const override {
    if (taken[10]) {
      int handled = 0;
      CuteBars3DControllerCall10 call = reinterpret_cast<CuteBars3DControllerCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QBar3DSeries *>(given);
    }
    return Bars3DController::primarySeries();
  }

  //  void Bars3DController::addSeries(QAbstract3DSeries *series)
  void addSeries(QAbstract3DSeries *series) override {
    if (taken[11]) {
      int handled = 0;
      CuteBars3DControllerCall11 call = reinterpret_cast<CuteBars3DControllerCall11>(taken[11]);
      call(this, series, &handled);
      if (handled) return;
    }
    Bars3DController::addSeries(series);
  }

  //  void Bars3DController::removeSeries(QAbstract3DSeries *series)
  void removeSeries(QAbstract3DSeries *series) override {
    if (taken[12]) {
      int handled = 0;
      CuteBars3DControllerCall12 call = reinterpret_cast<CuteBars3DControllerCall12>(taken[12]);
      call(this, series, &handled);
      if (handled) return;
    }
    Bars3DController::removeSeries(series);
  }

  //  void Bars3DController::insertSeries(int index, QAbstract3DSeries
  //      *series)
  void insertSeries(int index, QAbstract3DSeries *series) override {
    if (taken[13]) {
      int handled = 0;
      CuteBars3DControllerCall13 call = reinterpret_cast<CuteBars3DControllerCall13>(taken[13]);
      call(this, index, series, &handled);
      if (handled) return;
    }
    Bars3DController::insertSeries(index, series);
  }

  //  void Bars3DController::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[14]) {
      int handled = 0;
      CuteBars3DControllerCall14 call = reinterpret_cast<CuteBars3DControllerCall14>(taken[14]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Bars3DController::handleAxisRangeChangedBySender(sender);
  }

  //  void Bars3DController::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[15]) {
      int handled = 0;
      CuteBars3DControllerCall15 call = reinterpret_cast<CuteBars3DControllerCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DController::adjustAxisRanges();
  }

  //  QAbstract3DAxis
  //      *Bars3DController::createDefaultAxis(QAbstract3DAxis::AxisOrienta
  //      tion orientation)
  QAbstract3DAxis *createDefaultAxis(
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[16]) {
      int handled = 0;
      CuteBars3DControllerCall16 call = reinterpret_cast<CuteBars3DControllerCall16>(taken[16]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Bars3DController::createDefaultAxis(orientation);
  }

  //  void Abstract3DController::render(const GLuint defaultFboHandle)
  void render(const GLuint defaultFboHandle) override {
    if (taken[17]) {
      int handled = 0;
      CuteBars3DControllerCall17 call = reinterpret_cast<CuteBars3DControllerCall17>(taken[17]);
      call(this, defaultFboHandle, &handled);
      if (handled) return;
    }
    Abstract3DController::render(defaultFboHandle);
  }

  //  bool Abstract3DController::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[18]) {
      int handled = 0;
      CuteBars3DControllerCall18 call = reinterpret_cast<CuteBars3DControllerCall18>(taken[18]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return Abstract3DController::hasSeries(series);
  }

  //  QAbstract3DAxis *Abstract3DController::axisX() const
  QAbstract3DAxis *axisX() const override {
    if (taken[19]) {
      int handled = 0;
      CuteBars3DControllerCall19 call = reinterpret_cast<CuteBars3DControllerCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisX();
  }

  //  void Abstract3DController::setAxisY(QAbstract3DAxis *axis)
  void setAxisY(QAbstract3DAxis *axis) override {
    if (taken[20]) {
      int handled = 0;
      CuteBars3DControllerCall20 call = reinterpret_cast<CuteBars3DControllerCall20>(taken[20]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::setAxisY(axis);
  }

  //  QAbstract3DAxis *Abstract3DController::axisY() const
  QAbstract3DAxis *axisY() const override {
    if (taken[21]) {
      int handled = 0;
      CuteBars3DControllerCall21 call = reinterpret_cast<CuteBars3DControllerCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisY();
  }

  //  QAbstract3DAxis *Abstract3DController::axisZ() const
  QAbstract3DAxis *axisZ() const override {
    if (taken[22]) {
      int handled = 0;
      CuteBars3DControllerCall22 call = reinterpret_cast<CuteBars3DControllerCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisZ();
  }

  //  void Abstract3DController::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[23]) {
      int handled = 0;
      CuteBars3DControllerCall23 call = reinterpret_cast<CuteBars3DControllerCall23>(taken[23]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::addAxis(axis);
  }

  //  void Abstract3DController::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[24]) {
      int handled = 0;
      CuteBars3DControllerCall24 call = reinterpret_cast<CuteBars3DControllerCall24>(taken[24]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::releaseAxis(axis);
  }

  //  void Abstract3DController::addInputHandler(QAbstract3DInputHandler
  //      *inputHandler)
  void addInputHandler(QAbstract3DInputHandler *inputHandler) override {
    if (taken[25]) {
      int handled = 0;
      CuteBars3DControllerCall25 call = reinterpret_cast<CuteBars3DControllerCall25>(taken[25]);
      call(this, inputHandler, &handled);
      if (handled) return;
    }
    Abstract3DController::addInputHandler(inputHandler);
  }

  //  void
  //      Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
  //      *inputHandler)
  void releaseInputHandler(QAbstract3DInputHandler *inputHandler) override {
    if (taken[26]) {
      int handled = 0;
      CuteBars3DControllerCall26 call = reinterpret_cast<CuteBars3DControllerCall26>(taken[26]);
      call(this, inputHandler, &handled);
      if (handled) return;
    }
    Abstract3DController::releaseInputHandler(inputHandler);
  }

  //  void
  //      Abstract3DController::setActiveInputHandler(QAbstract3DInputHandl
  //      er *inputHandler)
  void setActiveInputHandler(
      QAbstract3DInputHandler *inputHandler) override {
    if (taken[27]) {
      int handled = 0;
      CuteBars3DControllerCall27 call = reinterpret_cast<CuteBars3DControllerCall27>(taken[27]);
      call(this, inputHandler, &handled);
      if (handled) return;
    }
    Abstract3DController::setActiveInputHandler(inputHandler);
  }

  //  QAbstract3DInputHandler *Abstract3DController::activeInputHandler()
  QAbstract3DInputHandler *activeInputHandler() override {
    if (taken[28]) {
      int handled = 0;
      CuteBars3DControllerCall28 call = reinterpret_cast<CuteBars3DControllerCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DInputHandler *>(given);
    }
    return Abstract3DController::activeInputHandler();
  }

  //  void Abstract3DController::addTheme(Q3DTheme *theme)
  void addTheme(Q3DTheme *theme) override {
    if (taken[29]) {
      int handled = 0;
      CuteBars3DControllerCall29 call = reinterpret_cast<CuteBars3DControllerCall29>(taken[29]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DController::addTheme(theme);
  }

  //  void Abstract3DController::releaseTheme(Q3DTheme *theme)
  void releaseTheme(Q3DTheme *theme) override {
    if (taken[30]) {
      int handled = 0;
      CuteBars3DControllerCall30 call = reinterpret_cast<CuteBars3DControllerCall30>(taken[30]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DController::releaseTheme(theme);
  }

  //  void Abstract3DController::setActiveTheme(Q3DTheme *theme, bool
  //      force)
  void setActiveTheme(Q3DTheme *theme, bool force) override {
    if (taken[31]) {
      int handled = 0;
      CuteBars3DControllerCall31 call = reinterpret_cast<CuteBars3DControllerCall31>(taken[31]);
      call(this, theme, force, &handled);
      if (handled) return;
    }
    Abstract3DController::setActiveTheme(theme, force);
  }

  //  Q3DTheme *Abstract3DController::activeTheme() const
  Q3DTheme *activeTheme() const override {
    if (taken[32]) {
      int handled = 0;
      CuteBars3DControllerCall32 call = reinterpret_cast<CuteBars3DControllerCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Q3DTheme *>(given);
    }
    return Abstract3DController::activeTheme();
  }

  //  QAbstract3DGraph::SelectionFlags
  //      Abstract3DController::selectionMode() const
  QAbstract3DGraph::SelectionFlags selectionMode() const override {
    if (taken[33]) {
      int handled = 0;
      CuteBars3DControllerCall33 call = reinterpret_cast<CuteBars3DControllerCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(given);
    }
    return Abstract3DController::selectionMode();
  }

  //  void Abstract3DController::setShadowQuality(QAbstract3DGraph::ShadowQ
  //      uality quality)
  void setShadowQuality(QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[34]) {
      int handled = 0;
      CuteBars3DControllerCall34 call = reinterpret_cast<CuteBars3DControllerCall34>(taken[34]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Abstract3DController::setShadowQuality(quality);
  }

  //  void Abstract3DController::doSetShadowQuality(QAbstract3DGraph::Shado
  //      wQuality quality)
  void doSetShadowQuality(QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[35]) {
      int handled = 0;
      CuteBars3DControllerCall35 call = reinterpret_cast<CuteBars3DControllerCall35>(taken[35]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Abstract3DController::doSetShadowQuality(quality);
  }

  //  QAbstract3DGraph::ShadowQuality Abstract3DController::shadowQuality()
  //      const
  QAbstract3DGraph::ShadowQuality shadowQuality() const override {
    if (taken[36]) {
      int handled = 0;
      CuteBars3DControllerCall36 call = reinterpret_cast<CuteBars3DControllerCall36>(taken[36]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DGraph::ShadowQuality>(given);
    }
    return Abstract3DController::shadowQuality();
  }

  //  bool Abstract3DController::shadowsSupported() const
  bool shadowsSupported() const override {
    if (taken[37]) {
      int handled = 0;
      CuteBars3DControllerCall37 call = reinterpret_cast<CuteBars3DControllerCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Abstract3DController::shadowsSupported();
  }

  //  void Abstract3DController::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteBars3DControllerCall38 call = reinterpret_cast<CuteBars3DControllerCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseDoubleClickEvent(event);
  }

  //  void Abstract3DController::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteBars3DControllerCall39 call = reinterpret_cast<CuteBars3DControllerCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::touchEvent(event);
  }

  //  void Abstract3DController::mousePressEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mousePressEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[40]) {
      int handled = 0;
      CuteBars3DControllerCall40 call = reinterpret_cast<CuteBars3DControllerCall40>(taken[40]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Abstract3DController::mousePressEvent(event, mousePos);
  }

  //  void Abstract3DController::mouseReleaseEvent(QMouseEvent *event,
  //      const QPoint &mousePos)
  void mouseReleaseEvent(
      QMouseEvent *event,
      const QPoint &mousePos) override {
    if (taken[41]) {
      int handled = 0;
      CuteBars3DControllerCall41 call = reinterpret_cast<CuteBars3DControllerCall41>(taken[41]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseReleaseEvent(event, mousePos);
  }

  //  void Abstract3DController::mouseMoveEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mouseMoveEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[42]) {
      int handled = 0;
      CuteBars3DControllerCall42 call = reinterpret_cast<CuteBars3DControllerCall42>(taken[42]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseMoveEvent(event, mousePos);
  }

#if QT_CONFIG(wheelevent)
  //  void Abstract3DController::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteBars3DControllerCall43 call = reinterpret_cast<CuteBars3DControllerCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void Abstract3DController::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[44]) {
      int handled = 0;
      CuteBars3DControllerCall44 call = reinterpret_cast<CuteBars3DControllerCall44>(taken[44]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[45]) {
      int handled = 0;
      CuteBars3DControllerCall45 call = reinterpret_cast<CuteBars3DControllerCall45>(taken[45]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelsChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleAxisSegmentCountChangedBySender(QObje
  //      ct *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[46]) {
      int handled = 0;
      CuteBars3DControllerCall46 call = reinterpret_cast<CuteBars3DControllerCall46>(taken[46]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisSubSegmentCountChangedBySender(Q
  //      Object *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[47]) {
      int handled = 0;
      CuteBars3DControllerCall47 call = reinterpret_cast<CuteBars3DControllerCall47>(taken[47]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleAxisLabelFormatChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[48]) {
      int handled = 0;
      CuteBars3DControllerCall48 call = reinterpret_cast<CuteBars3DControllerCall48>(taken[48]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[49]) {
      int handled = 0;
      CuteBars3DControllerCall49 call = reinterpret_cast<CuteBars3DControllerCall49>(taken[49]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisReversedChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[50]) {
      int handled = 0;
      CuteBars3DControllerCall50 call = reinterpret_cast<CuteBars3DControllerCall50>(taken[50]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisFormatterDirtyBySender(sender);
  }

  //  void Abstract3DController::handleAxisLabelAutoRotationChangedBySender
  //      (QObject *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[51]) {
      int handled = 0;
      CuteBars3DControllerCall51 call = reinterpret_cast<CuteBars3DControllerCall51>(taken[51]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelAutoRotationChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisTitleVisibilityChangedBySender(Q
  //      Object *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[52]) {
      int handled = 0;
      CuteBars3DControllerCall52 call = reinterpret_cast<CuteBars3DControllerCall52>(taken[52]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[53]) {
      int handled = 0;
      CuteBars3DControllerCall53 call = reinterpret_cast<CuteBars3DControllerCall53>(taken[53]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void Abstract3DController::handlePendingGraphPositionQuery()
  void handlePendingGraphPositionQuery() override {
    if (taken[54]) {
      int handled = 0;
      CuteBars3DControllerCall54 call = reinterpret_cast<CuteBars3DControllerCall54>(taken[54]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::handlePendingGraphPositionQuery();
  }

  //  void Abstract3DController::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[55]) {
      int handled = 0;
      CuteBars3DControllerCall55 call = reinterpret_cast<CuteBars3DControllerCall55>(taken[55]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::startRecordingRemovesAndInserts();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteBars3DControllerCall56 call = reinterpret_cast<CuteBars3DControllerCall56>(taken[56]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteBars3DControllerCall57 call = reinterpret_cast<CuteBars3DControllerCall57>(taken[57]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteBars3DControllerCall58 call = reinterpret_cast<CuteBars3DControllerCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteBars3DControllerCall59 call = reinterpret_cast<CuteBars3DControllerCall59>(taken[59]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[60]) {
      int handled = 0;
      CuteBars3DControllerCall60 call = reinterpret_cast<CuteBars3DControllerCall60>(taken[60]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[61]) {
      int handled = 0;
      CuteBars3DControllerCall61 call = reinterpret_cast<CuteBars3DControllerCall61>(taken[61]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[62]) {
      int handled = 0;
      CuteBars3DControllerCall62 call = reinterpret_cast<CuteBars3DControllerCall62>(taken[62]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Bars3DController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16Bars3DController10metaObjectEv(
    const Bars3DController *self) {
  return self->metaObject();
}

//  QString Bars3DController::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16Bars3DController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Bars3DController::tr(s, c, n));
}

//  Bars3DController::Bars3DController(QRect rect, Q3DScene *scene)
extern "C" Q_DECL_EXPORT
Bars3DController *ritual_ZN16Bars3DControllerC1E5QRectP8Q3DScene(
    const QRect *rect,
    Q3DScene *scene) {
  return new CuteBars3DController(*rect, scene);
}

//  Bars3DController::~Bars3DController()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DControllerD1Ev(Bars3DController *self) {
  delete self;
}

//  void Bars3DController::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController16initializeOpenGLEv(
    Bars3DController *self) {
  self->initializeOpenGL();
}

//  void Bars3DController::synchDataToRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController19synchDataToRendererEv(
    Bars3DController *self) {
  self->synchDataToRenderer();
}

//  void Bars3DController::setMultiSeriesScaling(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController21setMultiSeriesScalingEb(
    Bars3DController *self,
    bool uniform) {
  self->setMultiSeriesScaling(uniform);
}

//  bool Bars3DController::multiSeriesScaling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16Bars3DController18multiSeriesScalingEv(
    const Bars3DController *self) {
  return self->multiSeriesScaling();
}

//  void Bars3DController::setBarSpecs(GLfloat thicknessRatio, const QSizeF
//      &spacing, bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController11setBarSpecsEfRK6QSizeFb(
    Bars3DController *self,
    GLfloat thicknessRatio,
    const QSizeF *spacing,
    bool relative) {
  self->setBarSpecs(thicknessRatio, *spacing, relative);
}

//  void Bars3DController::setBarSeriesMargin(const QSizeF &margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController18setBarSeriesMarginERK6QSizeF(
    Bars3DController *self,
    const QSizeF *margin) {
  self->setBarSeriesMargin(*margin);
}

//  QSizeF Bars3DController::barSeriesMargin()
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN16Bars3DController15barSeriesMarginEv(
    Bars3DController *self) {
  return new QSizeF(self->barSeriesMargin());
}

//  QSizeF Bars3DController::barSpacing()
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN16Bars3DController10barSpacingEv(Bars3DController *self) {
  return new QSizeF(self->barSpacing());
}

//  bool Bars3DController::isBarSpecRelative()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16Bars3DController17isBarSpecRelativeEv(
    Bars3DController *self) {
  return self->isBarSpecRelative();
}

//  void Bars3DController::setFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController13setFloorLevelEf(
    Bars3DController *self,
    float level) {
  self->setFloorLevel(level);
}

//  float Bars3DController::floorLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16Bars3DController10floorLevelEv(
    const Bars3DController *self) {
  return self->floorLevel();
}

//  QBar3DSeries *Bars3DController::selectedSeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK16Bars3DController14selectedSeriesEv(
    const Bars3DController *self) {
  return self->selectedSeries();
}

//  void Bars3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Bars3DController *self,
    int mode) {
  self->setSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  void Bars3DController::setSelectedBar(const QPoint &position,
//      QBar3DSeries *series, bool enterSlice)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController14setSelectedBarERK6QPointP12QBar3DSeriesb(
    Bars3DController *self,
    const QPoint *position,
    QBar3DSeries *series,
    bool enterSlice) {
  self->setSelectedBar(*position, series, enterSlice);
}

//  void Bars3DController::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController14clearSelectionEv(Bars3DController *self) {
  self->clearSelection();
}

//  void Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(QAbs
//      tract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    Bars3DController *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void Bars3DController::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController37handleSeriesVisibilityChangedBySenderEP7QObject(
    Bars3DController *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  void Bars3DController::handlePendingClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController18handlePendingClickEv(
    Bars3DController *self) {
  self->handlePendingClick();
}

//  QPoint Bars3DController::invalidSelectionPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN16Bars3DController24invalidSelectionPositionEv() {
  return new QPoint(Bars3DController::invalidSelectionPosition());
}

//  void Bars3DController::setAxisX(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController8setAxisXEP15QAbstract3DAxis(
    Bars3DController *self,
    QAbstract3DAxis *axis) {
  self->setAxisX(axis);
}

//  void Bars3DController::setAxisZ(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController8setAxisZEP15QAbstract3DAxis(
    Bars3DController *self,
    QAbstract3DAxis *axis) {
  self->setAxisZ(axis);
}

//  void Bars3DController::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSeries(
    Bars3DController *self,
    QBar3DSeries *series) {
  self->setPrimarySeries(series);
}

//  QBar3DSeries *Bars3DController::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK16Bars3DController13primarySeriesEv(
    const Bars3DController *self) {
  return self->primarySeries();
}

//  void Bars3DController::addSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController9addSeriesEP17QAbstract3DSeries(
    Bars3DController *self,
    QAbstract3DSeries *series) {
  self->addSeries(series);
}

//  void Bars3DController::removeSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController12removeSeriesEP17QAbstract3DSeries(
    Bars3DController *self,
    QAbstract3DSeries *series) {
  self->removeSeries(series);
}

//  void Bars3DController::insertSeries(int index, QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController12insertSeriesEiP17QAbstract3DSeries(
    Bars3DController *self,
    int index,
    QAbstract3DSeries *series) {
  self->insertSeries(index, series);
}

//  QList<QBar3DSeries *> Bars3DController::barSeriesList()
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_ZN16Bars3DController13barSeriesListEv(
    Bars3DController *self) {
  return new QList<QBar3DSeries *>(self->barSeriesList());
}

//  void Bars3DController::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController30handleAxisRangeChangedBySenderEP7QObject(
    Bars3DController *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void Bars3DController::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController16adjustAxisRangesEv(
    Bars3DController *self) {
  self->adjustAxisRanges();
}

//  void Bars3DController::handleArrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController16handleArrayResetEv(
    Bars3DController *self) {
  self->handleArrayReset();
}

//  void Bars3DController::handleRowsAdded(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController15handleRowsAddedEii(
    Bars3DController *self,
    int startIndex,
    int count) {
  self->handleRowsAdded(startIndex, count);
}

//  void Bars3DController::handleRowsChanged(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController17handleRowsChangedEii(
    Bars3DController *self,
    int startIndex,
    int count) {
  self->handleRowsChanged(startIndex, count);
}

//  void Bars3DController::handleRowsRemoved(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController17handleRowsRemovedEii(
    Bars3DController *self,
    int startIndex,
    int count) {
  self->handleRowsRemoved(startIndex, count);
}

//  void Bars3DController::handleRowsInserted(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController18handleRowsInsertedEii(
    Bars3DController *self,
    int startIndex,
    int count) {
  self->handleRowsInserted(startIndex, count);
}

//  void Bars3DController::handleItemChanged(int rowIndex, int columnIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController17handleItemChangedEii(
    Bars3DController *self,
    int rowIndex,
    int columnIndex) {
  self->handleItemChanged(rowIndex, columnIndex);
}

//  void Bars3DController::handleDataRowLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController26handleDataRowLabelsChangedEv(
    Bars3DController *self) {
  self->handleDataRowLabelsChanged();
}

//  void Bars3DController::handleDataColumnLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController29handleDataColumnLabelsChangedEv(
    Bars3DController *self) {
  self->handleDataColumnLabelsChanged();
}

//  void Bars3DController::handleRowColorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16Bars3DController22handleRowColorsChangedEv(
    Bars3DController *self) {
  self->handleRowColorsChanged();
}

//  QAbstract3DAxis
//      *Bars3DController::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN16Bars3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    Bars3DController *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  a Python function taken by a CuteBars3DController, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Bars3DController(
    Bars3DController *self,
    const char *key,
    void *call) {
  return static_cast<CuteBars3DController *>(self)->take(key, call);
}

//  void Bars3DController::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController16initializeOpenGLEv(
    Bars3DController *self) {
  self->Bars3DController::initializeOpenGL();
}

//  void Bars3DController::synchDataToRenderer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController19synchDataToRendererEv(
    Bars3DController *self) {
  self->Bars3DController::synchDataToRenderer();
}

//  void Bars3DController::setSelectionMode(QAbstract3DGraph::SelectionFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Bars3DController *self,
    int mode) {
  self->Bars3DController::setSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  void Bars3DController::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController14clearSelectionEv(
    Bars3DController *self) {
  self->Bars3DController::clearSelection();
}

//  void Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(QAbs
//      tract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    Bars3DController *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->Bars3DController::handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void Bars3DController::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController37handleSeriesVisibilityChangedBySenderEP7QObject(
    Bars3DController *self,
    QObject *sender) {
  self->Bars3DController::handleSeriesVisibilityChangedBySender(sender);
}

//  void Bars3DController::handlePendingClick()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController18handlePendingClickEv(
    Bars3DController *self) {
  self->Bars3DController::handlePendingClick();
}

//  void Bars3DController::setAxisX(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController8setAxisXEP15QAbstract3DAxis(
    Bars3DController *self,
    QAbstract3DAxis *axis) {
  self->Bars3DController::setAxisX(axis);
}

//  void Bars3DController::setAxisZ(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController8setAxisZEP15QAbstract3DAxis(
    Bars3DController *self,
    QAbstract3DAxis *axis) {
  self->Bars3DController::setAxisZ(axis);
}

//  void Bars3DController::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController16setPrimarySeriesEP12QBar3DSeries(
    Bars3DController *self,
    QBar3DSeries *series) {
  self->Bars3DController::setPrimarySeries(series);
}

//  QBar3DSeries *Bars3DController::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_own_ZNK16Bars3DController13primarySeriesEv(
    const Bars3DController *self) {
  return self->Bars3DController::primarySeries();
}

//  void Bars3DController::addSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController9addSeriesEP17QAbstract3DSeries(
    Bars3DController *self,
    QAbstract3DSeries *series) {
  self->Bars3DController::addSeries(series);
}

//  void Bars3DController::removeSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController12removeSeriesEP17QAbstract3DSeries(
    Bars3DController *self,
    QAbstract3DSeries *series) {
  self->Bars3DController::removeSeries(series);
}

//  void Bars3DController::insertSeries(int index, QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController12insertSeriesEiP17QAbstract3DSeries(
    Bars3DController *self,
    int index,
    QAbstract3DSeries *series) {
  self->Bars3DController::insertSeries(index, series);
}

//  void Bars3DController::handleAxisRangeChangedBySender(QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController30handleAxisRangeChangedBySenderEP7QObject(
    Bars3DController *self,
    QObject *sender) {
  self->Bars3DController::handleAxisRangeChangedBySender(sender);
}

//  void Bars3DController::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16Bars3DController16adjustAxisRangesEv(
    Bars3DController *self) {
  self->Bars3DController::adjustAxisRanges();
}

//  QAbstract3DAxis
//      *Bars3DController::createDefaultAxis(QAbstract3DAxis::AxisOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN16Bars3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    Bars3DController *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnBars3DController *>(self)->OwnBars3DController::createDefaultAxis(
      orientation);
}
