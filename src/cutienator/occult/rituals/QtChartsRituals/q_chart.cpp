//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qchart.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qchart.h>
#include <QtCore/qstring.h>
#include <QtCharts/qabstractseries.h>
#include <QtCharts/qabstractaxis.h>
#include <QtGui/qfont.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlocale.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QChart that Python can take functions over in. Every QChart
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQChartCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQChartCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQChartCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall6)(const void *, QStyleOption *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQChartCall7)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQChartCall9)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQChartCall10)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQChartCall13)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall14)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall16)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall17)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall18)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall20)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall21)(const void *, QGraphicsSceneMoveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall22)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall23)(const void *, QGraphicsSceneResizeEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall24)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall25)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall27)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall28)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall30)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQChartCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall37)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall38)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall39)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall40)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall41)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall42)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQChartCall43)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartCall44)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall45)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall46)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall47)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall48)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall49)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall50)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall51)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall52)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall54)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall55)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall56)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall57)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQChartCall59)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQChartCall60)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQChart : public QChart {
public:
  using QChart::QChart;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16windowFrameEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget10closeEventEP11QCloseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget18focusNextPrevChildEb")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9hideEventEP10QHideEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11polishEventEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9showEventEP10QShowEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14grabMouseEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
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
    if (!std::strcmp(key, "_ZNK13QGraphicsItem9extensionERK8QVariant")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQChartCall0 call = reinterpret_cast<CuteQChartCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsWidget::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsWidget::type() const
  int type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQChartCall1 call = reinterpret_cast<CuteQChartCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      CuteQChartCall2 call = reinterpret_cast<CuteQChartCall2>(taken[2]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsWidget::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paintWindowFrame(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQChartCall3 call = reinterpret_cast<CuteQChartCall3>(taken[3]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsWidget::paintWindowFrame(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF QGraphicsWidget::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQChartCall4 call = reinterpret_cast<CuteQChartCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsWidget::shape() const
  QPainterPath shape() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQChartCall5 call = reinterpret_cast<CuteQChartCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
  void initStyleOption(QStyleOption *option) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQChartCall6 call = reinterpret_cast<CuteQChartCall6>(taken[6]);
      call(this, option, &handled);
      if (handled) return;
    }
    QGraphicsWidget::initStyleOption(option);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsWidget::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQChartCall7 call = reinterpret_cast<CuteQChartCall7>(taken[7]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::updateGeometry()
  void updateGeometry() override {
    if (taken[8]) {
      int handled = 0;
      CuteQChartCall8 call = reinterpret_cast<CuteQChartCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsWidget::itemChange(GraphicsItemChange change, const
  //      QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQChartCall9 call = reinterpret_cast<CuteQChartCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
  //      const QVariant &value)
  QVariant propertyChange(
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[10]) {
      int handled = 0;
      CuteQChartCall10 call = reinterpret_cast<CuteQChartCall10>(taken[10]);
      const QVariant * given = call(this, &propertyName, &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::propertyChange(propertyName, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQChartCall11 call = reinterpret_cast<CuteQChartCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
  bool windowFrameEvent(QEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQChartCall12 call = reinterpret_cast<CuteQChartCall12>(taken[12]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::windowFrameEvent(e);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  Qt::WindowFrameSection QGraphicsWidget::windowFrameSectionAt(const
  //      QPointF &pos) const
  Qt::WindowFrameSection windowFrameSectionAt(
      const QPointF &pos) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQChartCall13 call = reinterpret_cast<CuteQChartCall13>(taken[13]);
      int given = call(this, &pos, &handled);
      if (handled) return static_cast<Qt::WindowFrameSection>(given);
    }
    return QGraphicsWidget::windowFrameSectionAt(pos);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQChartCall14 call = reinterpret_cast<CuteQChartCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::event(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQChartCall15 call = reinterpret_cast<CuteQChartCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::changeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQChartCall16 call = reinterpret_cast<CuteQChartCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::closeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQChartCall17 call = reinterpret_cast<CuteQChartCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[18]) {
      int handled = 0;
      CuteQChartCall18 call = reinterpret_cast<CuteQChartCall18>(taken[18]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQChartCall19 call = reinterpret_cast<CuteQChartCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQChartCall20 call = reinterpret_cast<CuteQChartCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::hideEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
  void moveEvent(QGraphicsSceneMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQChartCall21 call = reinterpret_cast<CuteQChartCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::moveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::polishEvent()
  void polishEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQChartCall22 call = reinterpret_cast<CuteQChartCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::polishEvent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
  void resizeEvent(QGraphicsSceneResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQChartCall23 call = reinterpret_cast<CuteQChartCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::resizeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQChartCall24 call = reinterpret_cast<CuteQChartCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::showEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQChartCall25 call = reinterpret_cast<CuteQChartCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQChartCall26 call = reinterpret_cast<CuteQChartCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::grabMouseEvent(QEvent *event)
  void grabMouseEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQChartCall27 call = reinterpret_cast<CuteQChartCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::grabMouseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::ungrabMouseEvent(QEvent *event)
  void ungrabMouseEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQChartCall28 call = reinterpret_cast<CuteQChartCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::ungrabMouseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
  void grabKeyboardEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQChartCall29 call = reinterpret_cast<CuteQChartCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::grabKeyboardEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
  void ungrabKeyboardEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQChartCall30 call = reinterpret_cast<CuteQChartCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::ungrabKeyboardEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQChartCall31 call = reinterpret_cast<CuteQChartCall31>(taken[31]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQChartCall32 call = reinterpret_cast<CuteQChartCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQChartCall33 call = reinterpret_cast<CuteQChartCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQChartCall34 call = reinterpret_cast<CuteQChartCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[35]) {
      int handled = 0;
      CuteQChartCall35 call = reinterpret_cast<CuteQChartCall35>(taken[35]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQChartCall36 call = reinterpret_cast<CuteQChartCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQChartCall37 call = reinterpret_cast<CuteQChartCall37>(taken[37]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[38]) {
      int handled = 0;
      CuteQChartCall38 call = reinterpret_cast<CuteQChartCall38>(taken[38]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQChartCall39 call = reinterpret_cast<CuteQChartCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteQChartCall40 call = reinterpret_cast<CuteQChartCall40>(taken[40]);
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
    if (taken[41]) {
      int handled = 0;
      CuteQChartCall41 call = reinterpret_cast<CuteQChartCall41>(taken[41]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQChartCall42 call = reinterpret_cast<CuteQChartCall42>(taken[42]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQChartCall43 call = reinterpret_cast<CuteQChartCall43>(taken[43]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::opaqueArea();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::sceneEventFilter(QGraphicsItem *watched, QEvent
  //      *event)
  bool sceneEventFilter(QGraphicsItem *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQChartCall44 call = reinterpret_cast<CuteQChartCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQChartCall45 call = reinterpret_cast<CuteQChartCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQChartCall46 call = reinterpret_cast<CuteQChartCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQChartCall47 call = reinterpret_cast<CuteQChartCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQChartCall48 call = reinterpret_cast<CuteQChartCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQChartCall49 call = reinterpret_cast<CuteQChartCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQChartCall50 call = reinterpret_cast<CuteQChartCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsItem::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQChartCall51 call = reinterpret_cast<CuteQChartCall51>(taken[51]);
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
      CuteQChartCall52 call = reinterpret_cast<CuteQChartCall52>(taken[52]);
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
      CuteQChartCall53 call = reinterpret_cast<CuteQChartCall53>(taken[53]);
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
      CuteQChartCall54 call = reinterpret_cast<CuteQChartCall54>(taken[54]);
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
      CuteQChartCall55 call = reinterpret_cast<CuteQChartCall55>(taken[55]);
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
      CuteQChartCall56 call = reinterpret_cast<CuteQChartCall56>(taken[56]);
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
      CuteQChartCall57 call = reinterpret_cast<CuteQChartCall57>(taken[57]);
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
      CuteQChartCall58 call = reinterpret_cast<CuteQChartCall58>(taken[58]);
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
      CuteQChartCall59 call = reinterpret_cast<CuteQChartCall59>(taken[59]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[60]) {
      int handled = 0;
      CuteQChartCall60 call = reinterpret_cast<CuteQChartCall60>(taken[60]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *QChart::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QChart10metaObjectEv(const QChart *self) {
  return self->metaObject();
}

//  QString QChart::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QChart2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QChart::tr(s, c, n));
}

//  QChart::QChart(QGraphicsItem *parent, Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QChart *ritual_ZN6QChartC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new CuteQChart(parent, QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QChart::~QChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChartD1Ev(QChart *self) {
  delete self;
}

//  void QChart::addSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart9addSeriesEP15QAbstractSeries(
    QChart *self,
    QAbstractSeries *series) {
  self->addSeries(series);
}

//  void QChart::removeSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart12removeSeriesEP15QAbstractSeries(
    QChart *self,
    QAbstractSeries *series) {
  self->removeSeries(series);
}

//  void QChart::removeAllSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart15removeAllSeriesEv(QChart *self) {
  self->removeAllSeries();
}

//  QList<QAbstractSeries *> QChart::series() const
extern "C" Q_DECL_EXPORT
QList<QAbstractSeries *> *ritual_ZNK6QChart6seriesEv(const QChart *self) {
  return new QList<QAbstractSeries *>(self->series());
}

//  void QChart::setAxisX(QAbstractAxis *axis, QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart8setAxisXEP13QAbstractAxisP15QAbstractSeries(
    QChart *self,
    QAbstractAxis *axis,
    QAbstractSeries *series) {
  self->setAxisX(axis, series);
}

//  void QChart::setAxisY(QAbstractAxis *axis, QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart8setAxisYEP13QAbstractAxisP15QAbstractSeries(
    QChart *self,
    QAbstractAxis *axis,
    QAbstractSeries *series) {
  self->setAxisY(axis, series);
}

//  QAbstractAxis *QChart::axisX(QAbstractSeries *series) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK6QChart5axisXEP15QAbstractSeries(
    const QChart *self,
    QAbstractSeries *series) {
  return self->axisX(series);
}

//  QAbstractAxis *QChart::axisY(QAbstractSeries *series) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK6QChart5axisYEP15QAbstractSeries(
    const QChart *self,
    QAbstractSeries *series) {
  return self->axisY(series);
}

//  void QChart::addAxis(QAbstractAxis *axis, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart7addAxisEP13QAbstractAxis6QFlagsIN2Qt13AlignmentFlagEE(
    QChart *self,
    QAbstractAxis *axis,
    int alignment) {
  self->addAxis(axis, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QChart::removeAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart10removeAxisEP13QAbstractAxis(
    QChart *self,
    QAbstractAxis *axis) {
  self->removeAxis(axis);
}

//  QList<QAbstractAxis *> QChart::axes(Qt::Orientations orientation,
//      QAbstractSeries *series) const
extern "C" Q_DECL_EXPORT
QList<QAbstractAxis *> *ritual_ZNK6QChart4axesE6QFlagsIN2Qt11OrientationEEP15QAbstractSeries(
    const QChart *self,
    int orientation,
    QAbstractSeries *series) {
  return new QList<QAbstractAxis *>(
      self->axes(
          QFlags<Qt::Orientation>::fromInt(orientation),
          series));
}

//  void QChart::createDefaultAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart17createDefaultAxesEv(QChart *self) {
  self->createDefaultAxes();
}

//  void QChart::setTheme(QChart::ChartTheme theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart8setThemeENS_10ChartThemeE(
    QChart *self,
    QChart::ChartTheme theme) {
  self->setTheme(theme);
}

//  QChart::ChartTheme QChart::theme() const
extern "C" Q_DECL_EXPORT
QChart::ChartTheme ritual_ZNK6QChart5themeEv(const QChart *self) {
  return self->theme();
}

//  void QChart::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart8setTitleERK7QString(
    QChart *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QChart::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QChart5titleEv(const QChart *self) {
  return new QString(self->title());
}

//  void QChart::setTitleFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart12setTitleFontERK5QFont(
    QChart *self,
    const QFont *font) {
  self->setTitleFont(*font);
}

//  QFont QChart::titleFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK6QChart9titleFontEv(const QChart *self) {
  return new QFont(self->titleFont());
}

//  void QChart::setTitleBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart13setTitleBrushERK6QBrush(
    QChart *self,
    const QBrush *brush) {
  self->setTitleBrush(*brush);
}

//  QBrush QChart::titleBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK6QChart10titleBrushEv(const QChart *self) {
  return new QBrush(self->titleBrush());
}

//  void QChart::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart18setBackgroundBrushERK6QBrush(
    QChart *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush QChart::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK6QChart15backgroundBrushEv(const QChart *self) {
  return new QBrush(self->backgroundBrush());
}

//  void QChart::setBackgroundPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart16setBackgroundPenERK4QPen(
    QChart *self,
    const QPen *pen) {
  self->setBackgroundPen(*pen);
}

//  QPen QChart::backgroundPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK6QChart13backgroundPenEv(const QChart *self) {
  return new QPen(self->backgroundPen());
}

//  void QChart::setBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart20setBackgroundVisibleEb(QChart *self, bool visible) {
  self->setBackgroundVisible(visible);
}

//  bool QChart::isBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QChart19isBackgroundVisibleEv(const QChart *self) {
  return self->isBackgroundVisible();
}

//  void QChart::setDropShadowEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart20setDropShadowEnabledEb(QChart *self, bool enabled) {
  self->setDropShadowEnabled(enabled);
}

//  bool QChart::isDropShadowEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QChart19isDropShadowEnabledEv(const QChart *self) {
  return self->isDropShadowEnabled();
}

//  void QChart::setBackgroundRoundness(qreal diameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart22setBackgroundRoundnessEd(
    QChart *self,
    qreal diameter) {
  self->setBackgroundRoundness(diameter);
}

//  qreal QChart::backgroundRoundness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QChart19backgroundRoundnessEv(const QChart *self) {
  return self->backgroundRoundness();
}

//  void QChart::setAnimationOptions(AnimationOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart19setAnimationOptionsE6QFlagsINS_15AnimationOptionEE(
    QChart *self,
    int options) {
  self->setAnimationOptions(
      QFlags<QChart::AnimationOption>::fromInt(options));
}

//  AnimationOptions QChart::animationOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QChart16animationOptionsEv(const QChart *self) {
  return static_cast<int>(self->animationOptions().toInt());
}

//  void QChart::setAnimationDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart20setAnimationDurationEi(QChart *self, int msecs) {
  self->setAnimationDuration(msecs);
}

//  int QChart::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QChart17animationDurationEv(const QChart *self) {
  return self->animationDuration();
}

//  void QChart::setAnimationEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart23setAnimationEasingCurveERK12QEasingCurve(
    QChart *self,
    const QEasingCurve *curve) {
  self->setAnimationEasingCurve(*curve);
}

//  QEasingCurve QChart::animationEasingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK6QChart20animationEasingCurveEv(const QChart *self) {
  return new QEasingCurve(self->animationEasingCurve());
}

//  void QChart::zoomIn()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart6zoomInEv(QChart *self) {
  self->zoomIn();
}

//  void QChart::zoomOut()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart7zoomOutEv(QChart *self) {
  self->zoomOut();
}

//  void QChart::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart6zoomInERK6QRectF(QChart *self, const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void QChart::zoom(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart4zoomEd(QChart *self, qreal factor) {
  self->zoom(factor);
}

//  void QChart::zoomReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart9zoomResetEv(QChart *self) {
  self->zoomReset();
}

//  bool QChart::isZoomed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QChart8isZoomedEv(QChart *self) {
  return self->isZoomed();
}

//  void QChart::scroll(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart6scrollEdd(QChart *self, qreal dx, qreal dy) {
  self->scroll(dx, dy);
}

//  QLegend *QChart::legend() const
extern "C" Q_DECL_EXPORT
QLegend *ritual_ZNK6QChart6legendEv(const QChart *self) {
  return self->legend();
}

//  void QChart::setMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart10setMarginsERK8QMargins(
    QChart *self,
    const QMargins *margins) {
  self->setMargins(*margins);
}

//  QMargins QChart::margins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK6QChart7marginsEv(const QChart *self) {
  return new QMargins(self->margins());
}

//  QRectF QChart::plotArea() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QChart8plotAreaEv(const QChart *self) {
  return new QRectF(self->plotArea());
}

//  void QChart::setPlotArea(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart11setPlotAreaERK6QRectF(
    QChart *self,
    const QRectF *rect) {
  self->setPlotArea(*rect);
}

//  void QChart::setPlotAreaBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart26setPlotAreaBackgroundBrushERK6QBrush(
    QChart *self,
    const QBrush *brush) {
  self->setPlotAreaBackgroundBrush(*brush);
}

//  QBrush QChart::plotAreaBackgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK6QChart23plotAreaBackgroundBrushEv(const QChart *self) {
  return new QBrush(self->plotAreaBackgroundBrush());
}

//  void QChart::setPlotAreaBackgroundPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart24setPlotAreaBackgroundPenERK4QPen(
    QChart *self,
    const QPen *pen) {
  self->setPlotAreaBackgroundPen(*pen);
}

//  QPen QChart::plotAreaBackgroundPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK6QChart21plotAreaBackgroundPenEv(const QChart *self) {
  return new QPen(self->plotAreaBackgroundPen());
}

//  void QChart::setPlotAreaBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart28setPlotAreaBackgroundVisibleEb(
    QChart *self,
    bool visible) {
  self->setPlotAreaBackgroundVisible(visible);
}

//  bool QChart::isPlotAreaBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QChart27isPlotAreaBackgroundVisibleEv(const QChart *self) {
  return self->isPlotAreaBackgroundVisible();
}

//  void QChart::setLocalizeNumbers(bool localize)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart18setLocalizeNumbersEb(QChart *self, bool localize) {
  self->setLocalizeNumbers(localize);
}

//  bool QChart::localizeNumbers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QChart15localizeNumbersEv(const QChart *self) {
  return self->localizeNumbers();
}

//  void QChart::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QChart9setLocaleERK7QLocale(
    QChart *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QChart::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK6QChart6localeEv(const QChart *self) {
  return new QLocale(self->locale());
}

//  QPointF QChart::mapToValue(const QPointF &position, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN6QChart10mapToValueERK7QPointFP15QAbstractSeries(
    QChart *self,
    const QPointF *position,
    QAbstractSeries *series) {
  return new QPointF(self->mapToValue(*position, series));
}

//  QPointF QChart::mapToPosition(const QPointF &value, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN6QChart13mapToPositionERK7QPointFP15QAbstractSeries(
    QChart *self,
    const QPointF *value,
    QAbstractSeries *series) {
  return new QPointF(self->mapToPosition(*value, series));
}

//  ChartType QChart::chartType() const
extern "C" Q_DECL_EXPORT
QChart::ChartType ritual_ZNK6QChart9chartTypeEv(const QChart *self) {
  return self->chartType();
}

//  QChart::QChart(QChart::ChartType type, QGraphicsItem *parent,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QChart *ritual_ZN6QChartC1ENS_9ChartTypeEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QChart::ChartType type,
    QGraphicsItem *parent,
    int wFlags) {
  return new CuteQChart(
      type,
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  a Python function taken by a CuteQChart, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QChart(QChart *self, const char *key, void *call) {
  return static_cast<CuteQChart *>(self)->take(key, call);
}
