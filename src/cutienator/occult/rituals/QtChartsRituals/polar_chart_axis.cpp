//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/polarchartaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/polarchartaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A PolarChartAxis that Python can take functions over in. Every PolarChartAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CutePolarChartAxisCall0)(const void *, const QRectF *, const QRectF *, int *);
typedef qreal (*CutePolarChartAxisCall1)(const void *, const QSizeF *, int *);
typedef const QRectF * (*CutePolarChartAxisCall2)(const void *, int *);
typedef bool (*CutePolarChartAxisCall3)(const void *, int *);
typedef void (*CutePolarChartAxisCall4)(const void *, int, int *);
typedef void (*CutePolarChartAxisCall5)(const void *, int *);
typedef void (*CutePolarChartAxisCall6)(const void *, const QBrush *, int *);
typedef void (*CutePolarChartAxisCall7)(const void *, const QPen *, int *);
typedef void * (*CutePolarChartAxisCall8)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CutePolarChartAxisCall9)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall10)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall11)(const void *, const QPen *, int *);
typedef void (*CutePolarChartAxisCall12)(const void *, const QPen *, int *);
typedef void (*CutePolarChartAxisCall13)(const void *, const QPen *, int *);
typedef void (*CutePolarChartAxisCall14)(const void *, const QPen *, int *);
typedef void (*CutePolarChartAxisCall15)(const void *, const QColor *, int *);
typedef void (*CutePolarChartAxisCall16)(const void *, const QColor *, int *);
typedef void (*CutePolarChartAxisCall17)(const void *, ChartPresenter *, int *);
typedef void (*CutePolarChartAxisCall18)(const void *, ChartThemeManager *, int *);
typedef void (*CutePolarChartAxisCall19)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall20)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePolarChartAxisCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarChartAxisCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarChartAxisCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarChartAxisCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarChartAxisCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePolarChartAxisCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall27)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall28)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CutePolarChartAxisCall30)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall31)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePolarChartAxisCall32)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall33)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall34)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall35)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall36)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CutePolarChartAxisCall37)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CutePolarChartAxisCall38)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall39)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartAxisCall40)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall41)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall43)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall44)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall45)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall46)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall47)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall48)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall49)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall50)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall51)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall52)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall54)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall55)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall56)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall57)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartAxisCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePolarChartAxisCall59)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePolarChartAxisCall60)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CutePolarChartAxisCall61)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CutePolarChartAxis : public PolarChartAxis {
public:
  using PolarChartAxis::PolarChartAxis;
  void *taken[62] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16ChartAxisElement11setGeometryERK6QRectFS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14PolarChartAxis19preferredAxisRadiusERK6QSizeF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16ChartAxisElement12gridGeometryEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16ChartAxisElement9emptyAxisEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14PolarChartAxis11createItemsEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14PolarChartAxis20updateMinorTickItemsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement20handleGridPenChangedERK4QPen")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement26handleMinorArrowPenChangedERK4QPen")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement25handleMinorGridPenChangedERK4QPen")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QColor")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor")) {
      taken[16] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

  //  void PolarChartAxis::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[0]) {
      int handled = 0;
      CutePolarChartAxisCall0 call = reinterpret_cast<CutePolarChartAxisCall0>(taken[0]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
    PolarChartAxis::setGeometry(axis, grid);
  }

  //  qreal PolarChartAxis::preferredAxisRadius(const QSizeF &maxSize)
  qreal preferredAxisRadius(const QSizeF &maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CutePolarChartAxisCall1 call = reinterpret_cast<CutePolarChartAxisCall1>(taken[1]);
      qreal given = call(this, &maxSize, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF PolarChartAxis::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[2]) {
      int handled = 0;
      CutePolarChartAxisCall2 call = reinterpret_cast<CutePolarChartAxisCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return PolarChartAxis::gridGeometry();
  }

  //  bool PolarChartAxis::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[3]) {
      int handled = 0;
      CutePolarChartAxisCall3 call = reinterpret_cast<CutePolarChartAxisCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return PolarChartAxis::emptyAxis();
  }

  //  void PolarChartAxis::createItems(int count)
  void createItems(int count) override {
    if (taken[4]) {
      int handled = 0;
      CutePolarChartAxisCall4 call = reinterpret_cast<CutePolarChartAxisCall4>(taken[4]);
      call(this, count, &handled);
      if (handled) return;
    }
  }

  //  void PolarChartAxis::updateMinorTickItems()
  void updateMinorTickItems() override {
    if (taken[5]) {
      int handled = 0;
      CutePolarChartAxisCall5 call = reinterpret_cast<CutePolarChartAxisCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void PolarChartAxis::handleShadesBrushChanged(const QBrush &brush)
  void handleShadesBrushChanged(const QBrush &brush) override {
    if (taken[6]) {
      int handled = 0;
      CutePolarChartAxisCall6 call = reinterpret_cast<CutePolarChartAxisCall6>(taken[6]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    PolarChartAxis::handleShadesBrushChanged(brush);
  }

  //  void PolarChartAxis::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CutePolarChartAxisCall7 call = reinterpret_cast<CutePolarChartAxisCall7>(taken[7]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    PolarChartAxis::handleShadesPenChanged(pen);
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[8]) {
      int handled = 0;
      CutePolarChartAxisCall8 call = reinterpret_cast<CutePolarChartAxisCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<AxisAnimation *>(given);
    }
    return ChartAxisElement::animation();
  }

#if QT_CONFIG(graphicsview)
  //  QRectF ChartAxisElement::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CutePolarChartAxisCall9 call = reinterpret_cast<CutePolarChartAxisCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CutePolarChartAxisCall10 call = reinterpret_cast<CutePolarChartAxisCall10>(taken[10]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    ChartAxisElement::paint(a0, a1, a2);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void ChartAxisElement::handleArrowPenChanged(const QPen &pen)
  void handleArrowPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CutePolarChartAxisCall11 call = reinterpret_cast<CutePolarChartAxisCall11>(taken[11]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[12]) {
      int handled = 0;
      CutePolarChartAxisCall12 call = reinterpret_cast<CutePolarChartAxisCall12>(taken[12]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[13]) {
      int handled = 0;
      CutePolarChartAxisCall13 call = reinterpret_cast<CutePolarChartAxisCall13>(taken[13]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[14]) {
      int handled = 0;
      CutePolarChartAxisCall14 call = reinterpret_cast<CutePolarChartAxisCall14>(taken[14]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorGridLineColorChanged(const QColor
  //      &color)
  void handleMinorGridLineColorChanged(const QColor &color) override {
    if (taken[15]) {
      int handled = 0;
      CutePolarChartAxisCall15 call = reinterpret_cast<CutePolarChartAxisCall15>(taken[15]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleGridLineColorChanged(const QColor
  //      &color)
  void handleGridLineColorChanged(const QColor &color) override {
    if (taken[16]) {
      int handled = 0;
      CutePolarChartAxisCall16 call = reinterpret_cast<CutePolarChartAxisCall16>(taken[16]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[17]) {
      int handled = 0;
      CutePolarChartAxisCall17 call = reinterpret_cast<CutePolarChartAxisCall17>(taken[17]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[18]) {
      int handled = 0;
      CutePolarChartAxisCall18 call = reinterpret_cast<CutePolarChartAxisCall18>(taken[18]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[19]) {
      int handled = 0;
      CutePolarChartAxisCall19 call = reinterpret_cast<CutePolarChartAxisCall19>(taken[19]);
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
      CutePolarChartAxisCall20 call = reinterpret_cast<CutePolarChartAxisCall20>(taken[20]);
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
      CutePolarChartAxisCall21 call = reinterpret_cast<CutePolarChartAxisCall21>(taken[21]);
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
      CutePolarChartAxisCall22 call = reinterpret_cast<CutePolarChartAxisCall22>(taken[22]);
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
      CutePolarChartAxisCall23 call = reinterpret_cast<CutePolarChartAxisCall23>(taken[23]);
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
      CutePolarChartAxisCall24 call = reinterpret_cast<CutePolarChartAxisCall24>(taken[24]);
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
      CutePolarChartAxisCall25 call = reinterpret_cast<CutePolarChartAxisCall25>(taken[25]);
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
      CutePolarChartAxisCall26 call = reinterpret_cast<CutePolarChartAxisCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[27]) {
      int handled = 0;
      CutePolarChartAxisCall27 call = reinterpret_cast<CutePolarChartAxisCall27>(taken[27]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutItem::updateGeometry()
  void updateGeometry() override {
    if (taken[28]) {
      int handled = 0;
      CutePolarChartAxisCall28 call = reinterpret_cast<CutePolarChartAxisCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[29]) {
      int handled = 0;
      CutePolarChartAxisCall29 call = reinterpret_cast<CutePolarChartAxisCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[30]) {
      int handled = 0;
      CutePolarChartAxisCall30 call = reinterpret_cast<CutePolarChartAxisCall30>(taken[30]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[31]) {
      int handled = 0;
      CutePolarChartAxisCall31 call = reinterpret_cast<CutePolarChartAxisCall31>(taken[31]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::shape() const
  QPainterPath shape() const override {
    if (taken[32]) {
      int handled = 0;
      CutePolarChartAxisCall32 call = reinterpret_cast<CutePolarChartAxisCall32>(taken[32]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[33]) {
      int handled = 0;
      CutePolarChartAxisCall33 call = reinterpret_cast<CutePolarChartAxisCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CutePolarChartAxisCall34 call = reinterpret_cast<CutePolarChartAxisCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CutePolarChartAxisCall35 call = reinterpret_cast<CutePolarChartAxisCall35>(taken[35]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[36]) {
      int handled = 0;
      CutePolarChartAxisCall36 call = reinterpret_cast<CutePolarChartAxisCall36>(taken[36]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[37]) {
      int handled = 0;
      CutePolarChartAxisCall37 call = reinterpret_cast<CutePolarChartAxisCall37>(taken[37]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsItem::type() const
  int type() const override {
    if (taken[38]) {
      int handled = 0;
      CutePolarChartAxisCall38 call = reinterpret_cast<CutePolarChartAxisCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CutePolarChartAxisCall39 call = reinterpret_cast<CutePolarChartAxisCall39>(taken[39]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CutePolarChartAxisCall40 call = reinterpret_cast<CutePolarChartAxisCall40>(taken[40]);
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
    if (taken[41]) {
      int handled = 0;
      CutePolarChartAxisCall41 call = reinterpret_cast<CutePolarChartAxisCall41>(taken[41]);
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
    if (taken[42]) {
      int handled = 0;
      CutePolarChartAxisCall42 call = reinterpret_cast<CutePolarChartAxisCall42>(taken[42]);
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
    if (taken[43]) {
      int handled = 0;
      CutePolarChartAxisCall43 call = reinterpret_cast<CutePolarChartAxisCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CutePolarChartAxisCall44 call = reinterpret_cast<CutePolarChartAxisCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CutePolarChartAxisCall45 call = reinterpret_cast<CutePolarChartAxisCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CutePolarChartAxisCall46 call = reinterpret_cast<CutePolarChartAxisCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CutePolarChartAxisCall47 call = reinterpret_cast<CutePolarChartAxisCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CutePolarChartAxisCall48 call = reinterpret_cast<CutePolarChartAxisCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CutePolarChartAxisCall49 call = reinterpret_cast<CutePolarChartAxisCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CutePolarChartAxisCall50 call = reinterpret_cast<CutePolarChartAxisCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CutePolarChartAxisCall51 call = reinterpret_cast<CutePolarChartAxisCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CutePolarChartAxisCall52 call = reinterpret_cast<CutePolarChartAxisCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CutePolarChartAxisCall53 call = reinterpret_cast<CutePolarChartAxisCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CutePolarChartAxisCall54 call = reinterpret_cast<CutePolarChartAxisCall54>(taken[54]);
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
    if (taken[55]) {
      int handled = 0;
      CutePolarChartAxisCall55 call = reinterpret_cast<CutePolarChartAxisCall55>(taken[55]);
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
    if (taken[56]) {
      int handled = 0;
      CutePolarChartAxisCall56 call = reinterpret_cast<CutePolarChartAxisCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CutePolarChartAxisCall57 call = reinterpret_cast<CutePolarChartAxisCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CutePolarChartAxisCall58 call = reinterpret_cast<CutePolarChartAxisCall58>(taken[58]);
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
    if (taken[59]) {
      int handled = 0;
      CutePolarChartAxisCall59 call = reinterpret_cast<CutePolarChartAxisCall59>(taken[59]);
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
    if (taken[60]) {
      int handled = 0;
      CutePolarChartAxisCall60 call = reinterpret_cast<CutePolarChartAxisCall60>(taken[60]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[61]) {
      int handled = 0;
      CutePolarChartAxisCall61 call = reinterpret_cast<CutePolarChartAxisCall61>(taken[61]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *PolarChartAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14PolarChartAxis10metaObjectEv(
    const PolarChartAxis *self) {
  return self->metaObject();
}

//  QString PolarChartAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14PolarChartAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PolarChartAxis::tr(s, c, n));
}

//  PolarChartAxis::~PolarChartAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxisD1Ev(PolarChartAxis *self) {
  delete self;
}

//  void PolarChartAxis::setGeometry(const QRectF &axis, const QRectF &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis11setGeometryERK6QRectFS2_(
    PolarChartAxis *self,
    const QRectF *axis,
    const QRectF *grid) {
  self->setGeometry(*axis, *grid);
}

//  qreal PolarChartAxis::preferredAxisRadius(const QSizeF &maxSize)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14PolarChartAxis19preferredAxisRadiusERK6QSizeF(
    PolarChartAxis *self,
    const QSizeF *maxSize) {
  return self->preferredAxisRadius(*maxSize);
}

//  int PolarChartAxis::tickWidth()
extern "C" Q_DECL_EXPORT
int ritual_ZN14PolarChartAxis9tickWidthEv(PolarChartAxis *self) {
  return self->tickWidth();
}

//  QRectF PolarChartAxis::gridGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14PolarChartAxis12gridGeometryEv(
    const PolarChartAxis *self) {
  return new QRectF(self->gridGeometry());
}

//  bool PolarChartAxis::emptyAxis() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14PolarChartAxis9emptyAxisEv(const PolarChartAxis *self) {
  return self->emptyAxis();
}

//  void PolarChartAxis::createItems(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis11createItemsEi(
    PolarChartAxis *self,
    int count) {
  self->createItems(count);
}

//  void PolarChartAxis::updateMinorTickItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis20updateMinorTickItemsEv(
    PolarChartAxis *self) {
  self->updateMinorTickItems();
}

//  void PolarChartAxis::handleShadesBrushChanged(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis24handleShadesBrushChangedERK6QBrush(
    PolarChartAxis *self,
    const QBrush *brush) {
  self->handleShadesBrushChanged(*brush);
}

//  void PolarChartAxis::handleShadesPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis22handleShadesPenChangedERK4QPen(
    PolarChartAxis *self,
    const QPen *pen) {
  self->handleShadesPenChanged(*pen);
}

//  void PolarChartAxis::deleteItems(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14PolarChartAxis11deleteItemsEi(
    PolarChartAxis *self,
    int count) {
  self->deleteItems(count);
}

//  a Python function taken by a CutePolarChartAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PolarChartAxis(
    PolarChartAxis *self,
    const char *key,
    void *call) {
  return static_cast<CutePolarChartAxis *>(self)->take(key, call);
}

//  void PolarChartAxis::setGeometry(const QRectF &axis, const QRectF &grid)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14PolarChartAxis11setGeometryERK6QRectFS2_(
    PolarChartAxis *self,
    const QRectF *axis,
    const QRectF *grid) {
  self->PolarChartAxis::setGeometry(*axis, *grid);
}

//  QRectF PolarChartAxis::gridGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK14PolarChartAxis12gridGeometryEv(
    const PolarChartAxis *self) {
  return new QRectF(self->PolarChartAxis::gridGeometry());
}

//  bool PolarChartAxis::emptyAxis() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14PolarChartAxis9emptyAxisEv(const PolarChartAxis *self) {
  return self->PolarChartAxis::emptyAxis();
}

//  void PolarChartAxis::handleShadesBrushChanged(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14PolarChartAxis24handleShadesBrushChangedERK6QBrush(
    PolarChartAxis *self,
    const QBrush *brush) {
  self->PolarChartAxis::handleShadesBrushChanged(*brush);
}

//  void PolarChartAxis::handleShadesPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14PolarChartAxis22handleShadesPenChangedERK4QPen(
    PolarChartAxis *self,
    const QPen *pen) {
  self->PolarChartAxis::handleShadesPenChanged(*pen);
}
