//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartdatetimeaxisx_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_datetime_axis)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartdatetimeaxisx_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>
#include <QtCore/QList>

//  Only a class built on ChartDateTimeAxisX may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnChartDateTimeAxisX : ChartDateTimeAxisX {
  using ChartDateTimeAxisX::updateGeometry;
};

//  A ChartDateTimeAxisX that Python can take functions over in. Every ChartDateTimeAxisX
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteChartDateTimeAxisXCall0)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteChartDateTimeAxisXCall3)(const void *, int *);
typedef bool (*CuteChartDateTimeAxisXCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall5)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall6)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisXCall7)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisXCall8)(const void *, const QBrush *, int *);
typedef void (*CuteChartDateTimeAxisXCall9)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisXCall10)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisXCall11)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisXCall12)(const void *, const QColor *, int *);
typedef void (*CuteChartDateTimeAxisXCall13)(const void *, const QColor *, int *);
typedef void * (*CuteChartDateTimeAxisXCall14)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteChartDateTimeAxisXCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall16)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall17)(const void *, ChartPresenter *, int *);
typedef void (*CuteChartDateTimeAxisXCall18)(const void *, ChartThemeManager *, int *);
typedef void (*CuteChartDateTimeAxisXCall19)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartDateTimeAxisXCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisXCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisXCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisXCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisXCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisXCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartDateTimeAxisXCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall30)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall31)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall32)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall33)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartDateTimeAxisXCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteChartDateTimeAxisXCall35)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall36)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisXCall37)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall38)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall40)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall41)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall43)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall44)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall45)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall46)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall47)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall48)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall49)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall50)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall51)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall52)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall54)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisXCall55)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisXCall56)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisXCall57)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisXCall58)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteChartDateTimeAxisX : public ChartDateTimeAxisX {
public:
  using ChartDateTimeAxisX::ChartDateTimeAxisX;
  void *taken[59] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN16ChartAxisElement11setGeometryERK6QRectFS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16ChartAxisElement12gridGeometryEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16ChartAxisElement9emptyAxisEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement20handleGridPenChangedERK4QPen")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement26handleMinorArrowPenChangedERK4QPen")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement25handleMinorGridPenChangedERK4QPen")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QColor")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  QSizeF ChartDateTimeAxisX::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall0 call = reinterpret_cast<CuteChartDateTimeAxisXCall0>(taken[0]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return ChartDateTimeAxisX::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void ChartDateTimeAxisX::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall1 call = reinterpret_cast<CuteChartDateTimeAxisXCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    ChartDateTimeAxisX::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CartesianChartAxis::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[2]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall2 call = reinterpret_cast<CuteChartDateTimeAxisXCall2>(taken[2]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
    CartesianChartAxis::setGeometry(axis, grid);
  }

  //  QRectF CartesianChartAxis::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall3 call = reinterpret_cast<CuteChartDateTimeAxisXCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return CartesianChartAxis::gridGeometry();
  }

  //  bool CartesianChartAxis::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[4]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall4 call = reinterpret_cast<CuteChartDateTimeAxisXCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return CartesianChartAxis::emptyAxis();
  }

#if QT_CONFIG(graphicsview)
  //  void CartesianChartAxis::setGeometry(const QRectF &size)
  void setGeometry(const QRectF &size) override {
    if (taken[5]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall5 call = reinterpret_cast<CuteChartDateTimeAxisXCall5>(taken[5]);
      call(this, &size, &handled);
      if (handled) return;
    }
    CartesianChartAxis::setGeometry(size);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CartesianChartAxis::handleArrowPenChanged(const QPen &pen)
  void handleArrowPenChanged(const QPen &pen) override {
    if (taken[6]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall6 call = reinterpret_cast<CuteChartDateTimeAxisXCall6>(taken[6]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall7 call = reinterpret_cast<CuteChartDateTimeAxisXCall7>(taken[7]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleGridPenChanged(pen);
  }

  //  void CartesianChartAxis::handleShadesBrushChanged(const QBrush
  //      &brush)
  void handleShadesBrushChanged(const QBrush &brush) override {
    if (taken[8]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall8 call = reinterpret_cast<CuteChartDateTimeAxisXCall8>(taken[8]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesBrushChanged(brush);
  }

  //  void CartesianChartAxis::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[9]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall9 call = reinterpret_cast<CuteChartDateTimeAxisXCall9>(taken[9]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[10]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall10 call = reinterpret_cast<CuteChartDateTimeAxisXCall10>(taken[10]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall11 call = reinterpret_cast<CuteChartDateTimeAxisXCall11>(taken[11]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorGridPenChanged(pen);
  }

  //  void CartesianChartAxis::handleGridLineColorChanged(const QColor
  //      &color)
  void handleGridLineColorChanged(const QColor &color) override {
    if (taken[12]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall12 call = reinterpret_cast<CuteChartDateTimeAxisXCall12>(taken[12]);
      call(this, &color, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleGridLineColorChanged(color);
  }

  //  void CartesianChartAxis::handleMinorGridLineColorChanged(const QColor
  //      &color)
  void handleMinorGridLineColorChanged(const QColor &color) override {
    if (taken[13]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall13 call = reinterpret_cast<CuteChartDateTimeAxisXCall13>(taken[13]);
      call(this, &color, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorGridLineColorChanged(color);
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[14]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall14 call = reinterpret_cast<CuteChartDateTimeAxisXCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<AxisAnimation *>(given);
    }
    return ChartAxisElement::animation();
  }

#if QT_CONFIG(graphicsview)
  //  QRectF ChartAxisElement::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[15]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall15 call = reinterpret_cast<CuteChartDateTimeAxisXCall15>(taken[15]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return ChartAxisElement::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void ChartAxisElement::paint(QPainter *a0, const
  //      QStyleOptionGraphicsItem *a1, QWidget *a2)
  void paint(
      QPainter *a0,
      const QStyleOptionGraphicsItem *a1,
      QWidget *a2) override {
    if (taken[16]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall16 call = reinterpret_cast<CuteChartDateTimeAxisXCall16>(taken[16]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    ChartAxisElement::paint(a0, a1, a2);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[17]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall17 call = reinterpret_cast<CuteChartDateTimeAxisXCall17>(taken[17]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[18]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall18 call = reinterpret_cast<CuteChartDateTimeAxisXCall18>(taken[18]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[19]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall19 call = reinterpret_cast<CuteChartDateTimeAxisXCall19>(taken[19]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[20]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall20 call = reinterpret_cast<CuteChartDateTimeAxisXCall20>(taken[20]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QGraphicsObject::event(ev);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall21 call = reinterpret_cast<CuteChartDateTimeAxisXCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall22 call = reinterpret_cast<CuteChartDateTimeAxisXCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall23 call = reinterpret_cast<CuteChartDateTimeAxisXCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall24 call = reinterpret_cast<CuteChartDateTimeAxisXCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall25 call = reinterpret_cast<CuteChartDateTimeAxisXCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall26 call = reinterpret_cast<CuteChartDateTimeAxisXCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[27]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall27 call = reinterpret_cast<CuteChartDateTimeAxisXCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[28]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall28 call = reinterpret_cast<CuteChartDateTimeAxisXCall28>(taken[28]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[29]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall29 call = reinterpret_cast<CuteChartDateTimeAxisXCall29>(taken[29]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[30]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall30 call = reinterpret_cast<CuteChartDateTimeAxisXCall30>(taken[30]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::contains(point);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::collidesWithItem(const QGraphicsItem *other,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithItem(
      const QGraphicsItem *other,
      Qt::ItemSelectionMode mode) const override {
    if (taken[31]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall31 call = reinterpret_cast<CuteChartDateTimeAxisXCall31>(taken[31]);
      bool given = call(this, other, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithItem(other, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::collidesWithPath(const QPainterPath &path,
  //      Qt::ItemSelectionMode mode) const
  bool collidesWithPath(
      const QPainterPath &path,
      Qt::ItemSelectionMode mode) const override {
    if (taken[32]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall32 call = reinterpret_cast<CuteChartDateTimeAxisXCall32>(taken[32]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[33]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall33 call = reinterpret_cast<CuteChartDateTimeAxisXCall33>(taken[33]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[34]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall34 call = reinterpret_cast<CuteChartDateTimeAxisXCall34>(taken[34]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[35]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall35 call = reinterpret_cast<CuteChartDateTimeAxisXCall35>(taken[35]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall36 call = reinterpret_cast<CuteChartDateTimeAxisXCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall37 call = reinterpret_cast<CuteChartDateTimeAxisXCall37>(taken[37]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall38 call = reinterpret_cast<CuteChartDateTimeAxisXCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall39 call = reinterpret_cast<CuteChartDateTimeAxisXCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall40 call = reinterpret_cast<CuteChartDateTimeAxisXCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall41 call = reinterpret_cast<CuteChartDateTimeAxisXCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall42 call = reinterpret_cast<CuteChartDateTimeAxisXCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall43 call = reinterpret_cast<CuteChartDateTimeAxisXCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall44 call = reinterpret_cast<CuteChartDateTimeAxisXCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall45 call = reinterpret_cast<CuteChartDateTimeAxisXCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall46 call = reinterpret_cast<CuteChartDateTimeAxisXCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall47 call = reinterpret_cast<CuteChartDateTimeAxisXCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall48 call = reinterpret_cast<CuteChartDateTimeAxisXCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall49 call = reinterpret_cast<CuteChartDateTimeAxisXCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall50 call = reinterpret_cast<CuteChartDateTimeAxisXCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall51 call = reinterpret_cast<CuteChartDateTimeAxisXCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall52 call = reinterpret_cast<CuteChartDateTimeAxisXCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall53 call = reinterpret_cast<CuteChartDateTimeAxisXCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall54 call = reinterpret_cast<CuteChartDateTimeAxisXCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall55 call = reinterpret_cast<CuteChartDateTimeAxisXCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[56]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall56 call = reinterpret_cast<CuteChartDateTimeAxisXCall56>(taken[56]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[57]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall57 call = reinterpret_cast<CuteChartDateTimeAxisXCall57>(taken[57]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[58]) {
      int handled = 0;
      CuteChartDateTimeAxisXCall58 call = reinterpret_cast<CuteChartDateTimeAxisXCall58>(taken[58]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *ChartDateTimeAxisX::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18ChartDateTimeAxisX10metaObjectEv(
    const ChartDateTimeAxisX *self) {
  return self->metaObject();
}

//  void *ChartDateTimeAxisX::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18ChartDateTimeAxisX11qt_metacastEPKc(
    ChartDateTimeAxisX *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ChartDateTimeAxisX::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18ChartDateTimeAxisX11qt_metacallEN11QMetaObject4CallEiPPv(
    ChartDateTimeAxisX *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ChartDateTimeAxisX::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18ChartDateTimeAxisX2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartDateTimeAxisX::tr(s, c, n));
}

//  ChartDateTimeAxisX::ChartDateTimeAxisX(QDateTimeAxis *axis, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
ChartDateTimeAxisX *ritual_ZN18ChartDateTimeAxisXC1EP13QDateTimeAxisP13QGraphicsItem(
    QDateTimeAxis *axis,
    QGraphicsItem *item) {
  return new CuteChartDateTimeAxisX(axis, item);
}

//  ChartDateTimeAxisX::~ChartDateTimeAxisX()
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisXD1Ev(ChartDateTimeAxisX *self) {
  delete self;
}

//  QSizeF ChartDateTimeAxisX::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18ChartDateTimeAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartDateTimeAxisX *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  QList<qreal> ChartDateTimeAxisX::calculateLayout() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK18ChartDateTimeAxisX15calculateLayoutEv(
    const ChartDateTimeAxisX *self) {
  return new QList<qreal>(self->calculateLayout());
}

//  void ChartDateTimeAxisX::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisX14updateGeometryEv(
    ChartDateTimeAxisX *self) {
  self->updateGeometry();
}

//  void ChartDateTimeAxisX::handleTickCountChanged(int tick)
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisX22handleTickCountChangedEi(
    ChartDateTimeAxisX *self,
    int tick) {
  self->handleTickCountChanged(tick);
}

//  void ChartDateTimeAxisX::handleFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisX19handleFormatChangedERK7QString(
    ChartDateTimeAxisX *self,
    const QString *format) {
  self->handleFormatChanged(*format);
}

//  a Python function taken by a CuteChartDateTimeAxisX, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartDateTimeAxisX(
    ChartDateTimeAxisX *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartDateTimeAxisX *>(self)->take(key, call);
}

//  QSizeF ChartDateTimeAxisX::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK18ChartDateTimeAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartDateTimeAxisX *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->ChartDateTimeAxisX::sizeHint(which, *constraint));
}

//  void ChartDateTimeAxisX::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18ChartDateTimeAxisX14updateGeometryEv(
    ChartDateTimeAxisX *self) {
  static_cast<OwnChartDateTimeAxisX *>(self)->OwnChartDateTimeAxisX::updateGeometry();
}

//  a QList<qreal> a ritual of ChartDateTimeAxisX gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ChartDateTimeAxisX__QList_qreal(QList<qreal> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_datetime_axis)
