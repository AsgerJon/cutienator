//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstract3dcontroller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstract3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDataVisualization/qabstract3dseries.h>
#include <QtDataVisualization/qabstract3daxis.h>
#include <QtDataVisualization/qabstract3dinputhandler.h>
#include <QtDataVisualization/q3dtheme.h>
#include <QtGui/qvectornd.h>
#include <QtDataVisualization/qcustom3ditem.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on Abstract3DController may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAbstract3DController : Abstract3DController {
  using Abstract3DController::createDefaultAxis;
  using Abstract3DController::startRecordingRemovesAndInserts;
};

//  A Abstract3DController that Python can take functions over in. Every Abstract3DController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAbstract3DControllerCall0)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall1)(const void *, GLuint, int *);
typedef void (*CuteAbstract3DControllerCall2)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall3)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteAbstract3DControllerCall4)(const void *, int, QAbstract3DSeries *, int *);
typedef void (*CuteAbstract3DControllerCall5)(const void *, QAbstract3DSeries *, int *);
typedef bool (*CuteAbstract3DControllerCall6)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteAbstract3DControllerCall7)(const void *, QAbstract3DAxis *, int *);
typedef void * (*CuteAbstract3DControllerCall8)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall9)(const void *, QAbstract3DAxis *, int *);
typedef void * (*CuteAbstract3DControllerCall10)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall11)(const void *, QAbstract3DAxis *, int *);
typedef void * (*CuteAbstract3DControllerCall12)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall13)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteAbstract3DControllerCall14)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteAbstract3DControllerCall15)(const void *, QAbstract3DInputHandler *, int *);
typedef void (*CuteAbstract3DControllerCall16)(const void *, QAbstract3DInputHandler *, int *);
typedef void (*CuteAbstract3DControllerCall17)(const void *, QAbstract3DInputHandler *, int *);
typedef void * (*CuteAbstract3DControllerCall18)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall19)(const void *, Q3DTheme *, int *);
typedef void (*CuteAbstract3DControllerCall20)(const void *, Q3DTheme *, int *);
typedef void (*CuteAbstract3DControllerCall21)(const void *, Q3DTheme *, bool, int *);
typedef void * (*CuteAbstract3DControllerCall22)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall23)(const void *, int, int *);
typedef int (*CuteAbstract3DControllerCall24)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall25)(const void *, int, int *);
typedef void (*CuteAbstract3DControllerCall26)(const void *, int, int *);
typedef int (*CuteAbstract3DControllerCall27)(const void *, int *);
typedef bool (*CuteAbstract3DControllerCall28)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall29)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall30)(const void *, QMouseEvent *, int *);
typedef void (*CuteAbstract3DControllerCall31)(const void *, QTouchEvent *, int *);
typedef void (*CuteAbstract3DControllerCall32)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteAbstract3DControllerCall33)(const void *, QMouseEvent *, const QPoint *, int *);
typedef void (*CuteAbstract3DControllerCall34)(const void *, QMouseEvent *, const QPoint *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAbstract3DControllerCall35)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAbstract3DControllerCall36)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall37)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall38)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall39)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall40)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall41)(const void *, int, bool, int *);
typedef void (*CuteAbstract3DControllerCall42)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall43)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall44)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall45)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall46)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall47)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall48)(const void *, QObject *, int *);
typedef void (*CuteAbstract3DControllerCall49)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall50)(const void *, int *);
typedef void (*CuteAbstract3DControllerCall51)(const void *, int *);
typedef void * (*CuteAbstract3DControllerCall52)(const void *, int, int *);
typedef void (*CuteAbstract3DControllerCall53)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstract3DControllerCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstract3DControllerCall55)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstract3DControllerCall56)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstract3DControllerCall57)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstract3DControllerCall58)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstract3DControllerCall59)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstract3DControllerCall60)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAbstract3DController : public Abstract3DController {
public:
  using Abstract3DController::Abstract3DController;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20Abstract3DController19synchDataToRendererEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController6renderEj")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16initializeOpenGLEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSeries")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisXEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisYEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController5axisZEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInputHandler")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3DInputHandler")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstract3DInputHandler")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18activeInputHandlerEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController8addThemeEP8Q3DTheme")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController12releaseThemeEP8Q3DTheme")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController11activeThemeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController13selectionModeEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController13shadowQualityEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20Abstract3DController16shadowsSupportedEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14clearSelectionEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController10touchEventEP11QTouchEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6QPoint")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventRK6QPoint")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6QPoint")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN20Abstract3DController10wheelEventEP11QWheelEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7QObject")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP7QObject")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7QObject")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController37handleAxisSegmentCountChangedBySenderEP7QObject")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController40handleAxisSubSegmentCountChangedBySenderEP7QObject")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController36handleAxisLabelFormatChangedBySenderEP7QObject")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController33handleAxisReversedChangedBySenderEP7QObject")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderEP7QObject")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController42handleAxisLabelAutoRotationChangedBySenderEP7QObject")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController40handleAxisTitleVisibilityChangedBySenderEP7QObject")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController35handleAxisTitleFixedChangedBySenderEP7QObject")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController37handleSeriesVisibilityChangedBySenderEP7QObject")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController18handlePendingClickEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31handlePendingGraphPositionQueryEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController16adjustAxisRangesEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv")) {
      taken[53] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[59] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[60] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Abstract3DController::synchDataToRenderer()
  void synchDataToRenderer() override {
    if (taken[0]) {
      int handled = 0;
      CuteAbstract3DControllerCall0 call = reinterpret_cast<CuteAbstract3DControllerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::synchDataToRenderer();
  }

  //  void Abstract3DController::render(const GLuint defaultFboHandle)
  void render(const GLuint defaultFboHandle) override {
    if (taken[1]) {
      int handled = 0;
      CuteAbstract3DControllerCall1 call = reinterpret_cast<CuteAbstract3DControllerCall1>(taken[1]);
      call(this, defaultFboHandle, &handled);
      if (handled) return;
    }
    Abstract3DController::render(defaultFboHandle);
  }

  //  void Abstract3DController::initializeOpenGL()
  void initializeOpenGL() override {
    if (taken[2]) {
      int handled = 0;
      CuteAbstract3DControllerCall2 call = reinterpret_cast<CuteAbstract3DControllerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Abstract3DController::addSeries(QAbstract3DSeries *series)
  void addSeries(QAbstract3DSeries *series) override {
    if (taken[3]) {
      int handled = 0;
      CuteAbstract3DControllerCall3 call = reinterpret_cast<CuteAbstract3DControllerCall3>(taken[3]);
      call(this, series, &handled);
      if (handled) return;
    }
    Abstract3DController::addSeries(series);
  }

  //  void Abstract3DController::insertSeries(int index, QAbstract3DSeries
  //      *series)
  void insertSeries(int index, QAbstract3DSeries *series) override {
    if (taken[4]) {
      int handled = 0;
      CuteAbstract3DControllerCall4 call = reinterpret_cast<CuteAbstract3DControllerCall4>(taken[4]);
      call(this, index, series, &handled);
      if (handled) return;
    }
    Abstract3DController::insertSeries(index, series);
  }

  //  void Abstract3DController::removeSeries(QAbstract3DSeries *series)
  void removeSeries(QAbstract3DSeries *series) override {
    if (taken[5]) {
      int handled = 0;
      CuteAbstract3DControllerCall5 call = reinterpret_cast<CuteAbstract3DControllerCall5>(taken[5]);
      call(this, series, &handled);
      if (handled) return;
    }
    Abstract3DController::removeSeries(series);
  }

  //  bool Abstract3DController::hasSeries(QAbstract3DSeries *series)
  bool hasSeries(QAbstract3DSeries *series) override {
    if (taken[6]) {
      int handled = 0;
      CuteAbstract3DControllerCall6 call = reinterpret_cast<CuteAbstract3DControllerCall6>(taken[6]);
      bool given = call(this, series, &handled);
      if (handled) return given;
    }
    return Abstract3DController::hasSeries(series);
  }

  //  void Abstract3DController::setAxisX(QAbstract3DAxis *axis)
  void setAxisX(QAbstract3DAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteAbstract3DControllerCall7 call = reinterpret_cast<CuteAbstract3DControllerCall7>(taken[7]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::setAxisX(axis);
  }

  //  QAbstract3DAxis *Abstract3DController::axisX() const
  QAbstract3DAxis *axisX() const override {
    if (taken[8]) {
      int handled = 0;
      CuteAbstract3DControllerCall8 call = reinterpret_cast<CuteAbstract3DControllerCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisX();
  }

  //  void Abstract3DController::setAxisY(QAbstract3DAxis *axis)
  void setAxisY(QAbstract3DAxis *axis) override {
    if (taken[9]) {
      int handled = 0;
      CuteAbstract3DControllerCall9 call = reinterpret_cast<CuteAbstract3DControllerCall9>(taken[9]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::setAxisY(axis);
  }

  //  QAbstract3DAxis *Abstract3DController::axisY() const
  QAbstract3DAxis *axisY() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAbstract3DControllerCall10 call = reinterpret_cast<CuteAbstract3DControllerCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisY();
  }

  //  void Abstract3DController::setAxisZ(QAbstract3DAxis *axis)
  void setAxisZ(QAbstract3DAxis *axis) override {
    if (taken[11]) {
      int handled = 0;
      CuteAbstract3DControllerCall11 call = reinterpret_cast<CuteAbstract3DControllerCall11>(taken[11]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::setAxisZ(axis);
  }

  //  QAbstract3DAxis *Abstract3DController::axisZ() const
  QAbstract3DAxis *axisZ() const override {
    if (taken[12]) {
      int handled = 0;
      CuteAbstract3DControllerCall12 call = reinterpret_cast<CuteAbstract3DControllerCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::axisZ();
  }

  //  void Abstract3DController::addAxis(QAbstract3DAxis *axis)
  void addAxis(QAbstract3DAxis *axis) override {
    if (taken[13]) {
      int handled = 0;
      CuteAbstract3DControllerCall13 call = reinterpret_cast<CuteAbstract3DControllerCall13>(taken[13]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::addAxis(axis);
  }

  //  void Abstract3DController::releaseAxis(QAbstract3DAxis *axis)
  void releaseAxis(QAbstract3DAxis *axis) override {
    if (taken[14]) {
      int handled = 0;
      CuteAbstract3DControllerCall14 call = reinterpret_cast<CuteAbstract3DControllerCall14>(taken[14]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Abstract3DController::releaseAxis(axis);
  }

  //  void Abstract3DController::addInputHandler(QAbstract3DInputHandler
  //      *inputHandler)
  void addInputHandler(QAbstract3DInputHandler *inputHandler) override {
    if (taken[15]) {
      int handled = 0;
      CuteAbstract3DControllerCall15 call = reinterpret_cast<CuteAbstract3DControllerCall15>(taken[15]);
      call(this, inputHandler, &handled);
      if (handled) return;
    }
    Abstract3DController::addInputHandler(inputHandler);
  }

  //  void
  //      Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
  //      *inputHandler)
  void releaseInputHandler(QAbstract3DInputHandler *inputHandler) override {
    if (taken[16]) {
      int handled = 0;
      CuteAbstract3DControllerCall16 call = reinterpret_cast<CuteAbstract3DControllerCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteAbstract3DControllerCall17 call = reinterpret_cast<CuteAbstract3DControllerCall17>(taken[17]);
      call(this, inputHandler, &handled);
      if (handled) return;
    }
    Abstract3DController::setActiveInputHandler(inputHandler);
  }

  //  QAbstract3DInputHandler *Abstract3DController::activeInputHandler()
  QAbstract3DInputHandler *activeInputHandler() override {
    if (taken[18]) {
      int handled = 0;
      CuteAbstract3DControllerCall18 call = reinterpret_cast<CuteAbstract3DControllerCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DInputHandler *>(given);
    }
    return Abstract3DController::activeInputHandler();
  }

  //  void Abstract3DController::addTheme(Q3DTheme *theme)
  void addTheme(Q3DTheme *theme) override {
    if (taken[19]) {
      int handled = 0;
      CuteAbstract3DControllerCall19 call = reinterpret_cast<CuteAbstract3DControllerCall19>(taken[19]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DController::addTheme(theme);
  }

  //  void Abstract3DController::releaseTheme(Q3DTheme *theme)
  void releaseTheme(Q3DTheme *theme) override {
    if (taken[20]) {
      int handled = 0;
      CuteAbstract3DControllerCall20 call = reinterpret_cast<CuteAbstract3DControllerCall20>(taken[20]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DController::releaseTheme(theme);
  }

  //  void Abstract3DController::setActiveTheme(Q3DTheme *theme, bool
  //      force)
  void setActiveTheme(Q3DTheme *theme, bool force) override {
    if (taken[21]) {
      int handled = 0;
      CuteAbstract3DControllerCall21 call = reinterpret_cast<CuteAbstract3DControllerCall21>(taken[21]);
      call(this, theme, force, &handled);
      if (handled) return;
    }
    Abstract3DController::setActiveTheme(theme, force);
  }

  //  Q3DTheme *Abstract3DController::activeTheme() const
  Q3DTheme *activeTheme() const override {
    if (taken[22]) {
      int handled = 0;
      CuteAbstract3DControllerCall22 call = reinterpret_cast<CuteAbstract3DControllerCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Q3DTheme *>(given);
    }
    return Abstract3DController::activeTheme();
  }

  //  void Abstract3DController::setSelectionMode(QAbstract3DGraph::Selecti
  //      onFlags mode)
  void setSelectionMode(QAbstract3DGraph::SelectionFlags mode) override {
    if (taken[23]) {
      int handled = 0;
      CuteAbstract3DControllerCall23 call = reinterpret_cast<CuteAbstract3DControllerCall23>(taken[23]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    Abstract3DController::setSelectionMode(mode);
  }

  //  QAbstract3DGraph::SelectionFlags
  //      Abstract3DController::selectionMode() const
  QAbstract3DGraph::SelectionFlags selectionMode() const override {
    if (taken[24]) {
      int handled = 0;
      CuteAbstract3DControllerCall24 call = reinterpret_cast<CuteAbstract3DControllerCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(given);
    }
    return Abstract3DController::selectionMode();
  }

  //  void Abstract3DController::setShadowQuality(QAbstract3DGraph::ShadowQ
  //      uality quality)
  void setShadowQuality(QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[25]) {
      int handled = 0;
      CuteAbstract3DControllerCall25 call = reinterpret_cast<CuteAbstract3DControllerCall25>(taken[25]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Abstract3DController::setShadowQuality(quality);
  }

  //  void Abstract3DController::doSetShadowQuality(QAbstract3DGraph::Shado
  //      wQuality quality)
  void doSetShadowQuality(QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[26]) {
      int handled = 0;
      CuteAbstract3DControllerCall26 call = reinterpret_cast<CuteAbstract3DControllerCall26>(taken[26]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Abstract3DController::doSetShadowQuality(quality);
  }

  //  QAbstract3DGraph::ShadowQuality Abstract3DController::shadowQuality()
  //      const
  QAbstract3DGraph::ShadowQuality shadowQuality() const override {
    if (taken[27]) {
      int handled = 0;
      CuteAbstract3DControllerCall27 call = reinterpret_cast<CuteAbstract3DControllerCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstract3DGraph::ShadowQuality>(given);
    }
    return Abstract3DController::shadowQuality();
  }

  //  bool Abstract3DController::shadowsSupported() const
  bool shadowsSupported() const override {
    if (taken[28]) {
      int handled = 0;
      CuteAbstract3DControllerCall28 call = reinterpret_cast<CuteAbstract3DControllerCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Abstract3DController::shadowsSupported();
  }

  //  void Abstract3DController::clearSelection()
  void clearSelection() override {
    if (taken[29]) {
      int handled = 0;
      CuteAbstract3DControllerCall29 call = reinterpret_cast<CuteAbstract3DControllerCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Abstract3DController::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteAbstract3DControllerCall30 call = reinterpret_cast<CuteAbstract3DControllerCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseDoubleClickEvent(event);
  }

  //  void Abstract3DController::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteAbstract3DControllerCall31 call = reinterpret_cast<CuteAbstract3DControllerCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::touchEvent(event);
  }

  //  void Abstract3DController::mousePressEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mousePressEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[32]) {
      int handled = 0;
      CuteAbstract3DControllerCall32 call = reinterpret_cast<CuteAbstract3DControllerCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteAbstract3DControllerCall33 call = reinterpret_cast<CuteAbstract3DControllerCall33>(taken[33]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseReleaseEvent(event, mousePos);
  }

  //  void Abstract3DController::mouseMoveEvent(QMouseEvent *event, const
  //      QPoint &mousePos)
  void mouseMoveEvent(QMouseEvent *event, const QPoint &mousePos) override {
    if (taken[34]) {
      int handled = 0;
      CuteAbstract3DControllerCall34 call = reinterpret_cast<CuteAbstract3DControllerCall34>(taken[34]);
      call(this, event, &mousePos, &handled);
      if (handled) return;
    }
    Abstract3DController::mouseMoveEvent(event, mousePos);
  }

#if QT_CONFIG(wheelevent)
  //  void Abstract3DController::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteAbstract3DControllerCall35 call = reinterpret_cast<CuteAbstract3DControllerCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    Abstract3DController::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void Abstract3DController::handleAxisTitleChangedBySender(QObject
  //      *sender)
  void handleAxisTitleChangedBySender(QObject *sender) override {
    if (taken[36]) {
      int handled = 0;
      CuteAbstract3DControllerCall36 call = reinterpret_cast<CuteAbstract3DControllerCall36>(taken[36]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisLabelsChangedBySender(QObject
  //      *sender)
  void handleAxisLabelsChangedBySender(QObject *sender) override {
    if (taken[37]) {
      int handled = 0;
      CuteAbstract3DControllerCall37 call = reinterpret_cast<CuteAbstract3DControllerCall37>(taken[37]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelsChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisRangeChangedBySender(QObject
  //      *sender)
  void handleAxisRangeChangedBySender(QObject *sender) override {
    if (taken[38]) {
      int handled = 0;
      CuteAbstract3DControllerCall38 call = reinterpret_cast<CuteAbstract3DControllerCall38>(taken[38]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisRangeChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleAxisSegmentCountChangedBySender(QObje
  //      ct *sender)
  void handleAxisSegmentCountChangedBySender(QObject *sender) override {
    if (taken[39]) {
      int handled = 0;
      CuteAbstract3DControllerCall39 call = reinterpret_cast<CuteAbstract3DControllerCall39>(taken[39]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisSegmentCountChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisSubSegmentCountChangedBySender(Q
  //      Object *sender)
  void handleAxisSubSegmentCountChangedBySender(QObject *sender) override {
    if (taken[40]) {
      int handled = 0;
      CuteAbstract3DControllerCall40 call = reinterpret_cast<CuteAbstract3DControllerCall40>(taken[40]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisSubSegmentCountChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisAutoAdjustRangeChangedInOrientat
  //      ion(QAbstract3DAxis::AxisOrientation orientation, bool
  //      autoAdjust)
  void handleAxisAutoAdjustRangeChangedInOrientation(
      QAbstract3DAxis::AxisOrientation orientation,
      bool autoAdjust) override {
    if (taken[41]) {
      int handled = 0;
      CuteAbstract3DControllerCall41 call = reinterpret_cast<CuteAbstract3DControllerCall41>(taken[41]);
      call(this, static_cast<int>(orientation), autoAdjust, &handled);
      if (handled) return;
    }
  }

  //  void
  //      Abstract3DController::handleAxisLabelFormatChangedBySender(QObjec
  //      t *sender)
  void handleAxisLabelFormatChangedBySender(QObject *sender) override {
    if (taken[42]) {
      int handled = 0;
      CuteAbstract3DControllerCall42 call = reinterpret_cast<CuteAbstract3DControllerCall42>(taken[42]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelFormatChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisReversedChangedBySender(QObject
  //      *sender)
  void handleAxisReversedChangedBySender(QObject *sender) override {
    if (taken[43]) {
      int handled = 0;
      CuteAbstract3DControllerCall43 call = reinterpret_cast<CuteAbstract3DControllerCall43>(taken[43]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisReversedChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisFormatterDirtyBySender(QObject
  //      *sender)
  void handleAxisFormatterDirtyBySender(QObject *sender) override {
    if (taken[44]) {
      int handled = 0;
      CuteAbstract3DControllerCall44 call = reinterpret_cast<CuteAbstract3DControllerCall44>(taken[44]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisFormatterDirtyBySender(sender);
  }

  //  void Abstract3DController::handleAxisLabelAutoRotationChangedBySender
  //      (QObject *sender)
  void handleAxisLabelAutoRotationChangedBySender(QObject *sender) override {
    if (taken[45]) {
      int handled = 0;
      CuteAbstract3DControllerCall45 call = reinterpret_cast<CuteAbstract3DControllerCall45>(taken[45]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisLabelAutoRotationChangedBySender(sender);
  }

  //  void Abstract3DController::handleAxisTitleVisibilityChangedBySender(Q
  //      Object *sender)
  void handleAxisTitleVisibilityChangedBySender(QObject *sender) override {
    if (taken[46]) {
      int handled = 0;
      CuteAbstract3DControllerCall46 call = reinterpret_cast<CuteAbstract3DControllerCall46>(taken[46]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleVisibilityChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
  //      *sender)
  void handleAxisTitleFixedChangedBySender(QObject *sender) override {
    if (taken[47]) {
      int handled = 0;
      CuteAbstract3DControllerCall47 call = reinterpret_cast<CuteAbstract3DControllerCall47>(taken[47]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleAxisTitleFixedChangedBySender(sender);
  }

  //  void
  //      Abstract3DController::handleSeriesVisibilityChangedBySender(QObje
  //      ct *sender)
  void handleSeriesVisibilityChangedBySender(QObject *sender) override {
    if (taken[48]) {
      int handled = 0;
      CuteAbstract3DControllerCall48 call = reinterpret_cast<CuteAbstract3DControllerCall48>(taken[48]);
      call(this, sender, &handled);
      if (handled) return;
    }
    Abstract3DController::handleSeriesVisibilityChangedBySender(sender);
  }

  //  void Abstract3DController::handlePendingClick()
  void handlePendingClick() override {
    if (taken[49]) {
      int handled = 0;
      CuteAbstract3DControllerCall49 call = reinterpret_cast<CuteAbstract3DControllerCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::handlePendingClick();
  }

  //  void Abstract3DController::handlePendingGraphPositionQuery()
  void handlePendingGraphPositionQuery() override {
    if (taken[50]) {
      int handled = 0;
      CuteAbstract3DControllerCall50 call = reinterpret_cast<CuteAbstract3DControllerCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::handlePendingGraphPositionQuery();
  }

  //  void Abstract3DController::adjustAxisRanges()
  void adjustAxisRanges() override {
    if (taken[51]) {
      int handled = 0;
      CuteAbstract3DControllerCall51 call = reinterpret_cast<CuteAbstract3DControllerCall51>(taken[51]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QAbstract3DAxis *Abstract3DController::createDefaultAxis(QAbstract3DA
  //      xis::AxisOrientation orientation)
  QAbstract3DAxis *createDefaultAxis(
      QAbstract3DAxis::AxisOrientation orientation) override {
    if (taken[52]) {
      int handled = 0;
      CuteAbstract3DControllerCall52 call = reinterpret_cast<CuteAbstract3DControllerCall52>(taken[52]);
      void * given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return static_cast<QAbstract3DAxis *>(given);
    }
    return Abstract3DController::createDefaultAxis(orientation);
  }

  //  void Abstract3DController::startRecordingRemovesAndInserts()
  void startRecordingRemovesAndInserts() override {
    if (taken[53]) {
      int handled = 0;
      CuteAbstract3DControllerCall53 call = reinterpret_cast<CuteAbstract3DControllerCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DController::startRecordingRemovesAndInserts();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteAbstract3DControllerCall54 call = reinterpret_cast<CuteAbstract3DControllerCall54>(taken[54]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteAbstract3DControllerCall55 call = reinterpret_cast<CuteAbstract3DControllerCall55>(taken[55]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteAbstract3DControllerCall56 call = reinterpret_cast<CuteAbstract3DControllerCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteAbstract3DControllerCall57 call = reinterpret_cast<CuteAbstract3DControllerCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteAbstract3DControllerCall58 call = reinterpret_cast<CuteAbstract3DControllerCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[59]) {
      int handled = 0;
      CuteAbstract3DControllerCall59 call = reinterpret_cast<CuteAbstract3DControllerCall59>(taken[59]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[60]) {
      int handled = 0;
      CuteAbstract3DControllerCall60 call = reinterpret_cast<CuteAbstract3DControllerCall60>(taken[60]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Abstract3DController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20Abstract3DController10metaObjectEv(
    const Abstract3DController *self) {
  return self->metaObject();
}

//  QString Abstract3DController::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20Abstract3DController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Abstract3DController::tr(s, c, n));
}

//  Abstract3DController::~Abstract3DController()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DControllerD1Ev(Abstract3DController *self) {
  delete self;
}

//  bool Abstract3DController::isInitialized()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20Abstract3DController13isInitializedEv(
    Abstract3DController *self) {
  return self->isInitialized();
}

//  void Abstract3DController::synchDataToRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController19synchDataToRendererEv(
    Abstract3DController *self) {
  self->synchDataToRenderer();
}

//  void Abstract3DController::render(const GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController6renderEj(
    Abstract3DController *self,
    GLuint defaultFboHandle) {
  self->render(defaultFboHandle);
}

//  void Abstract3DController::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16initializeOpenGLEv(
    Abstract3DController *self) {
  self->initializeOpenGL();
}

//  void Abstract3DController::setRenderer(Abstract3DRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController11setRendererEP18Abstract3DRenderer(
    Abstract3DController *self,
    Abstract3DRenderer *renderer) {
  self->setRenderer(renderer);
}

//  void Abstract3DController::addSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  self->addSeries(series);
}

//  void Abstract3DController::insertSeries(int index, QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSeries(
    Abstract3DController *self,
    int index,
    QAbstract3DSeries *series) {
  self->insertSeries(index, series);
}

//  void Abstract3DController::removeSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  self->removeSeries(series);
}

//  bool Abstract3DController::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  QList<QAbstract3DSeries *> Abstract3DController::seriesList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DSeries *> *ritual_ZN20Abstract3DController10seriesListEv(
    Abstract3DController *self) {
  return new QList<QAbstract3DSeries *>(self->seriesList());
}

//  void Abstract3DController::setAxisX(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisX() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK20Abstract3DController5axisXEv(
    const Abstract3DController *self) {
  return self->axisX();
}

//  void Abstract3DController::setAxisY(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisY() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK20Abstract3DController5axisYEv(
    const Abstract3DController *self) {
  return self->axisY();
}

//  void Abstract3DController::setAxisZ(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisZ() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK20Abstract3DController5axisZEv(
    const Abstract3DController *self) {
  return self->axisZ();
}

//  void Abstract3DController::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->addAxis(axis);
}

//  void Abstract3DController::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QAbstract3DAxis *> Abstract3DController::axes() const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DAxis *> *ritual_ZNK20Abstract3DController4axesEv(
    const Abstract3DController *self) {
  return new QList<QAbstract3DAxis *>(self->axes());
}

//  void Abstract3DController::addInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->addInputHandler(inputHandler);
}

//  void Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->releaseInputHandler(inputHandler);
}

//  void Abstract3DController::setActiveInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->setActiveInputHandler(inputHandler);
}

//  QAbstract3DInputHandler *Abstract3DController::activeInputHandler()
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_ZN20Abstract3DController18activeInputHandlerEv(
    Abstract3DController *self) {
  return self->activeInputHandler();
}

//  QList<QAbstract3DInputHandler *> Abstract3DController::inputHandlers()
//      const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DInputHandler *> *ritual_ZNK20Abstract3DController13inputHandlersEv(
    const Abstract3DController *self) {
  return new QList<QAbstract3DInputHandler *>(self->inputHandlers());
}

//  void Abstract3DController::addTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController8addThemeEP8Q3DTheme(
    Abstract3DController *self,
    Q3DTheme *theme) {
  self->addTheme(theme);
}

//  void Abstract3DController::releaseTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController12releaseThemeEP8Q3DTheme(
    Abstract3DController *self,
    Q3DTheme *theme) {
  self->releaseTheme(theme);
}

//  void Abstract3DController::setActiveTheme(Q3DTheme *theme, bool force)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb(
    Abstract3DController *self,
    Q3DTheme *theme,
    bool force) {
  self->setActiveTheme(theme, force);
}

//  Q3DTheme *Abstract3DController::activeTheme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZNK20Abstract3DController11activeThemeEv(
    const Abstract3DController *self) {
  return self->activeTheme();
}

//  QList<Q3DTheme *> Abstract3DController::themes() const
extern "C" Q_DECL_EXPORT
QList<Q3DTheme *> *ritual_ZNK20Abstract3DController6themesEv(
    const Abstract3DController *self) {
  return new QList<Q3DTheme *>(self->themes());
}

//  void
//      Abstract3DController::setSelectionMode(QAbstract3DGraph::SelectionFla
//      gs mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Abstract3DController *self,
    int mode) {
  self->setSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  QAbstract3DGraph::SelectionFlags Abstract3DController::selectionMode()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20Abstract3DController13selectionModeEv(
    const Abstract3DController *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  void
//      Abstract3DController::setShadowQuality(QAbstract3DGraph::ShadowQualit
//      y quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Abstract3DController *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->setShadowQuality(quality);
}

//  void
//      Abstract3DController::doSetShadowQuality(QAbstract3DGraph::ShadowQual
//      ity quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Abstract3DController *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->doSetShadowQuality(quality);
}

//  QAbstract3DGraph::ShadowQuality Abstract3DController::shadowQuality()
//      const
extern "C" Q_DECL_EXPORT
QAbstract3DGraph::ShadowQuality ritual_ZNK20Abstract3DController13shadowQualityEv(
    const Abstract3DController *self) {
  return self->shadowQuality();
}

//  bool Abstract3DController::shadowsSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController16shadowsSupportedEv(
    const Abstract3DController *self) {
  return self->shadowsSupported();
}

//  void Abstract3DController::setOptimizationHints(QAbstract3DGraph::Optimiz
//      ationHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController20setOptimizationHintsE6QFlagsIN16QAbstract3DGraph16OptimizationHintEE(
    Abstract3DController *self,
    int hints) {
  self->setOptimizationHints(
      QFlags<QAbstract3DGraph::OptimizationHint>::fromInt(hints));
}

//  QAbstract3DGraph::OptimizationHints
//      Abstract3DController::optimizationHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20Abstract3DController17optimizationHintsEv(
    const Abstract3DController *self) {
  return static_cast<int>(self->optimizationHints().toInt());
}

//  bool Abstract3DController::isSlicingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController15isSlicingActiveEv(
    const Abstract3DController *self) {
  return self->isSlicingActive();
}

//  void Abstract3DController::setSlicingActive(bool isSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16setSlicingActiveEb(
    Abstract3DController *self,
    bool isSlicing) {
  self->setSlicingActive(isSlicing);
}

//  Q3DScene *Abstract3DController::scene()
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZN20Abstract3DController5sceneEv(
    Abstract3DController *self) {
  return self->scene();
}

//  void Abstract3DController::markDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController13markDataDirtyEv(
    Abstract3DController *self) {
  self->markDataDirty();
}

//  void Abstract3DController::markSeriesVisualsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController22markSeriesVisualsDirtyEv(
    Abstract3DController *self) {
  self->markSeriesVisualsDirty();
}

//  void Abstract3DController::requestRender(QOpenGLFramebufferObject *fbo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController13requestRenderEP24QOpenGLFramebufferObject(
    Abstract3DController *self,
    QOpenGLFramebufferObject *fbo) {
  self->requestRender(fbo);
}

//  int Abstract3DController::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
int ritual_ZN20Abstract3DController13addCustomItemEP13QCustom3DItem(
    Abstract3DController *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void Abstract3DController::deleteCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController17deleteCustomItemsEv(
    Abstract3DController *self) {
  self->deleteCustomItems();
}

//  void Abstract3DController::deleteCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16deleteCustomItemEP13QCustom3DItem(
    Abstract3DController *self,
    QCustom3DItem *item) {
  self->deleteCustomItem(item);
}

//  void Abstract3DController::deleteCustomItem(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16deleteCustomItemERK9QVector3D(
    Abstract3DController *self,
    const QVector3D *position) {
  self->deleteCustomItem(*position);
}

//  void Abstract3DController::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController17releaseCustomItemEP13QCustom3DItem(
    Abstract3DController *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  QList<QCustom3DItem *> Abstract3DController::customItems() const
extern "C" Q_DECL_EXPORT
QList<QCustom3DItem *> *ritual_ZNK20Abstract3DController11customItemsEv(
    const Abstract3DController *self) {
  return new QList<QCustom3DItem *>(self->customItems());
}

//  int Abstract3DController::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20Abstract3DController18selectedLabelIndexEv(
    const Abstract3DController *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *Abstract3DController::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK20Abstract3DController12selectedAxisEv(
    const Abstract3DController *self) {
  return self->selectedAxis();
}

//  int Abstract3DController::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20Abstract3DController23selectedCustomItemIndexEv(
    const Abstract3DController *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *Abstract3DController::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK20Abstract3DController18selectedCustomItemEv(
    const Abstract3DController *self) {
  return self->selectedCustomItem();
}

//  void Abstract3DController::setOrthoProjection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController18setOrthoProjectionEb(
    Abstract3DController *self,
    bool enable) {
  self->setOrthoProjection(enable);
}

//  bool Abstract3DController::isOrthoProjection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController17isOrthoProjectionEv(
    const Abstract3DController *self) {
  return self->isOrthoProjection();
}

//  void Abstract3DController::setMeasureFps(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController13setMeasureFpsEb(
    Abstract3DController *self,
    bool enable) {
  self->setMeasureFps(enable);
}

//  bool Abstract3DController::measureFps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController10measureFpsEv(
    const Abstract3DController *self) {
  return self->measureFps();
}

//  qreal Abstract3DController::currentFps() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20Abstract3DController10currentFpsEv(
    const Abstract3DController *self) {
  return self->currentFps();
}

//  QAbstract3DGraph::ElementType Abstract3DController::selectedElement()
//      const
extern "C" Q_DECL_EXPORT
QAbstract3DGraph::ElementType ritual_ZNK20Abstract3DController15selectedElementEv(
    const Abstract3DController *self) {
  return self->selectedElement();
}

//  void Abstract3DController::setAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController14setAspectRatioEd(
    Abstract3DController *self,
    qreal ratio) {
  self->setAspectRatio(ratio);
}

//  qreal Abstract3DController::aspectRatio()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20Abstract3DController11aspectRatioEv(
    Abstract3DController *self) {
  return self->aspectRatio();
}

//  void Abstract3DController::setHorizontalAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController24setHorizontalAspectRatioEd(
    Abstract3DController *self,
    qreal ratio) {
  self->setHorizontalAspectRatio(ratio);
}

//  qreal Abstract3DController::horizontalAspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20Abstract3DController21horizontalAspectRatioEv(
    const Abstract3DController *self) {
  return self->horizontalAspectRatio();
}

//  void Abstract3DController::setReflection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController13setReflectionEb(
    Abstract3DController *self,
    bool enable) {
  self->setReflection(enable);
}

//  bool Abstract3DController::reflection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController10reflectionEv(
    const Abstract3DController *self) {
  return self->reflection();
}

//  void Abstract3DController::setReflectivity(qreal reflectivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController15setReflectivityEd(
    Abstract3DController *self,
    qreal reflectivity) {
  self->setReflectivity(reflectivity);
}

//  qreal Abstract3DController::reflectivity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20Abstract3DController12reflectivityEv(
    const Abstract3DController *self) {
  return self->reflectivity();
}

//  void Abstract3DController::setPolar(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController8setPolarEb(
    Abstract3DController *self,
    bool enable) {
  self->setPolar(enable);
}

//  bool Abstract3DController::isPolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController7isPolarEv(
    const Abstract3DController *self) {
  return self->isPolar();
}

//  void Abstract3DController::setRadialLabelOffset(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController20setRadialLabelOffsetEf(
    Abstract3DController *self,
    float offset) {
  self->setRadialLabelOffset(offset);
}

//  float Abstract3DController::radialLabelOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20Abstract3DController17radialLabelOffsetEv(
    const Abstract3DController *self) {
  return self->radialLabelOffset();
}

//  void Abstract3DController::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController9setLocaleERK7QLocale(
    Abstract3DController *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale Abstract3DController::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK20Abstract3DController6localeEv(
    const Abstract3DController *self) {
  return new QLocale(self->locale());
}

//  QVector3D Abstract3DController::queriedGraphPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK20Abstract3DController20queriedGraphPositionEv(
    const Abstract3DController *self) {
  return new QVector3D(self->queriedGraphPosition());
}

//  void Abstract3DController::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController9setMarginEd(
    Abstract3DController *self,
    qreal margin) {
  self->setMargin(margin);
}

//  qreal Abstract3DController::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20Abstract3DController6marginEv(
    const Abstract3DController *self) {
  return self->margin();
}

//  void Abstract3DController::emitNeedRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController14emitNeedRenderEv(
    Abstract3DController *self) {
  self->emitNeedRender();
}

//  void Abstract3DController::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController14clearSelectionEv(
    Abstract3DController *self) {
  self->clearSelection();
}

//  void Abstract3DController::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEvent(
    Abstract3DController *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void Abstract3DController::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController10touchEventEP11QTouchEvent(
    Abstract3DController *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void Abstract3DController::mousePressEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mousePressEvent(event, *mousePos);
}

//  void Abstract3DController::mouseReleaseEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseReleaseEvent(event, *mousePos);
}

//  void Abstract3DController::mouseMoveEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void Abstract3DController::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController10wheelEventEP11QWheelEvent(
    Abstract3DController *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void Abstract3DController::handleAxisTitleChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisTitleChangedBySender(sender);
}

//  void Abstract3DController::handleAxisLabelsChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisLabelsChangedBySender(sender);
}

//  void Abstract3DController::handleAxisRangeChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisRangeChangedBySender(sender);
}

//  void Abstract3DController::handleAxisSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController37handleAxisSegmentCountChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisSegmentCountChangedBySender(sender);
}

//  void
//      Abstract3DController::handleAxisSubSegmentCountChangedBySender(QObjec
//      t *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController40handleAxisSubSegmentCountChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisSubSegmentCountChangedBySender(sender);
}

//  void Abstract3DController::handleAxisAutoAdjustRangeChangedInOrientation(
//      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController45handleAxisAutoAdjustRangeChangedInOrientationEN15QAbstract3DAxis15AxisOrientationEb(
    Abstract3DController *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChangedInOrientation(
      orientation,
      autoAdjust);
}

//  void Abstract3DController::handleAxisLabelFormatChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController36handleAxisLabelFormatChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisLabelFormatChangedBySender(sender);
}

//  void Abstract3DController::handleAxisReversedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController33handleAxisReversedChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisReversedChangedBySender(sender);
}

//  void Abstract3DController::handleAxisFormatterDirtyBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisFormatterDirtyBySender(sender);
}

//  void
//      Abstract3DController::handleAxisLabelAutoRotationChangedBySender(QObj
//      ect *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController42handleAxisLabelAutoRotationChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisLabelAutoRotationChangedBySender(sender);
}

//  void
//      Abstract3DController::handleAxisTitleVisibilityChangedBySender(QObjec
//      t *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController40handleAxisTitleVisibilityChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisTitleVisibilityChangedBySender(sender);
}

//  void Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController35handleAxisTitleFixedChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleAxisTitleFixedChangedBySender(sender);
}

//  void Abstract3DController::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController37handleSeriesVisibilityChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->handleSeriesVisibilityChangedBySender(sender);
}

//  void Abstract3DController::handlePendingClick()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController18handlePendingClickEv(
    Abstract3DController *self) {
  self->handlePendingClick();
}

//  void Abstract3DController::handlePendingGraphPositionQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController31handlePendingGraphPositionQueryEv(
    Abstract3DController *self) {
  self->handlePendingGraphPositionQuery();
}

//  void Abstract3DController::adjustAxisRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16adjustAxisRangesEv(
    Abstract3DController *self) {
  self->adjustAxisRanges();
}

//  void Abstract3DController::markSeriesItemLabelsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController25markSeriesItemLabelsDirtyEv(
    Abstract3DController *self) {
  self->markSeriesItemLabelsDirty();
}

//  bool Abstract3DController::isOpenGLES() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Abstract3DController10isOpenGLESEv(
    const Abstract3DController *self) {
  return self->isOpenGLES();
}

//  void Abstract3DController::destroyRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController15destroyRendererEv(
    Abstract3DController *self) {
  self->destroyRenderer();
}

//  void Abstract3DController::handleAxisTitleChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController22handleAxisTitleChangedERK7QString(
    Abstract3DController *self,
    const QString *title) {
  self->handleAxisTitleChanged(*title);
}

//  void Abstract3DController::handleAxisLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController23handleAxisLabelsChangedEv(
    Abstract3DController *self) {
  self->handleAxisLabelsChanged();
}

//  void Abstract3DController::handleAxisRangeChanged(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController22handleAxisRangeChangedEff(
    Abstract3DController *self,
    float min,
    float max) {
  self->handleAxisRangeChanged(min, max);
}

//  void Abstract3DController::handleAxisSegmentCountChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController29handleAxisSegmentCountChangedEi(
    Abstract3DController *self,
    int count) {
  self->handleAxisSegmentCountChanged(count);
}

//  void Abstract3DController::handleAxisSubSegmentCountChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController32handleAxisSubSegmentCountChangedEi(
    Abstract3DController *self,
    int count) {
  self->handleAxisSubSegmentCountChanged(count);
}

//  void Abstract3DController::handleAxisAutoAdjustRangeChanged(bool
//      autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController32handleAxisAutoAdjustRangeChangedEb(
    Abstract3DController *self,
    bool autoAdjust) {
  self->handleAxisAutoAdjustRangeChanged(autoAdjust);
}

//  void Abstract3DController::handleAxisLabelFormatChanged(const QString
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController28handleAxisLabelFormatChangedERK7QString(
    Abstract3DController *self,
    const QString *format) {
  self->handleAxisLabelFormatChanged(*format);
}

//  void Abstract3DController::handleAxisReversedChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController25handleAxisReversedChangedEb(
    Abstract3DController *self,
    bool enable) {
  self->handleAxisReversedChanged(enable);
}

//  void Abstract3DController::handleAxisFormatterDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController24handleAxisFormatterDirtyEv(
    Abstract3DController *self) {
  self->handleAxisFormatterDirty();
}

//  void Abstract3DController::handleAxisLabelAutoRotationChanged(float
//      angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController34handleAxisLabelAutoRotationChangedEf(
    Abstract3DController *self,
    float angle) {
  self->handleAxisLabelAutoRotationChanged(angle);
}

//  void Abstract3DController::handleAxisTitleVisibilityChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController32handleAxisTitleVisibilityChangedEb(
    Abstract3DController *self,
    bool visible) {
  self->handleAxisTitleVisibilityChanged(visible);
}

//  void Abstract3DController::handleAxisTitleFixedChanged(bool fixed)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController27handleAxisTitleFixedChangedEb(
    Abstract3DController *self,
    bool fixed) {
  self->handleAxisTitleFixedChanged(fixed);
}

//  void Abstract3DController::handleInputViewChanged(QAbstract3DInputHandler
//      ::InputView view)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController22handleInputViewChangedEN23QAbstract3DInputHandler9InputViewE(
    Abstract3DController *self,
    QAbstract3DInputHandler::InputView view) {
  self->handleInputViewChanged(view);
}

//  void Abstract3DController::handleInputPositionChanged(const QPoint
//      &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController26handleInputPositionChangedERK6QPoint(
    Abstract3DController *self,
    const QPoint *position) {
  self->handleInputPositionChanged(*position);
}

//  void Abstract3DController::handleSeriesVisibilityChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController29handleSeriesVisibilityChangedEb(
    Abstract3DController *self,
    bool visible) {
  self->handleSeriesVisibilityChanged(visible);
}

//  void
//      Abstract3DController::handleThemeColorStyleChanged(Q3DTheme::ColorSty
//      le style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController28handleThemeColorStyleChangedEN8Q3DTheme10ColorStyleE(
    Abstract3DController *self,
    Q3DTheme::ColorStyle style) {
  self->handleThemeColorStyleChanged(style);
}

//  void Abstract3DController::handleThemeBaseColorsChanged(const
//      QList<QColor> &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController28handleThemeBaseColorsChangedERK5QListI6QColorE(
    Abstract3DController *self,
    const QList<QColor> *color) {
  self->handleThemeBaseColorsChanged(*color);
}

//  void Abstract3DController::handleThemeBaseGradientsChanged(const
//      QList<QLinearGradient> &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController31handleThemeBaseGradientsChangedERK5QListI15QLinearGradientE(
    Abstract3DController *self,
    const QList<QLinearGradient> *gradient) {
  self->handleThemeBaseGradientsChanged(*gradient);
}

//  void Abstract3DController::handleThemeSingleHighlightColorChanged(const
//      QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController38handleThemeSingleHighlightColorChangedERK6QColor(
    Abstract3DController *self,
    const QColor *color) {
  self->handleThemeSingleHighlightColorChanged(*color);
}

//  void
//      Abstract3DController::handleThemeSingleHighlightGradientChanged(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController41handleThemeSingleHighlightGradientChangedERK15QLinearGradient(
    Abstract3DController *self,
    const QLinearGradient *gradient) {
  self->handleThemeSingleHighlightGradientChanged(*gradient);
}

//  void Abstract3DController::handleThemeMultiHighlightColorChanged(const
//      QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController37handleThemeMultiHighlightColorChangedERK6QColor(
    Abstract3DController *self,
    const QColor *color) {
  self->handleThemeMultiHighlightColorChanged(*color);
}

//  void Abstract3DController::handleThemeMultiHighlightGradientChanged(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController40handleThemeMultiHighlightGradientChangedERK15QLinearGradient(
    Abstract3DController *self,
    const QLinearGradient *gradient) {
  self->handleThemeMultiHighlightGradientChanged(*gradient);
}

//  void Abstract3DController::handleThemeTypeChanged(Q3DTheme::Theme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController22handleThemeTypeChangedEN8Q3DTheme5ThemeE(
    Abstract3DController *self,
    Q3DTheme::Theme theme) {
  self->handleThemeTypeChanged(theme);
}

//  void Abstract3DController::handleRequestShadowQuality(QAbstract3DGraph::S
//      hadowQuality quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController26handleRequestShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Abstract3DController *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->handleRequestShadowQuality(quality);
}

//  void Abstract3DController::updateCustomItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController16updateCustomItemEv(
    Abstract3DController *self) {
  self->updateCustomItem();
}

//  QAbstract3DAxis
//      *Abstract3DController::createDefaultAxis(QAbstract3DAxis::AxisOrienta
//      tion orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    Abstract3DController *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  QValue3DAxis *Abstract3DController::createDefaultValueAxis()
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZN20Abstract3DController22createDefaultValueAxisEv(
    Abstract3DController *self) {
  return self->createDefaultValueAxis();
}

//  QCategory3DAxis *Abstract3DController::createDefaultCategoryAxis()
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN20Abstract3DController25createDefaultCategoryAxisEv(
    Abstract3DController *self) {
  return self->createDefaultCategoryAxis();
}

//  void Abstract3DController::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv(
    Abstract3DController *self) {
  self->startRecordingRemovesAndInserts();
}

//  a Python function taken by a CuteAbstract3DController, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Abstract3DController(
    Abstract3DController *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstract3DController *>(self)->take(key, call);
}

//  void Abstract3DController::synchDataToRenderer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController19synchDataToRendererEv(
    Abstract3DController *self) {
  self->Abstract3DController::synchDataToRenderer();
}

//  void Abstract3DController::render(const GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController6renderEj(
    Abstract3DController *self,
    GLuint defaultFboHandle) {
  self->Abstract3DController::render(defaultFboHandle);
}

//  void Abstract3DController::addSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController9addSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  self->Abstract3DController::addSeries(series);
}

//  void Abstract3DController::insertSeries(int index, QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController12insertSeriesEiP17QAbstract3DSeries(
    Abstract3DController *self,
    int index,
    QAbstract3DSeries *series) {
  self->Abstract3DController::insertSeries(index, series);
}

//  void Abstract3DController::removeSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController12removeSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  self->Abstract3DController::removeSeries(series);
}

//  bool Abstract3DController::hasSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20Abstract3DController9hasSeriesEP17QAbstract3DSeries(
    Abstract3DController *self,
    QAbstract3DSeries *series) {
  return self->Abstract3DController::hasSeries(series);
}

//  void Abstract3DController::setAxisX(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController8setAxisXEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->Abstract3DController::setAxisX(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisX() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZNK20Abstract3DController5axisXEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::axisX();
}

//  void Abstract3DController::setAxisY(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController8setAxisYEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->Abstract3DController::setAxisY(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisY() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZNK20Abstract3DController5axisYEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::axisY();
}

//  void Abstract3DController::setAxisZ(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController8setAxisZEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->Abstract3DController::setAxisZ(axis);
}

//  QAbstract3DAxis *Abstract3DController::axisZ() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZNK20Abstract3DController5axisZEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::axisZ();
}

//  void Abstract3DController::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController7addAxisEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->Abstract3DController::addAxis(axis);
}

//  void Abstract3DController::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController11releaseAxisEP15QAbstract3DAxis(
    Abstract3DController *self,
    QAbstract3DAxis *axis) {
  self->Abstract3DController::releaseAxis(axis);
}

//  void Abstract3DController::addInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController15addInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->Abstract3DController::addInputHandler(inputHandler);
}

//  void Abstract3DController::releaseInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController19releaseInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->Abstract3DController::releaseInputHandler(inputHandler);
}

//  void Abstract3DController::setActiveInputHandler(QAbstract3DInputHandler
//      *inputHandler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController21setActiveInputHandlerEP23QAbstract3DInputHandler(
    Abstract3DController *self,
    QAbstract3DInputHandler *inputHandler) {
  self->Abstract3DController::setActiveInputHandler(inputHandler);
}

//  QAbstract3DInputHandler *Abstract3DController::activeInputHandler()
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandler *ritual_own_ZN20Abstract3DController18activeInputHandlerEv(
    Abstract3DController *self) {
  return self->Abstract3DController::activeInputHandler();
}

//  void Abstract3DController::addTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController8addThemeEP8Q3DTheme(
    Abstract3DController *self,
    Q3DTheme *theme) {
  self->Abstract3DController::addTheme(theme);
}

//  void Abstract3DController::releaseTheme(Q3DTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController12releaseThemeEP8Q3DTheme(
    Abstract3DController *self,
    Q3DTheme *theme) {
  self->Abstract3DController::releaseTheme(theme);
}

//  void Abstract3DController::setActiveTheme(Q3DTheme *theme, bool force)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController14setActiveThemeEP8Q3DThemeb(
    Abstract3DController *self,
    Q3DTheme *theme,
    bool force) {
  self->Abstract3DController::setActiveTheme(theme, force);
}

//  Q3DTheme *Abstract3DController::activeTheme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_own_ZNK20Abstract3DController11activeThemeEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::activeTheme();
}

//  void
//      Abstract3DController::setSelectionMode(QAbstract3DGraph::SelectionFla
//      gs mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController16setSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Abstract3DController *self,
    int mode) {
  self->Abstract3DController::setSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  QAbstract3DGraph::SelectionFlags Abstract3DController::selectionMode()
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20Abstract3DController13selectionModeEv(
    const Abstract3DController *self) {
  return static_cast<int>(
      self->Abstract3DController::selectionMode().toInt());
}

//  void
//      Abstract3DController::setShadowQuality(QAbstract3DGraph::ShadowQualit
//      y quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController16setShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Abstract3DController *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->Abstract3DController::setShadowQuality(quality);
}

//  void
//      Abstract3DController::doSetShadowQuality(QAbstract3DGraph::ShadowQual
//      ity quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController18doSetShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Abstract3DController *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->Abstract3DController::doSetShadowQuality(quality);
}

//  QAbstract3DGraph::ShadowQuality Abstract3DController::shadowQuality()
//      const
extern "C" Q_DECL_EXPORT
QAbstract3DGraph::ShadowQuality ritual_own_ZNK20Abstract3DController13shadowQualityEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::shadowQuality();
}

//  bool Abstract3DController::shadowsSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20Abstract3DController16shadowsSupportedEv(
    const Abstract3DController *self) {
  return self->Abstract3DController::shadowsSupported();
}

//  void Abstract3DController::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController21mouseDoubleClickEventEP11QMouseEvent(
    Abstract3DController *self,
    QMouseEvent *event) {
  self->Abstract3DController::mouseDoubleClickEvent(event);
}

//  void Abstract3DController::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController10touchEventEP11QTouchEvent(
    Abstract3DController *self,
    QTouchEvent *event) {
  self->Abstract3DController::touchEvent(event);
}

//  void Abstract3DController::mousePressEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController15mousePressEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Abstract3DController::mousePressEvent(event, *mousePos);
}

//  void Abstract3DController::mouseReleaseEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController17mouseReleaseEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Abstract3DController::mouseReleaseEvent(event, *mousePos);
}

//  void Abstract3DController::mouseMoveEvent(QMouseEvent *event, const
//      QPoint &mousePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController14mouseMoveEventEP11QMouseEventRK6QPoint(
    Abstract3DController *self,
    QMouseEvent *event,
    const QPoint *mousePos) {
  self->Abstract3DController::mouseMoveEvent(event, *mousePos);
}

#if QT_CONFIG(wheelevent)
//  void Abstract3DController::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController10wheelEventEP11QWheelEvent(
    Abstract3DController *self,
    QWheelEvent *event) {
  self->Abstract3DController::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void Abstract3DController::handleAxisTitleChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController30handleAxisTitleChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisTitleChangedBySender(sender);
}

//  void Abstract3DController::handleAxisLabelsChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController31handleAxisLabelsChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisLabelsChangedBySender(sender);
}

//  void Abstract3DController::handleAxisRangeChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController30handleAxisRangeChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisRangeChangedBySender(sender);
}

//  void Abstract3DController::handleAxisSegmentCountChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController37handleAxisSegmentCountChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisSegmentCountChangedBySender(sender);
}

//  void
//      Abstract3DController::handleAxisSubSegmentCountChangedBySender(QObjec
//      t *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController40handleAxisSubSegmentCountChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisSubSegmentCountChangedBySender(
      sender);
}

//  void Abstract3DController::handleAxisLabelFormatChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController36handleAxisLabelFormatChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisLabelFormatChangedBySender(sender);
}

//  void Abstract3DController::handleAxisReversedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController33handleAxisReversedChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisReversedChangedBySender(sender);
}

//  void Abstract3DController::handleAxisFormatterDirtyBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController32handleAxisFormatterDirtyBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisFormatterDirtyBySender(sender);
}

//  void
//      Abstract3DController::handleAxisLabelAutoRotationChangedBySender(QObj
//      ect *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController42handleAxisLabelAutoRotationChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisLabelAutoRotationChangedBySender(
      sender);
}

//  void
//      Abstract3DController::handleAxisTitleVisibilityChangedBySender(QObjec
//      t *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController40handleAxisTitleVisibilityChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisTitleVisibilityChangedBySender(
      sender);
}

//  void Abstract3DController::handleAxisTitleFixedChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController35handleAxisTitleFixedChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleAxisTitleFixedChangedBySender(sender);
}

//  void Abstract3DController::handleSeriesVisibilityChangedBySender(QObject
//      *sender)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController37handleSeriesVisibilityChangedBySenderEP7QObject(
    Abstract3DController *self,
    QObject *sender) {
  self->Abstract3DController::handleSeriesVisibilityChangedBySender(sender);
}

//  void Abstract3DController::handlePendingClick()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController18handlePendingClickEv(
    Abstract3DController *self) {
  self->Abstract3DController::handlePendingClick();
}

//  void Abstract3DController::handlePendingGraphPositionQuery()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController31handlePendingGraphPositionQueryEv(
    Abstract3DController *self) {
  self->Abstract3DController::handlePendingGraphPositionQuery();
}

//  QAbstract3DAxis
//      *Abstract3DController::createDefaultAxis(QAbstract3DAxis::AxisOrienta
//      tion orientation)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_own_ZN20Abstract3DController17createDefaultAxisEN15QAbstract3DAxis15AxisOrientationE(
    Abstract3DController *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  return static_cast<OwnAbstract3DController *>(self)->OwnAbstract3DController::createDefaultAxis(
      orientation);
}

//  void Abstract3DController::startRecordingRemovesAndInserts()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20Abstract3DController31startRecordingRemovesAndInsertsEv(
    Abstract3DController *self) {
  static_cast<OwnAbstract3DController *>(self)->OwnAbstract3DController::startRecordingRemovesAndInserts();
}
