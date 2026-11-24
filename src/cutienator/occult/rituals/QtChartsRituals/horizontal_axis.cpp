//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/horizontalaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/horizontalaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  Only a class built on HorizontalAxis may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnHorizontalAxis : HorizontalAxis {
  using HorizontalAxis::updateGeometry;
};

//  A HorizontalAxis that Python can take functions over in. Every HorizontalAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteHorizontalAxisCall0)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteHorizontalAxisCall3)(const void *, int *);
typedef bool (*CuteHorizontalAxisCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall5)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall6)(const void *, const QPen *, int *);
typedef void (*CuteHorizontalAxisCall7)(const void *, const QPen *, int *);
typedef void (*CuteHorizontalAxisCall8)(const void *, const QBrush *, int *);
typedef void (*CuteHorizontalAxisCall9)(const void *, const QPen *, int *);
typedef void (*CuteHorizontalAxisCall10)(const void *, const QPen *, int *);
typedef void (*CuteHorizontalAxisCall11)(const void *, const QPen *, int *);
typedef void (*CuteHorizontalAxisCall12)(const void *, const QColor *, int *);
typedef void (*CuteHorizontalAxisCall13)(const void *, const QColor *, int *);
typedef void * (*CuteHorizontalAxisCall14)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteHorizontalAxisCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall16)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall17)(const void *, ChartPresenter *, int *);
typedef void (*CuteHorizontalAxisCall18)(const void *, ChartThemeManager *, int *);
typedef void (*CuteHorizontalAxisCall19)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteHorizontalAxisCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteHorizontalAxisCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteHorizontalAxisCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteHorizontalAxisCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteHorizontalAxisCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteHorizontalAxisCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteHorizontalAxisCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall30)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall31)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall32)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall33)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteHorizontalAxisCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteHorizontalAxisCall35)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall36)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteHorizontalAxisCall37)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall38)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall40)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall41)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall43)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall44)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall45)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall46)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall47)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall48)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall49)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall50)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall51)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall52)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall54)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteHorizontalAxisCall55)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteHorizontalAxisCall56)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteHorizontalAxisCall57)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteHorizontalAxisCall58)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteHorizontalAxis : public HorizontalAxis {
public:
  using HorizontalAxis::HorizontalAxis;
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
  //  QSizeF HorizontalAxis::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteHorizontalAxisCall0 call = reinterpret_cast<CuteHorizontalAxisCall0>(taken[0]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return HorizontalAxis::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void HorizontalAxis::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteHorizontalAxisCall1 call = reinterpret_cast<CuteHorizontalAxisCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    HorizontalAxis::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CartesianChartAxis::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[2]) {
      int handled = 0;
      CuteHorizontalAxisCall2 call = reinterpret_cast<CuteHorizontalAxisCall2>(taken[2]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
    CartesianChartAxis::setGeometry(axis, grid);
  }

  //  QRectF CartesianChartAxis::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteHorizontalAxisCall3 call = reinterpret_cast<CuteHorizontalAxisCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return CartesianChartAxis::gridGeometry();
  }

  //  bool CartesianChartAxis::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[4]) {
      int handled = 0;
      CuteHorizontalAxisCall4 call = reinterpret_cast<CuteHorizontalAxisCall4>(taken[4]);
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
      CuteHorizontalAxisCall5 call = reinterpret_cast<CuteHorizontalAxisCall5>(taken[5]);
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
      CuteHorizontalAxisCall6 call = reinterpret_cast<CuteHorizontalAxisCall6>(taken[6]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CuteHorizontalAxisCall7 call = reinterpret_cast<CuteHorizontalAxisCall7>(taken[7]);
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
      CuteHorizontalAxisCall8 call = reinterpret_cast<CuteHorizontalAxisCall8>(taken[8]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesBrushChanged(brush);
  }

  //  void CartesianChartAxis::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[9]) {
      int handled = 0;
      CuteHorizontalAxisCall9 call = reinterpret_cast<CuteHorizontalAxisCall9>(taken[9]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[10]) {
      int handled = 0;
      CuteHorizontalAxisCall10 call = reinterpret_cast<CuteHorizontalAxisCall10>(taken[10]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CuteHorizontalAxisCall11 call = reinterpret_cast<CuteHorizontalAxisCall11>(taken[11]);
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
      CuteHorizontalAxisCall12 call = reinterpret_cast<CuteHorizontalAxisCall12>(taken[12]);
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
      CuteHorizontalAxisCall13 call = reinterpret_cast<CuteHorizontalAxisCall13>(taken[13]);
      call(this, &color, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorGridLineColorChanged(color);
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[14]) {
      int handled = 0;
      CuteHorizontalAxisCall14 call = reinterpret_cast<CuteHorizontalAxisCall14>(taken[14]);
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
      CuteHorizontalAxisCall15 call = reinterpret_cast<CuteHorizontalAxisCall15>(taken[15]);
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
      CuteHorizontalAxisCall16 call = reinterpret_cast<CuteHorizontalAxisCall16>(taken[16]);
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
      CuteHorizontalAxisCall17 call = reinterpret_cast<CuteHorizontalAxisCall17>(taken[17]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[18]) {
      int handled = 0;
      CuteHorizontalAxisCall18 call = reinterpret_cast<CuteHorizontalAxisCall18>(taken[18]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[19]) {
      int handled = 0;
      CuteHorizontalAxisCall19 call = reinterpret_cast<CuteHorizontalAxisCall19>(taken[19]);
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
      CuteHorizontalAxisCall20 call = reinterpret_cast<CuteHorizontalAxisCall20>(taken[20]);
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
      CuteHorizontalAxisCall21 call = reinterpret_cast<CuteHorizontalAxisCall21>(taken[21]);
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
      CuteHorizontalAxisCall22 call = reinterpret_cast<CuteHorizontalAxisCall22>(taken[22]);
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
      CuteHorizontalAxisCall23 call = reinterpret_cast<CuteHorizontalAxisCall23>(taken[23]);
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
      CuteHorizontalAxisCall24 call = reinterpret_cast<CuteHorizontalAxisCall24>(taken[24]);
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
      CuteHorizontalAxisCall25 call = reinterpret_cast<CuteHorizontalAxisCall25>(taken[25]);
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
      CuteHorizontalAxisCall26 call = reinterpret_cast<CuteHorizontalAxisCall26>(taken[26]);
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
      CuteHorizontalAxisCall27 call = reinterpret_cast<CuteHorizontalAxisCall27>(taken[27]);
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
      CuteHorizontalAxisCall28 call = reinterpret_cast<CuteHorizontalAxisCall28>(taken[28]);
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
      CuteHorizontalAxisCall29 call = reinterpret_cast<CuteHorizontalAxisCall29>(taken[29]);
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
      CuteHorizontalAxisCall30 call = reinterpret_cast<CuteHorizontalAxisCall30>(taken[30]);
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
      CuteHorizontalAxisCall31 call = reinterpret_cast<CuteHorizontalAxisCall31>(taken[31]);
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
      CuteHorizontalAxisCall32 call = reinterpret_cast<CuteHorizontalAxisCall32>(taken[32]);
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
      CuteHorizontalAxisCall33 call = reinterpret_cast<CuteHorizontalAxisCall33>(taken[33]);
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
      CuteHorizontalAxisCall34 call = reinterpret_cast<CuteHorizontalAxisCall34>(taken[34]);
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
      CuteHorizontalAxisCall35 call = reinterpret_cast<CuteHorizontalAxisCall35>(taken[35]);
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
      CuteHorizontalAxisCall36 call = reinterpret_cast<CuteHorizontalAxisCall36>(taken[36]);
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
      CuteHorizontalAxisCall37 call = reinterpret_cast<CuteHorizontalAxisCall37>(taken[37]);
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
      CuteHorizontalAxisCall38 call = reinterpret_cast<CuteHorizontalAxisCall38>(taken[38]);
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
      CuteHorizontalAxisCall39 call = reinterpret_cast<CuteHorizontalAxisCall39>(taken[39]);
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
      CuteHorizontalAxisCall40 call = reinterpret_cast<CuteHorizontalAxisCall40>(taken[40]);
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
      CuteHorizontalAxisCall41 call = reinterpret_cast<CuteHorizontalAxisCall41>(taken[41]);
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
      CuteHorizontalAxisCall42 call = reinterpret_cast<CuteHorizontalAxisCall42>(taken[42]);
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
      CuteHorizontalAxisCall43 call = reinterpret_cast<CuteHorizontalAxisCall43>(taken[43]);
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
      CuteHorizontalAxisCall44 call = reinterpret_cast<CuteHorizontalAxisCall44>(taken[44]);
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
      CuteHorizontalAxisCall45 call = reinterpret_cast<CuteHorizontalAxisCall45>(taken[45]);
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
      CuteHorizontalAxisCall46 call = reinterpret_cast<CuteHorizontalAxisCall46>(taken[46]);
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
      CuteHorizontalAxisCall47 call = reinterpret_cast<CuteHorizontalAxisCall47>(taken[47]);
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
      CuteHorizontalAxisCall48 call = reinterpret_cast<CuteHorizontalAxisCall48>(taken[48]);
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
      CuteHorizontalAxisCall49 call = reinterpret_cast<CuteHorizontalAxisCall49>(taken[49]);
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
      CuteHorizontalAxisCall50 call = reinterpret_cast<CuteHorizontalAxisCall50>(taken[50]);
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
      CuteHorizontalAxisCall51 call = reinterpret_cast<CuteHorizontalAxisCall51>(taken[51]);
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
      CuteHorizontalAxisCall52 call = reinterpret_cast<CuteHorizontalAxisCall52>(taken[52]);
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
      CuteHorizontalAxisCall53 call = reinterpret_cast<CuteHorizontalAxisCall53>(taken[53]);
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
      CuteHorizontalAxisCall54 call = reinterpret_cast<CuteHorizontalAxisCall54>(taken[54]);
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
      CuteHorizontalAxisCall55 call = reinterpret_cast<CuteHorizontalAxisCall55>(taken[55]);
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
      CuteHorizontalAxisCall56 call = reinterpret_cast<CuteHorizontalAxisCall56>(taken[56]);
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
      CuteHorizontalAxisCall57 call = reinterpret_cast<CuteHorizontalAxisCall57>(taken[57]);
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
      CuteHorizontalAxisCall58 call = reinterpret_cast<CuteHorizontalAxisCall58>(taken[58]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  HorizontalAxis::~HorizontalAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN14HorizontalAxisD1Ev(HorizontalAxis *self) {
  delete self;
}

//  QSizeF HorizontalAxis::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK14HorizontalAxis8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const HorizontalAxis *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void HorizontalAxis::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14HorizontalAxis14updateGeometryEv(HorizontalAxis *self) {
  self->updateGeometry();
}

//  void HorizontalAxis::updateMinorTickGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14HorizontalAxis23updateMinorTickGeometryEv(
    HorizontalAxis *self) {
  self->updateMinorTickGeometry();
}

//  a Python function taken by a CuteHorizontalAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_HorizontalAxis(
    HorizontalAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteHorizontalAxis *>(self)->take(key, call);
}

//  QSizeF HorizontalAxis::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK14HorizontalAxis8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const HorizontalAxis *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->HorizontalAxis::sizeHint(which, *constraint));
}

//  void HorizontalAxis::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14HorizontalAxis14updateGeometryEv(HorizontalAxis *self) {
  static_cast<OwnHorizontalAxis *>(self)->OwnHorizontalAxis::updateGeometry();
}
