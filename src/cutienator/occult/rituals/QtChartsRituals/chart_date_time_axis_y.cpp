//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartdatetimeaxisy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_datetime_axis)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartdatetimeaxisy_p.h>
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

//  Only a class built on ChartDateTimeAxisY may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnChartDateTimeAxisY : ChartDateTimeAxisY {
  using ChartDateTimeAxisY::updateGeometry;
};

//  A ChartDateTimeAxisY that Python can take functions over in. Every ChartDateTimeAxisY
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteChartDateTimeAxisYCall0)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteChartDateTimeAxisYCall3)(const void *, int *);
typedef bool (*CuteChartDateTimeAxisYCall4)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall5)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall6)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisYCall7)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisYCall8)(const void *, const QBrush *, int *);
typedef void (*CuteChartDateTimeAxisYCall9)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisYCall10)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisYCall11)(const void *, const QPen *, int *);
typedef void (*CuteChartDateTimeAxisYCall12)(const void *, const QColor *, int *);
typedef void (*CuteChartDateTimeAxisYCall13)(const void *, const QColor *, int *);
typedef void * (*CuteChartDateTimeAxisYCall14)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteChartDateTimeAxisYCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall16)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall17)(const void *, ChartPresenter *, int *);
typedef void (*CuteChartDateTimeAxisYCall18)(const void *, ChartThemeManager *, int *);
typedef void (*CuteChartDateTimeAxisYCall19)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartDateTimeAxisYCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisYCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisYCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisYCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisYCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDateTimeAxisYCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall27)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartDateTimeAxisYCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall30)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall31)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall32)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall33)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartDateTimeAxisYCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteChartDateTimeAxisYCall35)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall36)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartDateTimeAxisYCall37)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall38)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall40)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall41)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall43)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall44)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall45)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall46)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall47)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall48)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall49)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall50)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall51)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall52)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall54)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartDateTimeAxisYCall55)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisYCall56)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisYCall57)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartDateTimeAxisYCall58)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteChartDateTimeAxisY : public ChartDateTimeAxisY {
public:
  using ChartDateTimeAxisY::ChartDateTimeAxisY;
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
  //  QSizeF ChartDateTimeAxisY::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall0 call = reinterpret_cast<CuteChartDateTimeAxisYCall0>(taken[0]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return ChartDateTimeAxisY::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void ChartDateTimeAxisY::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall1 call = reinterpret_cast<CuteChartDateTimeAxisYCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    ChartDateTimeAxisY::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

  //  void CartesianChartAxis::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[2]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall2 call = reinterpret_cast<CuteChartDateTimeAxisYCall2>(taken[2]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
    CartesianChartAxis::setGeometry(axis, grid);
  }

  //  QRectF CartesianChartAxis::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall3 call = reinterpret_cast<CuteChartDateTimeAxisYCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return CartesianChartAxis::gridGeometry();
  }

  //  bool CartesianChartAxis::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[4]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall4 call = reinterpret_cast<CuteChartDateTimeAxisYCall4>(taken[4]);
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
      CuteChartDateTimeAxisYCall5 call = reinterpret_cast<CuteChartDateTimeAxisYCall5>(taken[5]);
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
      CuteChartDateTimeAxisYCall6 call = reinterpret_cast<CuteChartDateTimeAxisYCall6>(taken[6]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall7 call = reinterpret_cast<CuteChartDateTimeAxisYCall7>(taken[7]);
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
      CuteChartDateTimeAxisYCall8 call = reinterpret_cast<CuteChartDateTimeAxisYCall8>(taken[8]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesBrushChanged(brush);
  }

  //  void CartesianChartAxis::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[9]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall9 call = reinterpret_cast<CuteChartDateTimeAxisYCall9>(taken[9]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleShadesPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[10]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall10 call = reinterpret_cast<CuteChartDateTimeAxisYCall10>(taken[10]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorArrowPenChanged(pen);
  }

  //  void CartesianChartAxis::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall11 call = reinterpret_cast<CuteChartDateTimeAxisYCall11>(taken[11]);
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
      CuteChartDateTimeAxisYCall12 call = reinterpret_cast<CuteChartDateTimeAxisYCall12>(taken[12]);
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
      CuteChartDateTimeAxisYCall13 call = reinterpret_cast<CuteChartDateTimeAxisYCall13>(taken[13]);
      call(this, &color, &handled);
      if (handled) return;
    }
    CartesianChartAxis::handleMinorGridLineColorChanged(color);
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[14]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall14 call = reinterpret_cast<CuteChartDateTimeAxisYCall14>(taken[14]);
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
      CuteChartDateTimeAxisYCall15 call = reinterpret_cast<CuteChartDateTimeAxisYCall15>(taken[15]);
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
      CuteChartDateTimeAxisYCall16 call = reinterpret_cast<CuteChartDateTimeAxisYCall16>(taken[16]);
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
      CuteChartDateTimeAxisYCall17 call = reinterpret_cast<CuteChartDateTimeAxisYCall17>(taken[17]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[18]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall18 call = reinterpret_cast<CuteChartDateTimeAxisYCall18>(taken[18]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[19]) {
      int handled = 0;
      CuteChartDateTimeAxisYCall19 call = reinterpret_cast<CuteChartDateTimeAxisYCall19>(taken[19]);
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
      CuteChartDateTimeAxisYCall20 call = reinterpret_cast<CuteChartDateTimeAxisYCall20>(taken[20]);
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
      CuteChartDateTimeAxisYCall21 call = reinterpret_cast<CuteChartDateTimeAxisYCall21>(taken[21]);
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
      CuteChartDateTimeAxisYCall22 call = reinterpret_cast<CuteChartDateTimeAxisYCall22>(taken[22]);
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
      CuteChartDateTimeAxisYCall23 call = reinterpret_cast<CuteChartDateTimeAxisYCall23>(taken[23]);
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
      CuteChartDateTimeAxisYCall24 call = reinterpret_cast<CuteChartDateTimeAxisYCall24>(taken[24]);
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
      CuteChartDateTimeAxisYCall25 call = reinterpret_cast<CuteChartDateTimeAxisYCall25>(taken[25]);
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
      CuteChartDateTimeAxisYCall26 call = reinterpret_cast<CuteChartDateTimeAxisYCall26>(taken[26]);
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
      CuteChartDateTimeAxisYCall27 call = reinterpret_cast<CuteChartDateTimeAxisYCall27>(taken[27]);
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
      CuteChartDateTimeAxisYCall28 call = reinterpret_cast<CuteChartDateTimeAxisYCall28>(taken[28]);
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
      CuteChartDateTimeAxisYCall29 call = reinterpret_cast<CuteChartDateTimeAxisYCall29>(taken[29]);
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
      CuteChartDateTimeAxisYCall30 call = reinterpret_cast<CuteChartDateTimeAxisYCall30>(taken[30]);
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
      CuteChartDateTimeAxisYCall31 call = reinterpret_cast<CuteChartDateTimeAxisYCall31>(taken[31]);
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
      CuteChartDateTimeAxisYCall32 call = reinterpret_cast<CuteChartDateTimeAxisYCall32>(taken[32]);
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
      CuteChartDateTimeAxisYCall33 call = reinterpret_cast<CuteChartDateTimeAxisYCall33>(taken[33]);
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
      CuteChartDateTimeAxisYCall34 call = reinterpret_cast<CuteChartDateTimeAxisYCall34>(taken[34]);
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
      CuteChartDateTimeAxisYCall35 call = reinterpret_cast<CuteChartDateTimeAxisYCall35>(taken[35]);
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
      CuteChartDateTimeAxisYCall36 call = reinterpret_cast<CuteChartDateTimeAxisYCall36>(taken[36]);
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
      CuteChartDateTimeAxisYCall37 call = reinterpret_cast<CuteChartDateTimeAxisYCall37>(taken[37]);
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
      CuteChartDateTimeAxisYCall38 call = reinterpret_cast<CuteChartDateTimeAxisYCall38>(taken[38]);
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
      CuteChartDateTimeAxisYCall39 call = reinterpret_cast<CuteChartDateTimeAxisYCall39>(taken[39]);
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
      CuteChartDateTimeAxisYCall40 call = reinterpret_cast<CuteChartDateTimeAxisYCall40>(taken[40]);
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
      CuteChartDateTimeAxisYCall41 call = reinterpret_cast<CuteChartDateTimeAxisYCall41>(taken[41]);
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
      CuteChartDateTimeAxisYCall42 call = reinterpret_cast<CuteChartDateTimeAxisYCall42>(taken[42]);
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
      CuteChartDateTimeAxisYCall43 call = reinterpret_cast<CuteChartDateTimeAxisYCall43>(taken[43]);
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
      CuteChartDateTimeAxisYCall44 call = reinterpret_cast<CuteChartDateTimeAxisYCall44>(taken[44]);
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
      CuteChartDateTimeAxisYCall45 call = reinterpret_cast<CuteChartDateTimeAxisYCall45>(taken[45]);
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
      CuteChartDateTimeAxisYCall46 call = reinterpret_cast<CuteChartDateTimeAxisYCall46>(taken[46]);
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
      CuteChartDateTimeAxisYCall47 call = reinterpret_cast<CuteChartDateTimeAxisYCall47>(taken[47]);
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
      CuteChartDateTimeAxisYCall48 call = reinterpret_cast<CuteChartDateTimeAxisYCall48>(taken[48]);
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
      CuteChartDateTimeAxisYCall49 call = reinterpret_cast<CuteChartDateTimeAxisYCall49>(taken[49]);
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
      CuteChartDateTimeAxisYCall50 call = reinterpret_cast<CuteChartDateTimeAxisYCall50>(taken[50]);
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
      CuteChartDateTimeAxisYCall51 call = reinterpret_cast<CuteChartDateTimeAxisYCall51>(taken[51]);
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
      CuteChartDateTimeAxisYCall52 call = reinterpret_cast<CuteChartDateTimeAxisYCall52>(taken[52]);
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
      CuteChartDateTimeAxisYCall53 call = reinterpret_cast<CuteChartDateTimeAxisYCall53>(taken[53]);
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
      CuteChartDateTimeAxisYCall54 call = reinterpret_cast<CuteChartDateTimeAxisYCall54>(taken[54]);
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
      CuteChartDateTimeAxisYCall55 call = reinterpret_cast<CuteChartDateTimeAxisYCall55>(taken[55]);
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
      CuteChartDateTimeAxisYCall56 call = reinterpret_cast<CuteChartDateTimeAxisYCall56>(taken[56]);
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
      CuteChartDateTimeAxisYCall57 call = reinterpret_cast<CuteChartDateTimeAxisYCall57>(taken[57]);
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
      CuteChartDateTimeAxisYCall58 call = reinterpret_cast<CuteChartDateTimeAxisYCall58>(taken[58]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *ChartDateTimeAxisY::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18ChartDateTimeAxisY10metaObjectEv(
    const ChartDateTimeAxisY *self) {
  return self->metaObject();
}

//  void *ChartDateTimeAxisY::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18ChartDateTimeAxisY11qt_metacastEPKc(
    ChartDateTimeAxisY *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ChartDateTimeAxisY::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18ChartDateTimeAxisY11qt_metacallEN11QMetaObject4CallEiPPv(
    ChartDateTimeAxisY *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ChartDateTimeAxisY::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18ChartDateTimeAxisY2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartDateTimeAxisY::tr(s, c, n));
}

//  ChartDateTimeAxisY::ChartDateTimeAxisY(QDateTimeAxis *axis, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
ChartDateTimeAxisY *ritual_ZN18ChartDateTimeAxisYC1EP13QDateTimeAxisP13QGraphicsItem(
    QDateTimeAxis *axis,
    QGraphicsItem *item) {
  return new CuteChartDateTimeAxisY(axis, item);
}

//  ChartDateTimeAxisY::~ChartDateTimeAxisY()
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisYD1Ev(ChartDateTimeAxisY *self) {
  delete self;
}

//  QSizeF ChartDateTimeAxisY::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18ChartDateTimeAxisY8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartDateTimeAxisY *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  QList<qreal> ChartDateTimeAxisY::calculateLayout() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK18ChartDateTimeAxisY15calculateLayoutEv(
    const ChartDateTimeAxisY *self) {
  return new QList<qreal>(self->calculateLayout());
}

//  void ChartDateTimeAxisY::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisY14updateGeometryEv(
    ChartDateTimeAxisY *self) {
  self->updateGeometry();
}

//  void ChartDateTimeAxisY::handleTickCountChanged(int tick)
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisY22handleTickCountChangedEi(
    ChartDateTimeAxisY *self,
    int tick) {
  self->handleTickCountChanged(tick);
}

//  void ChartDateTimeAxisY::handleFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18ChartDateTimeAxisY19handleFormatChangedERK7QString(
    ChartDateTimeAxisY *self,
    const QString *format) {
  self->handleFormatChanged(*format);
}

//  a Python function taken by a CuteChartDateTimeAxisY, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartDateTimeAxisY(
    ChartDateTimeAxisY *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartDateTimeAxisY *>(self)->take(key, call);
}

//  QSizeF ChartDateTimeAxisY::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK18ChartDateTimeAxisY8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const ChartDateTimeAxisY *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->ChartDateTimeAxisY::sizeHint(which, *constraint));
}

//  void ChartDateTimeAxisY::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18ChartDateTimeAxisY14updateGeometryEv(
    ChartDateTimeAxisY *self) {
  static_cast<OwnChartDateTimeAxisY *>(self)->OwnChartDateTimeAxisY::updateGeometry();
}

//  a QList<qreal> a ritual of ChartDateTimeAxisY gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ChartDateTimeAxisY__QList_qreal(QList<qreal> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_datetime_axis)
