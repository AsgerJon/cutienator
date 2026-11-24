//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicswidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicswidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qaction.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QGraphicsWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsWidget : QGraphicsWidget {
  using QGraphicsWidget::initStyleOption;
  using QGraphicsWidget::sizeHint;
  using QGraphicsWidget::updateGeometry;
  using QGraphicsWidget::itemChange;
  using QGraphicsWidget::propertyChange;
  using QGraphicsWidget::sceneEvent;
  using QGraphicsWidget::windowFrameEvent;
  using QGraphicsWidget::windowFrameSectionAt;
  using QGraphicsWidget::event;
  using QGraphicsWidget::changeEvent;
  using QGraphicsWidget::closeEvent;
  using QGraphicsWidget::focusInEvent;
  using QGraphicsWidget::focusNextPrevChild;
  using QGraphicsWidget::focusOutEvent;
  using QGraphicsWidget::hideEvent;
  using QGraphicsWidget::moveEvent;
  using QGraphicsWidget::polishEvent;
  using QGraphicsWidget::resizeEvent;
  using QGraphicsWidget::showEvent;
  using QGraphicsWidget::hoverMoveEvent;
  using QGraphicsWidget::hoverLeaveEvent;
  using QGraphicsWidget::grabMouseEvent;
  using QGraphicsWidget::ungrabMouseEvent;
  using QGraphicsWidget::grabKeyboardEvent;
  using QGraphicsWidget::ungrabKeyboardEvent;
};

//  A QGraphicsWidget that Python can take functions over in. Every QGraphicsWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsWidgetCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall2)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall3)(const void *, QPainter *, const QStyleOptionGraphicsItem *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteQGraphicsWidgetCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsWidgetCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall6)(const void *, QStyleOption *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQGraphicsWidgetCall7)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsWidgetCall9)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsWidgetCall10)(const void *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsWidgetCall13)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall14)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall16)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall17)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall18)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall20)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall21)(const void *, QGraphicsSceneMoveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall22)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall23)(const void *, QGraphicsSceneResizeEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall24)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall25)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall26)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall27)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall28)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall30)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsWidgetCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsWidgetCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsWidgetCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsWidgetCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsWidgetCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsWidgetCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall37)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall38)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall39)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall40)(const void *, const QGraphicsItem *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall41)(const void *, const QPainterPath *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall42)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QPainterPath * (*CuteQGraphicsWidgetCall43)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetCall44)(const void *, QGraphicsItem *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall45)(const void *, QGraphicsSceneContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall46)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall47)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall48)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall49)(const void *, QGraphicsSceneDragDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall50)(const void *, QGraphicsSceneHoverEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall51)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall52)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall53)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall54)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall55)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall56)(const void *, QGraphicsSceneMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall57)(const void *, QGraphicsSceneWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsWidgetCall59)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQGraphicsWidgetCall60)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsWidget : public QGraphicsWidget {
public:
  using QGraphicsWidget::QGraphicsWidget;
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
      CuteQGraphicsWidgetCall0 call = reinterpret_cast<CuteQGraphicsWidgetCall0>(taken[0]);
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
      CuteQGraphicsWidgetCall1 call = reinterpret_cast<CuteQGraphicsWidgetCall1>(taken[1]);
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
      CuteQGraphicsWidgetCall2 call = reinterpret_cast<CuteQGraphicsWidgetCall2>(taken[2]);
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
      CuteQGraphicsWidgetCall3 call = reinterpret_cast<CuteQGraphicsWidgetCall3>(taken[3]);
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
      CuteQGraphicsWidgetCall4 call = reinterpret_cast<CuteQGraphicsWidgetCall4>(taken[4]);
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
      CuteQGraphicsWidgetCall5 call = reinterpret_cast<CuteQGraphicsWidgetCall5>(taken[5]);
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
      CuteQGraphicsWidgetCall6 call = reinterpret_cast<CuteQGraphicsWidgetCall6>(taken[6]);
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
      CuteQGraphicsWidgetCall7 call = reinterpret_cast<CuteQGraphicsWidgetCall7>(taken[7]);
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
      CuteQGraphicsWidgetCall8 call = reinterpret_cast<CuteQGraphicsWidgetCall8>(taken[8]);
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
      CuteQGraphicsWidgetCall9 call = reinterpret_cast<CuteQGraphicsWidgetCall9>(taken[9]);
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
      CuteQGraphicsWidgetCall10 call = reinterpret_cast<CuteQGraphicsWidgetCall10>(taken[10]);
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
      CuteQGraphicsWidgetCall11 call = reinterpret_cast<CuteQGraphicsWidgetCall11>(taken[11]);
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
      CuteQGraphicsWidgetCall12 call = reinterpret_cast<CuteQGraphicsWidgetCall12>(taken[12]);
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
      CuteQGraphicsWidgetCall13 call = reinterpret_cast<CuteQGraphicsWidgetCall13>(taken[13]);
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
      CuteQGraphicsWidgetCall14 call = reinterpret_cast<CuteQGraphicsWidgetCall14>(taken[14]);
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
      CuteQGraphicsWidgetCall15 call = reinterpret_cast<CuteQGraphicsWidgetCall15>(taken[15]);
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
      CuteQGraphicsWidgetCall16 call = reinterpret_cast<CuteQGraphicsWidgetCall16>(taken[16]);
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
      CuteQGraphicsWidgetCall17 call = reinterpret_cast<CuteQGraphicsWidgetCall17>(taken[17]);
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
      CuteQGraphicsWidgetCall18 call = reinterpret_cast<CuteQGraphicsWidgetCall18>(taken[18]);
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
      CuteQGraphicsWidgetCall19 call = reinterpret_cast<CuteQGraphicsWidgetCall19>(taken[19]);
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
      CuteQGraphicsWidgetCall20 call = reinterpret_cast<CuteQGraphicsWidgetCall20>(taken[20]);
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
      CuteQGraphicsWidgetCall21 call = reinterpret_cast<CuteQGraphicsWidgetCall21>(taken[21]);
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
      CuteQGraphicsWidgetCall22 call = reinterpret_cast<CuteQGraphicsWidgetCall22>(taken[22]);
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
      CuteQGraphicsWidgetCall23 call = reinterpret_cast<CuteQGraphicsWidgetCall23>(taken[23]);
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
      CuteQGraphicsWidgetCall24 call = reinterpret_cast<CuteQGraphicsWidgetCall24>(taken[24]);
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
      CuteQGraphicsWidgetCall25 call = reinterpret_cast<CuteQGraphicsWidgetCall25>(taken[25]);
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
      CuteQGraphicsWidgetCall26 call = reinterpret_cast<CuteQGraphicsWidgetCall26>(taken[26]);
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
      CuteQGraphicsWidgetCall27 call = reinterpret_cast<CuteQGraphicsWidgetCall27>(taken[27]);
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
      CuteQGraphicsWidgetCall28 call = reinterpret_cast<CuteQGraphicsWidgetCall28>(taken[28]);
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
      CuteQGraphicsWidgetCall29 call = reinterpret_cast<CuteQGraphicsWidgetCall29>(taken[29]);
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
      CuteQGraphicsWidgetCall30 call = reinterpret_cast<CuteQGraphicsWidgetCall30>(taken[30]);
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
      CuteQGraphicsWidgetCall31 call = reinterpret_cast<CuteQGraphicsWidgetCall31>(taken[31]);
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
      CuteQGraphicsWidgetCall32 call = reinterpret_cast<CuteQGraphicsWidgetCall32>(taken[32]);
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
      CuteQGraphicsWidgetCall33 call = reinterpret_cast<CuteQGraphicsWidgetCall33>(taken[33]);
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
      CuteQGraphicsWidgetCall34 call = reinterpret_cast<CuteQGraphicsWidgetCall34>(taken[34]);
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
      CuteQGraphicsWidgetCall35 call = reinterpret_cast<CuteQGraphicsWidgetCall35>(taken[35]);
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
      CuteQGraphicsWidgetCall36 call = reinterpret_cast<CuteQGraphicsWidgetCall36>(taken[36]);
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
      CuteQGraphicsWidgetCall37 call = reinterpret_cast<CuteQGraphicsWidgetCall37>(taken[37]);
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
      CuteQGraphicsWidgetCall38 call = reinterpret_cast<CuteQGraphicsWidgetCall38>(taken[38]);
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
      CuteQGraphicsWidgetCall39 call = reinterpret_cast<CuteQGraphicsWidgetCall39>(taken[39]);
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
      CuteQGraphicsWidgetCall40 call = reinterpret_cast<CuteQGraphicsWidgetCall40>(taken[40]);
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
      CuteQGraphicsWidgetCall41 call = reinterpret_cast<CuteQGraphicsWidgetCall41>(taken[41]);
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
      CuteQGraphicsWidgetCall42 call = reinterpret_cast<CuteQGraphicsWidgetCall42>(taken[42]);
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
      CuteQGraphicsWidgetCall43 call = reinterpret_cast<CuteQGraphicsWidgetCall43>(taken[43]);
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
      CuteQGraphicsWidgetCall44 call = reinterpret_cast<CuteQGraphicsWidgetCall44>(taken[44]);
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
      CuteQGraphicsWidgetCall45 call = reinterpret_cast<CuteQGraphicsWidgetCall45>(taken[45]);
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
      CuteQGraphicsWidgetCall46 call = reinterpret_cast<CuteQGraphicsWidgetCall46>(taken[46]);
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
      CuteQGraphicsWidgetCall47 call = reinterpret_cast<CuteQGraphicsWidgetCall47>(taken[47]);
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
      CuteQGraphicsWidgetCall48 call = reinterpret_cast<CuteQGraphicsWidgetCall48>(taken[48]);
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
      CuteQGraphicsWidgetCall49 call = reinterpret_cast<CuteQGraphicsWidgetCall49>(taken[49]);
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
      CuteQGraphicsWidgetCall50 call = reinterpret_cast<CuteQGraphicsWidgetCall50>(taken[50]);
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
      CuteQGraphicsWidgetCall51 call = reinterpret_cast<CuteQGraphicsWidgetCall51>(taken[51]);
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
      CuteQGraphicsWidgetCall52 call = reinterpret_cast<CuteQGraphicsWidgetCall52>(taken[52]);
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
      CuteQGraphicsWidgetCall53 call = reinterpret_cast<CuteQGraphicsWidgetCall53>(taken[53]);
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
      CuteQGraphicsWidgetCall54 call = reinterpret_cast<CuteQGraphicsWidgetCall54>(taken[54]);
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
      CuteQGraphicsWidgetCall55 call = reinterpret_cast<CuteQGraphicsWidgetCall55>(taken[55]);
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
      CuteQGraphicsWidgetCall56 call = reinterpret_cast<CuteQGraphicsWidgetCall56>(taken[56]);
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
      CuteQGraphicsWidgetCall57 call = reinterpret_cast<CuteQGraphicsWidgetCall57>(taken[57]);
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
      CuteQGraphicsWidgetCall58 call = reinterpret_cast<CuteQGraphicsWidgetCall58>(taken[58]);
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
      CuteQGraphicsWidgetCall59 call = reinterpret_cast<CuteQGraphicsWidgetCall59>(taken[59]);
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
      CuteQGraphicsWidgetCall60 call = reinterpret_cast<CuteQGraphicsWidgetCall60>(taken[60]);
      const QVariant * given = call(this, &variant, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsItem::extension(variant);
  }
#endif  // QT_CONFIG(graphicsview)
};

//  const QMetaObject *QGraphicsWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsWidget10metaObjectEv(
    const QGraphicsWidget *self) {
  return self->metaObject();
}

//  QString QGraphicsWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsWidget::tr(s, c, n));
}

//  QGraphicsWidget::QGraphicsWidget(QGraphicsItem *parent, Qt::WindowFlags
//      wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZN15QGraphicsWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new CuteQGraphicsWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsWidget::~QGraphicsWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidgetD1Ev(QGraphicsWidget *self) {
  delete self;
}

//  QGraphicsLayout *QGraphicsWidget::layout() const
extern "C" Q_DECL_EXPORT
QGraphicsLayout *ritual_ZNK15QGraphicsWidget6layoutEv(
    const QGraphicsWidget *self) {
  return self->layout();
}

//  void QGraphicsWidget::setLayout(QGraphicsLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9setLayoutEP15QGraphicsLayout(
    QGraphicsWidget *self,
    QGraphicsLayout *layout) {
  self->setLayout(layout);
}

//  void QGraphicsWidget::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10adjustSizeEv(QGraphicsWidget *self) {
  self->adjustSize();
}

//  Qt::LayoutDirection QGraphicsWidget::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK15QGraphicsWidget15layoutDirectionEv(
    const QGraphicsWidget *self) {
  return self->layoutDirection();
}

//  void QGraphicsWidget::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QGraphicsWidget *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  void QGraphicsWidget::unsetLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget20unsetLayoutDirectionEv(
    QGraphicsWidget *self) {
  self->unsetLayoutDirection();
}

//  QStyle *QGraphicsWidget::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK15QGraphicsWidget5styleEv(const QGraphicsWidget *self) {
  return self->style();
}

//  void QGraphicsWidget::setStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget8setStyleEP6QStyle(
    QGraphicsWidget *self,
    QStyle *style) {
  self->setStyle(style);
}

//  QFont QGraphicsWidget::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QGraphicsWidget4fontEv(const QGraphicsWidget *self) {
  return new QFont(self->font());
}

//  void QGraphicsWidget::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget7setFontERK5QFont(
    QGraphicsWidget *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QPalette QGraphicsWidget::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK15QGraphicsWidget7paletteEv(
    const QGraphicsWidget *self) {
  return new QPalette(self->palette());
}

//  void QGraphicsWidget::setPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10setPaletteERK8QPalette(
    QGraphicsWidget *self,
    const QPalette *palette) {
  self->setPalette(*palette);
}

//  bool QGraphicsWidget::autoFillBackground() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget18autoFillBackgroundEv(
    const QGraphicsWidget *self) {
  return self->autoFillBackground();
}

//  void QGraphicsWidget::setAutoFillBackground(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setAutoFillBackgroundEb(
    QGraphicsWidget *self,
    bool enabled) {
  self->setAutoFillBackground(enabled);
}

//  void QGraphicsWidget::resize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget6resizeERK6QSizeF(
    QGraphicsWidget *self,
    const QSizeF *size) {
  self->resize(*size);
}

//  void QGraphicsWidget::resize(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget6resizeEdd(
    QGraphicsWidget *self,
    qreal w,
    qreal h) {
  self->resize(w, h);
}

//  QSizeF QGraphicsWidget::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QGraphicsWidget4sizeEv(const QGraphicsWidget *self) {
  return new QSizeF(self->size());
}

//  void QGraphicsWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setGeometryERK6QRectF(
    QGraphicsWidget *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void QGraphicsWidget::setGeometry(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setGeometryEdddd(
    QGraphicsWidget *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setGeometry(x, y, w, h);
}

//  QRectF QGraphicsWidget::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget4rectEv(const QGraphicsWidget *self) {
  return new QRectF(self->rect());
}

//  void QGraphicsWidget::setContentsMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setContentsMarginsEdddd(
    QGraphicsWidget *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setContentsMargins(QMarginsF margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setContentsMarginsE9QMarginsF(
    QGraphicsWidget *self,
    const QMarginsF *margins) {
  self->setContentsMargins(*margins);
}

//  void QGraphicsWidget::getContentsMargins(qreal *left, qreal *top, qreal
//      *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsWidget18getContentsMarginsEPdS0_S0_S0_(
    const QGraphicsWidget *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setWindowFrameMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setWindowFrameMarginsEdddd(
    QGraphicsWidget *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setWindowFrameMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setWindowFrameMargins(QMarginsF margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setWindowFrameMarginsE9QMarginsF(
    QGraphicsWidget *self,
    const QMarginsF *margins) {
  self->setWindowFrameMargins(*margins);
}

//  void QGraphicsWidget::getWindowFrameMargins(qreal *left, qreal *top,
//      qreal *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsWidget21getWindowFrameMarginsEPdS0_S0_S0_(
    const QGraphicsWidget *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getWindowFrameMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::unsetWindowFrameMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget23unsetWindowFrameMarginsEv(
    QGraphicsWidget *self) {
  self->unsetWindowFrameMargins();
}

//  QRectF QGraphicsWidget::windowFrameGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget19windowFrameGeometryEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->windowFrameGeometry());
}

//  QRectF QGraphicsWidget::windowFrameRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget15windowFrameRectEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->windowFrameRect());
}

//  Qt::WindowFlags QGraphicsWidget::windowFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsWidget11windowFlagsEv(const QGraphicsWidget *self) {
  return static_cast<int>(self->windowFlags().toInt());
}

//  Qt::WindowType QGraphicsWidget::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK15QGraphicsWidget10windowTypeEv(
    const QGraphicsWidget *self) {
  return self->windowType();
}

//  void QGraphicsWidget::setWindowFlags(Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsWidget *self,
    int wFlags) {
  self->setWindowFlags(QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  bool QGraphicsWidget::isActiveWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget14isActiveWindowEv(
    const QGraphicsWidget *self) {
  return self->isActiveWindow();
}

//  void QGraphicsWidget::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setWindowTitleERK7QString(
    QGraphicsWidget *self,
    const QString *title) {
  self->setWindowTitle(*title);
}

//  QString QGraphicsWidget::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QGraphicsWidget11windowTitleEv(
    const QGraphicsWidget *self) {
  return new QString(self->windowTitle());
}

//  Qt::FocusPolicy QGraphicsWidget::focusPolicy() const
extern "C" Q_DECL_EXPORT
Qt::FocusPolicy ritual_ZNK15QGraphicsWidget11focusPolicyEv(
    const QGraphicsWidget *self) {
  return self->focusPolicy();
}

//  void QGraphicsWidget::setFocusPolicy(Qt::FocusPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setFocusPolicyEN2Qt11FocusPolicyE(
    QGraphicsWidget *self,
    Qt::FocusPolicy policy) {
  self->setFocusPolicy(policy);
}

//  void QGraphicsWidget::setTabOrder(QGraphicsWidget *first, QGraphicsWidget
//      *second)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setTabOrderEPS_S0_(
    QGraphicsWidget *first,
    QGraphicsWidget *second) {
  QGraphicsWidget::setTabOrder(first, second);
}

//  QGraphicsWidget *QGraphicsWidget::focusWidget() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK15QGraphicsWidget11focusWidgetEv(
    const QGraphicsWidget *self) {
  return self->focusWidget();
}

#if !defined(QT_NO_SHORTCUT)
//  int QGraphicsWidget::grabShortcut(const QKeySequence &sequence,
//      Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGraphicsWidget12grabShortcutERK12QKeySequenceN2Qt15ShortcutContextE(
    QGraphicsWidget *self,
    const QKeySequence *sequence,
    Qt::ShortcutContext context) {
  return self->grabShortcut(*sequence, context);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  void QGraphicsWidget::releaseShortcut(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget15releaseShortcutEi(
    QGraphicsWidget *self,
    int id) {
  self->releaseShortcut(id);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  void QGraphicsWidget::setShortcutEnabled(int id, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setShortcutEnabledEib(
    QGraphicsWidget *self,
    int id,
    bool enabled) {
  self->setShortcutEnabled(id, enabled);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  void QGraphicsWidget::setShortcutAutoRepeat(int id, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setShortcutAutoRepeatEib(
    QGraphicsWidget *self,
    int id,
    bool enabled) {
  self->setShortcutAutoRepeat(id, enabled);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_ACTION)
//  void QGraphicsWidget::addAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9addActionEP7QAction(
    QGraphicsWidget *self,
    QAction *action) {
  self->addAction(action);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  void QGraphicsWidget::addActions(const QList<QAction *> &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10addActionsERK5QListIP7QActionE(
    QGraphicsWidget *self,
    const QList<QAction *> *actions) {
  self->addActions(*actions);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  void QGraphicsWidget::insertActions(QAction *before, const QList<QAction
//      *> &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget13insertActionsEP7QActionRK5QListIS1_E(
    QGraphicsWidget *self,
    QAction *before,
    const QList<QAction *> *actions) {
  self->insertActions(before, *actions);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  void QGraphicsWidget::insertAction(QAction *before, QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12insertActionEP7QActionS1_(
    QGraphicsWidget *self,
    QAction *before,
    QAction *action) {
  self->insertAction(before, action);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  void QGraphicsWidget::removeAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12removeActionEP7QAction(
    QGraphicsWidget *self,
    QAction *action) {
  self->removeAction(action);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  QList<QAction *> QGraphicsWidget::actions() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK15QGraphicsWidget7actionsEv(
    const QGraphicsWidget *self) {
  return new QList<QAction *>(self->actions());
}
#endif  // !defined(QT_NO_ACTION)

//  void QGraphicsWidget::setAttribute(Qt::WidgetAttribute attribute, bool
//      on)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12setAttributeEN2Qt15WidgetAttributeEb(
    QGraphicsWidget *self,
    Qt::WidgetAttribute attribute,
    bool on) {
  self->setAttribute(attribute, on);
}

//  bool QGraphicsWidget::testAttribute(Qt::WidgetAttribute attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget13testAttributeEN2Qt15WidgetAttributeE(
    const QGraphicsWidget *self,
    Qt::WidgetAttribute attribute) {
  return self->testAttribute(attribute);
}

//  int QGraphicsWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsWidget4typeEv(const QGraphicsWidget *self) {
  return self->type();
}

//  void QGraphicsWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paintWindowFrame(painter, option, widget);
}

//  QRectF QGraphicsWidget::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget12boundingRectEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsWidget::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15QGraphicsWidget5shapeEv(
    const QGraphicsWidget *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsWidget::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget5closeEv(QGraphicsWidget *self) {
  return self->close();
}

//  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption(
    const QGraphicsWidget *self,
    QStyleOption *option) {
  self->initStyleOption(option);
}

//  QSizeF QGraphicsWidget::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QGraphicsWidget8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsWidget *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void QGraphicsWidget::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14updateGeometryEv(QGraphicsWidget *self) {
  self->updateGeometry();
}

//  QVariant QGraphicsWidget::itemChange(GraphicsItemChange change, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QGraphicsWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(self->itemChange(change, *value));
}

//  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant(
    QGraphicsWidget *self,
    const QString *propertyName,
    const QVariant *value) {
  return new QVariant(self->propertyChange(*propertyName, *value));
}

//  bool QGraphicsWidget::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget10sceneEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  return self->sceneEvent(event);
}

//  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget16windowFrameEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *e) {
  return self->windowFrameEvent(e);
}

//  Qt::WindowFrameSection QGraphicsWidget::windowFrameSectionAt(const
//      QPointF &pos) const
extern "C" Q_DECL_EXPORT
Qt::WindowFrameSection ritual_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF(
    const QGraphicsWidget *self,
    const QPointF *pos) {
  return self->windowFrameSectionAt(*pos);
}

//  bool QGraphicsWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget5eventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  return self->event(event);
}

//  void QGraphicsWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11changeEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QGraphicsWidget::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10closeEventEP11QCloseEvent(
    QGraphicsWidget *self,
    QCloseEvent *event) {
  self->closeEvent(event);
}

//  void QGraphicsWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12focusInEventEP11QFocusEvent(
    QGraphicsWidget *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  bool QGraphicsWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget18focusNextPrevChildEb(
    QGraphicsWidget *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  void QGraphicsWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget13focusOutEventEP11QFocusEvent(
    QGraphicsWidget *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QGraphicsWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9hideEventEP10QHideEvent(
    QGraphicsWidget *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent(
    QGraphicsWidget *self,
    QGraphicsSceneMoveEvent *event) {
  self->moveEvent(event);
}

//  void QGraphicsWidget::polishEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11polishEventEv(QGraphicsWidget *self) {
  self->polishEvent();
}

//  void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent(
    QGraphicsWidget *self,
    QGraphicsSceneResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QGraphicsWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9showEventEP10QShowEvent(
    QGraphicsWidget *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidget *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QGraphicsWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidget *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QGraphicsWidget::grabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14grabMouseEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  self->grabMouseEvent(event);
}

//  void QGraphicsWidget::ungrabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  self->ungrabMouseEvent(event);
}

//  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  self->grabKeyboardEvent(event);
}

//  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  self->ungrabKeyboardEvent(event);
}

//  QGraphicsWidgetPrivate *QGraphicsWidget::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsWidgetPrivate *ritual_ZN15QGraphicsWidget6d_funcEv(
    QGraphicsWidget *self) {
  return self->d_func();
}

//  const QGraphicsWidgetPrivate *QGraphicsWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsWidgetPrivate *ritual_ZNK15QGraphicsWidget6d_funcEv(
    const QGraphicsWidget *self) {
  return self->d_func();
}

//  QGraphicsWidget as the QGraphicsLayoutItem it is built on
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_cast_QGraphicsWidget_QGraphicsLayoutItem(
    QGraphicsWidget *self) {
  return static_cast<QGraphicsLayoutItem *>(self);
}

//  a Python function taken by a CuteQGraphicsWidget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsWidget(
    QGraphicsWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsWidget *>(self)->take(key, call);
}

//  void QGraphicsWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget11setGeometryERK6QRectF(
    QGraphicsWidget *self,
    const QRectF *rect) {
  self->QGraphicsWidget::setGeometry(*rect);
}

//  int QGraphicsWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QGraphicsWidget4typeEv(const QGraphicsWidget *self) {
  return self->QGraphicsWidget::type();
}

//  void QGraphicsWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsWidget::paint(painter, option, widget);
}

//  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->QGraphicsWidget::paintWindowFrame(painter, option, widget);
}

//  QRectF QGraphicsWidget::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK15QGraphicsWidget12boundingRectEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->QGraphicsWidget::boundingRect());
}

//  QPainterPath QGraphicsWidget::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK15QGraphicsWidget5shapeEv(
    const QGraphicsWidget *self) {
  return new QPainterPath(self->QGraphicsWidget::shape());
}

//  void QGraphicsWidget::initStyleOption(QStyleOption *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK15QGraphicsWidget15initStyleOptionEP12QStyleOption(
    const QGraphicsWidget *self,
    QStyleOption *option) {
  static_cast<const OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::initStyleOption(
      option);
}

//  QSizeF QGraphicsWidget::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK15QGraphicsWidget8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsWidget *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      static_cast<const OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::sizeHint(
          which,
          *constraint));
}

//  void QGraphicsWidget::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget14updateGeometryEv(
    QGraphicsWidget *self) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::updateGeometry();
}

//  QVariant QGraphicsWidget::itemChange(GraphicsItemChange change, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN15QGraphicsWidget10itemChangeEN13QGraphicsItem18GraphicsItemChangeERK8QVariant(
    QGraphicsWidget *self,
    QGraphicsItem::GraphicsItemChange change,
    const QVariant *value) {
  return new QVariant(
      static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::itemChange(
          change,
          *value));
}

//  QVariant QGraphicsWidget::propertyChange(const QString &propertyName,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN15QGraphicsWidget14propertyChangeERK7QStringRK8QVariant(
    QGraphicsWidget *self,
    const QString *propertyName,
    const QVariant *value) {
  return new QVariant(
      static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::propertyChange(
          *propertyName,
          *value));
}

//  bool QGraphicsWidget::sceneEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGraphicsWidget10sceneEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::sceneEvent(
      event);
}

//  bool QGraphicsWidget::windowFrameEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGraphicsWidget16windowFrameEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *e) {
  return static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::windowFrameEvent(
      e);
}

//  Qt::WindowFrameSection QGraphicsWidget::windowFrameSectionAt(const
//      QPointF &pos) const
extern "C" Q_DECL_EXPORT
Qt::WindowFrameSection ritual_own_ZNK15QGraphicsWidget20windowFrameSectionAtERK7QPointF(
    const QGraphicsWidget *self,
    const QPointF *pos) {
  return static_cast<const OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::windowFrameSectionAt(
      *pos);
}

//  bool QGraphicsWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGraphicsWidget5eventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::event(
      event);
}

//  void QGraphicsWidget::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget11changeEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::changeEvent(
      event);
}

//  void QGraphicsWidget::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget10closeEventEP11QCloseEvent(
    QGraphicsWidget *self,
    QCloseEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::closeEvent(
      event);
}

//  void QGraphicsWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget12focusInEventEP11QFocusEvent(
    QGraphicsWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::focusInEvent(
      event);
}

//  bool QGraphicsWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGraphicsWidget18focusNextPrevChildEb(
    QGraphicsWidget *self,
    bool next) {
  return static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::focusNextPrevChild(
      next);
}

//  void QGraphicsWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget13focusOutEventEP11QFocusEvent(
    QGraphicsWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::focusOutEvent(
      event);
}

//  void QGraphicsWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget9hideEventEP10QHideEvent(
    QGraphicsWidget *self,
    QHideEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::hideEvent(
      event);
}

//  void QGraphicsWidget::moveEvent(QGraphicsSceneMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget9moveEventEP23QGraphicsSceneMoveEvent(
    QGraphicsWidget *self,
    QGraphicsSceneMoveEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::moveEvent(
      event);
}

//  void QGraphicsWidget::polishEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget11polishEventEv(QGraphicsWidget *self) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::polishEvent();
}

//  void QGraphicsWidget::resizeEvent(QGraphicsSceneResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget11resizeEventEP25QGraphicsSceneResizeEvent(
    QGraphicsWidget *self,
    QGraphicsSceneResizeEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::resizeEvent(
      event);
}

//  void QGraphicsWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget9showEventEP10QShowEvent(
    QGraphicsWidget *self,
    QShowEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::showEvent(
      event);
}

//  void QGraphicsWidget::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidget *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::hoverMoveEvent(
      event);
}

//  void QGraphicsWidget::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidget *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::hoverLeaveEvent(
      event);
}

//  void QGraphicsWidget::grabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget14grabMouseEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::grabMouseEvent(
      event);
}

//  void QGraphicsWidget::ungrabMouseEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget16ungrabMouseEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::ungrabMouseEvent(
      event);
}

//  void QGraphicsWidget::grabKeyboardEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget17grabKeyboardEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::grabKeyboardEvent(
      event);
}

//  void QGraphicsWidget::ungrabKeyboardEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsWidget19ungrabKeyboardEventEP6QEvent(
    QGraphicsWidget *self,
    QEvent *event) {
  static_cast<OwnQGraphicsWidget *>(self)->OwnQGraphicsWidget::ungrabKeyboardEvent(
      event);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
