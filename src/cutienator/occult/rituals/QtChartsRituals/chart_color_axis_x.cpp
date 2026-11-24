//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartcoloraxisx_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartcoloraxisx_p.h>
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

//  Only a class built on ChartColorAxisX may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnChartColorAxisX : ChartColorAxisX {
  using ChartColorAxisX::updateGeometry;
};

//  A ChartColorAxisX that Python can take functions over in. Every ChartColorAxisX
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteChartColorAxisXCall0)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteChartColorAxisXCall3)(const void *, int *);
typedef bool (*CuteChartColorAxisXCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall5)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall6)(const void *, const QPen *, int *);
typedef void (*CuteChartColorAxisXCall7)(const void *, const QPen *, int *);
typedef void (*CuteChartColorAxisXCall8)(const void *, const QBrush *, int *);
typedef void (*CuteChartColorAxisXCall9)(const void *, const QPen *, int *);
typedef void (*CuteChartColorAxisXCall10)(const void *, const QPen *, int *);
typedef void (*CuteChartColorAxisXCall11)(const void *, const QPen *, int *);
typedef void (*CuteChartColorAxisXCall12)(const void *, const QColor *, int *);
typedef void (*CuteChartColorAxisXCall13)(const void *, const QColor *, int *);
typedef void * (*CuteChartColorAxisXCall14)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteChartColorAxisXCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall16)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall17)(const void *, ChartPresenter *, int *);
typedef void (*CuteChartColorAxisXCall18)(const void *, ChartThemeManager *, int *);
typedef void (*CuteChartColorAxisXCall19)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartColorAxisXCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartColorAxisXCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartColorAxisXCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartColorAxisXCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartColorAxisXCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartColorAxisXCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartColorAxisXCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall30)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall31)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall32)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall33)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartColorAxisXCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteChartColorAxisXCall35)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall36)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartColorAxisXCall37)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall38)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall40)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall41)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall43)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall44)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall45)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall46)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall47)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall48)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall49)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall50)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall51)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall52)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall54)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartColorAxisXCall55)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartColorAxisXCall56)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartColorAxisXCall57)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartColorAxisXCall58)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteChartColorAxisX : public ChartColorAxisX {
public:
  using ChartColorAxisX::ChartColorAxisX;
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
  //  QSizeF ChartColorAxisX::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteChartColorAxisXCall0 call = reinterpret_cast<CuteChartColorAxisXCall0>(taken[0]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return ChartColorAxisX::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void ChartColorAxisX::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteChartColorAxisXCall1 call = reinterpret_cast<CuteChartColorAxisXCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    ChartColorAxisX::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CartesianChartAxis::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[2]) {
      int handled = 0;
      CuteChartColorAxisXCall2 call = reinterpret_cast<CuteChartColorAxisXCall2>(taken[2]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
    CartesianChartAxis::setGeometry(axis, grid);
  }

  //  QRectF CartesianChartAxis::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteChartColorAxisXCall3 call = reinterpret_cast<CuteChartColorAxisXCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return CartesianChartAxis::gridGeometry();
  }

  //  bool CartesianChartAxis::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[4]) {
      int handled = 0;
      CuteChartColorAxisXCall4 call = reinterpret_cast<CuteChartColorAxisXCall4>(taken[4]);
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
      CuteChartColorAxisXCall5 call = reinterpret_cast<CuteChartColorAxisXCall5>(taken[5]);
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
      CuteChartColorAxisXCall6 call = reinterpret_cast<CuteChartColorAxisXCall6>(taken[6]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CuteChartColorAxisXCall7 call = reinterpret_cast<CuteChartColorAxisXCall7>(taken[7]);
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
      CuteChartColorAxisXCall8 call = reinterpret_cast<CuteChartColorAxisXCall8>(taken[8]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesBrushChanged(brush);
  }

  //  void CartesianChartAxis::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[9]) {
      int handled = 0;
      CuteChartColorAxisXCall9 call = reinterpret_cast<CuteChartColorAxisXCall9>(taken[9]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[10]) {
      int handled = 0;
      CuteChartColorAxisXCall10 call = reinterpret_cast<CuteChartColorAxisXCall10>(taken[10]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CuteChartColorAxisXCall11 call = reinterpret_cast<CuteChartColorAxisXCall11>(taken[11]);
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
      CuteChartColorAxisXCall12 call = reinterpret_cast<CuteChartColorAxisXCall12>(taken[12]);
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
      CuteChartColorAxisXCall13 call = reinterpret_cast<CuteChartColorAxisXCall13>(taken[13]);
      call(this, &color, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorGridLineColorChanged(color);
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[14]) {
      int handled = 0;
      CuteChartColorAxisXCall14 call = reinterpret_cast<CuteChartColorAxisXCall14>(taken[14]);
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
      CuteChartColorAxisXCall15 call = reinterpret_cast<CuteChartColorAxisXCall15>(taken[15]);
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
      CuteChartColorAxisXCall16 call = reinterpret_cast<CuteChartColorAxisXCall16>(taken[16]);
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
      CuteChartColorAxisXCall17 call = reinterpret_cast<CuteChartColorAxisXCall17>(taken[17]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[18]) {
      int handled = 0;
      CuteChartColorAxisXCall18 call = reinterpret_cast<CuteChartColorAxisXCall18>(taken[18]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[19]) {
      int handled = 0;
      CuteChartColorAxisXCall19 call = reinterpret_cast<CuteChartColorAxisXCall19>(taken[19]);
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
      CuteChartColorAxisXCall20 call = reinterpret_cast<CuteChartColorAxisXCall20>(taken[20]);
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
      CuteChartColorAxisXCall21 call = reinterpret_cast<CuteChartColorAxisXCall21>(taken[21]);
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
      CuteChartColorAxisXCall22 call = reinterpret_cast<CuteChartColorAxisXCall22>(taken[22]);
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
      CuteChartColorAxisXCall23 call = reinterpret_cast<CuteChartColorAxisXCall23>(taken[23]);
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
      CuteChartColorAxisXCall24 call = reinterpret_cast<CuteChartColorAxisXCall24>(taken[24]);
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
      CuteChartColorAxisXCall25 call = reinterpret_cast<CuteChartColorAxisXCall25>(taken[25]);
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
      CuteChartColorAxisXCall26 call = reinterpret_cast<CuteChartColorAxisXCall26>(taken[26]);
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
      CuteChartColorAxisXCall27 call = reinterpret_cast<CuteChartColorAxisXCall27>(taken[27]);
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
      CuteChartColorAxisXCall28 call = reinterpret_cast<CuteChartColorAxisXCall28>(taken[28]);
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
      CuteChartColorAxisXCall29 call = reinterpret_cast<CuteChartColorAxisXCall29>(taken[29]);
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
      CuteChartColorAxisXCall30 call = reinterpret_cast<CuteChartColorAxisXCall30>(taken[30]);
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
      CuteChartColorAxisXCall31 call = reinterpret_cast<CuteChartColorAxisXCall31>(taken[31]);
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
      CuteChartColorAxisXCall32 call = reinterpret_cast<CuteChartColorAxisXCall32>(taken[32]);
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
      CuteChartColorAxisXCall33 call = reinterpret_cast<CuteChartColorAxisXCall33>(taken[33]);
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
      CuteChartColorAxisXCall34 call = reinterpret_cast<CuteChartColorAxisXCall34>(taken[34]);
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
      CuteChartColorAxisXCall35 call = reinterpret_cast<CuteChartColorAxisXCall35>(taken[35]);
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
      CuteChartColorAxisXCall36 call = reinterpret_cast<CuteChartColorAxisXCall36>(taken[36]);
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
      CuteChartColorAxisXCall37 call = reinterpret_cast<CuteChartColorAxisXCall37>(taken[37]);
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
      CuteChartColorAxisXCall38 call = reinterpret_cast<CuteChartColorAxisXCall38>(taken[38]);
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
      CuteChartColorAxisXCall39 call = reinterpret_cast<CuteChartColorAxisXCall39>(taken[39]);
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
      CuteChartColorAxisXCall40 call = reinterpret_cast<CuteChartColorAxisXCall40>(taken[40]);
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
      CuteChartColorAxisXCall41 call = reinterpret_cast<CuteChartColorAxisXCall41>(taken[41]);
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
      CuteChartColorAxisXCall42 call = reinterpret_cast<CuteChartColorAxisXCall42>(taken[42]);
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
      CuteChartColorAxisXCall43 call = reinterpret_cast<CuteChartColorAxisXCall43>(taken[43]);
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
      CuteChartColorAxisXCall44 call = reinterpret_cast<CuteChartColorAxisXCall44>(taken[44]);
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
      CuteChartColorAxisXCall45 call = reinterpret_cast<CuteChartColorAxisXCall45>(taken[45]);
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
      CuteChartColorAxisXCall46 call = reinterpret_cast<CuteChartColorAxisXCall46>(taken[46]);
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
      CuteChartColorAxisXCall47 call = reinterpret_cast<CuteChartColorAxisXCall47>(taken[47]);
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
      CuteChartColorAxisXCall48 call = reinterpret_cast<CuteChartColorAxisXCall48>(taken[48]);
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
      CuteChartColorAxisXCall49 call = reinterpret_cast<CuteChartColorAxisXCall49>(taken[49]);
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
      CuteChartColorAxisXCall50 call = reinterpret_cast<CuteChartColorAxisXCall50>(taken[50]);
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
      CuteChartColorAxisXCall51 call = reinterpret_cast<CuteChartColorAxisXCall51>(taken[51]);
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
      CuteChartColorAxisXCall52 call = reinterpret_cast<CuteChartColorAxisXCall52>(taken[52]);
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
      CuteChartColorAxisXCall53 call = reinterpret_cast<CuteChartColorAxisXCall53>(taken[53]);
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
      CuteChartColorAxisXCall54 call = reinterpret_cast<CuteChartColorAxisXCall54>(taken[54]);
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
      CuteChartColorAxisXCall55 call = reinterpret_cast<CuteChartColorAxisXCall55>(taken[55]);
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
      CuteChartColorAxisXCall56 call = reinterpret_cast<CuteChartColorAxisXCall56>(taken[56]);
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
      CuteChartColorAxisXCall57 call = reinterpret_cast<CuteChartColorAxisXCall57>(taken[57]);
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
      CuteChartColorAxisXCall58 call = reinterpret_cast<CuteChartColorAxisXCall58>(taken[58]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *ChartColorAxisX::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15ChartColorAxisX10metaObjectEv(
    const ChartColorAxisX *self) {
  return self->metaObject();
}

//  QString ChartColorAxisX::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15ChartColorAxisX2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartColorAxisX::tr(s, c, n));
}

//  ChartColorAxisX::ChartColorAxisX(QColorAxis *axis, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
ChartColorAxisX *ritual_ZN15ChartColorAxisXC1EP10QColorAxisP13QGraphicsItem(
    QColorAxis *axis,
    QGraphicsItem *item) {
  return new CuteChartColorAxisX(axis, item);
}

//  ChartColorAxisX::~ChartColorAxisX()
extern "C" Q_DECL_EXPORT
void ritual_ZN15ChartColorAxisXD1Ev(ChartColorAxisX *self) {
  delete self;
}

//  QSizeF ChartColorAxisX::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15ChartColorAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartColorAxisX *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void ChartColorAxisX::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15ChartColorAxisX14updateGeometryEv(ChartColorAxisX *self) {
  self->updateGeometry();
}

//  a Python function taken by a CuteChartColorAxisX, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartColorAxisX(
    ChartColorAxisX *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartColorAxisX *>(self)->take(key, call);
}

//  QSizeF ChartColorAxisX::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK15ChartColorAxisX8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartColorAxisX *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->ChartColorAxisX::sizeHint(which, *constraint));
}

//  void ChartColorAxisX::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15ChartColorAxisX14updateGeometryEv(
    ChartColorAxisX *self) {
  static_cast<OwnChartColorAxisX *>(self)->OwnChartColorAxisX::updateGeometry();
}
