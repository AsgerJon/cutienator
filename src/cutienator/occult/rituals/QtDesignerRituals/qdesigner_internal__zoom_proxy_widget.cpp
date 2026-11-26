//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on qdesigner_internal::ZoomProxyWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_ZoomProxyWidget : qdesigner_internal::ZoomProxyWidget {
  using qdesigner_internal::ZoomProxyWidget::itemChange;
};

//  A qdesigner_internal::ZoomProxyWidget that Python can take functions over in. Every qdesigner_internal::ZoomProxyWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*Cuteqdesigner_internal_ZoomProxyWidgetCall0)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall1)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*Cuteqdesigner_internal_ZoomProxyWidgetCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall5)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall6)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall7)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall8)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall9)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall10)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall11)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall12)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall13)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall14)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall15)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall16)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall18)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall19)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall20)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall21)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall22)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall23)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall24)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall25)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall26)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall27)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*Cuteqdesigner_internal_ZoomProxyWidgetCall28)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall29)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*Cuteqdesigner_internal_ZoomProxyWidgetCall30)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall31)(const void *, QGraphicsSceneResizeEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall32)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*Cuteqdesigner_internal_ZoomProxyWidgetCall33)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*Cuteqdesigner_internal_ZoomProxyWidgetCall34)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall35)(const void *, QStyleOption *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall36)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*Cuteqdesigner_internal_ZoomProxyWidgetCall37)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall38)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall39)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*Cuteqdesigner_internal_ZoomProxyWidgetCall40)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall41)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall42)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall43)(const void *, QGraphicsSceneMoveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall44)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall45)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall46)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall47)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall48)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall49)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall52)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*Cuteqdesigner_internal_ZoomProxyWidgetCall53)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall54)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall55)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall56)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall57)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*Cuteqdesigner_internal_ZoomProxyWidgetCall58)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*Cuteqdesigner_internal_ZoomProxyWidgetCall59)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*Cuteqdesigner_internal_ZoomProxyWidgetCall60)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class Cuteqdesigner_internal_ZoomProxyWidget : public qdesigner_internal::ZoomProxyWidget {
public:
  using qdesigner_internal::ZoomProxyWidget::ZoomProxyWidget;
  void *taken[61] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10itemChangeENS_18GraphicsItemChangeERK8QVariant")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
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
    if (!std::strcmp(key, "_ZNK13QGraphicsItem4typeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9showEventEP10QShowEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9hideEventEP10QHideEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QGraphicsItem9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverEnterEventEP24QGraphicsSceneHoverEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14hoverMoveEventEP24QGraphicsSceneHoverEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14grabMouseEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13keyPressEventEP9QKeyEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget18focusNextPrevChildEb")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16inputMethodEventEP17QInputMethodEvent")) {
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
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12boundingRectEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem5shapeEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem10sceneEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget16windowFrameEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11changeEventEP6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget10closeEventEP11QCloseEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget11polishEventEv")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem7advanceEi")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem8containsERK7QPointF")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithItemEPKS_N2Qt17ItemSelectionModeE")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem16collidesWithPathERK12QPainterPathN2Qt17ItemSelectionModeE")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem12isObscuredByEPKS_")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK13QGraphicsItem10opaqueAreaEv")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsItem16sceneEventFilterEPS_P6QEvent")) {
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
  //  QVariant
  //      qdesigner_internal::ZoomProxyWidget::itemChange(GraphicsItemChang
  //      e change, const QVariant &value)
  QVariant itemChange(
      QGraphicsItem::GraphicsItemChange change,
      const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall0 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(change), &value, &handled);
      if (handled && given) return *given;
    }
    return qdesigner_internal::ZoomProxyWidget::itemChange(change, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall1 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall1>(taken[1]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::paint(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paint(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall2 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall2>(taken[2]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::paint(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsProxyWidget::type() const
  int type() const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall3 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::type();
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsProxyWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall4 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::event(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsProxyWidget::eventFilter(QObject *object, QEvent
  //      *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall5 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall5>(taken[5]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::eventFilter(object, event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall6 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::showEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall7 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hideEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if !defined(QT_NO_CONTEXTMENU)
  //  void
  //      QGraphicsProxyWidget::contextMenuEvent(QGraphicsSceneContextMenuE
  //      vent *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall8 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
  //  void QGraphicsProxyWidget::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall9 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
  //  void QGraphicsProxyWidget::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall10 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
  //  void QGraphicsProxyWidget::dragMoveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall11 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if QT_CONFIG(draganddrop)
  //  void QGraphicsProxyWidget::dropEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall12 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::hoverEnterEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall13 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall14 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::hoverMoveEvent(QGraphicsSceneHoverEvent
  //      *event)
  void hoverMoveEvent(QGraphicsSceneHoverEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall15 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::hoverMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::grabMouseEvent(QEvent *event)
  void grabMouseEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall16 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::grabMouseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::ungrabMouseEvent(QEvent *event)
  void ungrabMouseEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall17 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::ungrabMouseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::mouseMoveEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall18 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::mousePressEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall19 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mousePressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall20 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void
  //      QGraphicsProxyWidget::mouseDoubleClickEvent(QGraphicsSceneMouseEv
  //      ent *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall21 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
#if QT_CONFIG(wheelevent)
  //  void QGraphicsProxyWidget::wheelEvent(QGraphicsSceneWheelEvent
  //      *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall22 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall23 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall24 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall25 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall26 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsProxyWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall27 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall27>(taken[27]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidget::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsProxyWidget::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall28 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall28>(taken[28]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsProxyWidget::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall29 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsProxyWidget::sizeHint(Qt::SizeHint which, const
  //      QSizeF &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall30 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall30>(taken[30]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsProxyWidget::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsProxyWidget::resizeEvent(QGraphicsSceneResizeEvent
  //      *event)
  void resizeEvent(QGraphicsSceneResizeEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall31 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsProxyWidget::resizeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
  //      QStyleOptionGraphicsItem *option, QWidget *widget)
  void paintWindowFrame(
      QPainter *painter,
      const QStyleOptionGraphicsItem *option,
      QWidget *widget) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall32 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall32>(taken[32]);
      call(this, painter, option, widget, &handled);
      if (handled) return;
    }
    QGraphicsWidget::paintWindowFrame(painter, option, widget);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QRectF QGraphicsWidget::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall33 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall33>(taken[33]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::boundingRect();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsWidget::shape() const
  QPainterPath shape() const override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall34 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall34>(taken[34]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::shape();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
  void initStyleOption(QStyleOption *option) const override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall35 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall35>(taken[35]);
      call(this, option, &handled);
      if (handled) return;
    }
    QGraphicsWidget::initStyleOption(option);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::updateGeometry()
  void updateGeometry() override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall36 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
  //      const QVariant &value)
  QVariant propertyChange(
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall37 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall37>(taken[37]);
      const QVariant * given = call(this, &propertyName, &value, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsWidget::propertyChange(propertyName, value);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::sceneEvent(QEvent *event)
  bool sceneEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall38 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsWidget::sceneEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
  bool windowFrameEvent(QEvent *e) override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall39 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall40 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall40>(taken[40]);
      int given = call(this, &pos, &handled);
      if (handled) return static_cast<Qt::WindowFrameSection>(given);
    }
    return QGraphicsWidget::windowFrameSectionAt(pos);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall41 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::changeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall42 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::closeEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
  void moveEvent(QGraphicsSceneMoveEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall43 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::moveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::polishEvent()
  void polishEvent() override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall44 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidget::polishEvent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
  void grabKeyboardEvent(QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall45 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::grabKeyboardEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
  void ungrabKeyboardEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall46 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsWidget::ungrabKeyboardEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall47 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall48 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall49 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall50 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall51 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[52]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall52 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall52>(taken[52]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItem::advance(int phase)
  void advance(int phase) override {
    if (taken[53]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall53 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall53>(taken[53]);
      call(this, phase, &handled);
      if (handled) return;
    }
    QGraphicsItem::advance(phase);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[54]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall54 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall54>(taken[54]);
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
    if (taken[55]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall55 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall55>(taken[55]);
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
    if (taken[56]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall56 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall56>(taken[56]);
      bool given = call(this, &path, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QGraphicsItem::collidesWithPath(path, mode);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItem::isObscuredBy(const QGraphicsItem *item) const
  bool isObscuredBy(const QGraphicsItem *item) const override {
    if (taken[57]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall57 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall57>(taken[57]);
      bool given = call(this, item, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::isObscuredBy(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QPainterPath QGraphicsItem::opaqueArea() const
  QPainterPath opaqueArea() const override {
    if (taken[58]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall58 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall58>(taken[58]);
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
    if (taken[59]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall59 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall59>(taken[59]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsItem::sceneEventFilter(watched, event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsItem::extension(const QVariant &variant) const
  QVariant extension(const QVariant &variant) const override {
    if (taken[60]) {
      int handled = 0;
      Cuteqdesigner_internal_ZoomProxyWidgetCall60 call = reinterpret_cast<Cuteqdesigner_internal_ZoomProxyWidgetCall60>(taken[60]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  qdesigner_internal::ZoomProxyWidget::ZoomProxyWidget(QGraphicsItem
//      *parent, Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ZoomProxyWidget *ritual_ZN18qdesigner_internal15ZoomProxyWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new Cuteqdesigner_internal_ZoomProxyWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QVariant
//      qdesigner_internal::ZoomProxyWidget::itemChange(GraphicsItemChange
//      change, const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18qdesigner_internal15ZoomProxyWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    qdesigner_internal::ZoomProxyWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(self->itemChange(change, *value));
}

//  a Python function taken by a Cuteqdesigner_internal_ZoomProxyWidget, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_ZoomProxyWidget(
    qdesigner_internal::ZoomProxyWidget *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_ZoomProxyWidget *>(self)->take(key, call);
}

//  QVariant
//      qdesigner_internal::ZoomProxyWidget::itemChange(GraphicsItemChange
//      change, const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN18qdesigner_internal15ZoomProxyWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    qdesigner_internal::ZoomProxyWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(
      static_cast<Ownqdesigner_internal_ZoomProxyWidget *>(self)->Ownqdesigner_internal_ZoomProxyWidget::itemChange(
          change,
          *value));
}
