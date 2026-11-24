//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A ChartAxisElement that Python can take functions over in. Every ChartAxisElement
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteChartAxisElementCall0)(const void *, int *);
typedef void (*CuteChartAxisElementCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef bool (*CuteChartAxisElementCall2)(const void *, int *);
typedef void * (*CuteChartAxisElementCall3)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteChartAxisElementCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall5)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall6)(const void *, const QBrush *, int *);
typedef void (*CuteChartAxisElementCall7)(const void *, const QPen *, int *);
typedef void (*CuteChartAxisElementCall8)(const void *, const QPen *, int *);
typedef void (*CuteChartAxisElementCall9)(const void *, const QPen *, int *);
typedef void (*CuteChartAxisElementCall10)(const void *, const QPen *, int *);
typedef void (*CuteChartAxisElementCall11)(const void *, const QPen *, int *);
typedef void (*CuteChartAxisElementCall12)(const void *, const QColor *, int *);
typedef void (*CuteChartAxisElementCall13)(const void *, const QColor *, int *);
typedef void (*CuteChartAxisElementCall14)(const void *, ChartPresenter *, int *);
typedef void (*CuteChartAxisElementCall15)(const void *, ChartThemeManager *, int *);
typedef void (*CuteChartAxisElementCall16)(const void *, ChartDataSet *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartAxisElementCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartAxisElementCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartAxisElementCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartAxisElementCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartAxisElementCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartAxisElementCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall24)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall25)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall26)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteChartAxisElementCall27)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartAxisElementCall29)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall30)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall31)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall32)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall33)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteChartAxisElementCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteChartAxisElementCall35)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall36)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteChartAxisElementCall37)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall38)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall39)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall40)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall41)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall42)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall43)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall44)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall45)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall46)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall47)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall48)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall49)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall50)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall51)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall52)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall54)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteChartAxisElementCall55)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartAxisElementCall56)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartAxisElementCall57)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteChartAxisElementCall58)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteChartAxisElement : public ChartAxisElement {
public:
  using ChartAxisElement::ChartAxisElement;
  void *taken[59] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16ChartAxisElement12gridGeometryEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement11setGeometryERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16ChartAxisElement9emptyAxisEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12ChartElement9animationEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement20handleGridPenChangedERK4QPen")) {
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
    if (!std::strcmp(key, "_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QColor")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement12setPresenterEP14ChartPresenter")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement15setThemeManagerEP17ChartThemeManager")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12ChartElement10setDataSetEP12ChartDataSet")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
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

  //  QRectF ChartAxisElement::gridGeometry() const
  QRectF gridGeometry() const override {
    if (taken[0]) {
      int handled = 0;
      CuteChartAxisElementCall0 call = reinterpret_cast<CuteChartAxisElementCall0>(taken[0]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void ChartAxisElement::setGeometry(const QRectF &axis, const QRectF
  //      &grid)
  void setGeometry(const QRectF &axis, const QRectF &grid) override {
    if (taken[1]) {
      int handled = 0;
      CuteChartAxisElementCall1 call = reinterpret_cast<CuteChartAxisElementCall1>(taken[1]);
      call(this, &axis, &grid, &handled);
      if (handled) return;
    }
  }

  //  bool ChartAxisElement::emptyAxis() const
  bool emptyAxis() const override {
    if (taken[2]) {
      int handled = 0;
      CuteChartAxisElementCall2 call = reinterpret_cast<CuteChartAxisElementCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  AxisAnimation *ChartAxisElement::animation() const
  AxisAnimation *animation() const override {
    if (taken[3]) {
      int handled = 0;
      CuteChartAxisElementCall3 call = reinterpret_cast<CuteChartAxisElementCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<AxisAnimation *>(given);
    }
    return ChartAxisElement::animation();
  }

#if QT_CONFIG(graphicsview)
  //  QRectF ChartAxisElement::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteChartAxisElementCall4 call = reinterpret_cast<CuteChartAxisElementCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteChartAxisElementCall5 call = reinterpret_cast<CuteChartAxisElementCall5>(taken[5]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    ChartAxisElement::paint(a0, a1, a2);
  }
#endif  // QT_CONFIG(graphicsview)

  //  void ChartAxisElement::handleShadesBrushChanged(const QBrush &brush)
  void handleShadesBrushChanged(const QBrush &brush) override {
    if (taken[6]) {
      int handled = 0;
      CuteChartAxisElementCall6 call = reinterpret_cast<CuteChartAxisElementCall6>(taken[6]);
      call(this, &brush, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleShadesPenChanged(const QPen &pen)
  void handleShadesPenChanged(const QPen &pen) override {
    if (taken[7]) {
      int handled = 0;
      CuteChartAxisElementCall7 call = reinterpret_cast<CuteChartAxisElementCall7>(taken[7]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleArrowPenChanged(const QPen &pen)
  void handleArrowPenChanged(const QPen &pen) override {
    if (taken[8]) {
      int handled = 0;
      CuteChartAxisElementCall8 call = reinterpret_cast<CuteChartAxisElementCall8>(taken[8]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleGridPenChanged(const QPen &pen)
  void handleGridPenChanged(const QPen &pen) override {
    if (taken[9]) {
      int handled = 0;
      CuteChartAxisElementCall9 call = reinterpret_cast<CuteChartAxisElementCall9>(taken[9]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorArrowPenChanged(const QPen &pen)
  void handleMinorArrowPenChanged(const QPen &pen) override {
    if (taken[10]) {
      int handled = 0;
      CuteChartAxisElementCall10 call = reinterpret_cast<CuteChartAxisElementCall10>(taken[10]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorGridPenChanged(const QPen &pen)
  void handleMinorGridPenChanged(const QPen &pen) override {
    if (taken[11]) {
      int handled = 0;
      CuteChartAxisElementCall11 call = reinterpret_cast<CuteChartAxisElementCall11>(taken[11]);
      call(this, &pen, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleMinorGridLineColorChanged(const QColor
  //      &color)
  void handleMinorGridLineColorChanged(const QColor &color) override {
    if (taken[12]) {
      int handled = 0;
      CuteChartAxisElementCall12 call = reinterpret_cast<CuteChartAxisElementCall12>(taken[12]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void ChartAxisElement::handleGridLineColorChanged(const QColor
  //      &color)
  void handleGridLineColorChanged(const QColor &color) override {
    if (taken[13]) {
      int handled = 0;
      CuteChartAxisElementCall13 call = reinterpret_cast<CuteChartAxisElementCall13>(taken[13]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  void ChartElement::setPresenter(ChartPresenter *presenter)
  void setPresenter(ChartPresenter *presenter) override {
    if (taken[14]) {
      int handled = 0;
      CuteChartAxisElementCall14 call = reinterpret_cast<CuteChartAxisElementCall14>(taken[14]);
      call(this, presenter, &handled);
      if (handled) return;
    }
    ChartElement::setPresenter(presenter);
  }

  //  void ChartElement::setThemeManager(ChartThemeManager *manager)
  void setThemeManager(ChartThemeManager *manager) override {
    if (taken[15]) {
      int handled = 0;
      CuteChartAxisElementCall15 call = reinterpret_cast<CuteChartAxisElementCall15>(taken[15]);
      call(this, manager, &handled);
      if (handled) return;
    }
    ChartElement::setThemeManager(manager);
  }

  //  void ChartElement::setDataSet(ChartDataSet *dataSet)
  void setDataSet(ChartDataSet *dataSet) override {
    if (taken[16]) {
      int handled = 0;
      CuteChartAxisElementCall16 call = reinterpret_cast<CuteChartAxisElementCall16>(taken[16]);
      call(this, dataSet, &handled);
      if (handled) return;
    }
    ChartElement::setDataSet(dataSet);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsObject::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[17]) {
      int handled = 0;
      CuteChartAxisElementCall17 call = reinterpret_cast<CuteChartAxisElementCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteChartAxisElementCall18 call = reinterpret_cast<CuteChartAxisElementCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteChartAxisElementCall19 call = reinterpret_cast<CuteChartAxisElementCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteChartAxisElementCall20 call = reinterpret_cast<CuteChartAxisElementCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteChartAxisElementCall21 call = reinterpret_cast<CuteChartAxisElementCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteChartAxisElementCall22 call = reinterpret_cast<CuteChartAxisElementCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteChartAxisElementCall23 call = reinterpret_cast<CuteChartAxisElementCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[24]) {
      int handled = 0;
      CuteChartAxisElementCall24 call = reinterpret_cast<CuteChartAxisElementCall24>(taken[24]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutItem::updateGeometry()
  void updateGeometry() override {
    if (taken[25]) {
      int handled = 0;
      CuteChartAxisElementCall25 call = reinterpret_cast<CuteChartAxisElementCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[26]) {
      int handled = 0;
      CuteChartAxisElementCall26 call = reinterpret_cast<CuteChartAxisElementCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteChartAxisElementCall27 call = reinterpret_cast<CuteChartAxisElementCall27>(taken[27]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[28]) {
      int handled = 0;
      CuteChartAxisElementCall28 call = reinterpret_cast<CuteChartAxisElementCall28>(taken[28]);
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
      CuteChartAxisElementCall29 call = reinterpret_cast<CuteChartAxisElementCall29>(taken[29]);
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
      CuteChartAxisElementCall30 call = reinterpret_cast<CuteChartAxisElementCall30>(taken[30]);
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
      CuteChartAxisElementCall31 call = reinterpret_cast<CuteChartAxisElementCall31>(taken[31]);
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
      CuteChartAxisElementCall32 call = reinterpret_cast<CuteChartAxisElementCall32>(taken[32]);
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
      CuteChartAxisElementCall33 call = reinterpret_cast<CuteChartAxisElementCall33>(taken[33]);
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
      CuteChartAxisElementCall34 call = reinterpret_cast<CuteChartAxisElementCall34>(taken[34]);
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
      CuteChartAxisElementCall35 call = reinterpret_cast<CuteChartAxisElementCall35>(taken[35]);
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
      CuteChartAxisElementCall36 call = reinterpret_cast<CuteChartAxisElementCall36>(taken[36]);
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
      CuteChartAxisElementCall37 call = reinterpret_cast<CuteChartAxisElementCall37>(taken[37]);
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
      CuteChartAxisElementCall38 call = reinterpret_cast<CuteChartAxisElementCall38>(taken[38]);
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
      CuteChartAxisElementCall39 call = reinterpret_cast<CuteChartAxisElementCall39>(taken[39]);
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
      CuteChartAxisElementCall40 call = reinterpret_cast<CuteChartAxisElementCall40>(taken[40]);
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
      CuteChartAxisElementCall41 call = reinterpret_cast<CuteChartAxisElementCall41>(taken[41]);
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
      CuteChartAxisElementCall42 call = reinterpret_cast<CuteChartAxisElementCall42>(taken[42]);
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
      CuteChartAxisElementCall43 call = reinterpret_cast<CuteChartAxisElementCall43>(taken[43]);
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
      CuteChartAxisElementCall44 call = reinterpret_cast<CuteChartAxisElementCall44>(taken[44]);
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
      CuteChartAxisElementCall45 call = reinterpret_cast<CuteChartAxisElementCall45>(taken[45]);
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
      CuteChartAxisElementCall46 call = reinterpret_cast<CuteChartAxisElementCall46>(taken[46]);
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
      CuteChartAxisElementCall47 call = reinterpret_cast<CuteChartAxisElementCall47>(taken[47]);
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
      CuteChartAxisElementCall48 call = reinterpret_cast<CuteChartAxisElementCall48>(taken[48]);
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
      CuteChartAxisElementCall49 call = reinterpret_cast<CuteChartAxisElementCall49>(taken[49]);
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
      CuteChartAxisElementCall50 call = reinterpret_cast<CuteChartAxisElementCall50>(taken[50]);
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
      CuteChartAxisElementCall51 call = reinterpret_cast<CuteChartAxisElementCall51>(taken[51]);
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
      CuteChartAxisElementCall52 call = reinterpret_cast<CuteChartAxisElementCall52>(taken[52]);
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
      CuteChartAxisElementCall53 call = reinterpret_cast<CuteChartAxisElementCall53>(taken[53]);
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
      CuteChartAxisElementCall54 call = reinterpret_cast<CuteChartAxisElementCall54>(taken[54]);
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
      CuteChartAxisElementCall55 call = reinterpret_cast<CuteChartAxisElementCall55>(taken[55]);
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
      CuteChartAxisElementCall56 call = reinterpret_cast<CuteChartAxisElementCall56>(taken[56]);
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
      CuteChartAxisElementCall57 call = reinterpret_cast<CuteChartAxisElementCall57>(taken[57]);
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
      CuteChartAxisElementCall58 call = reinterpret_cast<CuteChartAxisElementCall58>(taken[58]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *ChartAxisElement::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16ChartAxisElement10metaObjectEv(
    const ChartAxisElement *self) {
  return self->metaObject();
}

//  QString ChartAxisElement::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16ChartAxisElement2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartAxisElement::tr(s, c, n));
}

//  ChartAxisElement::~ChartAxisElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElementD1Ev(ChartAxisElement *self) {
  delete self;
}

//  QRectF ChartAxisElement::gridGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16ChartAxisElement12gridGeometryEv(
    const ChartAxisElement *self) {
  return new QRectF(self->gridGeometry());
}

//  void ChartAxisElement::setGeometry(const QRectF &axis, const QRectF
//      &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement11setGeometryERK6QRectFS2_(
    ChartAxisElement *self,
    const QRectF *axis,
    const QRectF *grid) {
  self->setGeometry(*axis, *grid);
}

//  bool ChartAxisElement::emptyAxis() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16ChartAxisElement9emptyAxisEv(const ChartAxisElement *self) {
  return self->emptyAxis();
}

//  void ChartAxisElement::setAnimation(AxisAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement12setAnimationEP13AxisAnimation(
    ChartAxisElement *self,
    AxisAnimation *animation) {
  self->setAnimation(animation);
}

//  AxisAnimation *ChartAxisElement::animation() const
extern "C" Q_DECL_EXPORT
AxisAnimation *ritual_ZNK16ChartAxisElement9animationEv(
    const ChartAxisElement *self) {
  return self->animation();
}

//  QAbstractAxis *ChartAxisElement::axis() const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK16ChartAxisElement4axisEv(
    const ChartAxisElement *self) {
  return self->axis();
}

//  qreal ChartAxisElement::labelPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement12labelPaddingEv(
    const ChartAxisElement *self) {
  return self->labelPadding();
}

//  qreal ChartAxisElement::titlePadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement12titlePaddingEv(
    const ChartAxisElement *self) {
  return self->titlePadding();
}

//  qreal ChartAxisElement::colorScalePadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement17colorScalePaddingEv(
    const ChartAxisElement *self) {
  return self->colorScalePadding();
}

//  void ChartAxisElement::setLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement9setLabelsERK5QListI7QStringE(
    ChartAxisElement *self,
    const QList<QString> *labels) {
  self->setLabels(*labels);
}

//  QStringList ChartAxisElement::labels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16ChartAxisElement6labelsEv(
    const ChartAxisElement *self) {
  return new QList<QString>(self->labels());
}

//  qreal ChartAxisElement::min() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement3minEv(const ChartAxisElement *self) {
  return self->min();
}

//  qreal ChartAxisElement::max() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement3maxEv(const ChartAxisElement *self) {
  return self->max();
}

//  qreal ChartAxisElement::tickInterval() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement12tickIntervalEv(
    const ChartAxisElement *self) {
  return self->tickInterval();
}

//  qreal ChartAxisElement::tickAnchor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16ChartAxisElement10tickAnchorEv(
    const ChartAxisElement *self) {
  return self->tickAnchor();
}

//  QRectF ChartAxisElement::axisGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16ChartAxisElement12axisGeometryEv(
    const ChartAxisElement *self) {
  return new QRectF(self->axisGeometry());
}

//  void ChartAxisElement::setAxisGeometry(const QRectF &axisGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement15setAxisGeometryERK6QRectF(
    ChartAxisElement *self,
    const QRectF *axisGeometry) {
  self->setAxisGeometry(*axisGeometry);
}

//  void ChartAxisElement::axisSelected()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement12axisSelectedEv(ChartAxisElement *self) {
  self->axisSelected();
}

//  bool ChartAxisElement::intervalAxis() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16ChartAxisElement12intervalAxisEv(
    const ChartAxisElement *self) {
  return self->intervalAxis();
}

//  QStringList ChartAxisElement::createValueLabels(qreal max, qreal min, int
//      ticks, qreal tickInterval, qreal tickAnchor, QValueAxis::TickType
//      tickType, const QString &format) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16ChartAxisElement17createValueLabelsEddiddN10QValueAxis8TickTypeERK7QString(
    const ChartAxisElement *self,
    qreal max,
    qreal min,
    int ticks,
    qreal tickInterval,
    qreal tickAnchor,
    QValueAxis::TickType tickType,
    const QString *format) {
  return new QList<QString>(
      self->createValueLabels(
          max,
          min,
          ticks,
          tickInterval,
          tickAnchor,
          tickType,
          *format));
}

//  QStringList ChartAxisElement::createLogValueLabels(qreal min, qreal max,
//      qreal base, int ticks, const QString &format) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16ChartAxisElement20createLogValueLabelsEdddiRK7QString(
    const ChartAxisElement *self,
    qreal min,
    qreal max,
    qreal base,
    int ticks,
    const QString *format) {
  return new QList<QString>(
      self->createLogValueLabels(
          min,
          max,
          base,
          ticks,
          *format));
}

//  QStringList ChartAxisElement::createDateTimeLabels(qreal max, qreal min,
//      int ticks, const QString &format) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16ChartAxisElement20createDateTimeLabelsEddiRK7QString(
    const ChartAxisElement *self,
    qreal max,
    qreal min,
    int ticks,
    const QString *format) {
  return new QList<QString>(
      self->createDateTimeLabels(
          max,
          min,
          ticks,
          *format));
}

//  QStringList ChartAxisElement::createColorLabels(qreal min, qreal max, int
//      ticks) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16ChartAxisElement17createColorLabelsEddi(
    const ChartAxisElement *self,
    qreal min,
    qreal max,
    int ticks) {
  return new QList<QString>(self->createColorLabels(min, max, ticks));
}

//  QRectF ChartAxisElement::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16ChartAxisElement12boundingRectEv(
    const ChartAxisElement *self) {
  return new QRectF(self->boundingRect());
}

//  void ChartAxisElement::paint(QPainter *a0, const QStyleOptionGraphicsItem
//      *a1, QWidget *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    ChartAxisElement *self,
    QPainter *a0,
    const QStyleOptionGraphicsItem *a1,
    QWidget *a2) {
  self->paint(a0, a1, a2);
}

//  bool ChartAxisElement::labelsEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16ChartAxisElement14labelsEditableEv(
    const ChartAxisElement *self) {
  return self->labelsEditable();
}

//  void ChartAxisElement::setLabelsEditable(bool labelsEditable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement17setLabelsEditableEb(
    ChartAxisElement *self,
    bool labelsEditable) {
  self->setLabelsEditable(labelsEditable);
}

//  bool ChartAxisElement::labelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16ChartAxisElement13labelsVisibleEv(
    const ChartAxisElement *self) {
  return self->labelsVisible();
}

//  QList<QGraphicsItem *> ChartAxisElement::gridItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement9gridItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->gridItems());
}

//  QList<QGraphicsItem *> ChartAxisElement::minorGridItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement14minorGridItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->minorGridItems());
}

//  QList<QGraphicsItem *> ChartAxisElement::labelItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement10labelItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->labelItems());
}

//  QList<QGraphicsItem *> ChartAxisElement::shadeItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement10shadeItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->shadeItems());
}

//  QList<QGraphicsItem *> ChartAxisElement::arrowItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement10arrowItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->arrowItems());
}

//  QList<QGraphicsItem *> ChartAxisElement::minorArrowItems()
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZN16ChartAxisElement15minorArrowItemsEv(
    ChartAxisElement *self) {
  return new QList<QGraphicsItem *>(self->minorArrowItems());
}

//  QGraphicsTextItem *ChartAxisElement::titleItem() const
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZNK16ChartAxisElement9titleItemEv(
    const ChartAxisElement *self) {
  return self->titleItem();
}

//  QGraphicsPixmapItem *ChartAxisElement::colorScaleItem() const
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZNK16ChartAxisElement14colorScaleItemEv(
    const ChartAxisElement *self) {
  return self->colorScaleItem();
}

//  QGraphicsItemGroup *ChartAxisElement::gridGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement9gridGroupEv(
    ChartAxisElement *self) {
  return self->gridGroup();
}

//  QGraphicsItemGroup *ChartAxisElement::minorGridGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement14minorGridGroupEv(
    ChartAxisElement *self) {
  return self->minorGridGroup();
}

//  QGraphicsItemGroup *ChartAxisElement::labelGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement10labelGroupEv(
    ChartAxisElement *self) {
  return self->labelGroup();
}

//  QGraphicsItemGroup *ChartAxisElement::shadeGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement10shadeGroupEv(
    ChartAxisElement *self) {
  return self->shadeGroup();
}

//  QGraphicsItemGroup *ChartAxisElement::arrowGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement10arrowGroupEv(
    ChartAxisElement *self) {
  return self->arrowGroup();
}

//  QGraphicsItemGroup *ChartAxisElement::minorArrowGroup()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN16ChartAxisElement15minorArrowGroupEv(
    ChartAxisElement *self) {
  return self->minorArrowGroup();
}

//  void ChartAxisElement::prepareColorScale(const qreal width, const qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement17prepareColorScaleEdd(
    ChartAxisElement *self,
    qreal width,
    qreal height) {
  self->prepareColorScale(width, height);
}

//  void ChartAxisElement::handleVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement20handleVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleVisibleChanged(visible);
}

//  void ChartAxisElement::handleArrowVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement25handleArrowVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleArrowVisibleChanged(visible);
}

//  void ChartAxisElement::handleGridVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement24handleGridVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleGridVisibleChanged(visible);
}

//  void ChartAxisElement::handleLabelsVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement26handleLabelsVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleLabelsVisibleChanged(visible);
}

//  void ChartAxisElement::handleShadesVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement26handleShadesVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleShadesVisibleChanged(visible);
}

//  void ChartAxisElement::handleLabelsAngleChanged(int angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement24handleLabelsAngleChangedEi(
    ChartAxisElement *self,
    int angle) {
  self->handleLabelsAngleChanged(angle);
}

//  void ChartAxisElement::handleShadesBrushChanged(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush(
    ChartAxisElement *self,
    const QBrush *brush) {
  self->handleShadesBrushChanged(*brush);
}

//  void ChartAxisElement::handleShadesPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen(
    ChartAxisElement *self,
    const QPen *pen) {
  self->handleShadesPenChanged(*pen);
}

//  void ChartAxisElement::handleArrowPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen(
    ChartAxisElement *self,
    const QPen *pen) {
  self->handleArrowPenChanged(*pen);
}

//  void ChartAxisElement::handleGridPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement20handleGridPenChangedERK4QPen(
    ChartAxisElement *self,
    const QPen *pen) {
  self->handleGridPenChanged(*pen);
}

//  void ChartAxisElement::handleMinorArrowPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement26handleMinorArrowPenChangedERK4QPen(
    ChartAxisElement *self,
    const QPen *pen) {
  self->handleMinorArrowPenChanged(*pen);
}

//  void ChartAxisElement::handleMinorGridPenChanged(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement25handleMinorGridPenChangedERK4QPen(
    ChartAxisElement *self,
    const QPen *pen) {
  self->handleMinorGridPenChanged(*pen);
}

//  void ChartAxisElement::handleMinorGridLineColorChanged(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QColor(
    ChartAxisElement *self,
    const QColor *color) {
  self->handleMinorGridLineColorChanged(*color);
}

//  void ChartAxisElement::handleGridLineColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor(
    ChartAxisElement *self,
    const QColor *color) {
  self->handleGridLineColorChanged(*color);
}

//  void ChartAxisElement::handleLabelsBrushChanged(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement24handleLabelsBrushChangedERK6QBrush(
    ChartAxisElement *self,
    const QBrush *brush) {
  self->handleLabelsBrushChanged(*brush);
}

//  void ChartAxisElement::handleLabelsFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement23handleLabelsFontChangedERK5QFont(
    ChartAxisElement *self,
    const QFont *font) {
  self->handleLabelsFontChanged(*font);
}

//  void ChartAxisElement::handleTitleBrushChanged(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement23handleTitleBrushChangedERK6QBrush(
    ChartAxisElement *self,
    const QBrush *brush) {
  self->handleTitleBrushChanged(*brush);
}

//  void ChartAxisElement::handleTitleFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement22handleTitleFontChangedERK5QFont(
    ChartAxisElement *self,
    const QFont *font) {
  self->handleTitleFontChanged(*font);
}

//  void ChartAxisElement::handleTitleTextChanged(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement22handleTitleTextChangedERK7QString(
    ChartAxisElement *self,
    const QString *title) {
  self->handleTitleTextChanged(*title);
}

//  void ChartAxisElement::handleTitleVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement25handleTitleVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleTitleVisibleChanged(visible);
}

//  void ChartAxisElement::handleRangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement18handleRangeChangedEdd(
    ChartAxisElement *self,
    qreal min,
    qreal max) {
  self->handleRangeChanged(min, max);
}

//  void ChartAxisElement::handleReverseChanged(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement20handleReverseChangedEb(
    ChartAxisElement *self,
    bool reverse) {
  self->handleReverseChanged(reverse);
}

//  void ChartAxisElement::handleMinorArrowVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement30handleMinorArrowVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleMinorArrowVisibleChanged(visible);
}

//  void ChartAxisElement::handleMinorGridVisibleChanged(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement29handleMinorGridVisibleChangedEb(
    ChartAxisElement *self,
    bool visible) {
  self->handleMinorGridVisibleChanged(visible);
}

//  void ChartAxisElement::handleLabelsPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement27handleLabelsPositionChangedEv(
    ChartAxisElement *self) {
  self->handleLabelsPositionChanged();
}

//  void ChartAxisElement::handleTruncateLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement27handleTruncateLabelsChangedEv(
    ChartAxisElement *self) {
  self->handleTruncateLabelsChanged();
}

//  void ChartAxisElement::handleColorScaleSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement27handleColorScaleSizeChangedEv(
    ChartAxisElement *self) {
  self->handleColorScaleSizeChanged();
}

//  void ChartAxisElement::handleColorScaleGradientChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement31handleColorScaleGradientChangedEv(
    ChartAxisElement *self) {
  self->handleColorScaleGradientChanged();
}

//  void ChartAxisElement::valueLabelEdited(qreal oldValue, qreal newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement16valueLabelEditedEdd(
    ChartAxisElement *self,
    qreal oldValue,
    qreal newValue) {
  self->valueLabelEdited(oldValue, newValue);
}

//  void ChartAxisElement::dateTimeLabelEdited(const QDateTime &oldTime,
//      const QDateTime &newTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement19dateTimeLabelEditedERK9QDateTimeS2_(
    ChartAxisElement *self,
    const QDateTime *oldTime,
    const QDateTime *newTime) {
  self->dateTimeLabelEdited(*oldTime, *newTime);
}

//  void ChartAxisElement::connectSlots()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ChartAxisElement12connectSlotsEv(ChartAxisElement *self) {
  self->connectSlots();
}

//  QString ChartAxisElement::formatLabel(const QString &formatSpec, const
//      QByteArray &array, qreal value, int precision, const QString &preStr,
//      const QString &postStr) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16ChartAxisElement11formatLabelERK7QStringRK10QByteArraydiS2_S2_(
    const ChartAxisElement *self,
    const QString *formatSpec,
    const QByteArray *array,
    qreal value,
    int precision,
    const QString *preStr,
    const QString *postStr) {
  return new QString(
      self->formatLabel(
          *formatSpec,
          *array,
          value,
          precision,
          *preStr,
          *postStr));
}

//  ChartAxisElement as the QGraphicsLayoutItem it is built on
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_cast_ChartAxisElement_QGraphicsLayoutItem(
    ChartAxisElement *self) {
  return static_cast<QGraphicsLayoutItem *>(self);
}

//  a Python function taken by a CuteChartAxisElement, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartAxisElement(
    ChartAxisElement *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartAxisElement *>(self)->take(key, call);
}

//  AxisAnimation *ChartAxisElement::animation() const
extern "C" Q_DECL_EXPORT
AxisAnimation *ritual_own_ZNK16ChartAxisElement9animationEv(
    const ChartAxisElement *self) {
  return self->ChartAxisElement::animation();
}

//  QRectF ChartAxisElement::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK16ChartAxisElement12boundingRectEv(
    const ChartAxisElement *self) {
  return new QRectF(self->ChartAxisElement::boundingRect());
}

//  void ChartAxisElement::paint(QPainter *a0, const QStyleOptionGraphicsItem
//      *a1, QWidget *a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ChartAxisElement5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    ChartAxisElement *self,
    QPainter *a0,
    const QStyleOptionGraphicsItem *a1,
    QWidget *a2) {
  self->ChartAxisElement::paint(a0, a1, a2);
}

//  QList<ChartAxisElement *>::QList()
extern "C" Q_DECL_EXPORT
QList<ChartAxisElement *> *ritual_list_make_ChartAxisElement_ptr() {
  return new QList<ChartAxisElement *>();
}

//  void QList<ChartAxisElement *>::append(const ChartAxisElement * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_ChartAxisElement_ptr(
    QList<ChartAxisElement *> *self,
    ChartAxisElement *element) {
  self->append(element);
}

//  qsizetype QList<ChartAxisElement *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_ChartAxisElement_ptr(
    const QList<ChartAxisElement *> *self) {
  return self->size();
}

//  const ChartAxisElement * &QList<ChartAxisElement *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
ChartAxisElement *ritual_list_at_ChartAxisElement_ptr(
    const QList<ChartAxisElement *> *self,
    long long index) {
  return self->at(index);
}

//  QList<ChartAxisElement *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_ChartAxisElement_ptr(QList<ChartAxisElement *> *self) {
  delete self;
}
