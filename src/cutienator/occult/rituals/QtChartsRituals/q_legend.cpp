//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qlegend.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/qlegend.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpen.h>
#include <QtGui/qfont.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QLegend may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLegend : QLegend {
  using QLegend::hideEvent;
  using QLegend::showEvent;
};

//  A QLegend that Python can take functions over in. Every QLegend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall0)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall1)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall2)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall3)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQLegendCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall5)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQLegendCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQLegendCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall8)(const void *, QStyleOption *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQLegendCall9)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall10)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQLegendCall11)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQLegendCall12)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall14)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQLegendCall15)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall16)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall18)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall20)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall21)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall22)(const void *, QGraphicsSceneMoveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall23)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall24)(const void *, QGraphicsSceneResizeEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall25)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall27)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall28)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall30)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall37)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall38)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall39)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall40)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall41)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall42)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQLegendCall43)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQLegendCall44)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall45)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall46)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall47)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall48)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall49)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall50)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall51)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall52)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall54)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall55)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall56)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall57)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQLegendCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQLegendCall59)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQLegendCall60)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQLegend : public QLegend {
public:
  using QLegend::QLegend;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9hideEventEP10QHideEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9showEventEP10QShowEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16windowFrameEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11changeEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget10closeEventEP11QCloseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget18focusNextPrevChildEb")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11polishEventEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent")) {
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
  //  void QLegend::paint(QPainter *painter, const QStyleOptionGraphicsItem
  //      *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLegendCall0 call = reinterpret_cast<CuteQLegendCall0>(taken[0]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QLegend::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QLegend::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLegendCall1 call = reinterpret_cast<CuteQLegendCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QLegend::hideEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QLegend::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLegendCall2 call = reinterpret_cast<CuteQLegendCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QLegend::showEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLegendCall3 call = reinterpret_cast<CuteQLegendCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsWidget::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsWidget::type() const
  int type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLegendCall4 call = reinterpret_cast<CuteQLegendCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paintWindowFrame(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLegendCall5 call = reinterpret_cast<CuteQLegendCall5>(taken[5]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsWidget::paintWindowFrame(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF QGraphicsWidget::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLegendCall6 call = reinterpret_cast<CuteQLegendCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsWidget::shape() const
  QPainterPath shape() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLegendCall7 call = reinterpret_cast<CuteQLegendCall7>(taken[7]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
  void initStyleOption(QStyleOption *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLegendCall8 call = reinterpret_cast<CuteQLegendCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQLegendCall9 call = reinterpret_cast<CuteQLegendCall9>(taken[9]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::updateGeometry()
  void updateGeometry() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLegendCall10 call = reinterpret_cast<CuteQLegendCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQLegendCall11 call = reinterpret_cast<CuteQLegendCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQLegendCall12 call = reinterpret_cast<CuteQLegendCall12>(taken[12]);
      const QVariant * given = call(this, &propertyName, &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::propertyChange(propertyName, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLegendCall13 call = reinterpret_cast<CuteQLegendCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
  bool windowFrameEvent(QEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLegendCall14 call = reinterpret_cast<CuteQLegendCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQLegendCall15 call = reinterpret_cast<CuteQLegendCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQLegendCall16 call = reinterpret_cast<CuteQLegendCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQLegendCall17 call = reinterpret_cast<CuteQLegendCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::changeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLegendCall18 call = reinterpret_cast<CuteQLegendCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::closeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLegendCall19 call = reinterpret_cast<CuteQLegendCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLegendCall20 call = reinterpret_cast<CuteQLegendCall20>(taken[20]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLegendCall21 call = reinterpret_cast<CuteQLegendCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
  void moveEvent(QGraphicsSceneMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLegendCall22 call = reinterpret_cast<CuteQLegendCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::moveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::polishEvent()
  void polishEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQLegendCall23 call = reinterpret_cast<CuteQLegendCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::polishEvent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
  void resizeEvent(QGraphicsSceneResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLegendCall24 call = reinterpret_cast<CuteQLegendCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::resizeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQLegendCall25 call = reinterpret_cast<CuteQLegendCall25>(taken[25]);
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
      CuteQLegendCall26 call = reinterpret_cast<CuteQLegendCall26>(taken[26]);
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
      CuteQLegendCall27 call = reinterpret_cast<CuteQLegendCall27>(taken[27]);
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
      CuteQLegendCall28 call = reinterpret_cast<CuteQLegendCall28>(taken[28]);
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
      CuteQLegendCall29 call = reinterpret_cast<CuteQLegendCall29>(taken[29]);
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
      CuteQLegendCall30 call = reinterpret_cast<CuteQLegendCall30>(taken[30]);
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
      CuteQLegendCall31 call = reinterpret_cast<CuteQLegendCall31>(taken[31]);
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
      CuteQLegendCall32 call = reinterpret_cast<CuteQLegendCall32>(taken[32]);
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
      CuteQLegendCall33 call = reinterpret_cast<CuteQLegendCall33>(taken[33]);
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
      CuteQLegendCall34 call = reinterpret_cast<CuteQLegendCall34>(taken[34]);
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
      CuteQLegendCall35 call = reinterpret_cast<CuteQLegendCall35>(taken[35]);
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
      CuteQLegendCall36 call = reinterpret_cast<CuteQLegendCall36>(taken[36]);
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
      CuteQLegendCall37 call = reinterpret_cast<CuteQLegendCall37>(taken[37]);
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
      CuteQLegendCall38 call = reinterpret_cast<CuteQLegendCall38>(taken[38]);
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
      CuteQLegendCall39 call = reinterpret_cast<CuteQLegendCall39>(taken[39]);
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
      CuteQLegendCall40 call = reinterpret_cast<CuteQLegendCall40>(taken[40]);
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
      CuteQLegendCall41 call = reinterpret_cast<CuteQLegendCall41>(taken[41]);
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
      CuteQLegendCall42 call = reinterpret_cast<CuteQLegendCall42>(taken[42]);
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
      CuteQLegendCall43 call = reinterpret_cast<CuteQLegendCall43>(taken[43]);
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
      CuteQLegendCall44 call = reinterpret_cast<CuteQLegendCall44>(taken[44]);
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
      CuteQLegendCall45 call = reinterpret_cast<CuteQLegendCall45>(taken[45]);
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
      CuteQLegendCall46 call = reinterpret_cast<CuteQLegendCall46>(taken[46]);
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
      CuteQLegendCall47 call = reinterpret_cast<CuteQLegendCall47>(taken[47]);
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
      CuteQLegendCall48 call = reinterpret_cast<CuteQLegendCall48>(taken[48]);
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
      CuteQLegendCall49 call = reinterpret_cast<CuteQLegendCall49>(taken[49]);
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
      CuteQLegendCall50 call = reinterpret_cast<CuteQLegendCall50>(taken[50]);
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
      CuteQLegendCall51 call = reinterpret_cast<CuteQLegendCall51>(taken[51]);
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
      CuteQLegendCall52 call = reinterpret_cast<CuteQLegendCall52>(taken[52]);
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
      CuteQLegendCall53 call = reinterpret_cast<CuteQLegendCall53>(taken[53]);
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
      CuteQLegendCall54 call = reinterpret_cast<CuteQLegendCall54>(taken[54]);
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
      CuteQLegendCall55 call = reinterpret_cast<CuteQLegendCall55>(taken[55]);
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
      CuteQLegendCall56 call = reinterpret_cast<CuteQLegendCall56>(taken[56]);
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
      CuteQLegendCall57 call = reinterpret_cast<CuteQLegendCall57>(taken[57]);
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
      CuteQLegendCall58 call = reinterpret_cast<CuteQLegendCall58>(taken[58]);
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
      CuteQLegendCall59 call = reinterpret_cast<CuteQLegendCall59>(taken[59]);
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
      CuteQLegendCall60 call = reinterpret_cast<CuteQLegendCall60>(taken[60]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *QLegend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QLegend10metaObjectEv(const QLegend *self) {
  return self->metaObject();
}

//  QString QLegend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLegend2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLegend::tr(s, c, n));
}

//  QLegend::QLegend(QChart *chart)
extern "C" Q_DECL_EXPORT
QLegend *ritual_ZN7QLegendC1EP6QChart(QChart *chart) {
  return new CuteQLegend(chart);
}

//  QLegend::~QLegend()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegendD1Ev(QLegend *self) {
  delete self;
}

//  void QLegend::paint(QPainter *painter, const QStyleOptionGraphicsItem
//      *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QLegend *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void QLegend::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend8setBrushERK6QBrush(
    QLegend *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QLegend::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK7QLegend5brushEv(const QLegend *self) {
  return new QBrush(self->brush());
}

//  void QLegend::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend8setColorE6QColor(QLegend *self, const QColor *color) {
  self->setColor(*color);
}

//  QColor QLegend::color()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN7QLegend5colorEv(QLegend *self) {
  return new QColor(self->color());
}

//  void QLegend::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend6setPenERK4QPen(QLegend *self, const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QLegend::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK7QLegend3penEv(const QLegend *self) {
  return new QPen(self->pen());
}

//  void QLegend::setBorderColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend14setBorderColorE6QColor(
    QLegend *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  QColor QLegend::borderColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN7QLegend11borderColorEv(QLegend *self) {
  return new QColor(self->borderColor());
}

//  void QLegend::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend7setFontERK5QFont(QLegend *self, const QFont *font) {
  self->setFont(*font);
}

//  QFont QLegend::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK7QLegend4fontEv(const QLegend *self) {
  return new QFont(self->font());
}

//  void QLegend::setLabelBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend13setLabelBrushERK6QBrush(
    QLegend *self,
    const QBrush *brush) {
  self->setLabelBrush(*brush);
}

//  QBrush QLegend::labelBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK7QLegend10labelBrushEv(const QLegend *self) {
  return new QBrush(self->labelBrush());
}

//  void QLegend::setLabelColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend13setLabelColorE6QColor(
    QLegend *self,
    const QColor *color) {
  self->setLabelColor(*color);
}

//  QColor QLegend::labelColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QLegend10labelColorEv(const QLegend *self) {
  return new QColor(self->labelColor());
}

//  void QLegend::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLegend *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QLegend::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLegend9alignmentEv(const QLegend *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLegend::detachFromChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend15detachFromChartEv(QLegend *self) {
  self->detachFromChart();
}

//  void QLegend::attachToChart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend13attachToChartEv(QLegend *self) {
  self->attachToChart();
}

//  bool QLegend::isAttachedToChart()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLegend17isAttachedToChartEv(QLegend *self) {
  return self->isAttachedToChart();
}

//  void QLegend::setBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend20setBackgroundVisibleEb(QLegend *self, bool visible) {
  self->setBackgroundVisible(visible);
}

//  bool QLegend::isBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLegend19isBackgroundVisibleEv(const QLegend *self) {
  return self->isBackgroundVisible();
}

//  QList<QLegendMarker *> QLegend::markers(QAbstractSeries *series) const
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZNK7QLegend7markersEP15QAbstractSeries(
    const QLegend *self,
    QAbstractSeries *series) {
  return new QList<QLegendMarker *>(self->markers(series));
}

//  bool QLegend::reverseMarkers()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QLegend14reverseMarkersEv(QLegend *self) {
  return self->reverseMarkers();
}

//  void QLegend::setReverseMarkers(bool reverseMarkers)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend17setReverseMarkersEb(
    QLegend *self,
    bool reverseMarkers) {
  self->setReverseMarkers(reverseMarkers);
}

//  bool QLegend::showToolTips() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLegend12showToolTipsEv(const QLegend *self) {
  return self->showToolTips();
}

//  void QLegend::setShowToolTips(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend15setShowToolTipsEb(QLegend *self, bool show) {
  self->setShowToolTips(show);
}

//  bool QLegend::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLegend13isInteractiveEv(const QLegend *self) {
  return self->isInteractive();
}

//  void QLegend::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend14setInteractiveEb(QLegend *self, bool interactive) {
  self->setInteractive(interactive);
}

//  MarkerShape QLegend::markerShape() const
extern "C" Q_DECL_EXPORT
QLegend::MarkerShape ritual_ZNK7QLegend11markerShapeEv(const QLegend *self) {
  return self->markerShape();
}

//  void QLegend::setMarkerShape(MarkerShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend14setMarkerShapeENS_11MarkerShapeE(
    QLegend *self,
    QLegend::MarkerShape shape) {
  self->setMarkerShape(shape);
}

//  void QLegend::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend9hideEventEP10QHideEvent(
    QLegend *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void QLegend::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLegend9showEventEP10QShowEvent(
    QLegend *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  a Python function taken by a CuteQLegend, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLegend(QLegend *self, const char *key, void *call) {
  return static_cast<CuteQLegend *>(self)->take(key, call);
}

//  void QLegend::paint(QPainter *painter, const QStyleOptionGraphicsItem
//      *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLegend5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QLegend *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QLegend::paint(painter, option, widget);
}

//  void QLegend::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLegend9hideEventEP10QHideEvent(
    QLegend *self,
    QHideEvent *event) {
  static_cast<OwnQLegend *>(self)->OwnQLegend::hideEvent(event);
}

//  void QLegend::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QLegend9showEventEP10QShowEvent(
    QLegend *self,
    QShowEvent *event) {
  static_cast<OwnQLegend *>(self)->OwnQLegend::showEvent(event);
}
